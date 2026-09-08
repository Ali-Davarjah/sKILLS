# یک سؤال واقعی، از اول تا آخر

**سؤال کاربر:** «مرداد ۱۴۰۵ چقدر از مشتری‌ها وصول شد؟»

سؤالِ ساده‌ای که **سه راهِ متفاوت برای دوباره‌شماریِ پول** در آن هست. هر سه
عددِ بزرگ‌ترِ به‌ظاهر معقول می‌دهند.

---

## گام ۰ — جهانِ PPC، قبل از هر چیز

```sql
-- کوئری ۰.۲ references/queries.md
SELECT COUNT(*) AS moshtarak
FROM [Treasury].[DariaftPardakht] AS a
JOIN [Treasury].[DariaftPardakhtPPC] AS b
  ON b.ccDariaftPardakht = a.ccDariaftPardakht;
```

**این اولین کوئری است، نه آخرین.** سه نتیجه، سه کوئریِ نهاییِ متفاوت:

| نتیجه | یعنی | کوئری نهایی |
|---|---|---|
| هم‌پوشانیِ بالا | PPC سینکِ همان است | فقط جدولِ اصلی |
| هم‌پوشانیِ صفر | دو مجموعه‌ی جدا | `UNION ALL` هر دو |
| هم‌پوشانیِ جزئی | نامعلوم | **بپرس — حدس نزن** |

اگر این گام را رد کنی و هر دو را جمع بزنی، در حالت اول **وصول را دو برابر
گزارش کرده‌ای**.

## گام ۱ — «وصول» یعنی کدام جهت

```sql
SELECT d.CodeNoeDariaftPardakht, n.NameNoeDariaftPardakht,
       COUNT(*) AS tedad, SUM(d.Mablagh) AS jam
FROM [Treasury].[DariaftPardakht] AS d
LEFT JOIN [Treasury].[NoeDariaftPardakht] AS n
       ON n.CodeNoeDariaftPardakht = d.CodeNoeDariaftPardakht
GROUP BY d.CodeNoeDariaftPardakht, n.NameNoeDariaftPardakht
ORDER BY tedad DESC;
```

**کدام کد «دریافت» است را از داده و دیکشنری تأیید بگیر، نه از حدس.** جمعِ
دریافت و پرداخت با هم عددی می‌دهد که هیچ معنایی ندارد.

## گام ۲ — مبلغِ سربرگ یا مبلغِ آخرین وضعیت

`DariaftPardakhtVazeiat` خودش ستون `Mablagh` دارد. کوئری ۰.۶ می‌گوید این دو
چقدر فرق دارند.

- **`moghayer = 0`** → سربرگ کافی است، ادامه بده.
- **`moghayer > 0`** → **بپرس**: «وصولِ واقعی مبلغِ سند است یا مبلغِ آخرین
  وضعیت؟» این تنها سؤالِ متوقف‌کننده‌ی این مسیر است.

## گام ۳ — وضعیت

```sql
SELECT CodeVazeiat, COUNT(*) AS tedad, SUM(Mablagh) AS jam
FROM [Treasury].[DariaftPardakht]
GROUP BY CodeVazeiat ORDER BY tedad DESC;
```

سندِ باطل یا در جریان نباید در «وصول شد» بیاید. کدِ معتبر را پیدا کن و
فیلتر کن.

## گام ۴ — کوئری

فرض: PPC سینک است (پس فقط جدولِ اصلی)، مبلغِ سربرگ مرجع است، کد وصول ۱ و
کد وضعیتِ معتبر ۳.

```sql
WITH params AS (
    SELECT CAST('2026-07-23' AS date) AS az_tarikh,   -- ۱۴۰۵/۰۵/۰۱
           CAST('2026-08-22' AS date) AS ta_tarikh,   -- ۱۴۰۵/۰۵/۳۱
           1                          AS code_daryaft,
           3                          AS code_vazeiat_motabar
)
SELECT d.ccMarkazPakhsh,
       d.CodeNoeSanad,
       COUNT(*)                      AS tedad_sanad,
       COUNT(DISTINCT d.ccMoshtary)  AS tedad_moshtary,
       SUM(d.Mablagh)                AS jam_vosol
FROM [Treasury].[DariaftPardakht] AS d
CROSS JOIN params AS p
WHERE d.ZamaneSabt >= p.az_tarikh
  AND d.ZamaneSabt <  DATEADD(day, 1, p.ta_tarikh)
  AND d.CodeNoeDariaftPardakht = p.code_daryaft
  AND d.CodeVazeiat            = p.code_vazeiat_motabar
GROUP BY d.ccMarkazPakhsh, d.CodeNoeSanad
ORDER BY jam_vosol DESC;
```

چهار چیز عمدی:

- **`< DATEADD(day, 1, ta_tarikh)`** — `ZamaneSabt` از نوع `datetime` است و
  ساعت دارد؛ `<= ta_tarikh` سندهای بعدازظهرِ روز آخر را می‌اندازد.
- **بدونِ `JOIN` به هیچ جدول سطر** — چون مبلغ روی سربرگ است و هر join
  ضربش می‌کند.
- **تفکیک `CodeNoeSanad`** — نقد و چک و فیش یک چیز نیستند؛ چکِ وصول‌نشده
  پولِ نقد نیست.
- **`tedad_moshtary` کنارِ مبلغ** — تا معلوم شود عدد از چند مشتری آمده.

## گام ۵ — گزارش

```
وصول از مشتریان — مرداد ۱۴۰۵

بازه       : ۱۴۰۵/۰۵/۰۱ تا ۱۴۰۵/۰۵/۳۱ (۲۰۲۶-۰۷-۲۳ تا ۲۰۲۶-۰۸-۲۲)
جهت        : فقط دریافت (CodeNoeDariaftPardakht = 1)
وضعیت      : فقط کد ۳ (معتبر) — اسناد باطل و در جریان حذف شدند
منبع       : Treasury.DariaftPardakht — بدون DariaftPardakhtPPC،
             چون هم‌پوشانی کلید N٪ بود و PPC سینکِ همین جدول است
مبلغ       : مبلغِ سربرگ (با آخرین وضعیت مغایرتی نداشت)

┌───┬──────────────┬────────────┬───────────┬──────────────┐
│ ۱ │ مرکز پخش     │ نوع سند    │ مشتری     │ جمع وصول     │
└───┴──────────────┴────────────┴───────────┴──────────────┘

نوعِ سند تفکیک شده چون چکِ وصول‌نشده با نقد یکی نیست.

تأییدنشده: اتصال ccMoshtary به Sales.Moshtary از هم‌نامی است و کلید خارجی
ندارد؛ N سند از M سند مشتری گرفتند.
```

---

## چه پرسیده شد و چه پرسیده نشد

| پرسیده شد | چون |
|---|---|
| مبلغِ سربرگ یا آخرین وضعیت؟ | **فقط اگر** کوئری ۰.۶ مغایرت نشان داد |
| PPC جدا است یا سینک؟ | اگر هم‌پوشانی جزئی بود — نه صفر و نه کامل |

| پرسیده نشد | چون |
|---|---|
| کدام کد «دریافت» است | از دیکشنری و توزیع معلوم می‌شود |
| کدام وضعیت معتبر است | از توزیع معلوم می‌شود |
| چک وصول‌نشده حساب شود؟ | تفکیک شد تا خواننده خودش تصمیم بگیرد |

**سؤالی که با یک کوئری جواب می‌گیرد، سؤال نیست.** ولی سؤالی که دو جوابِ
هم‌ارز دارد — مثل مبلغِ سربرگ در برابر وضعیت — سؤال است.

---

## اگر جواب خالی درآمد

۱. `MAX(ZamaneSabt)` واقعی.
۲. **جدولِ دیگر را امتحان کن** — اگر اصلی خالی بود، PPC را ببین. در این
   اسکیما اولین حدسِ درست همین است.
۳. فیلترها را یکی‌یکی بردار: بدون وضعیت چند؟ بدون جهت چند؟

معمول‌ترین علتِ خالی بودن: **فیلترِ وضعیت روی کدی که در این دوره استفاده
نمی‌شود**.
