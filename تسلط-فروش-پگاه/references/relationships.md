# اتصال‌ها، واژگان مشترک، و تله‌ها

```
اگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB
```

**هیچ‌کدام اثبات‌شده نیست** — این اسکیما کلید خارجی ندارد.

## مرکزهای ثقل

| موجودیت | ارجاع ورودی | نقش |
|---|---:|---|
| `Foroshandeh` | 127 | فروشنده — ولی کلیدش **مسیر** است نه آدم. |
| `Moshtary` | 113 | مشتری — لنگرگاه دامنه‌ی مشتری. |
| `GorohForosh` | 62 | — |
| `DarkhastFaktor` | 45 | سربرگ سفارش/فاکتور. |
| `MoshtarySazmanForosh` | 32 | — |
| `Masir` | 24 | مسیر فروش. |
| `NoeMashin` | 12 | — |
| `Mashin` | 9 | — |
| `ElatAdamFaalMoshtary` | 9 | — |
| `DarkhastHavaleh` | 8 | — |
| `NoeForoshandeh` | 7 | نوع فروشنده — فیلترِ حیاتیِ هر رتبه‌بندی. |
| `MoshtaryTaghirat` | 7 | — |
| `MasirRoozVisit` | 6 | — |
| `NoeMalekiatMoshtary` | 6 | — |
| `TafkikJoze` | 5 | — |

## ارجاع‌های بیرونی

| `cc` | تکرار | تفسیر |
|---|---:|---|
| `ccMarkazForosh` | 124 | مرکز فروش — در هیچ اسکیما جدول هم‌نام ندارد؛ مقصدش را پیدا کن |
| `ccKalaCode` | 68 | ✔ `Warehouse.Kala`  — کد کالا — کلیدِ کالا در آمار فروش. مقصدش هم‌نام نیست؛ Warehouse را ببین |
| `ccMarkazPakhsh` | 62 | ✔ `Global.MarkazPakhsh` |
| `ccMantaghehForosh` | 61 | ✔ `Global.MantaghehForosh`  — منطقه فروش |
| `ccUser` | 57 | کاربر — دامنه‌ی امنیت، بیرون از این دیتابیس |
| `ccHouzehForosh` | 40 | ✔ `Global.HouzehForosh`  — حوزه فروش |
| `ccNoeMoshtary` | 40 | نوع مشتری — نامش از Global.Goroh با ccGorohLink = 304 می‌آید (خرده، عمده، زنجیره‌ای، ...) |
| `ccAfradForoshandeh` | 37 | **شخصِ فروشنده** → Global.Afrad (FName، LName). با ccForoshandeh که مسیر است اشتباه نشود. |
| `ccTaminKonandeh` | 36 | ✔ `Purchase.TaminKonandeh` |
| `ccNoeVahedForosh` | 32 | ✔ `Global.NoeVahedForosh`  — نوع واحد فروش |
| `ccUserSabegheh` | 32 | کاربرِ سابقه — دامنه‌ی امنیت |
| `ccBrand` | 30 | ✔ `Amargar.Brand` |
| `ccSazmanForosh` | 29 | ✔ `Global.SazmanForosh`  — لاین فروش → Global.SazmanForosh (۱ لاین یک، ۲ نوشيدني، ۳ لاین دو، ۴ مشتريان ويژه) |
| `ccMarkazSazmanForosh` | 27 | ✔ `Global.MarkazSazmanForosh` |
| `ccAfrad` | 27 | ✔ `Global.Afrad` |
| `ccNoeSenf` | 25 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMantaghehPakhsh` | 24 | ✔ `Global.MantaghehPakhsh` |
| `ccGorohKala` | 21 | گروه کالا — نامش از Global.Goroh با ccGorohLink = 560 (۵۵ گروه). vGorohMahsol را نگیر. |
| `ccGoroh` | 20 | ✔ `Global.Goroh` |
| `ccHouzeh` | 18 | ✔ `Global.Houzeh` |
| `ccMarkazAnbar` | 16 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccKala` | 15 | ✔ `Amargar.Kala` |
| `ccShahr` | 15 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccReport` | 14 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccDarajeh` | 14 | ✔ `Global.Darajeh` |
| `ccAfradModirMantagheh` | 13 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMantagheh` | 12 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkaz` | 12 | ✔ `Global.Markaz` |
| `ccMahaleh` | 12 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazSazmanForoshSakhtarForosh` | 11 | ✔ `Global.MarkazSazmanForoshSakhtarForosh` |
| `ccAfradGoroh` | 11 | ✔ `Global.AfradGoroh` |
| `ccPhoto` | 10 | ✔ `Global.Photo` |
| `ccAfradGorohForosh` | 10 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccElatOdat` | 9 | ✔ `Global.ElatOdat` |
| `ccElat` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazPakhshAsli` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradRaees` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccShahrestan` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccKalaCodeAsli` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccNoeField` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |

✔ یعنی جدولِ هم‌نام در آن اسکیما **وجود دارد**. مقصد قطعی
است؛ خوردنِ ستون‌ها هنوز آزمونِ یتیم می‌خواهد.

## تله‌ها

`python scripts/map.py traps` همه را می‌دهد. خلاصه:

- دوقلو: **2** جفت
- سطرِ با پدرِ غیرمنتظره: **1**
- ناسازگاری نوع: **11**
- عرضِ ناسازگار: **20**
- جدول با ستون مرده: **0**

## فهرست کامل اتصال‌ها

| مبدأ | ستون | مقصد |
|---|---|---|
| `AdamDarkhast` | `ccAdamDarkhastPPC` | `AdamDarkhastPPC` |
| `AdamDarkhast` | `ccForoshandeh` | `Foroshandeh` |
| `AdamDarkhast` | `ccMoshtary` | `Moshtary` |
| `AdamDarkhastPPC` | `ccAdamDarkhast` | `AdamDarkhast` |
| `AdamDarkhastPPC` | `ccElatAdamDarkhast` | `ElatAdamDarkhast` |
| `AdamDarkhastPPC` | `ccForoshandeh` | `Foroshandeh` |
| `AdamDarkhastPPC` | `ccGorohForosh` | `GorohForosh` |
| `AdamDarkhastPPC` | `ccMoshtary` | `Moshtary` |
| `AdamDarkhastSatr` | `ccAdamDarkhast` | `AdamDarkhast` |
| `AdamDarkhastSatr` | `ccElatAdamDarkhast` | `ElatAdamDarkhast` |
| `AmalKardMorajehBeMoshtary` | `ccMoshtary` | `Moshtary` |
| `AmalkardForoshandeh` | `ccAdamDarkhast` | `AdamDarkhast` |
| `AmalkardForoshandeh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `AmalkardForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `AmalkardForoshandeh` | `ccMoshtary` | `Moshtary` |
| `AmalkardHaftegiTeamForosh_Archive` | `ccForoshandeh` | `Foroshandeh` |
| `AmalkardHaftegiTeamForosh_Archive` | `ccGorohForosh` | `GorohForosh` |
| `AmalkardRozanehForosh` | `ccForoshandeh` | `Foroshandeh` |
| `AmalkardRozanehReisForosh_Archive` | `ccForoshandeh` | `Foroshandeh` |
| `AmalkardRozanehReisForosh_Archive` | `ccGorohForosh` | `GorohForosh` |
| `AmalkardRozanehReisForosh_ListMoshtary_Archive` | `ccForoshandeh` | `Foroshandeh` |
| `AmalkardRozanehReisForosh_ListMoshtary_Archive` | `ccGorohForosh` | `GorohForosh` |
| `AmalkardRozanehReisForosh_ListMoshtary_Archive` | `ccMasir` | `Masir` |
| `AmalkardRozanehReisForosh_ListMoshtary_Archive` | `ccMoshtary` | `Moshtary` |
| `AmarForosh_Arshive` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `AmarForosh_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `AmarForosh_Arshive` | `ccGorohForosh` | `GorohForosh` |
| `AmarForosh_Arshive` | `ccMoshtary` | `Moshtary` |
| `AmarForosh_Arshive` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `AmarForosh_Arshive` | `ccSarGorohForosh` | `SarGorohForosh` |
| `AmarMoghayesehForosh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `AmarMoghayesehForosh_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `AmarMoghayesehForosh_Arshiv` | `ccMoshtary` | `Moshtary` |
| `AmarMoghayesehForosh_ArshivMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `AmarMoghayesehForosh_ArshivMoshtary` | `ccGorohForosh` | `GorohForosh` |
| `AmarMoghayesehForosh_ArshivMoshtary` | `ccMoshtary` | `Moshtary` |
| `AmarMoghayesehForosh_WithMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `AmarMoghayesehForosh_WithMoshtary` | `ccGorohForosh` | `GorohForosh` |
| `AmarMoghayesehForosh_WithMoshtary` | `ccMoshtary` | `Moshtary` |
| `AmarTatbighiForosh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `AmarTatbighiForosh_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `AmarTatbighiForosh_Arshiv` | `ccMoshtary` | `Moshtary` |
| `AmarTatbighiForosh_Kala_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `AmarTatbighiForosh_Kala_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `AmarTatbighiForosh_Kala_Arshiv` | `ccMoshtary` | `Moshtary` |
| `AnbarGardaniMashin` | `ccMashin` | `Mashin` |
| `AnbarGardaniMashinKala` | `ccAnbarGardaniMashin` | `AnbarGardaniMashin` |
| `AnbarGardaniMashinKala` | `ccMashin` | `Mashin` |
| `AnbarMoshtary` | `ccMoshtary` | `Moshtary` |
| `ArshiveMandehdar` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `ArshiveMandehdar` | `ccFaktorKhadamat` | `FaktorKhadamat` |
| `Arzyabi3MaheForoshandeh_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `Arzyabi3MaheForoshandeh_Arshive` | `ccGorohForosh` | `GorohForosh` |
| `ArzyabiRoozanehForoshandeh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `BarkhordForoshandehBaMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `BarkhordForoshandehBaMoshtary` | `ccMoshtary` | `Moshtary` |
| `ConfigShakhesAmarForoshErsalBetaminKonandeh` | `ccShakhes` | `Shakhes` |
| `Config_Foroshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `Config_NoeMoshtaryNoeVosolSatr` | `ccConfig_NoeMoshtaryNoeVosol` | `Config_NoeMoshtaryNoeVosol` |
| `DarkhastFaktor` | `ccDarkhastFaktorNoeForosh` | `DarkhastFaktorNoeForosh` |
| `DarkhastFaktor` | `ccDarkhastFaktorPPC` | `DarkhastFaktorPPC` |
| `DarkhastFaktor` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `DarkhastFaktor` | `ccForoshandeh` | `Foroshandeh` |
| `DarkhastFaktor` | `ccGorohForosh` | `GorohForosh` |
| `DarkhastFaktor` | `ccMoshtary` | `Moshtary` |
| `DarkhastFaktor` | `ccMoshtaryKerayeHaml` | `MoshtaryKerayeHaml` |
| `DarkhastFaktor` | `ccNoeMashin` | `NoeMashin` |
| `DarkhastFaktor` | `ccZamanTahvil` | `ZamanTahvil` |
| `DarkhastFaktorAfradForosh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorArshive` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorPPC` | `ccForoshandeh` | `Foroshandeh` |
| `DarkhastFaktorPPC` | `ccGorohForosh` | `GorohForosh` |
| `DarkhastFaktorPPC` | `ccMoshtary` | `Moshtary` |
| `DarkhastFaktorPPC` | `ccNoeMashin` | `NoeMashin` |
| `DarkhastFaktorSatr` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorSatr` | `ccDarkhastFaktorSatrPPC` | `DarkhastFaktorSatrPPC` |
| `DarkhastFaktorSatr` | `ccTafkikJoze` | `TafkikJoze` |
| `DarkhastFaktorSatrPPC` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorSatrPPC` | `ccDarkhastFaktorPPC` | `DarkhastFaktorPPC` |
| `DarkhastFaktorSatrPPC` | `ccDarkhastFaktorSatr` | `DarkhastFaktorSatr` |
| `DarkhastFaktorSatrPPC` | `ccTafkikJoze` | `TafkikJoze` |
| `DarkhastFaktorSatrTakhfif` | `ccDarkhastFaktorSatr` | `DarkhastFaktorSatr` |
| `DarkhastFaktorSatrTakhfifPPC` | `ccDarkhastFaktorSatr` | `DarkhastFaktorSatr` |
| `DarkhastFaktorSatrTakhfifPPC` | `ccDarkhastFaktorSatrTakhfif` | `DarkhastFaktorSatrTakhfif` |
| `DarkhastFaktorSatrTakhfifPPC` | `ccDarkhastHavalehSatr` | `DarkhastHavalehSatr` |
| `DarkhastFaktorSatr_ElatOdat` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorSatr_ElatOdat` | `ccDarkhastFaktorSatr` | `DarkhastFaktorSatr` |
| `DarkhastFaktorSatr_Saderat` | `ccDarkhastFaktorSatr` | `DarkhastFaktorSatr` |
| `DarkhastFaktorTakhfif` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorTakhfifDorei_Archive` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorTakhfifDorei_Archive` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `DarkhastFaktorTakhfifDorei_Archive` | `ccNoeTakhfifDorei` | `NoeTakhfifDorei` |
| `DarkhastFaktorTakhfifDorei_Archive` | `ccTakhfifDorei` | `TakhfifDorei` |
| `DarkhastFaktorTakhfifPPC` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktorTakhfifPPC` | `ccDarkhastFaktorPPC` | `DarkhastFaktorPPC` |
| `DarkhastFaktorTakhfifPPC` | `ccDarkhastFaktorTakhfif` | `DarkhastFaktorTakhfif` |
| `DarkhastFaktorTakhfifPPC` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `DarkhastFaktorVazeiat` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_Afrad` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_AfradTaaVoni` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_Anbar` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_CodeVazeiat` | `ccDarkhastFaktorVazeiat` | `DarkhastFaktorVazeiat` |
| `DarkhastFaktor_EmzaMoshtary` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_EmzaMoshtary` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `DarkhastFaktor_EmzaMoshtary` | `ccMoshtary` | `Moshtary` |
| `DarkhastFaktor_MoshtaryGharardad` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_MoshtaryGharardad` | `ccMoshtaryGharardad` | `MoshtaryGharardad` |
| `DarkhastFaktor_Saderat` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_SodorFaktor_InsertVazeiat` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastFaktor_SodorFaktor_InsertVazeiat` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `DarkhastFaktor_TaxId` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastHavaleh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `DarkhastHavaleh` | `ccForoshandeh` | `Foroshandeh` |
| `DarkhastHavaleh` | `ccMoshtary` | `Moshtary` |
| `DarkhastHavaleh` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `DarkhastHavaleh` | `ccZamanTahvil` | `ZamanTahvil` |
| `DarkhastHavalehSatr` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `DarkhastHavalehSatr` | `ccTafkikJoze` | `TafkikJoze` |
| `DarkhastSaatSabt` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `ElamMarjoee` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `ElamMarjoee` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `ElamMarjoee` | `ccElamMarjoeePPC` | `ElamMarjoeePPC` |
| `ElamMarjoee` | `ccForoshandeh` | `Foroshandeh` |
| `ElamMarjoee` | `ccMoshtary` | `Moshtary` |
| `ElamMarjoeePPC` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `ElamMarjoeePPC` | `ccForoshandeh` | `Foroshandeh` |
| `ElamMarjoeePPC` | `ccMoshtary` | `Moshtary` |
| `ElamMarjoeeSatr` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `ElamMarjoeeSatr` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `ElamMarjoeeSatr` | `ccElamMarjoee` | `ElamMarjoee` |
| `ElamMarjoeeSatrPPC` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `ElamMarjoeeSatrPPC` | `ccElamMarjoeePPC` | `ElamMarjoeePPC` |
| `ElamMarjoeeSatrPPC_Tedad` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `ElatAdamDarkhast_NoeMoshtary` | `ccElatAdamDarkhast` | `ElatAdamDarkhast` |
| `ElatAdamDarkhast_NoeMoshtary` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `FaktorKhadamat` | `ccForoshandeh` | `Foroshandeh` |
| `FaktorKhadamat` | `ccMoshtary` | `Moshtary` |
| `FaktorKhadamatSatr` | `ccFaktorKhadamat` | `FaktorKhadamat` |
| `FaktorKhadamatSatr` | `ccKhadamat` | `Khadamat` |
| `FaktorKhadamatSatrTakhfif` | `ccFaktorKhadamatSatr` | `FaktorKhadamatSatr` |
| `FaktorKhadamatSatrTakhfif` | `ccFaktorKhadamatTakhfif` | `FaktorKhadamatTakhfif` |
| `FaktorKhadamatTakhfif` | `ccFaktorKhadamat` | `FaktorKhadamat` |
| `FaktorKhadamatVazeiat` | `ccFaktorKhadamat` | `FaktorKhadamat` |
| `FaktorTozieNashode_Arshiv` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `FaktorTozieNashode_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `FaktorTozieNashode_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `FaktorTozieNashode_Arshiv` | `ccMoshtary` | `Moshtary` |
| `FaktorZayeat` | `ccForoshandeh` | `Foroshandeh` |
| `FaktorZayeat` | `ccMoshtary` | `Moshtary` |
| `FaktorZayeatSatr` | `ccFaktorZayeat` | `FaktorZayeat` |
| `FaktorZayeatSatr` | `ccZayeat` | `Zayeat` |
| `FaktorZayeatSatrTakhfif` | `ccFaktorZayeatSatr` | `FaktorZayeatSatr` |
| `FaktorZayeatTakhfif` | `ccFaktorZayeat` | `FaktorZayeat` |
| `FaktorZayeatVazeiat` | `ccFaktorZayeat` | `FaktorZayeat` |
| `ForoshKharejAzMahal` | `ccForoshandeh` | `Foroshandeh` |
| `Forosh_Hadaf_WithMoshtary_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `Forosh_Hadaf_WithMoshtary_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `Forosh_Hadaf_WithMoshtary_Arshiv` | `ccMoshtary` | `Moshtary` |
| `Foroshandeh` | `ccDarkhastFaktorNoeForosh` | `DarkhastFaktorNoeForosh` |
| `Foroshandeh` | `ccGorohForosh` | `GorohForosh` |
| `Foroshandeh` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `ForoshandehAfrad` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehBeForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehControl` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehControl` | `ccNoeControlForosh` | `NoeControlForosh` |
| `ForoshandehEtebar` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehMarjoee_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehMorakhasy` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehMosavabehKalaSazmanForosh` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehMoshtary` | `ccMasir` | `Masir` |
| `ForoshandehMoshtary` | `ccMoshtary` | `Moshtary` |
| `ForoshandehMoshtary` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `ForoshandehMoshtary_DarkhastMoshtary_Archive` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehMoshtary_DarkhastMoshtary_Archive` | `ccForoshandeh_Asli` | `Foroshandeh` |
| `ForoshandehMoshtary_DarkhastMoshtary_Archive` | `ccMasir` | `Masir` |
| `ForoshandehMoshtary_DarkhastMoshtary_Archive` | `ccMoshtary` | `Moshtary` |
| `ForoshandehMoshtary_DarkhastMoshtary_Archive` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `ForoshandehSaatHozour` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehSahmiehKala` | `ccForoshandeh` | `Foroshandeh` |
| `ForoshandehTelephoni_ListMoshtaryRooz` | `ccForoshandeh_Asli` | `Foroshandeh` |
| `ForoshandehTelephoni_ListMoshtaryRooz` | `ccMasir` | `Masir` |
| `ForoshandehTelephoni_ListMoshtaryRooz` | `ccMoshtary` | `Moshtary` |
| `ForoshandehTelephoni_MoshtaryMasir` | `ccForoshandeh_Asli` | `Foroshandeh` |
| `ForoshandehTelephoni_MoshtaryMasir` | `ccMasir` | `Masir` |
| `ForoshandehTelephoni_MoshtaryMasir` | `ccMoshtary` | `Moshtary` |
| `Foroshandeh_DarkhastFaktorNoeForosh` | `ccDarkhastFaktorNoeForosh` | `DarkhastFaktorNoeForosh` |
| `Foroshandeh_DarkhastFaktorNoeForosh` | `ccForoshandeh` | `Foroshandeh` |
| `GorohForosh` | `ccSarGorohForosh` | `SarGorohForosh` |
| `GorohForoshAfrad` | `ccGorohForosh` | `GorohForosh` |
| `GorohNoeHazinehMashinSatr` | `ccGorohNoeHazinehmashin` | `GorohNoeHazinehMashin` |
| `GpsData_PPC` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `GpsData_PPC` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `GpsData_PPC` | `ccForoshandeh` | `Foroshandeh` |
| `GpsData_PPC` | `ccMasir` | `Masir` |
| `GpsData_PPC` | `ccMoshtary` | `Moshtary` |
| `HadafForosh` | `ccForoshandeh` | `Foroshandeh` |
| `HadafForosh` | `ccGorohForosh` | `GorohForosh` |
| `HadafForosh` | `ccMasir` | `Masir` |
| `HadafForoshRoozaneh` | `ccForoshandeh` | `Foroshandeh` |
| `HadafForoshRoozaneh` | `ccGorohForosh` | `GorohForosh` |
| `HadafForoshRoozanehNew` | `ccForoshandeh` | `Foroshandeh` |
| `HadafForoshRoozanehNew` | `ccGorohForosh` | `GorohForosh` |
| `HadafForoshRoozanehNew` | `ccMasir` | `Masir` |
| `HadafForoshRoozanehWithTatily` | `ccForoshandeh` | `Foroshandeh` |
| `HadafForoshRoozanehWithTatily` | `ccGorohForosh` | `GorohForosh` |
| `HadafForoshRoozanehWithTatily` | `ccHadafForoshRoozanehNew` | `HadafForoshRoozanehNew` |
| `HadafForoshRoozanehWithTatily` | `ccMasir` | `Masir` |
| `HadafForoshRoozaneh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `HadafForoshRoozaneh_Arshiv` | `ccMasir` | `Masir` |
| `HadafForoshandeh_PG` | `ccForoshandeh` | `Foroshandeh` |
| `HadafMoshtary_PG` | `ccMoshtary` | `Moshtary` |
| `Jameiat_MasouliatForosh_Tmp` | `ccMoshtary` | `Moshtary` |
| `JashnvarehForoshGoroh` | `ccJashnvarehForosh` | `JashnvarehForosh` |
| `JashnvarehForoshMarkaz` | `ccJashnvarehForosh` | `JashnvarehForosh` |
| `JashnvarehForoshSatr` | `ccJashnvarehForosh` | `JashnvarehForosh` |
| `JashnvarehForosh_Emtiaz` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `JashnvarehForosh_Emtiaz` | `ccJashnvarehForosh` | `JashnvarehForosh` |
| `JashnvarehForosh_Emtiaz` | `ccJashnvarehForoshSatr` | `JashnvarehForoshSatr` |
| `JashnvarehForosh_Emtiaz` | `ccMoshtary` | `Moshtary` |
| `Jayezeh` | `ccTakhfifHajmi` | `TakhfifHajmi` |
| `JayezehDelpazir` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForosh1400_3_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForosh1400_Arshive` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `JayezehForosh1400_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForosh1400_Arshive` | `ccMoshtary` | `Moshtary` |
| `JayezehForosh1400_Arshive` | `ccNoeMashin` | `NoeMashin` |
| `JayezehForoshEmtiazSarparast` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshNoeMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshNoeMoshtary` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshVijeh_Arshive98` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForosh_ArshiveReport97` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForosh_ArshiveReport97` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForosh_ArshiveReport98` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForosh_ArshiveReport98` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh1402` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh1402` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh1402_OLD` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh1402_OLD` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh1403` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh1403` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh1404` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh1404` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh14040321` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh14040321` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh96` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh96` | `ccGorohForosh` | `GorohForosh` |
| `JayezehForoshandeh97` | `ccForoshandeh` | `Foroshandeh` |
| `JayezehForoshandeh97` | `ccGorohForosh` | `GorohForosh` |
| `JayezehSatr` | `ccJayezeh` | `Jayezeh` |
| `JayezehSatrKala` | `ccJayezehSatr` | `JayezehSatr` |
| `JayezehTelephoni_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `KalaAdamForoshForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `KalaAdamForoshMarkazForosh` | `ccNoeAdamForosh` | `NoeAdamForosh` |
| `KalaAdamForoshMarkazSazmanForosh` | `ccNoeAdamForosh` | `NoeAdamForosh` |
| `KalaAdamForoshMarkazSazmanForoshSakhtarForosh` | `ccNoeAdamForosh` | `NoeAdamForosh` |
| `KalaAdamForoshSazmanForosh` | `ccNoeAdamForosh` | `NoeAdamForosh` |
| `KalaMojodyForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `KalaZaribForosh` | `ccNoeForoshandeh` | `NoeForoshandeh` |
| `Khadamat` | `ccNoeKhadamat` | `NoeKhadamat` |
| `KhadamatGheymat` | `ccKhadamat` | `Khadamat` |
| `MandehDarForoshVaMamoorPakhsh_Arshiv` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `MandehDarForoshVaMamoorPakhsh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `MandehDarForoshVaMamoorPakhsh_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `MandehDarForoshVaMamoorPakhsh_Arshiv` | `ccMoshtary` | `Moshtary` |
| `Mashin` | `ccMashinShomarehPelak` | `MashinShomarehPelak` |
| `Mashin` | `ccNoeMashin` | `NoeMashin` |
| `MashinHazineh` | `ccMashin` | `Mashin` |
| `MashinHazinehSatr` | `ccMashinHazineh` | `MashinHazineh` |
| `MashinHazinehSatr` | `ccMashinNoeHazinehSatr` | `MashinNoeHazinehSatr` |
| `MashinNoeHazinehSatr` | `ccMashinNoeHazineh` | `MashinNoeHazineh` |
| `MashinShomarehPelak` | `ccNoeMashin` | `NoeMashin` |
| `MashinSookht` | `ccMashin` | `Mashin` |
| `Mashin_Polygon_MahdodiatePakhsh` | `ccMahdodiatePakhsh` | `MahdodiatePakhsh` |
| `Masir` | `ccForoshandeh` | `Foroshandeh` |
| `Masir` | `ccMasirRoozVisit` | `MasirRoozVisit` |
| `Masir` | `ccNoeMashin` | `NoeMashin` |
| `MasirForoshandeh_Tedad` | `ccForoshandeh` | `Foroshandeh` |
| `MasirHamsanSatr` | `ccMasirHamsan` | `MasirHamsan` |
| `MasirRoozForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `MasirRoozForoshandeh` | `ccMasir` | `Masir` |
| `MasirRoozVisitForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `MasirRoozVisitForoshandeh` | `ccMasirRoozVisit` | `MasirRoozVisit` |
| `MasirRoozVisitMarkazForosh` | `ccMasirRoozVisit` | `MasirRoozVisit` |
| `MasirSatr` | `ccMasir` | `Masir` |
| `Masir_ErsalFaktor` | `ccForoshandeh` | `Foroshandeh` |
| `Masir_ErsalFaktor` | `ccMasir` | `Masir` |
| `Moavagh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Moavagh` | `ccForoshandeh` | `Foroshandeh` |
| `Moavagh` | `ccMoshtary` | `Moshtary` |
| `ModatVosolGoroh` | `ccModatVosol` | `ModatVosol` |
| `ModatVosolMarkazPakhsh` | `ccModatVosol` | `ModatVosol` |
| `ModatVosolSatr` | `ccModatVosol` | `ModatVosol` |
| `MojoodiGiri` | `ccForoshandeh` | `Foroshandeh` |
| `MojoodiGiri` | `ccMoshtary` | `Moshtary` |
| `MoshtarianBedonehPolygan` | `ccMoshtary` | `Moshtary` |
| `Moshtary` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `Moshtary` | `ccMoshtaryJadid` | `MoshtaryJadid` |
| `Moshtary` | `ccNoeMalekiatMoshtary` | `NoeMalekiatMoshtary` |
| `Moshtary14030626` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `Moshtary14030626` | `ccMoshtary` | `Moshtary` |
| `Moshtary14030626` | `ccMoshtaryJadid` | `MoshtaryJadid` |
| `Moshtary14030626` | `ccMoshtary_Link` | `Moshtary` |
| `Moshtary14030626` | `ccNoeMalekiatMoshtary` | `NoeMalekiatMoshtary` |
| `MoshtaryAdamForosh` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryAddress` | `ccMoshtary` | `Moshtary` |
| `MoshtaryAddress` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryAddress14030701` | `ccMoshtary` | `Moshtary` |
| `MoshtaryAddress14030701` | `ccMoshtaryAddress` | `MoshtaryAddress` |
| `MoshtaryAddress14030701` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryAddressSaatTahvil` | `ccMoshtaryAddress` | `MoshtaryAddress` |
| `MoshtaryAddress_Export_To_Tehran_West` | `ccMoshtary` | `Moshtary` |
| `MoshtaryAddress_Export_To_Tehran_West` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryAfrad` | `ccMoshtary` | `Moshtary` |
| `MoshtaryBrand` | `ccMoshtary` | `Moshtary` |
| `MoshtaryBrand` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryChidman` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `MoshtaryChidman` | `ccMasir` | `Masir` |
| `MoshtaryChidman` | `ccMoshtary` | `Moshtary` |
| `MoshtaryDaraee` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `MoshtaryDaraee` | `ccMoshtary` | `Moshtary` |
| `MoshtaryEtebar` | `ccMoshtary` | `Moshtary` |
| `MoshtaryEtebar` | `ccMoshtaryNoeEtebar` | `MoshtaryNoeEtebar` |
| `MoshtaryEtebar` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryEtebarKol` | `ccMoshtaryNoeEtebar` | `MoshtaryNoeEtebar` |
| `MoshtaryEtebarOLD` | `ccMoshtary` | `Moshtary` |
| `MoshtaryEtebarOLD` | `ccMoshtaryEtebar` | `MoshtaryEtebar` |
| `MoshtaryEtebarOLD` | `ccMoshtaryNoeEtebar` | `MoshtaryNoeEtebar` |
| `MoshtaryEtebarOLD` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryEtebarPishnahady` | `ccMoshtary` | `Moshtary` |
| `MoshtaryEtebarPishnahady` | `ccMoshtaryNoeEtebar` | `MoshtaryNoeEtebar` |
| `MoshtaryEtebarPishnahady` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryEtebarPishnahadyOLD` | `ccMoshtary` | `Moshtary` |
| `MoshtaryEtebarPishnahadyOLD` | `ccMoshtaryEtebarPishnahady` | `MoshtaryEtebarPishnahady` |
| `MoshtaryEtebarPishnahadyOLD` | `ccMoshtaryNoeEtebar` | `MoshtaryNoeEtebar` |
| `MoshtaryEtebarPishnahadyOLD` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryEtebarSazmanForosh` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryEtebarTarikhMohasebeh` | `ccMoshtary` | `Moshtary` |
| `MoshtaryGharardad` | `ccDarkhastFaktorNoeForosh` | `DarkhastFaktorNoeForosh` |
| `MoshtaryGharardad` | `ccMoshtary` | `Moshtary` |
| `MoshtaryGharardad` | `ccMoshtaryNoeGharardad` | `MoshtaryNoeGharardad` |
| `MoshtaryGharardad` | `ccMoshtaryNoeVosol` | `MoshtaryNoeVosol` |
| `MoshtaryGharardad` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryGharardad` | `ccNoeVisit` | `NoeVisit` |
| `MoshtaryGharardadPhoto` | `ccMoshtaryGharardad` | `MoshtaryGharardad` |
| `MoshtaryGharardadSatr` | `ccMoshtaryGharardad` | `MoshtaryGharardad` |
| `MoshtaryGharardadSatr` | `ccNoeTakhfifHazineh` | `NoeTakhfifHazineh` |
| `MoshtaryGharardadSazmanForosh` | `ccMoshtaryGharardad` | `MoshtaryGharardad` |
| `MoshtaryGoroh` | `ccMoshtary` | `Moshtary` |
| `MoshtaryGoroh` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryJadid` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtaryJadid` | `ccNoeMalekiatMoshtary` | `NoeMalekiatMoshtary` |
| `MoshtaryKerayeHaml` | `ccMoshtary` | `Moshtary` |
| `MoshtaryKerayeHaml` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryKharejAzMahal` | `ccMoshtary` | `Moshtary` |
| `MoshtaryMarkazForoshHistory` | `ccMoshtary` | `Moshtary` |
| `MoshtaryNoeEtebar` | `ccMoshtary` | `Moshtary` |
| `MoshtaryPhoto` | `ccMoshtary` | `Moshtary` |
| `MoshtaryPhoto` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryPhotoPPC` | `ccMoshtary` | `Moshtary` |
| `MoshtaryPhotoPPC` | `ccMoshtaryPhoto` | `MoshtaryPhoto` |
| `MoshtaryPosition` | `ccMoshtary` | `Moshtary` |
| `MoshtaryPosition` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryRotbeh` | `ccMoshtary` | `Moshtary` |
| `MoshtaryRotbeh` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtarySahmiehKala` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtarySaraneh` | `ccMoshtary` | `Moshtary` |
| `MoshtarySazmanForosh` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `MoshtarySazmanForosh` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtarySazmanForosh` | `ccMasir` | `Masir` |
| `MoshtarySazmanForosh` | `ccMoshtary` | `Moshtary` |
| `MoshtarySazmanForosh14030701` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `MoshtarySazmanForosh14030701` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtarySazmanForosh14030701` | `ccMasir` | `Masir` |
| `MoshtarySazmanForosh14030701` | `ccMoshtary` | `Moshtary` |
| `MoshtarySazmanForosh14030701` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtarySazmanForoshOLD` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `MoshtarySazmanForoshOLD` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtarySazmanForoshOLD` | `ccMasir` | `Masir` |
| `MoshtarySazmanForoshOLD` | `ccMoshtary` | `Moshtary` |
| `MoshtarySazmanForoshOLD` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtarySazmanForoshSaatTahvil` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtarySazmanForoshSaatTahvil` | `ccZamanTahvil` | `ZamanTahvil` |
| `MoshtarySazmanForosh_Export_To_Tehran_West` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `MoshtarySazmanForosh_Export_To_Tehran_West` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtarySazmanForosh_Export_To_Tehran_West` | `ccMasir` | `Masir` |
| `MoshtarySazmanForosh_Export_To_Tehran_West` | `ccMoshtary` | `Moshtary` |
| `MoshtaryShomarehHesab` | `ccMoshtary` | `Moshtary` |
| `MoshtaryShomarehHesab` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryShomarehHesab14030701` | `ccMoshtary` | `Moshtary` |
| `MoshtaryShomarehHesab14030701` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryShomarehHesab_Export_To_Tehran_West` | `ccMoshtary` | `Moshtary` |
| `MoshtaryShomarehHesab_Export_To_Tehran_West` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `MoshtaryShoraka` | `ccMoshtary` | `Moshtary` |
| `MoshtaryShoraka` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryTaghirat` | `ccMoshtary` | `Moshtary` |
| `MoshtaryTaghirat` | `ccMoshtary_Link` | `Moshtary` |
| `MoshtaryTaghirat` | `ccNoeMalekiatMoshtary` | `NoeMalekiatMoshtary` |
| `MoshtaryTaghiratAddress` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryTaghiratMadarek` | `ccMoshtary` | `Moshtary` |
| `MoshtaryTaghiratMadarek` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryTaghiratSazmanForosh` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtaryTaghiratSazmanForosh` | `ccMasirRoozVisit` | `MasirRoozVisit` |
| `MoshtaryTaghiratSazmanForosh` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryTaghiratShomarehHesab` | `ccMoshtary` | `Moshtary` |
| `MoshtaryTaghiratShomarehHesab` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryTaghiratShoraka` | `ccMoshtary` | `Moshtary` |
| `MoshtaryTaghiratShoraka` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryTaghiratVazeiat` | `ccMoshtaryTaghirat` | `MoshtaryTaghirat` |
| `MoshtaryYakhchal` | `ccMoshtary` | `Moshtary` |
| `MoshtaryYakhchal` | `ccYakhchal` | `Yakhchal` |
| `MoshtaryZemanat` | `ccMoshtary` | `Moshtary` |
| `MoshtaryZemanatPhoto` | `ccMoshtaryZemanat` | `MoshtaryZemanat` |
| `MoshtaryZemanat_Vaziat` | `ccMoshtaryZemanat` | `MoshtaryZemanat` |
| `MoshtaryfaalForoshandeh_Arshive` | `ccForoshandeh` | `Foroshandeh` |
| `MoshtaryfaalForoshandeh_Arshive` | `ccMoshtary` | `Moshtary` |
| `RotbehBandyMoshtary` | `ccNoeMashin` | `NoeMashin` |
| `SabeghehForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `SabeghehForoshandehMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `SabeghehForoshandehMoshtary` | `ccForoshandehMoshtary` | `ForoshandehMoshtary` |
| `SabeghehForoshandehMoshtary` | `ccMasir` | `Masir` |
| `SabeghehForoshandehMoshtary` | `ccMoshtary` | `Moshtary` |
| `SabeghehForoshandehMoshtary` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `SabeghehMoshtary` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `SabeghehMoshtary` | `ccMoshtary` | `Moshtary` |
| `SabeghehMoshtary` | `ccMoshtaryJadid` | `MoshtaryJadid` |
| `SabeghehMoshtary` | `ccMoshtary_Link` | `Moshtary` |
| `SabeghehMoshtary` | `ccNoeMalekiatMoshtary` | `NoeMalekiatMoshtary` |
| `SabeghehMoshtary1` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `SabeghehMoshtary1` | `ccMoshtary` | `Moshtary` |
| `SabeghehMoshtary1` | `ccMoshtaryJadid` | `MoshtaryJadid` |
| `SabeghehMoshtary1` | `ccMoshtary_Link` | `Moshtary` |
| `SabeghehMoshtary1` | `ccNoeMalekiatMoshtary` | `NoeMalekiatMoshtary` |
| `SabeghehMoshtaryAddress` | `ccMoshtary` | `Moshtary` |
| `SabeghehMoshtaryAddress` | `ccMoshtaryAddress` | `MoshtaryAddress` |
| `SabeghehMoshtaryAddress` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `SabeghehMoshtaryBrand` | `ccMoshtary` | `Moshtary` |
| `SabeghehMoshtaryBrand` | `ccMoshtaryBrand` | `MoshtaryBrand` |
| `SabeghehMoshtaryBrand` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `SabeghehMoshtaryGoroh` | `ccMoshtary` | `Moshtary` |
| `SabeghehMoshtaryGoroh` | `ccMoshtaryGoroh` | `MoshtaryGoroh` |
| `SabeghehMoshtaryGoroh` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `SabeghehMoshtaryShomarehHesab` | `ccMoshtary` | `Moshtary` |
| `SabeghehMoshtaryShomarehHesab` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `TafkikJoze` | `ccMashin` | `Mashin` |
| `TafkikJoze` | `ccNoeMashin` | `NoeMashin` |
| `TafkikJozeForoshAnbarak` | `ccMashin` | `Mashin` |
| `TafkikJozeForoshAnbarakSatr` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `TafkikJozeSatr` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `TafkikJozeSatr` | `ccDarkhastHavaleh` | `DarkhastHavaleh` |
| `TafkikJozeSatr` | `ccTafkikJoze` | `TafkikJoze` |
| `TafkikKolSatr` | `ccTafkikJoze` | `TafkikJoze` |
| `TafkikKolSatr` | `ccTafkikKol` | `TafkikKol` |
| `TakhfifDorei` | `ccMoshtary` | `Moshtary` |
| `TakhfifDorei` | `ccNoeTakhfifDorei` | `NoeTakhfifDorei` |
| `TakhfifHajmiQuery` | `ccTakhfifHajmi` | `TakhfifHajmi` |
| `TakhfifHajmiSatr` | `ccTakhfifHajmi` | `TakhfifHajmi` |
| `TakhfifHamlMostaghim` | `ccNoeMashin` | `NoeMashin` |
| `TakhfifHamlMostaghimSatr` | `ccTakhfifHamlMostaghim` | `TakhfifHamlMostaghim` |
| `TakhfifJayezeh` | `ccNoeMashin` | `NoeMashin` |
| `TakhfifJayezehAdam` | `ccTakhfifJayezeh` | `TakhfifJayezeh` |
| `TakhfifJayezehGoroh` | `ccTakhfifJayezeh` | `TakhfifJayezeh` |
| `TakhfifJayezehMarkaz` | `ccTakhfifJayezeh` | `TakhfifJayezeh` |
| `TakhfifJayezehMarkazPakhsh` | `ccTakhfifJayezeh` | `TakhfifJayezeh` |
| `TakhfifJayezehSatr` | `ccTakhfifJayezeh` | `TakhfifJayezeh` |
| `TakhfifSefareshSatr` | `ccTakhfifSefaresh` | `TakhfifSefaresh` |
| `TakhfifSenfi` | `ccMoshtaryGharardad` | `MoshtaryGharardad` |
| `TakhfifSenfiSatr` | `ccTakhfifSenfi` | `TakhfifSenfi` |
| `TakhfifSenfiVijehMoshtary` | `ccTakhfifSenfiVijeh` | `TakhfifSenfiVijeh` |
| `TakhfifSenfiVijehSatr` | `ccTakhfifSenfiVijeh` | `TakhfifSenfiVijeh` |
| `TakhfifSenfiVijehSatrKala` | `ccTakhfifSenfiVijehSatr` | `TakhfifSenfiVijehSatr` |
| `TasvieBaDahDarsadJayezeh_Vaziat` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `TedadMoshtarianBaZaribSenf` | `ccForoshandeh` | `Foroshandeh` |
| `TedadMoshtaryByRotbeh_Archive` | `ccForoshandeh` | `Foroshandeh` |
| `TmpMasirForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `TmpMasirForoshandeh` | `ccMasir` | `Masir` |
| `TmpMasirForoshandeh` | `ccMoshtary` | `Moshtary` |
| `Tmp_AmalkardForosh` | `ccMoshtary` | `Moshtary` |
| `Tmp_AmarForosh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Tmp_AmarForosh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarForosh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarForosh` | `ccMoshtary` | `Moshtary` |
| `Tmp_AmarForosh` | `ccSarGorohForosh` | `SarGorohForosh` |
| `Tmp_AmarForoshBarHasbVazn` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarForoshBarHasbVazn` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarForoshBarHasbVazn` | `ccTmp_AmarForosh` | `Tmp_AmarForosh` |
| `Tmp_AmarForoshRozanehMahsolat` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarForoshRozanehMahsolat` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarKharidMoshtary_SenfForoshandeh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Tmp_AmarKharidMoshtary_SenfForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarKharidMoshtary_SenfForoshandeh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarKharidMoshtary_SenfForoshandeh` | `ccMoshtary` | `Moshtary` |
| `Tmp_AmarMarjoeeForosh` | `ccElatMarjoee` | `ElatMarjoee` |
| `Tmp_AmarMarjoeeForosh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarMarjoeeForosh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarMarjoeeForosh` | `ccMoshtary` | `Moshtary` |
| `Tmp_AmarMoghayesehForosh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarMoghayesehForosh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarMoghayesehForosh` | `ccMoshtary` | `Moshtary` |
| `Tmp_AmarMoghayesehForoshBarHasbVazn` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarMoghayesehForoshBarHasbVazn` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_AmarMoghayesehForoshBarHasbVazn` | `cctmp_AmarMoghayesehForosh` | `Tmp_AmarMoghayesehForosh` |
| `Tmp_AmarMoghayesehMoshtarian` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_AmarMoghayesehMoshtarian` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_ArzyabiRoozanehForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_ArzyabiRoozanehForoshandeh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_DarajeBandiMoshtaryBrand` | `ccMoshtary` | `Moshtary` |
| `Tmp_DarsadPakhsh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_DarsadPakhsh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_FaktorToziNashodeh` | `ccMoshtary` | `Moshtary` |
| `Tmp_FindKalayeSeSetareyeHarMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_InsertError_DarkhastMoshtaryOnline` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Tmp_MamorPakhsh` | `ccMashin` | `Mashin` |
| `Tmp_MandehBoodjeh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_MizanForoshMahsoolat` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_MizanForoshMahsoolat` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_MoshtarianKharidNakardeh` | `ccElatAdamFaalMoshtary` | `ElatAdamFaalMoshtary` |
| `Tmp_MoshtarianKharidNakardeh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_MoshtarianKharidNakardeh` | `ccMasir` | `Masir` |
| `Tmp_MoshtarianKharidNakardeh` | `ccMasirRoozVisit` | `MasirRoozVisit` |
| `Tmp_MoshtarianKharidNakardeh` | `ccMoshtary` | `Moshtary` |
| `Tmp_Ranandeh` | `ccMashin` | `Mashin` |
| `Tmp_ReportJayezeh_Foroshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_ReportJayezeh_Foroshandeh` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_RotbeBandiMoshtarian` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_RotbeBandiMoshtarian` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_RotbeBandiMoshtarian` | `ccMoshtary` | `Moshtary` |
| `Tmp_RotbeBandiMoshtarianBeTafkikBrand` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_RotbeBandiMoshtarianBeTafkikBrand` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_RotbeBandiMoshtarianBeTafkikBrand` | `ccMasir` | `Masir` |
| `Tmp_RotbeBandiMoshtarianBeTafkikBrand` | `ccMasirRoozVisit` | `MasirRoozVisit` |
| `Tmp_RotbeBandiMoshtarianBeTafkikBrand` | `ccMoshtary` | `Moshtary` |
| `Tmp_RotbeBandiMoshtarian_Brand` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_RotbeBandiMoshtarian_Brand` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_RotbeBandiMoshtarian_Brand` | `ccMoshtary` | `Moshtary` |
| `Tmp_RotbeBandiMoshtarian_Brand` | `ccTmp_RotbeBandiMoshtarian` | `Tmp_RotbeBandiMoshtarian` |
| `Tmp_RotbeBandiMoshtary` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_RotbeBandiMoshtary` | `ccMoshtary` | `Moshtary` |
| `Tmp_RotbeBandiMoshtary` | `ccMoshtarySazmanForosh` | `MoshtarySazmanForosh` |
| `Tmp_SaranehForoshMarkaz` | `ccMoshtary` | `Moshtary` |
| `Tmp_SodourTafkikAuto` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Tmp_SodourTafkikAuto` | `ccMashin` | `Mashin` |
| `Tmp_SodourTafkikAuto` | `ccMoshtary` | `Moshtary` |
| `Tmp_SodourTafkikAuto` | `ccNoeMashin` | `NoeMashin` |
| `Tmp_TakhfifHajmi` | `ccTakhfifHajmi` | `TakhfifHajmi` |
| `Tmp_TakhfifHajmi` | `ccTakhfifHajmiSatr` | `TakhfifHajmiSatr` |
| `Tmp_TedadMoshtarianBaZaribSenf` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_TedadMoshtarianBaZaribSenf` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_TedadMoshtaryForKharidMoshtarian` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_TedadMoshtaryForKharidMoshtarian` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_TedadMoshtaryForKharidMoshtarian` | `ccMoshtary` | `Moshtary` |
| `Tmp_VazeiatDarkhastAuto` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Tmp_VazeiatDarkhastAuto` | `ccMoshtary` | `Moshtary` |
| `Tmp_VazeiatDarkhastAuto` | `ccNoeMashin` | `NoeMashin` |
| `Tmp_VazieatForoshande` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `Tmp_VazieatForoshande` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_VazieatForoshande` | `ccMasir` | `Masir` |
| `Tmp_VazieatForoshande` | `ccMoshtary` | `Moshtary` |
| `Tmp_VisitForoshandeh_GozareshRooz` | `ccForoshandeh` | `Foroshandeh` |
| `Tmp_VisitForoshandeh_GozareshRooz` | `ccGorohForosh` | `GorohForosh` |
| `Tmp_VisitForoshandeh_GozareshRooz` | `ccMoshtary` | `Moshtary` |
| `VisitForoshandeh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `VisitForoshandeh_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `VisitForoshandeh_Arshiv` | `ccMoshtary` | `Moshtary` |
| `ZakhirehYekDarHezarKaranehAutomatic` | `ccForoshandeh` | `Foroshandeh` |
| `rpt_AsibShenasiForosh_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `rpt_JayezehForosh_Sarparast_Arshiv` | `ccForoshandeh` | `Foroshandeh` |
| `rpt_JayezehForosh_Sarparast_Arshiv` | `ccGorohForosh` | `GorohForosh` |
| `tmpForoshJayezehKala` | `ccForoshandeh` | `Foroshandeh` |
| `tmpForoshJayezehKala` | `ccGorohForosh` | `GorohForosh` |
| `tmpForoshJayezehKala` | `ccMoshtary` | `Moshtary` |
| `tmpReportAmarForoshTaminKonandegan` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportAmarForoshTaminKonandegan` | `ccGorohForosh` | `GorohForosh` |
| `tmpReportAmarForoshTaminKonandegan` | `ccMoshtary` | `Moshtary` |
| `tmpReportEtebarMoshtary` | `ccMoshtary` | `Moshtary` |
| `tmpReportForoosh` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportForoosh` | `ccMoshtary` | `Moshtary` |
| `tmpReportHadaf` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportHadaf` | `ccGorohForosh` | `GorohForosh` |
| `tmpReportJaizehForosh` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportJaizehForosh` | `ccGorohForosh` | `GorohForosh` |
| `tmpReportJaizehForosh96` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportJaizehForosh96` | `ccGorohForosh` | `GorohForosh` |
| `tmpReportJaizehForosh97` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportJaizehForosh97` | `ccGorohForosh` | `GorohForosh` |
| `tmpReportJaizehForosh98` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportJaizehForosh98` | `ccGorohForosh` | `GorohForosh` |
| `tmpReportJaizehForoshDelpazir` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportRoozMojazForoshandeh` | `ccForoshandeh` | `Foroshandeh` |
| `tmpReportRoozMojazForoshandeh` | `ccGorohForosh` | `GorohForosh` |
| `tmp_DarkhastMoshtary_JayezehEntekhabi` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `tmp_DarkhastMoshtary_JayezehEntekhabi` | `ccJayezeh` | `Jayezeh` |
| `tmp_DarkhastMoshtary_JayezehEntekhabi` | `ccTakhfifHajmi` | `TakhfifHajmi` |
| `tmp_FaktorHayeTozieNashodeh` | `ccDarkhastFaktor` | `DarkhastFaktor` |
| `tmp_FaktorHayeTozieNashodeh` | `ccMoshtary` | `Moshtary` |
| `tmp_ForoshSherkatha` | `ccGorohForosh` | `GorohForosh` |
| `tmp_JayezehForosh_Froshandeh98New` | `ccForoshandeh` | `Foroshandeh` |
| `tmp_JayezehForosh_MoshtarianVijeh98New` | `ccForoshandeh` | `Foroshandeh` |
| `tmp_JayezehForosh_Sarparast98New` | `ccGorohForosh` | `GorohForosh` |
| `tmp_KharidMoshtary_ForHadaf` | `ccForoshandeh` | `Foroshandeh` |
| `tmp_KharidMoshtary_ForHadaf` | `ccMasir` | `Masir` |
| `tmp_KharidMoshtary_ForHadaf` | `ccMoshtary` | `Moshtary` |
| `tmp_ModatVosol` | `ccModatVosol` | `ModatVosol` |
