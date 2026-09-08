# اتصال‌ها، واژگان مشترک، و تله‌ها

```
اگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB
```

**هیچ‌کدام اثبات‌شده نیست** — این اسکیما کلید خارجی ندارد.

## مرکزهای ثقل

| موجودیت | ارجاع ورودی | نقش |
|---|---:|---|
| `Anbar` | 17 | انبار — زیرِ یک مرکز پخش. |
| `Kardex` | 12 | سربرگِ گردش انبار — دفترِ مرکزیِ ورود و خروج کالا. |
| `AnbarGhesmat` | 10 | قسمتِ انبار — سطحِ ریزترِ مکان. |
| `Kala` | 10 | کالا — جدول مرجعِ محصول با **دو شناسه**. |
| `KardexSatr` | 7 | سطرِ گردش انبار — کالا، بچ، تعداد، قیمت. |
| `Anbarak` | 6 | انبارک — انبارِ سیار/فرعی (مثلاً روی ماشین فروش). |
| `GorohPakhsh` | 5 | — |
| `Brand` | 5 | — |
| `NoeKardex` | 4 | نوع کاردکس. |
| `MamorPakhsh` | 3 | مأمور پخش |
| `AnbarSazmanSakhtar` | 3 | — |
| `Sefaresh` | 3 | سفارشِ انبار — سربرگ. |
| `Anbar_Goroh` | 2 | — |
| `BarNameh` | 2 | بارنامه — حملِ کالا به مرکز/مشتری. |
| `Config_GheymatTamamShodeh` | 2 | — |

## ارجاع‌های بیرونی

| `cc` | تکرار | تفسیر |
|---|---:|---|
| `ccMarkazAnbar` | 37 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccTaminKonandeh` | 31 | ✔ `Purchase.TaminKonandeh` |
| `ccMarkazPakhsh` | 27 | ✔ `Global.MarkazPakhsh` |
| `ccUser` | 16 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMoshtary` | 12 | ✔ `Sales.Moshtary` |
| `ccAfrad` | 11 | ✔ `Global.Afrad` |
| `ccForoshandeh` | 11 | ✔ `Sales.Foroshandeh` |
| `ccDarkhastFaktor` | 10 | ✔ `Sales.DarkhastFaktor` |
| `ccUserSabegheh` | 10 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccElat` | 10 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazForosh` | 7 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccTafkikJoze` | 6 | ✔ `Sales.TafkikJoze` |
| `ccAfradMamorPakhsh` | 5 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccNoeMashin` | 5 | ✔ `Sales.NoeMashin` |
| `ccRefrence` | 5 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccGoroh` | 5 | ✔ `Global.Goroh` |
| `ccMantaghehAnbarPakhsh` | 5 | ✔ `Global.MantaghehAnbarPakhsh` |
| `ccAfradRanandeh` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradSabegheh` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccElatOdat` | 4 | ✔ `Global.ElatOdat` |
| `ccMantaghehPakhsh` | 4 | ✔ `Global.MantaghehPakhsh` |
| `ccAmalkardRozanehPakhsh` | 3 | ✔ `Sales.AmalkardRozanehPakhsh` |
| `ccAnbarBe` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccVahedSize` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccVahedVazn` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazSazmanForoshSakhtarForosh` | 3 | ✔ `Global.MarkazSazmanForoshSakhtarForosh` |
| `ccPhoto` | 3 | ✔ `Global.Photo` |
| `ccNoeSys` | 3 | ✔ `Global.NoeSys` |
| `ccAfradGoroh` | 3 | ✔ `Global.AfradGoroh` |
| `ccKalaCodeAsli` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazPakhshBe` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradMamurPakhsh` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazAnbarBe` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccElatMarjoee` | 3 | ✔ `Sales.ElatMarjoee` |
| `ccSystem` | 2 | ✔ `dbo.System` |
| `ccMarkazSazmanForosh` | 2 | ✔ `Global.MarkazSazmanForosh` |
| `ccGorohKala` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccKalaLink` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccVahedShomaresh` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccTaminkonandeh` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |

✔ یعنی جدولِ هم‌نام در آن اسکیما **وجود دارد**. مقصد قطعی
است؛ خوردنِ ستون‌ها هنوز آزمونِ یتیم می‌خواهد.

## تله‌ها

`python scripts/map.py traps` همه را می‌دهد. خلاصه:

- دوقلو: **1** جفت
- سطرِ با پدرِ غیرمنتظره: **1**
- ناسازگاری نوع: **0**
- عرضِ ناسازگار: **11**
- جدول با ستون مرده: **0**

## فهرست کامل اتصال‌ها

| مبدأ | ستون | مقصد |
|---|---|---|
| `Anbar` | `ccAnbar_DamayeNegahdari` | `Anbar_DamayeNegahdari` |
| `Anbar` | `ccAnbar_Goroh` | `Anbar_Goroh` |
| `Anbar` | `ccAnbar_Noe` | `Anbar_Noe` |
| `Anbar` | `ccAnbar_NoeEstefadeh` | `Anbar_NoeEstefadeh` |
| `Anbar` | `ccAnbar_NoeSakhteman` | `Anbar_NoeSakhteman` |
| `AnbarGardany` | `ccAnbar` | `Anbar` |
| `AnbarGardanyForoshSayar` | `ccAnbar` | `Anbar` |
| `AnbarGardanyForoshSayarShomareshKala` | `ccAnbarGardanyForoshSayar` | `AnbarGardanyForoshSayar` |
| `AnbarGardanyForoshSayarShomareshKala` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `AnbarGardanyShomaresh` | `ccAnbarGardany` | `AnbarGardany` |
| `AnbarGardanyShomareshKala` | `ccAnbarGardanyShomaresh` | `AnbarGardanyShomaresh` |
| `AnbarGardanyShomareshKala` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `AnbarGhesmat` | `ccAnbar` | `Anbar` |
| `AnbarPermission` | `ccAnbar` | `Anbar` |
| `AnbarSazmanSakhtar` | `ccAnbar` | `Anbar` |
| `Anbar_Noe` | `ccAnbar_Goroh` | `Anbar_Goroh` |
| `Anbar_TajhizatJabeJaei` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `Anbar_TajhizatJabeJaei` | `ccAnbar_Tajhizat` | `Anbar_Tajhizat` |
| `Anbarak` | `ccNoeAnbarak` | `NoeAnbarak` |
| `AnbarakAfrad` | `ccAnbarak` | `Anbarak` |
| `AnbarakAfrad` | `ccMamorPakhsh` | `MamorPakhsh` |
| `Anbarak_Control` | `ccAnbarak` | `Anbarak` |
| `BarNameh` | `ccKardex` | `Kardex` |
| `BarNamehSatr` | `ccBarnameh` | `BarNameh` |
| `BarNamehSatr` | `ccKardex` | `Kardex` |
| `BarnamehPhoto` | `ccBarnameh` | `BarNameh` |
| `Config_ControlKeyfi` | `ccNoeKardex` | `NoeKardex` |
| `Config_GheymatTamamShodeh_Hesab` | `ccConfig_GheymatTamamShodeh` | `Config_GheymatTamamShodeh` |
| `Config_GheymatTamamShodeh_StandardSatr` | `ccConfig_GheymatTamamShodeh` | `Config_GheymatTamamShodeh` |
| `Config_GheymatTamamShodeh_StandardSatr` | `ccConfig_GheymatTamamShodeh_Standard` | `Config_GheymatTamamShodeh_Standard` |
| `ControlKeyfi_Azmon` | `ccKardexSatr` | `KardexSatr` |
| `ControlKeyfi_AzmonSatr` | `ccControlKeyfi_Azmon` | `ControlKeyfi_Azmon` |
| `DarkhastMalzomat` | `ccAnbar` | `Anbar` |
| `DarkhastMalzomat` | `ccElatOdatMalzomat` | `ElatOdatMalzomat` |
| `DarkhastMalzomatSatr` | `ccDarkhastMalzomat` | `DarkhastMalzomat` |
| `DastehBandiNezaraty` | `ccNoeDastehBandiNezaraty` | `NoeDastehBandiNezaraty` |
| `ElamMarjoeeZayeatAnbarak` | `ccKardexAnbarak` | `KardexAnbarak` |
| `ElamMarjoeeZayeatAnbarak` | `ccKardexAnbarakSatr` | `KardexAnbarakSatr` |
| `FaktorKharidSatr` | `ccFaktorKharid` | `FaktorKharid` |
| `FaktorKharidSatrAnbar` | `ccFaktorKharidSatr` | `FaktorKharidSatr` |
| `FaktorKharidSatrAnbar` | `ccKardexSatr` | `KardexSatr` |
| `GheymatMianginKala` | `ccKardexSatr` | `KardexSatr` |
| `GorohPakhshMahal` | `ccGorohPakhsh` | `GorohPakhsh` |
| `JaizehMamorPakhsh96_ArshiveReport98` | `ccGorohPakhsh` | `GorohPakhsh` |
| `Kala` | `ccBrand` | `Brand` |
| `KalaAnbar` | `ccAnbar` | `Anbar` |
| `KalaAnbarGhesmat` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `KalaDastehBandiNezaraty` | `ccDastehBandiNezaraty` | `DastehBandiNezaraty` |
| `Kala_14020830` | `ccBrand` | `Brand` |
| `Kala_14020830` | `ccKala` | `Kala` |
| `KaranehAnbar` | `ccAmalkardRoozanehAnbar` | `AmalkardRoozanehAnbar` |
| `Kardex` | `ccAnbar` | `Anbar` |
| `Kardex` | `ccAnbarSazmanSakhtar` | `AnbarSazmanSakhtar` |
| `Kardex` | `ccNoeKardex` | `NoeKardex` |
| `KardexAnbarak` | `ccAnbar` | `Anbar` |
| `KardexAnbarak` | `ccAnbarSazmanSakhtar` | `AnbarSazmanSakhtar` |
| `KardexAnbarak` | `ccAnbarak` | `Anbarak` |
| `KardexAnbarak` | `ccMamorPakhsh` | `MamorPakhsh` |
| `KardexAnbarak` | `ccNoeKardex` | `NoeKardex` |
| `KardexAnbarakSatr` | `ccKardexAnbarak` | `KardexAnbarak` |
| `KardexPPC` | `ccAnbar` | `Anbar` |
| `KardexPPC` | `ccKardex` | `Kardex` |
| `KardexPhoto` | `ccKardex` | `Kardex` |
| `KardexSatr` | `ccKala` | `Kala` |
| `KardexSatr` | `ccKardex` | `Kardex` |
| `KardexSatrGhesmat` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `KardexSatrGhesmat` | `ccKardexSatr` | `KardexSatr` |
| `KardexSatrGhesmatPPC` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `KardexSatrGhesmatPPC` | `ccKardexSatr` | `KardexSatr` |
| `KardexSatrPPC` | `ccKala` | `Kala` |
| `KardexSatrPPC` | `ccKardex` | `Kardex` |
| `KardexSatrPPC` | `ccKardexSatr` | `KardexSatr` |
| `KardexSatr_GheymatMiangin` | `ccKardexSatr` | `KardexSatr` |
| `KardexSharh` | `ccKardex` | `Kardex` |
| `KardexTolid` | `ccAnbar` | `Anbar` |
| `KardexTolid` | `ccAnbarSazmanSakhtar` | `AnbarSazmanSakhtar` |
| `KardexTolid` | `ccKardex` | `Kardex` |
| `KardexTolid` | `ccNoeKardex` | `NoeKardex` |
| `KardexTolidSatr` | `ccKardexTolid` | `KardexTolid` |
| `KardexTolidSatrGhesmat` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `KardexTolidSatrGhesmat` | `ccKardexTolidSatr` | `KardexTolidSatr` |
| `KardexTolidSharh` | `ccKardexTolid` | `KardexTolid` |
| `KardexVazeiatPPC` | `ccKardex` | `Kardex` |
| `KardexVazeiatPPC` | `ccKardexVazeiat` | `KardexVazeiat` |
| `MamorPakhsh` | `ccGorohPakhsh` | `GorohPakhsh` |
| `MamorPakhsh` | `ccNoeMamorPakhsh` | `NoeMamorPakhsh` |
| `MamorPakhshEtebar` | `ccMamorPakhsh` | `MamorPakhsh` |
| `MarjoeeKamel_Image` | `ccKardex` | `Kardex` |
| `MojodyAnbarGharantineh` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `MojodyAnbarZayeat` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `MojodyForosh` | `ccAnbarGhesmat` | `AnbarGhesmat` |
| `MojodyForoshAnbar` | `ccAnbar` | `Anbar` |
| `MojodyForoshAnbarak` | `ccAnbar` | `Anbar` |
| `MojodyForoshAnbarak` | `ccAnbarak` | `Anbarak` |
| `MojodyForosh_ArshiveJob` | `ccAnbar` | `Anbar` |
| `MojodyForosh_ArshiveJob` | `ccAnbarak` | `Anbarak` |
| `MojodyMajazi` | `ccAnbar` | `Anbar` |
| `MojodyMoshtary` | `ccBrand` | `Brand` |
| `SabeghehSefareshKala` | `ccKala` | `Kala` |
| `SabeghehSefareshMalzomatKala` | `ccKala` | `Kala` |
| `Sdpms` | `ccNoeSanadSdpms` | `NoeSanadSdpms` |
| `SdpmsSatr` | `ccKardex` | `Kardex` |
| `SdpmsSatr` | `ccSdpms` | `Sdpms` |
| `SefareshAnbarak` | `ccAnbarak` | `Anbarak` |
| `SefareshAnbarak` | `ccNoeSefaresh` | `NoeSefaresh` |
| `SefareshAnbarakSatr` | `ccSefareshAnbarak` | `SefareshAnbarak` |
| `SefareshNoeMashin` | `ccBrand` | `Brand` |
| `SefareshSatr` | `ccKala` | `Kala` |
| `SefareshSatr` | `ccSefaresh` | `Sefaresh` |
| `TafkikJozeForoshSayar` | `ccKardex` | `Kardex` |
| `TafkikKolForoshSayarSatr` | `ccTafkikJozeForoshSayar` | `TafkikJozeForoshSayar` |
| `TafkikKolForoshSayarSatr` | `ccTafkikKolForoshSayar` | `TafkikKolForoshSayar` |
| `TafkikKolMalzomatSatr` | `ccDarkhastMalzomat` | `DarkhastMalzomat` |
| `TafkikKolMalzomatSatr` | `ccTafkikKolMalzomat` | `TafkikKolMalzomat` |
| `Tmp_EnteghalAnbar` | `ccKala` | `Kala` |
| `Tmp_EnteghalSefarsh` | `ccSefaresh` | `Sefaresh` |
| `Tmp_MojodyAnbar` | `ccKala` | `Kala` |
| `Tmp_PishBiniSefareshAnbar` | `ccBrand` | `Brand` |
| `VGheymatMianginKala` | `ccKala` | `Kala` |
| `VazeiatMarjoeeFaktor` | `ccAnbar` | `Anbar` |
| `VazeiatSefaresh` | `ccSefaresh` | `Sefaresh` |
| `hashemi` | `ccvahed` | `Vahed` |
| `tmpReportJaizehMamorPakhsh` | `ccGorohPakhsh` | `GorohPakhsh` |
| `tmpReportJaizehMamorPakhsh96` | `ccGorohPakhsh` | `GorohPakhsh` |
| `tmp_TajziehTahlilAnbar` | `ccAnbar` | `Anbar` |
| `tmp_TajziehTahlilAnbar` | `ccKala` | `Kala` |
