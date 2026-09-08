---
name: تسلط-خزانه-پگاه
description: نقشه‌ی اسکیمای Treasury پگاه — دریافت و پرداخت، اجازه پرداخت، تنخواه، صندوق، چک و سفته، وصول و تحصیل، بودجه و پیش‌بینی، مغایرت بانکی، کارت بانکی، تسویه معوقات و تسهیلات. جهانِ موازیِ PPC، جهتِ BedBes، و کدینگ حساب ccHesab0..7. Load when asked about treasury, cash, receipts, payments, cheques, petty cash, collections, bank reconciliation or payment authorization — خزانه، دریافت، پرداخت، اجازه پرداخت، تنخواه، صندوق، چک، سفته، وصول، تحصیلدار، مغایرت بانکی، بودجه، کارت بانکی، تسویه معوقات، تسهیلات، بستانکاری، محل واریز.
---

# تسلط خزانه پگاه

**۱۵۲ جدول در اسکیمای `Treasury` دیتابیس `PegahAI`** — و ۵۴ ویو که از نقشه
بیرون است. این اسکیما **پول** را جابه‌جا می‌کند؛ هر خطای دانه یا دوباره‌شماری
مستقیم به عددِ ریالی می‌رسد.

> **نقشه می‌گوید کجا را نگاه کنی؛ جواب از دیتابیس می‌آید.** نقشه برای پیدا
> کردنِ جدول، مسیر اتصال، دانه و تله قابل اعتماد است — دوباره کشفش نکن. ولی
> **هیچ عددی در گزارش از نقشه نمی‌آید**؛ هر رقمی باید از یک کوئری بیاید.

> **جهانِ موازیِ `PPC` — مهم‌ترین تله‌ی این اسکیما.** پنج جفت جدول با ساختارِ
> تقریباً یکسان و **همان نامِ کلید** وجود دارد:
> `DariaftPardakht` / `DariaftPardakhtPPC` (۵۴ در برابر ۶۳ ستون)، و همین‌طور
> `...Bargashty`، `...DarkhastFaktor`، `...FaktorZayeat`، `...Vazeiat`.
> `PPC` یعنی ثبت روی **دستگاه همراه**. اینکه به جدول اصلی سینک می‌شود یا
> موازی است **تصمیمِ کسب‌وکاری است و باید بپرسی**.
> **جمعِ هر دو یعنی دوباره‌شماریِ پول.**

> **`EjazehPardakhtFaktor` دروازه‌ی خروجِ پول است — و پرارجاع‌ترین پل به
> بقیه‌ی سیستم.** حقوق، وام، تسویه‌حساب و هزینه‌ی درمان در `HumanResource`،
> و اسناد در `Sales` و `AssetAccounting`، همه به آن ارجاع می‌دهند. هر سؤالِ
> «این پول کِی و با چه مجوزی پرداخت شد» از اینجا شروع می‌شود.

> **مبلغ فقط در سربرگ نیست.** `DariaftPardakhtVazeiat` خودش ستون `Mablagh`
> دارد — یعنی مبلغِ سند با تغییرِ وضعیت عوض می‌شود. برای «چقدر **واقعاً**
> وصول شد» ممکن است لازم باشد آخرین وضعیت را بگیری، نه سربرگ را. **این را
> قبل از هر گزارشِ وصول تعیین کن.**

> **`BedBes` جهت است، نه مقدار.** در `EjazehPardakhtFaktorSatr` و `Tankhah`
> مبلغ همیشه مثبت است و `BedBes` می‌گوید بده یا بستان. جمعِ بدونِ علامت،
> بدهکار و بستانکار را با هم جمع می‌کند و عددِ بی‌معنی می‌دهد.

> **`ccRefrence` چندریخت است** (`SandoghMarkazi`) و `ccLinkSandoghMarkazi`
> خودارجاع. بدونِ دانستنِ نوعشان join نکن.

## ترتیب کار

۱. **اول تأیید.** بخش ۰ [queries.md](references/queries.md): آخرین تاریخ،
   **تعداد سطرِ جدولِ اصلی در برابر PPC**، دیکشنری وضعیت، و جهتِ `BedBes`.

۲. **سؤال را به یک دامنه ببند.** جدول «نقشه‌ی دامنه» پایین.

۳. **جنس سؤال:** گردش (بازه‌ای) یا مانده (لحظه‌ای)؟ و **دریافت یا پرداخت** —
   `CodeNoeDariaftPardakht` این را جدا می‌کند.

۴. **مسیر اتصال:**

   ```python
   import subprocess, sys
   r = subprocess.run(
       [sys.executable, "skills/تسلط-خزانه-پگاه/scripts/map.py",
        "path", "EjazehPardakhtFaktor", "Tankhah"],
       capture_output=True, text=True, encoding="utf-8")
   print(r.stdout or r.stderr)
   ```

   با `kind='python'` اجرا کن، نه `kind='bash'`.

   دستورها: `table`، `refs`، `path`، `find`، `domain`، `external`، `traps`،
   `drift`.

۵. **دانه و علامت را با هم چک کن.** `BedBes` و وضعیت، هر دو.

۶. **گزارش بده.** [reporting.md](references/reporting.md) — بخش پول را رد نکن.

## نقشه‌ی دامنه — از کجا شروع کنی

| سؤال | جدول شروع | نکته |
|---|---|---|
| چه پولی جابه‌جا شد | `DariaftPardakht` | `CodeNoeDariaftPardakht` جهت را می‌گوید |
| با چه مجوزی پرداخت شد | `EjazehPardakhtFaktor` + `...Satr` | `ccBoodjeh` بودجه را می‌بندد |
| تخصیصِ حسابداری | `EjazehPardakhtFaktorSatr` | `ccHesab0..7` + `BedBes` |
| تنخواه | `Tankhah` + `TankhahDar` | `BedBes`؛ سقف در `SaghfTankhah` |
| صندوق | `Sandogh`، `SandoghMarkazi` | `SaghfeSandogh`؛ `IsForVosol` |
| چک | `DastehCheck` + `...Barg` | سریال و برگِ مانده |
| وصول | `Tahsildar`، `Config_Vosol*` | `ModatVosol` مهلت |
| بدهکاری مشتری | `ElamiehBedehkari` + `...Satr` | |
| بستانکاری مشتری | `BestankaryMoshtary`، `BestankariRoozMoshtary` | دو جدول، دو دانه |
| مغایرت بانکی | `MoghayeratBank` + `...Satr` | بازه‌دار |
| بودجه | `Boodjeh`، `Boodjeh_Hesab` | |
| پیش‌بینی نقدینگی | `Pishbini`، `ItemPishbini` | |
| تسویه معوقات | `TasviehMoavaghat_Boodjeh`، `Tamdid*` | |
| تسهیلات بانکی | `Tashilat` + `TashilatSatr` | |

`DariaftPardakht` (۲۵ ارجاع ورودی) و `EjazehPardakhtFaktor` (۱۴) دو مرکز
ثقل‌اند.

## قاعده‌های خواندن این اسکیما

### شناسه‌ی نوع‌دار

```
اگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB
```

**۱۱۰ یال، هیچ‌کدام کلید خارجیِ اثبات‌شده نیست.**

### جهت و علامت — قبل از هر `SUM`

دو ستون جهت را می‌گویند و هیچ‌کدام در خودِ مبلغ نیست:

| ستون | کجا | یعنی |
|---|---|---|
| `BedBes` | `EjazehPardakhtFaktorSatr`، `Tankhah` | بدهکار / بستانکار |
| `CodeNoeDariaftPardakht` | `DariaftPardakht` | دریافت / پرداخت |

**بدون اعمالِ اینها، جمعِ مبلغ عددِ بی‌معنی است.** و جهتِ واقعیِ هر کد را از
داده تأیید بگیر — کوئری ۰.۴.

### وضعیت

`CodeVazeiat` را فیلتر کن. `DariaftPardakhtVazeiat`، `TankhahVazeiat`،
`EjazehPardakhtFaktorVazeiat` و `KartBankVazeiat` هرکدام دیکشنریِ خودشان را
دارند و **کدهایشان یکسان نیست**.

و در این اسکیما تاریخچه‌ی وضعیت **مبلغ هم دارد** — بخش بالا.

### کدینگ حساب

`EjazehPardakhtFaktorSatr` ستون‌های `ccHesab0` تا `ccHesab7` و
`ccCodeHesab7Name` دارد — سطوحِ کدینگِ حساب. **اینجا خزانه به حسابداری وصل
می‌شود**؛ برای تفسیرشان به اسکیمای `FinancialAccounting` نیاز داری.

### جدول‌های موقت و آرشیو

۲۸ جدول در دامنه‌ی `gozaresh`: `Tmp_*`، `TMP_*`، `Sabegheh_*`،
`ArshiveCheck`، `MoeenHesabMoshtaryKol_Archive`، `MojodySandogh_Arshiv`.
`map.py domain gozaresh` همه را می‌دهد. **از هیچ‌کدام عدد نگیر.**

## پل به بقیه‌ی اسکیماها

۴۳ ارجاعِ `cc` این اسکیما مقصدشان بیرونِ `Treasury` است:

| مقصد | از | چه می‌دهد |
|---|---|---|
| `Global.MarkazPakhsh` | `ccMarkazPakhsh` | مرکز پخش |
| `Global.Afrad` | `ccAfrad*` | صندوق‌دار، تحصیل‌دار، تنخواه‌دار |
| `Global.ShomarehHesab` / `Global.Bank` | — | حساب و بانک |
| `Sales.Moshtary` | `ccMoshtary` | طرفِ وصول |
| `Sales.DarkhastFaktor` | `ccDarkhastFaktor` | فاکتور — منشأِ مطالبات |
| `Purchase.TaminKonandeh` | `ccTaminKonandeh` | طرفِ پرداخت |

**و در جهت عکس — این مهم‌ترین است:** `EjazehPardakhtFaktor` مقصدِ ارجاع از
`HumanResource` (حقوق، وام، تسویه‌حساب، هزینه درمان)، `Sales` و
`AssetAccounting` است. **این اسکیما جایی است که تعهدِ همه‌ی دامنه‌ها به پولِ
واقعی تبدیل می‌شود.**

## این اسکیل کجا تمام می‌شود

| سؤال | اسکیل |
|---|---|
| خزانه، دریافت/پرداخت، تنخواه، چک | **این** |
| فروش، فاکتور، هدف، تخفیف | `تسلط-فروش-پگاه` |
| انبار، موجودی، کالا | `تسلط-انبار-پگاه` |
| پرسنل و حقوق | `منابع-انسانی-پگاه` |
| نمره‌ی فروشنده | `ارزیابی-فروشنده-پگاه` (**تست‌شده**) |
| درجه‌بندی مشتری | `رتبه-بندی-مشتریان-پگاه` (**تست‌شده**) |

## سؤال‌های باز — از خزانه‌دار بپرس، خودت تصمیم نگیر

**همه را با هم نپرس.**

### الف) بار اول، قبل از هر گزارشِ ریالی — جهانِ PPC

**«جدولِ اصلی مرجع است یا PPC؟ یا هر کدام بخشی از سندها را دارند؟»**
تعداد سطر و آخرین تاریخِ هر دو را بگیر (کوئری ۰.۲)، عددها را نشان بده، و
بپرس. **تا این حل نشده، هیچ جمعِ ریالی قطعی نیست.**

### ب) وقتی سؤال «وصول» است

**«مبلغِ سربرگ یا مبلغِ آخرین وضعیت؟»** `DariaftPardakhtVazeiat` مبلغ دارد و
اگر با سربرگ فرق کند، یکی از این دو «وصول واقعی» است.

### ج) وقتی سؤال «مانده» است

**«مانده‌ی اول سال حساب شود؟»** `MandehAvalSalDariaftPardakht` جداست و جمعش
با گردشِ جاری بدون تصمیم، دوباره‌شماری است.

### د) وقتی سؤال حسابداری است

**«کدام سطحِ کدینگ؟»** `ccHesab0` تا `ccHesab7` هشت سطح‌اند و گزارش در سطحِ
اشتباه بی‌معنی است.

## وقتی داده‌ای نیست

- **بازه ردیف ندارد** → `MAX(ZamaneSabt)` روی `DariaftPardakht`.
- **جدول خالی است ولی PPC پر** → همان تله‌ی جهانِ موازی؛ بند الف.
- **جدول در نقشه نیست ولی مطمئنی هست** → `map.py drift`. نقشه از یک نسخه‌ی
  پشتیبان است؛ **نگو وجود ندارد**.

**با تخمین پر نکن** و **جدول از خودت نساز.**

## فایل‌های این اسکیل

- [references/queries.md](references/queries.md) — **اول این.**
- [references/entities.md](references/entities.md) — دامنه به دامنه.
- [references/relationships.md](references/relationships.md) — گراف، پل‌ها، تله‌ها.
- [references/reporting.md](references/reporting.md) — شکل گزارش و انضباطِ پول.
- `schema.json` — نقشه‌ی ماشین‌خوان. داده است، نه کد.
- `scripts/map.py` — پیمایش نقشه. اجرا کن، نخوان.
- [examples/walkthrough.md](examples/walkthrough.md) — یک سؤال واقعی از اول تا آخر.
