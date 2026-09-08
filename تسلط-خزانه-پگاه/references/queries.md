# کوئری‌ها

> **این کوئری‌ها الگو هستند و هنوز اجرا نشده‌اند.** نام جدول‌ها و ستون‌ها از
> فهرست کاملِ اشیای `PegahAI` آمده، پس درست‌اند — ولی خودِ کوئری اجرا نشده.
> **وقتی دسترسی داری اجرایشان کن و بالای هرکدام «تست‌شده» بنویس.**

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود. پارامتر را با `params` بساز.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** در SQL جمع بزن.

---

## ۰. تأیید — قبل از هر چیز

### ۰.۱ آخرین تاریخِ داده

```sql
SELECT 'DariaftPardakht' AS jadval, MAX(ZamaneSabt) AS akharin
FROM [Treasury].[DariaftPardakht]
UNION ALL SELECT 'DariaftPardakhtPPC', MAX(ZamaneSabt)
FROM [Treasury].[DariaftPardakhtPPC]
UNION ALL SELECT 'EjazehPardakhtFaktor', MAX(ZamaneSabt)
FROM [Treasury].[EjazehPardakhtFaktor]
UNION ALL SELECT 'Tankhah', MAX(TarikhSabt)
FROM [Treasury].[Tankhah]
ORDER BY akharin DESC;
```

### ۰.۲ جهانِ PPC — **مهم‌ترین کوئری این صفحه**

تا این حل نشده، **هیچ جمعِ ریالی قطعی نیست**.

```sql
SELECT 'DariaftPardakht' AS jadval, COUNT(*) AS tedad,
       MIN(ZamaneSabt) AS az, MAX(ZamaneSabt) AS ta
FROM [Treasury].[DariaftPardakht]
UNION ALL
SELECT 'DariaftPardakhtPPC', COUNT(*), MIN(ZamaneSabt), MAX(ZamaneSabt)
FROM [Treasury].[DariaftPardakhtPPC];
```

و مهم‌تر: **آیا کلیدها مشترک‌اند؟**

```sql
SELECT COUNT(*) AS moshtarak
FROM [Treasury].[DariaftPardakht] AS a
JOIN [Treasury].[DariaftPardakhtPPC] AS b
  ON b.ccDariaftPardakht = a.ccDariaftPardakht;
```

سه نتیجه، سه معنیِ متفاوت:

| نتیجه | یعنی |
|---|---|
| هم‌پوشانیِ بالا | PPC به جدول اصلی **سینک می‌شود** — یکی را بگیر، نه هر دو |
| هم‌پوشانیِ صفر | **دو مجموعه‌ی جدا** — برای تصویر کامل هر دو لازم است |
| هم‌پوشانیِ جزئی | بدترین حالت — **بپرس**، حدس نزن |

همین آزمون را برای چهار جفتِ دیگر هم بزن: `...Bargashty`،
`...DarkhastFaktor`، `...FaktorZayeat`، `...Vazeiat`.

### ۰.۳ دیکشنری نوع دریافت/پرداخت — جهت

```sql
SELECT CodeNoeDariaftPardakht, NameNoeDariaftPardakht
FROM [Treasury].[NoeDariaftPardakht]
ORDER BY CodeNoeDariaftPardakht;
```

و توزیعِ واقعی:

```sql
SELECT d.CodeNoeDariaftPardakht, COUNT(*) AS tedad, SUM(d.Mablagh) AS jam
FROM [Treasury].[DariaftPardakht] AS d
GROUP BY d.CodeNoeDariaftPardakht
ORDER BY tedad DESC;
```

**کدام کد دریافت است و کدام پرداخت را از داده تأیید بگیر**، نه از اسم.

### ۰.۴ جهتِ `BedBes`

```sql
SELECT s.BedBes, COUNT(*) AS tedad, SUM(s.Mablagh) AS jam
FROM [Treasury].[EjazehPardakhtFaktorSatr] AS s
GROUP BY s.BedBes;
```

اگر جمعِ دو طرف نزدیک به هم بود، `BedBes` واقعاً بده/بستان است و باید
علامت‌دار جمع بزنی. اگر یک طرف خالی بود، تعریفش چیز دیگری است — **بپرس**.

### ۰.۵ دیکشنری وضعیت — هر دامنه جدا

```sql
SELECT DISTINCT CodeVazeiat FROM [Treasury].[DariaftPardakht] ORDER BY CodeVazeiat;
```

```sql
SELECT DISTINCT CodeVazeiat FROM [Treasury].[EjazehPardakhtFaktor] ORDER BY CodeVazeiat;
```

**کدها بین این دو یکسان نیستند.** توزیع را هم بگیر: کدی که ۹۰٪ سطرها را
دارد معمولاً «تأییدشده» است — ولی **تأیید بگیر**.

### ۰.۶ مبلغِ سربرگ در برابر مبلغِ وضعیت

```sql
WITH akhar AS (
    SELECT v.ccDariaftPardakht,
           MAX(v.ZamanVazeiat) AS akharin
    FROM [Treasury].[DariaftPardakhtVazeiat] AS v
    GROUP BY v.ccDariaftPardakht
)
SELECT COUNT(*) AS barresi_shode,
       SUM(CASE WHEN ABS(ISNULL(d.Mablagh,0) - ISNULL(v.Mablagh,0)) > 1
                THEN 1 ELSE 0 END) AS moghayer
FROM [Treasury].[DariaftPardakht] AS d
JOIN akhar AS a ON a.ccDariaftPardakht = d.ccDariaftPardakht
JOIN [Treasury].[DariaftPardakhtVazeiat] AS v
  ON v.ccDariaftPardakht = a.ccDariaftPardakht
 AND v.ZamanVazeiat = a.akharin;
```

`moghayer` صفر یعنی سربرگ کافی است. غیرصفر یعنی **باید تصمیم بگیری کدام
«مبلغ واقعی» است** — و در گزارش بنویسی.

### ۰.۷ کلید خارجی واقعی

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
WHERE OBJECT_SCHEMA_NAME(fkc.parent_object_id) = 'Treasury'
ORDER BY ParentTable, ParentColumn;
```

---

## ۱. دریافت و پرداخت در یک بازه

```sql
WITH params AS (
    SELECT CAST('2026-08-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh,
           CAST(NULL AS int)          AS cc_markaz
)
SELECT d.ccMarkazPakhsh,
       d.CodeNoeDariaftPardakht,
       n.NameNoeDariaftPardakht,
       d.CodeNoeSanad,
       COUNT(*)        AS tedad_sanad,
       SUM(d.Mablagh)  AS jam_mablagh
FROM [Treasury].[DariaftPardakht] AS d
CROSS JOIN params AS p
LEFT JOIN [Treasury].[NoeDariaftPardakht] AS n
       ON n.CodeNoeDariaftPardakht = d.CodeNoeDariaftPardakht
WHERE d.ZamaneSabt >= p.az_tarikh AND d.ZamaneSabt < DATEADD(day, 1, p.ta_tarikh)
  AND (p.cc_markaz IS NULL OR d.ccMarkazPakhsh = p.cc_markaz)
GROUP BY d.ccMarkazPakhsh, d.CodeNoeDariaftPardakht,
         n.NameNoeDariaftPardakht, d.CodeNoeSanad
ORDER BY jam_mablagh DESC;
```

سه نکته:

- **تفکیک بر `CodeNoeDariaftPardakht`** — دریافت و پرداخت را با هم جمع نکن.
- **`CodeVazeiat` عمداً فیلتر نشده** — اول کوئری ۰.۵ را بزن و کدِ معتبر را
  اضافه کن، وگرنه اسنادِ باطل هم می‌آیند.
- **`DariaftPardakhtPPC` اینجا نیست.** اگر کوئری ۰.۲ گفت دو مجموعه‌ی جدایند،
  باید `UNION ALL` شود — و اگر گفت سینک می‌شوند، نباید.

## ۲. اجازه پرداخت و سرنوشتش

```sql
WITH params AS (
    SELECT CAST('2026-08-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT e.CodeVazeiat,
       COUNT(*)                      AS tedad,
       SUM(e.Mablagh)                AS jam_mablagh,
       COUNT(e.TarikhTaeedNahaee)    AS tedad_taeed_nahaee,
       COUNT(e.ccElatOdat)           AS tedad_bargashti
FROM [Treasury].[EjazehPardakhtFaktor] AS e
CROSS JOIN params AS p
WHERE e.ZamaneSabt >= p.az_tarikh AND e.ZamaneSabt < DATEADD(day, 1, p.ta_tarikh)
GROUP BY e.CodeVazeiat
ORDER BY tedad DESC;
```

`ccElatOdat`ِ پرشده یعنی برگشت خورده. `TarikhTaeedNahaee`ِ پرشده یعنی تأیید
نهایی گرفته.

## ۳. تخصیصِ حسابداری — با علامت

```sql
WITH params AS (SELECT CAST(0 AS bigint) AS cc_ejazeh)
SELECT s.ccHesab0, s.ccHesab1, s.ccHesab2, s.ccHesab7,
       SUM(CASE WHEN s.BedBes = 1 THEN  s.Mablagh ELSE 0 END) AS bedehkar,
       SUM(CASE WHEN s.BedBes = 2 THEN  s.Mablagh ELSE 0 END) AS bestankar,
       SUM(CASE WHEN s.BedBes = 1 THEN  s.Mablagh
                ELSE -s.Mablagh END)                          AS khales
FROM [Treasury].[EjazehPardakhtFaktorSatr] AS s
CROSS JOIN params AS p
WHERE s.ccEjazehPardakhtFaktor = p.cc_ejazeh
GROUP BY s.ccHesab0, s.ccHesab1, s.ccHesab2, s.ccHesab7
ORDER BY khales DESC;
```

> **مقدارِ `BedBes` (۱ = بدهکار؟) حدس است.** کوئری ۰.۴ تکلیفش را روشن
> می‌کند. اگر برعکس بود، `khales` علامتش وارونه می‌شود — و این یعنی گزارشِ
> کاملاً غلطِ به‌ظاهر درست.

**آزمونِ سلامت:** اگر سند متوازن باشد، `SUM(bedehkar) = SUM(bestankar)` و
`SUM(khales) = 0`. اگر نشد، یا `BedBes` را اشتباه فهمیده‌ای یا سند ناقص است.

## ۴. تنخواه — گردش و مانده

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_tankhah_dar)
SELECT t.ccTankhahDar,
       COUNT(*) AS tedad,
       SUM(CASE WHEN t.BedBes = 1 THEN  t.Mablagh ELSE 0 END) AS bedehkar,
       SUM(CASE WHEN t.BedBes = 2 THEN  t.Mablagh ELSE 0 END) AS bestankar,
       SUM(CASE WHEN t.BedBes = 1 THEN  t.Mablagh
                ELSE -t.Mablagh END)                          AS mandeh
FROM [Treasury].[Tankhah] AS t
CROSS JOIN params AS p
WHERE (p.cc_tankhah_dar IS NULL OR t.ccTankhahDar = p.cc_tankhah_dar)
GROUP BY t.ccTankhahDar
ORDER BY mandeh DESC;
```

مانده را با `SaghfTankhah` مقایسه کن تا تجاوز از سقف معلوم شود.

## ۵. دسته‌چک و برگ‌های مانده

```sql
SELECT d.ccDastehCheck,
       d.ccShomarehHesab,
       d.Serial_Begin,
       d.TedadBarg,
       d.TedadBargMandeh,
       d.TedadBarg - d.TedadBargMandeh AS masraf_shodeh,
       d.Faal
FROM [Treasury].[DastehCheck] AS d
WHERE d.Faal = 1
ORDER BY d.TedadBargMandeh;
```

## ۹. کیفیت داده

### ۹.۱ ارجاعِ یتیم

```sql
SELECT COUNT(*) AS kol,
       SUM(CASE WHEN e.ccEjazehPardakhtFaktor IS NULL THEN 1 ELSE 0 END) AS yatim
FROM [Treasury].[EjazehPardakhtFaktorSatr] AS s
LEFT JOIN [Treasury].[EjazehPardakhtFaktor] AS e
       ON e.ccEjazehPardakhtFaktor = s.ccEjazehPardakhtFaktor
WHERE s.ccEjazehPardakhtFaktor IS NOT NULL;
```

روی این‌ها بزن: `ccEjazehPardakhtFaktor`، `ccDariaftPardakht`، `ccSandogh`،
`ccTankhahDar`، `ccBoodjeh`.

### ۹.۲ دانه — سربرگ در برابر سطر

```sql
SELECT COUNT(*)                                   AS satr,
       COUNT(DISTINCT s.ccEjazehPardakhtFaktor)   AS sarbarg,
       CAST(COUNT(*) AS decimal(18,2))
         / NULLIF(COUNT(DISTINCT s.ccEjazehPardakhtFaktor), 0) AS satr_har_sarbarg
FROM [Treasury].[EjazehPardakhtFaktorSatr] AS s;
```

**قبل از هر `JOIN` از سربرگ به سطر این را بزن** — وگرنه مبلغِ سربرگ به تعدادِ
سطرها ضرب می‌شود.

### ۹.۳ ناسازگاری نوع

`EjazehPardakhtPishPardakht.ccTankhahDar` از نوع `nchar` است ولی
`TankhahDar.ccTankhahDar` از نوع `bigint`. این join بدون `CAST` نمی‌شکند ولی
کند و مستعدِ خطاست — و اگر مقدارها فاصله‌ی انتهایی داشته باشند، بی‌صدا
نمی‌خورند.

## اندازه‌ها

| اندازه | مقدار واقعی |
|---|---|
| آخرین تاریخِ `DariaftPardakht` | ؟ |
| نسبت سطر `DariaftPardakht` به `...PPC` | ؟ |
| هم‌پوشانیِ کلیدِ دو جدول | ؟ |
| مقدارِ `BedBes` برای بدهکار | ؟ |
| میانگین سطر به ازای هر اجازه پرداخت | ؟ |
