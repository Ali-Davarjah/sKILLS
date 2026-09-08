# کوئری‌ها

دیتابیس `pakhsh`.

> **`run_query` نتیجه را در ۵۰۰ سطر می‌برد** (`connectors.max_results`). با
> ۲۶ هزار مشتری، کوئری‌ای که سطرِ خام برمی‌گرداند بی‌صدا قیچی می‌شود — و چون
> مرتب‌سازی معمولاً با نوع مشتری شروع می‌شود، **نوع‌های کم‌جمعیت کلاً از جدول
> می‌افتند**. این دقیقاً همان باگی بود که «فقط ۲ عمده» می‌داد. پس: **در SQL جمع
> بزن، سطر خام نخواه.**

> **نمره در SQL حساب می‌شود، نه در کوئریِ خام + اسکریپت.** بلوک `astaneh` در هر
> کوئری همان چیزی است که در `rules.json` است. **اگر یکی را عوض کردی، آن یکی را
> هم بکن.** `scripts/rank.py` برای وقتی است که سطرها را از قبل در دست داری
> (زیرمجموعه‌ی کوچک، یا خروجی صادرشده).

> **چهار کد رتبه می‌گیرند: ۳۴۷، ۳۴۸، ۳۴۹ و ۳۵۰.** «مشتریان ویژه» در `rules.json`
> آستانه دارد ولی کد `ccNoeMoshtary`ش تأیید نشده، پس هنوز سطری در `astaneh`
> ندارد و آن مشتریان در «سایر» می‌افتند. تعاونی کارکنان (۶۰۷) و سایر آستانه
> ندارند و **رتبه نمی‌گیرند** — با کوئری ۵ فقط شمرده می‌شوند.

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود. در SSMS اگر `USE pakhsh` بالایش می‌گذاری، **نقطه‌ویرگول لازم دارد**
> وگرنه `Incorrect syntax near 'with'` می‌گیری.

## ۰. آخرین تاریخِ داده — قبل از هر چیز

```sql
SELECT MAX(Tarikh) AS "آخرین تاریخ" FROM Sales.AmarForosh_Arshive
```

## ۱. توزیع رتبه‌ها — کوئری پیش‌فرض

این را اول بزن؛ خطای بازه و اشباع آستانه هر دو همین‌جا دیده می‌شوند.

```sql
/* توزیع رتبه‌ها به تفکیک نوع مشتری — حداکثر ۲۴ سطر، زیر سقف ۵۰۰. */
WITH params AS (
    SELECT CAST('2026-08-31' AS date) AS rooz_payan, 3 AS tedad_mah,
           CAST(NULL AS int) AS sazman_forosh
),
bazeh AS (
    SELECT p.sazman_forosh,
           DATEADD(day, 1, DATEADD(month, -p.tedad_mah, CAST(p.rooz_payan AS datetime))) AS d_from,
           DATEADD(day, 1, CAST(p.rooz_payan AS datetime))                                AS d_to
    FROM params p
),
noe_ha AS (                     -- فقط نوع‌هایی که آستانه دارند
    SELECT * FROM (VALUES
        (347, N'خرد'), (348, N'عمده'), (349, N'تعاونی ویژه'), (350, N'زنجیره‌ای')
    ) AS t(noe, name_noe)
),
astaneh AS (                    -- باید با rules.json یکی بماند
    SELECT * FROM (VALUES
    --   معیار     نوع  ضریب  حد۲   حد۳   حد۴   حد۵
        ('aghlam', 347,  3,    350,  500,  650,   800),
        ('aghlam', 348,  3,   3500, 5000, 6500,  7500),
        ('aghlam', 349,  3,   3500, 5000, 6500,  8000),
        ('aghlam', 350,  3,   2000, 3000, 4000,  5000),
        ('vizit',  347,  4,     40,   50,   60,    70),
        ('vizit',  348,  4,     40,   50,   60,    70),
        ('vizit',  349,  4,     40,   50,   60,    70),
        ('vizit',  350,  4,     40,   50,   60,    70),
        ('sku',    347,  5,     16,   21,   26,    31),
        ('sku',    348,  5,     16,   21,   26,    31),
        ('sku',    349,  5,     16,   21,   26,    31),
        ('sku',    350,  5,     16,   21,   26,    31)
    ) AS t(meyar, noe, zarib, h2, h3, h4, h5)
),
baand AS (
    SELECT * FROM (VALUES
        (N'سوپر ممتاز', 60, 1), (N'ممتاز', 44, 2), (N'درجه ۱', 28, 3),
        (N'درجه ۲', 13, 4), (N'درجه ۳', NULL, 5), (N'ناقص', NULL, 6)
    ) AS t(rotbe, hadd_paeen, olaviat)
),
kharid AS (
    SELECT a.ccMoshtary, MAX(a.ccNoeMoshtary) AS noe,
           SUM(a.Tedad) AS tedad_aghlam, COUNT(DISTINCT a.ccKalaCode) AS tedad_sku
    FROM Sales.AmarForosh_Arshive a CROSS JOIN bazeh b
    WHERE a.Tarikh >= b.d_from AND a.Tarikh < b.d_to AND a.IsMarjoee = 0
      AND a.ccNoeMoshtary IN (347, 348, 349, 350)
      AND (b.sazman_forosh IS NULL OR a.ccSazmanForosh = b.sazman_forosh)
    GROUP BY a.ccMoshtary
),
vizit AS (
    SELECT v.ccMoshtary, SUM(v.MorajehShodeh) AS rafteh, SUM(v.VisitMosbat) AS mosbat
    FROM Sales.VisitForoshandeh_Arshiv v CROSS JOIN bazeh b
    WHERE v.TarikhVisit >= b.d_from AND v.TarikhVisit < b.d_to AND v.IsTatil = 0
      AND (b.sazman_forosh IS NULL OR v.ccSazmanForosh = b.sazman_forosh)
    GROUP BY v.ccMoshtary
),
paye AS (
    SELECT k.ccMoshtary, k.noe, k.tedad_aghlam, k.tedad_sku,
           CASE WHEN z.rafteh > 0 THEN 100.0 * z.mosbat / z.rafteh END AS vizit_pct
    FROM kharid k LEFT JOIN vizit z ON z.ccMoshtary = k.ccMoshtary
),
meyarha AS (
    SELECT ccMoshtary, noe, 'aghlam' AS meyar, CAST(tedad_aghlam AS decimal(18,4)) AS meghdar FROM paye
    UNION ALL SELECT ccMoshtary, noe, 'vizit', CAST(vizit_pct AS decimal(18,4)) FROM paye
    UNION ALL SELECT ccMoshtary, noe, 'sku',   CAST(tedad_sku AS decimal(18,4)) FROM paye
),
nomreh AS (
    SELECT m.ccMoshtary, MAX(m.noe) AS noe,
           CASE WHEN SUM(CASE WHEN r.rotbe_meyar IS NULL THEN 1 ELSE 0 END) > 0 THEN NULL
                ELSE SUM(r.rotbe_meyar * a.zarib) END AS emtiaz
    FROM meyarha m
    JOIN astaneh a ON a.meyar = m.meyar AND a.noe = m.noe
    CROSS APPLY (SELECT CASE WHEN m.meghdar IS NULL THEN NULL
                             WHEN m.meghdar >= a.h5 THEN 5 WHEN m.meghdar >= a.h4 THEN 4
                             WHEN m.meghdar >= a.h3 THEN 3 WHEN m.meghdar >= a.h2 THEN 2
                             ELSE 1 END AS rotbe_meyar) r
    GROUP BY m.ccMoshtary
),
barchasb AS (
    SELECT n.noe, ISNULL(g.rotbe, N'ناقص') AS rotbe, ISNULL(g.olaviat, 6) AS olaviat
    FROM nomreh n
    OUTER APPLY (SELECT TOP 1 d.rotbe, d.olaviat FROM baand d
                 WHERE d.olaviat < 6 AND n.emtiaz IS NOT NULL
                   AND (d.hadd_paeen IS NULL OR n.emtiaz >= d.hadd_paeen)
                 ORDER BY d.olaviat) g
)
SELECT t.name_noe                                     AS "نوع",
       b.rotbe                                        AS "رتبه",
       COUNT(*)                                       AS "تعداد مشتری",
       CAST(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY b.noe) AS decimal(5,1)) AS "سهم ٪"
FROM barchasb b JOIN noe_ha t ON t.noe = b.noe
GROUP BY b.noe, t.name_noe, b.rotbe, b.olaviat
ORDER BY b.noe, b.olaviat
```

## ۲. برترها — یک سطر به ازای هر نمره، نه هر نفر

**«۱۰ مشتری برتر» تعریف ندارد** چون هم‌نمره‌ها زیادند: در سه ماه منتهی به
۲۰۲۶-۰۸-۳۰، **۳۴۸ مشتری خرد** همه نمره‌ی ۶۰ داشتند. اگر به ازای هر نفر یک سطر
بدهی، «۱۰ جایگاه برتر» می‌شود ۱٬۲۹۷ سطر و باز قیچی می‌شود.

این کوئری هر نمره را یک سطر می‌دهد و می‌گوید چند نفر روی آن نشسته‌اند:

```sql
/* N مشتری برتر هر نوع — سطرها کراندار، زیر سقف ۵۰۰. */
WITH params AS (
    SELECT CAST('2026-08-31' AS date) AS rooz_payan, 3 AS tedad_mah, 10 AS tedad_bartar,
           CAST(NULL AS int) AS sazman_forosh
),
bazeh AS (
    SELECT p.sazman_forosh, p.tedad_bartar,
           DATEADD(day, 1, DATEADD(month, -p.tedad_mah, CAST(p.rooz_payan AS datetime))) AS d_from,
           DATEADD(day, 1, CAST(p.rooz_payan AS datetime))                                AS d_to
    FROM params p
),
noe_ha AS (
    SELECT * FROM (VALUES
        (347, N'خرد'), (348, N'عمده'), (349, N'تعاونی ویژه'), (350, N'زنجیره‌ای')
    ) AS t(noe, name_noe)
),
astaneh AS (
    SELECT * FROM (VALUES
        ('aghlam', 347, 3,  350,  500,  650,  800), ('aghlam', 348, 3, 3500, 5000, 6500, 7500),
        ('aghlam', 349, 3, 3500, 5000, 6500, 8000), ('aghlam', 350, 3, 2000, 3000, 4000, 5000),
        ('vizit',  347, 4,   40,   50,   60,   70), ('vizit',  348, 4,   40,   50,   60,   70),
        ('vizit',  349, 4,   40,   50,   60,   70), ('vizit',  350, 4,   40,   50,   60,   70),
        ('sku',    347, 5,   16,   21,   26,   31), ('sku',    348, 5,   16,   21,   26,   31),
        ('sku',    349, 5,   16,   21,   26,   31), ('sku',    350, 5,   16,   21,   26,   31)
    ) AS t(meyar, noe, zarib, h2, h3, h4, h5)
),
baand AS (
    SELECT * FROM (VALUES
        (N'سوپر ممتاز', 60, 1), (N'ممتاز', 44, 2), (N'درجه ۱', 28, 3),
        (N'درجه ۲', 13, 4), (N'درجه ۳', NULL, 5), (N'ناقص', NULL, 6)
    ) AS t(rotbe, hadd_paeen, olaviat)
),
kharid AS (
    SELECT a.ccMoshtary, MAX(a.ccNoeMoshtary) AS noe,
           SUM(a.Tedad) AS tedad_aghlam, COUNT(DISTINCT a.ccKalaCode) AS tedad_sku
    FROM Sales.AmarForosh_Arshive a CROSS JOIN bazeh b
    WHERE a.Tarikh >= b.d_from AND a.Tarikh < b.d_to AND a.IsMarjoee = 0
      AND a.ccNoeMoshtary IN (347, 348, 349, 350)
      AND (b.sazman_forosh IS NULL OR a.ccSazmanForosh = b.sazman_forosh)
    GROUP BY a.ccMoshtary
),
vizit AS (
    SELECT v.ccMoshtary, SUM(v.MorajehShodeh) AS rafteh, SUM(v.VisitMosbat) AS mosbat
    FROM Sales.VisitForoshandeh_Arshiv v CROSS JOIN bazeh b
    WHERE v.TarikhVisit >= b.d_from AND v.TarikhVisit < b.d_to AND v.IsTatil = 0
      AND (b.sazman_forosh IS NULL OR v.ccSazmanForosh = b.sazman_forosh)
    GROUP BY v.ccMoshtary
),
paye AS (
    SELECT k.ccMoshtary, k.noe, k.tedad_aghlam, k.tedad_sku,
           CASE WHEN z.rafteh > 0 THEN 100.0 * z.mosbat / z.rafteh END AS vizit_pct
    FROM kharid k LEFT JOIN vizit z ON z.ccMoshtary = k.ccMoshtary
),
meyarha AS (
    SELECT ccMoshtary, noe, 'aghlam' AS meyar, CAST(tedad_aghlam AS decimal(18,4)) AS meghdar FROM paye
    UNION ALL SELECT ccMoshtary, noe, 'vizit', CAST(vizit_pct AS decimal(18,4)) FROM paye
    UNION ALL SELECT ccMoshtary, noe, 'sku',   CAST(tedad_sku AS decimal(18,4)) FROM paye
),
nomreh AS (
    SELECT m.ccMoshtary, MAX(m.noe) AS noe,
           CASE WHEN SUM(CASE WHEN r.rotbe_meyar IS NULL THEN 1 ELSE 0 END) > 0 THEN NULL
                ELSE SUM(r.rotbe_meyar * a.zarib) END AS emtiaz
    FROM meyarha m
    JOIN astaneh a ON a.meyar = m.meyar AND a.noe = m.noe
    CROSS APPLY (SELECT CASE WHEN m.meghdar IS NULL THEN NULL
                             WHEN m.meghdar >= a.h5 THEN 5 WHEN m.meghdar >= a.h4 THEN 4
                             WHEN m.meghdar >= a.h3 THEN 3 WHEN m.meghdar >= a.h2 THEN 2
                             ELSE 1 END AS rotbe_meyar) r
    GROUP BY m.ccMoshtary
),
bartar AS (
    SELECT n.noe, n.emtiaz,
           COUNT(*)                 AS tedad_hamnomreh,
           MIN(p.tedad_aghlam)      AS aghlam_min,
           MAX(p.tedad_aghlam)      AS aghlam_max,
           DENSE_RANK() OVER (PARTITION BY n.noe ORDER BY n.emtiaz DESC) AS jaygah
    FROM nomreh n JOIN paye p ON p.ccMoshtary = n.ccMoshtary
    WHERE n.emtiaz IS NOT NULL
    GROUP BY n.noe, n.emtiaz
)
SELECT b.jaygah                                         AS "جایگاه",
       t.name_noe                                       AS "نوع",
       b.emtiaz                                         AS "امتیاز",
       g.rotbe                                          AS "رتبه",
       b.tedad_hamnomreh                                AS "تعداد مشتری هم‌نمره",
       CAST(b.aghlam_min AS bigint)                     AS "کمترین اقلام",
       CAST(b.aghlam_max AS bigint)                     AS "بیشترین اقلام"
FROM bartar b
JOIN noe_ha t ON t.noe = b.noe
CROSS JOIN bazeh z
OUTER APPLY (SELECT TOP 1 d.rotbe FROM baand d
             WHERE d.olaviat < 6 AND (d.hadd_paeen IS NULL OR b.emtiaz >= d.hadd_paeen)
             ORDER BY d.olaviat) g
WHERE b.jaygah <= z.tedad_bartar
ORDER BY b.noe, b.jaygah
```

اگر اسم‌های یک گروه هم‌نمره را خواستند، کوئری ۳ را با فیلترِ همان نمره بزن — و
در گزارش بگو که فهرست، **نمونه‌ای از یک گروه هم‌نمره** است، نه ترتیب.

## ۳. فهرست مشتریان با جزئیات — حتماً کراندار

سی‌ودو ستون به ازای هر مشتری. **بدون فیلتر ۲۶ هزار سطر می‌شود و قیچی می‌خورد.**
با `noe`، `sazman_forosh` یا نمره محدودش کن تا زیر ۵۰۰ بماند، یا خروجی را جای
دیگری بگیر.

```sql
/* مشتریانی که در سه ماه گذشته خرید داشته‌اند — با جزئیات و امتیاز.
   noe = NULL هر چهار نوعِ دارای آستانه، یا یکی از 347/348/349/350. */
WITH params AS (
    SELECT CAST('2026-08-31' AS date) AS rooz_payan,   -- روز پایان بازه
           3                          AS tedad_mah,    -- طول بازه به ماه
           CAST(NULL AS int)          AS noe           -- NULL = هر چهار نوع
),
bazeh AS (
    SELECT p.noe,
           DATEADD(day, 1, DATEADD(month, -p.tedad_mah, CAST(p.rooz_payan AS datetime))) AS d_from,
           DATEADD(day, 1, CAST(p.rooz_payan AS datetime))                                AS d_to
    FROM params p
),
noe_ha AS (
    SELECT * FROM (VALUES
        (347, N'خرد'), (348, N'عمده'), (349, N'تعاونی ویژه'), (350, N'زنجیره‌ای')
    ) AS t(noe, name_noe)
),
astaneh AS (                    -- باید با rules.json یکی بماند
    SELECT * FROM (VALUES
    --   معیار     نوع  ضریب  حد۲   حد۳   حد۴   حد۵
        ('aghlam', 347,  3,    350,  500,  650,   800),
        ('aghlam', 348,  3,   3500, 5000, 6500,  7500),
        ('aghlam', 349,  3,   3500, 5000, 6500,  8000),
        ('aghlam', 350,  3,   2000, 3000, 4000,  5000),
        ('vizit',  347,  4,     40,   50,   60,    70),
        ('vizit',  348,  4,     40,   50,   60,    70),
        ('vizit',  349,  4,     40,   50,   60,    70),
        ('vizit',  350,  4,     40,   50,   60,    70),
        ('sku',    347,  5,     16,   21,   26,    31),
        ('sku',    348,  5,     16,   21,   26,    31),
        ('sku',    349,  5,     16,   21,   26,    31),
        ('sku',    350,  5,     16,   21,   26,    31)
    ) AS t(meyar, noe, zarib, h2, h3, h4, h5)
),
baand AS (
    SELECT * FROM (VALUES
        (N'سوپر ممتاز', 60, 1), (N'ممتاز', 44, 2), (N'درجه ۱', 28, 3),
        (N'درجه ۲', 13, 4), (N'درجه ۳', NULL, 5)
    ) AS t(rotbe, hadd_paeen, olaviat)
),
kharid AS (
    SELECT a.ccMoshtary,
           MAX(a.ccNoeMoshtary)               AS noe,
           SUM(a.Tedad)                       AS tedad_aghlam,
           COUNT(DISTINCT a.ccKalaCode)       AS tedad_sku,
           COUNT(DISTINCT a.ccDarkhastFaktor) AS tedad_faktor,
           COUNT(DISTINCT a.Tarikh)           AS rooz_kharid,
           MAX(a.Tarikh)                      AS akharin_kharid,
           SUM(a.Rial)                        AS mablagh
    FROM Sales.AmarForosh_Arshive a CROSS JOIN bazeh b
    WHERE a.Tarikh >= b.d_from AND a.Tarikh < b.d_to
      AND a.IsMarjoee = 0
      AND a.ccNoeMoshtary IN (347, 348, 349, 350)
      AND (b.noe IS NULL OR a.ccNoeMoshtary = b.noe)
    GROUP BY a.ccMoshtary
),
vizit AS (
    SELECT v.ccMoshtary,
           SUM(v.MorajehShodeh) AS vizit_rafteh,
           SUM(v.VisitMosbat)   AS vizit_mosbat
    FROM Sales.VisitForoshandeh_Arshiv v CROSS JOIN bazeh b
    WHERE v.TarikhVisit >= b.d_from AND v.TarikhVisit < b.d_to
      AND v.IsTatil = 0
    GROUP BY v.ccMoshtary
),
paye AS (
    SELECT k.*, z.vizit_rafteh, z.vizit_mosbat,
           CASE WHEN z.vizit_rafteh > 0
                THEN 100.0 * z.vizit_mosbat / z.vizit_rafteh END AS vizit_pct
    FROM kharid k LEFT JOIN vizit z ON z.ccMoshtary = k.ccMoshtary
),
meyarha AS (
    SELECT ccMoshtary, noe, 'aghlam' AS meyar, CAST(tedad_aghlam AS decimal(18,4)) AS meghdar FROM paye
    UNION ALL SELECT ccMoshtary, noe, 'vizit', CAST(vizit_pct AS decimal(18,4)) FROM paye
    UNION ALL SELECT ccMoshtary, noe, 'sku',   CAST(tedad_sku AS decimal(18,4)) FROM paye
),
nomreh AS (
    SELECT m.ccMoshtary,
           MAX(CASE WHEN m.meyar='aghlam' THEN r.rotbe_meyar END) AS r_aghlam,
           MAX(CASE WHEN m.meyar='vizit'  THEN r.rotbe_meyar END) AS r_vizit,
           MAX(CASE WHEN m.meyar='sku'    THEN r.rotbe_meyar END) AS r_sku,
           CASE WHEN SUM(CASE WHEN r.rotbe_meyar IS NULL THEN 1 ELSE 0 END) > 0 THEN NULL
                ELSE SUM(r.rotbe_meyar * a.zarib) END AS emtiaz
    FROM meyarha m
    JOIN astaneh a ON a.meyar = m.meyar AND a.noe = m.noe   -- آستانه‌ی همان نوع مشتری
    CROSS APPLY (SELECT CASE WHEN m.meghdar IS NULL THEN NULL
                             WHEN m.meghdar >= a.h5 THEN 5 WHEN m.meghdar >= a.h4 THEN 4
                             WHEN m.meghdar >= a.h3 THEN 3 WHEN m.meghdar >= a.h2 THEN 2
                             ELSE 1 END AS rotbe_meyar) r
    GROUP BY m.ccMoshtary
),
rotbe_rasmi AS (
    SELECT t.ccMoshtary, t.CodeMoshtary, t.NameMarkaz, t.NameMarkazSazmanForosh,
           t.NameSenfMoshtary, t.NameVazeiat, t.CodeForoshandeh, t.ToorVisit,
           t.NameNoeVosolAzMoshtary, t.NameDarajeh, t.Emtiaz
    FROM Sales.Tmp_RotbeBandiMoshtary t
    WHERE t.ccBrand = 0
      AND t.Tarikh = (SELECT MAX(Tarikh) FROM Sales.Tmp_RotbeBandiMoshtary)
)
SELECT
    p.ccMoshtary                              AS "کد سیستمی",
    r.CodeMoshtary                            AS "کد مشتری",
    m.NameMoshtary                            AS "نام",
    m.NameTablo                               AS "نام تابلو",
    p.noe                                     AS "کد نوع",
    nt.name_noe                               AS "نوع مشتری",
    r.NameMarkaz                              AS "شعبه",
    r.NameMarkazSazmanForosh                  AS "لاین فروش",
    r.NameSenfMoshtary                        AS "صنف",
    r.NameVazeiat                             AS "وضعیت",
    r.CodeForoshandeh                         AS "کد فروشنده",
    r.ToorVisit                               AS "تور ویزیت",
    r.NameNoeVosolAzMoshtary                  AS "نحوه وصول",
    m.Telephone                               AS "تلفن",
    m.MasahatMaghazeh                         AS "مساحت مغازه",
    CAST(m.TarikhMoarefiMoshtary AS date)     AS "تاریخ معرفی",
    CAST(p.akharin_kharid AS date)            AS "آخرین خرید",
    p.tedad_faktor                            AS "تعداد فاکتور",
    p.rooz_kharid                             AS "روز دارای خرید",
    CAST(p.tedad_aghlam AS bigint)            AS "تعداد اقلام",
    p.tedad_sku                               AS "تعداد SKU",
    CAST(p.mablagh AS bigint)                 AS "مبلغ خرید",
    p.vizit_rafteh                            AS "ویزیت رفته",
    p.vizit_mosbat                            AS "ویزیت مثبت",
    CAST(p.vizit_pct AS decimal(5,1))         AS "درصد ویزیت مثبت",
    n.r_aghlam                                AS "رتبه اقلام",
    n.r_vizit                                 AS "رتبه ویزیت",
    n.r_sku                                   AS "رتبه SKU",
    n.emtiaz                                  AS "امتیاز اسکیل",
    ISNULL(g.rotbe, N'ناقص')                  AS "رتبه اسکیل",
    r.Emtiaz                                  AS "امتیاز پگاه",
    r.NameDarajeh                             AS "درجه پگاه"
FROM paye p
JOIN nomreh n              ON n.ccMoshtary = p.ccMoshtary
JOIN noe_ha nt             ON nt.noe = p.noe
LEFT JOIN Sales.Moshtary m ON m.ccMoshtary = p.ccMoshtary
LEFT JOIN rotbe_rasmi r    ON r.ccMoshtary = p.ccMoshtary
OUTER APPLY (
    SELECT TOP 1 d.rotbe FROM baand d
    WHERE n.emtiaz IS NOT NULL AND (d.hadd_paeen IS NULL OR n.emtiaz >= d.hadd_paeen)
    ORDER BY d.olaviat
) g
ORDER BY p.noe, n.emtiaz DESC, p.tedad_aghlam DESC, p.ccMoshtary
```

## ۴. کالیبره کردن آستانه — وقتی هشدار اشباع آمد

**آستانه را از توزیعِ همه‌ی مشتریانِ آن نوع دربیاور، نه از چند نفر بالای جدول.**
صدک‌های ۲۰/۴۰/۶۰/۸۰ هر رتبه را حدوداً یک‌پنجم می‌کنند — نقطه‌ی شروعِ گفت‌وگو با
مدیر فروش، نه جواب نهایی.

```sql
WITH params AS (
    SELECT CAST('2026-08-30' AS date) AS rooz_payan,
           3                          AS tedad_mah,
           CAST(NULL AS int)          AS sazman_forosh
),
bazeh AS (
    SELECT DATEADD(day, 1, DATEADD(month, -p.tedad_mah, CAST(p.rooz_payan AS datetime))) AS d_from,
           DATEADD(day, 1, CAST(p.rooz_payan AS datetime))                                AS d_to,
           p.sazman_forosh
    FROM params p
),
noe_ha AS (                     -- تعاونی کارکنان هم هست تا وقتی آستانه‌اش آمد عددی داشته باشی
    SELECT * FROM (VALUES
        (347, N'خرد'), (348, N'عمده'), (349, N'تعاونی ویژه'), (350, N'زنجیره‌ای'),
        (607, N'تعاونی کارکنان')
    ) AS t(noe, name_noe)
),
kharid AS (
    SELECT a.ccMoshtary,
           MAX(a.ccNoeMoshtary)         AS noe_moshtary,
           SUM(a.Tedad)                 AS tedad_aghlam,
           COUNT(DISTINCT a.ccKalaCode) AS tedad_sku
    FROM Sales.AmarForosh_Arshive a CROSS JOIN bazeh b
    WHERE a.Tarikh >= b.d_from AND a.Tarikh < b.d_to
      AND a.IsMarjoee = 0
      AND (b.sazman_forosh IS NULL OR a.ccSazmanForosh = b.sazman_forosh)
    GROUP BY a.ccMoshtary
)
SELECT DISTINCT
    t.name_noe                                                                      AS "نوع",
    COUNT(*)            OVER (PARTITION BY k.noe_moshtary)                          AS "تعداد مشتری",
    MIN(k.tedad_aghlam) OVER (PARTITION BY k.noe_moshtary)                          AS "اقلام کمینه",
    PERCENTILE_CONT(0.20) WITHIN GROUP (ORDER BY k.tedad_aghlam) OVER (PARTITION BY k.noe_moshtary) AS "اقلام ۲۰٪",
    PERCENTILE_CONT(0.40) WITHIN GROUP (ORDER BY k.tedad_aghlam) OVER (PARTITION BY k.noe_moshtary) AS "اقلام ۴۰٪",
    PERCENTILE_CONT(0.60) WITHIN GROUP (ORDER BY k.tedad_aghlam) OVER (PARTITION BY k.noe_moshtary) AS "اقلام ۶۰٪",
    PERCENTILE_CONT(0.80) WITHIN GROUP (ORDER BY k.tedad_aghlam) OVER (PARTITION BY k.noe_moshtary) AS "اقلام ۸۰٪",
    MAX(k.tedad_aghlam) OVER (PARTITION BY k.noe_moshtary)                          AS "اقلام بیشینه",
    PERCENTILE_CONT(0.20) WITHIN GROUP (ORDER BY k.tedad_sku) OVER (PARTITION BY k.noe_moshtary) AS "SKU ۲۰٪",
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY k.tedad_sku) OVER (PARTITION BY k.noe_moshtary) AS "SKU ۵۰٪",
    PERCENTILE_CONT(0.80) WITHIN GROUP (ORDER BY k.tedad_sku) OVER (PARTITION BY k.noe_moshtary) AS "SKU ۸۰٪"
FROM kharid k JOIN noe_ha t ON t.noe = k.noe_moshtary
```

بعد `python scripts/rules.py set item_count.khord <۲۰٪> <۴۰٪> <۶۰٪> <۸۰٪>` —
و **همان عددها را در بلوک `astaneh` کوئری‌ها هم بگذار**.

- **عدد را گرد کن.** آستانه‌ی ۱۸٬۴۳۷ در جلسه قابل دفاع نیست؛ ۱۸٬۰۰۰ همان کار را می‌کند.
- **این کوئری فقط مشتریِ خریدکرده را می‌بیند**، پس صدک‌ها به بالا منحرف‌اند.
- **صدک، قاعده‌ی کسب‌وکار نیست.** خروجی را به مدیر فروش نشان بده.

## ۵. مشتریانِ خارج از رتبه‌بندی — برای بند ۵ گزارش

تعاونی کارکنان و «سایر» آستانه ندارند و در چهار کوئری بالا نمی‌آیند. **این کوئری
را هر بار بزن**، وگرنه در گزارش نمی‌توانی بگویی چند مشتری کنار گذاشته شدند.
خروجی‌اش کدهای واقعیِ موجود در بازه را هم می‌دهد — همان‌جا معلوم می‌شود کد
«مشتریان ویژه» کدام است.

```sql
/* یک سطر به ازای هر کد نوع مشتری — همه‌ی کدها، نه فقط رتبه‌گیرها. */
WITH params AS (
    SELECT CAST('2026-08-31' AS date) AS rooz_payan, 3 AS tedad_mah
),
bazeh AS (
    SELECT DATEADD(day, 1, DATEADD(month, -p.tedad_mah, CAST(p.rooz_payan AS datetime))) AS d_from,
           DATEADD(day, 1, CAST(p.rooz_payan AS datetime))                                AS d_to
    FROM params p
)
SELECT a.ccNoeMoshtary                                 AS "کد نوع",
       COUNT(DISTINCT a.ccMoshtary)                    AS "تعداد مشتری",
       CAST(SUM(a.Tedad) AS bigint)                    AS "تعداد اقلام",
       CASE WHEN a.ccNoeMoshtary IN (347, 348, 349, 350)
            THEN N'رتبه می‌گیرد' ELSE N'بدون رتبه' END AS "وضعیت"
FROM Sales.AmarForosh_Arshive a CROSS JOIN bazeh b
WHERE a.Tarikh >= b.d_from AND a.Tarikh < b.d_to AND a.IsMarjoee = 0
GROUP BY a.ccNoeMoshtary
ORDER BY COUNT(DISTINCT a.ccMoshtary) DESC
```

## اعتبارسنجی — بار اول روی هر بازه‌ی تازه

**۱. جمع اقلام.** با جمع ستون «تعداد اقلام» مقایسه کن:

```sql
SELECT SUM(Tedad) AS "جمع اقلام", COUNT(DISTINCT ccMoshtary) AS "تعداد مشتری"
FROM Sales.AmarForosh_Arshive
WHERE Tarikh >= '2026-05-31' AND Tarikh < '2026-08-31' AND IsMarjoee = 0
```

خروجی باید **کمتر یا مساوی** این باشد؛ اختلاف = مشتریانِ خارج از
۳۴۷/۳۴۸/۳۴۹/۳۵۰، که کوئری ۵ به تفکیک کد می‌شماردشان.

**۲. مشتری با بیش از یک کد نوع** (که `MAX` پنهانش می‌کند):

```sql
SELECT COUNT(*) AS "مشتری چندنوعی" FROM (
    SELECT ccMoshtary FROM Sales.AmarForosh_Arshive
    WHERE Tarikh >= '2026-05-31' AND Tarikh < '2026-08-31'
    GROUP BY ccMoshtary HAVING COUNT(DISTINCT ccNoeMoshtary) > 1
) x
```

**۳. توزیع را نگاه کن.** اگر یک رتبه بیش از ۸۰٪ گرفت، آستانه با واقعیتِ بازه
نمی‌خواند — از هر دو طرف:

- **همه ته جدول** — آستانه برای این نوع خیلی بالاست، یا بازه کوتاه‌تر از فرضِ
  آستانه است، یا «تعداد اقلام» را سطر گرفته‌ای نه واحد. روی سه ماه منتهی به
  ۲۰۲۶-۰۸-۳۰ علتش آستانه بود: میانه‌ی خرد ۱۴۹ قلم و ۱۴ SKU، و ۸۴٪ رتبه ۱ گرفتند.
- **همه سرِ جدول** — اول جمعیت را نگاه کن، نه آستانه را. یک لیستِ از پیش
  مرتب‌شده (مثل «۱۰ برتر») همیشه همه رتبه ۵ می‌گیرد.

**۴. سهم مشتریانِ بدون رکورد ویزیت.** اگر بالاست، رتبه‌ی ویزیت برای بخش بزرگی
از جدول محاسبه نشده — این را باید بالای گزارش گفت.

**۵. زنجیره‌ای و تعاونی ویژه روی هیچ بازه‌ای اجرا نشده‌اند.** آستانه‌شان از مدیر
فروش آمده، ولی جمعیتشان کوچک است و معیارِ اشباع‌شده در گروه ۴۰ نفره راحت‌تر از
خرد پنهان می‌ماند. بار اول توزیعشان را جدا نگاه کن.

## ورودی `rank.py` — وقتی سطرها را در دست داری

| ستون | کلید JSON |
|---|---|
| `کد مشتری` | `code` |
| نام | `name` |
| `کد نوع` | `type` — کد عددی، یا کلید انگلیسی، یا برچسب فارسی |
| `تعداد اقلام` | `item_count` |
| `ویزیت رفته` | `visits_total` |
| `ویزیت مثبت` | `visits_positive` |
| `تعداد SKU` | `sku_count` |

کلیدهای نوع مشتری را با `rules.py show` ببین. **کدی که در هیچ نوعی نباشد به
«سایر» می‌افتد و رتبه نمی‌گیرد** — خطا نمی‌دهد، پس اگر جدولی خالی درآمد اول کد
نوع را چک کن.

مقدارِ نداشته را `null` بفرست، نه صفر. با `kind='python'` اجرا کن —
`kind='bash'` روی میزبان ویندوزی خروجی فارسی را خراب می‌کند:

```python
import subprocess, sys
r = subprocess.run(
    [sys.executable, "pegah-skills/رتبه-بندی-مشتریان-پگاه/scripts/rank.py", "input.json"],
    capture_output=True, text=True, encoding="utf-8")
print(r.stdout or r.stderr)
```
