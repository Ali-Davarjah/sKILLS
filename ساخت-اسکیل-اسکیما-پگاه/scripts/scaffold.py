#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
از schema.json دو چیز می‌سازد: سند دانش، و اسکلتِ اسکیل.

    python scaffold.py readme schema.json --out "Sales Map.md"
    python scaffold.py skill  schema.json --out ../تسلط-فروش-پگاه --name تسلط-فروش-پگاه

هیچ‌کدام از خروجی‌ها **تمام‌شده نیستند**. هرجا `<!-- TODO -->` هست یعنی آنجا
قضاوت لازم است و ماشین نباید جایش تصمیم بگیرد. `references/authoring.md`
می‌گوید هرکدام را چطور پر کنی.
"""

import argparse
import io
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict

for _s in ("stdout", "stderr"):
    _st = getattr(sys, _s, None)
    if _st is not None and hasattr(_st, "reconfigure"):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass

TODO = "<!-- TODO -->"
ROLE_SUFFIXES = ("_Link", "_Old", "_OLD", "_Jadid", "_Asli", "_Movaghat",
                 "_SabtKonandeh", "_Zamen", "_Bimar", "_Mabda", "_Maghsad",
                 "_RoozTatil", "_Next", "_Hoghogh", "_Bimeh", "_Maliat",
                 "_Eydi", "_Parent", "_Sabegh")


def load(path):
    with io.open(path, encoding="utf-8") as fh:
        return json.load(fh)


def resolve(cc, tables):
    if not cc.startswith("cc") or len(cc) < 4:
        return None
    base = cc[2:]
    if base in tables:
        return base
    for suf in ROLE_SUFFIXES:
        if base.endswith(suf) and base[: -len(suf)] in tables:
            return base[: -len(suf)]
    low = {t.lower(): t for t in tables}
    return low.get(base.lower())


def edges_of(data):
    tables = data["tables"]
    out = []
    for name, meta in tables.items():
        for cc in meta.get("cc", []):
            tgt = resolve(cc, tables)
            if tgt and tgt != name:
                out.append((name, cc, tgt))
    return out


def incoming_of(data):
    return Counter(t for _, _, t in edges_of(data))


def by_domain(data):
    groups = defaultdict(list)
    for name, meta in data["tables"].items():
        groups[meta.get("domain", "other")].append(name)
    return {k: sorted(v) for k, v in groups.items()}


def flag(meta, f):
    return f in meta.get("flags", [])


# ============================================================ سند دانش

def render_readme(data, schema_name):
    tables = data["tables"]
    inc = incoming_of(data)
    edges = edges_of(data)
    groups = by_domain(data)
    domains = data.get("domains", {})
    nfk = data["meta"].get("foreign_keys_declared", 0)
    L = []
    a = L.append

    a("# `%s` Schema — پایگاه دانش عامل هوشمند\n" % schema_name)
    a("> **هدف:** مستندات پایه‌ی دیتابیس/کسب‌وکار برای عاملی که روی اسکیمای "
      "زنده‌ی `%s` کار می‌کند." % schema_name)
    a("> **منبع:** درون‌نگری مستقیم دیتابیس (`references/introspection.md`).")
    a("> **کلید خارجی اعلام‌شده:** %d\n" % nfk)

    a("## ۰. قاعده‌های تفسیر — قبل از هر کوئری\n")
    a("۱. **نام اسکیما اجباری است.** `[%s].[TableName]`." % schema_name)
    a("۲. **`ccX` شناسه‌ی نوع‌دار است، نه عدد.** `ccA` هیچ‌وقت با `ccB` مقایسه "
      "نمی‌شود، حتی اگر عددهایشان بخواند.")
    a("۳. **قاعده‌ی اتصال:** اگر `A.ccB` هست و جدول `B` هم هست، حدسِ اول "
      "`A.ccB = B.ccB` است.")
    if nfk == 0:
        a("۴. **این اسکیما کلید خارجی ندارد.** پس همه‌ی %d اتصالِ زیر **حدس** "
          "است. قبل از هر جواب مهم اعتبارسنجی کن." % len(edges))
    else:
        a("۴. **%d اتصال با کلید خارجی اثبات شده‌اند** و بقیه حدسِ هم‌نامی‌اند. "
          "ستون «اثبات» در بخش ۶ تفکیک می‌کند." % nfk)
    a("۵. **بازه‌ی اعتبار.** جدولِ `FromDate`/`EndDate`دار سطرش بازه است؛ "
      "«آخرین سطر» با «سطر فعلی» یکی نیست.")
    a("۶. **وضعیت.** `CodeVazeiat` باید فیلتر شود و کدها **بین جدول‌ها یکسان "
      "نیستند**؛ هر دامنه `X_CodeVazeiat` خودش را دارد.")
    a("۷. **سربرگ/سطر.** `XSatr` معمولاً جزئیاتِ `X` است — با استثناهای بخش ۷.۳.")
    a("۸. **رابطه‌ی نساخته گزارش نکن.** اگر مقصدِ یک `cc` در این اسکیما نیست، "
      "بنویس «بیرونی/حل‌نشده» و جدول از خودت نساز.\n")

    a("## ۱. معماری دامنه در یک نگاه\n")
    a("```text")
    if domains and set(domains) != {"other"}:
        for key, label in domains.items():
            n = len(groups.get(key, []))
            if n:
                a("%-14s %s  (%d جدول)" % (key, label, n))
    else:
        a("%s دامنه‌ها هنوز نام‌گذاری نشده‌اند." % TODO)
    a("```\n")
    a("%s نمودار جریانِ کسب‌وکار را اینجا بنویس: کدام موجودیت به کدام "
      "می‌رسد و چرخه‌ی عمر چیست. این از داده درنمی‌آید.\n" % TODO)

    a("## ۲. نقشه‌ی موجودیت‌ها\n")
    a("| دامنه | جدول‌های اصلی | نقش |")
    a("|---|---|---|")
    for key in (domains or {"other": "other"}):
        members = groups.get(key, [])
        if not members:
            continue
        top = sorted(members, key=lambda t: -inc.get(t, 0))[:4]
        a("| %s | %s | %s |"
          % (domains.get(key, key),
             "، ".join("`%s`" % t for t in top),
             (tables[top[0]].get("role") or TODO) if top else TODO))
    a("")

    a("## ۳. دستگاه نوعِ `cc`\n")
    ccs = set()
    for meta in tables.values():
        ccs.update(meta.get("cc", []))
    a("این اسکیما **%d ستون `cc*`** یکتا در **%d جدول** دارد. قاعده‌ی نام‌گذاری "
      "**%d ارجاع داخلی** و **%d نامِ حل‌نشده/مشترک** می‌دهد.\n"
      % (len(ccs), len(tables), len(edges), len(data.get("external_cc", {}))))

    a("### ۳.۱ موجودیت‌های پرارجاع\n")
    for t, n in inc.most_common(20):
        a("- `%s` — %d ارجاع ورودی%s"
          % (t, n, ("  — %s" % tables[t]["role"]) if tables[t].get("role") else ""))
    a("")
    a("### ۳.۲ واژگان مشترک/بیرونی\n")
    a("اینها در این اسکیما جدول ندارند. **جدول محلی برایشان نساز.**\n")
    a("| `cc` | تکرار | تفسیر |")
    a("|---|---:|---|")
    for cc, m in list(data.get("external_cc", {}).items())[:40]:
        a("| `%s` | %s | %s |" % (cc, m.get("count", "?"), m.get("note") or TODO))
    a("")

    a("## ۴. فرهنگ جدول‌ها\n")
    for key in (domains or {"other": "other"}):
        members = groups.get(key, [])
        if not members:
            continue
        a("### %s\n" % domains.get(key, key))
        for t in sorted(members, key=lambda x: -inc.get(x, 0)):
            meta = tables[t]
            if flag(meta, "legacy"):
                continue
            bits = []
            if meta.get("pk"):
                bits.append("کلید `%s`" % meta["pk"])
            if meta.get("rows") is not None:
                bits.append("%s سطر" % meta["rows"])
            marks = [f for f in ("effective_dated", "status_header", "detail",
                                 "ledger", "tree", "dict", "migration",
                                 "sensitive", "empty")
                     if flag(meta, f)]
            if marks:
                bits.append("، ".join(marks))
            a("- **`%s`** — %s  \n  %s"
              % (t, meta.get("role") or TODO, "؛ ".join(bits)))
        a("")

    a("## ۵. فهرست اتصال‌های داخلی\n")
    a("| مبدأ | ستون | مقصد | اثبات |")
    a("|---|---|---|---|")
    proven = set()
    for tr in data["traps"].get("fk_contradicts_naming", []):
        proven.add(tr["col"])
    for s, cc, t in sorted(edges):
        a("| `%s` | `%s` | `%s` | %s |"
          % (s, cc, t, "کلید خارجی" if nfk else "هم‌نامی"))
    a("")

    a("## ۶. تله‌ها\n")
    tp = data["traps"]
    if tp.get("fk_contradicts_naming"):
        a("### ۶.۰ کلید خارجی با نام‌گذاری نمی‌خواند — مهم‌ترین بخش\n")
        a("| ستون | نام می‌گوید | کلید خارجی می‌گوید |")
        a("|---|---|---|")
        for c in tp["fk_contradicts_naming"]:
            a("| `%s` | %s | **%s** |" % (c["col"], c["naming_says"], c["fk_says"]))
        a("")
    if tp.get("twins"):
        a("### ۶.۱ جدول‌های دوقلو\n")
        a("اشتباه گرفتنشان خطا نمی‌دهد — **جدولِ خالی می‌دهد**.\n")
        a("| نامزدها | اطمینان | سطرها |")
        a("|---|---|---|")
        for tw in tp["twins"]:
            cnt = "، ".join("%s=%s" % (m, tables.get(m, {}).get("rows", "?"))
                            for m in tw["pair"])
            a("| %s | %s | %s |" % ("  ⟷  ".join("`%s`" % m for m in tw["pair"]),
                                    tw.get("confidence", ""), cnt))
        a("")
    if tp.get("misleading_satr"):
        a("### ۶.۲ سطری که زیرِ سربرگِ هم‌نامش نیست\n")
        a("| جدول | با اسمش انتظار داری زیرِ | واقعاً زیرِ |")
        a("|---|---|---|")
        for m in tp["misleading_satr"]:
            a("| `%s` | `%s` | **`%s`** |"
              % (m["table"], m["expected_parent"], m["actual_parent"]))
        a("")
    if tp.get("type_mismatch"):
        a("### ۶.۳ ناسازگاری نوع\n")
        a("| ستون | نوع اعلام‌شده | مقصد |")
        a("|---|---|---|")
        for x in tp["type_mismatch"]:
            a("| `%s` | `%s` | `%s` |" % (x["col"], x["declared"], x["target"]))
        a("")
    if tp.get("width_mismatch"):
        a("### ۶.۴ عرضِ ناسازگار\n")
        a("| فرزند | نوع | والد | نوع | خطر |")
        a("|---|---|---|---|---|")
        for x in tp["width_mismatch"]:
            a("| `%s` | `%s` | `%s` | `%s` | %s |"
              % (x["child"], x["child_type"], x["parent"], x["parent_type"],
                 x.get("note", "")))
        a("")
    dead = tp.get("dead_columns", {}).get("by_table", {})
    if dead:
        a("### ۶.۵ ستون‌های مرده\n")
        for t, cols in sorted(dead.items()):
            a("- `%s`: %s" % (t, "، ".join("`%s`" % c for c in cols)))
        a("")
    if tp.get("begin_date_tables"):
        a("### ۶.۶ ستون شروع `FromDate` نیست\n")
        a("`" + "`، `".join(tp["begin_date_tables"]) + "`\n")
    if tp.get("end_date_not_null"):
        a("### ۶.۷ `EndDate` تهی‌پذیر نیست — الگوی `IS NULL` کار نمی‌کند\n")
        a("`" + "`، `".join(tp["end_date_not_null"]) + "`\n")

    a("## ۷. معنای کسب‌وکاری\n")
    a("%s این بخش از داده درنمی‌آید. بنویس: داده‌ی مرجع در برابر "
      "تراکنشی، لایه‌ی تعریف در برابر نتیجه، قاعده‌ی بازه‌ی اعتبار، و واحدِ "
      "مبالغ.\n" % TODO)

    a("## ۸. دستورالعمل عامل\n")
    a("```text\nسؤال → موجودیت کسب‌وکاری → جدول مرجع → مسیر cc →\n"
      "منطق بازه/دوره → فیلتر وضعیت → تجمیع در دانه‌ی درست → اعتبارسنجی\n```\n")
    a("**قبل از هر `SUM` دانه را بشمار.** این اسکیما پر از یک‌به‌چند است.\n")

    a("## ۹. محدودیت‌های شناخته‌شده\n")
    if nfk == 0:
        a("- **کلید خارجی وجود ندارد.** همه‌ی اتصال‌ها از نام حدس زده شده‌اند.")
    a("- نقشِ جدول‌هایی که `role` خالی دارند نوشته نشده است.")
    empt = [t for t, m in tables.items() if m.get("rows") == 0]
    if empt:
        a("- **%d جدول خالی‌اند** — یا مرده‌اند یا ماژولشان استفاده نمی‌شود." % len(empt))
    a("- تفسیر ارجاع‌های بیرونی تأیید نشده است.")
    return "\n".join(L) + "\n"


# ============================================================ اسکلت اسکیل

def render_skill_md(data, schema_name, skill_name):
    tables = data["tables"]
    inc = incoming_of(data)
    tp = data["traps"]
    nfk = data["meta"].get("foreign_keys_declared", 0)
    top = inc.most_common(1)
    anchor = top[0][0] if top else "؟"
    L = []
    a = L.append

    a("---")
    a("name: %s" % skill_name)
    a("description: نقشه‌ی اسکیمای %s — %s TODO: دامنه‌ها و کلیدواژه‌های "
      "فارسی و انگلیسی را اینجا بنویس تا اسکیل درست بارگذاری شود."
      % (schema_name, TODO))
    a("---\n")
    a("# %s\n" % skill_name)
    a("**%d جدول، %d کلید خارجی اعلام‌شده.** این اسکیل نقشه است: از کجا شروع "
      "کنی، چه چیزی به چه چیزی وصل است، و کدام تله‌ها وقت می‌خورند.\n"
      % (len(tables), nfk))

    if nfk == 0:
        a("> **این اسکیما کلید خارجی ندارد.** همه‌ی اتصال‌ها از **هم‌نامی** حدس "
          "زده شده‌اند. قبل از هر جواب مهم، بخش ۰ "
          "[queries.md](references/queries.md) را بزن.\n")
    else:
        a("> **%d اتصال کلید خارجی واقعی دارند و بقیه حدسِ هم‌نامی‌اند.** "
          "`hr_map`/`map.py` با `proven` تفکیک می‌کند.\n" % nfk)

    a("> **`ccX` عدد نیست، شناسه‌ی نوع‌دار است.** قاعده‌ی اتصال: اگر `A.ccB` "
      "هست و جدول `B` هم هست، حدسِ اول `A.ccB = B.ccB` است.\n")

    if tp.get("twins"):
        names = "، ".join("`%s`/`%s`" % (t["pair"][0], t["pair"][1])
                          for t in tp["twins"][:3] if len(t["pair"]) == 2)
        a("> **جدول‌های دوقلو.** %s و بقیه در "
          "[relationships.md](references/relationships.md). اشتباه گرفتنشان "
          "خطا نمی‌دهد — جدولِ **خالی** می‌دهد.\n" % names)

    if tp.get("misleading_satr"):
        m = tp["misleading_satr"][0]
        a("> **`XSatr` همیشه زیرِ `X` نیست.** `%s` زیرِ `%s` است، نه `%s`.\n"
          % (m["table"], m["actual_parent"], m["expected_parent"]))

    a("> **بودنِ ردیف یعنی ثبت شده، نه معتبر.** `CodeVazeiat` را فیلتر کن و "
      "کدها را از `X_CodeVazeiat` بخوان — بین جدول‌ها یکسان نیستند.\n")

    a("%s بلوک‌های هشدارِ مخصوصِ این اسکیما را اینجا اضافه کن: "
      "لایه‌ی تعریف در برابر نتیجه، واحدِ مبالغ، هر چیزی که یک بار وقت گرفت.\n"
      % TODO)

    a("## ترتیب کار\n")
    a("۱. **اول تأیید، بعد جواب.** بخش ۰ [queries.md](references/queries.md).")
    a("۲. **سؤال را به یک دامنه ببند** — جدول «نقشه‌ی دامنه» پایین.")
    a("۳. **جنس سؤال را تعیین کن:** لحظه‌ای، دوره‌ای، یا وضع فعلی.")
    a("۴. **مسیر اتصال را بساز** با `scripts/map.py path <A> <B>`.")
    a("۵. **بازه و وضعیت را با هم اعمال کن.**")
    a("۶. **دانه را بشمار، بعد جمع بزن.**")
    a("۷. **گزارش بده** — [reporting.md](references/reporting.md).\n")

    a("## نقشه‌ی دامنه — از کجا شروع کنی\n")
    a("| سؤال | جدول شروع | نکته |")
    a("|---|---|---|")
    for t, n in inc.most_common(12):
        a("| %s | `%s` | %s |" % (TODO, t, tables[t].get("role") or TODO))
    a("\n`%s` مرکز ثقل است (%d ارجاع ورودی).\n" % (anchor, inc.get(anchor, 0)))

    a("## قاعده‌های خواندن این اسکیما\n")
    a("### بازه‌ی اعتبار\n")
    a("```sql\nWHERE [FromDate] <= @AsOfDate\n"
      "  AND ([EndDate] IS NULL OR [EndDate] > @AsOfDate)\n```\n")
    if tp.get("begin_date_tables"):
        a("**ستون شروع همیشه `FromDate` نیست** — در `%s` ستون `BeginDate` است.\n"
          % "`، `".join(tp["begin_date_tables"][:6]))
    if tp.get("end_date_not_null"):
        a("**و `EndDate` همیشه تهی‌پذیر نیست** — در `%s` الگوی `IS NULL` جواب "
          "نمی‌دهد.\n" % "`، `".join(tp["end_date_not_null"][:6]))

    a("### وضعیت — سه لایه\n")
    a("- `X.CodeVazeiat` وضعیت فعلی روی سربرگ.")
    a("- `X_CodeVazeiat` دیکشنری کدها — `NameVazeiat` را از همین بخوان.")
    a("- `X_Vazeiat` تاریخچه — برای فیلتر به سربرگ join نکن مگر با `TOP 1`.\n")

    a("### دانه\n")
    a("**هیچ‌وقت دو جدول `Satr` را به یک سربرگ join نکن و بعد جمع بزن.**\n")

    a("## سؤال‌های باز — از کارشناس بپرس، خودت تصمیم نگیر\n")
    a("%s این بخش را از `findings.md` پر کن. **همه را با هم نپرس.**\n"
      % TODO)
    if tp.get("twins"):
        a("### الف) کدام جهانِ دوقلو زنده است\n")
        a("تعداد سطر و آخرین تاریخِ هر جفت را بگیر، نشان بده، و بپرس کدام مرجع "
          "است. عدد می‌گوید کدام پرکارتر است، نه کدام درست.\n")

    a("## وقتی داده‌ای نیست\n")
    a("فرقِ «جدول نیست»، «ستون نیست»، «بازه ردیف ندارد» و «معیار داده ندارد» را "
      "نگه دار. **با تخمین پر نکن** و **جدول از خودت نساز**.\n")

    a("## فایل‌های این اسکیل\n")
    a("- [references/queries.md](references/queries.md) — **اول این.**")
    a("- [references/entities.md](references/entities.md) — دامنه به دامنه.")
    a("- [references/relationships.md](references/relationships.md) — گراف و تله‌ها.")
    a("- [references/reporting.md](references/reporting.md) — شکل گزارش.")
    a("- `schema.json` — نقشه‌ی ماشین‌خوان. داده است، نه کد.")
    a("- `scripts/map.py` — پیمایش نقشه. اجرا کن، نخوان.")
    return "\n".join(L) + "\n"


def render_entities(data, schema_name):
    tables, inc = data["tables"], incoming_of(data)
    groups, domains = by_domain(data), data.get("domains", {})
    L = ["# موجودیت‌ها، دامنه به دامنه\n",
         "برای هر دامنه: جدول مرجع، ستون‌های لازم، **دانه‌ی هر سطر**، و آنچه "
         "اسم جدول نمی‌گوید.\n",
         "پیشوند اسکیما لازم است: `[%s].[TableName]`.\n" % schema_name,
         "%s برای هر جدولِ مهم یک جمله نقش بنویس و دانه‌اش را مشخص کن.\n"
         % TODO]
    for key in (domains or {"other": "other"}):
        members = groups.get(key, [])
        if not members:
            continue
        L.append("---\n\n## %s\n" % domains.get(key, key))
        L.append("| جدول | کلید | سطر | نشانه‌ها | نقش |")
        L.append("|---|---|---:|---|---|")
        for t in sorted(members, key=lambda x: -inc.get(x, 0)):
            m = tables[t]
            marks = [f for f in m.get("flags", []) if not f.startswith("nonstandard")]
            L.append("| `%s` | `%s` | %s | %s | %s |"
                     % (t, m.get("pk") or "؟", m.get("rows", "?"),
                        "، ".join(marks) or "—", m.get("role") or "—"))
        L.append("")
    return "\n".join(L) + "\n"


def render_relationships(data, schema_name):
    tables, inc, edges = data["tables"], incoming_of(data), edges_of(data)
    tp = data["traps"]
    nfk = data["meta"].get("foreign_keys_declared", 0)
    L = ["# اتصال‌ها، واژگان مشترک، و تله‌ها\n",
         "```\nاگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB\n```\n"]
    L.append(("**هیچ‌کدام اثبات‌شده نیست** — این اسکیما کلید خارجی ندارد.\n"
              if nfk == 0 else
              "**%d یال کلید خارجی واقعی دارند**؛ بقیه حدس‌اند.\n" % nfk))
    L.append("## مرکزهای ثقل\n")
    L.append("| موجودیت | ارجاع ورودی | نقش |")
    L.append("|---|---:|---|")
    for t, n in inc.most_common(15):
        L.append("| `%s` | %d | %s |" % (t, n, tables[t].get("role") or "—"))
    L.append("\n## ارجاع‌های بیرونی\n")
    L.append("| `cc` | تکرار | تفسیر |")
    L.append("|---|---:|---|")
    for cc, m in list(data.get("external_cc", {}).items())[:40]:
        if m.get("resolves_to"):
            tafsir = "✔ `%s`%s" % (m["resolves_to"],
                                   ("  — " + m["note"]) if m.get("note") else "")
        else:
            tafsir = m.get("note") or "حل‌نشده — در هیچ اسکیمای این دیتابیس نیست"
        L.append("| `%s` | %s | %s |" % (cc, m.get("count", "?"), tafsir))
    L.append("")
    L.append("✔ یعنی جدولِ هم‌نام در آن اسکیما **وجود دارد**. مقصد قطعی")
    L.append("است؛ خوردنِ ستون‌ها هنوز آزمونِ یتیم می‌خواهد.")
    L.append("\n## تله‌ها\n")
    L.append("`python scripts/map.py traps` همه را می‌دهد. خلاصه:\n")
    L.append("- دوقلو: **%d** جفت" % len(tp.get("twins", [])))
    L.append("- سطرِ با پدرِ غیرمنتظره: **%d**" % len(tp.get("misleading_satr", [])))
    L.append("- ناسازگاری نوع: **%d**" % len(tp.get("type_mismatch", [])))
    L.append("- عرضِ ناسازگار: **%d**" % len(tp.get("width_mismatch", [])))
    L.append("- جدول با ستون مرده: **%d**\n"
             % len(tp.get("dead_columns", {}).get("by_table", {})))
    L.append("## فهرست کامل اتصال‌ها\n")
    L.append("| مبدأ | ستون | مقصد |")
    L.append("|---|---|---|")
    for s, cc, t in sorted(edges):
        L.append("| `%s` | `%s` | `%s` |" % (s, cc, t))
    return "\n".join(L) + "\n"


QUERIES_TMPL = """# کوئری‌ها

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود. پارامترها را با `params` بساز.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** در SQL جمع بزن.

## ۰. تأیید — قبل از هر چیز

### ۰.۱ جدول‌ها و تعداد سطر
```sql
SELECT s.name AS schema_name, t.name AS table_name, SUM(p.rows) AS row_count
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
JOIN sys.partitions AS p ON p.object_id = t.object_id AND p.index_id IN (0,1)
WHERE s.name = '{schema}'
GROUP BY s.name, t.name
ORDER BY row_count DESC;
```

### ۰.۲ دنبال یک اسم بگرد
```sql
WITH params AS (SELECT N'%TODO%' AS alago)
SELECT s.name AS schema_name, t.name AS table_name
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
CROSS JOIN params AS p
WHERE t.name LIKE p.alago
ORDER BY s.name, t.name;
```

### ۰.۳ ستون‌های یک جدول
```sql
WITH params AS (SELECT N'TODO' AS jadval)
SELECT c.COLUMN_NAME, c.DATA_TYPE, c.IS_NULLABLE, c.ORDINAL_POSITION
FROM INFORMATION_SCHEMA.COLUMNS AS c
CROSS JOIN params AS p
WHERE c.TABLE_SCHEMA = '{schema}' AND c.TABLE_NAME = p.jadval
ORDER BY c.ORDINAL_POSITION;
```

### ۰.۴ کلید خارجی واقعی — اگر بود، حرف آخر است
```sql
SELECT OBJECT_NAME(fkc.parent_object_id) AS ParentTable, pc.name AS ParentColumn,
       OBJECT_NAME(fkc.referenced_object_id) AS RefTable, rc.name AS RefColumn
FROM sys.foreign_key_columns AS fkc
JOIN sys.columns AS pc ON pc.object_id = fkc.parent_object_id
                      AND pc.column_id = fkc.parent_column_id
JOIN sys.columns AS rc ON rc.object_id = fkc.referenced_object_id
                      AND rc.column_id = fkc.referenced_column_id
WHERE OBJECT_SCHEMA_NAME(fkc.parent_object_id) = '{schema}'
ORDER BY ParentTable, ParentColumn;
```

### ۰.۵ دیکشنری وضعیت — قبل از هر فیلترِ وضعیت
```sql
SELECT CodeVazeiat, NameVazeiat FROM [{schema}].[TODO_CodeVazeiat]
ORDER BY CodeVazeiat;
```

{twin_block}
## ۱. الگوهای دامنه

<!-- TODO --> برای هر سؤال پرتکرار یک کوئری بنویس و **تست‌شده** علامت بزن.
هر کوئری باید: بلوک `params` داشته باشد، بازه و وضعیت را فیلتر کند، و در
دانه‌ی درست تجمیع کند.

## ۹. کیفیت داده

### ۹.۱ ارجاعِ یتیم
```sql
SELECT COUNT(*) AS tedad_yatim
FROM [{schema}].[CHILD] AS c
LEFT JOIN [{schema}].[PARENT] AS p ON p.KEY = c.KEY
WHERE p.KEY IS NULL;
```
عددِ غیرصفر یعنی اتصال حدسی درست نیست یا داده ناسازگار است. **این را روی
پرترافیک‌ترین یال‌ها بزن؛ همین اعتبارسنجیِ نقشه است.**

### ۹.۲ بازه‌های هم‌پوشان
<!-- TODO --> روی جدول‌های بازه‌دار.

## اندازه‌ها

بار اول که روی داده‌ی زنده اجرا کردی، عددهای مرجع را اینجا بنویس تا دفعه‌ی
بعد معیار داشته باشی.

| اندازه | مقدار |
|---|---|
| <!-- TODO --> | ؟ |
"""


def render_queries(data, schema_name):
    tp = data["traps"]
    tw = ""
    if tp.get("twins"):
        rows = "\nUNION ALL ".join(
            "SELECT '%s' AS jadval, COUNT(*) AS tedad FROM [%s].[%s]"
            % (m, schema_name, m)
            for t in tp["twins"][:6] for m in t["pair"])
        tw = ("### ۰.۶ جدول‌های دوقلو — کدام زنده است\n```sql\n%s\nORDER BY "
              "tedad DESC;\n```\n\nتعداد کافی نیست؛ `MAX(تاریخ)` را هم بگیر.\n"
              % rows)
    return QUERIES_TMPL.format(schema=schema_name, twin_block=tw)


REPORTING_TMPL = """# گزارش

## هرچه گزارش می‌دهی، اینها را کنارش بگذار

۱. **تاریخ یا دوره‌ی دقیق** — و اگر تاریخ‌ها میلادی‌اند، معادل شمسی را هم بنویس.
۲. **جنسِ سؤال** — لحظه‌ای، دوره‌ای، یا وضع فعلی.
۳. **دامنه** — کدام مرکز/واحد، و چه چیزی فیلتر شده.
۴. **از کدام جدول‌ها** — در اسکیمایی که جدول دوقلو دارد، این حیاتی است.
۵. **فیلترِ وضعیت** — کدام `CodeVazeiat` نگه داشته شد و از کدام دیکشنری.
۶. **چه چیزی تأیید شده و چه چیزی حدس.**

## بگو کدام قسمت روی حدس ایستاده

- **تأیید‌شده** — کوئری زده شد و جواب داد.
- **فرض‌شده** — اتصال از هم‌نامی حدس زده شد و نتیجه معقول بود.
- **تأیید‌نشده** — لازم بود ولی فرصت نبود.

**عددِ یتیم‌ها را همیشه بنویس.** «۴۱۸ از ۴۲۰» اطلاعات است؛ «۴۱۸ نفر» نیست.

## هر جدول ستون ردیف دارد

بدون آن در جلسه نمی‌شود گفت «سطر هفت».

## دانه را صریح بگو

اگر برای هر کلید بیش از یک سطر بود، بگو با آن چه کردی. این تفاوت بین عدد و
چند برابرِ عدد است.

## وقتی جواب خالی است

۱. آخرین تاریخِ واقعی از `MAX`.
۲. در کدام جدول‌ها گشتی — با نام.
۳. پیشنهاد بعدی.

**حدس را جای کوئری ننشان.**

## وقتی عددها بین دو منبع نمی‌خوانند

هر دو عدد را بنویس و اختلاف را نام ببر. یکی را بی‌صدا انتخاب نکن.

<!-- TODO --> اگر این اسکیما داده‌ی محرمانه دارد (حقوق، کد ملی، سلامت)،
بخش محرمانگی را اینجا اضافه کن: جمعِ گروهی آزاد، سطرِ فردی فقط وقتی خواسته شده.
"""


def cmd_readme(args):
    data = load(args.schema_json)
    name = args.schema or data["meta"].get("schema", "Schema")
    out = args.out or ("%s Map.md" % name)
    with io.open(out, "w", encoding="utf-8") as fh:
        fh.write(render_readme(data, name))
    print("سند دانش → %s" % out)
    return 0


def cmd_skill(args):
    data = load(args.schema_json)
    schema_name = args.schema or data["meta"].get("schema", "Schema")
    skill_name = args.name or os.path.basename(os.path.abspath(args.out))
    root = args.out
    for sub in ("references", "scripts", "examples"):
        os.makedirs(os.path.join(root, sub), exist_ok=True)

    def w(rel, text):
        with io.open(os.path.join(root, rel), "w", encoding="utf-8") as fh:
            fh.write(text)

    w("SKILL.md", render_skill_md(data, schema_name, skill_name))
    w("references/entities.md", render_entities(data, schema_name))
    w("references/relationships.md", render_relationships(data, schema_name))
    w("references/queries.md", render_queries(data, schema_name))
    w("references/reporting.md", REPORTING_TMPL)
    w("examples/walkthrough.md",
      "# یک سؤال واقعی، از اول تا آخر\n\n%s یک سؤالِ واقعی را از "
      "تأیید تا گزارش دنبال کن. نشان بده کدام تصمیم کجا گرفته شد، چه چیزی "
      "پرسیده شد و چه چیزی نه.\n" % TODO)
    w("README.md",
      "# %s\n\nاسکیل تسلط بر اسکیمای `%s`.\n\n"
      "%s ساختار، نگاشت داده، تله‌ها، ایمپورت، و آنچه باید با کارشناس "
      "چک شود.\n\n"
      "ساخته‌شده با `ساخت-اسکیل-اسکیما-پگاه` از درون‌نگری زنده.\n"
      % (skill_name, schema_name, TODO))

    shutil.copyfile(args.schema_json, os.path.join(root, "schema.json"))
    tmpl = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        os.pardir, "templates", "map.py")
    if os.path.exists(tmpl):
        shutil.copyfile(tmpl, os.path.join(root, "scripts", "map.py"))

    print("اسکلت اسکیل → %s" % root)
    print("\nحالا `%s` را در همه‌ی فایل‌ها پیدا کن و پر کن." % TODO)
    print("`references/authoring.md` می‌گوید هرکدام را چطور.")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("readme")
    r.add_argument("schema_json")
    r.add_argument("--out")
    r.add_argument("--schema")
    r.set_defaults(fn=cmd_readme)
    s = sub.add_parser("skill")
    s.add_argument("schema_json")
    s.add_argument("--out", required=True)
    s.add_argument("--schema")
    s.add_argument("--name")
    s.set_defaults(fn=cmd_skill)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
