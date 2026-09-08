# موجودیت‌ها، دامنه به دامنه

برای هر دامنه: جدول مرجع، ستون‌هایی که واقعاً لازم می‌شوند، **دانه‌ی هر سطر**،
و آنچه اسم جدول نمی‌گوید.

> همه‌ی اینها از `HR Map.xlsx` درآمده، نه از دیتابیس زنده. ستون‌ها و نوع‌ها را
> قبل از تکیه کردن با کوئری ۰.۳ [queries.md](queries.md) تأیید کن.

پیشوند اسکیما در همه‌جا لازم است: `[HumanResource].[TableName]`.

---

## ۱. پرسنل — هویت و پرونده

### `Personel` — لنگرگاه اصلی

**دانه: یک سطر به ازای هر کارمند.** بیشترین ارجاع ورودی کل اسکیما به اینجاست.

| ستون | معنی |
|---|---|
| `ccPersonel` | کلید اصلی |
| `ccAfrad` | **پل به `Global.Afrad`** — نام و مشخصات فردی آنجاست |
| `ShomarehPersonely` | شماره پرسنلی؛ کلید انسانی، و کلیدِ `VorodKhorojPersonel` |
| `TarikhEstekhdam` / `TarikhEnfesal` | استخدام / انفصال |
| `CodeVazeiat` | وضعیت؛ معانی در `Personel_CodeVazeiat` |
| `IsBazneshasteh` / `ccNoeBazneshasteh` | بازنشستگی |
| `ccAfradModir` | مدیرِ مستقیم — **به `Global.Afrad` می‌رود، نه به `Personel`** |
| `ccPersonelVazeiatMoafiat_BimehMaliat` | معافیت بیمه/مالیات |
| `ShomarehBimeh` | شماره بیمه |
| `ccMarkazEstekhdam` | مرکز استخدام (بیرونی) |

> **نام کارمند در این جدول نیست.** نه `FName`، نه `LName`. از `ccAfrad` به
> `Global.Afrad` برو. اگر جواب بدون نام درآمد، همین جا را جا انداخته‌ای.

> **`ccAfradModir` سلسله‌مراتب را از مسیر `Afrad` می‌سازد نه `Personel`.** برای
> «تیمِ فلانی» باید `Personel.ccAfradModir` را به `Personel.ccAfrad`ِ زیردست‌ها
> وصل کنی، یعنی یک self-join از مسیر `ccAfrad`.

### پرونده‌ی فردی — همه با دانه‌ی «یک سطر به ازای هر رکورد، نه هر کارمند»

| جدول | چه چیزی | نکته |
|---|---|---|
| `PersonelTakmily` | اطلاعات تکمیلی | **`ccPersonel` کلید اصلی است** — یک‌به‌یک با `Personel` |
| `PersonelVabasteh` | افراد وابسته (خانواده، ضامن، معرف) | `IsFamily`/`IsZamen`/`IsMoaref`/`IsTahtehTakafol` — یک سطر می‌تواند چند نقش داشته باشد |
| `PersonelMadrakTahsily` | مدارک تحصیلی | چند سطر به ازای هر نفر |
| `PersonelSabegheKari` / `PersonelSavabeghKary` | **دو جدول سابقه‌ی کار** | هر دو زنده‌اند؛ اول بشمار |
| `PersonelKhedmatSarbazy` | خدمت سربازی | |
| `PersonelZaban` / `PersonelMaharatComputer` | زبان / مهارت | |
| `PersonelGavahinamehRanandegy` | گواهینامه | |
| `PersonelBimary` / `PersonelSabeghehBimari` | بیماری — **داده‌ی سلامت** | محرمانه |
| `PersonelShomarehHesab` | حساب بانکی | بازه‌دار؛ `CodeVazeiat` نوع `bit` |
| `PersonelPhoto` / `PersonelMadrak` / `Personel_Madrak` | تصویر و مدرک | **`PersonelMadrak` و `Personel_Madrak` دو جدول جدا با ساختار تقریباً یکسان‌اند** |
| `PersonelMoaref` | معرف | |
| `PersonelTashvighiEnzebati` | تشویق و انضباط — محرمانه | `Noe` در `NoeTashvighiEnzebati` تشویق را از انضباط جدا می‌کند |

### دیکشنری‌های پرسنلی

`BloodGroup`، `DinMazhab`، `VazeiatTaahol`، `MadrakTahsily`، `Reshteh`،
`ReshtehGeraiesh`، `MoasesehTahsili`، `NoeZaban`، `NoeMaharatComputer`،
`NoeGavahinamehRanandegy`، `NoeMadrak`، `YeganKhedmat`، `RastehKhedmat`،
`NoeMoafiat`، `Bimary`.

---

## ۲. سازمان — پست، شغل، واحد

| جدول | دانه | نکته |
|---|---|---|
| `VahedSazmani` | واحد سازمانی | `ccVahedSazmaniLink` **سلسله‌مراتب درختی** است — والدِ خودش |
| `Post` | پست سازمانی | `ccShoghl` شغل را می‌دهد؛ `ccShoghl_Old` را نگیر |
| `Shoghl` | شغل | |
| `PostShoghl` | پست × شغل | یک پست می‌تواند چند شغل داشته باشد |
| `ShoghlTitr` | عنوان شغلی | |
| `GorohShoghli` | گروه شغلی | پایه‌ی سنوات و حقوق پایه |
| `RastehShoghli` | رسته | **کلیدش `Id` است، نه `ccRastehShoghli`** |
| `VahedSazmani_Post` | تخصیص پست به واحد | |
| `VahedSazmaniPostShoghl` | واحد × پست‌شغل | مرجعِ `DarkhastJazbNiro` |
| `PostBimeh` | پستِ بیمه‌ای | برای لیست بیمه |

> **`VahedSazmani` درخت است.** `ccVahedSazmaniLink` به والد اشاره می‌کند. برای
> «همه‌ی زیرمجموعه‌های یک واحد» باید CTE بازگشتی بنویسی — کوئری ۲.۲.

> **چارت را از `Post`/`VahedSazmani` نگیر، از `PersonelHokmPostVahedSazmani`
> بگیر.** آن دو تعریف‌اند؛ اینکه چه کسی کجا نشسته در جدول حکم است و بازه دارد.

---

## ۳. قرارداد و حکم

### `PersonelGharardad` — قرارداد

**دانه: یک سطر به ازای هر قرارداد.** `FromDate`/`EndDate` هر دو `NOT NULL`.

| ستون | معنی |
|---|---|
| `ccNoeEstekhdam` | نوع استخدام → `NoeEstekhdam` |
| `ShomareGharardad` | شماره قرارداد |
| `CodeVaziat` | **`Vaziat` نه `Vazeiat`** — دیکشنری در `PersonelGharardad_CodeVazeiat` |
| `IsTasvieh` / `ccTasviyehesab` | تسویه شده؟ |

`PersonelGharardad_Movaghat` قراردادِ موقت است و `ccPersonelGharardad_Asli`
قرارداد اصلی را نشان می‌دهد. `PersonelGharardadVaziat` تاریخچه‌ی وضعیت.

> `NoeEstekhdam` فقط دیکشنری نیست — **قواعد مشمولیت بیمه و مالیات را حمل
> می‌کند**: `Mashmol_BimehPersonel`، `Mashmol_Maliat`، `Mashmol_HaghMaskan`،
> `IsMoaf_*`، `DarsadMaliatPardakhti`، `ErsalBeEdarehMaliat`. برای هر سؤال
> «چرا این نفر بیمه نشده» اول اینجا را ببین.

### `PersonelHokm` — حکم

**دانه: یک سطر به ازای هر حکم.** سربرگ است و چند جدولِ اقماری دارد که هرکدام یک
بُعد از حکم را نگه می‌دارند:

| جدول اقماری | چه بُعدی |
|---|---|
| `PersonelHokmHoghogh` | حقوق و مزایا |
| `PersonelHokmPostVahedSazmani` | پست و واحد |
| `PersonelHokmPostShoghl` | پست‌شغل و نوع همکاری |
| `PersonelHokmVahedSazmani` | واحد |
| `PersonelHokmShiftKary` | شیفت |
| `PersonelHokmVazeiat` | تاریخچه‌ی وضعیت |

> **`PersonelHokmPostVahedSazmani` مستقل از `PersonelHokm` هم زندگی می‌کند** —
> `ccPersonelHokm` ندارد و مستقیم به `ccPersonel` و `ccPersonelGharardad` وصل
> است. برای «کجای چارت نشسته» همین را بگیر و سراغ `PersonelHokm` نرو.

### `PersonelHokmHoghogh` — حقوق مصوب

**دانه: یک سطر به ازای هر حکم حقوقی، بازه‌دار.** سه لایه فیلتر می‌خواهد:

```sql
WHERE FromDate <= @AsOfDate AND (EndDate IS NULL OR EndDate > @AsOfDate)
  AND CodeVazeiat = <کد تأییدشده از PersonelHokmHoghogh_CodeVazeiat>
  AND ZamanGheirFaali IS NULL          -- غیرفعال نشده باشد
```

> **بازه‌دار بودن کافی نیست.** این جدول علاوه بر `FromDate`/`EndDate` هم
> `CodeVazeiat` دارد و هم `ZamanGheirFaali`/`UserGheirFaalkonandeh`. سطری که
> تاریخش می‌خورد ممکن است باطل یا غیرفعال شده باشد.

مبالغ پایه روی سربرگ‌اند (`MablaghMozdeShoghl`، `MablaghSanavat`،
`MablaghHaghFanni`) و پرچم‌های مشمولیت هم (`Maskan`، `Bon`، `HaghOlad`،
`Ezafekar`، `Nahar`، `Kharebar`). اقلام متغیر در
`PersonelHokmHoghoghSatr` (`ccItemHoghogh` + `Meghdar`).

`PersonelHokmHoghogh_SayerAvamel` + `...Satr_SayerAvamel` مسیر موازیِ «سایر
عوامل» است با همان ساختار. `PardakhtHoghogh` به هر دو ارجاع دارد.

---

## ۴. حقوق و دستمزد

### `ItemHoghogh` — دیکشنری اقلام حقوق

**مرکز ثقل دوم اسکیما.** هر قلم حقوقی یک سطر: مزد، اضافه‌کار، بن، مسکن، بیمه،
مالیات، کسورات. ستون‌های تصمیم‌ساز:

| ستون | معنی |
|---|---|
| `Noe_KaheshAfzayesh` | افزاینده یا کاهنده |
| `IsMazaya` / `IsKosorat` | مزایا / کسورات |
| `IsHoghoghMabna` / `IsKarkard` / `IsHokmHoghogh` | از کدام لایه می‌آید |
| `Noe_Roozaneh_Mahaneh` | روزانه یا ماهانه |
| `ccVahedMohasebehHoghogh` | واحد محاسبه |
| `Faal` | فعال بودن قلم |
| `ViewIn_Report_FishHoghogh` | در فیش دیده می‌شود |

> برای «مزایا چقدر شد» از `IsMazaya`/`IsKosorat` استفاده کن، نه از فهرست دستیِ
> اسم اقلام. اقلام عوض می‌شوند، پرچم‌ها می‌مانند.

جدول‌های وابسته: `ItemHoghogh_FormulMohasebeh` (فرمول)،
`ItemHoghogh_Mashmol_BimehMaliat` (مشمولیت، بازه‌دار)،
`ItemHoghogh_SabetPardakhti` (مبلغ ثابت، بازه‌دار)،
`ItemHoghogh_Sanavat_Eydi`، `ItemHoghogh_ChandPardakhti`.

### `PardakhtHoghogh` — پرداخت واقعی

**دانه‌ی اسمی: کارمند × سال × ماه. ولی این را باور نکن تا نشمرده‌ای.**
`ccNoePardakhti`، `CodeNoeRecord` و `ccMarkaz` می‌توانند چند سطر بدهند. کوئری
۵.۱ دانه را چک می‌کند.

سه دسته ستون:

1. **مبالغ پهن** — `MablaghMozdeShoghl`، `MablaghEzafeKar`، `MablaghMaliat`،
   `MablaghBimehPersonel`، `MablaghKhalesPardakhti`...
2. **سطرِ اقلام** — `PardakhtHoghoghSatr` با `ccItemHoghogh` + `Meghdar`.
3. **ستون‌های مرده** — پسوند `_deeeel`. استفاده نکن.

> **۱ و ۲ دو نمایشِ یک چیزند.** جمعِ هر دو دوباره‌شماری است. کدام مرجع است را
> با کوئری ۵.۲ مغایرت‌گیری کن.

ستون‌های روز کارکرد: `Tedad_RoozKarkard`، `TedadRoozKarkard_Sanavat`،
`TedadRoozKarkard_Eydi` — سه عددِ متفاوت برای سه هدف متفاوت.

`BastanListHoghogh` بستنِ لیست حقوق ماه است (سال، ماه، مرکز، وضعیت) — برای
«این ماه نهایی شده؟» همین را ببین.

### دور و برِ حقوق

| جدول | چه چیزی |
|---|---|
| `PardakhtEydi` | عیدی، جدا از حقوق ماهانه |
| `Karaneh` | کارانه |
| `PardakhtMosaedehGorohi` | مساعده |
| `AfzayeshHoghoghSalianeh` | افزایش سالانه؛ `..._Old` و `..._Jadid` حکم قبلی و جدید |
| `MaliatBarDaramadHoghogh` | جدول پلکان مالیات حقوق |
| `Zakhireh_ItemHoghogh` | ذخیره/تعهد — لایه‌ی سوم |
| `SerialDisketeHoghogh` / `Config_DisketHoghogh` | دیسکت بانک |

---

## ۵. کارکرد، شیفت، مرخصی، مأموریت

### `PersonelKarkard` — کارکرد روزانه

**دانه: یک سطر به ازای کارمند × روز.** واحد همه‌ی مقادیر **دقیقه** است
(`_Daghigheh`)، و ستون‌های `_Modat` همان عدد را متنی نگه می‌دارند.

`Karkard_Daghigheh`، `EzafehKar_Daghigheh`، `EzafehkarTatili_Daghigheh`،
`Takhir_Daghigheh`، `Gheybat_Daghigheh`، `Morakhasi_Daghigheh`،
`Mamoriat_Daghigheh`، `ShabKari_Daghigheh`، `NobatKari_Daghigheh`.

> **برای جمعِ ساعتی از ستون‌های `_Daghigheh` استفاده کن، نه `_Modat`.**
> `_Modat` رشته است و جمعِ رشته یعنی خطا یا الحاق.

`PersonelKarkardSatr` تردد داخل روز را می‌دهد (ورود/خروج، و ارجاع به
`ccPersonelMorakhasi` و `ccPersonelMamoriat`).

`VorodKhorojPersonel` تردد خام دستگاه است و **با `ShomarehPersonely` کلید
می‌خورد نه `ccPersonel`** — برای اتصال باید از `Personel.ShomarehPersonely` رد
شوی.

### شیفت — دو جهان موازی

| جهان | جدول‌ها | مشتری‌ها |
|---|---|---|
| **`ShiftKari`** (با i) | `ShiftKari` (پرستون: ساعت، رمضان، تأخیر مجاز، نوبت‌کاری) | `PersonelKarkard`، `TaghvimKariPersonel`، `GorohKari`، `GorohKariDorehGardesh` |
| **`ShiftKary`** (با y) | `ShiftKary` (فقط ۳ ستون) + `ShiftKarySatr` + `ShiftKaryTaghirat` | `PersonelShiftKary`، `PersonelHokmShiftKary` |

`ShiftKari` جدولِ پرمحتواست و `ShiftKary` نحیف — ولی `ShiftKary` جدول‌های
اقماری دارد و `ShiftKari` ندارد. **کدام زنده است را با `COUNT` و `MAX` تعیین
کن، بعد بپرس.**

`GorohKari` گروه کاری است و `TaghvimKariPersonel` تقویم کاریِ هر نفر به تفکیک
روز — برای «امروز شیفتش چه بود» این را بگیر.

### مرخصی

| جدول | نقش |
|---|---|
| `PersonelDarkhastMorakhasi` | درخواست |
| `PersonelMorakhasi` | مرخصیِ ثبت‌شده |
| `PersonelMorakhasiSatr` | سطر، با `Daghigheh_MorakhasiDarkhasti` و `..._Vaghei` |
| `PersonelMandehMorakhasi` | **دفترِ گردشِ مانده** |
| `NoeMorakhasi` | نوع، با سقف‌های مجاز |

> **`PersonelMandehMorakhasi` مانده را در یک ستون نگه نمی‌دارد** — دفترِ
> بدهکار/بستانکار است. `BedBes` جهت را می‌گوید و مانده از جمعِ جبریِ سطرها
> درمی‌آید. کوئری ۶.۲.

`NoeMorakhasi` سقف‌ها را دارد: `TedadRoozMojaz`، `TedadRoozMojazMah`،
`TedadRoozMojazGharardad`، `ModatMojazSabtMorakhasi_Daghigheh`.

### غیبت و مأموریت

`PersonelDarkhastGheybat` (با `BeginDate`) و `PersonelGheybat`.

**مأموریت دو جهان دارد:**

| جهان | سربرگ | اقماری |
|---|---|---|
| `PersonelMamoriat` | `ccPersonelMamoriat`؛ `ccNoeMamoriat`، `ccShahr`، `Masafat`، `Mablagh_FogholadehMamoriat` | `PersonelMamoriat_Madarek`، `PersonelMamoriatVazeiat` |
| `PersonelMamuryat` | `ccMamuryat`؛ `ccNoeMamuryat`، `ccOstan`، `ccVasile`، `FogholadeBegirad` | `PersonelMamuryat_Satr`، `PersonelMamuryat_Vazeiat`، `PersonelMamuryat_Madrak`، `PersonelMandehMamuryat` |

هر دو کاملند. `PersonelKarkardSatr` به **`PersonelMamoriat`** وصل است و
`PersonelMandehMamuryat` به **`PersonelMamuryat`**.

آیین‌نامه‌ی فوق‌العاده: `AeenNameFogholadehMamoriat` و نسخه‌های `...New` —
`AeenNameFogholadehMamoriatNew`، `...SatrNew`، `...PostNew`،
`...KilometrNew`. **جایی که `New` هست، بی‌`New` قدیمی است.**

---

## ۶. مالیات و بیمه

### مالیات

| جدول | نقش |
|---|---|
| `Maliat` | پلکان نرخ، بازه‌دار |
| `MaliatBarDaramadHoghogh` | پلکان مالیات حقوق به تفکیک نوع استخدام |
| `PersonelMaliat` | سربرگِ مالیات ماه (سال، ماه، مرکز، نحوه پرداخت) |
| `PersonelMaliatSatr` | **سطرِ مالیات هر نفر** — پرحجم‌ترین جدول مالیاتی |
| `PersonelMaliatInformation` | مشخصات ارسالی به اداره مالیات |
| `MaliatRizPersonel` / `MaliatTitrPersonel` | فایل خروجی؛ ستون‌ها شماره‌دارند (`Hoghogh17`) |
| `Maliat_RadifMaliati` + `...Satr` | نگاشتِ ردیف مالیاتی به `ItemHoghogh` |
| `DarsadTakhfifMaliat_Personel` | تخفیف، بازه‌دار |

> `MaliatRizPersonel` و `MaliatTitrPersonel` **قالبِ فایل سازمان امور
> مالیاتی‌اند**، نه جدول تحلیلی. اسم ستون‌ها شماره‌ی ستونِ فایل است. برای
> تحلیل از `PersonelMaliatSatr` استفاده کن.

### بیمه

| جدول | نقش |
|---|---|
| `ListBime` + `ListBimeSatr` | لیست بیمه؛ ستون‌ها با نام‌های `DSK_*`/`DSW_*` قالبِ تأمین اجتماعی‌اند |
| `PersonelSabeghehBimeh` | سابقه‌ی بیمه، بازه‌دار |
| `KargahBimeh` / `ShobehBimeh` / `MarkazBimeh` | کارگاه، شعبه، مرکز |
| `SherkateBimeh` / `BimehGharardad` | بیمه تکمیلی |
| `NoeNesbat_TarefeBimehTakmily` | تعرفه به تفکیک نسبت و سن، بازه‌دار |
| `BimehTakmilyPardakhti` | پرداختی تکمیلی |
| `PersonelVazeiatMoafiat_BimehMaliat` | معافیت |

`ListBimeSatr.ccPersonel` پل به پرسنل است؛ بقیه‌ی ستون‌ها فرمتِ فایل‌اند.

---

## ۷. رفاه، وام، درمان

### `DarkhastAzSandoghRefah` — درِ ورودیِ همه‌ی خدمات رفاهی

**این جدول از آنچه اسمش می‌گوید مهم‌تر است.** هم وام و هم هزینه‌ی درمان از
اینجا رد می‌شوند:

```
DarkhastAzSandoghRefah
  ├── DarkhastVam            (ccDarkhastAzSandoghRefah)
  ├── DarkhastVamSatr        (ccDarkhastAzSandoghRefah)  ← نه زیرِ DarkhastVam
  ├── DarkhastHazineDarmanSatr (ccDarkhastAzSandoghRefah) ← نه زیرِ DarkhastHazinehDarman
  └── SandoghRefah           (ccDarkhastAzSandoghRefah)
```

`SandoghRefah` دفترِ گردشِ صندوق است: `BedBes`، `MablaghPersonel`،
`MablaghSherkat`، و ارجاع به `ccPardakhtHoghogh` و `ccBazKharid`.

### وام

`DarkhastVam` (سربرگ) → `DarkhastVamPardakhtAghsat` (اقساط، با
`ccPardakhtHoghogh` که کسر از حقوق را نشان می‌دهد) و `DarkhastVamZamen`
(ضامن‌ها) و `DarkhastVamVazeiat` (تاریخچه).

قواعد: `AeenNamehVam`، `NoeVam_Items`، `SaghfeNoeVam`،
`AeenNamehVam_TakhsisMablaghPost`، `SaghfeMablaghAghsat`.

> برای «مانده‌ی وام» جمعِ اقساطِ پرداخت‌شده را از مبلغ وام کم کن؛ ستونی به اسم
> «مانده» وجود ندارد. `EnteghalAvalieh_MandehVam` فقط ماندهٔ ابتدای انتقال است.

### درمان

`DarkhastHazinehDarman` مسیر مستقیم، `DarkhastHazineDarmanSatr` مسیرِ زیرِ
صندوق. سقف‌ها در `AeenNamehHazinehDarman` و `SaghfeNoeHazineDarman`، و
گروه‌بندی در `GorohBandiHazinehDarman` + `...Satr`.

> `NoeHazinehDarman` زنده است و `NoeHazineDarman_Deeel` مرده — یک حرف فرق
> دارند و پسوند `_Deeel` تکلیف را روشن می‌کند.

---

## ۸. ارزیابی، آموزش، جذب

`ArzyabiPersonel` + `ArzyabiPersonelSatr` (نمره‌ی هر شاخص)، `FormArzyabi` +
`FormArzyabiSatr` (شاخص و وزن)، `ShakhesArzyabi`، `NoeRotbehArzyabi` (با
`Of_points`/`To_points` یعنی باندِ نمره)، `ArzyabiPersonel_TabaghebandiEmtiazat`.

`PersonelDorehAmozeshi` (+ `_Madrak`) آموزش.

جذب: `DarkhastJazbNiro` → `DarkhastJazbNiroAgahi` → `...Mosahebeh` →
`...MosahebehRadif`، و `Agahi`، و آزمون‌ها (`AzmoonNoe`، `AzmoonSoal`،
`AzmoonTitr`، `AzmoonSatr`، `AzmoonSoalEmtiyaz`).

> `PersonelMosahebeh` و `PersonelMosahebehRadif` به `ccPersonel` وصل‌اند — یعنی
> **متقاضی قبل از مصاحبه یک رکورد `Personel` دارد**. برای شمارش «کارمند فعلی»
> این‌ها را با `CodeVazeiat` کنار بگذار، وگرنه متقاضی‌های ردشده هم شمرده
> می‌شوند.

---

## ۹. تسویه‌حساب و خروج

**دو مسیر موازی برای یک کار:**

| جدول | ستون‌های شاخص |
|---|---|
| `TasviehHesab` + `TasviehHesabSatr` | `ccElatTasviehHesab`، `TarikhTasviehHesab`، `MablaghKhalesPardakhti`، `MablaghNahaee` |
| `BazKharid` | ستون‌های پهن: `Eydi`، `Sanavat`، `MandeMorakhasi`، `Vam1`..`Vam8`، `Bime`، `Maliat` |

`BazKharid` سبکِ قدیمی است (هشت ستون وام!) و `TasviehHesab` سبکِ سربرگ/سطر.
هر دو به `ccPardakhtHoghogh` و `ccPersonel` وصل‌اند، و
`PersonelMandehMorakhasi.ccBazKharid` و `SandoghRefah.ccBazKharid` هنوز به
`BazKharid` ارجاع می‌دهند.

> **`TasviehHesab.ccPersonelGharardad` و `ccDarkhastVam` نوعشان `varchar` است**
> در حالی که مقصدشان عددی است. یا لیست‌اند یا میراثِ قدیمی. قبل از join تأیید
> بگیر.

`Config_TasviehHesab`، `NoeTasviehHesab`، `ElatTasviehHesabeDaem`،
`MosaedeNazdikBazneshastegi`، `NoeBazneshasteh`.

---

## ۱۰. انتقال اولیه — `EnteghalAvalieh_*`

**یازده جدول که داده‌ی مهاجرت از سیستم قبلی‌اند، نه داده‌ی جاری.** با
`ShomarehPersonely` کلید می‌خورند (نه `ccPersonel`) و `Sal`/`Mah` انتقال را
دارند.

`EnteghalAvalieh_PersonelInfo`، `..._PersonelKarkard`،
`..._PersonelHokmHoghogh`، `..._PersonelHokmPostVahedSazmani`،
`..._MandehMorakhasi`، `..._MandehVam`، `..._SandoghRefah`،
`..._MaliatPardakhti`، `..._MadrakTahsily`، `..._AfradVabasteh`،
`..._ShomarehHesabPersonel`، `..._KhedmatSarbazy`.

> **در گزارشِ جاری استفاده نکن.** فقط وقتی لازم می‌شوند که سؤال درباره‌ی
> ماندهٔ ابتدای دوره یا صحت مهاجرت باشد. جمع کردنشان با داده‌ی جاری یعنی
> دوباره‌شماری.

---

## ۱۱. پیکربندی و گردش کار

`Config_*` قواعد گردش کار را نگه می‌دارند و همه یک شکل‌اند: `ccSystem`،
`CodeVazeiat`، `ccSystemNext`، `CodeVazeiatNext`، `ButtonText` — یعنی
**ماشینِ حالت**: از این وضعیت با این دکمه به آن وضعیت.

`Config_Vam`، `Config_VamDetail`، `Config_Morakhasi`، `Config_Mamoriat`،
`Config_TasviehHesab`، `Config_Eydi`، `Config_MohasebehHoghogh`،
`Config_BastanListHoghogh`، `Config_Hokm`، `Config_DastgahSaatZani`،
`Config_DisketHoghogh`، `Config_Item` (+ `Satr`، `Satr_Info`).

> برای «چه وضعیت‌هایی ممکن است و ترتیبشان چیست» به‌جای حدس زدن،
> `Config_<دامنه>` را بخوان. گردشِ واقعی همان‌جاست.

`SystemConfig` تنظیمات کلی: `MaxSenOlad`، `SaghfMorakhasiPardakhti_Rooz`،
`TedadMojazZemanat`، `Tabdil_KaranehBeEzafehkar`.

`MessageInbox` و `OutBoxEventItems` صفِ رویداد بین سرویس‌ها هستند — داده‌ی
کسب‌وکاری نیستند.

---

## ۱۲. مرکز و تقویم

`MarkazMohasebat` وضعیتِ محاسبات هر مرکز در هر ماه را نگه می‌دارد:
`IsHoghogh`، `IsTaeedNahaeeHoghogh`، `IsUpdateKarkard`،
`IsMohasebatTasviehHesab`، `IsEbtal`. برای «حقوق این ماه نهایی شده؟» این و
`BastanListHoghogh` را با هم ببین.

`TaghvimTatilManabeEnsani` تعطیلات منابع انسانی است — ممکن است با
`Global.Taghvim` یکی نباشد. اگر عددِ روز کاری مهم است، **هر دو را بگیر و
اختلاف را گزارش کن**.
