# اتصال‌ها، واژگان مشترک، و تله‌ها

قاعده‌ی کل این فایل یک خط است:

```
اگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB
```

**حدس، نه واقعیت.** هیچ‌کدام از این اتصال‌ها کلید خارجیِ اثبات‌شده نیست؛ همه از
هم‌نامی درآمده‌اند. کوئری ۰.۴ [queries.md](queries.md) کلیدهای واقعی را
می‌آورد — اگر وجود داشتند، آن‌ها حرف آخرند.

---

## ۱. مرکزهای ثقل — چه چیزی بیشترین ارجاع را دارد

| موجودیت | ارجاع ورودی | یعنی |
|---|---:|---|
| `Personel` | ۱۰۳ | لنگرگاه؛ هر سؤال کارمندمحور از اینجا |
| `ItemHoghogh` | ۱۸ | دیکشنری اقلام حقوق، مشترک بین تعریف و پرداخت و ذخیره |
| `PardakhtHoghogh` | ۱۶ | همه‌ی کسورات و پرداخت‌ها به آن گره می‌خورند |
| `Post` | ۱۶ | پست سازمانی |
| `VahedSazmani` | ۱۱ | واحد سازمانی |
| `PersonelGharardad` | ۱۰ | قرارداد |
| `NoeVam` | ۹ | نوع وام |
| `NoeMorakhasi` / `NoeNesbat` | ۷ | نوع مرخصی / نسبت |
| `DarkhastAzSandoghRefah` | ۶ | درِ ورودیِ خدمات رفاهی |
| `PersonelHokmPostVahedSazmani` | ۶ | جایگاه سازمانی بازه‌دار |

> `PardakhtHoghogh` با ۱۶ ارجاعِ ورودی **مقصد است نه مبدأ**: وام، مرخصیِ
> بازخریدی، مأموریت، صندوق رفاه، بیمه و مالیات همه به آن اشاره می‌کنند. برای
> «در فیش این ماه چه چیزهایی کسر شد» باید معکوس بگردی — کوئری ۵.۳.

---

## ۲. مسیرهای پرکاربرد — دستی، بدون اسکریپت

### کارمند تا هویت کامل
```
Personel.ccAfrad → Global.Afrad.ccAfrad
```

### کارمند تا جایگاه سازمانی در یک تاریخ
```
Personel.ccPersonel
  → PersonelHokmPostVahedSazmani.ccPersonel        (بازه‌دار + CodeVazeiat)
      → Post.ccPost           → Shoghl.ccShoghl
      → VahedSazmani.ccVahedSazmani                (درختی)
```

### کارمند تا حقوق مصوب در یک تاریخ
```
Personel.ccPersonel
  → PersonelHokmHoghogh.ccPersonel   (بازه‌دار + CodeVazeiat + ZamanGheirFaali)
      → PersonelHokmHoghoghSatr.ccPersonelHokmHoghogh
          → ItemHoghogh.ccItemHoghogh
```

### کارمند تا پرداخت واقعی یک ماه
```
Personel.ccPersonel
  → PardakhtHoghogh.ccPersonel        (Sal + Mah؛ دانه را بشمار)
      → PardakhtHoghoghSatr.ccPardakhtHoghogh
          → ItemHoghogh.ccItemHoghogh
```

### وام تا کسر از حقوق
```
Personel → DarkhastVam.ccPersonel
  → DarkhastVamPardakhtAghsat.ccDarkhastVam
      → PardakhtHoghogh.ccPardakhtHoghogh
```

### کارکرد تا شیفت
```
Personel → PersonelKarkard.ccPersonel
  → ShiftKari.ccShiftKari        ← دقت: ShiftKari با i
  → GorohKari.ccGorohKari
  → PersonelKarkardSatr.ccPersonelKarkard
```

### مرخصی تا مانده
```
Personel → PersonelMorakhasi.ccPersonel
  → PersonelMorakhasiSatr.ccPersonelMorakhasi
Personel → PersonelMandehMorakhasi.ccPersonel      (دفترِ بد/بس)
```

### تسویه‌حساب
```
Personel → TasviehHesab.ccPersonel → TasviehHesabSatr.ccTasviehHesab → ItemHoghogh
Personel → BazKharid.ccPersonel                    (مسیر دوم، سبک قدیمی)
```

---

## ۳. واژگان مشترک/بیرونی — `cc`هایی که در `HumanResource` جدول ندارند

اینها در `HumanResource` جدول ندارند. **۲۸ تای آنها در اسکیمای دیگری پیدا
شدند** (ستون «مقصد»)؛ بقیه واقعاً بیرون از این دیتابیس‌اند. فهرست کامل و
اثبات‌شده در `schema.json` بخش `cross_schema` — یا
`python scripts/hr_map.py external`. **جدولِ محلی برایشان نساز.**

| `cc` | تکرار | تفسیر | مقصد |
|---|---:|---|---|
| `ccUserSabtKonandeh` | ۶۸ | کاربرِ ثبت‌کننده | **حل‌نشده** — در هیچ اسکیمای `PegahAI` نیست |
| `ccMarkaz` | ۵۳ | مرکز | ✔ `Global.Markaz` |
| `ccElatOdat` | ۳۷ | علت برگشت | ✔ `Global.ElatOdat` — **ولی اول جدولِ دامنه‌ی خودت** |
| `ccUser` | ۲۹ | کاربر | **حل‌نشده** — دامنه‌ی امنیت بیرون از این دیتابیس |
| `ccSystem` | ۲۵ | سیستم/زیرسامانه | ✔ `dbo.System` |
| `ccPhoto` | ۲۳ | تصویر/پیوست | ✔ `Global.Photo` |
| `ccAfrad` | ۱۵ | **شخص** | ✔ `Global.Afrad` — **پل به فروش** |
| `ccMarkazPakhsh` | ۱۰ | مرکز پخش | ✔ `Global.MarkazPakhsh` |
| `ccShahr` / `ccOstan` | ۹ / ۳ | شهر / استان | **حل‌نشده** — `Global.Shahr` وجود ندارد |
| `ccBank` / `ccShomarehHesab` | ۵ / ۴ | بانک / حساب | ✔ `Global.Bank` / `Global.ShomarehHesab` |
| `ccEjazehPardakhtFaktor` | ۷ | اجازه پرداخت | ✔ `Treasury.EjazehPardakhtFaktor` |
| `ccCompany` | ۲ | شرکت | ✔ `Global.Company` |
| `ccTafsily` / `ccMarkazHazineh` | — | تفصیلی / مرکز هزینه | ✔ `FinancialAccounting.*` |

✔ یعنی جدولِ هم‌نام در آن اسکیما **وجود دارد** (از فهرست کاملِ اشیای
`PegahAI`). یعنی مقصد قطعی است؛ اینکه ستون‌ها واقعاً به هم می‌خورند هنوز
آزمونِ یتیم می‌خواهد.

> **`ccElatOdat` هر دو است — و این را اول اشتباه نوشته بودم.**
> `Global.ElatOdat` **وجود دارد**، ولی هر دامنه جدولِ علتِ **خودش** را هم
> دارد: `PersonelMorakhasi_ElatOdat`، `DarkhastVamZamen_ElatOdat`،
> `PersonelHokmHoghogh_ElatOdat`، `TasviehHesab_ElatOdat`... . کد ۲ در یکی با
> کد ۲ در دیگری فرق دارد. **پیش‌فرض: به جدولِ علتِ همان دامنه join کن**؛ اگر
> نبود، سراغ `Global.ElatOdat` برو.

> **`ccAfrad` مهم‌ترینِ این فهرست است.** `Personel.ccAfrad` و
> `Sales.AmarForosh_Arshive.ccAfradForoshandeh` هر دو به `Global.Afrad`
> می‌روند — پرونده‌ی پرسنلی به عملکرد فروش وصل می‌شود. تأیید بگیر، بعد استفاده
> کن.

---

## ۴. تله‌ها

### ۴.۱ جدول‌های دوقلو — یک حرف فرق، دو جهان

| جفت | فرق | مشتری‌های هرکدام |
|---|---|---|
| `ShiftKari` / `ShiftKary` | i در برابر y | `PersonelKarkard`، `TaghvimKariPersonel`، `GorohKari` → **Kari** ‖ `PersonelShiftKary`، `PersonelHokmShiftKary`، `ShiftKarySatr`، `ShiftKaryTaghirat` → **Kary** |
| `PersonelMamoriat` / `PersonelMamuryat` | o در برابر u | `PersonelKarkardSatr` → **Mamoriat** ‖ `PersonelMandehMamuryat` → **Mamuryat** |
| `NoeMamoriat` / `NoeMamuryat` | همان | هرکدام به جهانِ خودش |
| `ItemSandoghRefah` / `ItemhayeSandoghRefah` | `haye` | `SandoghRefah` → **ItemSandoghRefah** |
| `ItemHoghogh` / `ItemhayeHoghogh` | `haye` | همه‌ی حقوق → **ItemHoghogh**؛ `ItemhayeHoghogh` جدولِ کوچکِ جداست |
| `TasviehHesab_ElatOdat` / `Tasviehesab_ElatOdat` | یک `H` | هر دو موجودند |
| `PersonelMadrak` / `Personel_Madrak` | یک `_` | ساختار تقریباً یکسان |
| `PersonelSabegheKari` / `PersonelSavabeghKary` | کل کلمه | هر دو سابقه‌ی کار |
| `NoeHazinehDarman` / `NoeHazineDarman_Deeel` | `_Deeel` | دومی **مرده** |
| `BastanListHoghogh` / `BastaneListHoghogh` | یک `e` | هر دو موجودند |

**اشتباه گرفتنشان خطای SQL نمی‌دهد** — نتیجه‌ی خالی یا ناقص می‌دهد، که بی‌صداتر
است. قبل از استفاده `COUNT(*)` هر دو را بگیر (کوئری ۰.۵).

### ۴.۲ ناسازگاری نوع — join این‌ها بدون `CAST` می‌شکند یا کند می‌شود

| ستون | نوع اعلام‌شده | نوعِ مقصد | خطر |
|---|---|---|---|
| `VaziatZaheri.ccPersonel` | `nvarchar` | `int` | تبدیل ضمنی، شکست روی داده‌ی بد |
| `TasviehHesab.ccPersonelGharardad` | `varchar` | `int` | ممکن است لیست باشد |
| `TasviehHesab.ccDarkhastVam` | `varchar` | `bigint` | ممکن است لیست باشد |
| `MaliatBarDaramadHoghogh.ccNoeEstekhdam` | `nvarchar` | `tinyint` | ممکن است چندمقداری باشد |
| `GorohKari.ccShiftKari` | `varchar` | `int` | ممکن است فهرست شیفت باشد |
| `ShiftKari.ccNoeVorod` / `ccNoeKhoroj` | `varchar` | — | |
| `TarefeBimehTakmily_SabeghehPersonel.ccNoeNesbat` | `nvarchar` | `tinyint` | |

> **ستون `varchar` که باید عدد باشد، معمولاً یعنی چندمقداری است.** قبل از
> `CAST`، چند سطرِ نمونه را ببین — اگر «۱۲,۱۵,۱۸» بود، join معمولی جواب
> نمی‌دهد.

### ۴.۳ عرضِ ناسازگار — سرریز و برش

| ستون فرزند | نوع | ستون والد | نوع | خطر |
|---|---|---|---|---|
| `PardakhtHoghoghSatr.ccPardakhtHoghogh` | `int` | `PardakhtHoghogh.ccPardakhtHoghogh` | **`bigint`** | فرزند کوچک‌تر از والد |
| `PersonelMaliatSatr.ccPardakhtHoghogh` | `int` | همان | `bigint` | همان |
| `DarkhastVamPardakhtAghsat.ccPardakhtHoghogh` | `int` | همان | `bigint` | همان |
| `TasviehHesab.ccPardakhtHoghogh` | `int` | همان | `bigint` | همان |
| `PardakhtEydi.ccPardakhtHoghogh` | `int` | همان | `bigint` | همان |
| `Zakhireh_ItemHoghogh.ccItemHoghogh` | **`tinyint`** | `ItemHoghogh.ccItemHoghogh` | `int` | **سقف ۲۵۵** |
| `Personel_Madrak.ccPersonel` | `bigint` | `Personel.ccPersonel` | `int` | فرزند بزرگ‌تر |

> **`PardakhtHoghogh.ccPardakhtHoghogh` کلیدِ `bigint` است ولی تقریباً همه‌ی
> فرزندانش آن را `int` نگه می‌دارند.** تا وقتی شناسه‌ها زیر ۲٫۱ میلیارد بمانند
> مشکلی پیش نمی‌آید، ولی این را در گزارشِ کیفیت داده بنویس.

> **`Zakhireh_ItemHoghogh.ccItemHoghogh` از نوع `tinyint` است.** یعنی قلم‌های
> حقوقیِ با کد بالای ۲۵۵ اصلاً در این جدول ذخیره نمی‌شوند. اگر جمعِ ذخیره با
> جمعِ اقلام نخواند، اول اینجا را ببین.

### ۴.۴ ستون‌های مرده

**مرده — استفاده نکن:**

`PardakhtHoghogh`: `Mablagh_MashmolBimeh_deeeel`، `MablaghBimeh_Pardakhti_deeeel`،
`MablaghBimeh_Bikari_deeeel`، `MablaghBimeh_SahmKarfarma_deeeel`،
`MablaghBimeh_SahmPersonel_deeeel`، `Mablagh_HaghOlad_deeeel`،
`cctmp_PardakhtHoghogh_deeeel`، `Mablagh_MashmolMaliat_old`.

`PersonelMorakhasiSatr`: `BedBes_deeeel`، `Kind_deeeel`.

`Post`: `ccShoghl_Old`.

**زنده با معنیِ «قبلی» — لازم است:**

`AfzayeshHoghoghSalianeh.ccPersonelHokmHoghogh_Old` در برابر
`..._Jadid` — حکم قبلی و حکم جدید. این `_Old` مرده نیست.

**مشکوک — اول ببین:**

`SandoghRefah.MablaghPersonelOLD` و `MablaghSherkatOLD` کنارِ
`Mablagh_SahmPersonel` و `Mablagh_SahmSherkat` نشسته‌اند. کدام مرجع است معلوم
نیست؛ با کوئری مغایرت‌گیری تعیین کن.

### ۴.۵ جدول‌هایی که در فهرست ماندند ولی نباید بمانند

سند اصلی قرار بود میراث را کنار بگذارد؛ اینها از قلم افتاده‌اند:

`PersonelKarkard_oooold`، `DELETED_vShoghlSharh`،
`DELETED_vKarKardMamoorPakhshKaregarAnbar`، `MaliatMoshakhasateKarfarmaBackup`،
`Tmp_Rpt_SandoghRefah`، `PersonelKarkard_ExcelDariafti_Arshive`،
`PersonelKarkard_ExcelDariafti_Arshive_Nahaee`، `NoeHazineDarman_Deeel`،
`Insert_VamDasti`، `ShomarehPersonel_SabtNashodeh`،
`Personel_GheyreFaal_Voc`، `ListPersonelForDeleteDastresi_InJob`،
`personel_UpdateKarkardByJob`.

سه دسته‌اند: میراث (`_oooold`، `DELETED_`، `Backup`)، موقت/گزارشی (`Tmp_`،
`_Arshive`)، و صفِ کار (`_InJob`، `ByJob`). **هیچ‌کدام منبعِ حقیقت نیستند.**

### ۴.۶ کلیدهایی که `cc` نیستند

بعضی جدول‌ها از قرارداد نام‌گذاری بیرون‌اند و کلیدشان `Id` یا `<Name>Id` است:

`RastehShoghli.Id`، `PardakhtHoghogh_CodeVazeiat.Id`، `Maliat_RadifMaliati.Id`،
`Maliat_RadifMaliatiSatr.Id`، `MessageInbox.Id`،
`LitsBimeh_AdamErsalPersonel.Id`، `MashmolBimehMaliat_NoeMashmol.Id`،
`NoeFormArzyabi_SendConfig.ID`، `ArzyabiPersonel_TabaghebandiEmtiazat.ID`،
`PersonelMaliatSatrNew.PersonelMaliatSatrId`،
`TasviehHesab_PersonelForTasvieh.TasviehHesab_PersonelForTasviehId`،
`SaghfeMablaghAghsat.SaghfeMablaghAghsatId`،
`TashvighiBeNesbatRoozKarkard.TashvighiBeNesbatRoozKarkardId`،
`BimehTakmilyPardakhti.BimehTakmilyPardakhtiId`،
`OutBoxEventItems.OutBoxEventItemId`، `Kind_Vam.KIND`،
`PersonelHokmHoghoghSatr_SayerAvamel.PersonelHokmHoghoghSatr_SayerAvamel`.

> این جدول‌ها معمولاً **تازه‌ترند** — ستون‌های `CreatedByUserId` /
> `CreatedDateTime` / `ModifiedDateTime` و `BusinessId` از نوع
> `uniqueidentifier` نشانه‌ی لایه‌ی جدید سیستم‌اند (`NoeMorakhasi`،
> `BimehTakmilyPardakhti`، `OutBoxEventItems`). جایی که هر دو سبک کنار هم‌اند،
> سبکِ جدید احتمالاً مرجع است — ولی تأیید بگیر.

### ۴.۷ ارجاع‌های `_Link` — خودارجاع، نه اتصال به بیرون

`ccXLink` معمولاً یعنی **والدِ خودِ همان جدول** (سلسله‌مراتب):
`VahedSazmani.ccVahedSazmaniLink`، `DinMazhab.ccDinMazhabLink`،
`ReshtehGeraiesh.ccReshtehGeraieshLink`، `NoeHazinehDarman.ccNoeHazinehDarmanLink`،
`ShakhesArzyabi.ccShakhesArzyabiLink`، `NoeRotbehArzyabi.ccNoeRotbehArzyabiLink`،
`PersonelVabasteh.ccPersonelVabasteh_Link`.

ولی `PersonelHokmHoghogh.ccPersonelHokmPostVahedSazmani_Link` و
`ElatTasviehHesabeDaem.ccLink` و `ElateBedehy.ccLink` این‌طور نیستند — به جدول
دیگری می‌روند. **`_Link` را خودکار خودارجاع فرض نکن.**

---

## ۵. الگوهای ساختاری — از روی اسم بشناس

| الگو | معنی | مثال |
|---|---|---|
| `X` + `XSatr` | سربرگ و سطر | `PardakhtHoghogh` + `PardakhtHoghoghSatr` |
| `X_Madarek` / `X_Madrak` | پیوست و مدرک | `DarkhastVam_Madarek` |
| `X_Vazeiat` / `XVazeiat` | تاریخچه‌ی گردش | `DarkhastVamVazeiat` |
| `X_CodeVazeiat` | دیکشنری کد وضعیت | `TasviehHesab_CodeVazeiat` |
| `X_ElatOdat` | علت برگشت | `PersonelMorakhasi_ElatOdat` |
| `Noe*` | دیکشنری نوع | `NoeVam`، `NoeMorakhasi` |
| `AeenNameh*` / `AeenName*` | آیین‌نامه و قاعده، بازه‌دار | `AeenNamehVam` |
| `Saghf*` | سقف | `SaghfeNoeVam` |
| `Config_*` | ماشینِ حالتِ گردش کار | `Config_Vam` |
| `EnteghalAvalieh_*` | داده‌ی مهاجرت | `EnteghalAvalieh_MandehVam` |
| `Darkhast*` | درخواست | `DarkhastVam` |
| `*_Movaghat` | نسخه‌ی موقت/پیش‌نویس | `PersonelGharardad_Movaghat` |
| `*New` | نسخه‌ی جایگزین | `AeenNameFogholadehMamoriatNew` |

> **`*New` یعنی نسخه‌ی بی‌`New` قدیمی است** — ولی هر دو در دیتابیس‌اند و ممکن
> است هر دو داده داشته باشند. بشمار، بعد تصمیم بگیر.

> **`Madarek` و `Madrak` هر دو استفاده شده‌اند** و به یک معنی‌اند. موقع
> جست‌وجوی اسم هر دو را امتحان کن.
