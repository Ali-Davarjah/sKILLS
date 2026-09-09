# یک سؤال واقعی، از اول تا آخر

**سؤال کاربر:** «حقوق مرداد ۱۴۰۵ واحد فروش چقدر شد؟»

این سؤال کوتاه است ولی شش تصمیم در آن پنهان است. مسیر زیر نشان می‌دهد کدام
تصمیم کجا گرفته می‌شود و چه چیزی را باید از کاربر پرسید و چه چیزی را خودت
تعیین می‌کنی.

---

## گام ۰ — تأیید، قبل از هر چیز

سه کوئری، هر سه ارزان:

```sql
-- الف) جدول‌ها هستند و چقدر داده دارند؟  (کوئری ۰.۱)
-- ب) آخرین دوره‌ی موجود کدام است؟        (کوئری ۰.۶)
-- ج) کلید خارجی واقعی هست؟               (کوئری ۰.۴)
```

**چرا اول اینها:** اگر مرداد ۱۴۰۵ در `PardakhtHoghogh` ردیف ندارد، هر کاری
بعدش انجام دهی هدر رفته. و اگر کلید خارجی واقعی وجود داشت، دیگر لازم نیست به
حدس‌های این نقشه تکیه کنی.

فرض کنیم `MAX(Sal) = 1405` و برای ۱۴۰۵ `MAX(Mah) = 6` — پس مرداد (۵) داده
دارد. ادامه بده.

---

## گام ۱ — «واحد فروش» یعنی چه

دو ابهام که **جنسِ متفاوتی** دارند:

| ابهام | چه کنی |
|---|---|
| «واحد فروش» کدام `ccVahedSazmani` است؟ | خودت پیدا کن — جست‌وجو در `VahedSazmani` |
| زیرمجموعه‌هایش هم حساب می‌شوند؟ | **بپرس** — جواب عدد را عوض می‌کند |

اولی از داده حل می‌شود، دومی نه. `VahedSazmani` درخت است
(`ccVahedSazmaniLink`)، پس «واحد فروش» می‌تواند یک گره یا یک زیردرخت باشد.
اگر زیردرخت است، کوئری ۲.۲ لازم می‌شود.

---

## گام ۲ — کدام لایه

**«حقوق» دو چیز است** و باید انتخاب شود:

- `PersonelHokmHoghogh` — حقوق **مصوب**: چقدر باید می‌گرفتند.
- `PardakhtHoghogh` — حقوق **پرداختی**: چقدر گرفتند.

«حقوق مرداد چقدر شد» یعنی پرداختی. اگر کاربر «حقوق پایه‌ی واحد فروش» می‌پرسید،
جواب از جدول اول می‌آمد.

و در خودِ پرداختی سه عدد هست: ناخالص، مشمول، خالص. **پیش‌فرض را خالص بگیر و در
گزارش بنویس** — این یکی سؤالِ متوقف‌کننده نیست.

---

## گام ۳ — مسیر اتصال

```
python scripts/map.py path VahedSazmani PardakhtHoghogh --avoid Personel
```

مسیر واقعی سه جدول است:

```
VahedSazmani.ccVahedSazmani
  = PersonelHokmPostVahedSazmani.ccVahedSazmani     ← بازه‌دار
      PersonelHokmPostVahedSazmani.ccPersonel
        = PardakhtHoghogh.ccPersonel                ← Sal/Mah
```

> **`--avoid Personel` عمدی است.** بدون آن، BFS از لنگرگاه رد می‌شود و مسیر
> کوتاه‌تری پیدا می‌کند که واحد سازمانی را از دست می‌دهد. مسیرِ کوتاه‌تر همیشه
> مسیرِ درست نیست.

---

## گام ۴ — دو فیلتری که فراموش می‌شوند

```
python scripts/map.py table PersonelHokmPostVahedSazmani
```

می‌گوید `effective_dated` و `status_header` است. یعنی:

۱. **بازه:** عضویت در واحد در **کدام تاریخِ** مرداد؟ اول ماه، آخر ماه، یا هر
   روز که بود؟ کسی که ۲۰ مرداد جابه‌جا شده در کدام واحد شمرده می‌شود؟
   **پیش‌فرض: آخرین روز ماه، و در گزارش بنویس.**

۲. **وضعیت:** کوئری ۰.۷ را روی
   `PersonelHokmPostVahedSazmani_CodeVazeiat` بزن و کدِ تأییدشده را پیدا کن.
   بدون این، احکامِ باطل هم شمرده می‌شوند.

---

## گام ۵ — دانه، قبل از جمع

**این گام را رد نکن.** کوئری ۵.۱:

```sql
WITH params AS (SELECT 1405 AS sal, 5 AS mah)
SELECT COUNT(*) AS tedad_satr,
       COUNT(DISTINCT ph.ccPersonel) AS tedad_nafar,
       CAST(COUNT(*) AS decimal(18,2))
         / NULLIF(COUNT(DISTINCT ph.ccPersonel), 0) AS satr_be_ezaye_nafar
FROM [HumanResource].[PardakhtHoghogh] AS ph
CROSS JOIN params AS p
WHERE ph.Sal = p.sal AND ph.Mah = p.mah;
```

دو حالت:

- **`satr_be_ezaye_nafar = 1`** → هر نفر یک سطر. جمع بزن.
- **بزرگ‌تر از ۱** → اول بفهم چه چیزی سطرها را جدا می‌کند (`ccNoePardakhti`،
  `CodeNoeRecord`، `ccMarkaz`)، بعد تصمیم بگیر جمع می‌زنی یا تفکیک می‌کنی.
  **جمعِ کورکورانه یعنی حقوقِ چندبرابر.**

و یک تله‌ی دوم: اگر هم‌زمان بخواهی «تفکیک به اقلام» بدهی، `PardakhtHoghoghSatr`
را join می‌کنی و آن‌وقت هر نفر چند سطر می‌شود. **ستون‌های پهن و جدول سطر دو
نمایشِ یک چیزند** — کوئری ۵.۲ می‌گوید کدام مرجع است. جمعِ هر دو دوباره‌شماری
است.

---

## گام ۶ — کوئری

```sql
WITH params AS (
    SELECT 1405                       AS sal,
           5                          AS mah,
           CAST('2026-08-22' AS date) AS as_of,      -- آخرین روز مرداد، میلادی
           12                         AS cc_vahed,   -- واحد فروش
           3                          AS code_taeed  -- از کوئری ۰.۷
),
jaygah AS (
    SELECT DISTINCT hp.ccPersonel
    FROM [HumanResource].[PersonelHokmPostVahedSazmani] AS hp
    CROSS JOIN params AS p
    WHERE hp.ccVahedSazmani = p.cc_vahed
      AND hp.FromDate <= p.as_of
      AND (hp.EndDate IS NULL OR hp.EndDate > p.as_of)
      AND hp.CodeVazeiat = p.code_taeed
)
SELECT COUNT(DISTINCT ph.ccPersonel)        AS tedad_nafar,
       COUNT(*)                             AS tedad_satr,
       SUM(ph.MablaghKhalesPardakhti)       AS jam_khales,
       AVG(ph.MablaghKhalesPardakhti)       AS miangin_khales,
       SUM(ph.MablaghMaliat)                AS jam_maliat,
       SUM(ph.MablaghBimehPersonel)         AS jam_bimeh
FROM [HumanResource].[PardakhtHoghogh] AS ph
CROSS JOIN params AS p
JOIN jaygah AS j ON j.ccPersonel = ph.ccPersonel
WHERE ph.Sal = p.sal AND ph.Mah = p.mah;
```

`DISTINCT` داخل `jaygah` عمدی است: یک نفر می‌تواند دو حکمِ هم‌پوشان در یک واحد
داشته باشد (کوئری ۹.۱) و بدون `DISTINCT` حقوقش دو بار جمع می‌شود.

`tedad_satr` کنار `tedad_nafar` عمدی است — اگر برابر نبودند، گام ۵ را جدی
نگرفته‌ای.

---

## گام ۷ — گزارش

```
حقوق پرداختی واحد فروش — مرداد ۱۴۰۵

دوره      : ۱۴۰۵/۰۵ (سال ۱۴۰۵، ماه ۵ در PardakhtHoghogh)
تاریخ مبنا: عضویت واحد به تاریخ ۱۴۰۵/۰۵/۳۱ سنجیده شده
دامنه     : واحد سازمانی «فروش» (کد ۱۲) — بدون زیرمجموعه‌ها
لایه      : حقوق پرداختی (PardakhtHoghogh)، مبلغ خالص
منبع      : HumanResource.PardakhtHoghogh + PersonelHokmPostVahedSazmani
فیلتر وضعیت: فقط احکام با CodeVazeiat = ۳ («تأییدشده» از
             PersonelHokmPostVahedSazmani_CodeVazeiat)

┌───┬──────────────────────┬─────────────┐
│ ۱ │ تعداد نفرات          │          ۳۸ │
│ ۲ │ تعداد سطر پرداخت     │          ۳۸ │
│ ۳ │ جمع خالص پرداختی     │ ...         │
│ ۴ │ میانگین خالص         │ ...         │
└───┴──────────────────────┴─────────────┘

سطر ۲ برابر سطر ۱ است، یعنی هر نفر یک سطر پرداخت دارد و جمع دوباره‌شماری ندارد.

آنچه تأیید نشده: اتصال PersonelHokmPostVahedSazmani به PardakhtHoghogh از روی
هم‌نامی ccPersonel است و کلید خارجی ندارد.
```

**بدون نام و بدون مبلغ فردی** — سؤال گروهی بود.
[reporting.md](../references/reporting.md).

---

## آنچه در این مسیر پرسیده شد و آنچه پرسیده نشد

| پرسیده شد | چون |
|---|---|
| زیرمجموعه‌های واحد حساب شوند؟ | عدد را عوض می‌کند و از داده حل نمی‌شود |

| پرسیده نشد | چون |
|---|---|
| کدام `ccVahedSazmani` | از داده پیدا می‌شود |
| ناخالص یا خالص | پیش‌فرضِ معقول دارد؛ در گزارش نوشته شد |
| تاریخ مبنای عضویت | پیش‌فرضِ معقول دارد؛ در گزارش نوشته شد |
| کد وضعیت تأییدشده | از `X_CodeVazeiat` خوانده می‌شود |

**همه را با هم از قبل نپرس.** یک سؤالِ به‌جا بهتر از چهار سؤالِ پیشاپیش است.

---

## اگر جواب خالی درآمد

نه بگو «داده‌ای نیست» و نه حدس بزن چرا. سه چیز را بده:

۱. `MAX(Sal)` و `MAX(Mah)` واقعی از `PardakhtHoghogh`.
۲. اینکه کدام فیلتر خالی کرد — بدون فیلتر واحد چند سطر می‌شود؟ بدون فیلتر
   وضعیت چند؟ **یکی‌یکی بردار تا معلوم شود کدام کشنده بود.**
۳. پیشنهاد بعدی: «آخرین ماهِ موجود را بیاورم؟»

بیشترِ جواب‌های خالی در این اسکیما یکی از این دو است: کدِ وضعیتِ اشتباه، یا
`Sal`/`Mah`ِ شمسی که میلادی فرض شده.
