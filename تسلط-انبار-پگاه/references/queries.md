# کوئری‌ها

> **این کوئری‌ها الگو هستند و هنوز اجرا نشده‌اند.** نام جدول‌ها و ستون‌ها از
> فهرست کاملِ اشیای `PegahAI` آمده، پس درست‌اند — ولی خودِ کوئری اجرا نشده.
> **وقتی دسترسی داری اجرایشان کن و بالای هرکدام «تست‌شده» بنویس.**

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود. پارامتر را با `params` بساز.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** موجودی و کاردکس میلیون‌ها سطر
> دارند. **در SQL جمع بزن.**

---

## ۰. تأیید — قبل از هر چیز

### ۰.۱ آخرین تاریخِ داده

```sql
SELECT 'Kardex' AS jadval, MAX(TarikhForm) AS akharin FROM [Warehouse].[Kardex]
UNION ALL SELECT 'MojodyForosh', MAX(Tarikh)    FROM [Warehouse].[MojodyForosh]
UNION ALL SELECT 'Sefaresh',     MAX(TarikhSefaresh) FROM [Warehouse].[Sefaresh]
UNION ALL SELECT 'AnbarGardany', MAX(TarikhPaian)    FROM [Warehouse].[AnbarGardany]
ORDER BY akharin DESC;
```

### ۰.۲ سه ستون تعداد — کدام پر است و آیا یکی‌اند

**قبل از هر گزارشِ مقداری این را بزن.** جوابش تعیین می‌کند کل گزارش را با
کدام ستون بنویسی.

```sql
SELECT TOP 200
       s.Tedad1, s.Tedad2, s.Tedad3,
       CASE WHEN s.Tedad1 = s.Tedad2 AND s.Tedad2 = s.Tedad3
            THEN N'هر سه یکی' ELSE N'متفاوت' END AS vazeiat
FROM [Warehouse].[KardexSatr] AS s
WHERE s.Tedad1 IS NOT NULL;
```

و توزیعِ کلی:

```sql
SELECT COUNT(*)                                                  AS kol,
       SUM(CASE WHEN Tedad2 IS NULL THEN 1 ELSE 0 END)           AS tedad2_khali,
       SUM(CASE WHEN Tedad3 IS NULL THEN 1 ELSE 0 END)           AS tedad3_khali,
       SUM(CASE WHEN Tedad1 = Tedad2 AND Tedad2 = Tedad3
                THEN 1 ELSE 0 END)                               AS har_se_yeki
FROM [Warehouse].[KardexSatr];
```

اگر `har_se_yeki` نزدیک `kol` بود، `Tedad1` را بگیر و تمام. اگر نه، **بپرس
کدام واحد مبناست**.

### ۰.۳ سه ستون قیمت — همان آزمون

```sql
SELECT COUNT(*)                                        AS kol,
       SUM(CASE WHEN Gheymat  IS NULL THEN 1 ELSE 0 END) AS g1_khali,
       SUM(CASE WHEN Gheymat2 IS NULL THEN 1 ELSE 0 END) AS g2_khali,
       SUM(CASE WHEN Gheymat3 IS NULL THEN 1 ELSE 0 END) AS g3_khali
FROM [Warehouse].[KardexSatr];
```

### ۰.۴ انواع عملیات کاردکس — جهتِ حرکت

```sql
SELECT k.CodeNoeAmalyat, COUNT(*) AS tedad
FROM [Warehouse].[Kardex] AS k
GROUP BY k.CodeNoeAmalyat
ORDER BY tedad DESC;
```

و دیکشنری:

```sql
SELECT ccNoeKardex, NameNoeKardex, IsYekTarafe FROM [Warehouse].[NoeKardex]
ORDER BY ccNoeKardex;
```

**بدون فیلترِ نوع عملیات، ورود و خروج و انتقال با هم جمع می‌شوند.**

### ۰.۵ دیکشنری وضعیت

```sql
SELECT ccKardexVazeiat, NameKardexVazeiat, CodeVazeiat
FROM [Warehouse].[KardexVazeiat] ORDER BY CodeVazeiat;
```

کدها بین `KardexVazeiat`، `VazeiatSefaresh` و `VazeiatMarjoeeFaktor` یکسان
**نیستند**.

### ۰.۶ علت مرجوعی و مسئولیت

```sql
SELECT e.ccElatMarjoeeKala, e.Sharh, e.MasoleiatElat,
       e.IsZayeat, e.IsZayeatTolid
FROM [Warehouse].[ElatMarjoeeKala] AS e
ORDER BY e.MasoleiatElat, e.ccElatMarjoeeKala;
```

`MasoleiatElat`: **۱ فروش**، ۲ پخش، ۳ تولید، ۴ فروش و پخش، ۰ نامشخص.

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
WHERE OBJECT_SCHEMA_NAME(fkc.parent_object_id) = 'Warehouse'
ORDER BY ParentTable, ParentColumn;
```

---

## ۱. گردش انبار در یک بازه

```sql
WITH params AS (
    SELECT CAST('2026-08-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh,
           CAST(NULL AS int)          AS cc_anbar   -- NULL = همه‌ی انبارها
)
SELECT k.ccAnbar,
       a.NameAnbar,
       k.CodeNoeAmalyat,
       COUNT(DISTINCT k.ccKardex) AS tedad_sanad,
       COUNT(*)                   AS tedad_satr,
       SUM(s.Tedad1)              AS jam_tedad
FROM [Warehouse].[Kardex] AS k
CROSS JOIN params AS p
JOIN [Warehouse].[KardexSatr] AS s ON s.ccKardex = k.ccKardex
LEFT JOIN [Warehouse].[Anbar] AS a ON a.ccAnbar = k.ccAnbar
WHERE k.TarikhForm >= p.az_tarikh AND k.TarikhForm <= p.ta_tarikh
  AND (p.cc_anbar IS NULL OR k.ccAnbar = p.cc_anbar)
GROUP BY k.ccAnbar, a.NameAnbar, k.CodeNoeAmalyat
ORDER BY a.NameAnbar, k.CodeNoeAmalyat;
```

**`CodeVazeiat` عمداً فیلتر نشده** — اول کوئری ۰.۵ را بزن و کدِ تأییدشده را
اضافه کن، وگرنه اسنادِ باطل هم می‌آیند.

`tedad_sanad` کنارِ `tedad_satr` عمدی است: نسبتشان می‌گوید هر سند چند سطر
دارد.

## ۲. موجودیِ الان — نه جمعِ همه‌ی روزها

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_markaz),
akharin AS (
    SELECT MAX(Tarikh) AS tarikh FROM [Warehouse].[MojodyForosh]
)
SELECT m.ccMarkazPakhsh,
       m.ccKalaCode,
       k.NameKala,
       SUM(m.Mojody) AS mojody
FROM [Warehouse].[MojodyForosh] AS m
CROSS JOIN params AS p
CROSS JOIN akharin AS t
LEFT JOIN [Warehouse].[Kala] AS k ON k.ccKalaCode = m.ccKalaCode
WHERE m.Tarikh = t.tarikh
  AND (p.cc_markaz IS NULL OR m.ccMarkazPakhsh = p.cc_markaz)
GROUP BY m.ccMarkazPakhsh, m.ccKalaCode, k.NameKala
ORDER BY mojody DESC;
```

سه نکته:

- **`m.Tarikh = آخرین تاریخ`** — بدون آن، موجودیِ همه‌ی روزها جمع می‌شود.
- **`k.ccKalaCode = m.ccKalaCode`** — نه `ccKala`. کلیدِ اقمار همین است.
- `SUM` روی بچ و قسمتِ انبار جمع می‌کند؛ اگر تفکیک می‌خواهی آنها را هم به
  `GROUP BY` اضافه کن.

## ۳. کالای نزدیک انقضا

```sql
WITH params AS (SELECT 60 AS rooz_baghimandeh)
SELECT b.ccKalaCode,
       k.NameKala,
       b.ShomarehBach,
       b.TarikhTolid,
       b.TarikhEngheza,
       DATEDIFF(day, GETDATE(), b.TarikhEngheza) AS rooz_ta_engheza
FROM [Warehouse].[KalaShomarehBach] AS b
CROSS JOIN params AS p
LEFT JOIN [Warehouse].[Kala] AS k ON k.ccKalaCode = b.ccKalaCode
WHERE b.TarikhEngheza IS NOT NULL
  AND b.TarikhEngheza >= GETDATE()
  AND DATEDIFF(day, GETDATE(), b.TarikhEngheza) <= p.rooz_baghimandeh
ORDER BY b.TarikhEngheza;
```

> این فقط می‌گوید **بچ** نزدیک انقضاست، نه اینکه **موجودی دارد**. برای
> موجودیِ آن بچ به `MojodyForosh` روی `ccKalaCode` + `ShomarehBach` وصل شو.

## ۴. مرجوعی به تفکیک مسئولیت

```sql
WITH params AS (
    SELECT CAST('2026-06-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT e.MasoleiatElat,
       e.Sharh,
       COUNT(*)      AS tedad_satr,
       SUM(s.Tedad1) AS tedad_kala
FROM [Warehouse].[Kardex] AS k
CROSS JOIN params AS p
JOIN [Warehouse].[KardexSatr] AS s ON s.ccKardex = k.ccKardex
JOIN [Warehouse].[ElatMarjoeeKala] AS e
     ON e.ccElatMarjoeeKala = s.ccElat
WHERE k.TarikhForm >= p.az_tarikh AND k.TarikhForm <= p.ta_tarikh
GROUP BY e.MasoleiatElat, e.Sharh
ORDER BY e.MasoleiatElat, tedad_kala DESC;
```

> **`s.ccElat` به `ElatMarjoeeKala` وصل می‌شود — این حدس است.** `ccElat` نامِ
> کوتاه‌شده است و قاعده‌ی `ccX → X` به آن نمی‌رسد. با آزمونِ یتیم (۹.۱)
> تأییدش کن قبل از اینکه گزارش بدهی.

## ۵. سفارش انبار و منشأش در فروش

```sql
WITH params AS (
    SELECT CAST('2026-08-01' AS date) AS az_tarikh,
           CAST('2026-08-30' AS date) AS ta_tarikh
)
SELECT s.ccMarkazPakhsh,
       s.CodeNoeSefaresh,
       s.CodeVazeiat,
       COUNT(DISTINCT s.ccSefaresh)      AS tedad_sefaresh,
       COUNT(DISTINCT s.ccDarkhastFaktor) AS tedad_faktor_forosh,
       SUM(ss.Tedad1)                    AS jam_tedad
FROM [Warehouse].[Sefaresh] AS s
CROSS JOIN params AS p
JOIN [Warehouse].[SefareshSatr] AS ss ON ss.ccSefaresh = s.ccSefaresh
WHERE s.TarikhSefaresh >= p.az_tarikh AND s.TarikhSefaresh <= p.ta_tarikh
GROUP BY s.ccMarkazPakhsh, s.CodeNoeSefaresh, s.CodeVazeiat
ORDER BY tedad_sefaresh DESC;
```

`ccDarkhastFaktor` پل به `Sales.DarkhastFaktor` است — سفارشِ انبار از فاکتور
فروش می‌آید.

## ۹. کیفیت داده

### ۹.۱ ارجاعِ یتیم — اعتبارسنجیِ یال

```sql
SELECT COUNT(*) AS kol,
       SUM(CASE WHEN k.ccKalaCode IS NULL THEN 1 ELSE 0 END) AS yatim
FROM [Warehouse].[KardexSatr] AS s
LEFT JOIN [Warehouse].[Kala] AS k ON k.ccKalaCode = s.ccKalaCode
WHERE s.ccKalaCode IS NOT NULL;
```

این را روی یال‌های پرکاربرد بزن: `ccKalaCode`، `ccAnbar`، `ccKardex`،
`ccElat`، `ccTaminKonandeh`. **نسبتِ یتیمِ بالا یعنی یال غلط است.**

### ۹.۲ دانه — قبل از هر `SUM`

```sql
SELECT COUNT(*)                          AS satr,
       COUNT(DISTINCT s.ccKardex)        AS sanad,
       COUNT(DISTINCT s.ccKalaCode)      AS kala,
       COUNT(DISTINCT CONCAT(s.ccKalaCode, '|', s.ShomarehBach)) AS kala_bach
FROM [Warehouse].[KardexSatr] AS s;
```

`kala_bach` بزرگ‌تر از `kala` یعنی **بچ دانه را ضرب می‌کند** — که در این
اسکیما عادی است. اگر گزارش در سطح کالاست، روی بچ جمع بزن.

## اندازه‌ها

| اندازه | مقدار واقعی |
|---|---|
| آخرین تاریخِ `Kardex` | ؟ |
| نسبت `Tedad1`=`Tedad2`=`Tedad3` | ؟ |
| میانگین سطر به ازای هر سند کاردکس | ؟ |
| تعداد بچِ فعال | ؟ |
