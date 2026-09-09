# منابع-انسانی-پگاه

اسکیل تسلط بر اسکیمای `HumanResource`، در فرمت استاندارد `SKILL.md`. مستقل است:
این پوشه را هرجا بگذاری کار می‌کند.

```
SKILL.md                      دستورالعمل — چیزی که مدل هر بار می‌خواند
schema.json                   نقشه‌ی ماشین‌خوان ۴۱۳ جدول و ۴۳۳ یال (داده، نه کد)
scripts/map.py                پیمایش نقشه — table / refs / path / find / domain / external / crossref / traps / drift
scripts/hr_map.py             نامِ قدیمی — به map.py می‌سپارد
references/entities.md        دامنه به دامنه: جدول مرجع، ستون‌های مهم، دانه
references/relationships.md   گراف اتصال، واژگان مشترک، و فهرست کامل تله‌ها
references/queries.md         کوئری‌های تأیید و الگوهای آماده
references/reporting.md       شکل گزارش و محرمانگی
examples/walkthrough.md       یک سؤال واقعی از اول تا آخر
```

## این اسکیل با دو اسکیل دیگر یک فرق بنیادی دارد

`ارزیابی-فروشنده-پگاه` و `رتبه-بندی-مشتریان-پگاه` روی داده‌ی زنده تست شده‌اند و
عددهای واقعی دارند. **این یکی نه.**

منبعش `HR Map.xlsx` است: فهرست جدول، ستون، نوع داده و NULL‌پذیری — و **نه** کلید
خارجی، نه ایندکس، نه رویه‌ی ذخیره‌شده، نه سطر نمونه. هر ۴۳۳ اتصالِ داخلی از
روی **هم‌نامی** حدس زده شده‌اند.

نتیجه‌ی عملی: **بخش ۰ `queries.md` بخشی از کار است، نه مقدمه‌ی اختیاری.** اگر
دیتابیس کلید خارجی واقعی داشته باشد، آن حرف آخر است و این نقشه فقط میان‌بر.

## نگاشت داده

روی اسکیمای `HumanResource` (SQL Server). پیشوند اسکیما در همه‌جا لازم است.

| دامنه | جدول مرجع |
|---|---|
| هویت کارمند | `Personel` + `Global.Afrad` (نام اینجا نیست) |
| جایگاه سازمانی | `PersonelHokmPostVahedSazmani` → `Post` / `VahedSazmani` |
| قرارداد | `PersonelGharardad` + `NoeEstekhdam` |
| حقوق مصوب | `PersonelHokmHoghogh` + `...Satr` + `ItemHoghogh` |
| حقوق پرداختی | `PardakhtHoghogh` + `...Satr` |
| کارکرد | `PersonelKarkard` + `...Satr`، `VorodKhorojPersonel` |
| مرخصی | `PersonelMorakhasi`، `PersonelMandehMorakhasi` |
| مأموریت | `PersonelMamoriat` **یا** `PersonelMamuryat` |
| مالیات | `PersonelMaliat` + `...Satr`، `Maliat` |
| بیمه | `ListBime` + `ListBimeSatr`، `PersonelSabeghehBimeh` |
| وام و رفاه | `DarkhastAzSandoghRefah` → `DarkhastVam` → `SandoghRefah` |
| درمان | `DarkhastHazinehDarman` |
| ارزیابی | `ArzyabiPersonel` + `FormArzyabi` |
| تسویه | `TasviehHesab` + `...Satr`، `BazKharid` |
| تقویم | `Global.Taghvim` (`CodeNoeTatili IS NULL` = روز کاری) |

## هفت تله که وقت زیادی می‌گیرند اگر از قبل ندانی

- **جدول‌های دوقلو با یک حرف فرق.** `ShiftKari`/`ShiftKary` و
  `PersonelMamoriat`/`PersonelMamuryat` دو جهانِ جدا با دو دسته مشتریِ جدا
  هستند. اشتباه گرفتنشان **خطا نمی‌دهد، جدولِ خالی می‌دهد.**
- **`XSatr` همیشه زیرِ `X` نیست.** `DarkhastVamSatr` و
  `DarkhastHazineDarmanSatr` هر دو زیرِ `DarkhastAzSandoghRefah` هستند.
  ستونی به اسم `DarkhastVamSatr.ccDarkhastVam` **وجود ندارد**.
- **بودنِ ردیف یعنی ثبت شده، نه معتبر.** `CodeVazeiat` باید فیلتر شود و
  کدهایش **بین جدول‌ها یکسان نیستند** — هر دامنه `X_CodeVazeiat` خودش را دارد.
- **`PardakhtHoghogh` دو نمایش دارد:** ستون‌های پهنِ مبلغ و
  `PardakhtHoghoghSatr`. جمعِ هر دو دوباره‌شماری است.
- **ستون شروع همیشه `FromDate` نیست** — شش جدول `BeginDate` دارند، و
  `PersonelGharardad.EndDate` تهی‌پذیر **نیست** (الگوی `EndDate IS NULL` آنجا
  کار نمی‌کند).
- **ستون‌های مرده در جدول‌های زنده.** `PardakhtHoghogh` هشت ستون مرده دارد
  (هفت‌تا با پسوند `_deeeel`) که کنارِ ستون‌های زنده‌ی هم‌معنی نشسته‌اند.
- **ناسازگاری نوع.** `PardakhtHoghogh.ccPardakhtHoghogh` از نوع `bigint` است
  ولی تقریباً همه‌ی فرزندانش `int`، و
  `Zakhireh_ItemHoghogh.ccItemHoghogh` از نوع `tinyint` است — سقف ۲۵۵.

`python scripts/map.py traps` همه را یک‌جا می‌دهد.

## پل به اسکیل‌های فروش

`Personel.ccAfrad` و `Sales.AmarForosh_Arshive.ccAfradForoshandeh` **هر دو به
`Global.Afrad` می‌روند** — یعنی پرونده‌ی پرسنلی به عملکرد فروش وصل می‌شود.
کوئری ۸ `queries.md` این را می‌سازد.

**این فرض تأیید نشده.** از دو سندِ مستقل درآمده، نه از یک کوئری. اول با یک
`COUNT` ببین چند سطر مشترک درمی‌آید.

## ایمپورت

در بخش Skills، «افزودن از URL» و آدرس این پوشه در گیت‌هاب:

```
https://github.com/<owner>/<repo>/tree/main/منابع-انسانی-پگاه
```

کل پوشه با هم می‌آید. چون اسکریپت اجرایی دارد، اسکیل **خاموش** ایمپورت می‌شود؛
بعد از اینکه یک نفر `scripts/map.py` را خواند، روشنش کنید. تغییرات این
فایل‌ها تا ایمپورت دوباره به محصول نمی‌رسد.

## اجرای مستقیم

```bash
python scripts/map.py table  PersonelHokmHoghogh
python scripts/map.py refs   Personel
python scripts/map.py path   DarkhastVam PardakhtHoghogh --avoid Personel
python scripts/map.py find   Morakhasi
python scripts/map.py domain hoghogh
python scripts/map.py external
python scripts/map.py crossref ccMarkazForosh
python scripts/map.py traps  ShiftKari
```

پایتون ۳.۹ به بالا، بدون هیچ وابستگی بیرونی.

> `path` مسیرِ **ساختاری** می‌دهد نه معنایی. چون `Personel` مرکز ثقل است،
> کوتاه‌ترین مسیر معمولاً از آن رد می‌شود و ممکن است بُعدی را که سؤال به آن
> نیاز دارد (مثل واحد سازمانی) دور بزند. `--avoid Personel` را امتحان کن.

## به‌روزرسانی نقشه

همه‌ی دانشِ ساختاری در `schema.json` است — جدول، دامنه، کلید، ستون‌های `cc`،
پرچم‌ها و تله‌ها. اسکریپت را برای اضافه کردن جدول یا اتصال دست نزنید.

اتصال‌ها **در فایل ذخیره نشده‌اند**؛ از قاعده‌ی `A.ccB → B` ساخته می‌شوند. پس
اضافه کردن یک `cc` به فهرست `cc` یک جدول، خودبه‌خود یال را می‌سازد.

وقتی چیزی روی دیتابیس زنده تأیید شد:

۱. `verified_against_live_db` را در `meta` عوض کنید.
۲. برای اتصالی که کلید خارجی واقعی دارد، در یادداشتِ جدول بنویسید تأیید شده.
۳. `version` را عوض کنید تا معلوم باشد گزارش‌های قبلی با کدام نقشه درآمده‌اند.
۴. جدول «اندازه‌ها» در انتهای `queries.md` را با عددهای واقعی پر کنید.

## تصمیم‌هایی که در نقشه کدگذاری شده

- **`ccElatOdat` بیرونی شمرده نشده.** با ۳۷ تکرار شبیه موجودیت مشترک است، ولی
  هر دامنه جدولِ علتِ خودش را دارد و کدها منتقل نمی‌شوند.
- **`ccAfradModir` به `Global.Afrad` می‌رود، نه `Personel`.** سلسله‌مراتب
  مدیریتی از مسیر `Afrad` ساخته می‌شود.
- **`EnteghalAvalieh_*` داده‌ی جاری نیست.** چهارده جدول مهاجرت که با
  `ShomarehPersonely` کلید می‌خورند؛ جمعشان با داده‌ی جاری دوباره‌شماری است.
- **پیش‌فرض مرزِ بازه:** `FromDate <= @AsOfDate AND (EndDate IS NULL OR EndDate
  > @AsOfDate)` — یعنی `EndDate` استثنا. برای هر ماژول تأیید بگیرید.
- **`_Old` خودکار مرده فرض نشده.**
  `AfzayeshHoghoghSalianeh.ccPersonelHokmHoghogh_Old` یعنی «حکم قبلی» و زنده
  است، ولی `Post.ccShoghl_Old` مرده.

## آنچه هنوز باید با کارشناس منابع انسانی پگاه چک شود

- **کدام جهانِ دوقلو زنده است** — `ShiftKari` یا `ShiftKary`،
  `PersonelMamoriat` یا `PersonelMamuryat`، و مسیر مستقیم درمان یا مسیرِ زیرِ
  صندوق رفاه. `COUNT` و `MAX(تاریخ)` می‌گویند کدام پرکارتر است، نه کدام مرجع.
- **`Sal`/`Mah` شمسی است یا میلادی** در `PardakhtHoghogh`، `PersonelMaliat` و
  `PersonelKarkard`.
- **جهت `BedBes`** در `PersonelMandehMorakhasi` و `SandoghRefah` — علامتِ
  اشتباه یعنی طلبکار را بدهکار نشان دادن.
- **ستون پهن یا سطرِ اقلام** در `PardakhtHoghogh` کدام مرجع است (کوئری ۵.۲).
- **`MablaghPersonelOLD` در `SandoghRefah`** کنارِ `Mablagh_SahmPersonel` — کدام
  زنده است.

## پیوند با بقیه‌ی اسکیل‌ها

۲۸ مقصدِ `cc` بیرونِ `HumanResource` و **۲۳ تای آنها در `Global`** — این
اسکیما تقریباً فقط با واژگانِ مشترک حرف می‌زند.

| مقصد | اسکیل | برای چه |
|---|---|---|
| `Global` (۲۳ جدول) | `تسلط-مشترک-پگاه` | **نام کارمند** (`Afrad`)، مرکز، تقویم، بانک |
| `Treasury` (۱) | `تسلط-خزانه-پگاه` | `EjazehPardakhtFaktor` — مجوزِ خروجِ پول |
| `Sales` (۱) | `تسلط-فروش-پگاه` | فاکتور |

**«چقدر باید بگیرد» و «چقدر گرفت» اینجاست، ولی «کِی و با چه مجوزی پرداخت
شد» در `Treasury` است.**

نقشه حالا ۴۳۳ یالِ داخلی و ۱۱۱ ارجاعِ بیرونی دارد (قبلاً یال ذخیره‌شده
نداشت و ۱۹ ارجاع ثبت شده بود). ۳۵ ارجاع نامزدِ نقش‌دار گرفتند و ۴۹ تا
واقعاً بی‌مقصد ماندند.

نقشه‌ی کامل خانواده، ماتریسِ ارجاع و فهرستِ ارجاع‌های حل‌نشده در
[../SKILLS.md](../SKILLS.md). عددها را `crosslink.py` می‌سازد؛ دستی
به‌روزشان نکن.
