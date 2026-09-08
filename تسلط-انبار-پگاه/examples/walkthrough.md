# یک سؤال واقعی، از اول تا آخر

**سؤال کاربر:** «موجودی انبار مرکز تهران الان چقدر است؟»

سؤالِ کوتاهی که چهار تصمیم در آن پنهان است — و یکی از آنها تفاوتِ بینِ جوابِ
درست و جوابی است که چند برابر بزرگ‌تر درمی‌آید **بدون اینکه غلط به نظر
برسد**.

---

## گام ۰ — «موجودی» یعنی گردش یا عکس؟

**اولین و مهم‌ترین تصمیم.** دو جوابِ کاملاً متفاوت:

| اگر منظور | از کجا |
|---|---|
| «الان چقدر هست» | `MojodyForosh` — عکسِ روزانه |
| «در بازه چه گذشت» | `Kardex` + `KardexSatr` — دفترِ حرکت |

«الان چقدر است» یعنی عکس. **این را نپرس؛ از خودِ سؤال معلوم است.**

## گام ۱ — تله‌ی اصلی: `MojodyForosh` تاریخ‌دار است

```sql
SELECT MAX(Tarikh) AS akharin, COUNT(DISTINCT Tarikh) AS tedad_rooz
FROM [Warehouse].[MojodyForosh];
```

`MojodyForosh` **هر روز یک نسخه** دارد. اگر بدون فیلترِ تاریخ جمع بزنی،
موجودی به تعدادِ روزها ضرب می‌شود — و چون عددِ بزرگ و به‌ظاهر معقول درمی‌آید،
**هیچ‌کس متوجه نمی‌شود**. این خرابیِ خاموشِ این دامنه است.

## گام ۲ — کدام انبار، و آیا ضایعات حساب می‌شود

`MojodyForosh` موجودیِ **قابل فروش** است. ضایعات و قرنطینه جدولِ جدا دارند:
`MojodyAnbarZayeat` و `MojodyAnbarGharantineh`.

**این را بپرس** — «موجودی» برای انباردار ممکن است شاملشان باشد و برای فروش نه.

و «مرکز تهران» را پیدا کن:

```sql
WITH params AS (SELECT N'%تهران%' AS nam)
SELECT a.ccAnbar, a.NameAnbar, a.ccMarkazPakhsh, a.Faal
FROM [Warehouse].[Anbar] AS a
CROSS JOIN params AS p
WHERE a.NameAnbar LIKE p.nam
ORDER BY a.NameAnbar;
```

`Faal` را نگاه کن — انبارِ غیرفعال هم ممکن است سطر داشته باشد.

## گام ۳ — کدام واحد

کوئری ۰.۲ [queries.md](../references/queries.md). اینجا کار ساده است چون
`MojodyForosh` خودش ستونِ تک‌واحدیِ `Mojody` دارد — سه‌گانه‌ی
`Tedad1/2/3` مالِ `KardexSatr` است.

## گام ۴ — کوئری

```sql
WITH params AS (SELECT CAST(NULL AS int) AS cc_markaz),
akharin AS (
    SELECT MAX(Tarikh) AS tarikh FROM [Warehouse].[MojodyForosh]
)
SELECT m.ccMarkazPakhsh,
       COUNT(DISTINCT m.ccKalaCode)                              AS tedad_kala,
       COUNT(DISTINCT CONCAT(m.ccKalaCode, '|', m.ShomarehBach)) AS tedad_kala_bach,
       SUM(m.Mojody)                                             AS jam_mojody,
       SUM(m.Mojody * m.MablaghForosh)                           AS arzesh_forosh,
       MAX(t.tarikh)                                             AS tarikh_aks
FROM [Warehouse].[MojodyForosh] AS m
CROSS JOIN params AS p
CROSS JOIN akharin AS t
WHERE m.Tarikh = t.tarikh
  AND (p.cc_markaz IS NULL OR m.ccMarkazPakhsh = p.cc_markaz)
GROUP BY m.ccMarkazPakhsh
ORDER BY jam_mojody DESC;
```

سه چیز عمدی:

- **`m.Tarikh = t.tarikh`** — قلبِ درستیِ این کوئری.
- **`tedad_kala` کنارِ `tedad_kala_bach`** — نشان می‌دهد بچ چقدر دانه را ضرب
  کرده.
- **`tarikh_aks` در خروجی** — تا خواننده بداند عکس از چه تاریخی است.

## گام ۵ — گزارش

```
موجودی قابل فروش — مرکز تهران

تاریخِ عکس : <آخرین Tarikh در MojodyForosh> (میلادی و شمسی)
دامنه      : انبارهای فعالِ مرکز <کد> — بدون ضایعات و قرنطینه
منبع       : Warehouse.MojodyForosh (عکسِ روزانه، نه گردش)
واحد       : ستون Mojody

┌───┬──────────────┬────────────┬──────────────┬─────────────┐
│ ۱ │ تعداد کالا   │ کالا×بچ    │ جمع موجودی   │ ارزش فروش   │
└───┴──────────────┴────────────┴──────────────┴─────────────┘

ضایعات و قرنطینه در این عدد نیستند (MojodyAnbarZayeat و
MojodyAnbarGharantineh جدولِ جدا دارند).

تأییدنشده: اتصال ccKalaCode به Kala از هم‌نامیِ کلیدِ دوم است و کلید خارجی
ندارد؛ N کالا از M کالا نام گرفتند.
```

---

## چه پرسیده شد و چه پرسیده نشد

| پرسیده شد | چون |
|---|---|
| ضایعات و قرنطینه حساب شوند؟ | تعریفِ «موجودی» بین انبار و فروش فرق دارد |

| پرسیده نشد | چون |
|---|---|
| گردش یا عکس | «الان چقدر است» یعنی عکس |
| کدام تاریخ | آخرین — با `MAX` معلوم می‌شود |
| کدام انبار «تهران» است | با `LIKE` پیدا می‌شود |
| واحد | `MojodyForosh.Mojody` تک‌ستونی است |

**سؤالی که با یک کوئری جواب می‌گیرد، سؤال نیست.**

---

## اگر جواب خالی درآمد

۱. `MAX(Tarikh)` واقعی — شاید عکسِ امروز هنوز ساخته نشده.
۲. فیلترها را یکی‌یکی بردار تا معلوم شود کدام کشنده بود.
۳. `Faal` انبار را چک کن.

معمول‌ترین علتِ خالی بودن در این دامنه: **فیلترِ تاریخ روی روزی که عکس
ندارد**.
