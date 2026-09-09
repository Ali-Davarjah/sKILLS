# یک سؤال واقعی، از اول تا آخر

**سؤال کاربر:** «فروش مرداد ۱۴۰۵ را به تفکیک منطقه بده.»

سؤالی که **در این اسکیما شروع نمی‌شود ولی بدونِ آن جواب نمی‌گیرد**. و کلمه‌ی
«منطقه» سه چیز می‌تواند باشد.

---

## گام ۰ — «منطقه» کدام است؟

این اسکیما **سه** سلسله‌مراتبِ سازمانی دارد و هر سه به فارسی «منطقه» دارند:

| سلسله‌مراتب | جدول‌ها | چه کسی به کار می‌برد |
|---|---|---|
| پخش | `MantaghehPakhsh` → `MarkazPakhsh` | Sales, Treasury, Warehouse |
| فروش | `MantaghehForosh` → `HouzehForosh` | Sales (۶۱ ارجاع) |
| مرکز | `Markaz` | **HumanResource (۶۳ ارجاع)** |

```sql
-- کوئری ۰.۳ — کدام سطح چند تا دارد
```

عددها کمک می‌کنند ولی **تصمیم را نمی‌گیرند**. اگر سؤال از مدیر فروش آمده،
احتمالاً `MantaghehForosh` است؛ اگر از مالی، `Markaz`.

**این تنها سؤالِ متوقف‌کننده‌ی این مسیر است.** بپرس.

فرض: منظور منطقه‌ی **فروش** است.

## گام ۱ — مسیر از فروش به منطقه

جدولِ فروش `Sales.AmarForosh_Arshive` است و `ccForoshandeh` دارد (مسیر).
مسیر به منطقه‌ی فروش می‌رسد — ولی **از کدام راه؟**

```
python scripts/map.py refs MantaghehForosh
```

`MantaghehForosh` ۷۴ ارجاع دارد که ۶۱ تایش از `Sales` است. یعنی خودِ
`Sales` جدولی دارد که مسیر را به منطقه وصل می‌کند — آن را در اسکیل
`تسلط-فروش-پگاه` پیدا کن، نه اینجا.

> **این اسکیل برچسب می‌دهد، نه واقعیت.** عددِ فروش از `Sales` می‌آید؛
> `Global` فقط می‌گوید آن عدد به کدام منطقه تعلق دارد و اسمش چیست.

## گام ۲ — تاریخِ شمسی به میلادی

`AmarForosh_Arshive.Tarikh` میلادی است و سؤال شمسی. `Taghvim` مترجم است:

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah)
SELECT MIN(t.Tarikh) AS az_miladi,
       MAX(t.Tarikh) AS ta_miladi,
       MIN(t.TarikhShamsi) AS az_shamsi,
       MAX(t.TarikhShamsi) AS ta_shamsi
FROM [Global].[Taghvim] AS t
CROSS JOIN params AS p
WHERE t.Sal = p.sal AND t.Mah = p.mah;
```

**بازه را از تقویم بگیر، دستی حساب نکن.** و یادت باشد `TarikhShamsi` عددی
است (`14050501`)، نه رشته.

## گام ۳ — نامِ منطقه

```sql
SELECT mf.ccMantaghehForosh,
       mf.NameMantaghehForosh,
       nv.NameNoeVahedForosh,
       a.FName + N' ' + a.LName AS modir
FROM [Global].[MantaghehForosh] AS mf
LEFT JOIN [Global].[NoeVahedForosh] AS nv
       ON nv.ccNoeVahedForosh = mf.ccNoeVahedForosh
LEFT JOIN [Global].[Afrad] AS a ON a.ccAfrad = mf.ccAfradModir
ORDER BY mf.NameMantaghehForosh;
```

`ccNoeVahedForosh` سطحِ واحد را می‌گوید — ممکن است «منطقه» در این جدول چند
سطحِ متفاوت داشته باشد. **اگر داشت، فیلترش کن و در گزارش بنویس.**

## گام ۴ — کوئری نهایی (در اسکیل فروش اجرا می‌شود)

```sql
WITH params AS (
    SELECT 1405 AS sal, 5 AS mah
),
bazeh AS (
    SELECT MIN(t.Tarikh) AS az, MAX(t.Tarikh) AS ta
    FROM [Global].[Taghvim] AS t
    CROSS JOIN params AS p
    WHERE t.Sal = p.sal AND t.Mah = p.mah
)
SELECT mf.ccMantaghehForosh,
       mf.NameMantaghehForosh,
       COUNT(DISTINCT f.ccDarkhastFaktor) AS tedad_faktor,
       COUNT(DISTINCT f.ccMoshtary)       AS moshtary_yekta,
       SUM(f.Rial)                        AS jam_rial
FROM [Sales].[AmarForosh_Arshive] AS f
CROSS JOIN bazeh AS b
JOIN /* جدولِ اتصالِ مسیر به منطقه — از اسکیل فروش */ AS lnk
     ON lnk.ccForoshandeh = f.ccForoshandeh
JOIN [Global].[MantaghehForosh] AS mf
     ON mf.ccMantaghehForosh = lnk.ccMantaghehForosh
WHERE f.Tarikh >= b.az AND f.Tarikh <= b.ta
  AND f.IsMarjoee = 0
GROUP BY mf.ccMantaghehForosh, mf.NameMantaghehForosh
ORDER BY jam_rial DESC;
```

**`JOIN` وسط عمداً ناتمام است** — آن حلقه در `Sales` است و باید از آنجا
پیدایش کنی. این اسکیل تا اینجا کارش را کرده: بازه، نام منطقه، و اینکه کدام
سلسله‌مراتب.

## گام ۵ — گزارش

```
فروش به تفکیک منطقه — مرداد ۱۴۰۵

بازه         : ۱۴۰۵/۰۵/۰۱ تا ۱۴۰۵/۰۵/۳۱ (از Global.Taghvim، نه حساب دستی)
سلسله‌مراتب  : منطقه‌ی **فروش** (MantaghehForosh) — نه منطقه‌ی پخش و نه Markaz
منبع عدد     : Sales.AmarForosh_Arshive با IsMarjoee = 0
منبع برچسب   : Global.MantaghehForosh

┌───┬────────────────┬──────────┬──────────┬──────────────┐
│ ۱ │ منطقه          │ فاکتور   │ مشتری    │ جمع ریال     │
└───┴────────────────┴──────────┴──────────┴──────────────┘

N مسیر از M مسیر به منطقه‌ای نگاشت نشدند و در جدول نیستند.

تأییدنشده: اتصال مسیر به منطقه از هم‌نامی است و کلید خارجی ندارد.
```

---

## چه پرسیده شد و چه پرسیده نشد

| پرسیده شد | چون |
|---|---|
| کدام «منطقه» | سه سلسله‌مراتب هست و از داده حل نمی‌شود |

| پرسیده نشد | چون |
|---|---|
| بازه‌ی میلادیِ مرداد | `Taghvim` می‌دهد |
| نام منطقه از کجا | `MantaghehForosh` تنها گزینه است |
| مرجوعی حساب شود؟ | `IsMarjoee = 0` پیش‌فرضِ فروش است و در گزارش نوشته شد |

---

## اگر جواب خالی درآمد

۱. **`Taghvim` آن ماه را دارد؟** تقویم ممکن است تا امروز پر نشده باشد.
۲. **مسیرها به منطقه نگاشت شده‌اند؟** آزمونِ یتیم روی `ccMantaghehForosh`.
۳. **فیلترِ `Faal`** روی منطقه — منطقه‌ی غیرفعال هم سطر دارد.

معمول‌ترین علتِ خالی بودن در این اسکیما: **گرفتنِ سلسله‌مراتبِ اشتباه** —
مسیرها به `MantaghehForosh` وصل‌اند ولی تو `MantaghehPakhsh` را join
کرده‌ای، و نتیجه صفر سطر است بدون هیچ خطایی.
