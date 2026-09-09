#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
پیوندِ خانوادگیِ اسکیل‌های نقشه — چند `schema.json` را کنار هم می‌گذارد و
چیزی را حل می‌کند که هیچ‌کدام به‌تنهایی نمی‌توانند.

    python crosslink.py report <root>            # فقط چاپ می‌کند، چیزی نمی‌نویسد
    python crosslink.py index  <root> [--out skills-index.json]
    python crosslink.py apply  <root>            # cc_resolution را در هر schema.json می‌نویسد

سه چیز که با یک اسکیمای تنها به دست نمی‌آید:

۱. **ارجاعِ نقش‌دار.** `ccAfradForoshandeh` جدولی به این نام ندارد، ولی
   `Afrad` دارد و بقیه‌اش نقش است. با فهرستِ جدولِ همه‌ی اسکیماها این را
   می‌شود دید؛ با یکی نه.
۲. **ارجاعِ واقعاً بی‌مقصد.** وقتی هیچ‌کدام از اسکیماهای نقشه‌شده جدولش را
   ندارند، «بیرونی» درست است — و شمارشِ خانوادگی‌اش می‌گوید چقدر مهم است.
۳. **ارجاعِ دوپهلو.** یک `cc` که در دو اسکیما جدولِ هم‌نام دارد.

خروجی همیشه **نامزد** است، نه واقعیت. `confidence: LOW` یعنی از نام درآمده.
"""

import io
import json
import os
import sys
from collections import defaultdict

for _s in ("stdout", "stderr"):
    _st = getattr(sys, _s, None)
    if _st is not None and hasattr(_st, "reconfigure"):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass

MIN_BASE = 4          # کوتاه‌تر از این پیشوند، هم‌نامیِ تصادفی است
MIN_ROLE = 1

# ارجاع‌هایی که معنایشان از سند دانش می‌آید، نه از نام.
DOCUMENTED = {
    "ccNoeMoshtary": {
        "target": "Global.Goroh",
        "filter": "ccGorohLink = 304",
        "note": "نوع مشتری جدول جدا ندارد — سطرهای Goroh با ccGorohLink = 304 "
                "است (خرده، عمده، زنجیره‌ای…).",
    },
    "ccGorohKala": {
        "target": "Global.Goroh",
        "filter": "ccGorohLink = 560",
        "note": "گروه کالا سطرهای Goroh با ccGorohLink = 560 است (۵۵ گروه). "
                "vGorohMahsol فقط ۳۳ تا را دارد — از آن استفاده نکن.",
    },
    "ccElatMarjoeeKala": {
        "target": "Warehouse.ElatMarjoeeKala",
        "filter": "MasoleiatElat = 1 برای مرجوعیِ مسئولیتِ فروش",
        "note": "علتِ مرجوعی و مسئولیتش. اسکیل ارزیابی فروشنده روی همین می‌نشیند.",
    },
}


def load_family(root):
    fam = {}
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name, "schema.json")
        if not os.path.exists(path):
            continue
        with io.open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        schema = data.get("meta", {}).get("schema")
        if not schema:
            continue
        fam[schema] = {"skill": name, "path": path, "data": data}
    return fam


def owners(fam):
    """نام جدول → فهرست اسکیماهایی که آن را دارند."""
    out = defaultdict(list)
    for schema, e in fam.items():
        for t in e["data"]["tables"]:
            out[t].append(schema)
    return out


def role_split(base, owned, home):
    """بلندترین پیشوندی که نام جدول باشد، و بقیه‌اش نقش."""
    best = None
    for t in owned:
        if len(t) < MIN_BASE or t == base or not base.startswith(t):
            continue
        role = base[len(t):]
        if len(role) < MIN_ROLE:
            continue
        # مرزِ نقش باید دیده شود، وگرنه Mahal + "eh" هم قبول می‌شود.
        if not (role[0] == "_" or role[0].isupper() or role[0].isdigit()):
            continue
        if best is None or len(t) > len(best[0]):
            best = (t, role)
    if best is None:
        return None
    table, role = best
    schema = home if home in owned[table] else owned[table][0]
    return schema + "." + table, role, len(owned[table]) > 1


def resolve(fam):
    owned = owners(fam)
    per = {}
    family_unresolved = defaultdict(int)
    family_where = defaultdict(list)
    for schema, e in fam.items():
        data = e["data"]
        ext = data.get("external_cc", {})
        cross = data.get("cross_schema", {})
        already = {k.split(".", 1)[1] for k in cross if "." in k}
        role_q, documented, ambiguous, unresolved = {}, {}, {}, {}
        for cc, info in sorted(ext.items()):
            count = info.get("count", 0)
            base = cc[2:] if cc.startswith("cc") else cc
            if cc in DOCUMENTED:
                documented[cc] = dict(DOCUMENTED[cc], count=count,
                                      evidence="DOCUMENTED", confidence="MEDIUM")
                continue
            picked = info.get("resolves_to")
            if base in owned:
                homes = list(owned[base])
                if picked and picked not in [s + "." + base for s in homes]:
                    # سازنده مقصدی بیرونِ خانواده انتخاب کرده، ولی جدولِ
                    # هم‌نام داخلِ خانواده هم هست. این خطرناک‌ترین حالت است.
                    homes_full = sorted(s + "." + base for s in homes)
                    ambiguous[cc] = {
                        "count": count,
                        "picked_by_builder": picked,
                        "candidates": [picked] + homes_full,
                        "evidence": "NAME_MATCH_OUTSIDE_AND_INSIDE_FAMILY",
                        "confidence": "LOW",
                        "note": "سازنده %s را برداشت چون اول در فهرست بود؛ "
                                "%s هم جدولِ هم‌نام دارد. کدام درست است از "
                                "داده تأیید بگیر."
                                % (picked, "، ".join(homes_full)),
                    }
                elif len(homes) > 1:
                    ambiguous[cc] = {
                        "count": count,
                        "candidates": sorted(s + "." + base for s in homes),
                        "evidence": "MULTI_SCHEMA_NAME_MATCH",
                        "confidence": "LOW",
                        "note": "بیش از یک اسکیما جدولِ هم‌نام دارد — "
                                "قبل از join تعیین کن کدام.",
                    }
                continue
            if base in already:
                continue
            hit = role_split(base, owned, schema)
            if hit:
                target, role, multi = hit
                role_q[cc] = {
                    "count": count,
                    "target": target,
                    "role": role.lstrip("_"),
                    "evidence": "ROLE_QUALIFIED_PREFIX",
                    "confidence": "LOW",
                }
                if multi:
                    role_q[cc]["note"] = "نام جدول در بیش از یک اسکیما هست."
            else:
                unresolved[cc] = count
                family_unresolved[cc] += count
                family_where[cc].append(schema)
        per[schema] = {"role_qualified": role_q, "documented": documented,
                       "ambiguous": ambiguous, "unresolved": unresolved}
    return per, family_unresolved, family_where


def matrix(fam):
    out = {}
    for schema, e in fam.items():
        counts = defaultdict(int)
        for target in e["data"].get("cross_schema", {}):
            counts[target.split(".", 1)[0]] += 1
        out[schema] = dict(sorted(counts.items(), key=lambda kv: -kv[1]))
    return out


def build_index(fam, per, family_unresolved, family_where):
    mat = matrix(fam)
    skills = {}
    for schema, e in sorted(fam.items()):
        d = e["data"]
        skills[schema] = {
            "skill": e["skill"],
            "database": d.get("meta", {}).get("database"),
            "tables": len(d.get("tables", {})),
            "views_excluded": len(d.get("views_excluded", []) or []),
            "internal_edges": len(d.get("edges", []) or []),
            "cross_schema_targets": len(d.get("cross_schema", {})),
            "external_cc": len(d.get("external_cc", {})),
            "refers_to": mat.get(schema, {}),
        }
    referred_by = defaultdict(dict)
    for src, targets in mat.items():
        for dst, n in targets.items():
            referred_by[dst][src] = n
    for schema in skills:
        skills[schema]["referred_to_by"] = dict(
            sorted(referred_by.get(schema, {}).items(), key=lambda kv: -kv[1]))
    ordered = sorted(family_unresolved.items(), key=lambda kv: -kv[1])
    unresolved = {cc: {"count": n, "schemas": sorted(set(family_where[cc]))}
                  for cc, n in ordered if n >= 2}
    singles = sorted(cc for cc, n in ordered if n < 2)
    return {
        "generated_by": "ساخت-اسکیل-اسکیما-پگاه/scripts/crosslink.py",
        "note": "نامزد است، نه واقعیت. هر یالِ LOW باید روی دیتابیس زنده "
                "تأیید شود.",
        "schemas": skills,
        "spelling_variants": spelling_variants(fam),
        "unresolved_family": unresolved,
        "unresolved_family_singletons": {
            "count": len(singles),
            "note": "یک‌بارمصرف‌اند و بیشترشان ستونِ جدولِ گزارش‌اند، نه ارجاع.",
            "names": singles,
        },
    }


def spelling_variants(fam):
    """یک شناسه با دو املا — بی‌صداترین خطای این خانواده.

    `ccSazmanForosh` و `ccSazmanforosh` یک چیزند و join روی اشتباهی‌اش
    خطا نمی‌دهد؛ صفر سطر می‌دهد.
    """
    seen = defaultdict(lambda: defaultdict(int))
    for schema, e in fam.items():
        d = e["data"]
        for cc, info in d.get("external_cc", {}).items():
            seen[cc.lower()][cc] += info.get("count", 0)
        for t, meta in d.get("tables", {}).items():
            for cc in meta.get("cc", []):
                seen[cc.lower()].setdefault(cc, 0)
    out = {}
    for key, forms in sorted(seen.items()):
        if len(forms) > 1:
            out[key] = dict(sorted(forms.items(), key=lambda kv: -kv[1]))
    return out


def cmd_report(fam, per, fu, fw):
    idx = build_index(fam, per, fu, fw)
    for schema, s in idx["schemas"].items():
        print("=== %s  (%s)" % (schema, s["skill"]))
        print("    جدول %s | یال داخلی %s | مقصدِ بیرونی %s | ccِ بیرونی %s"
              % (s["tables"], s["internal_edges"], s["cross_schema_targets"],
                 s["external_cc"]))
        print("    به:   ", s["refers_to"])
        print("    از:   ", s["referred_to_by"])
        p = per[schema]
        print("    نقش‌دار %s | مستند %s | دوپهلو %s | بی‌مقصد %s"
              % (len(p["role_qualified"]), len(p["documented"]),
                 len(p["ambiguous"]), len(p["unresolved"])))
        top = sorted(p["role_qualified"].items(),
                     key=lambda kv: -kv[1]["count"])[:6]
        for cc, v in top:
            print("       %-32s x%-4s -> %-30s نقش: %s"
                  % (cc, v["count"], v["target"], v["role"]))
    print()
    print("=== بی‌مقصد در کلِ خانواده (جمعِ ارجاع)")
    for cc, v in list(idx["unresolved_family"].items())[:20]:
        print("    %-28s x%-5s %s" % (cc, v["count"], ",".join(v["schemas"])))
    return idx


def cmd_apply(fam, per, fu, fw):
    idx = build_index(fam, per, fu, fw)
    top_unres = {cc: v["count"] for cc, v in idx["unresolved_family"].items()
                 if v["count"] >= 5}
    for schema, e in fam.items():
        p = per[schema]
        block = {
            "generated_by": "ساخت-اسکیل-اسکیما-پگاه/scripts/crosslink.py",
            "family": sorted(fam),
            "note": "همه‌ی اینها نامزدند. ROLE_QUALIFIED_PREFIX از نام درآمده "
                    "و کلید خارجی نیست — قبل از استفاده با کوئریِ ارجاعِ یتیم "
                    "تأیید بگیر.",
            "role_qualified": dict(sorted(p["role_qualified"].items(),
                                          key=lambda kv: -kv[1]["count"])),
            "documented": p["documented"],
            "ambiguous": p["ambiguous"],
            "unresolved_here": dict(sorted(p["unresolved"].items(),
                                           key=lambda kv: -kv[1])),
            "unresolved_family_top": top_unres,
        }
        e["data"]["cc_resolution"] = block
        with io.open(e["path"], "w", encoding="utf-8") as fh:
            json.dump(e["data"], fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("نوشته شد: %s  (نقش‌دار %s، مستند %s، دوپهلو %s، بی‌مقصد %s)"
              % (e["path"], len(block["role_qualified"]),
                 len(block["documented"]), len(block["ambiguous"]),
                 len(block["unresolved_here"])))
    return idx


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd, root = argv[0], argv[1]
    fam = load_family(root)
    if not fam:
        print("هیچ schema.json ای زیر %s پیدا نشد." % root)
        return 1
    per, fu, fw = resolve(fam)
    if cmd == "report":
        cmd_report(fam, per, fu, fw)
        return 0
    if cmd in ("apply", "index"):
        if cmd == "apply":
            idx = cmd_apply(fam, per, fu, fw)
        else:
            idx = build_index(fam, per, fu, fw)
        out = (argv[argv.index("--out") + 1] if "--out" in argv
               else os.path.join(root, "skills-index.json"))
        with io.open(out, "w", encoding="utf-8") as fh:
            json.dump(idx, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("نوشته شد: %s" % out)
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
