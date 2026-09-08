#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
پیمایش نقشه‌ی اسکیمای HumanResource.

نقشه از HR Map.xlsx درآمده و هیچ اتصالی در آن کلید خارجیِ اثبات‌شده نیست.
خروجی این اسکریپت «حدسِ اول» است، نه واقعیتِ دیتابیس.

    python hr_map.py table    <TableName>
    python hr_map.py refs     <TableName>
    python hr_map.py path     <From> <To> [--avoid T1,T2]
    python hr_map.py find     <متن>
    python hr_map.py domain   [<domain-key>]
    python hr_map.py external
    python hr_map.py traps    [<TableName>]
    python hr_map.py drift    <live-tables.txt>
"""

import io
import json
import os
import sys
from collections import deque

# روی ویندوز، خروجی فارسی با کدپیج سیستم به هم می‌ریزد.
for _s in ("stdout", "stderr"):
    _stream = getattr(sys, _s, None)
    if _stream is not None and hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8")
        except Exception:
            pass

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           os.pardir, "schema.json")

# پسوندهایی که روی نام یک ارجاع می‌نشینند بدون اینکه مقصد را عوض کنند.
ROLE_SUFFIXES = ("_Link", "_Old", "_OLD", "_Jadid", "_Asli", "_Movaghat",
                 "_SabtKonandeh", "_Zamen", "_Bimar", "_Mabda", "_Maghsad",
                 "_ArzyabiKonandeh", "_RoozTatil", "_Hoghogh", "_Bimeh",
                 "_Maliat", "_Eydi", "_Next")

FLAG_LABEL = {
    "anchor": "لنگرگاه — بیشترین ارجاع ورودی",
    "hub": "دیکشنری مرکزی",
    "hub_target": "مقصدِ پرارجاع — برای دیدن فرزندان از refs استفاده کن",
    "effective_dated": "بازه‌دار — FromDate/EndDate را اعمال کن",
    "status_header": "وضعیت‌دار — CodeVazeiat را فیلتر کن",
    "status_dict": "دیکشنری کد وضعیت",
    "status_history": "تاریخچه‌ی وضعیت — برای فیلتر به سربرگ join نکن",
    "reason_dict": "دیکشنری علت برگشت",
    "detail": "جدول سطر — دانه را قبل از جمع بشمار",
    "dict": "دیکشنری/داده‌ی مرجع",
    "ledger": "دفترِ بد/بس — مانده از جمع جبری درمی‌آید",
    "tree": "سلسله‌مراتبی — CTE بازگشتی لازم است",
    "twin": "جدول دوقلو دارد — قبل از استفاده بشمار",
    "misleading_name": "اسمش گمراه‌کننده است — یادداشت را بخوان",
    "type_mismatch": "ناسازگاری نوع در اتصال",
    "dead_column": "ستون مرده دارد",
    "legacy": "میراث — منبع حقیقت نیست",
    "migration": "داده‌ی مهاجرت — با داده‌ی جاری جمع نزن",
    "sensitive": "داده‌ی محرمانه — بخش محرمانگی reporting.md",
    "grain_risk": "دانه‌اش قطعی نیست — قبل از SUM بشمار",
    "deactivatable": "ZamanGheirFaali دارد — علاوه بر بازه و وضعیت",
    "rule": "جدول قاعده/آیین‌نامه",
    "rate_table": "جدول نرخ",
    "config": "پیکربندی گردش کار",
    "export_format": "قالب فایل خروجی — برای تحلیل استفاده نکن",
    "non_cc_key": "کلیدش cc نیست",
    "modern": "لایه‌ی جدید سیستم",
    "infra": "زیرساخت — داده‌ی کسب‌وکاری نیست",
    "job_queue": "صف کار",
}


def load():
    with io.open(SCHEMA_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def resolve(cc, tables):
    """ccX را به جدول X می‌رساند. (target, is_exact) یا (None, False)."""
    if not cc.startswith("cc") or len(cc) < 3:
        return None, False
    base = cc[2:]
    if base in tables:
        return base, True
    for suf in ROLE_SUFFIXES:
        if base.endswith(suf):
            trimmed = base[: -len(suf)]
            if trimmed in tables:
                return trimmed, False
    # حالت حساس‌نبودن به بزرگی و کوچکی حروف (ccphoto، ccuser و مانند آن)
    low = {t.lower(): t for t in tables}
    if base.lower() in low:
        return low[base.lower()], False
    return None, False


def build_edges(data):
    """[(source, cc, target, exact)] — قاعده: A.ccB → B."""
    tables = data["tables"]
    edges = []
    for name, meta in tables.items():
        for cc in meta.get("cc", []):
            target, exact = resolve(cc, tables)
            if target and target != name:
                edges.append((name, cc, target, exact))
    return edges


def adjacency(edges):
    adj = {}
    for src, cc, dst, exact in edges:
        adj.setdefault(src, []).append((dst, cc, src, exact))
        adj.setdefault(dst, []).append((src, cc, src, exact))
    return adj


def match_table(name, tables):
    if name in tables:
        return name
    low = {t.lower(): t for t in tables}
    if name.lower() in low:
        return low[name.lower()]
    return None


def suggest(name, tables, limit=8):
    n = name.lower()
    hits = [t for t in tables if n in t.lower()]
    if not hits:
        hits = [t for t in tables if t.lower().startswith(n[:4])]
    return sorted(hits)[:limit]


def show_flags(meta, indent="  "):
    out = []
    for f in meta.get("flags", []):
        out.append("%s! %s" % (indent, FLAG_LABEL.get(f, f)))
    return out


def cmd_table(data, args):
    tables = data["tables"]
    if not args:
        return err("نام جدول را بده.")
    name = match_table(args[0], tables)
    if not name:
        s = suggest(args[0], tables)
        print("جدول «%s» در نقشه نیست." % args[0])
        if s:
            print("شبیه‌ها: " + "، ".join(s))
        print("\nنقشه ناقص است، نه دیتابیس. کوئری ۰.۲ references/queries.md "
              "اسم واقعی را می‌آورد.")
        return 1

    meta = tables[name]
    print("[HumanResource].[%s]" % name)
    print("  دامنه : %s" % data["domains"].get(meta.get("domain"), "—"))
    print("  نقش   : %s" % meta.get("role", "—"))
    print("  کلید  : %s" % meta.get("pk", "— نامشخص"))

    for line in show_flags(meta):
        print(line)

    if meta.get("note"):
        print("\n  یادداشت: %s" % meta["note"])

    if meta.get("cols"):
        print("\n  ستون‌های شاخص:")
        for c in meta["cols"]:
            print("    - %s" % c)

    if meta.get("dead_cols"):
        print("\n  ستون‌های مرده — استفاده نکن:")
        for c in meta["dead_cols"]:
            print("    x %s" % c)

    edges = build_edges(data)
    out = [(cc, dst, ex) for (s, cc, dst, ex) in edges if s == name]
    if out:
        print("\n  به بیرون اشاره می‌کند:")
        for cc, dst, ex in sorted(out):
            mark = "" if ex else "   (حدسِ ضعیف‌تر — پسوند نقش)"
            print("    %s.%s = %s.%s%s" % (name, cc, dst, cc, mark))

    unresolved = []
    for cc in meta.get("cc", []):
        target, _ = resolve(cc, tables)
        if not target:
            unresolved.append(cc)
    if unresolved:
        print("\n  ارجاعِ بیرونی/حل‌نشده (جدول محلی برایشان نساز):")
        for cc in sorted(unresolved):
            note = data["external_cc"].get(cc, {}).get("note", "خارج از این اسکیما")
            print("    ? %s — %s" % (cc, note))

    inc = [(s, cc) for (s, cc, dst, ex) in edges if dst == name]
    print("\n  ارجاعِ ورودی: %d جدول (برای فهرست: refs %s)" % (len(inc), name))
    return 0


def cmd_refs(data, args):
    tables = data["tables"]
    if not args:
        return err("نام جدول را بده.")
    name = match_table(args[0], tables)
    if not name:
        print("جدول «%s» در نقشه نیست." % args[0])
        s = suggest(args[0], tables)
        if s:
            print("شبیه‌ها: " + "، ".join(s))
        return 1

    edges = build_edges(data)
    inc = sorted({(s, cc) for (s, cc, dst, ex) in edges if dst == name})
    print("چه چیزهایی به [%s] اشاره می‌کنند — %d مورد\n" % (name, len(inc)))
    by_domain = {}
    for src, cc in inc:
        d = tables[src].get("domain", "?")
        by_domain.setdefault(d, []).append((src, cc))
    for d in sorted(by_domain):
        print("· %s" % data["domains"].get(d, d))
        for src, cc in sorted(by_domain[d]):
            flags = tables[src].get("flags", [])
            tag = ""
            if "legacy" in flags:
                tag = "   [میراث]"
            elif "migration" in flags:
                tag = "   [مهاجرت]"
            elif "detail" in flags:
                tag = "   [سطر]"
            print("    %s.%s%s" % (src, cc, tag))
        print("")
    return 0


def cmd_path(data, args):
    tables = data["tables"]
    if len(args) < 2:
        return err("مبدأ و مقصد را بده: path <From> <To>")

    avoid = set()
    rest = []
    i = 0
    while i < len(args):
        if args[i] == "--avoid" and i + 1 < len(args):
            avoid = {a.strip() for a in args[i + 1].split(",") if a.strip()}
            i += 2
        else:
            rest.append(args[i])
            i += 1

    src = match_table(rest[0], tables)
    dst = match_table(rest[1], tables) if len(rest) > 1 else None
    if not src or not dst:
        bad = rest[0] if not src else rest[1]
        print("جدول «%s» در نقشه نیست." % bad)
        s = suggest(bad, tables)
        if s:
            print("شبیه‌ها: " + "، ".join(s))
        return 1

    adj = adjacency(build_edges(data))
    seen = {src}
    q = deque([(src, [])])
    found = None
    while q:
        node, trail = q.popleft()
        if node == dst:
            found = trail
            break
        for nxt, cc, owner, exact in adj.get(node, []):
            if nxt in seen or nxt in avoid:
                continue
            seen.add(nxt)
            q.append((nxt, trail + [(node, nxt, cc, owner)]))

    if found is None:
        print("مسیری از %s به %s در نقشه نیست." % (src, dst))
        print("یعنی یا واقعاً وصل نیستند، یا از یک موجودیتِ بیرونی "
              "(مثل ccAfrad یا ccMarkaz) رد می‌شوند که این نقشه ندارد.")
        return 1

    print("مسیر: %s ← %s   (%d پرش)\n" % (dst, src, len(found)))
    for step, (a, b, cc, owner) in enumerate(found, 1):
        left, right = (a, b) if owner == a else (b, a)
        print("%d. %s.%s = %s.%s" % (step, left, cc, right, cc))
        for t in (a, b):
            meta = tables[t]
            for f in ("effective_dated", "status_header", "detail", "ledger",
                      "misleading_name", "deactivatable", "grain_risk"):
                if f in meta.get("flags", []):
                    print("     ! %s: %s" % (t, FLAG_LABEL[f]))
    print("\nاین مسیر ساختاری است، نه معنایی. ممکن است از جدولی رد شود که "
          "به سؤال تو ربطی ندارد —")
    print("با --avoid آن را کنار بگذار و دوباره بگیر. و هیچ‌کدام از این "
          "اتصال‌ها کلید خارجی ندارند.")
    return 0


def cmd_find(data, args):
    tables = data["tables"]
    if not args:
        return err("یک متن برای جست‌وجو بده.")
    q = args[0].lower()
    hits = sorted(t for t in tables if q in t.lower())
    if not hits:
        print("چیزی با «%s» پیدا نشد." % args[0])
        print("املای دیگر را امتحان کن — این اسکیما i/y و o/u و "
              "Madrak/Madarek را جابه‌جا به کار می‌برد.")
        return 1
    print("%d جدول با «%s»\n" % (len(hits), args[0]))
    for t in hits:
        meta = tables[t]
        tags = []
        for f in ("legacy", "migration", "twin", "misleading_name",
                  "export_format", "sensitive"):
            if f in meta.get("flags", []):
                tags.append(f)
        tag = ("   [%s]" % ", ".join(tags)) if tags else ""
        print("%-52s %s%s" % (t, meta.get("role", ""), tag))
    return 0


def cmd_domain(data, args):
    tables = data["tables"]
    if not args:
        print("دامنه‌ها:\n")
        counts = {}
        for meta in tables.values():
            counts[meta.get("domain")] = counts.get(meta.get("domain"), 0) + 1
        for k, label in data["domains"].items():
            print("  %-14s %-42s %d جدول" % (k, label, counts.get(k, 0)))
        return 0
    key = args[0]
    if key not in data["domains"]:
        print("دامنه‌ی «%s» نیست. یکی از: %s"
              % (key, "، ".join(data["domains"])))
        return 1
    print("%s\n" % data["domains"][key])
    for t in sorted(t for t, m in tables.items() if m.get("domain") == key):
        meta = tables[t]
        tags = [f for f in ("legacy", "migration", "twin", "detail", "dict")
                if f in meta.get("flags", [])]
        tag = ("   [%s]" % ", ".join(tags)) if tags else ""
        print("%-52s %s%s" % (t, meta.get("role", ""), tag))
    return 0


def cmd_external(data, args):
    print("ارجاع‌هایی که در HumanResource جدول ندارند — جدول محلی برایشان نساز\n")
    items = sorted(data["external_cc"].items(),
                   key=lambda kv: -kv[1].get("count", 0))
    for cc, meta in items:
        print("%-26s %4s   %s" % (cc, meta.get("count", "?"), meta.get("note", "")))
    print("\nپلِ بین اسکیمایی:")
    for name, meta in data.get("cross_schema", {}).items():
        flag = "تأییدشده" if meta.get("verified") else "تأییدنشده"
        print("  %-18s [%s] از %s — %s"
              % (name, flag, meta.get("via", "?"), meta.get("note", "")))
    return 0


def cmd_traps(data, args):
    traps = data["traps"]
    tables = data["tables"]

    if args:
        name = match_table(args[0], tables)
        if not name:
            print("جدول «%s» در نقشه نیست." % args[0])
            return 1
        hits = 0
        print("تله‌های [%s]\n" % name)
        for pair in traps["twins"]:
            if name in pair["pair"]:
                other = [p for p in pair["pair"] if p != name][0]
                print("· دوقلو: %s (فرق: %s)" % (other, pair["diff"]))
                if pair.get("note"):
                    print("    %s" % pair["note"])
                hits += 1
        for tm in traps["type_mismatch"]:
            if tm["col"].split(".")[0] == name:
                print("· ناسازگاری نوع: %s از نوع %s ولی مقصد %s"
                      % (tm["col"], tm["declared"], tm["target"]))
                hits += 1
        for wm in traps["width_mismatch"]:
            if wm["child"].split(".")[0] == name or wm["parent"].split(".")[0] == name:
                print("· عرضِ ناسازگار: %s (%s) → %s (%s)"
                      % (wm["child"], wm["child_type"], wm["parent"], wm["parent_type"]))
                if wm.get("note"):
                    print("    %s" % wm["note"])
                hits += 1
        for ms in traps["misleading_satr"]:
            if ms["table"] == name:
                print("· اسم گمراه‌کننده: زیرِ %s نیست، زیرِ %s است."
                      % (ms["expected_parent"], ms["actual_parent"]))
                hits += 1
        if name in traps["begin_date_tables"]:
            print("· ستون شروع BeginDate است، نه FromDate.")
            hits += 1
        if name in traps["end_date_not_null"]:
            print("· EndDate تهی‌پذیر نیست — الگوی EndDate IS NULL کار نمی‌کند.")
            hits += 1
        meta = tables[name]
        if meta.get("dead_cols"):
            print("· ستون‌های مرده: %s" % "، ".join(meta["dead_cols"]))
            hits += 1
        if not hits:
            print("تله‌ی ثبت‌شده‌ای ندارد. یعنی چیزی یادداشت نشده، "
                  "نه اینکه بی‌خطر است.")
        return 0

    print("=== جدول‌های دوقلو — اشتباه گرفتنشان جدولِ خالی می‌دهد، نه خطا ===\n")
    for p in traps["twins"]:
        print("  %s  ⟷  %s      (فرق: %s)" % (p["pair"][0], p["pair"][1], p["diff"]))
        if p.get("note"):
            print("      %s" % p["note"])

    print("\n=== سطری که زیرِ سربرگِ هم‌نامش نیست ===\n")
    for m in traps["misleading_satr"]:
        print("  %s → انتظار: %s ، واقعاً: %s"
              % (m["table"], m["expected_parent"], m["actual_parent"]))

    print("\n=== ناسازگاری نوع ===\n")
    for tm in traps["type_mismatch"]:
        print("  %-56s %-10s → %s" % (tm["col"], tm["declared"], tm["target"]))

    print("\n=== عرضِ ناسازگار ===\n")
    for wm in traps["width_mismatch"]:
        note = ("   " + wm["note"]) if wm.get("note") else ""
        print("  %-48s %-8s → %-8s%s"
              % (wm["child"], wm["child_type"], wm["parent_type"], note))

    print("\n=== ستون‌های مرده ===\n")
    dc = traps["dead_columns"]
    print("  %s" % dc["rule_dead"])
    print("  %s" % dc["rule_suspect"])
    print("  زنده با معنیِ «قبلی»: %s" % "، ".join(dc["alive_old"]))
    print("  مشکوک: %s" % "، ".join(dc["suspect"]))

    print("\n=== ستون شروع BeginDate است، نه FromDate ===\n")
    print("  " + "، ".join(traps["begin_date_tables"]))

    print("\n=== EndDate تهی‌پذیر نیست ===\n")
    print("  " + "، ".join(traps["end_date_not_null"]))

    legacy = sorted(t for t, m in tables.items()
                    if "legacy" in m.get("flags", []))
    print("\n=== میراث — منبع حقیقت نیستند ===\n")
    print("  " + "، ".join(legacy))
    return 0



STABILITY_LABEL = {
    "core": "هسته — ساختاری",
    "connected": "متصل",
    "leaf": "برگ — هیچ‌کس به آن اشاره نمی‌کند",
    "volatile": "ناپایدار — میراث/مهاجرت/آرشیو",
}

# چیزهایی که نقشه **عمداً** ندارد. نبودنشان اختلاف نیست.
_SKIP = ("tmp", "V_", "v")
_SKIP_MARK = ("_old", "_ooold", "_History", "History", "_Archive",
              "_Backup", "Backup", "DeletedFile", "_Deeel")


def _excluded_kind(t):
    if t[:1] == "v" and t[1:2].isupper():
        return "ویو"
    if t[:2] == "V_" or t[:4] == "vtmp":
        return "ویو"
    if t[:3].lower() == "tmp":
        return "موقت"
    low = t.lower()
    for k in _SKIP_MARK:
        if low.endswith(k.lower()) or k.lower() in low:
            return "میراث"
    return None


def _read_live(path):
    live = set()
    with io.open(path, encoding="utf-8-sig") as fh:
        for line in fh:
            t = line.strip()
            if not t:
                continue
            if chr(9) in t:
                t = t.split(chr(9))[-1].strip()
            t = t.strip("[]" + chr(34) + "',")
            if "." in t and " " not in t:
                t = t.split(".")[-1].strip("[]")
            if not t or t.lower() in ("table", "table_name", "name",
                                      "tablename", "objectname"):
                continue
            live.add(t)
    return live


def cmd_drift(data, args):
    """نقشه در برابر دیتابیسِ زنده.

    نقشه قابل اعتماد است؛ این فقط تطبیقِ گاه‌به‌گاه است. ساکت می‌ماند
    مگر چیزی واقعاً عوض شده باشد.
    """
    if not args:
        print("فهرست جدول‌های زنده را بده (یک نام در هر خط).")
        print("")
        print("این کوئری فهرست را می‌دهد:")
        print("  SELECT t.name FROM sys.tables AS t")
        print("  JOIN sys.schemas AS s ON s.schema_id = t.schema_id")
        print("  WHERE s.name = '%s' ORDER BY t.name;"
              % data["meta"].get("schema", "<Schema>"))
        return 2

    tables = data["tables"]
    live = _read_live(args[0])
    if not live:
        print("فایل خالی بود یا خوانده نشد.")
        return 1

    mapped = set(tables)
    known_views = set(data.get("views_excluded", []))
    gone = sorted(mapped - live)

    new_all = live - mapped - known_views
    skipped = {}
    new_core = []
    for t in sorted(new_all):
        kind = _excluded_kind(t)
        if kind:
            skipped[kind] = skipped.get(kind, 0) + 1
        else:
            new_core.append(t)

    print("نقشه %d جدولِ هسته دارد؛ دیتابیس %d شیء."
          % (len(mapped), len(live)))
    if skipped:
        print("عمداً بیرون از نقشه: %s — این درست است."
              % "، ".join("%d %s" % (n, k) for k, n in sorted(skipped.items())))
    print("")

    if not gone and not new_core:
        print("**نقشه می‌خواند.** هیچ جدولِ هسته‌ای اضافه یا کم نشده.")
        return 0

    if new_core:
        print("=== تازه در دیتابیس، نبود در نقشه (%d) ===" % len(new_core))
        for t in new_core:
            print("    %s" % t)
        print("")
        print("بعد از گرفتنِ نقشه اضافه شده‌اند. **«وجود ندارد» گزارششان نکن.**")
        print("")

    if gone:
        by_stab = {}
        for t in gone:
            by_stab.setdefault(tables[t].get("stability", "?"), []).append(t)
        print("=== در نقشه هست، در دیتابیس نیست (%d) ===" % len(gone))
        for key in ("core", "connected", "leaf", "volatile", "?"):
            group = by_stab.get(key)
            if not group:
                continue
            print("· %s" % STABILITY_LABEL.get(key, key))
            for t in group:
                print("    %s" % t)
        print("")
        if by_stab.get("core"):
            print("جدولِ هسته‌ای غایب است — احتمالِ اولش تغییرِ نام است، نه")
            print("حذف. با کوئری ۰.۲ دنبال نامِ شبیه بگرد.")
    return 0


def err(msg):
    print(msg)
    print(__doc__)
    return 2


COMMANDS = {
    "table": cmd_table,
    "refs": cmd_refs,
    "path": cmd_path,
    "find": cmd_find,
    "domain": cmd_domain,
    "external": cmd_external,
    "traps": cmd_traps,
    "drift": cmd_drift,
}


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    cmd = argv[0]
    if cmd not in COMMANDS:
        return err("دستور «%s» نیست." % cmd)
    data = load()
    return COMMANDS[cmd](data, argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
