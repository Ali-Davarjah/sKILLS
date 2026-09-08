# کوئری‌ها

> **این کوئری‌ها الگو هستند و هنوز روی دیتابیس اجرا نشده‌اند.** جدول‌ها و
> ستون‌هایشان از نقشه‌ای آمده که با فهرست اشیای دیتابیس خوانده، پس اسم‌ها
> درست‌اند — ولی خودِ کوئری اجرا نشده. **وقتی دسترسی داری اجرایشان کن و
> بالای هرکدام «تست‌شده» بنویس.** بخش ۰ را اول بزن.

> **و یادت باشد: جوابِ نهایی از دیتابیس می‌آید، نه از نقشه.** نقشه می‌گوید
> کدام جدول و کدام مسیر؛ عدد را کوئری می‌دهد.

> **`DECLARE` ننویس.** `run_query` فقط **یک** دستور می‌پذیرد که با `SELECT` یا
> `WITH` شروع شود؛ `DECLARE` کوئری را دودستوری می‌کند و کل آن رد می‌شود. به
> همین دلیل پارامترها با `params` ساخته می‌شوند. `WITH` خودش مجاز است — اگر
> خطای ردشدن دیدی دنبال `DECLARE` بگرد، نه دنبال CTE.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** این اسکیما هزاران کارمند دارد.
> **در SQL جمع بزن**، سطر خام نخواه. اگر فهرست فردی لازم است، حتماً با فیلتر و
> `ORDER BY` معنادار.

---

## ۰. تأیید — قبل از هر چیز

### ۰.۱ کدام جدول‌ها واقعاً هستند و چقدر داده دارند

```sql
SELECT s.name AS schema_name,
       t.name AS table_name,
       SUM(p.rows) AS row_count
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
JOIN sys.partitions AS p
  ON p.object_id = t.object_id AND p.index_id IN (0, 1)
WHERE s.name = 'HumanResource'
GROUP BY s.name, t.name
ORDER BY row_count DESC;
```

جدولِ خالی یعنی یا مرده است یا این ماژول استفاده نمی‌شود. هر دو را در گزارش
بگو.

### ۰.۲ دنبال یک اسم بگرد — وقتی جدولِ نقشه پیدا نشد

```sql
WITH params AS (SELECT N'%Morakhasi%' AS alago)
SELECT s.name AS schema_name, t.name AS table_name
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
CROSS JOIN params AS p
WHERE t.name LIKE p.alago
ORDER BY s.name, t.name;
```

اسکیما را عمداً فیلتر نکرده — اگر جدول در `HumanResource` نبود، شاید در
`Global` باشد.

### ۰.۳ ستون‌های یک جدول — اسم و نوع

```sql
WITH params AS (SELECT N'PardakhtHoghogh' AS jadval)
SELECT c.COLUMN_NAME, c.DATA_TYPE, c.CHARACTER_MAXIMUM_LENGTH,
       c.IS_NULLABLE, c.ORDINAL_POSITION
FROM INFORMATION_SCHEMA.COLUMNS AS c
CROSS JOIN params AS p
WHERE c.TABLE_SCHEMA = 'HumanResource' AND c.TABLE_NAME = p.jadval
ORDER BY c.ORDINAL_POSITION;
```

### ۰.۴ کلید خارجی واقعی — اگر بود، حرف آخر است

```sql
SELECT OBJECT_NAME(fkc.parent_object_id)     AS ParentTable,
       pc.name                               AS ParentColumn,
       OBJECT_SCHEMA_NAME(fkc.referenced_object_id) AS RefSchema,
       OBJECT_NAME(fkc.referenced_object_id) AS RefTable,
       rc.name                               AS RefColumn
FROM sys.foreign_key_columns AS fkc
JOIN sys.columns AS pc
  ON pc.object_id = fkc.parent_object_id AND pc.column_id = fkc.parent_column_id
JOIN sys.columns AS rc
  ON rc.object_id = fkc.referenced_object_id AND rc.column_id = fkc.referenced_column_id
WHERE OBJECT_SCHEMA_NAME(fkc.parent_object_id) = 'HumanResource'
ORDER BY ParentTable, ParentColumn;
```

خروجی خالی یعنی روابط در کدِ برنامه اعمال می‌شوند و این نقشه تنها راهنماست.
خروجی پر یعنی **نقشه را با آن بسنج و هرجا اختلاف بود، اسکیمای واقعی درست
است**.

### ۰.۵ جدول‌های دوقلو — کدام زنده است

```sql
SELECT 'ShiftKari'  AS jadval, COUNT(*) AS tedad FROM [HumanResource].[ShiftKari]
UNION ALL SELECT 'ShiftKary',            COUNT(*) FROM [HumanResource].[ShiftKary]
UNION ALL SELECT 'PersonelMamoriat',     COUNT(*) FROM [HumanResource].[PersonelMamoriat]
UNION ALL SELECT 'PersonelMamuryat',     COUNT(*) FROM [HumanResource].[PersonelMamuryat]
UNION ALL SELECT 'PersonelSabegheKari',  COUNT(*) FROM [HumanResource].[PersonelSabegheKari]
UNION ALL SELECT 'PersonelSavabeghKary', COUNT(*) FROM [HumanResource].[PersonelSavabeghKary]
UNION ALL SELECT 'PersonelMadrak',       COUNT(*) FROM [HumanResource].[PersonelMadrak]
UNION ALL SELECT 'Personel_Madrak',      COUNT(*) FROM [HumanResource].[Personel_Madrak]
ORDER BY tedad DESC;
```

تعداد کافی نیست — **تازگی** هم لازم است. برای هر جفتِ مشکوک `MAX(تاریخ)` را هم
بگیر:

```sql
SELECT 'PersonelMamoriat' AS jadval, MAX(FromDate) AS akharin
FROM [HumanResource].[PersonelMamoriat]
UNION ALL
SELECT 'PersonelMamuryat', MAX(FromDate)
FROM [HumanResource].[PersonelMamuryat];
```

### ۰.۶ آخرین تاریخِ داده — قبل از هر گزارش دوره‌ای

```sql
SELECT MAX(Sal) AS akharin_sal FROM [HumanResource].[PardakhtHoghogh];
```

```sql
WITH params AS (SELECT 1405 AS sal)
SELECT MAX(ph.Mah) AS akharin_mah
FROM [HumanResource].[PardakhtHoghogh] AS ph
CROSS JOIN params AS p
WHERE ph.Sal = p.sal;
```

### ۰.۷ دیکشنری وضعیت — قبل از هر فیلترِ وضعیت

```sql
SELECT CodeVazeiat, NameVazeiat, ccSystem, IsEbtal
FROM [HumanResource].[PardakhtHoghogh_CodeVazeiat]
ORDER BY CodeVazeiat;
```

`IsEbtal = 1` مستقیم می‌گوید کدام کد یعنی «باطل». جدول‌های
`TasviehHesab_CodeVazeiat` هم این ستون را دارند. برای بقیه‌ی دامنه‌ها
`X_CodeVazeiat` را بخوان و **کدها را بین دامنه‌ها منتقل نکن**.

---

## ۱. هویت کارمند و وضع فعلی

```sql
WITH params AS (
    SELECT CAST('2026-08-22' AS date) AS as_of,
           CAST(NULL AS int)          AS cc_personel   -- NULL = همه
)
SELECT pr.ccPersonel,
       pr.ShomarehPersonely,
       a.FName, a.LName,
       pr.TarikhEstekhdam,
       pr.TarikhEnfesal,
       pr.CodeVazeiat,
       v.NameVazeiat,
       pr.IsBazneshasteh
FROM [HumanResource].[Personel] AS pr
CROSS JOIN params AS p
LEFT JOIN [Global].[Afrad] AS a
       ON a.ccAfrad = pr.ccAfrad
LEFT JOIN [HumanResource].[Personel_CodeVazeiat] AS v
       ON v.CodeVazeiat = pr.CodeVazeiat
WHERE (p.cc_personel IS NULL OR pr.ccPersonel = p.cc_personel)
  AND (pr.TarikhEnfesal IS NULL OR pr.TarikhEnfesal > p.as_of)
ORDER BY a.LName, a.FName;
```

> **`Global.Afrad` وجود دارد و ستون‌هایش تأیید شده‌اند** — `ccAfrad`،
> `FName`، `LName`، `CodeMely`، `Mobile` (از فهرست اشیای `PegahAI`). پس این
> `JOIN` مسیرِ درست است. اگر با این حال همه‌جا `NULL` داد، مشکل در داده است
> نه در مسیر — با شمردنِ یتیم‌ها (کوئری ۹.۲) اندازه‌اش بگیر.

> بدون فیلتر `TarikhEnfesal`، همه‌ی کارکنانِ رفته هم می‌آیند. و یادت باشد
> متقاضیانِ استخدام هم رکورد `Personel` دارند — `CodeVazeiat` جدایشان می‌کند.

---

## ۲. جایگاه سازمانی

### ۲.۱ کجای چارت است، در یک تاریخ

```sql
WITH params AS (
    SELECT CAST('2026-08-22' AS date) AS as_of,
           CAST(NULL AS int)          AS cc_vahed
)
SELECT hp.ccPersonel,
       a.FName, a.LName,
       vs.ccVahedSazmani, vs.NameVahedSazmani,
       po.ccPost, po.NamePost,
       sh.NameShoghl,
       hp.FromDate, hp.EndDate
FROM [HumanResource].[PersonelHokmPostVahedSazmani] AS hp
CROSS JOIN params AS p
JOIN [HumanResource].[Personel]      AS pr ON pr.ccPersonel = hp.ccPersonel
LEFT JOIN [Global].[Afrad]           AS a  ON a.ccAfrad = pr.ccAfrad
LEFT JOIN [HumanResource].[Post]     AS po ON po.ccPost = hp.ccPost
LEFT JOIN [HumanResource].[Shoghl]   AS sh ON sh.ccShoghl = po.ccShoghl
LEFT JOIN [HumanResource].[VahedSazmani] AS vs ON vs.ccVahedSazmani = hp.ccVahedSazmani
WHERE hp.FromDate <= p.as_of
  AND (hp.EndDate IS NULL OR hp.EndDate > p.as_of)
  AND (p.cc_vahed IS NULL OR hp.ccVahedSazmani = p.cc_vahed)
ORDER BY vs.NameVahedSazmani, a.LName;
```

**`CodeVazeiat` عمداً فیلتر نشده** — اول کوئری ۰.۷ را روی
`PersonelHokmPostVahedSazmani_CodeVazeiat` بزن، کدِ تأییدشده را پیدا کن و
اینجا اضافه کن. بدون آن، احکامِ باطل هم می‌آیند.

### ۲.۲ زیرمجموعه‌های یک واحد — درختِ سازمانی

```sql
WITH params AS (SELECT 1 AS cc_vahed_rishe),
derakht AS (
    SELECT v.ccVahedSazmani, v.NameVahedSazmani, v.ccVahedSazmaniLink, 0 AS sath
    FROM [HumanResource].[VahedSazmani] AS v
    CROSS JOIN params AS p
    WHERE v.ccVahedSazmani = p.cc_vahed_rishe
    UNION ALL
    SELECT c.ccVahedSazmani, c.NameVahedSazmani, c.ccVahedSazmaniLink, d.sath + 1
    FROM [HumanResource].[VahedSazmani] AS c
    JOIN derakht AS d ON c.ccVahedSazmaniLink = d.ccVahedSazmani
    WHERE d.sath < 20
)
SELECT sath, ccVahedSazmani, NameVahedSazmani
FROM derakht
ORDER BY sath, NameVahedSazmani;
```

`sath < 20` محافظِ حلقه است. اگر به آن خورد یعنی درخت چرخه دارد — خودش یک
یافته‌ی کیفیت داده است و باید گزارش شود.

### ۲.۳ تعداد نفرات هر واحد در یک تاریخ

```sql
WITH params AS (SELECT CAST('2026-08-22' AS date) AS as_of)
SELECT vs.ccVahedSazmani,
       vs.NameVahedSazmani,
       COUNT(DISTINCT hp.ccPersonel) AS tedad_nafar
FROM [HumanResource].[PersonelHokmPostVahedSazmani] AS hp
CROSS JOIN params AS p
JOIN [HumanResource].[VahedSazmani] AS vs ON vs.ccVahedSazmani = hp.ccVahedSazmani
WHERE hp.FromDate <= p.as_of
  AND (hp.EndDate IS NULL OR hp.EndDate > p.as_of)
GROUP BY vs.ccVahedSazmani, vs.NameVahedSazmani
ORDER BY tedad_nafar DESC;
```

`COUNT(DISTINCT ccPersonel)` عمدی است: یک نفر می‌تواند در یک تاریخ چند حکمِ
هم‌پوشان داشته باشد. با `COUNT(*)` دو بار شمرده می‌شود — و همین را با
کوئری ۹.۱ چک کن.

---

## ۳. قرارداد

```sql
WITH params AS (SELECT CAST('2026-08-22' AS date) AS as_of)
SELECT g.ccPersonel,
       a.FName, a.LName,
       ne.NameNoeEstekhdam,
       g.ShomareGharardad,
       g.FromDate, g.EndDate,
       g.CodeVaziat,
       g.IsTasvieh
FROM [HumanResource].[PersonelGharardad] AS g
CROSS JOIN params AS p
JOIN [HumanResource].[Personel] AS pr ON pr.ccPersonel = g.ccPersonel
LEFT JOIN [Global].[Afrad]      AS a  ON a.ccAfrad = pr.ccAfrad
LEFT JOIN [HumanResource].[NoeEstekhdam] AS ne
       ON ne.ccNoeEstekhdam = g.ccNoeEstekhdam
WHERE g.FromDate <= p.as_of
  AND g.EndDate  >  p.as_of        -- EndDate اینجا NOT NULL است
ORDER BY a.LName;
```

> **`PersonelGharardad.EndDate` تهی‌پذیر نیست.** الگوی `EndDate IS NULL` اینجا
> جواب نمی‌دهد. قراردادِ باز احتمالاً با تاریخِ دور نشان داده می‌شود؛ توزیعش را
> ببین:
> `SELECT TOP 20 EndDate, COUNT(*) FROM [HumanResource].[PersonelGharardad] GROUP BY EndDate ORDER BY COUNT(*) DESC`

---

## ۴. حقوق مصوب در یک تاریخ

```sql
WITH params AS (
    SELECT CAST('2026-08-22' AS date) AS as_of,
           CAST(NULL AS int)          AS cc_personel
)
SELECT hh.ccPersonel,
       a.FName, a.LName,
       hh.FromDate, hh.EndDate,
       hh.MablaghMozdeShoghl,
       hh.MablaghSanavat,
       hh.MablaghHaghFanni,
       gs.NameGorohShoghli,
       hh.CodeVazeiat
FROM [HumanResource].[PersonelHokmHoghogh] AS hh
CROSS JOIN params AS p
JOIN [HumanResource].[Personel] AS pr ON pr.ccPersonel = hh.ccPersonel
LEFT JOIN [Global].[Afrad]      AS a  ON a.ccAfrad = pr.ccAfrad
LEFT JOIN [HumanResource].[GorohShoghli] AS gs
       ON gs.ccGorohShoghli = hh.ccGorohShoghli
WHERE hh.FromDate <= p.as_of
  AND (hh.EndDate IS NULL OR hh.EndDate > p.as_of)
  AND hh.ZamanGheirFaali IS NULL
  AND (p.cc_personel IS NULL OR hh.ccPersonel = p.cc_personel)
ORDER BY a.LName;
```

**سه فیلتر با هم:** بازه، `ZamanGheirFaali`، و `CodeVazeiat` (که باید بعد از
خواندن `PersonelHokmHoghogh_CodeVazeiat` اضافه شود).

### ۴.۱ اقلام حکم

```sql
WITH params AS (SELECT CAST(0 AS int) AS cc_hokm_hoghogh)   -- شناسه‌ی حکم
SELECT ih.CodeItemHoghogh,
       ih.NameItemHoghogh_Farsi,
       s.Meghdar,
       ih.IsMazaya, ih.IsKosorat, ih.Noe_Roozaneh_Mahaneh
FROM [HumanResource].[PersonelHokmHoghoghSatr] AS s
CROSS JOIN params AS p
JOIN [HumanResource].[ItemHoghogh] AS ih ON ih.ccItemHoghogh = s.ccItemHoghogh
WHERE s.ccPersonelHokmHoghogh = p.cc_hokm_hoghogh
ORDER BY ih.OlaviatNamayesh, ih.CodeItemHoghogh;
```

---

## ۵. پرداخت واقعی

### ۵.۱ دانه را اول بشمار — قبل از هر `SUM`

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah)
SELECT COUNT(*)                          AS tedad_satr,
       COUNT(DISTINCT ph.ccPersonel)     AS tedad_nafar,
       CAST(COUNT(*) AS decimal(18,2))
         / NULLIF(COUNT(DISTINCT ph.ccPersonel), 0) AS satr_be_ezaye_nafar,
       COUNT(DISTINCT ph.ccNoePardakhti) AS tedad_noe_pardakhti,
       COUNT(DISTINCT ph.CodeNoeRecord)  AS tedad_noe_record,
       COUNT(DISTINCT ph.ccMarkaz)       AS tedad_markaz
FROM [HumanResource].[PardakhtHoghogh] AS ph
CROSS JOIN params AS p
WHERE ph.Sal = p.sal AND ph.Mah = p.mah;
```

> **اگر `satr_be_ezaye_nafar` بزرگ‌تر از ۱ بود، «حقوق ماهانه‌ی هر نفر» یک سطر
> نیست.** قبل از هر جمعی باید بفهمی کدام ستون سطرها را از هم جدا می‌کند —
> `ccNoePardakhti`، `CodeNoeRecord` یا `ccMarkaz`. جمع زدنِ کورکورانه یعنی
> حقوقِ چندبرابر.

### ۵.۲ ستون‌های پهن در برابر سطرِ اقلام — کدام مرجع است

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah),
sarbarg AS (
    SELECT ph.ccPardakhtHoghogh, ph.ccPersonel, ph.MablaghKhalesPardakhti
    FROM [HumanResource].[PardakhtHoghogh] AS ph
    CROSS JOIN params AS p
    WHERE ph.Sal = p.sal AND ph.Mah = p.mah
),
satr AS (
    SELECT s.ccPardakhtHoghogh,
           SUM(CASE WHEN ih.IsMazaya  = 1 THEN s.Meghdar ELSE 0 END) AS jam_mazaya,
           SUM(CASE WHEN ih.IsKosorat = 1 THEN s.Meghdar ELSE 0 END) AS jam_kosorat,
           COUNT(*) AS tedad_item
    FROM [HumanResource].[PardakhtHoghoghSatr] AS s
    JOIN [HumanResource].[ItemHoghogh] AS ih ON ih.ccItemHoghogh = s.ccItemHoghogh
    GROUP BY s.ccPardakhtHoghogh
)
SELECT COUNT(*) AS tedad_barresi_shode,
       SUM(CASE WHEN st.ccPardakhtHoghogh IS NULL THEN 1 ELSE 0 END) AS bedone_satr,
       SUM(CASE WHEN ABS(ISNULL(sb.MablaghKhalesPardakhti, 0)
                       - (ISNULL(st.jam_mazaya, 0) - ISNULL(st.jam_kosorat, 0))) > 1
                THEN 1 ELSE 0 END) AS tedad_moghayer
FROM sarbarg AS sb
LEFT JOIN satr AS st ON st.ccPardakhtHoghogh = sb.ccPardakhtHoghogh;
```

سه نتیجه‌ی ممکن، و هرکدام معنیِ متفاوتی دارد:

- **`bedone_satr` بزرگ** → سطرِ اقلام برای این دوره پر نشده؛ ستون‌های پهن مرجع‌اند.
- **`tedad_moghayer` صفر** → هر دو یکی‌اند؛ هرکدام را خواستی بگیر، ولی **فقط
  یکی**.
- **`tedad_moghayer` بزرگ** → تعریفِ «خالص» با جمعِ اقلام فرق دارد. تا معلوم
  نشده چرا، هیچ‌کدام را گزارش نکن.

> `IsMazaya`/`IsKosorat` هر دو `tinyint`اند و مقدارشان تأیید نشده. اگر نتیجه
> بی‌معنی بود، اول `SELECT DISTINCT IsMazaya, IsKosorat, COUNT(*) FROM ItemHoghogh
> GROUP BY IsMazaya, IsKosorat` را ببین.

### ۵.۳ در فیش این ماه چه چیزهایی نشست — جست‌وجوی معکوس

`PardakhtHoghogh` مقصد است؛ برای دیدن آنچه به آن گره خورده باید از طرفِ
فرزندها بروی:

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah),
ph AS (
    SELECT x.ccPardakhtHoghogh
    FROM [HumanResource].[PardakhtHoghogh] AS x
    CROSS JOIN params AS p
    WHERE x.Sal = p.sal AND x.Mah = p.mah
)
SELECT 'قسط وام' AS mabna, COUNT(*) AS tedad, SUM(v.MablaghGhestPardakhti) AS mablagh
FROM [HumanResource].[DarkhastVamPardakhtAghsat] AS v
JOIN ph ON ph.ccPardakhtHoghogh = v.ccPardakhtHoghogh
UNION ALL
SELECT 'صندوق رفاه', COUNT(*), SUM(sr.MablaghPersonel)
FROM [HumanResource].[SandoghRefah] AS sr
JOIN ph ON ph.ccPardakhtHoghogh = sr.ccPardakhtHoghogh
UNION ALL
SELECT 'مانده مرخصی', COUNT(*), NULL
FROM [HumanResource].[PersonelMandehMorakhasi] AS mm
JOIN ph ON ph.ccPardakhtHoghogh = mm.ccPardakhtHoghogh;
```

توجه: `ccPardakhtHoghogh` در این جدول‌ها گاهی `int` و گاهی `bigint` است
(بخش ۴.۳ [relationships.md](relationships.md)). اگر خطای تبدیل گرفتی، همان است.

---

## ۶. کارکرد و مرخصی

### ۶.۱ کارکرد یک ماه، با روز کاریِ تقویم

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah),
rooz_kari AS (
    SELECT COUNT(*) AS tedad_rooz_kari
    FROM [Global].[Taghvim] AS t
    CROSS JOIN params AS p
    WHERE t.Sal = p.sal AND t.Mah = p.mah
      AND t.CodeNoeTatili IS NULL
)
SELECT k.ccPersonel,
       a.FName, a.LName,
       rk.tedad_rooz_kari,
       COUNT(*)                                  AS rooz_dara_satr,
       SUM(k.Karkard_Daghigheh)      / 60.0      AS saat_karkard,
       SUM(k.EzafehKar_Daghigheh)    / 60.0      AS saat_ezafehkar,
       SUM(k.Takhir_Daghigheh)       / 60.0      AS saat_takhir,
       SUM(k.Gheybat_Daghigheh)      / 60.0      AS saat_gheybat,
       SUM(k.Morakhasi_Daghigheh)    / 60.0      AS saat_morakhasi
FROM [HumanResource].[PersonelKarkard] AS k
CROSS JOIN params AS p
CROSS JOIN rooz_kari AS rk
JOIN [HumanResource].[Personel] AS pr ON pr.ccPersonel = k.ccPersonel
LEFT JOIN [Global].[Afrad]      AS a  ON a.ccAfrad = pr.ccAfrad
WHERE k.Sal = p.sal AND k.Mah = p.mah
GROUP BY k.ccPersonel, a.FName, a.LName, rk.tedad_rooz_kari
ORDER BY saat_ezafehkar DESC;
```

> **`rooz_dara_satr` را با `tedad_rooz_kari` اشتباه نگیر.** اولی روزهایی است که
> سطر دارند و دومی روزهای کاریِ تقویم. اختلافشان یعنی روزِ بی‌سطر — که ممکن
> است غیبت باشد یا نبودِ داده. این دو یکی نیستند.

> `Sal`/`Mah` در این جدول شمسی است یا میلادی؟ **تأیید بگیر.** یک نفر و یک ماه
> را با `Tarikh` و `TarikhKarkard_Shamsi` کنار هم بگذار.

### ۶.۲ مانده‌ی مرخصی — دفترِ بد/بس

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_personel)
SELECT mm.ccPersonel,
       a.FName, a.LName,
       nm.NameNoeMorakhasi,
       SUM(CASE WHEN mm.BedBes = 1 THEN  mm.ZamanMorakhasi
                                   ELSE -mm.ZamanMorakhasi END) / 60.0 AS mandeh_saat,
       COUNT(*) AS tedad_gardesh
FROM [HumanResource].[PersonelMandehMorakhasi] AS mm
CROSS JOIN params AS p
JOIN [HumanResource].[Personel] AS pr ON pr.ccPersonel = mm.ccPersonel
LEFT JOIN [Global].[Afrad]      AS a  ON a.ccAfrad = pr.ccAfrad
LEFT JOIN [HumanResource].[NoeMorakhasi] AS nm
       ON nm.ccNoeMorakhasi = mm.ccNoeMorakhasi
WHERE (p.cc_personel IS NULL OR mm.ccPersonel = p.cc_personel)
GROUP BY mm.ccPersonel, a.FName, a.LName, nm.NameNoeMorakhasi
ORDER BY mandeh_saat;
```

> **جهتِ `BedBes` حدس زده شده.** اینجا `1` بستانکار فرض شده. اگر مانده‌ها همه
> منفی درآمدند، جهت برعکس است. با یک نفرِ شناخته‌شده اعتبارسنجی کن، و **تا وقتی
> جهت تأیید نشده این عدد را گزارش نکن** — علامتِ اشتباه یعنی طلبکار را بدهکار
> نشان دادن.

> واحد `ZamanMorakhasi` دقیقه فرض شده. اگر عددها هزاران ساعت درآمدند، واحد
> چیز دیگری است.

---

## ۷. وام — مانده

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_personel),
aghsat AS (
    SELECT a.ccDarkhastVam,
           SUM(a.MablaghGhestPardakhti) AS jam_pardakht_shode,
           COUNT(*)                     AS tedad_ghest_pardakhti,
           MAX(a.TarikhPardakhtGhest)   AS akharin_ghest
    FROM [HumanResource].[DarkhastVamPardakhtAghsat] AS a
    GROUP BY a.ccDarkhastVam
)
SELECT v.ccDarkhastVam,
       v.ccPersonel,
       a2.FName, a2.LName,
       nv.NameNoeVam,
       v.MablaghVamPardakhtiBePersonel                       AS mablagh_vam,
       ISNULL(ag.jam_pardakht_shode, 0)                      AS pardakht_shode,
       v.MablaghVamPardakhtiBePersonel
         - ISNULL(ag.jam_pardakht_shode, 0)                  AS mandeh,
       v.TedadAghsat,
       ISNULL(ag.tedad_ghest_pardakhti, 0)                   AS ghest_pardakhti,
       ag.akharin_ghest,
       v.CodeVazeiat
FROM [HumanResource].[DarkhastVam] AS v
CROSS JOIN params AS p
LEFT JOIN aghsat AS ag ON ag.ccDarkhastVam = v.ccDarkhastVam
JOIN [HumanResource].[Personel] AS pr ON pr.ccPersonel = v.ccPersonel
LEFT JOIN [Global].[Afrad]      AS a2 ON a2.ccAfrad = pr.ccAfrad
LEFT JOIN [HumanResource].[NoeVam] AS nv ON nv.ccNoeVam = v.ccNoeVam
WHERE (p.cc_personel IS NULL OR v.ccPersonel = p.cc_personel)
  AND v.MablaghVamPardakhtiBePersonel > ISNULL(ag.jam_pardakht_shode, 0)
ORDER BY mandeh DESC;
```

> **`CodeVazeiat` فیلتر نشده.** وامِ رد‌شده و باطل هم در این فهرست‌اند. کد
> تأییدشده را از `DarkhastVam_CodeVazeiat` بردار و اضافه کن، وگرنه «مانده‌ی
> وام» شامل وام‌هایی است که اصلاً پرداخت نشده‌اند.

> **`DarkhastVamSatr` را به این join نکن** — زیرِ `DarkhastVam` نیست، زیرِ
> `DarkhastAzSandoghRefah` است.

---

## ۸. پل به فروش — پرونده‌ی پرسنلی کنارِ عملکرد فروش

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
),
forosh AS (
    SELECT f.ccAfradForoshandeh,
           SUM(f.Rial)                     AS jam_rial,
           COUNT(DISTINCT f.ccDarkhastFaktor) AS tedad_faktor
    FROM [Sales].[AmarForosh_Arshive] AS f
    CROSS JOIN params AS p
    WHERE f.Tarikh >= p.az_tarikh AND f.Tarikh <= p.ta_tarikh
      AND f.IsMarjoee = 0
    GROUP BY f.ccAfradForoshandeh
)
SELECT pr.ccPersonel,
       pr.ShomarehPersonely,
       a.FName, a.LName,
       pr.TarikhEstekhdam,
       fo.tedad_faktor,
       fo.jam_rial
FROM [HumanResource].[Personel] AS pr
JOIN [Global].[Afrad] AS a ON a.ccAfrad = pr.ccAfrad
JOIN forosh AS fo          ON fo.ccAfradForoshandeh = pr.ccAfrad
ORDER BY fo.jam_rial DESC;
```

> **این کوئری بیش از بقیه محتاجِ تأیید است.** دو فرض دارد که هیچ‌کدام اثبات
> نشده‌اند: اینکه `Global.Afrad` مقصدِ مشترکِ هر دو است، و اینکه هر دو اسکیما در
> یک دیتابیس‌اند. اول با یک `COUNT` ببین اصلاً چند سطر مشترک درمی‌آید — اگر صفر
> بود، فرض غلط است و **نتیجه‌ی خالی را با «فروشنده‌ای نبود» اشتباه نگیر**.

> `ccForoshandeh` مسیر است و `ccAfradForoshandeh` آدم. برای این پل حتماً دومی.

---

## ۹. کیفیت داده — چیزهایی که باید بدانی

### ۹.۱ بازه‌های هم‌پوشان — یک نفر، دو حکمِ هم‌زمان

```sql
SELECT hp.ccPersonel, COUNT(*) AS tedad_hokm_hampooshan
FROM [HumanResource].[PersonelHokmPostVahedSazmani] AS hp
JOIN [HumanResource].[PersonelHokmPostVahedSazmani] AS hp2
     ON hp2.ccPersonel = hp.ccPersonel
    AND hp2.ccPersonelHokmPostVahedSazmani <> hp.ccPersonelHokmPostVahedSazmani
    AND hp.FromDate < ISNULL(hp2.EndDate, '2999-12-31')
    AND hp2.FromDate < ISNULL(hp.EndDate, '2999-12-31')
GROUP BY hp.ccPersonel
ORDER BY tedad_hokm_hampooshan DESC;
```

هم‌پوشانی همیشه خطا نیست — ممکن است یک نفر واقعاً دو پست هم‌زمان داشته باشد.
ولی **اگر هست، هر کوئریِ «جایگاه در تاریخ» چند سطر برمی‌گرداند** و باید
`COUNT(DISTINCT ccPersonel)` بزنی، نه `COUNT(*)`.

### ۹.۲ ارجاعِ یتیم — به کارمندی که نیست

```sql
SELECT COUNT(*) AS tedad_yatim
FROM [HumanResource].[PardakhtHoghogh] AS ph
LEFT JOIN [HumanResource].[Personel] AS pr ON pr.ccPersonel = ph.ccPersonel
WHERE pr.ccPersonel IS NULL;
```

عددِ غیرصفر یعنی نبودِ کلید خارجی به داده‌ی ناسازگار رسیده. در گزارش بنویس —
جمع‌های گروهی را تحت تأثیر می‌گذارد.

### ۹.۳ داده‌ی انتقال اولیه با داده‌ی جاری قاطی نشده باشد

```sql
SELECT 'EnteghalAvalieh_MandehVam' AS jadval, COUNT(*) AS tedad,
       MIN(Sal) AS az_sal, MAX(Sal) AS ta_sal
FROM [HumanResource].[EnteghalAvalieh_MandehVam]
UNION ALL
SELECT 'EnteghalAvalieh_MandehMorakhasi', COUNT(*), MIN(Sal), MAX(Sal)
FROM [HumanResource].[EnteghalAvalieh_MandehMorakhasi];
```

اگر `ta_sal` نزدیک به امروز بود، این جدول‌ها فقط «انتقال اولیه» نیستند و
دارند به‌روز می‌شوند — که یعنی فرضِ «فقط مهاجرت» غلط است.

---

## اندازه‌ها — برای اینکه بفهمی جواب معقول است

هیچ عددِ مرجعی از داده‌ی واقعی در دست نیست. **بار اول که روی یک دیتابیس زنده
اجرا کردی، این چهار عدد را یادداشت کن و در همین فایل بنویس** تا دفعه‌ی بعد
معیار داشته باشی:

| اندازه | مقدار واقعی |
|---|---|
| تعداد کارمند فعال | ؟ |
| تعداد سطر `PardakhtHoghogh` در یک ماه | ؟ |
| نسبت سطر به نفر در `PardakhtHoghogh` | ؟ |
| تعداد سطر `PersonelKarkard` در یک ماه | ؟ |
