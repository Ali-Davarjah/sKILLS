# کوئری‌ها

> **این کوئری‌ها الگو هستند و هنوز اجرا نشده‌اند.** نام جدول‌ها و ستون‌ها از
> فهرست کاملِ اشیای `PegahAI` آمده، پس درست‌اند — ولی خودِ کوئری اجرا نشده.
> **وقتی دسترسی داری اجرایشان کن و بالای هرکدام «تست‌شده» بنویس.**

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** جدول‌های مرجعِ این اسکیما
> کوچک‌اند، ولی `Taghvim` و `Afrad` نه.

---

## ۰. تأیید — قبل از هر چیز

### ۰.۱ `Goroh` چند تاکسونومی دارد — **مهم‌ترین کوئری این صفحه**

```sql
SELECT g.ccGorohLink,
       COUNT(*)          AS tedad_goroh,
       MIN(g.NameGoroh)  AS nemooneh_1,
       MAX(g.NameGoroh)  AS nemooneh_2
FROM [Global].[Goroh] AS g
GROUP BY g.ccGorohLink
ORDER BY tedad_goroh DESC;
```

انتظار: **۵۶۰** گروه کالا (حدود ۵۵ سطر) و **۳۰۴** نوع مشتری. بقیه‌ی مقادیر
را با نمونه‌ی نامشان تشخیص بده — و **اگر معنی‌شان معلوم نشد، بپرس**.

بدون این فیلتر، گروه کالا و نوع مشتری در یک جدول قاطی‌اند و چون هر دو
`NameGoroh` دارند، **خطا دیده نمی‌شود**.

### ۰.۲ `Markaz` در برابر `MarkazPakhsh`

```sql
SELECT 'Markaz' AS jadval, COUNT(*) AS tedad FROM [Global].[Markaz]
UNION ALL
SELECT 'MarkazPakhsh', COUNT(*) FROM [Global].[MarkazPakhsh];
```

و نسبتشان — آیا اصلاً به هم وصل‌اند؟

```sql
SELECT COUNT(*) AS markaz_ba_markazpakhsh_old
FROM [Global].[Markaz] AS m
JOIN [Global].[MarkazPakhsh] AS p
  ON p.ccMarkazPakhsh = m.ccMarkazPakhsh_Old;
```

> **`ccMarkazPakhsh_Old` ستونِ مرده است** و این کوئری فقط برای فهمیدنِ
> رابطه‌ی تاریخی است — **برای اتصال در گزارش از آن استفاده نکن**.

### ۰.۳ سلسله‌مراتب سازمانی — کدام سطح چند تا دارد

```sql
SELECT 'MantaghehPakhsh' AS sath, COUNT(*) AS tedad FROM [Global].[MantaghehPakhsh]
UNION ALL SELECT 'MarkazPakhsh',    COUNT(*) FROM [Global].[MarkazPakhsh]
UNION ALL SELECT 'Houzeh',          COUNT(*) FROM [Global].[Houzeh]
UNION ALL SELECT 'MantaghehForosh', COUNT(*) FROM [Global].[MantaghehForosh]
UNION ALL SELECT 'HouzehForosh',    COUNT(*) FROM [Global].[HouzehForosh]
UNION ALL SELECT 'SazmanForosh',    COUNT(*) FROM [Global].[SazmanForosh]
UNION ALL SELECT 'Markaz',          COUNT(*) FROM [Global].[Markaz]
ORDER BY tedad DESC;
```

عددها می‌گویند کدام سطح ریزتر است — و کدام سلسله‌مراتب برای سؤالِ تو مناسب.

### ۰.۴ تقویم — پوشش و شکلِ تاریخ

```sql
SELECT MIN(t.Tarikh)        AS az,
       MAX(t.Tarikh)        AS ta,
       MIN(t.TarikhShamsi)  AS az_shamsi,
       MAX(t.TarikhShamsi)  AS ta_shamsi,
       COUNT(*)             AS tedad_rooz
FROM [Global].[Taghvim] AS t;
```

`TarikhShamsi` باید عددی مثل `14050531` بدهد. **اگر با رشته مقایسه‌اش کنی،
بی‌صدا شکست می‌خورد.**

و روز کاری:

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah)
SELECT COUNT(*) AS rooz_dar_mah
FROM [Global].[Taghvim] AS t
CROSS JOIN params AS p
WHERE t.Sal = p.sal AND t.Mah = p.mah;
```

برای تعطیلات به `TaghvimTatil` وصل شو — و اگر عددِ روز کاری در محاسبه‌ای
می‌رود، `TaghvimTatilManabeEnsani` را هم بگیر و اختلاف را ببین.

### ۰.۵ فیلترِ فعال — پنج اسمِ متفاوت

```sql
SELECT 'SazmanForosh' AS jadval, COUNT(*) AS kol,
       SUM(CASE WHEN Faal = 1 THEN 1 ELSE 0 END) AS faal
FROM [Global].[SazmanForosh]
UNION ALL
SELECT 'Markaz', COUNT(*), SUM(CASE WHEN Faal = 1 THEN 1 ELSE 0 END)
FROM [Global].[Markaz]
UNION ALL
SELECT 'Bank', COUNT(*), SUM(CASE WHEN IsActive = 1 THEN 1 ELSE 0 END)
FROM [Global].[Bank];
```

`Goroh` دو پرچم دارد (`CheckFaal` و `GhabeleEstefade`) و `ShomarehHesab` هم
`Faal` و `Faal2`. **کدام مبناست را تأیید بگیر.**

### ۰.۶ کلید خارجی واقعی

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
WHERE OBJECT_SCHEMA_NAME(fkc.referenced_object_id) = 'Global'
ORDER BY ParentTable, ParentColumn;
```

> توجه: اینجا فیلتر روی **`referenced`** است نه `parent` — چون سؤالِ این
> اسکیما «چه کسی به من اشاره می‌کند» است، نه برعکس.

---

## ۱. نام گروه — با تفکیکِ درست

```sql
WITH params AS (SELECT 560 AS goroh_link)   -- ۵۶۰ کالا ، ۳۰۴ نوع مشتری
SELECT g.ccGoroh, g.NameGoroh, g.CodeGoroh, g.CheckFaal, g.GhabeleEstefade
FROM [Global].[Goroh] AS g
CROSS JOIN params AS p
WHERE g.ccGorohLink = p.goroh_link
ORDER BY g.NameGoroh;
```

**همیشه با `ccGorohLink`.** و `Global.vGorohMahsol` را برای نام گروه کالا
استفاده نکن — فقط ۳۳ گروه از ۵۵ را دارد.

## ۲. شخص — با همه‌ی نقش‌هایش

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_afrad)
SELECT a.ccAfrad, a.FName, a.LName, a.Mobile, a.Email
FROM [Global].[Afrad] AS a
CROSS JOIN params AS p
WHERE (p.cc_afrad IS NULL OR a.ccAfrad = p.cc_afrad)
ORDER BY a.LName, a.FName;
```

> **کد ملی و شماره شناسنامه عمداً در `SELECT` نیستند.** اگر سؤال دقیقاً
> آنها را نخواسته، نیاورشان.

**پلِ بین اسکیمایی** — همان شخص در دو نقش:

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_afrad)
SELECT a.ccAfrad, a.FName, a.LName,
       pr.ccPersonel,
       pr.ShomarehPersonely
FROM [Global].[Afrad] AS a
CROSS JOIN params AS p
LEFT JOIN [HumanResource].[Personel] AS pr ON pr.ccAfrad = a.ccAfrad
WHERE (p.cc_afrad IS NULL OR a.ccAfrad = p.cc_afrad)
  AND pr.ccPersonel IS NOT NULL
ORDER BY a.LName;
```

## ۳. سلسله‌مراتب پخش

```sql
SELECT mp.ccMarkazPakhsh,
       mp.NameMarkazPakhsh,
       mt.NameMantaghehPakhsh,
       h.NameHouzeh,
       mp.Setad,
       mp.CodeDarajeh
FROM [Global].[MarkazPakhsh] AS mp
LEFT JOIN [Global].[MantaghehPakhsh] AS mt
       ON mt.ccMantaghehPakhsh = mp.ccMantaghehPakhsh
LEFT JOIN [Global].[Houzeh] AS h ON h.ccHouzeh = mp.ccHouzeh
ORDER BY mt.NameMantaghehPakhsh, mp.NameMarkazPakhsh;
```

## ۴. سلسله‌مراتب فروش

```sql
SELECT hf.ccHouzehForosh,
       hf.NameHouzehForosh,
       mf.NameMantaghehForosh,
       nv.NameNoeVahedForosh,
       a.FName + N' ' + a.LName AS modir
FROM [Global].[HouzehForosh] AS hf
LEFT JOIN [Global].[MantaghehForosh] AS mf
       ON mf.ccMantaghehForosh = hf.ccMantaghehForosh
LEFT JOIN [Global].[NoeVahedForosh] AS nv
       ON nv.ccNoeVahedForosh = mf.ccNoeVahedForosh
LEFT JOIN [Global].[Afrad] AS a ON a.ccAfrad = mf.ccAfradModir
ORDER BY mf.NameMantaghehForosh, hf.NameHouzehForosh;
```

**این سلسله‌مراتبِ فروش است، نه پخش.** با کوئری ۳ قاطی نکن.

## ۵. روز کاری یک ماه

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah)
SELECT COUNT(*) AS rooz_kari
FROM [Global].[Taghvim] AS t
CROSS JOIN params AS p
LEFT JOIN [Global].[TaghvimTatil] AS tt ON tt.Tarikh = t.Tarikh
WHERE t.Sal = p.sal AND t.Mah = p.mah
  AND tt.Tarikh IS NULL;
```

> **ساختارِ `TaghvimTatil` را اول با کوئری ۰.۳ `references` ببین** — اگر
> کلیدش `Tarikh` نیست، این `JOIN` را عوض کن. و نتیجه را با
> `TaghvimTatilManabeEnsani` مقایسه کن.

## ۹. کیفیت داده

### ۹.۱ ارجاعِ یتیم — از بیرون به Global

این مهم‌ترین آزمونِ این اسکیماست، چون همه از اینجا می‌خوانند:

```sql
SELECT COUNT(*) AS kol,
       SUM(CASE WHEN a.ccAfrad IS NULL THEN 1 ELSE 0 END) AS yatim
FROM [HumanResource].[Personel] AS pr
LEFT JOIN [Global].[Afrad] AS a ON a.ccAfrad = pr.ccAfrad
WHERE pr.ccAfrad IS NOT NULL;
```

همین را برای `Sales.AmarForosh_Arshive.ccAfradForoshandeh`،
`ccMarkazPakhsh` و `ccMarkaz` هم بزن. **نسبتِ یتیمِ بالا یعنی پلِ بین
اسکیمایی درست نیست** — و آن پل زیرِ پای چند اسکیل است.

### ۹.۲ تکرار در جدول مرجع

```sql
SELECT g.ccGorohLink, g.NameGoroh, COUNT(*) AS tekrar
FROM [Global].[Goroh] AS g
GROUP BY g.ccGorohLink, g.NameGoroh
HAVING COUNT(*) > 1
ORDER BY tekrar DESC;
```

نامِ تکراری در یک تاکسونومی یعنی `JOIN` روی نام سطر را ضرب می‌کند —
**همیشه روی `ccGoroh` بپیوند، نه روی `NameGoroh`**.

## اندازه‌ها

| اندازه | مقدار واقعی |
|---|---|
| مقادیر متمایز `ccGorohLink` | ؟ |
| تعداد `Markaz` / `MarkazPakhsh` | ؟ |
| بازه‌ی پوششِ `Taghvim` | ؟ |
| نسبت یتیمِ `Personel.ccAfrad` | ؟ |
