# کوئری‌ها

> **این کوئری‌ها الگو هستند و هنوز اجرا نشده‌اند.** اسم جدول‌ها و ستون‌ها از
> نقشه‌ای آمده که با فهرست اشیای `PegahAI` خوانده، پس نام‌ها درست‌اند — ولی
> خودِ کوئری اجرا نشده. **وقتی دسترسی داری اجرایشان کن و بالای هرکدام
> «تست‌شده» بنویس.**

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود. پارامتر را با `params` بساز.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** این اسکیما ده‌ها هزار مشتری
> دارد. **در SQL جمع بزن**، سطر خام نخواه.

---

## ۰. تأیید — قبل از هر چیز

### ۰.۱ آخرین تاریخِ داده — مهم‌ترین کوئری این صفحه

سه جدولِ این اسکیما در ۲۰۱۸ ایستاده‌اند و اسمشان دقیقاً همان کاری است که
می‌خواهی. **قبل از هر کاری این را بزن:**

```sql
SELECT 'AmarForosh_Arshive'     AS jadval, MAX(Tarikh) AS akharin
FROM [Sales].[AmarForosh_Arshive]
UNION ALL SELECT 'HadafForoshRoozanehNew',   MAX(Tarikh)
FROM [Sales].[HadafForoshRoozanehNew]
UNION ALL SELECT 'HadafForoshRoozaneh',      MAX(Tarikh)
FROM [Sales].[HadafForoshRoozaneh]
UNION ALL SELECT 'AmalkardRozanehForosh',    MAX(Tarikh)
FROM [Sales].[AmalkardRozanehForosh]
UNION ALL SELECT 'VisitForoshandeh_Arshiv',  MAX(Tarikh)
FROM [Sales].[VisitForoshandeh_Arshiv]
ORDER BY akharin DESC;
```

انتظار: سه ردیفِ آخر عقب‌اند. اگر `AmalkardRozanehForosh` تاریخِ تازه داشت،
یعنی زنده شده و این یادداشت باید عوض شود.

### ۰.۲ ستون‌های یک جدول

```sql
WITH params AS (SELECT N'AmarForosh_Arshive' AS jadval)
SELECT c.COLUMN_NAME, c.DATA_TYPE, c.IS_NULLABLE, c.ORDINAL_POSITION
FROM INFORMATION_SCHEMA.COLUMNS AS c
CROSS JOIN params AS p
WHERE c.TABLE_SCHEMA = 'Sales' AND c.TABLE_NAME = p.jadval
ORDER BY c.ORDINAL_POSITION;
```

### ۰.۳ دنبال یک اسم بگرد

```sql
WITH params AS (SELECT N'%Jayezeh%' AS alago)
SELECT s.name AS schema_name, t.name AS table_name
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
CROSS JOIN params AS p
WHERE t.name LIKE p.alago
ORDER BY s.name, t.name;
```

اسکیما عمداً فیلتر نشده — مقصد ممکن است در `Global` یا `Warehouse` باشد.

### ۰.۴ کلید خارجی واقعی

```sql
SELECT OBJECT_NAME(fkc.parent_object_id)            AS ParentTable,
       pc.name                                      AS ParentColumn,
       OBJECT_SCHEMA_NAME(fkc.referenced_object_id) AS RefSchema,
       OBJECT_NAME(fkc.referenced_object_id)        AS RefTable,
       rc.name                                      AS RefColumn
FROM sys.foreign_key_columns AS fkc
JOIN sys.columns AS pc
  ON pc.object_id = fkc.parent_object_id AND pc.column_id = fkc.parent_column_id
JOIN sys.columns AS rc
  ON rc.object_id = fkc.referenced_object_id
 AND rc.column_id = fkc.referenced_column_id
WHERE OBJECT_SCHEMA_NAME(fkc.parent_object_id) = 'Sales'
ORDER BY ParentTable, ParentColumn;
```

خروجی خالی یعنی همه‌ی ۶۰۴ یال حدس‌اند. خروجی پر یعنی **نقشه را با آن بسنج**.

### ۰.۵ دیکشنری نوع فروشنده — قبل از هر رتبه‌بندی

```sql
SELECT ccNoeForoshandeh, NameNoeForoshandeh
FROM [Sales].[NoeForoshandeh]
ORDER BY ccNoeForoshandeh;
```

انتظار: ۱ درخواست‌گیر، ۲ سیار، ۳ آمارگر، ۴ مقیم، ۵ تلفنی، ۶ زنجیره‌ای،
۷ کترینگ، ۸ سرپرست، ۹ رییس مرکز، ۱۰ مدیر منطقه، ۱۱ ویژه.

### ۰.۶ ضریب نوع مشتری

```sql
SELECT z.ccNoeMoshtary, g.NameGoroh, z.Zarib
FROM [Sales].[ZaribNoeMoshtary] AS z
LEFT JOIN [Global].[Goroh] AS g ON g.ccGoroh = z.ccNoeMoshtary
ORDER BY z.ccNoeMoshtary;
```

سه نوع **ردیف ندارند**: شبه عمده (۳۵۳)، داروخانه (۳۵۴)، تعاونی کارکنان
(۶۰۷). و عمده (۳۴۸) در جدول ۲ است ولی تصمیم مدیر فروش ۳ — این را در گزارش
بنویس.

### ۰.۷ جهانِ PPC — قبل از هر جمع

```sql
SELECT 'DarkhastFaktor' AS joft, COUNT(*) AS moshtarak
FROM [Sales].[DarkhastFaktor] AS a
JOIN [Sales].[DarkhastFaktorPPC] AS b ON b.ccDarkhastFaktor = a.ccDarkhastFaktor
UNION ALL
SELECT 'ElamMarjoee', COUNT(*)
FROM [Sales].[ElamMarjoee] AS a
JOIN [Sales].[ElamMarjoeePPC] AS b ON b.ccElamMarjoee = a.ccElamMarjoee;
```

و تعدادِ هرکدام:

```sql
SELECT 'ElamMarjoee' AS jadval, COUNT(*) AS tedad FROM [Sales].[ElamMarjoee]
UNION ALL SELECT 'ElamMarjoeePPC', COUNT(*) FROM [Sales].[ElamMarjoeePPC];
```

| هم‌پوشانی | یعنی | چه کنی |
|---|---|---|
| بالا | PPC سینک است | فقط یکی |
| صفر | دو مجموعه‌ی جدا | هر دو با `UNION ALL` |
| جزئی | نامعلوم | **بپرس** |

> **این روی معیارِ مرجوعیِ اسکیل ارزیابی فروشنده اثر دارد.** آن اسکیل از
> `ElamMarjoee` استفاده می‌کند؛ اگر `ElamMarjoeePPC` سطرهای جدا داشته باشد،
> آن معیار کم‌شماری می‌کند.

---

## ۱. فروش یک بازه

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh,
           CAST(NULL AS int)          AS sazman_forosh   -- NULL = همه‌ی لاین‌ها
)
SELECT COUNT(*)                                AS satr_kala,
       COUNT(DISTINCT f.ccDarkhastFaktor)      AS tedad_faktor,
       COUNT(DISTINCT f.ccMoshtary)            AS moshtary_yekta,
       COUNT(DISTINCT f.ccForoshandeh)         AS masir,
       SUM(f.Rial)                             AS jam_rial,
       SUM(f.Tedad)                            AS jam_tedad
FROM [Sales].[AmarForosh_Arshive] AS f
CROSS JOIN params AS p
WHERE f.Tarikh >= p.az_tarikh AND f.Tarikh <= p.ta_tarikh
  AND f.IsMarjoee = 0;
```

**`IsMarjoee = 0` اجباری است** — بدون آن مرجوعی با فروش جمع می‌شود.
`satr_kala` کنارِ `tedad_faktor` عمدی است: نسبتشان میانگین سطرِ هر فاکتور
است و اگر برابر بودند یعنی چیزی غلط است.

## ۲. فروش به تفکیک فروشنده — با نام واقعی

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT f.ccAfradForoshandeh,
       a.FName, a.LName,
       COUNT(DISTINCT f.ccForoshandeh)     AS tedad_masir,
       COUNT(DISTINCT f.ccDarkhastFaktor)  AS tedad_faktor,
       COUNT(DISTINCT f.ccMoshtary)        AS moshtary_yekta,
       SUM(f.Rial)                         AS jam_rial
FROM [Sales].[AmarForosh_Arshive] AS f
CROSS JOIN params AS p
LEFT JOIN [Global].[Afrad] AS a ON a.ccAfrad = f.ccAfradForoshandeh
WHERE f.Tarikh >= p.az_tarikh AND f.Tarikh <= p.ta_tarikh
  AND f.IsMarjoee = 0
GROUP BY f.ccAfradForoshandeh, a.FName, a.LName
ORDER BY jam_rial DESC;
```

> **گروه‌بندی روی `ccAfradForoshandeh` است، نه `ccForoshandeh`** — چون
> سؤال «کدام آدم» است. ستون `tedad_masir` نشان می‌دهد یک نفر چند مسیر دارد.
> اگر سؤال «کدام مسیر» بود، کلید را عوض کن و در گزارش بگو.

## ۳. مرجوعی با علت و مسئولیت

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT e.ccForoshandeh,
       el.MasoleiatElat,
       COUNT(DISTINCT e.ccElamMarjoee) AS tedad_elam,
       SUM(s.Tedad1)                   AS tedad_kala
FROM [Sales].[ElamMarjoee] AS e
CROSS JOIN params AS p
JOIN [Sales].[ElamMarjoeeSatr] AS s ON s.ccElamMarjoee = e.ccElamMarjoee
LEFT JOIN [Warehouse].[ElatMarjoeeKala] AS el
       ON el.ccElatMarjoeeKala = s.ccElatMarjoeeKala
WHERE e.TarikhElamMarjoee >= p.az_tarikh
  AND e.TarikhElamMarjoee <= p.ta_tarikh
GROUP BY e.ccForoshandeh, el.MasoleiatElat
ORDER BY e.ccForoshandeh, el.MasoleiatElat;
```

`MasoleiatElat`: **۱ فروش** (مرجوعیِ ویزیتور)، ۲ پخش، ۳ تولید، ۴ فروش و پخش،
۰ نامشخص. برای «مرجوعی ویزیتور» فقط ۱.

> **این «اعلامِ» مرجوعی است.** برای حجمِ واقعیِ برگشتی،
> `AmarForosh_Arshive.IsMarjoee = 1` را بگیر — ولی آن علت ندارد. **هر دو را
> در گزارش بیاور و تفاوتشان را نام ببر.**

## ۴. تحقق هدف

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT h.ccForoshandeh,
       h.ccGorohKala,
       SUM(h.TedadHadaf)   AS hadaf_tedadi,
       SUM(h.TedadForosh)  AS forosh_tedadi,
       CASE WHEN SUM(h.TedadHadaf) = 0 THEN NULL
            ELSE 100.0 * SUM(h.TedadForosh) / SUM(h.TedadHadaf)
       END                 AS darsad_tahaghogh
FROM [Sales].[HadafForoshRoozanehNew] AS h
CROSS JOIN params AS p
WHERE h.Tarikh >= p.az_tarikh AND h.Tarikh <= p.ta_tarikh
GROUP BY h.ccForoshandeh, h.ccGorohKala
ORDER BY h.ccForoshandeh, h.ccGorohKala;
```

سه نکته که اشتباه‌شان گران است:

- **`TedadHadaf` هدفِ روزانه است** و هر روز عدد یکسانی دارد؛ جمعش روی بازه
  هدفِ بازه می‌شود.
- **واحد تعدادی مرجع است، نه ریالی.** هر سه واحد هست و جواب‌های متفاوتی
  می‌دهند — در یک مسیر واقعی تعدادی ۲۶۸٪ و ریالی ۱۷۶٪ درآمد.
- **تحققِ کل = جمعِ فروش ÷ جمعِ هدف**، نه میانگینِ درصدِ گروه‌ها. میانگینِ
  گروه‌ها با یک گروهِ ریزِ پرتحقق تا ۴۲۳٪ بالا می‌رود.

## ۵. ویزیت — دو مخرجِ متفاوت

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT v.ccForoshandeh,
       SUM(v.MorajehShodeh)                    AS rooydad_visit,
       SUM(v.VisitMosbat)                      AS rooydad_mosbat,
       100.0 * SUM(v.VisitMosbat)
             / NULLIF(SUM(v.MorajehShodeh), 0) AS darsad_visit_mosbat,
       COUNT(DISTINCT CASE WHEN v.MorajehShodeh = 1
                           THEN v.ccMoshtary END) AS moshtary_visit_shodeh,
       COUNT(DISTINCT CASE WHEN v.VisitMosbat = 1
                           THEN v.ccMoshtary END) AS moshtary_kharid_kardeh
FROM [Sales].[VisitForoshandeh_Arshiv] AS v
CROSS JOIN params AS p
WHERE v.Tarikh >= p.az_tarikh AND v.Tarikh <= p.ta_tarikh
GROUP BY v.ccForoshandeh
ORDER BY darsad_visit_mosbat DESC;
```

دو ستونِ اول **رویداد** می‌شمارند و دو ستونِ آخر **مشتریِ متمایز**. نسبتِ
اولی حدود ۴۰٪ می‌نشیند و دومی حدود ۸۰٪ — **این دو را با هم اشتباه نگیر**.

## ۶. مشتری — خرید در بازه

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh,
           CAST(NULL AS int)          AS noe_moshtary
)
SELECT f.ccMoshtary,
       f.ccNoeMoshtary,
       COUNT(DISTINCT f.ccDarkhastFaktor) AS tedad_faktor,
       COUNT(DISTINCT f.ccKalaCode)       AS tedad_sku,
       SUM(f.Tedad)                       AS tedad_aghlam,
       SUM(f.Rial)                        AS jam_rial
FROM [Sales].[AmarForosh_Arshive] AS f
CROSS JOIN params AS p
WHERE f.Tarikh >= p.az_tarikh AND f.Tarikh <= p.ta_tarikh
  AND f.IsMarjoee = 0
  AND (p.noe_moshtary IS NULL OR f.ccNoeMoshtary = p.noe_moshtary)
GROUP BY f.ccMoshtary, f.ccNoeMoshtary
ORDER BY jam_rial DESC;
```

> **بدون فیلترِ نوع مشتری، ۵۰۰ سطرِ اول همه خرد می‌شوند** و بقیه‌ی نوع‌ها
> کامل از جدول می‌افتند — بدون هیچ خطایی. یا فیلتر بگذار یا تجمیع کن.

## ۹. کیفیت داده

### ۹.۱ ارجاعِ یتیم — اعتبارسنجیِ یال

```sql
SELECT COUNT(*) AS kol,
       SUM(CASE WHEN m.ccMoshtary IS NULL THEN 1 ELSE 0 END) AS yatim
FROM [Sales].[AmarForosh_Arshive] AS f
LEFT JOIN [Sales].[Moshtary] AS m ON m.ccMoshtary = f.ccMoshtary
WHERE f.ccMoshtary IS NOT NULL;
```

نسبتِ یتیمِ بالا یعنی **یال غلط است**، نه اینکه داده کثیف است. این را روی
یال‌های پرکاربرد بزن (`ccMoshtary`، `ccForoshandeh`، `ccKalaCode`،
`ccDarkhastFaktor`) و هر کدام که صفر داد در `schema.json` به
`confidence: "CONFIRMED"` ببر.

### ۹.۲ دانه — قبل از هر `SUM`

```sql
WITH params AS (SELECT CAST('2026-08-01' AS date) AS az,
                       CAST('2026-08-30' AS date) AS ta)
SELECT COUNT(*)                                    AS satr,
       COUNT(DISTINCT f.ccDarkhastFaktor)          AS faktor,
       CAST(COUNT(*) AS decimal(18,2))
         / NULLIF(COUNT(DISTINCT f.ccDarkhastFaktor), 0) AS satr_har_faktor
FROM [Sales].[AmarForosh_Arshive] AS f
CROSS JOIN params AS p
WHERE f.Tarikh >= p.az AND f.Tarikh <= p.ta AND f.IsMarjoee = 0;
```

`satr_har_faktor` باید حدود ۶ تا ۷ باشد. خیلی کمتر یا خیلی بیشتر یعنی
فیلتر یا دانه را اشتباه گرفته‌ای.

## اندازه‌ها — برای اینکه بفهمی جواب معقول است

بار اول که روی داده‌ی زنده اجرا کردی، این عددها را اینجا بنویس:

| اندازه | مقدار واقعی |
|---|---|
| آخرین تاریخِ `AmarForosh_Arshive` | ؟ |
| فروشنده‌ی درخواست‌گیرِ فعال در یک ماه | ؟ |
| میانگین سطرِ هر فاکتور | ؟ (انتظار ~۶.۸) |
| درصد ویزیت مثبت (رویدادی) | ؟ (انتظار ~۴۰٪) |
| نسبت `IsMarjoee=1` به `ElamMarjoee` | ؟ (انتظار ۱۰ تا ۲۵ برابر) |
