# موجودیت‌ها، دامنه به دامنه

برای هر دامنه: جدول مرجع، ستون‌های لازم، **دانه‌ی هر سطر**، و آنچه اسم جدول نمی‌گوید.

پیشوند اسکیما لازم است: `[Warehouse].[TableName]`.

<!-- TODO --> برای هر جدولِ مهم یک جمله نقش بنویس و دانه‌اش را مشخص کن.

---

## گزارش و جدول موقت — منبع حقیقت نیست

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `AmalkardRoozanehAnbar` | `ccAmalkardRoozanehAnbar` | None | rows_unknown | عملکرد روزانه انبار — نسخه‌ی «Roozaneh». |
| `AmalkardRozanehAnbar` | `ccAmalkardRozanehPakhsh` | None | rows_unknown | عملکرد روزانه انبار — نسخه‌ی «Rozaneh». |
| `AmalkardRozanehPakhsh96` | `ccAmalkardRozanehPakhsh` | None | year_snapshot، rows_unknown | — |
| `AmalkardRozanehPakhsh99` | `ccAmalkardRozanehPakhsh` | None | year_snapshot، rows_unknown | — |
| `TmpGroupKala` | `؟` | None | rows_unknown | — |
| `Tmp_AmarForoshTaminKonandeh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_EnteghalAnbar` | `ccTmp_EnteghalAnbar` | None | legacy، rows_unknown | — |
| `Tmp_EnteghalSefarsh` | `ccSefaresh` | None | legacy، rows_unknown | — |
| `Tmp_KasriAnbar` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_MojodyAnbar` | `ccRpt` | None | legacy، rows_unknown | — |
| `Tmp_MojodyKadBanoo_Namayandehgan` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_MojodyKadbanoo` | `ccTmp_MojodyKadbanoo` | None | legacy، rows_unknown | — |
| `Tmp_MojodyRialy_MaxMojoudy` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_PishBiniSefareshAnbar` | `ccTmp_PishBiniSefareshAnbar` | None | legacy، rows_unknown | — |
| `Tmp_RoozMojodyToziNashodeh` | `ccTmp_RoozMojodyToziNashodeh` | None | legacy، rows_unknown | — |
| `Tmp_ToziNashodehDoreh` | `؟` | None | legacy، rows_unknown | — |
| `hashemi` | `؟` | None | rows_unknown | — |
| `rptTaghiratKala` | `ccKalaCode` | None | rows_unknown | — |
| `tmpAmalkardRoozanehMamoorPakhshRanandeh` | `؟` | None | rows_unknown | — |
| `tmpAmalkardRoozanehMamoorPakhshRanandehFaktor` | `؟` | None | rows_unknown | — |
| `tmpReportJaizehMamorPakhsh` | `ccReport` | None | rows_unknown | — |
| `tmpReportJaizehMamorPakhsh96` | `ccReport` | None | year_snapshot، rows_unknown | — |
| `tmp_TajziehTahlilAnbar` | `؟` | None | legacy، rows_unknown | — |

---

## کاردکس — دفترِ گردش انبار

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Kardex` | `ccKardex` | None | status_header، hub_target، rows_unknown، anchor | سربرگِ گردش انبار — دفترِ مرکزیِ ورود و خروج کالا. |
| `KardexSatr` | `ccKardexSatr` | None | detail، status_header، rows_unknown | سطرِ گردش انبار — کالا، بچ، تعداد، قیمت. |
| `NoeKardex` | `ccNoeKardex` | None | dict، rows_unknown | نوع کاردکس. |
| `KardexAnbarak` | `ccKardexAnbarak` | None | status_header، rows_unknown | — |
| `KardexTolid` | `ccKardexTolid` | None | status_header، rows_unknown | — |
| `KardexAnbarakSatr` | `ccKardexAnbarakSatr` | None | detail، status_header، rows_unknown | — |
| `KardexTolidSatr` | `ccKardexTolidSatr` | None | detail، status_header، rows_unknown | — |
| `KardexVazeiat` | `ccKardexVazeiat` | None | status_header، dict، rows_unknown | — |
| `KardexPPC` | `ccMarkazPakhsh` | None | status_header، rows_unknown | — |
| `KardexPhoto` | `ccKardexPhoto` | None | rows_unknown | — |
| `KardexSatrGhesmat` | `ccKardexSatr` | None | rows_unknown | — |
| `KardexSatrGhesmatPPC` | `ccKardexSatr` | None | rows_unknown | — |
| `KardexSatrPPC` | `ccKardex` | None | rows_unknown | — |
| `KardexSatr_GheymatMiangin` | `؟` | None | rows_unknown | — |
| `KardexSharh` | `ccKardexSharh` | None | rows_unknown | — |
| `KardexTolidSatrGhesmat` | `ccKardexTolidSatrGhesmat` | None | rows_unknown | — |
| `KardexTolidSharh` | `ccKardexTolidSharh` | None | rows_unknown | — |
| `KardexVazeiatPPC` | `ccKardex` | None | status_header، rows_unknown | — |
| `NoeAmalyatKardex` | `؟` | None | dict، rows_unknown | — |
| `NoeFormKardex` | `؟` | None | dict، rows_unknown | — |

---

## کالا — تعریف، گروه، بچ، معادل

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Kala` | `ccKala` | None | effective_dated، status_header، tree، anchor، rows_unknown | کالا — جدول مرجعِ محصول با **دو شناسه**. |
| `Brand` | `ccBrand` | None | tree، rows_unknown | — |
| `GorohPakhsh` | `ccGorohPakhsh` | None | status_header، dict، rows_unknown | — |
| `DastehBandiNezaraty` | `ccDastehBandiNezaraty` | None | dict، rows_unknown | — |
| `NoeDastehBandiNezaraty` | `ccNoeDastehBandiNezaraty` | None | dict، rows_unknown | — |
| `Vahed` | `ccVahed` | None | dict، rows_unknown | — |
| `GorohPakhshMahal` | `ccGorohPakhsh` | None | dict، rows_unknown | — |
| `KalaAdamElat` | `ccKalaAdamElat` | None | rows_unknown | — |
| `KalaAdamMarjoee` | `ccKalaAdamMarjoee` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamSefaresh` | `ccKalaAdamSefaresh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAnbar` | `ccKalaAnbar` | None | rows_unknown | — |
| `KalaAnbarForoshandeh` | `ccKalaAnbarForoshandeh` | None | rows_unknown | — |
| `KalaAnbarGhesmat` | `ccKalaCode` | None | rows_unknown | — |
| `KalaAnbarMoshtary` | `ccKalaAnbarMoshtary` | None | rows_unknown | — |
| `KalaArzeshAfzodeh` | `ccKalaArzeshAfzodeh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAsli` | `ccKalaCodeAsli` | None | effective_dated، status_header، rows_unknown | — |
| `KalaBachAdamForosh` | `ccKalaBachAdamForosh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaBachAdamMarjoee` | `ccKalaBachAdamMarjoee` | None | effective_dated، status_header، rows_unknown | — |
| `KalaDastehBandiNezaraty` | `ccKalaDastehBandiNezaraty` | None | rows_unknown | — |
| `KalaGheymatKharid` | `ccKalaGheymatKharid` | None | effective_dated، status_header، rows_unknown | — |
| `KalaGheymatMasrafKonandeh` | `ccKalaGheymatMasrafKonandeh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaGoroh` | `ccKalaCode` | None | rows_unknown | — |
| `KalaHamsan` | `ccKalaHamsan` | None | effective_dated، rows_unknown | کالای همسان/معادل. |
| `KalaHamsanOld` | `ccKalaHamsanOld` | None | rows_unknown | کالای همسان — نسخه‌ی قدیمی. |
| `KalaModatEngheza` | `ccKalaModatEngheza` | None | effective_dated، status_header، rows_unknown | — |
| `KalaMosavabeh` | `ccKalaMosavabeh` | None | effective_dated، rows_unknown | — |
| `KalaPegahKadbanooProject` | `ccKalaPegahKadbanooProject` | None | effective_dated، rows_unknown | — |
| `KalaPhoto` | `ccKalaCode` | None | rows_unknown | — |
| `KalaSahmiehBandy` | `؟` | None | effective_dated، status_header، rows_unknown | — |
| `KalaShomarehBach` | `ccKalaCode` | None | rows_unknown | ثبتِ بچ — کالا × شماره بچ، با تاریخ تولید و انقضا. |
| `KalaTaminKonandeh` | `ccKalaCode` | None | status_header، rows_unknown | — |
| `KalaTolidKonandeh` | `ccKalaCode` | None | rows_unknown | — |
| `KalaVazeiat` | `ccKalaVazeiat` | None | status_header، dict، rows_unknown | — |
| `KalaZaribBazariaby` | `ccKalaZaribBazariaby` | None | effective_dated، status_header، rows_unknown | — |
| `KalaZaribSefareshAnbarShobeh` | `ccKalaZaribSefareshAnbarShobeh` | None | effective_dated، rows_unknown | — |
| `KalaZayeatTolid` | `ccKalaZayeatTolid` | None | effective_dated، status_header، rows_unknown | — |
| `Kala_14020830` | `ccKala` | None | year_snapshot، effective_dated، status_header، rows_unknown | عکسِ جدول کالا در تاریخ ۱۴۰۲/۰۸/۳۰. |
| `VahedTabdil` | `ccVahedAz` | None | dict، rows_unknown | — |

---

## انبار و انبارک

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Anbar` | `ccAnbar` | None | effective_dated، hub_target، rows_unknown، anchor | انبار — زیرِ یک مرکز پخش. |
| `AnbarGhesmat` | `ccAnbarGhesmat` | None | hub_target، rows_unknown | قسمتِ انبار — سطحِ ریزترِ مکان. |
| `Anbarak` | `ccAnbarak` | None | rows_unknown | انبارک — انبارِ سیار/فرعی (مثلاً روی ماشین فروش). |
| `AnbarSazmanSakhtar` | `ccAnbarSazmanSakhtar` | None | rows_unknown | — |
| `Anbar_Goroh` | `ccAnbar_Goroh` | None | dict، rows_unknown | — |
| `AnbarGardany` | `ccAnbarGardany` | None | status_header، rows_unknown | انبارگردانی — سربرگِ شمارشِ موجودی. |
| `AnbarGardanyForoshSayar` | `ccAnbarGardanyForoshSayar` | None | status_header، rows_unknown | — |
| `AnbarGardanyShomaresh` | `ccAnbarGardanyShomaresh` | None | status_header، rows_unknown | شمارشِ انبارگردانی |
| `Anbar_DamayeNegahdari` | `ccAnbar_DamayeNegahdari` | None | dict، rows_unknown | — |
| `Anbar_Noe` | `ccAnbar_Noe` | None | dict، rows_unknown | — |
| `Anbar_NoeEstefadeh` | `ccAnbar_NoeEstefadeh` | None | rows_unknown | — |
| `Anbar_NoeSakhteman` | `ccAnbar_NoeSakhteman` | None | dict، rows_unknown | — |
| `Anbar_Tajhizat` | `ccAnbar_Tajhizat` | None | dict، rows_unknown | — |
| `AnbarBeAnbar` | `ccAnbarBeAnbar` | None | rows_unknown | — |
| `AnbarGardanyForoshSayarShomareshKala` | `ccAnbarGardanyForoshSayarShomareshKala` | None | rows_unknown | — |
| `AnbarGardanyShomareshKala` | `ccAnbarGardanyShomareshKala` | None | rows_unknown | — |
| `AnbarMalzoomat_Kala` | `ccAnbarMalzoomat_Kala` | None | rows_unknown | — |
| `AnbarPermission` | `ccAnbarPermission` | None | rows_unknown | — |
| `Anbar_TajhizatJabeJaei` | `ccAnbar_TajhizatJabeJaei` | None | rows_unknown | — |
| `AnbarakAfrad` | `ccAnbarakAfrad` | None | effective_dated، rows_unknown | — |
| `Anbarak_Control` | `ccAnbarak` | None | rows_unknown | — |
| `HadafMarkazAnbar` | `ccHadafMarkazAnbar` | None | effective_dated، rows_unknown | — |
| `KaranehAnbar` | `ccKaranehAnbar` | None | rows_unknown | — |

---

## موجودی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `MojodyAnbarGharantineh` | `ccMojodyAnbarGharantineh` | None | rows_unknown | موجودی انبار قرنطینه |
| `MojodyAnbarZayeat` | `ccMojodyAnbarZayeat` | None | rows_unknown | موجودی انبار ضایعات |
| `MojodyForosh` | `ccMojodyForosh` | None | rows_unknown | موجودیِ قابل فروش — **عکسِ روزانه**، به تفکیک تاریخ × مرکز × کالا × قسمت × بچ. |
| `MojodyForoshAnbar` | `ccMojodyForoshAnbar` | None | rows_unknown | — |
| `MojodyForoshAnbarak` | `ccMojodyForoshAnbarak` | None | rows_unknown | — |
| `MojodyForosh_ArshiveJob` | `ccMojodyForosh_ArshiveJob` | None | rows_unknown | — |
| `MojodyMajazi` | `ccMojodyMajazi` | None | effective_dated، rows_unknown | موجودی مجازی |
| `MojodyMoshtary` | `ccMojodyMoshtary` | None | rows_unknown | — |
| `MojodySefaresh` | `ccMojodySefaresh` | None | rows_unknown | موجودیِ سفارش‌شده |

---

## سفارش و درخواست

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Sefaresh` | `ccSefaresh` | None | status_header، tree، rows_unknown | سفارشِ انبار — سربرگ. |
| `DarkhastMalzomat` | `ccDarkhastMalzomat` | None | status_header، rows_unknown | — |
| `ElatOdatMalzomat` | `ccElatOdatMalzomat` | None | reason_dict، dict، rows_unknown | — |
| `SefareshAnbarak` | `ccSefareshAnbarak` | None | status_header، rows_unknown | — |
| `DarkhastMalzomatSatr` | `ccDarkhastMalzomatSatr` | None | detail، status_header، rows_unknown | — |
| `MizanMasrafMalzomat` | `ccMizanMasrafMalzomat` | None | effective_dated، rows_unknown | — |
| `ModatMojazErsaleSefaresh` | `ccModatMojazErsaleSefaresh` | None | rows_unknown | — |
| `SabeghehSefareshKala` | `cctmpSefareshKala` | None | rows_unknown | — |
| `SabeghehSefareshMalzomatKala` | `ccSabeghehSefareshMalzomatKala` | None | rows_unknown | — |
| `SefareshAnbarakSatr` | `ccSefareshAnbarakSatr` | None | detail، rows_unknown | — |
| `SefareshAnbarakVazeiat` | `ccSefareshVazeiat` | None | status_header، dict، rows_unknown | — |
| `SefareshNoeBastehBandyKala` | `ccSefareshNoeBastehBandyKala` | None | status_header، rows_unknown | — |
| `SefareshNoeMashin` | `ccSefareshNoeMashin` | None | rows_unknown | — |
| `SefareshSatr` | `ccSefareshSatr` | None | detail، effective_dated، rows_unknown | سطر سفارش — کالا، تعداد، تأمین‌کننده، بچ. |
| `VazeiatSefaresh` | `ccVazeiatSefaresh` | None | status_header، rows_unknown | — |

---

## تفکیک، بارنامه و مأمور پخش

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `MamorPakhsh` | `ccMamorPakhsh` | None | effective_dated، status_header، rows_unknown | مأمور پخش |
| `BarNameh` | `ccBarNameh` | None | status_header، rows_unknown | بارنامه — حملِ کالا به مرکز/مشتری. |
| `NoeMamorPakhsh` | `ccNoeMamorPakhsh` | None | dict، rows_unknown | — |
| `TafkikJozeForoshSayar` | `ccTafkikJozeForoshSayar` | None | status_header، rows_unknown | — |
| `TafkikKolForoshSayar` | `ccTafkikKolForoshSayar` | None | rows_unknown | — |
| `TafkikKolMalzomat` | `ccTafkikKolMalzomat` | None | rows_unknown | — |
| `BarNamehSatr` | `ccBarnamehSatr` | None | detail، rows_unknown | — |
| `BarnamehPhoto` | `ccBarnamehPhoto` | None | rows_unknown | — |
| `MamorPakhshEtebar` | `ccMamorPakhshEtebar` | None | effective_dated، rows_unknown | — |
| `TafkikKolForoshSayarSatr` | `ccTafkikKolForoshSayar` | None | detail، rows_unknown | — |
| `TafkikKolMalzomatSatr` | `ccTafkikKolMalzomat` | None | detail، rows_unknown | — |

---

## قیمت و بهای تمام‌شده

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Config_GheymatTamamShodeh` | `ccConfig_GheymatTamamShodeh` | None | config، status_header، tree، rows_unknown | — |
| `Config_GheymatTamamShodeh_Standard` | `ccConfig_GheymatTamamShodeh_Standard` | None | config، status_header، rows_unknown | — |
| `Config_GheymatTamamShodeh_Hesab` | `ccConfig_GheymatTamamShodeh_Hesab` | None | config، status_header، rows_unknown | — |
| `Config_GheymatTamamShodeh_StandardSatr` | `ccConfig_GheymatTamamShodeh_StandardSatr` | None | config، detail، effective_dated، rows_unknown | — |
| `GheymatMianginKala` | `؟` | None | rows_unknown | قیمت میانگین کالا |
| `GheymatMianginKalaTaminKonandeh` | `؟` | None | rows_unknown | — |
| `GheymatMiangin_Arshiv` | `ccGheymatMiangin` | None | archive_check، rows_unknown | — |
| `VGheymatMianginKala` | `؟` | None | rows_unknown | — |

---

## مرجوعی و ضایعات

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `ElamMarjoeeZayeatAnbarak` | `ccElamMarjoeeZayeatAnbarak` | None | status_header، rows_unknown | — |
| `ElatMarjoeeKala` | `ccElatMarjoeeKala` | None | rows_unknown | علتِ مرجوعی کالا — و **مسئولیتِ آن**. |
| `MarjoeeKamel_Image` | `ccMarjooeeKamel_Image` | None | rows_unknown | — |
| `VazeiatMarjoeeFaktor` | `ccVazeiatMarjoeeFaktor` | None | status_header، rows_unknown | — |

---

## خرید و تأمین‌کننده

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `FaktorKharid` | `ccFaktorKharid` | None | status_header، rows_unknown | فاکتور خرید |
| `FaktorKharidSatr` | `ccFaktorKharidSatr` | None | detail، rows_unknown | — |
| `FaktorKharidSatrAnbar` | `ccFaktorKharidSatrAnbar` | None | rows_unknown | — |

---

## کنترل کیفی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `ControlKeyfi_Azmon` | `ccControlKeyfi_Azmon` | None | status_header، rows_unknown | — |
| `Config_ControlKeyfi` | `ccConfig_ControlKeyfi` | None | config، effective_dated، rows_unknown | — |
| `ControlKeyfi_AzmonSatr` | `ccControlKeyfi_AzmonSatr` | None | detail، rows_unknown | — |

---

## SDPMS

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `NoeSanadSdpms` | `ccNoeSanadSdpms` | None | dict، rows_unknown | — |
| `Sdpms` | `ccSdpms` | None | effective_dated، rows_unknown، end_date_not_null | — |
| `SdpmsLog` | `ccSdpmsLog` | None | rows_unknown | — |
| `SdpmsSatr` | `ccSdpmsSatr` | None | detail، sensitive، rows_unknown | — |

---

## پیکربندی و مرجع

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `NoeAnbarak` | `ccNoeAnbarak` | None | dict، rows_unknown | — |
| `NoeSefaresh` | `ccNoeSefaresh` | None | dict، rows_unknown | — |
| `Config_Anbar` | `ccConfig_Anbar` | None | config، rows_unknown | — |
| `Config_CodingKala` | `ccConfig_CodingKala` | None | config، effective_dated، rows_unknown | — |
| `Config_GorohKala` | `ccConfig_GorohKala` | None | config، effective_dated، rows_unknown | — |
| `Config_TajziehTahlilAnbar` | `ccConfig_TajziehTahlilAnbar` | None | config، rows_unknown | — |
| `Config_Varedeh` | `ccConfig_Varedeh` | None | config، rows_unknown | — |
| `SystemConfig` | `؟` | None | rows_unknown | — |

---

## دسته‌بندی‌نشده — دستی ببین

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `JaizehMamorPakhsh96_ArshiveReport98` | `ccJaizehMamorPakhsh96_ArshiveReport98` | None | year_snapshot، rows_unknown | — |

