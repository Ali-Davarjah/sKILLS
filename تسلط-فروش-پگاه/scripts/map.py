#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
پیمایش نقشه‌ی اسکیما. مستقل از اسکیما کار می‌کند — هر چه لازم دارد در
`schema.json` کنارِ همین پوشه است.

    python map.py table    <TableName>
    python map.py refs     <TableName>
    python map.py path     <From> <To> [--avoid T1,T2]
    python map.py find     <متن>
    python map.py domain   [<domain-key>]
    python map.py external
    python map.py traps    [<TableName>]
    python map.py drift    <live-tables.txt>

خروجی «حدسِ اول» است مگر جایی که `CONFIRMED` بنویسد؛ آن یعنی کلید خارجی
واقعی. بقیه از هم‌نامی درآمده و اسکیمای زنده حرف آخر را می‌زند.
"""

import io
import json
import os
import sys
from collections import deque

for _s in ("stdout", "stderr"):
    _st = getattr(sys, _s, None)
    if _st is not None and hasattr(_st, "reconfigure"):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = next(
    (p for p in (os.path.join(HERE, os.pardir, "schema.json"),
                 os.path.join(HERE, "schema.json"))
     if os.path.exists(p)), os.path.join(HERE, os.pardir, "schema.json"))

ROLE_SUFFIXES = ("_Link", "_Old", "_OLD", "_Jadid", "_Asli", "_Movaghat",
                 "_SabtKonandeh", "_Zamen", "_Bimar", "_Mabda", "_Maghsad",
                 "_RoozTatil", "_Next", "_Hoghogh", "_Bimeh", "_Maliat",
                 "_Eydi", "_Parent", "_Sabegh")

FLAG_LABEL = {
    "anchor": "لنگرگاه — بیشترین ارجاع ورودی",
    "hub_target": "مقصدِ پرارجاع — فرزندانش را با refs ببین",
    "effective_dated": "بازه‌دار — FromDate/EndDate را اعمال کن",
    "status_header": "وضعیت‌دار — CodeVazeiat را فیلتر کن",
    "status_dict": "دیکشنری کد وضعیت",
    "status_history": "تاریخچه‌ی وضعیت — برای فیلتر به سربرگ join نکن",
    "reason_dict": "دیکشنری علت برگشت",
    "detail": "جدول سطر — دانه را قبل از جمع بشمار",
    "attachment": "پیوست/مدرک",
    "dict": "دیکشنری/داده‌ی مرجع",
    "ledger": "دفترِ بد/بس — مانده از جمع جبری درمی‌آید",
    "tree": "سلسله‌مراتبی — CTE بازگشتی لازم است",
    "deactivatable": "ZamanGheirFaali دارد — علاوه بر بازه و وضعیت",
    "sensitive": "داده‌ی محرمانه",
    "grain_risk": "دانه‌اش قطعی نیست — قبل از SUM بشمار",
    "legacy": "میراث — منبع حقیقت نیست",
    "migration": "داده‌ی مهاجرت — با داده‌ی جاری جمع نزن",
    "config": "پیکربندی گردش کار",
    "rule": "جدول قاعده/آیین‌نامه",
    "empty": "خالی — صفر سطر",
    "archive_check": "اسمش آرشیو است — ولی ممکن است خودِ جدولِ اصلی باشد؛ بشمار",
    "rows_unknown": "تعداد سطر گرفته نشده",
    "end_date_not_null": "EndDate تهی‌پذیر نیست — الگوی IS NULL کار نمی‌کند",
}


def load():
    with io.open(SCHEMA_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def resolve(cc, tables):
    if not cc.startswith("cc") or len(cc) < 4:
        return None, False
    base = cc[2:]
    if base in tables:
        return base, True
    for suf in ROLE_SUFFIXES:
        if base.endswith(suf) and base[: -len(suf)] in tables:
            return base[: -len(suf)], False
    low = {t.lower(): t for t in tables}
    if base.lower() in low:
        return low[base.lower()], False
    return None, False


def build_edges(data):
    """یال‌های ذخیره‌شده را ترجیح بده؛ نبود، از قاعده بساز."""
    if data.get("edges"):
        return [(e["source"], e["col"], e["target"],
                 e.get("confidence", "LOW"), e.get("evidence", "NAMING_ONLY"))
                for e in data["edges"]]
    tables = data["tables"]
    out = []
    for name, meta in tables.items():
        for cc in meta.get("cc", []):
            tgt, exact = resolve(cc, tables)
            if tgt and tgt != name:
                out.append((name, cc, tgt, "HIGH" if exact else "LOW",
                            "EXACT_CC_ID_MATCH" if exact else "NAMING_ONLY"))
    return out


def adjacency(edges):
    adj = {}
    for src, cc, dst, conf, ev in edges:
        adj.setdefault(src, []).append((dst, cc, src, conf))
        adj.setdefault(dst, []).append((src, cc, src, conf))
    return adj


def match_table(name, tables):
    if name in tables:
        return name
    low = {t.lower(): t for t in tables}
    return low.get(name.lower())


def suggest(name, tables, limit=8):
    n = name.lower()
    hits = [t for t in tables if n in t.lower()]
    if not hits:
        hits = [t for t in tables if t.lower().startswith(n[:4])]
    return sorted(hits)[:limit]


def cmd_table(data, args):
    tables = data["tables"]
    if not args:
        return err("نام جدول را بده.")
    name = match_table(args[0], tables)
    if not name:
        print("جدول «%s» در نقشه نیست." % args[0])
        s = suggest(args[0], tables)
        if s:
            print("شبیه‌ها: " + "، ".join(s))
        print("\nنقشه ناقص است، نه دیتابیس. کوئری ۰.۲ اسم واقعی را می‌آورد.")
        return 1

    meta = tables[name]
    print("[%s].[%s]" % (data["meta"].get("schema", "?"), name))
    print("  دامنه : %s" % data.get("domains", {}).get(meta.get("domain"), "—"))
    print("  نقش   : %s" % (meta.get("role") or "— هنوز نوشته نشده"))
    print("  کلید  : %s" % (meta.get("pk") or "— نامشخص"))
    if meta.get("rows") is not None:
        print("  سطر   : %s" % meta["rows"])
    for f in meta.get("flags", []):
        print("  ! %s" % FLAG_LABEL.get(f, f))
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
    out = [(cc, dst, conf) for (s, cc, dst, conf, ev) in edges if s == name]
    if out:
        print("\n  به بیرون اشاره می‌کند:")
        for cc, dst, conf in sorted(out):
            tag = "" if conf == "CONFIRMED" else "   [%s]" % conf
            print("    %s.%s = %s.%s%s" % (name, cc, dst, cc, tag))

    unresolved = [cc for cc in meta.get("cc", []) if not resolve(cc, tables)[0]]
    if unresolved:
        print("\n  ارجاعِ بیرونی/حل‌نشده (جدول محلی برایشان نساز):")
        for cc in sorted(unresolved):
            note = data.get("external_cc", {}).get(cc, {}).get("note", "")
            print("    ? %s%s" % (cc, ("  — " + note) if note else ""))

    inc = [s for (s, cc, dst, conf, ev) in edges if dst == name]
    print("\n  ارجاعِ ورودی: %d جدول (برای فهرست: refs %s)" % (len(inc), name))
    return 0


def cmd_refs(data, args):
    tables = data["tables"]
    if not args:
        return err("نام جدول را بده.")
    name = match_table(args[0], tables)
    if not name:
        print("جدول «%s» در نقشه نیست." % args[0])
        return 1
    edges = build_edges(data)
    inc = sorted({(s, cc, conf) for (s, cc, d, conf, ev) in edges if d == name})
    print("چه چیزهایی به [%s] اشاره می‌کنند — %d مورد\n" % (name, len(inc)))
    by_dom = {}
    for src, cc, conf in inc:
        by_dom.setdefault(tables[src].get("domain", "?"), []).append((src, cc, conf))
    for d in sorted(by_dom):
        print("· %s" % data.get("domains", {}).get(d, d))
        for src, cc, conf in sorted(by_dom[d]):
            fl = tables[src].get("flags", [])
            tag = "   [میراث]" if "legacy" in fl else (
                "   [مهاجرت]" if "migration" in fl else (
                    "   [سطر]" if "detail" in fl else ""))
            print("    %s.%s%s" % (src, cc, tag))
        print("")
    return 0


def cmd_path(data, args):
    tables = data["tables"]
    avoid, rest, i = set(), [], 0
    while i < len(args):
        if args[i] == "--avoid" and i + 1 < len(args):
            avoid = {a.strip() for a in args[i + 1].split(",") if a.strip()}
            i += 2
        else:
            rest.append(args[i]); i += 1
    if len(rest) < 2:
        return err("مبدأ و مقصد را بده: path <From> <To>")
    src, dst = match_table(rest[0], tables), match_table(rest[1], tables)
    if not src or not dst:
        bad = rest[0] if not src else rest[1]
        print("جدول «%s» در نقشه نیست." % bad)
        s = suggest(bad, tables)
        if s:
            print("شبیه‌ها: " + "، ".join(s))
        return 1

    adj = adjacency(build_edges(data))
    seen, q, found = {src}, deque([(src, [])]), None
    while q:
        node, trail = q.popleft()
        if node == dst:
            found = trail
            break
        for nxt, cc, owner, conf in adj.get(node, []):
            if nxt in seen or nxt in avoid:
                continue
            seen.add(nxt)
            q.append((nxt, trail + [(node, nxt, cc, owner, conf)]))

    if found is None:
        print("مسیری از %s به %s در نقشه نیست." % (src, dst))
        print("یعنی یا وصل نیستند، یا از موجودیتی بیرونی رد می‌شوند که نقشه ندارد.")
        return 1

    print("مسیر: %s ← %s   (%d پرش)\n" % (dst, src, len(found)))
    for n, (a, b, cc, owner, conf) in enumerate(found, 1):
        left, right = (a, b) if owner == a else (b, a)
        tag = "" if conf == "CONFIRMED" else "   [%s]" % conf
        print("%d. %s.%s = %s.%s%s" % (n, left, cc, right, cc, tag))
        for t in (a, b):
            for f in ("effective_dated", "status_header", "detail", "ledger",
                      "deactivatable", "grain_risk", "end_date_not_null"):
                if f in tables[t].get("flags", []):
                    print("     ! %s: %s" % (t, FLAG_LABEL[f]))
    print("\nمسیر ساختاری است، نه معنایی — ممکن است از جدولی رد شود که به سؤال")
    print("تو ربطی ندارد. با --avoid کنارش بگذار و دوباره بگیر.")
    return 0


def cmd_find(data, args):
    tables = data["tables"]
    if not args:
        return err("یک متن برای جست‌وجو بده.")
    q = args[0].lower()
    hits = sorted(t for t in tables if q in t.lower())
    if not hits:
        print("چیزی با «%s» پیدا نشد." % args[0])
        print("املای دیگر را امتحان کن — i/y و o/u و Madrak/Madarek جابه‌جا می‌شوند.")
        return 1
    print("%d جدول با «%s»\n" % (len(hits), args[0]))
    for t in hits:
        meta = tables[t]
        tags = [f for f in ("legacy", "migration", "twin", "detail", "dict",
                            "empty", "sensitive") if f in meta.get("flags", [])]
        print("%-52s %s%s" % (t, meta.get("role") or "",
                              ("   [%s]" % ", ".join(tags)) if tags else ""))
    return 0


def cmd_domain(data, args):
    tables, domains = data["tables"], data.get("domains", {})
    if not args:
        counts = {}
        for m in tables.values():
            counts[m.get("domain")] = counts.get(m.get("domain"), 0) + 1
        print("دامنه‌ها:\n")
        for k, label in domains.items():
            print("  %-14s %-42s %d جدول" % (k, label, counts.get(k, 0)))
        return 0
    key = args[0]
    if key not in domains:
        print("دامنه‌ی «%s» نیست. یکی از: %s" % (key, "، ".join(domains)))
        return 1
    print("%s\n" % domains[key])
    for t in sorted(t for t, m in tables.items() if m.get("domain") == key):
        print("%-52s %s" % (t, tables[t].get("role") or ""))
    return 0


def cmd_external(data, args):
    print("ارجاع‌هایی که در این اسکیما جدول ندارند — جدول محلی برایشان نساز\n")
    for cc, m in data.get("external_cc", {}).items():
        print("%-30s %4s   %s" % (cc, m.get("count", "?"), m.get("note") or "؟"))
    cs = data.get("cross_schema", {})
    if cs:
        print("\nپلِ بین اسکیمایی:")
        for name, m in cs.items():
            print("  %-20s [%s] از %s — %s"
                  % (name, "تأییدشده" if m.get("verified") else "تأییدنشده",
                     m.get("via", "?"), m.get("note", "")))
    return 0


def cmd_traps(data, args):
    tp, tables = data.get("traps", {}), data["tables"]
    if args:
        name = match_table(args[0], tables)
        if not name:
            print("جدول «%s» در نقشه نیست." % args[0])
            return 1
        print("تله‌های [%s]\n" % name)
        hits = 0
        for tw in tp.get("twins", []):
            if name in tw["pair"]:
                other = [p for p in tw["pair"] if p != name]
                print("· دوقلو: %s (اطمینان %s)"
                      % ("، ".join(other), tw.get("confidence", "?")))
                hits += 1
        for x in tp.get("type_mismatch", []):
            if x["col"].split(".")[0] == name:
                print("· ناسازگاری نوع: %s از نوع %s، مقصد %s"
                      % (x["col"], x["declared"], x["target"]))
                hits += 1
        for x in tp.get("width_mismatch", []):
            if name in (x["child"].split(".")[0], x["parent"].split(".")[0]):
                print("· عرض: %s (%s) → %s (%s) %s"
                      % (x["child"], x["child_type"], x["parent"],
                         x["parent_type"], x.get("note", "")))
                hits += 1
        for m in tp.get("misleading_satr", []):
            if m["table"] == name:
                print("· اسم گمراه‌کننده: زیرِ %s نیست، زیرِ %s است."
                      % (m["expected_parent"], m["actual_parent"]))
                hits += 1
        if name in tp.get("begin_date_tables", []):
            print("· ستون شروع FromDate نیست."); hits += 1
        if name in tp.get("end_date_not_null", []):
            print("· EndDate تهی‌پذیر نیست — الگوی IS NULL کار نمی‌کند."); hits += 1
        if tables[name].get("dead_cols"):
            print("· ستون مرده: %s" % "، ".join(tables[name]["dead_cols"])); hits += 1
        if not hits:
            print("تله‌ی ثبت‌شده‌ای ندارد — یعنی چیزی یادداشت نشده، نه اینکه بی‌خطر است.")
        return 0

    if tp.get("fk_contradicts_naming"):
        print("=== کلید خارجی با نام‌گذاری نمی‌خواند — اینجا قرارداد می‌شکند ===\n")
        for c in tp["fk_contradicts_naming"]:
            print("  %-46s نام: %-24s کلید خارجی: %s"
                  % (c["col"], c["naming_says"], c["fk_says"]))
        print("")
    if tp.get("twins"):
        print("=== جدول‌های دوقلو — اشتباه گرفتنشان جدولِ خالی می‌دهد ===\n")
        for tw in tp["twins"]:
            cnt = "، ".join("%s=%s" % (m, tables.get(m, {}).get("rows", "?"))
                            for m in tw["pair"])
            print("  %-56s [%s]  %s"
                  % ("  ⟷  ".join(tw["pair"]), tw.get("confidence", "?"), cnt))
        print("")
    if tp.get("misleading_satr"):
        print("=== سطری که زیرِ سربرگِ هم‌نامش نیست ===\n")
        for m in tp["misleading_satr"]:
            print("  %-34s انتظار: %-26s واقعاً: %s"
                  % (m["table"], m["expected_parent"], m["actual_parent"]))
        print("")
    if tp.get("type_mismatch"):
        print("=== ناسازگاری نوع ===\n")
        for x in tp["type_mismatch"]:
            print("  %-52s %-10s → %s" % (x["col"], x["declared"], x["target"]))
        print("")
    if tp.get("width_mismatch"):
        print("=== عرضِ ناسازگار ===\n")
        for x in tp["width_mismatch"]:
            print("  %-48s %-8s → %-8s %s"
                  % (x["child"], x["child_type"], x["parent_type"], x.get("note", "")))
        print("")
    dead = tp.get("dead_columns", {}).get("by_table", {})
    if dead:
        print("=== ستون‌های مرده ===\n")
        for t, cols in sorted(dead.items()):
            print("  %-40s %s" % (t, "، ".join(cols)))
        print("")
    if tp.get("begin_date_tables"):
        print("=== ستون شروع FromDate نیست ===\n  %s\n"
              % "، ".join(tp["begin_date_tables"]))
    if tp.get("end_date_not_null"):
        print("=== EndDate تهی‌پذیر نیست ===\n  %s\n"
              % "، ".join(tp["end_date_not_null"]))
    legacy = sorted(t for t, m in tables.items() if "legacy" in m.get("flags", []))
    if legacy:
        print("=== میراث — منبع حقیقت نیستند ===\n  %s" % "، ".join(legacy))
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


COMMANDS = {"table": cmd_table, "refs": cmd_refs, "path": cmd_path,
            "find": cmd_find, "domain": cmd_domain, "external": cmd_external,
            "traps": cmd_traps,
            "drift": cmd_drift}


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    if argv[0] not in COMMANDS:
        return err("دستور «%s» نیست." % argv[0])
    return COMMANDS[argv[0]](load(), argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
