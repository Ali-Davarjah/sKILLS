#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
از خروجی درون‌نگری دیتابیس، schema.json می‌سازد.

    python build_map.py <raw-dir> --schema Sales --out schema.json

<raw-dir> این فایل‌ها را می‌خواهد (فقط tables و columns اجباری‌اند):

    tables.json   [{"table":"X","rows":123}]
    columns.json  [{"table":"X","column":"ccY","type":"int","nullable":"NO","pos":1}]
                  یا شکل فشرده: [{"table":"X","cols":"ccY:int:NO|Name:nvarchar:YES"}]
    fks.json      [{"parent":"A","parent_col":"ccB","ref":"B","ref_col":"ccB"}]
    pks.json      [{"table":"X","column":"ccX"}]
    dates.json    [{"table":"X","column":"Tarikh","max_value":"2026-08-30"}]

کلید خارجیِ واقعی اگر باشد، بر حدسِ هم‌نامی مقدم است و در خروجی
proven=true می‌گیرد. اگر نباشد، همه‌چیز حدس است و صادقانه علامت می‌خورد.

خروجی دوم `findings.md` است: هرچه ماشین نمی‌تواند تصمیم بگیرد.
"""

import argparse
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

for _s in ("stdout", "stderr"):
    _st = getattr(sys, _s, None)
    if _st is not None and hasattr(_st, "reconfigure"):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass

# ---------------------------------------------------------------- الگوهای نام

LEGACY_RE = re.compile(
    r"(_o+ld$|_o+ld_|^tmp_|^Tmp_|_Backup$|Backup$|DeletedFile"
    r"|^DELETED_|_Deeel$|_deeel$|_InJob$|ByJob$|_Voc$|_SabtNashodeh$"
    r"|_History$|History$|_TakmilyHistory$|_EbtalHistory$)", re.I)
DEAD_COL_RE = re.compile(r"_dee+l$", re.I)
SUSPECT_COL_RE = re.compile(r"_old$", re.I)
MIGRATION_RE = re.compile(r"^EnteghalAvalieh_")
CONFIG_RE = re.compile(r"^Config_")
DETAIL_RE = re.compile(r"Satr$|_Satr$")
STATUS_DICT_RE = re.compile(r"_?Code ?Vaz[ei]+at$", re.I)
STATUS_HIST_RE = re.compile(r"_?Vaz[ei]+at$", re.I)
REASON_RE = re.compile(r"Elat ?Odat", re.I)
ATTACH_RE = re.compile(r"_(Madarek|Madrak|Photo)$", re.I)
DICT_PREFIX_RE = re.compile(r"^(Noe|Elat|Vahed|Goroh|Rasteh|Maghta)")
RULE_RE = re.compile(r"^(AeenNameh?|Saghfe?|Tarefe|Zarib)")
# ویوها: vXxx یا V_Xxx . ۲۵٪ اشیای این دیتابیس‌اند و از فهرست ستون‌ها
# جدانشدنی‌اند مگر با همین قاعده یا با sys.tables.
VIEW_RE = re.compile(r"^(v[A-Z_]|V_|vtmp|vrpt)")
# «آرشیو» در این دیتابیس دو معنی دارد: گاهی جدولِ مرده، و گاهی خودِ
# جدولِ اصلیِ واقعیت (Sales.AmarForosh_Arshive مرکزِ کلِ گزارش‌های فروش است).
# پس میراث علامتش نمی‌زنیم — فقط «بررسی کن» می‌گذاریم و تعداد سطر تصمیم می‌گیرد.
ARCHIVE_RE = re.compile(r"(_Arshive?$|_Archive$|Arshiv$)", re.I)
# جدولِ سال‌دار: عکسِ یک سال یا یک تاریخ. AmalkardRozanehPakhsh96،
# JayezehForosh_ArshiveReport98، Kala_14020830، Taghirgheymat1402.
YEAR_RE = re.compile(r"(?:[^0-9](9[0-9]|1[34][0-9]{2}|20[0-2][0-9])$"
                     r"|_1[34][0-9]{6}$|_[0-9]{8}$)")

# پسوندهای نقشی که روی نام یک ارجاع می‌نشینند بدون عوض‌کردن مقصد
ROLE_SUFFIXES = ("_Link", "_Old", "_OLD", "_Jadid", "_Asli", "_Movaghat",
                 "_SabtKonandeh", "_Zamen", "_Bimar", "_Mabda", "_Maghsad",
                 "_RoozTatil", "_Next", "_Hoghogh", "_Bimeh", "_Maliat",
                 "_Eydi", "_Parent", "_Sabegh")

KEY_SUFFIXES = ("Code", "Codes")

START_COLS = ("FromDate", "BeginDate", "DateBegin", "AzTarikh", "StartDate")
END_COLS = ("EndDate", "DateEnd", "TaTarikh", "SarTarikh")
STATUS_COLS = ("CodeVazeiat", "CodeVaziat", "CodeVazieat", "Codevazieat")
LEDGER_COLS = ("BedBes", "BedBess")

EVIDENCE_OF = {"exact": "EXACT_CC_ID_MATCH", "exact_id": "EXACT_CC_ID_MATCH",
               "altkey": "SAME_NAME_ID_PATTERN",
               "case": "SAME_NAME_ID_PATTERN", "case_id": "SAME_NAME_ID_PATTERN",
               "suffix": "NAMING_ONLY", "tail_id": "NAMING_ONLY"}
CONFIDENCE_OF = {"exact": "HIGH", "exact_id": "HIGH", "case": "MEDIUM",
                 "altkey": "MEDIUM",
                 "case_id": "MEDIUM", "suffix": "LOW", "tail_id": "LOW"}

SEP_TAB = chr(9)
SPLIT_RE = re.compile(chr(9) + "+|  +")

INT_TYPES = {"tinyint": 1, "smallint": 2, "int": 4, "bigint": 8}

# ستون‌های ممیزی لایه‌ی جدید — شناسه‌ی کاربرند، نه ارجاع به این اسکیما
AUDIT_COLS = {"createdbyuserid", "modifiedbyuserid", "createddatetime",
              "modifieddatetime", "accuredbyuserid", "businessid"}
# شناسه‌های زیرساختِ صف رویداد — ارجاع کسب‌وکاری نیستند
INFRA_ID_COLS = {"eventid", "messageid", "traceid", "spanid", "aggregateid",
                 "outboxeventitemid", "id"}


# ---------------------------------------------------------------- ورودی

def read_json(path, required=False):
    if not os.path.exists(path):
        if required:
            sys.exit("فایل لازم نیست: %s" % path)
        return []
    with io.open(path, encoding="utf-8-sig") as fh:
        txt = fh.read().strip()
    if not txt:
        return []
    data = json.loads(txt)
    if isinstance(data, dict):
        for key in ("rows", "data", "result", "recordset"):
            if key in data and isinstance(data[key], list):
                return data[key]
        return [data]
    return data


def pick(row, *names):
    """اولین کلیدِ موجود را برمی‌گرداند — نام ستون‌ها بین ابزارها فرق می‌کند."""
    low = {str(k).lower(): v for k, v in row.items()}
    for n in names:
        if n.lower() in low:
            return low[n.lower()]
    return None


def load_inventory_tsv(path, schema=None):
    """فهرست کاملِ ستون‌های دیتابیس در قالبِ خروجیِ SSMS (جدا شده با tab):

        db | schema | table | column | pos | type | maxlen | precision
           | scale | nullable

    برمی‌گرداند (cols_by_table برای اسکیمای خواسته‌شده، catalog کلِ دیتابیس،
    نام دیتابیس). catalog برای حلِ ارجاع‌های بین‌اسکیمایی لازم است.
    """
    cols_by_table = defaultdict(list)
    catalog = defaultdict(lambda: defaultdict(set))
    dbname = None
    with io.open(path, encoding="utf-8-sig") as fh:
        for raw in fh:
            line = raw.rstrip()
            if not line.strip():
                continue
            f = line.split(SEP_TAB)
            if len(f) < 10:
                f = [x for x in re.split(SPLIT_RE, line) if x != ""]
            if len(f) < 10:
                continue
            db, sch, tbl, col, pos, typ, maxlen, prec, scale, nul = f[:10]
            if db.lower() in ("database", "db", "table_catalog"):
                continue
            dbname = dbname or db
            catalog[sch][tbl].add(col)
            if schema and sch != schema:
                continue
            try:
                pos_i = int(pos)
            except ValueError:
                pos_i = 0
            cols_by_table[tbl].append(
                (col, typ.strip().lower(), nul.strip().upper(), pos_i))
    for t in cols_by_table:
        cols_by_table[t].sort(key=lambda c: c[3])
    return (cols_by_table,
            {k: {t: sorted(c) for t, c in v.items()}
             for k, v in catalog.items()}, dbname)


def load_columns(raw_dir):
    """{table: [(col, type, nullable, pos)]}"""
    rows = read_json(os.path.join(raw_dir, "columns.json"), required=True)
    out = defaultdict(list)
    for r in rows:
        tbl = pick(r, "table", "TABLE_NAME", "table_name")
        if not tbl:
            continue
        compact = pick(r, "cols", "columns")
        if compact:
            for i, part in enumerate(str(compact).split("|"), 1):
                bits = part.split(":")
                col = bits[0].strip()
                typ = bits[1].strip().lower() if len(bits) > 1 else ""
                nul = bits[2].strip().upper() if len(bits) > 2 else "YES"
                if col:
                    out[tbl].append((col, typ, nul, i))
        else:
            col = pick(r, "column", "COLUMN_NAME", "column_name")
            if not col:
                continue
            typ = (pick(r, "type", "DATA_TYPE", "data_type") or "").lower()
            nul = (pick(r, "nullable", "IS_NULLABLE", "is_nullable") or "YES").upper()
            pos = pick(r, "pos", "ORDINAL_POSITION", "ordinal_position") or 0
            out[tbl].append((col, typ, nul, int(pos or 0)))
    for t in out:
        out[t].sort(key=lambda c: c[3])
    return out


# ---------------------------------------------------------------- دوقلوها

def norm_tight(name):
    """i↔y و u↔o و حذف زیرخط — دقتِ بالا."""
    s = name.lower().replace("_", "")
    s = s.replace("y", "i").replace("u", "o")
    return s


def norm_loose(name):
    """حذف واکه‌ها و h — یادآوریِ بالا، خطای مثبت بیشتر."""
    s = norm_tight(name)
    return re.sub(r"[aeioh]", "", s)


def twin_base(name):
    """پسوندهایی که نسخه‌ی جایگزین می‌سازند را برمی‌دارد."""
    base = name
    # PPC = نسخه‌ی دستگاه همراه. جهانِ موازیِ همان جدول است، پس دوقلو
    # حساب می‌شود: DariaftPardakht / DariaftPardakhtPPC.
    for suf in ("_Deeel", "_deeel", "_New", "New", "_Old", "_old",
                "PPC", "_PPC", "PPc", "_Tablet", "Tablet"):
        if base.endswith(suf) and len(base) > len(suf) + 3:
            base = base[: -len(suf)]
            break
    return base


def find_twins(tables):
    groups_t, groups_l = defaultdict(list), defaultdict(list)
    for t in tables:
        base = twin_base(t)
        groups_t[norm_tight(base)].append(t)
        groups_l[norm_loose(base)].append(t)

    twins, seen = [], set()
    for key, members in sorted(groups_t.items()):
        if len(members) > 1:
            twins.append({"pair": sorted(members), "confidence": "high"})
            seen.add(tuple(sorted(members)))
    for key, members in sorted(groups_l.items()):
        if len(members) > 1 and tuple(sorted(members)) not in seen:
            # زیرمجموعه‌ی یک گروهِ دقیق‌تر را دوباره گزارش نکن
            twins.append({"pair": sorted(members), "confidence": "low"})
    return twins


# ---------------------------------------------------------------- یال‌ها

def resolve(cc, tables):
    """ccX → X . قرارداد قدیمیِ کلِ دیتابیس."""
    if not cc.startswith("cc") or len(cc) < 4:
        return None, None
    base = cc[2:]
    if base in tables:
        return base, "exact"
    for suf in ROLE_SUFFIXES:
        if base.endswith(suf):
            trimmed = base[: -len(suf)]
            if trimmed in tables:
                return trimmed, "suffix"
    # کلیدِ دوم: جدول می‌تواند دو شناسه داشته باشد و اقمارش روی دومی
    # کلید بخورند. Warehouse.Kala هم ccKala دارد و هم ccKalaCode، و ۲۵
    # جدولِ اقماری روی ccKalaCode می‌نشینند.
    for suf in KEY_SUFFIXES:
        if base.endswith(suf) and len(base) > len(suf) + 2:
            trimmed = base[: -len(suf)]
            if trimmed in tables:
                return trimmed, "altkey"
    low = {t.lower(): t for t in tables}
    if base.lower() in low:
        return low[base.lower()], "case"
    return None, None


def resolve_id(col, tables):
    """XId → X / Xs — قرارداد لایه‌ی جدید (EF Core).

    این لایه کنارِ لایه‌ی cc زندگی می‌کند و جدول‌هایش جمعِ انگلیسی می‌گیرند:
    SherkatProjectEtmam.SherkatProjectId → SherkatProjects
    """
    if col.startswith("cc") or not col.endswith("Id") or len(col) <= 4:
        return None, None
    if col.lower() in AUDIT_COLS or col.lower() in INFRA_ID_COLS:
        return None, None
    base = col[:-2]
    for cand in (base, base + "s", base + "es"):
        if cand in tables:
            return cand, "exact_id"
    low = {t.lower(): t for t in tables}
    for cand in (base, base + "s", base + "es"):
        if cand.lower() in low:
            return low[cand.lower()], "case_id"
    # ارجاع کوتاه‌شده: GharardadId → PeymankarGharardads
    tail = [t for t in tables
            if t.endswith(base) or t.endswith(base + "s")]
    if len(tail) == 1:
        return tail[0], "tail_id"
    return None, None


def resolve_any(col, tables):
    t, how = resolve(col, tables)
    if t:
        return t, how
    return resolve_id(col, tables)


def build_edges(tables, cols_by_table, fks):
    """یال‌های حدسی + کلیدهای خارجی واقعی، با علامتِ منشأ."""
    edges = {}
    tableset = set(tables)
    for tbl, cols in cols_by_table.items():
        if tbl not in tableset:
            continue          # ویو مبدأِ یال نیست
        for col, typ, nul, pos in cols:
            if col.lower() in AUDIT_COLS:
                continue
            if not col.startswith("cc") and not col.endswith("Id"):
                continue
            target, how = resolve_any(col, tables)
            if target and target != tbl:
                edges[(tbl, col, target)] = {
                    "source": tbl, "col": col, "target": target,
                    "match": how, "proven": False,
                    "evidence": EVIDENCE_OF.get(how, "NAMING_ONLY"),
                    "confidence": CONFIDENCE_OF.get(how, "LOW"),
                }

    fk_only, contradictions = [], []
    for fk in fks:
        p = pick(fk, "parent", "ParentTable", "parent_table")
        pc = pick(fk, "parent_col", "ParentColumn", "parent_column")
        r = pick(fk, "ref", "RefTable", "ref_table", "ReferencedTable")
        rc = pick(fk, "ref_col", "RefColumn", "ref_column", "ReferencedColumn")
        if not (p and pc and r):
            continue
        key = (p, pc, r)
        if key in edges:
            edges[key]["proven"] = True
            edges[key]["ref_col"] = rc
            edges[key]["evidence"] = "DECLARED_FK"
            edges[key]["confidence"] = "CONFIRMED"
        else:
            edges[key] = {"source": p, "col": pc, "target": r, "ref_col": rc,
                          "match": "fk", "proven": True,
                          "evidence": "DECLARED_FK", "confidence": "CONFIRMED"}
            guess, _ = resolve(pc, tables)
            if guess and guess != r:
                contradictions.append(
                    {"col": "%s.%s" % (p, pc), "naming_says": guess, "fk_says": r})
            else:
                fk_only.append("%s.%s → %s" % (p, pc, r))
    return list(edges.values()), fk_only, contradictions


# ---------------------------------------------------------------- طبقه‌بندی

def classify(tbl, cols, incoming, rows, has_fks):
    """rows=None یعنی نمی‌دانیم (فهرست بدونِ تعداد سطر)، نه اینکه خالی است."""
    names = [c[0] for c in cols]
    nset = {n.lower() for n in names}
    flags = []

    def has(*cands):
        return any(c.lower() in nset for c in cands)

    if LEGACY_RE.search(tbl):
        flags.append("legacy")
    elif YEAR_RE.search(tbl):
        flags.append("year_snapshot")
    elif ARCHIVE_RE.search(tbl):
        flags.append("archive_check")
    if MIGRATION_RE.match(tbl):
        flags.append("migration")
    if CONFIG_RE.match(tbl):
        flags.append("config")
    if DETAIL_RE.search(tbl):
        flags.append("detail")
    if ATTACH_RE.search(tbl):
        flags.append("attachment")
    if STATUS_DICT_RE.search(tbl):
        flags.append("status_dict")
    elif STATUS_HIST_RE.search(tbl) and has("Tarikh", "ZamanSabt", "TarikhSabt",
                                            "TarikhVazeiat"):
        flags.append("status_history")
    if REASON_RE.search(tbl):
        flags.append("reason_dict")
    if RULE_RE.match(tbl):
        flags.append("rule")
    if has(*START_COLS) and has(*END_COLS):
        flags.append("effective_dated")
    if has(*STATUS_COLS) and "status_dict" not in flags:
        flags.append("status_header")
    if has(*LEDGER_COLS):
        flags.append("ledger")
    if has("ZamanGheirFaali", "ZamanGherFaali"):
        flags.append("deactivatable")
    if has("CodeMely", "ShomarehHesab", "ShomarehSheba", "Photo"):
        flags.append("sensitive")
    if "cc%sLink" % tbl in names or ("cc%s_Link" % tbl) in names:
        flags.append("tree")
    if DICT_PREFIX_RE.match(tbl) and len(cols) <= 8:
        flags.append("dict")
    if len(cols) <= 4 and any(n.lower().startswith("name") for n in names):
        if "dict" not in flags:
            flags.append("dict")
    if incoming >= 40:
        flags.append("anchor")
    elif incoming >= 10:
        flags.append("hub_target")
    if rows == 0:
        flags.append("empty")
    elif rows is None:
        flags.append("rows_unknown")

    # ستون شروع غیرمتعارف
    start = next((c for c in START_COLS if c.lower() in nset), None)
    if start and start != "FromDate" and "effective_dated" in flags:
        flags.append("nonstandard_start:%s" % start)
    # پایانِ باز با NOT NULL
    for c, typ, nul, pos in cols:
        if c in END_COLS and nul == "NO":
            flags.append("end_date_not_null")
            break
    return flags


def stability_of(flags, incoming):
    """نقشه از یک نسخه‌ی پشتیبان است. کدام بخشش ثابت می‌ماند؟

    معیار، تعدادِ ارجاعِ ورودی است: جدولی که ۵۰ چیز به آن اشاره می‌کند
    بدونِ شکستنِ نصفِ سیستم حذف نمی‌شود. جدولی که هیچ‌کس به آن اشاره
    نمی‌کند، می‌تواند فردا نباشد.
    """
    if any(f in flags for f in ("legacy", "migration", "archive_check",
                                "year_snapshot")):
        return "volatile"
    if incoming >= 5 or "anchor" in flags or "hub_target" in flags:
        return "core"
    if incoming >= 1 or "dict" in flags:
        return "connected"
    return "leaf"


def guess_pk(tbl, cols, declared_pk):
    if declared_pk:
        return declared_pk
    names = [c[0] for c in cols]
    if ("cc" + tbl) in names:
        return "cc" + tbl
    for c, typ, nul, pos in cols:
        if c.startswith("cc") and nul == "NO" and pos == 1:
            return c
    for cand in ("Id", "ID", tbl + "Id"):
        if cand in names:
            return cand
    return None


# ---------------------------------------------------------------- دامنه‌ها

def suggest_domains(tables):
    """با نشانه‌ی اولِ CamelCase خوشه می‌سازد. نام‌گذاری کارِ آدم است."""
    def head(t):
        m = re.match(r"^[A-Z][a-z]+", t)
        return m.group(0) if m else t[:6]
    buckets = defaultdict(list)
    for t in tables:
        buckets[head(t)].append(t)
    big = {k: v for k, v in buckets.items() if len(v) >= 3}
    return dict(sorted(big.items(), key=lambda kv: -len(kv[1])))


def _domain_labels(domains_cfg, assign):
    """برچسب دامنه‌ها؛ اگر جدولی بی‌دامنه مانده، other هم باید دیده شود."""
    if not domains_cfg:
        return {"other": "دسته‌بندی‌نشده"}
    labels = {k: v.get("label", k) for k, v in domains_cfg.items()}
    if any(d == "other" for d in assign.values()):
        labels["other"] = "دسته‌بندی‌نشده — دستی ببین"
    return labels


def apply_domains(tables, domains_cfg):
    assign = {}
    if domains_cfg:
        for key, meta in domains_cfg.items():
            for pat in meta.get("match", []):
                rx = re.compile(pat)
                for t in tables:
                    if t not in assign and rx.search(t):
                        assign[t] = key
    for t in tables:
        assign.setdefault(t, "other")
    return assign


# ---------------------------------------------------------------- تله‌ها

def detect_type_traps(edges, cols_by_table, pk_by_table):
    types = {}
    for tbl, cols in cols_by_table.items():
        for c, typ, nul, pos in cols:
            types[(tbl, c)] = typ

    type_mismatch, width_mismatch = [], []
    for e in edges:
        src, col, tgt = e["source"], e["col"], e["target"]
        child = types.get((src, col))
        parent_col = e.get("ref_col") or pk_by_table.get(tgt) or col
        parent = types.get((tgt, parent_col))
        if not child or not parent or child == parent:
            continue
        if child in INT_TYPES and parent in INT_TYPES:
            if INT_TYPES[child] != INT_TYPES[parent]:
                width_mismatch.append({
                    "child": "%s.%s" % (src, col), "child_type": child,
                    "parent": "%s.%s" % (tgt, parent_col), "parent_type": parent,
                    "note": ("سقف %d — مقادیر بزرگ‌تر ذخیره نمی‌شوند"
                             % (2 ** (8 * INT_TYPES[child] - 1) - 1))
                    if INT_TYPES[child] < INT_TYPES[parent] else ""})
        else:
            type_mismatch.append({
                "col": "%s.%s" % (src, col), "declared": child,
                "target": "%s.%s %s" % (tgt, parent_col, parent)})
    return type_mismatch, width_mismatch


def detect_misleading_detail(tables, cols_by_table, edges, incoming):
    """XSatr که ستون ccX ندارد و در واقع زیرِ چیز دیگری است."""
    out = []
    by_source = defaultdict(list)
    for e in edges:
        by_source[e["source"]].append(e)
    # نگاشتِ نرمال‌شده، تا ساقه‌ای مثل DarkhastHazineDarman هم
    # DarkhastHazinehDarman را پیدا کند (یک h فرق)
    by_norm = defaultdict(list)
    for t in tables:
        by_norm[norm_loose(t)].append(t)

    for t in tables:
        if not DETAIL_RE.search(t):
            continue
        stem = re.sub(r"_?Satr$", "", t)
        if not stem or stem == t:
            continue
        names = {c[0] for c in cols_by_table.get(t, [])}
        if ("cc" + stem) in names:
            continue
        # ساقه ممکن است دقیقاً جدول نباشد؛ نزدیک‌ترین را بگیر
        expected = stem if stem in tables else None
        if expected is None:
            cand = [x for x in by_norm.get(norm_loose(stem), []) if x != t]
            expected = cand[0] if len(cand) == 1 else None
        if expected is None:
            continue
        if ("cc" + expected) in names:
            continue
        def is_lookup(x):
            return bool(REASON_RE.search(x) or STATUS_DICT_RE.search(x)
                        or ATTACH_RE.search(x) or DICT_PREFIX_RE.match(x))

        parents = {e["target"] for e in by_source.get(t, [])
                   if e["target"] != t and not LEGACY_RE.search(e["target"])
                   and not is_lookup(e["target"])}
        if parents:
            # کم‌عمومی‌ترین نامزد محتمل‌ترین پدر است: لنگرگاهی مثل Personel
            # به همه‌چیز وصل است و پدر بودنش چیزی نمی‌گوید.
            ranked = sorted(parents, key=lambda p: (incoming.get(p, 0), p))
            out.append({"table": t, "expected_parent": expected,
                        "actual_parent": ranked[0],
                        "all_candidates": ranked,
                        "stem_exact": stem in tables})
    return out


def detect_dead_columns(cols_by_table):
    dead, suspect = {}, {}
    for tbl, cols in cols_by_table.items():
        d = [c for c, _, _, _ in cols if DEAD_COL_RE.search(c)]
        s = [c for c, _, _, _ in cols if SUSPECT_COL_RE.search(c)
             and not DEAD_COL_RE.search(c)]
        if d:
            dead[tbl] = d
        if s:
            suspect[tbl] = s
    return dead, suspect


# ---------------------------------------------------------------- ساخت

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("raw_dir", nargs="?")
    ap.add_argument("--inventory", help="فهرست کاملِ TSV دیتابیس")
    ap.add_argument("--schema", required=True)
    ap.add_argument("--out", default="schema.json")
    ap.add_argument("--domains", help="فایل نگاشت دامنه (اختیاری)")
    ap.add_argument("--findings", default="findings.md")
    ap.add_argument("--snapshot", default="",
                    help="تاریخ/برچسبِ نسخه‌ای که نقشه از آن ساخته شده")
    args = ap.parse_args(argv)

    catalog, dbname = {}, None
    if args.inventory:
        cols_by_table, catalog, dbname = load_inventory_tsv(args.inventory,
                                                            args.schema)
        tbl_rows = read_json(os.path.join(args.raw_dir or ".", "tables.json"))
        fks = read_json(os.path.join(args.raw_dir or ".", "fks.json"))
        pks = read_json(os.path.join(args.raw_dir or ".", "pks.json"))
        dates = read_json(os.path.join(args.raw_dir or ".", "dates.json"))
    else:
        if not args.raw_dir:
            sys.exit("یا <raw-dir> بده یا --inventory")
        tbl_rows = read_json(os.path.join(args.raw_dir, "tables.json"),
                             required=True)
        cols_by_table = load_columns(args.raw_dir)
        fks = read_json(os.path.join(args.raw_dir, "fks.json"))
        pks = read_json(os.path.join(args.raw_dir, "pks.json"))
        dates = read_json(os.path.join(args.raw_dir, "dates.json"))

    rows_by_table = {}
    for r in tbl_rows:
        t = pick(r, "table", "TABLE_NAME", "table_name", "name")
        if t:
            rows_by_table[t] = pick(r, "rows", "row_count", "rowcount")

    # ویوها را از هسته بیرون بگذار. اگر tables.json از sys.tables آمده، آن
    # مرجع است؛ وگرنه از روی نام تشخیص بده.
    all_objects = sorted(set(rows_by_table) | set(cols_by_table))
    if rows_by_table:
        views = sorted(t for t in cols_by_table if t not in rows_by_table)
    else:
        views = sorted(t for t in all_objects if VIEW_RE.match(t))
    viewset = set(views)
    tables = [t for t in all_objects if t not in viewset]
    if not tables:
        sys.exit("هیچ جدولی در ورودی نبود.")

    pk_by_table = {}
    for r in pks:
        t = pick(r, "table", "TABLE_NAME")
        c = pick(r, "column", "COLUMN_NAME")
        if t and c and t not in pk_by_table:
            pk_by_table[t] = c

    edges, fk_only, contradictions = build_edges(tables, cols_by_table, fks)
    incoming = Counter(e["target"] for e in edges)

    for t in tables:
        pk_by_table[t] = guess_pk(t, cols_by_table.get(t, []), pk_by_table.get(t))

    domains_cfg = None
    if args.domains and os.path.exists(args.domains):
        with io.open(args.domains, encoding="utf-8") as fh:
            domains_cfg = json.load(fh)
    assign = apply_domains(tables, domains_cfg)

    dead, suspect = detect_dead_columns(cols_by_table)
    type_mm, width_mm = detect_type_traps(edges, cols_by_table, pk_by_table)
    misleading = detect_misleading_detail(tables, cols_by_table, edges, incoming)
    twins = find_twins(tables)

    max_date = {}
    for r in dates:
        t = pick(r, "table", "TABLE_NAME")
        if t:
            max_date[t] = {"column": pick(r, "column", "COLUMN_NAME"),
                           "max": str(pick(r, "max_value", "max", "akharin"))}

    out_tables = {}
    for t in tables:
        cols = cols_by_table.get(t, [])
        flags = classify(t, cols, incoming.get(t, 0), rows_by_table.get(t),
                         bool(fks))
        cc = [c for c, _, _, _ in cols if c.startswith("cc")]
        entry = {
            "domain": assign[t],
            "pk": pk_by_table.get(t),
            "role": "",                       # ← آدم پر می‌کند
            "rows": rows_by_table.get(t),
            "flags": flags,
            "stability": stability_of(flags, incoming.get(t, 0)),
        }
        if cc:
            entry["cc"] = cc
        if dead.get(t):
            entry["dead_cols"] = dead[t]
        if max_date.get(t):
            entry["max_date"] = max_date[t]
        out_tables[t] = entry

    external = Counter()
    cross_target = {}
    other = {s2: ts for s2, ts in catalog.items() if s2 != args.schema}
    for t in tables:
        for c, _, _, _ in cols_by_table.get(t, []):
            if not c.startswith("cc") or resolve(c, tables)[0]:
                continue
            external[c] += 1
            base = c[2:]
            cands = [base]
            for suf in ROLE_SUFFIXES + KEY_SUFFIXES:
                if base.endswith(suf) and len(base) > len(suf) + 2:
                    cands.append(base[: -len(suf)])
            for cand in cands:
                hits = sorted(s2 for s2, ts in other.items() if cand in ts)
                if not hits:
                    continue
                # چند اسکیما جدولِ هم‌نام دارند؛ آنکه **همین ستون را دارد**
                # مقصد است. Sales.ccKalaCode به Warehouse.Kala می‌رود نه
                # Amargar.Kala، چون فقط اولی ستون ccKalaCode را دارد.
                best = [s2 for s2 in hits if c in other[s2].get(cand, ())]
                cross_target[c] = "%s.%s" % ((best or hits)[0], cand)
                break

    schema = {
        "meta": {
            "version": "0.1-generated",
            "database": dbname or "",
            "schema": args.schema,
            "source": "درون‌نگری زنده‌ی دیتابیس",
            "verified_against_live_db": False,
            "snapshot": args.snapshot or "نامشخص",
            "snapshot_note": ("نقشه قابل اعتماد است و از آن استفاده کن. "
                              "فقط بدان عکسِ یک لحظه است: فهرست اسکیماها و "
                              "اشیای هسته ثابت‌اند، و در حاشیه ممکن است چند "
                              "جدول اضافه یا کم شده باشد. اگر جدولی که "
                              "مطمئنی هست در نقشه نبود، `map.py drift` "
                              "بزن — نه اینکه بگویی وجود ندارد."),
            "foreign_keys_declared": len(fks),
            "join_rule": "اگر A.ccB هست و جدول B هم هست → حدسِ اول A.ccB = B.ccB.",
            "warning": ("یال‌های proven=false از هم‌نامی حدس زده شده‌اند و کلید "
                        "خارجی ندارند." if len(fks) == 0 else
                        "یال‌های proven=true کلید خارجی واقعی دارند؛ بقیه حدس‌اند."),
        },
        "domains": _domain_labels(domains_cfg, assign),
        "external_cc": {
            cc: ({"count": n, "resolves_to": cross_target[cc],
                  "evidence": "CROSS_SCHEMA_CC_MATCH", "note": ""}
                 if cc in cross_target else {"count": n, "note": ""})
            for cc, n in external.most_common()},
        "tables": out_tables,
        "traps": {
            "twins": twins,
            "type_mismatch": type_mm,
            "width_mismatch": width_mm,
            "misleading_satr": misleading,
            "dead_columns": {
                "rule_dead": "پسوند _deeeel / _deeel — استفاده نکن",
                "rule_suspect": "پسوند _Old — اول ببین؛ گاهی یعنی «قبلی»",
                "by_table": dead,
                "suspect_by_table": suspect,
            },
            "begin_date_tables": sorted(
                t for t in tables
                if any(f.startswith("nonstandard_start:")
                       for f in out_tables[t]["flags"])),
            "end_date_not_null": sorted(
                t for t in tables if "end_date_not_null" in out_tables[t]["flags"]),
            "fk_contradicts_naming": contradictions,
        },
        "cross_schema": {
            v: {"via": k, "evidence": "CROSS_SCHEMA_CC_MATCH", "verified": True,
                "note": "مقصد در فهرست اشیای دیتابیس پیدا شد"}
            for k, v in sorted(cross_target.items(), key=lambda kv: kv[1])},
        "views_excluded": views,
        "edges": sorted(edges, key=lambda e: (e["source"], e["col"])),
    }

    with io.open(args.out, "w", encoding="utf-8") as fh:
        json.dump(schema, fh, ensure_ascii=False, indent=2, sort_keys=False)

    write_findings(args, schema, tables, edges, incoming, contradictions,
                   fk_only, twins, misleading)

    print("schema.json → %s" % args.out)
    print("  جدول: %d    یال: %d (اثبات‌شده: %d)"
          % (len(tables), len(edges), sum(1 for e in edges if e["proven"])))
    print("  ویوِ کنارگذاشته‌شده: %d    ارجاع بین‌اسکیمایی: %d"
          % (len(views), len(cross_target)))
    print("  دوقلوی مشکوک: %d    ناسازگاری نوع: %d    عرض: %d"
          % (len(twins), len(type_mm), len(width_mm)))
    print("findings → %s   ← این را بخوان، تصمیم‌های آدمی آنجاست" % args.findings)
    return 0


def write_findings(args, schema, tables, edges, incoming, contradictions,
                   fk_only, twins, misleading):
    L = []
    add = L.append
    add("# یافته‌های ساخت نقشه — اسکیمای `%s`\n" % args.schema)
    add("این فایل چیزهایی است که **ماشین نمی‌تواند تصمیم بگیرد**. تا وقتی اینها")
    add("حل نشده‌اند، `schema.json` ناقص است و اسکیل ساخته‌شده روی حدس می‌ایستد.\n")

    nfk = schema["meta"]["foreign_keys_declared"]
    add("## وضعیت اثبات\n")
    add("- جدول: **%d**" % len(tables))
    add("- یال حدسی (هم‌نامی): **%d**" % sum(1 for e in edges if not e["proven"]))
    add("- یال با کلید خارجی واقعی: **%d**" % sum(1 for e in edges if e["proven"]))
    add("- کلید خارجی اعلام‌شده در دیتابیس: **%d**\n" % nfk)
    if nfk == 0:
        add("> **این اسکیما کلید خارجی ندارد.** یعنی هر اتصال حدس است و اسکیل")
        add("> باید همین را صریح بگوید. مثل اسکیمای HumanResource.\n")
    else:
        add("> کلید خارجی هست — یال‌های `proven=true` قطعی‌اند و بقیه حدس.\n")

    if contradictions:
        add("## ⚠ کلید خارجی با قاعده‌ی نام‌گذاری نمی‌خواند\n")
        add("**مهم‌ترین بخش این فایل.** اینجا قرارداد نام‌گذاری می‌شکند:\n")
        add("| ستون | نام می‌گوید | کلید خارجی می‌گوید |")
        add("|---|---|---|")
        for c in contradictions:
            add("| `%s` | %s | **%s** |" % (c["col"], c["naming_says"], c["fk_says"]))
        add("")

    add("## دامنه‌ها — نام‌گذاری با توست\n")
    if schema["domains"] == {"other": "دسته‌بندی‌نشده"}:
        add("هیچ نگاشت دامنه‌ای داده نشد، پس همه‌ی جدول‌ها `other` شدند.")
        add("خوشه‌های پیشنهادی بر پایه‌ی نشانه‌ی اول نام:\n")
        for head, members in list(suggest_domains(tables).items())[:20]:
            add("- `%s*` → %d جدول  (%s%s)"
                % (head, len(members), "، ".join(sorted(members)[:4]),
                   " ..." if len(members) > 4 else ""))
        add("\nیک `domains.json` بساز و دوباره اجرا کن:\n")
        add("```json")
        add('{ "hoghogh": {"label": "حقوق و دستمزد", "match": ["^Pardakht", "Hoghogh"]} }')
        add("```\n")
    else:
        add("نگاشت داده شد. توزیع:\n")
        cnt = Counter(v["domain"] for v in schema["tables"].values())
        for k, label in schema["domains"].items():
            add("- `%s` %s — %d جدول" % (k, label, cnt.get(k, 0)))
        if cnt.get("other"):
            add("- `other` **%d جدول بی‌دامنه — اینها را دستی ببین**" % cnt["other"])
        add("")

    add("## نقشِ جدول‌ها خالی است\n")
    add("`role` هر جدول در `schema.json` خالی گذاشته شده. **این را ماشین حدس")
    add("نمی‌زند** — یک جمله برای هر جدولِ مهم بنویس. از پرتکرارترین‌ها شروع کن:\n")
    for t, n in incoming.most_common(15):
        add("- `%s` — %d ارجاع ورودی" % (t, n))
    add("")

    if twins:
        add("## جدول‌های دوقلو — کدام زنده است؟\n")
        add("اشتباه گرفتنشان خطا نمی‌دهد، **جدولِ خالی می‌دهد**. تعداد سطر را")
        add("کنار هم بگذار و اگر باز هم معلوم نشد، از کارشناس بپرس.\n")
        add("| نامزدها | اطمینان | سطرها |")
        add("|---|---|---|")
        for tw in twins[:40]:
            counts = "، ".join("%s=%s" % (m, schema["tables"].get(m, {}).get("rows", "?"))
                               for m in tw["pair"])
            add("| %s | %s | %s |" % ("  ⟷  ".join(tw["pair"]), tw["confidence"], counts))
        add("")

    if misleading:
        add("## سطری که زیرِ سربرگِ هم‌نامش نیست\n")
        for m in misleading:
            add("- `%s` → انتظار `%s` ، واقعاً `%s`"
                % (m["table"], m["expected_parent"], m["actual_parent"]))
        add("")

    years = sorted(t for t, v in schema["tables"].items()
                   if "year_snapshot" in v["flags"])
    if years:
        add("## جدول‌های سال‌دار (%d)" % len(years))
        add("")
        add("اسمشان به سال یا تاریخ ختم می‌شود — عکسِ یک دوره‌اند، نه جدولِ")
        add("جاری. برای گزارشِ امروز از هیچ‌کدام عدد نگیر.")
        add("")
        add("`" + "`، `".join(years) + "`")
        add("")

    empties = sorted(t for t, v in schema["tables"].items() if v["rows"] == 0)
    unknown = [t for t, v in schema["tables"].items() if v["rows"] is None]
    if unknown:
        add("## تعداد سطر نامعلوم است (%d جدول)" % len(unknown))
        add("")
        add("فهرست ستون‌ها تعداد سطر ندارد. **بدون آن نمی‌شود گفت کدامِ دو")
        add("جدولِ دوقلو زنده است و کدام جدول مرده.** بخش ۱")
        add("`references/introspection.md` را بزن.")
        add("")
    if empties:
        add("## جدول‌های خالی (%d)\n" % len(empties))
        add("خالی یعنی یا مرده است یا این ماژول استفاده نمی‌شود — **هر دو را در")
        add("گزارش بگو**، ولی به‌عنوان منبع حقیقت رویشان حساب نکن.\n")
        add("`" + "`، `".join(empties[:60]) + "`\n")

    unnamed = [cc for cc, m in schema["external_cc"].items() if not m["note"]]
    if unnamed:
        add("## ارجاع‌های بیرونی بی‌تفسیر (%d)\n" % len(unnamed))
        add("اینها در این اسکیما جدول ندارند. **مقصدشان را پیدا کن** (اسکیمای")
        add("دیگر؟) و در `external_cc[..].note` بنویس. جدول محلی برایشان نساز.\n")
        for cc in unnamed[:40]:
            add("- `%s` — %d بار" % (cc, schema["external_cc"][cc]["count"]))
        add("")

    add("## بعد از حل اینها\n")
    add("۱. `role` و `domains` و `external_cc[..].note` را پر کن.")
    add("۲. `python scripts/scaffold.py readme schema.json --out \"%s Map.md\"`" % args.schema)
    add("۳. `python scripts/scaffold.py skill schema.json --out <پوشه‌ی اسکیل>`")
    add("۴. اعتبارسنجی: بخش ۹ `references/introspection.md`.")

    with io.open(args.findings, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
