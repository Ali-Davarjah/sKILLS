# موجودیت‌ها، دامنه به دامنه

برای هر دامنه: جدول مرجع، ستون‌های لازم، **دانه‌ی هر سطر**، و آنچه اسم جدول نمی‌گوید.

پیشوند اسکیما لازم است: `[Sales].[TableName]`.

<!-- TODO --> برای هر جدولِ مهم یک جمله نقش بنویس و دانه‌اش را مشخص کن.

---

## گزارش و جدول موقت — منبع حقیقت نیست

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Tmp_AmarForosh` | `ccTmp_AmarForosh` | None | legacy، rows_unknown | — |
| `Tmp_AmarMoghayesehForosh` | `ccReport` | None | legacy، rows_unknown | — |
| `Tmp_RotbeBandiMoshtarian` | `ccTmp_RotbeBandiMoshtarian` | None | legacy، rows_unknown | — |
| `Jameiat_MasouliatForosh_Tmp` | `ccMasouliatForosh_Tmp` | None | rows_unknown | — |
| `TmpMasirForoshandeh` | `cctmpMasirForoshandeh` | None | rows_unknown | — |
| `Tmp_AmalkardForosh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_AmarForoshBarHasbVazn` | `ccTmp_AmarForosh` | None | legacy، rows_unknown | — |
| `Tmp_AmarForoshRozanehMahsolat` | `cctmp_AmarForoshRozanehMahsolat` | None | legacy، rows_unknown | — |
| `Tmp_AmarKharidMoshtary_SenfForoshandeh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_AmarMarjoeeForosh` | `ccAmarMarjoeeForosh` | None | legacy، rows_unknown | — |
| `Tmp_AmarMoghayesehForoshBarHasbVazn` | `cctmp_AmarMoghayesehForosh` | None | legacy، rows_unknown | — |
| `Tmp_AmarMoghayesehMoshtarian` | `ccReport` | None | legacy، rows_unknown | — |
| `Tmp_ArzyabiRoozanehForoshandeh` | `ccRow` | None | legacy، rows_unknown | — |
| `Tmp_DarajeBandiMoshtaryBrand` | `ccTmp_DarajeBandiMoshtaryBrand` | None | legacy، rows_unknown | — |
| `Tmp_DarajeBandiMoshtaryBrandZarib` | `ccTmp_DarajeBandiMoshtaryBrandZarib` | None | legacy، rows_unknown | — |
| `Tmp_DarsadPakhsh` | `ccTmp_DarsadPakhsh` | None | legacy، rows_unknown | — |
| `Tmp_DarsadTakhfifJadid` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_FaktorToziNashodeh` | `ccTmp_FaktorToziNashodeh` | None | legacy، status_header، rows_unknown | — |
| `Tmp_FindKalayeSeSetareyeHarMoshtary` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_InsertError_DarkhastMoshtaryOnline` | `ccTmp_Error` | None | legacy، rows_unknown | — |
| `Tmp_JayezehForoshModirMantagheh` | `ccRow` | None | legacy، rows_unknown | — |
| `Tmp_ListMoshtaryTekrari` | `ccTmpListMoshtaryTekrari` | None | legacy، sensitive، rows_unknown | — |
| `Tmp_MamorPakhsh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_MandehBoodjeh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_Mashin` | `ccTmp_Mashin` | None | legacy، rows_unknown | — |
| `Tmp_MizanForoshMahsoolat` | `ccRow` | None | legacy، rows_unknown | — |
| `Tmp_MoshtarianKharidNakardeh` | `؟` | None | legacy، status_header، rows_unknown | — |
| `Tmp_Ranandeh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_ReportJayezeh_Foroshandeh` | `ccReport` | None | legacy، rows_unknown | — |
| `Tmp_ReportJayezeh_RaeesAndModirMantagheh` | `ccReport` | None | legacy، rows_unknown | — |
| `Tmp_RotbeBandiMoshtarianBeTafkikBrand` | `ccRow` | None | legacy، status_header، sensitive، rows_unknown | — |
| `Tmp_RotbeBandiMoshtarian_Brand` | `ccTmp_RotbeBandiMoshtarian` | None | legacy، rows_unknown | — |
| `Tmp_RotbeBandiMoshtary` | `ccTmp_RotbeBandiMoshtary` | None | legacy، status_header، rows_unknown | — |
| `Tmp_SaranehForosh` | `ccSaranehForosh` | None | legacy، rows_unknown | — |
| `Tmp_SaranehForoshMarkaz` | `ccSaranehForoshMarkaz` | None | legacy، rows_unknown | — |
| `Tmp_SaranehOstan` | `ccTmp_JamiatSaraneForosh` | None | legacy، rows_unknown | — |
| `Tmp_SodourTafkikAuto` | `ccTmp_SodourTafkikAuto` | None | legacy، rows_unknown | — |
| `Tmp_TTMS_Forosh` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_TTMS_Kharid` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_TakhfifHajmi` | `ccTakhfifHajmiSatr` | None | legacy، rows_unknown | — |
| `Tmp_TedadMoshtarianBaZaribSenf` | `ccRow` | None | legacy، rows_unknown | — |
| `Tmp_TedadMoshtaryForKharidMoshtarian` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_VazeiatDarkhastAuto` | `ccDarkhastAuto` | None | legacy، rows_unknown | — |
| `Tmp_VazieatForoshande` | `ccVazietForoshandeh` | None | legacy، sensitive، rows_unknown | — |
| `Tmp_VisitForoshandeh_GozareshRooz` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_rptTakhfifHajmi` | `ccTmp_rptTakhfifHajmi` | None | legacy، rows_unknown | — |
| `rpt_AsibShenasiForosh_Arshiv` | `cc_AsibShenasiForosh` | None | archive_check، rows_unknown | — |
| `rpt_JayezehForosh_ModirMantagheh_Arshiv` | `ccJayezehModirMantagheh` | None | archive_check، rows_unknown | — |
| `rpt_JayezehForosh_RaeesMarkaz_Arshiv` | `ccJayezehRaeesMarkaz` | None | archive_check، rows_unknown | — |
| `rpt_JayezehForosh_Sarparast_Arshiv` | `ccJayezehSarparast` | None | archive_check، rows_unknown | — |
| `tmpBodjehYekDarHezar` | `؟` | None | rows_unknown | — |
| `tmpForoshJayezehKala` | `cctmpForoshJayezehKala` | None | rows_unknown | — |
| `tmpJobEtebarMoshtary` | `؟` | None | rows_unknown | — |
| `tmpReportAmarForoshTaminKonandegan` | `ccReport` | None | rows_unknown | — |
| `tmpReportEtebarMoshtary` | `ccEtebar` | None | rows_unknown | — |
| `tmpReportForoosh` | `ccRpt` | None | ledger، rows_unknown | — |
| `tmpReportHadaf` | `ccRpt` | None | rows_unknown | — |
| `tmpReportJaizehForosh` | `ccReport` | None | rows_unknown | — |
| `tmpReportJaizehForosh96` | `ccReport` | None | year_snapshot، rows_unknown | — |
| `tmpReportJaizehForosh97` | `ccReport` | None | year_snapshot، rows_unknown | — |
| `tmpReportJaizehForosh98` | `ccReport` | None | year_snapshot، rows_unknown | — |
| `tmpReportJaizehForoshDelpazir` | `ccReport` | None | rows_unknown | — |
| `tmpReportJaizehForoshEmtiaz` | `ccRpt` | None | rows_unknown | — |
| `tmpReportJaizehForoshKala` | `ccRpt` | None | rows_unknown | — |
| `tmpReportJaizehRaeesMarkazPakhsh` | `ccReport` | None | rows_unknown | — |
| `tmpReportRoozMojazForoshandeh` | `ccReport` | None | status_header، rows_unknown | — |
| `tmp_DarkhastMoshtary_JayezehEntekhabi` | `ccJayezehEntekhabi` | None | legacy، rows_unknown | — |
| `tmp_FaktorHayeTozieNashodeh` | `؟` | None | legacy، rows_unknown | — |
| `tmp_ForoshAzDastRafteh` | `cctmp_ForoshAzDastRafteh_Shahr` | None | legacy، rows_unknown | — |
| `tmp_ForoshSherkatha` | `؟` | None | legacy، rows_unknown | — |
| `tmp_Hadaf_ForoshTedadi_New` | `cctmp_Hadaf_ForoshTedadi_New` | None | legacy، effective_dated، rows_unknown | — |
| `tmp_JayezehForoshHoghogh` | `cctmp_JayezehForoshHoghogh` | None | legacy، rows_unknown | — |
| `tmp_JayezehForosh_Froshandeh98New` | `ccJayezehForosh_Froshandeh98New` | None | legacy، rows_unknown | — |
| `tmp_JayezehForosh_ModirMantagheh98New` | `ccJayezehForosh_ModirMantagheh98New` | None | legacy، rows_unknown | — |
| `tmp_JayezehForosh_MoshtarianVijeh98New` | `ccJayezehForosh_MoshtarianVijeh98New` | None | legacy، rows_unknown | — |
| `tmp_JayezehForosh_RaeesMarkaz98New` | `ccJayezehForosh_RaeesMarkaz98New` | None | legacy، rows_unknown | — |
| `tmp_JayezehForosh_Sarparast98New` | `ccJayezehForosh_Sarparast98New` | None | legacy، rows_unknown | — |
| `tmp_KharidMoshtary_ForHadaf` | `؟` | None | legacy، rows_unknown | — |
| `tmp_KholasehSakhtSefaresh_Shobeh` | `cctmp` | None | legacy، rows_unknown | — |
| `tmp_ModatVosol` | `؟` | None | legacy، rows_unknown | — |
| `tmp_MoghayeratForosh_HadafForoshandeh` | `؟` | None | legacy، rows_unknown | — |
| `tmp_SamanehTozie_Forosh` | `cctmp_SamanehTozie_Forosh` | None | legacy، sensitive، rows_unknown | — |

---

## فروش — سفارش، فاکتور، آمار

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `DarkhastFaktor` | `ccDarkhastFaktor` | None | status_header، anchor، rows_unknown | سربرگ سفارش/فاکتور. |
| `DarkhastHavaleh` | `ccDarkhastHavaleh` | None | status_header، rows_unknown | — |
| `DarkhastFaktorSatr` | `ccDarkhastFaktorSatr` | None | detail، status_header، rows_unknown | سطر فاکتور — COUNT(*) یعنی تعداد سطر. |
| `DarkhastFaktorNoeForosh` | `ccDarkhastFaktorNoeForosh` | None | dict، rows_unknown | — |
| `FaktorKhadamat` | `ccFaktorKhadamat` | None | status_header، rows_unknown | — |
| `ModatVosol` | `ccModatVosol` | None | effective_dated، rows_unknown | — |
| `AdamDarkhast` | `ccAdamDarkhast` | None | status_header، rows_unknown | — |
| `DarkhastFaktorPPC` | `ccDarkhastFaktorPPC` | None | status_header، rows_unknown | — |
| `FaktorZayeat` | `ccFaktorZayeat` | None | status_header، rows_unknown | — |
| `AdamDarkhastPPC` | `ccAdamDarkhast` | None | rows_unknown | — |
| `DarkhastFaktorSatrPPC` | `ccDarkhastFaktorSatrPPC` | None | status_header، rows_unknown | — |
| `DarkhastFaktorSatrTakhfif` | `ccDarkhastFaktorSatrTakhfif` | None | rows_unknown | — |
| `DarkhastFaktorTakhfif` | `ccDarkhastFaktorTakhfif` | None | rows_unknown | — |
| `DarkhastFaktorVazeiat` | `ccDarkhastFaktorVazeiat` | None | status_header، rows_unknown | — |
| `DarkhastHavalehSatr` | `ccDarkhastHavalehSatr` | None | detail، rows_unknown | — |
| `FaktorKhadamatSatr` | `ccFaktorKhadamatSatr` | None | detail، rows_unknown | — |
| `FaktorKhadamatTakhfif` | `ccFaktorKhadamatTakhfif` | None | rows_unknown | — |
| `FaktorZayeatSatr` | `ccFaktorZayeatSatr` | None | detail، rows_unknown | — |
| `AdamDarkhastSatr` | `ccAdamDarkhast` | None | detail، status_header، rows_unknown | — |
| `AmalKardMorajehBeMoshtary` | `ccAmalKardMorajehBeMoshtary` | None | status_header، rows_unknown | — |
| `AmalkardForoshandeh` | `ccAmalkardForoshandeh` | None | rows_unknown | — |
| `AmalkardHaftegiTeamForosh_Archive` | `ccAmalkard` | None | archive_check، rows_unknown | — |
| `AmalkardRozanehForosh` | `ccAmalkardRozanehForosh` | None | rows_unknown، legacy | عملکرد روزانه فروش. |
| `AmalkardRozanehPakhsh` | `ccAmalkardRozanehPakhsh` | None | rows_unknown | — |
| `AmalkardRozanehReisForosh_Archive` | `ccAmalkard` | None | archive_check، status_header، rows_unknown | — |
| `AmalkardRozanehReisForosh_ListMoshtary_Archive` | `ccAmalkard` | None | archive_check، status_header، rows_unknown | — |
| `AmarForosh_Arshive` | `ccAmarForosh_Arshive` | None | archive_check، rows_unknown، anchor، fact_table | جدول مرکزیِ فروش — یک سطر به ازای (تاریخ، فروشنده، مشتری، کالا، فاکتور). چهار معیار از شش معیارِ ارزیابی فروشنده از همین درمی‌آید. |
| `AmarMoghayesehForosh_Arshiv` | `ccAmarMoghayesehForosh_Arshiv` | None | archive_check، rows_unknown | — |
| `AmarMoghayesehForosh_ArshivMoshtary` | `ccAmarMoghayesehForosh_ArshivMoshtary` | None | rows_unknown | — |
| `AmarMoghayesehForosh_WithMoshtary` | `ccAmarMoghayesehForosh_WithMoshtary` | None | rows_unknown | — |
| `AmarTatbighiForosh_Arshiv` | `ccReport` | None | archive_check، rows_unknown | — |
| `AmarTatbighiForosh_Kala_Arshiv` | `ccReport` | None | archive_check، rows_unknown | — |
| `DarkhastConfig` | `ccDarkhastConfig` | None | effective_dated، rows_unknown | — |
| `DarkhastFaktorAfradForosh` | `ccDarkhastFaktorAfradForosh` | None | rows_unknown | — |
| `DarkhastFaktorArshive` | `ccDarkhastFaktorArshive` | None | rows_unknown | — |
| `DarkhastFaktorSatrTakhfifPPC` | `ccDarkhastFaktorSatr` | None | rows_unknown | — |
| `DarkhastFaktorSatr_ElatOdat` | `ccDarkhastFaktorSatr_ElatOdat` | None | reason_dict، rows_unknown | — |
| `DarkhastFaktorSatr_Saderat` | `ccDarkhastFaktorSatr_Saderat` | None | rows_unknown | — |
| `DarkhastFaktorTakhfifDorei_Archive` | `ccDarkhastFaktorTakhfifDorei_Archive` | None | archive_check، status_header، rows_unknown | — |
| `DarkhastFaktorTakhfifPPC` | `ccDarkhastFaktor` | None | rows_unknown | — |
| `DarkhastFaktor_Afrad` | `ccDarkhastFaktor_Afrad` | None | rows_unknown | — |
| `DarkhastFaktor_AfradTaaVoni` | `ccDarkhastFaktor_AfradTaavoni` | None | rows_unknown | — |
| `DarkhastFaktor_Anbar` | `ccDarkhastFaktor_Anbar` | None | rows_unknown | — |
| `DarkhastFaktor_CodeNoeVorod` | `ccDarkhastFaktor_CodeNoeVorod` | None | rows_unknown | — |
| `DarkhastFaktor_CodeVazeiat` | `ccDarkhastFaktorVazeiat` | None | status_dict، rows_unknown | — |
| `DarkhastFaktor_EmzaMoshtary` | `ccEmzaMoshtary` | None | rows_unknown | — |
| `DarkhastFaktor_MoshtaryGharardad` | `ccDarkhastFaktor_MoshtaryGharardad` | None | rows_unknown | — |
| `DarkhastFaktor_Saderat` | `ccDarkhastFaktor_Saderat` | None | rows_unknown | — |
| `DarkhastFaktor_SodorFaktor_InsertVazeiat` | `؟` | None | status_history، status_header، rows_unknown | — |
| `DarkhastFaktor_TaxId` | `ccDarkhastFaktor_TaxId` | None | rows_unknown | — |
| `DarkhastSaatSabt` | `ccDarkhastSaatSabt` | None | effective_dated، rows_unknown | — |
| `EtelaatForoshSherkatha` | `ccEtelaatForoshSherkatha` | None | rows_unknown | — |
| `FaktorKhadamatSatrTakhfif` | `ccFaktorKhadamatSatrTakhfif` | None | rows_unknown | — |
| `FaktorKhadamatVazeiat` | `ccFaktorKhadamatVazeiat` | None | status_history، status_header، rows_unknown | — |
| `FaktorTozieNashode_Arshiv` | `ccRow` | None | archive_check، rows_unknown | — |
| `FaktorZayeatSatrTakhfif` | `ccFaktorZayeatSatrTakhfif` | None | rows_unknown | — |
| `FaktorZayeatTakhfif` | `ccFaktorZayeatTakhfif` | None | rows_unknown | — |
| `FaktorZayeatVazeiat` | `ccFaktorZayeatVazeiat` | None | status_history، status_header، rows_unknown | — |
| `Forosh_Hadaf_WithMoshtary_Arshiv` | `ccHadafForoshRoozanehWithMoshtary` | None | archive_check، rows_unknown | — |
| `KholasehAmalkard` | `ccKholaseh` | None | rows_unknown | — |
| `MaxFaktorMandehDar` | `ccMaxFaktorMandehDar` | None | rows_unknown | — |
| `ModatVosolGoroh` | `ccModatVosolGoroh` | None | rows_unknown | — |
| `ModatVosolMarkazPakhsh` | `ccModatVosolMarkazPakhsh` | None | rows_unknown | — |
| `ModatVosolSatr` | `ccModatVosolSatr` | None | detail، rows_unknown | — |
| `SabeghehForoshandeh` | `ccSabeghehForoshandeh` | None | rows_unknown | — |
| `SabeghehForoshandehMoshtary` | `ccForoshandeh` | None | status_header، rows_unknown | — |
| `SabeghehMojodiShobeh` | `ccMojodi` | None | rows_unknown | — |
| `SabeghehMoshtary` | `ccMoshtary` | None | status_header، sensitive، rows_unknown | — |
| `SabeghehMoshtary1` | `ccMoshtary` | None | status_header، sensitive، rows_unknown | — |
| `SabeghehMoshtaryAddress` | `ccMoshtaryAddress` | None | status_header، rows_unknown | — |
| `SabeghehMoshtaryBrand` | `ccMoshtaryBrand` | None | rows_unknown | — |
| `SabeghehMoshtaryGoroh` | `؟` | None | rows_unknown | — |
| `SabeghehMoshtaryShomarehHesab` | `ccMoshtary` | None | sensitive، rows_unknown | — |

---

## مشتری — هویت، رتبه، اعتبار

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Moshtary` | `ccMoshtary` | None | status_header، sensitive، tree، anchor، rows_unknown | مشتری — لنگرگاه دامنه‌ی مشتری. |
| `MoshtarySazmanForosh` | `ccMoshtarySazmanForosh` | None | effective_dated، status_header، hub_target، rows_unknown | — |
| `MoshtaryTaghirat` | `ccMoshtaryTaghirat` | None | sensitive، rows_unknown | — |
| `MoshtaryGharardad` | `ccMoshtaryGharardad` | None | effective_dated، rows_unknown | — |
| `MoshtaryNoeEtebar` | `ccMoshtaryNoeEtebar` | None | effective_dated، rows_unknown | — |
| `MoshtaryJadid` | `ccMoshtaryJadid` | None | status_header، rows_unknown | — |
| `MoshtaryAddress` | `ccMoshtaryAddress` | None | status_header، rows_unknown | — |
| `MoshtaryZemanat` | `ccMoshtaryZemanat` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtaryBrand` | `ccMoshtaryBrand` | None | rows_unknown | — |
| `MoshtaryEtebar` | `ccMoshtaryEtebar` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtaryEtebarPishnahady` | `ccMoshtaryEtebarPishnahady` | None | effective_dated، tree، rows_unknown | — |
| `MoshtaryGoroh` | `ccMoshtaryGoroh` | None | rows_unknown | — |
| `MoshtaryKerayeHaml` | `ccMoshtaryKerayeHaml` | None | effective_dated، rows_unknown | — |
| `MoshtaryNoeGharardad` | `ccMoshtaryNoeGharardad` | None | dict، rows_unknown | — |
| `MoshtaryNoeVosol` | `ccMoshtaryNoeVosol` | None | dict، rows_unknown | — |
| `MoshtaryPhoto` | `ccMoshtary` | None | rows_unknown | — |
| `ArshiveMandehdar` | `ccArshiveMandehdar` | None | status_header، rows_unknown | — |
| `EtebarMojazAeenNameh` | `ccEMojaz` | None | effective_dated، status_header، rows_unknown | — |
| `MandehDarForoshVaMamoorPakhsh_Arshiv` | `ccRow` | None | archive_check، rows_unknown | — |
| `Moavagh` | `ccMoavagh` | None | effective_dated، rows_unknown، end_date_not_null | — |
| `MoshtarianBedonehPolygan` | `ccMoshtary` | None | rows_unknown | — |
| `Moshtary14030626` | `ccMoshtary` | None | status_header، sensitive، rows_unknown | — |
| `MoshtaryAdamForosh` | `ccMoshtaryAdamForosh` | None | effective_dated، rows_unknown | — |
| `MoshtaryAddress14030701` | `ccMoshtaryAddress` | None | status_header، rows_unknown | — |
| `MoshtaryAddressSaatTahvil` | `ccMoshtaryAddressSaatTahvil` | None | rows_unknown | — |
| `MoshtaryAddress_Export_To_Tehran_West` | `ccMoshtaryAddress_Export_To_Tehran_West` | None | status_header، rows_unknown | — |
| `MoshtaryAfrad` | `ccMoshtary` | None | rows_unknown | — |
| `MoshtaryChidman` | `ccMoshtaryChidman` | None | rows_unknown | — |
| `MoshtaryCodeVazeiat` | `ccMoshtaryCodeVazeiat` | None | status_dict، rows_unknown | — |
| `MoshtaryDaraee` | `ccMoshtaryDaraee` | None | sensitive، rows_unknown | — |
| `MoshtaryEtebarDarajeh` | `ccMoshtaryEtebarDarajeh` | None | effective_dated، rows_unknown | — |
| `MoshtaryEtebarKol` | `ccMoshtaryEtebarKol` | None | rows_unknown | — |
| `MoshtaryEtebarOLD` | `ccMoshtaryEtebar` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtaryEtebarPishFarz` | `ccMoshtaryEtebarPishFarz` | None | effective_dated، rows_unknown | — |
| `MoshtaryEtebarPishnahadyOLD` | `ccMoshtaryEtebarPishnahady` | None | effective_dated، rows_unknown | — |
| `MoshtaryEtebarSazmanForosh` | `ccMoshtaryEtebarSazmanForosh` | None | effective_dated، rows_unknown | — |
| `MoshtaryEtebarTarikhMohasebeh` | `؟` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtaryGharardadPhoto` | `ccMoshtaryGharardadPhoto` | None | rows_unknown | — |
| `MoshtaryGharardadSatr` | `ccMoshtaryGharardadSatr` | None | detail، rows_unknown | — |
| `MoshtaryGharardadSazmanForosh` | `ccMoshtaryGharardadSazmanForosh` | None | rows_unknown | — |
| `MoshtaryJadidDarkhastPPC` | `ccMoshtaryJadidDarkhastPPC` | None | rows_unknown | — |
| `MoshtaryKharejAzMahal` | `ccMoshtaryKharejAzMahal` | None | effective_dated، rows_unknown | — |
| `MoshtaryMarkazForoshHistory` | `ccMoshtaryMarkazForoshHistory` | None | legacy، effective_dated، rows_unknown | — |
| `MoshtaryPhotoPPC` | `ccMoshtaryPhoto` | None | rows_unknown | — |
| `MoshtaryPosition` | `ccMoshtary` | None | rows_unknown | — |
| `MoshtaryRotbeh` | `ccMoshtaryRotbeh` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtarySahmiehKala` | `ccMoshtarySahmiehKala` | None | effective_dated، rows_unknown | — |
| `MoshtarySaraneh` | `ccMoshtarySaraneh` | None | effective_dated، rows_unknown | — |
| `MoshtarySazmanForosh14030701` | `ccMoshtarySazmanForosh` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtarySazmanForoshOLD` | `ccMoshtarySazmanForosh` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtarySazmanForoshSaatTahvil` | `ccMoshtarySazmanForoshSaatTahvil` | None | rows_unknown | — |
| `MoshtarySazmanForosh_Export_To_Tehran_West` | `ccMoshtarySazmanForosh_Export_To_Tehran_West` | None | effective_dated، status_header، rows_unknown | — |
| `MoshtaryShomarehHesab` | `ccMoshtaryShomarehHesab` | None | status_header، rows_unknown | — |
| `MoshtaryShomarehHesab14030701` | `ccMoshtary` | None | status_header، rows_unknown | — |
| `MoshtaryShomarehHesab_Export_To_Tehran_West` | `ccMoshtaryShomarehHesab_Export_To_Tehran_West` | None | status_header، rows_unknown | — |
| `MoshtaryShoraka` | `ccMoshtaryShoraka` | None | sensitive، rows_unknown | — |
| `MoshtaryTaghiratAddress` | `ccMoshtaryTaghiratAddress` | None | status_header، rows_unknown | — |
| `MoshtaryTaghiratElatOdat` | `ccElatOdat` | None | reason_dict، rows_unknown | — |
| `MoshtaryTaghiratMadarek` | `ccMoshtaryTaghiratMadarek` | None | rows_unknown | — |
| `MoshtaryTaghiratSazmanForosh` | `ccMoshtaryTaghiratSazmanForosh` | None | status_header، rows_unknown | — |
| `MoshtaryTaghiratShomarehHesab` | `ccMoshtaryTaghiratShomareHesab` | None | status_header، sensitive، rows_unknown | — |
| `MoshtaryTaghiratShoraka` | `ccMoshtaryTaghiratShoraka` | None | sensitive، rows_unknown | — |
| `MoshtaryTaghiratVazeiat` | `ccMoshtaryTaghiratVazeiat` | None | status_history، status_header، rows_unknown | — |
| `MoshtaryYakhchal` | `ccMoshtaryYakhchal` | None | status_header، rows_unknown | — |
| `MoshtaryZemanatCodeVaziat` | `؟` | None | status_dict، rows_unknown | — |
| `MoshtaryZemanatPhoto` | `ccMoshtaryZemanat` | None | rows_unknown | — |
| `MoshtaryZemanat_Vaziat` | `ccMoshtaryZemanat_Vaziat` | None | status_header، rows_unknown | — |
| `MoshtaryfaalForoshandeh_Arshive` | `ccMoshtaryfaalForoshandeh_Arshive` | None | archive_check، rows_unknown | — |
| `NoeMoshtaryCheckBargashty` | `ccNoeMoshtaryCheckBargashty` | None | dict، rows_unknown | — |
| `NoeMoshtaryRialKharid` | `ccNoeMoshtaryRialKharid` | None | rows_unknown | — |
| `NoeMoshtaryZemanat` | `ccNoeZemanat` | None | dict، rows_unknown | — |
| `RotbehBandyMoshtary` | `ccRotbehBandyMoshtary` | None | effective_dated، rows_unknown | — |
| `TabaghehBandiRialKharidMoshtarian` | `؟` | None | rows_unknown | — |
| `TedadMoshtarianBaZaribSenf` | `ccTedadMoshtaryBaZaribSenf` | None | rows_unknown | — |
| `TedadMoshtaryByRotbeh_Archive` | `ccMoshtaryRotbehByBrand` | None | archive_check، rows_unknown | — |
| `Zemanat_CodeVaziat` | `؟` | None | status_dict، rows_unknown | — |

---

## فروشنده، مسیر، ویزیت و ارزیابی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Foroshandeh` | `ccForoshandeh` | None | status_header، anchor، rows_unknown | فروشنده — ولی کلیدش **مسیر** است نه آدم. |
| `Masir` | `ccMasir` | None | status_header، hub_target، rows_unknown | مسیر فروش. |
| `NoeForoshandeh` | `ccNoeForoshandeh` | None | dict، rows_unknown | نوع فروشنده — فیلترِ حیاتیِ هر رتبه‌بندی. |
| `MasirRoozVisit` | `ccMasirRoozVisit` | None | rows_unknown | — |
| `SarGorohForosh` | `ccSarGorohForosh` | None | status_header، rows_unknown | — |
| `ForoshandehMoshtary` | `ccForoshandehMoshtary` | None | status_header، rows_unknown | — |
| `MasirHamsan` | `ccMasirHamsan` | None | rows_unknown | — |
| `Arzyabi3MaheForoshandeh_Arshive` | `ccArzyabi3MaheForoshandeh_Arshive` | None | archive_check، rows_unknown | — |
| `ArzyabiForoshandeh_Emtiaz` | `ccEmtiaz` | None | effective_dated، rows_unknown | — |
| `ArzyabiRoozanehForoshandeh_Arshiv` | `ccArazyabi` | None | archive_check، rows_unknown | — |
| `BarkhordForoshandehBaMoshtary` | `ccBarkhordForoshandeh` | None | rows_unknown | — |
| `ForoshKharejAzMahal` | `ccForoshKharejAzMahal` | None | effective_dated، rows_unknown | — |
| `ForoshandehAfrad` | `ccForoshandehAfrad` | None | effective_dated، rows_unknown | — |
| `ForoshandehAmoozeshi_DeviceNumber` | `ccDeviceNumber` | None | sensitive، rows_unknown | — |
| `ForoshandehBeForoshandeh` | `ccForoshandehBeForoshandeh` | None | effective_dated، rows_unknown | — |
| `ForoshandehControl` | `ccForoshandehControl` | None | effective_dated، rows_unknown | — |
| `ForoshandehEtebar` | `ccForoshandehEtebar` | None | effective_dated، rows_unknown | — |
| `ForoshandehJaygozin` | `ccForoshandehJaygozin` | None | effective_dated، rows_unknown | — |
| `ForoshandehMarjoee_Arshive` | `ccForoshandehMarjoee_Arshive` | None | archive_check، rows_unknown | — |
| `ForoshandehMorakhasy` | `ccForoshandehMorakhasy` | None | effective_dated، status_header، rows_unknown، end_date_not_null | — |
| `ForoshandehMosavabehKalaSazmanForosh` | `ccForoshandehMosavabehKalaSazmanForosh` | None | rows_unknown | — |
| `ForoshandehMoshtary_DarkhastMoshtary_Archive` | `ccForoshandehMoshtary_Zanjiree_Archive` | None | archive_check، rows_unknown | — |
| `ForoshandehSaatHozour` | `ccForoshandehSaatHozour` | None | rows_unknown | — |
| `ForoshandehSahmiehKala` | `ccForoshandehSahmiehKala` | None | effective_dated، rows_unknown | — |
| `ForoshandehTelephoni_KalaOlaviat` | `؟` | None | rows_unknown | — |
| `ForoshandehTelephoni_ListMoshtaryRooz` | `ccForoshandehMoshtary_Telephoni` | None | rows_unknown | — |
| `ForoshandehTelephoni_MoshtaryMasir` | `ccMoshtary` | None | rows_unknown | — |
| `Foroshandeh_CodeVazeiat` | `ccForoshandeh_CodeVazeiat` | None | status_dict، rows_unknown | — |
| `Foroshandeh_DarkhastFaktorNoeForosh` | `ccForoshandeh_DarkhastFaktorNoeForosh` | None | rows_unknown | — |
| `GpsData_PPC` | `ccGpsData_PPC` | None | rows_unknown | — |
| `MasirForoshandeh_Tedad` | `ccTedadMasirForoshandeh` | None | rows_unknown | — |
| `MasirHamjavar` | `ccMasirHamjavar` | None | rows_unknown | — |
| `MasirHamsanSatr` | `ccMasirHamsanSatr` | None | detail، rows_unknown | — |
| `MasirRoozForoshandeh` | `ccMasirRoozForoshandeh` | None | rows_unknown | — |
| `MasirRoozVisitForoshandeh` | `ccMasirRoozVisitForoshandeh` | None | rows_unknown | — |
| `MasirRoozVisitMarkazForosh` | `؟` | None | rows_unknown | — |
| `MasirSatr` | `ccMasirSatr` | None | detail، rows_unknown | — |
| `MasirToorVisit` | `؟` | None | dict، rows_unknown | — |
| `Masir_ErsalFaktor` | `ccMasirErsalFaktor` | None | effective_dated، rows_unknown | — |
| `VisitForoshandeh_Arshiv` | `ccVisitForoshandeh` | None | archive_check، rows_unknown | رویدادِ ویزیت — مبنای درصد ویزیت مثبت. |

---

## مرجوعی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `ElamMarjoeePPC` | `ccElamMarjoeePPC` | None | status_header، rows_unknown | — |
| `ElamMarjoee` | `ccElamMarjoee` | None | status_header، rows_unknown | سربرگِ اعلامِ مرجوعی — تنها جایی که علتِ مرجوعی هست. |
| `ElatMarjoee` | `ccElatMarjoee` | None | dict، rows_unknown | — |
| `Zayeat` | `ccZayeat` | None | rows_unknown | — |
| `ElamMarjoeeSatr` | `ccElamMarjoeeSatr` | None | detail، rows_unknown | سطرِ مرجوعی: ccKalaCode، Tedad1، ccElatMarjoeeKala. |
| `ElamMarjoeeSatrPPC` | `ccElamMarjoeeSatrPPC` | None | rows_unknown | — |
| `ElamMarjoeeSatrPPC_Tedad` | `ccElamMarjoeeSatrPPC_Tedad` | None | rows_unknown | — |

---

## هدف و بودجه

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `HadafForoshRoozanehNew` | `ccHadafForoshRoozanehNew` | None | rows_unknown | هدف فروش روزانه به تفکیک فروشنده × گروه کالا — **هدف و عملکرد را با هم دارد**. |
| `BodjehDahDarsadForosh_DasteMoaref` | `؟` | None | rows_unknown | — |
| `BodjehYekDarHezarKaraneh_CodeNoe` | `؟` | None | rows_unknown | — |
| `HadafForosh` | `ccHadafForosh` | None | rows_unknown، legacy | هدف فروش. |
| `HadafForoshRoozaneh` | `ccHadafForoshRoozaneh` | None | rows_unknown، legacy | نسخه‌ی بدونِ New. |
| `HadafForoshRoozanehWithTatily` | `ccHadafForoshRoozanehNew` | None | rows_unknown | — |
| `HadafForoshRoozaneh_Arshiv` | `ccHadafForoshRoozaneh_Arshiv` | None | archive_check، rows_unknown | — |
| `HadafForoshandeh_PG` | `ccHadafForoshandeh_PG` | None | rows_unknown، legacy | هدف فروشنده به تفکیک کد کالا، ماهانه. |
| `HadafMoshtary_PG` | `ccHadafMoshtary_PG` | None | rows_unknown | — |
| `HadafOlaviatForosh` | `ccHadafOlaviatForosh` | None | rows_unknown | — |
| `Hadaf_PG` | `ccHadaf` | None | rows_unknown | — |

---

## تخفیف، جایزه و جشنواره

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `TakhfifHajmi` | `ccTakhfifHajmi` | None | effective_dated، rows_unknown | — |
| `TakhfifJayezeh` | `ccTakhfifJayezeh` | None | effective_dated، rows_unknown | — |
| `JashnvarehForosh` | `ccJashnvarehForosh` | None | effective_dated، rows_unknown | — |
| `Jayezeh` | `ccJayezeh` | None | effective_dated، rows_unknown | — |
| `TakhfifSenfiVijeh` | `ccTakhfifSenfiVijeh` | None | effective_dated، rows_unknown | — |
| `JashnvarehForoshSatr` | `ccJashnvarehForoshSatr` | None | detail، effective_dated، rows_unknown | — |
| `JayezehSatr` | `ccJayezehSatr` | None | detail، rows_unknown | — |
| `TakhfifDorei` | `ccTakhfifDorei` | None | effective_dated، status_header، rows_unknown | — |
| `TakhfifHajmiSatr` | `ccTakhfifHajmiSatr` | None | detail، effective_dated، rows_unknown | — |
| `TakhfifHamlMostaghim` | `ccTakhfifHamlMostaghim` | None | effective_dated، rows_unknown | — |
| `TakhfifSefaresh` | `ccTakhfifSefaresh` | None | effective_dated، rows_unknown | — |
| `TakhfifSenfi` | `ccTakhfifSenfi` | None | effective_dated، rows_unknown | — |
| `TakhfifSenfiVijehSatr` | `ccTakhfifSenfiVijehSatr` | None | detail، rows_unknown | — |
| `AvamelJayezeRaeesMarkazPakhsh` | `ccAvamelJayezeRaeesMarkazPakhsh` | None | rows_unknown | — |
| `DastehBandyJaizehForosh` | `ccDastehBandyJaizehForosh` | None | rows_unknown | — |
| `JashnvarehForoshGoroh` | `ccJashnvarehForoshGoroh` | None | rows_unknown | — |
| `JashnvarehForoshMarkaz` | `ccJashnvarehForoshMarkaz` | None | effective_dated، rows_unknown | — |
| `JashnvarehForosh_Emtiaz` | `ccJashnvarehForosh_Emtiaz` | None | rows_unknown | — |
| `JashnvarehForosh_MabnaMohasebeh` | `ccMabnaMohasebeh` | None | rows_unknown | — |
| `JayezehDelpazir` | `ccJayezehDelpazir` | None | rows_unknown | — |
| `JayezehForosh1400_3_Arshive` | `ccJayezehForosh1400_3_Arshive` | None | archive_check، rows_unknown | — |
| `JayezehForosh1400_Arshive` | `ccJayezehForosh1400_Arshive` | None | archive_check، rows_unknown | — |
| `JayezehForoshConfig` | `؟` | None | effective_dated، rows_unknown، end_date_not_null | — |
| `JayezehForoshConfig95` | `؟` | None | year_snapshot، effective_dated، rows_unknown، end_date_not_null | — |
| `JayezehForoshConfig_Noe` | `؟` | None | rows_unknown | — |
| `JayezehForoshDarsadKala` | `ccJayezehForoshDarsadKala` | None | rows_unknown | — |
| `JayezehForoshEmtiazConfig` | `؟` | None | effective_dated، rows_unknown، end_date_not_null | — |
| `JayezehForoshEmtiazSarparast` | `ccJayezehForoshEmtiazSarparast` | None | rows_unknown | — |
| `JayezehForoshKalaTakidi` | `ccJayezehForoshKalaTakidi` | None | rows_unknown | — |
| `JayezehForoshModirMantagheh_Emtiaz` | `ccEmtiaz` | None | rows_unknown | — |
| `JayezehForoshNoeMoshtary` | `؟` | None | rows_unknown | — |
| `JayezehForoshVijeh_Arshive98` | `ccJayezehForoshVijeh_Arshive98` | None | year_snapshot، rows_unknown | — |
| `JayezehForosh_ArshiveReport97` | `ccJayezehForosh_ArshiveReport` | None | year_snapshot، rows_unknown | — |
| `JayezehForosh_ArshiveReport98` | `ccJayezehForosh_ArshiveReport` | None | year_snapshot، rows_unknown | — |
| `JayezehForoshandeh1402` | `ccJayezehForoshandeh` | None | year_snapshot، rows_unknown | — |
| `JayezehForoshandeh1402_OLD` | `ccJayezehForoshandeh` | None | legacy، rows_unknown | — |
| `JayezehForoshandeh1403` | `ccJayezehForoshandeh` | None | year_snapshot، rows_unknown | — |
| `JayezehForoshandeh1404` | `ccJayezehForoshandeh` | None | year_snapshot، rows_unknown | — |
| `JayezehForoshandeh14040321` | `ccJayezehForoshandeh` | None | rows_unknown | — |
| `JayezehForoshandeh96` | `ccJayezehForoshandeh` | None | year_snapshot، rows_unknown | — |
| `JayezehForoshandeh97` | `ccJayezehForoshandeh` | None | year_snapshot، rows_unknown | — |
| `JayezehRaeesMarkaz1402` | `ccJayezehRaeesMarkaz` | None | year_snapshot، rows_unknown | — |
| `JayezehRaeesMarkaz1402_OLD` | `ccJayezehRaeesMarkaz` | None | legacy، rows_unknown | — |
| `JayezehRaeesMarkaz1403` | `ccJayezehRaeesMarkaz` | None | year_snapshot، rows_unknown | — |
| `JayezehSatrKala` | `ccJayezehSatrKala` | None | rows_unknown | — |
| `JayezehTelephoni_Arshive` | `ccJayezehTelephoni_Arshive` | None | archive_check، rows_unknown | — |
| `KalaJayezehForosh` | `ccKalaJayezehForosh` | None | effective_dated، rows_unknown | — |
| `TakhfifHajmiQuery` | `ccTakhfifHajmiQuery` | None | rows_unknown | — |
| `TakhfifHamlMostaghimSatr` | `ccTakhfifHamlMostaghimSatr` | None | detail، rows_unknown | — |
| `TakhfifJayezehAdam` | `ccTakhfifJayezehAdam` | None | effective_dated، rows_unknown | — |
| `TakhfifJayezehGoroh` | `ccTakhfifJayezehGoroh` | None | rows_unknown | — |
| `TakhfifJayezehMarkaz` | `ccTakhfifJayezehMarkaz` | None | effective_dated، rows_unknown | — |
| `TakhfifJayezehMarkazPakhsh` | `ccMarkazPakhsh` | None | effective_dated، rows_unknown | — |
| `TakhfifJayezehSatr` | `ccTakhfifJayezehSatr` | None | detail، rows_unknown | — |
| `TakhfifNaghdy` | `ccTakhfifNaghdy` | None | effective_dated، rows_unknown | — |
| `TakhfifSefareshSatr` | `ccTakhfifSefareshSatr` | None | detail، rows_unknown | — |
| `TakhfifSenfiSatr` | `ccTakhfifSenfiSatr` | None | detail، effective_dated، rows_unknown | — |
| `TakhfifSenfiVijehMoshtary` | `ccTakhfifSenfiVijehMoshtary` | None | dict، rows_unknown | — |
| `TakhfifSenfiVijehSatrKala` | `ccTakhfifSenfiVijehSatrKala` | None | rows_unknown | — |
| `TasvieBaDahDarsadJayezeh_Vaziat` | `ccTasvieBaDahDarsadJayezeh_Vaziat` | None | status_header، rows_unknown | — |
| `ZakhirehYekDarHezarKaranehAutomatic` | `ccZakhirehYekDarHezarKaranehAutomatic` | None | ledger، rows_unknown | — |

---

## کالا و گروه‌بندی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `GorohForosh` | `ccGorohForosh` | None | status_header، anchor، rows_unknown | — |
| `Khadamat` | `ccKhadamat` | None | effective_dated، status_header، rows_unknown | — |
| `GorohNoeHazinehMashin` | `ccGorohNoeHazinehmashin` | None | dict، rows_unknown | — |
| `GorohForoshAfrad` | `ccGorohForoshAfrad` | None | effective_dated، dict، rows_unknown | — |
| `GorohKalaNoeSenf` | `ccGorohKalaNoeSenf` | None | dict، rows_unknown | — |
| `GorohNoeHazinehMashinSatr` | `ccGorohNoeHazinehmashinSatr` | None | detail، dict، rows_unknown | — |
| `GorohOlaviatTozih` | `ccGorohOlaviatTozih` | None | dict، rows_unknown | — |
| `KalaAdamForoshForoshandeh` | `ccKalaAdamForoshForoshandeh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshInMarkazPakhsh` | `ccKalaCode` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshMarkazForosh` | `ccKalaAdamForoshMarkaz` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshMarkazPakhsh` | `ccKalaAdamForoshMarkazPakhsh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshMarkazSazmanForosh` | `ccKalaAdamForoshMarkaz` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshMarkazSazmanForoshNoeMoshtary` | `ccKalaAdamForoshMarkazSazmanForoshNoeMoshtary` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshMarkazSazmanForoshSakhtarForosh` | `ccKalaAdamForoshMarkazSazmanForoshSakhtarForosh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshMarkazSazmanNoeMoshtary` | `ccKalaAdamForoshMarkazSazmanNoeMoshtary` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshSazmanForosh` | `ccKalaAdamForoshSazmanForosh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaAdamForoshShahr` | `ccKalaAdamForoshShahr` | None | effective_dated، status_header، rows_unknown | — |
| `KalaGheymatForosh` | `ccKalaGheymatForosh` | None | effective_dated، status_header، rows_unknown | — |
| `KalaGheymatForoshMarkazSenf` | `ccKalaGheymatForoshMarkazSenf` | None | effective_dated، rows_unknown | — |
| `KalaMaxTedadForosh` | `ccKalaMaxTedadForosh` | None | effective_dated، rows_unknown | — |
| `KalaModatVosolCheck` | `ccKalaModatVosolCheck` | None | effective_dated، status_header، rows_unknown | — |
| `KalaMojodyForoshandeh` | `ccForoshandeh` | None | rows_unknown | — |
| `KalaMojodyGhabelForosh` | `ccMarkazPakhsh` | None | rows_unknown | — |
| `KalaNotMinKharid` | `ccKalaNotMinKharid` | None | rows_unknown | — |
| `KalaZaribForosh` | `ccKalaZaribForosh` | None | effective_dated، status_header، rows_unknown | — |
| `KhadamatGheymat` | `ccKhadamatGheymat` | None | effective_dated، status_header، rows_unknown | — |

---

## توزیع، بارگیری و موجودی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Mashin` | `ccMashin` | None | rows_unknown | — |
| `TafkikJoze` | `ccTafkikJoze` | None | status_header، rows_unknown | — |
| `ZamanTahvil` | `ccZamanTahvil` | None | rows_unknown | — |
| `AnbarGardaniMashin` | `ccAnbarGardaniMashin` | None | rows_unknown | — |
| `MahdodiatePakhsh` | `ccMahdodiatePakhsh` | None | dict، rows_unknown | — |
| `MashinHazineh` | `ccMashinHazineh` | None | status_header، rows_unknown | — |
| `MashinNoeHazineh` | `ccMashinNoeHazineh` | None | rows_unknown | — |
| `MashinNoeHazinehSatr` | `ccMashinNoeHazinehSatr` | None | detail، rows_unknown | — |
| `MashinShomarehPelak` | `ccMashinShomarehPelak` | None | effective_dated، rows_unknown | — |
| `TafkikKol` | `ccTafkikKol` | None | rows_unknown | — |
| `Yakhchal` | `ccYakhchal` | None | rows_unknown | — |
| `AnbarGardaniMashinKala` | `ccAnbarGardaniMashinKala` | None | rows_unknown | — |
| `AnbarMoshtary` | `ccAnbarMoshtary` | None | rows_unknown | — |
| `CodeTozieeForTafkik` | `ccCodeToziee` | None | rows_unknown | — |
| `MahdodiatSakhtTafkik` | `ccMahdodiatSakhtTafkik` | None | rows_unknown | — |
| `MashinHazinehSatr` | `ccMashinHazinehSatr` | None | detail، rows_unknown | — |
| `MashinSookht` | `ccMashinSookht` | None | status_header، rows_unknown | — |
| `Mashin_Polygon_MahdodiatePakhsh` | `ccPolygon_MahdodiatePakhsh` | None | rows_unknown | — |
| `MaxKartonAdams` | `ccMaxKartonAdams` | None | rows_unknown | — |
| `MojoodiGiri` | `ccMojoodiGiri` | None | rows_unknown | — |
| `TafkikJozeForoshAnbarak` | `ccTafkikJozeAnbarak` | None | status_header، rows_unknown | — |
| `TafkikJozeForoshAnbarakSatr` | `؟` | None | detail، rows_unknown | — |
| `TafkikJozeSatr` | `ccTafkikJozeSatr` | None | detail، rows_unknown | — |
| `TafkikJoze_CodeVazeiat` | `ccTafkikJoze_CodeVazeiat` | None | status_dict، rows_unknown | — |
| `TafkikKolSatr` | `ccTafkikKol` | None | detail، rows_unknown | — |
| `Tafkik_MarkazSazmanForosh` | `ccTafkik_MarkazSazmanForosh` | None | rows_unknown | — |
| `YakhchalNoe` | `ccNoeYakhchal` | None | rows_unknown | — |

---

## پیکربندی و مرجع

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `NoeMashin` | `ccNoeMashin` | None | hub_target، rows_unknown | — |
| `ElatAdamFaalMoshtary` | `ccElatAdamFaalMoshtary` | None | dict، rows_unknown | — |
| `NoeMalekiatMoshtary` | `ccNoeMalekiatMoshtary` | None | dict، rows_unknown | — |
| `NoeAdamForosh` | `ccNoeAdamForosh` | None | dict، rows_unknown | — |
| `ElatAdamDarkhast` | `ccElatAdamDarkhast` | None | rows_unknown | — |
| `NoeTakhfifDorei` | `ccNoeTakhfifDorei` | None | dict، rows_unknown | — |
| `Config_NoeMoshtaryNoeVosol` | `ccConfig_NoeMoshtaryNoeVosol` | None | config، effective_dated، rows_unknown | — |
| `NoeControlForosh` | `ccNoeControlForosh` | None | dict، rows_unknown | — |
| `NoeKhadamat` | `ccNoeKhadamat` | None | dict، rows_unknown | — |
| `NoeTakhfifHazineh` | `ccNoeTakhfifHazineh` | None | dict، rows_unknown | — |
| `NoeVisit` | `ccNoeVisit` | None | dict، rows_unknown | — |
| `Shakhes` | `ccShakhes` | None | rows_unknown | — |
| `ConfigShakhesAmarForoshErsalBetaminKonandeh` | `ccConfig` | None | rows_unknown | — |
| `Config_DarkhastMoshtary` | `ccConfig_DarkhastMoshtary` | None | config، rows_unknown | — |
| `Config_DarkhastTaavoni` | `ccConfig_DarkhastTaavoni` | None | config، rows_unknown | — |
| `Config_Foroshandeh` | `ccConfig_Foroshandeh` | None | config، effective_dated، rows_unknown | — |
| `Config_NoeMoshtaryNoeVosolSatr` | `ccConfig_NoeMoshtaryNoeVosolSatr` | None | config، detail، effective_dated، rows_unknown | — |
| `DeviceModel` | `ccDeviceModel` | None | rows_unknown | — |
| `ElatAdamDarkhast_NoeMoshtary` | `ccElatAdamDarkhast_NoeMoshtary` | None | dict، rows_unknown | — |
| `ElatAdamForoshMarkazPakhsh` | `ccElatAdamForoshMarkazPakhsh` | None | dict، rows_unknown | — |
| `MessageInbox` | `Id` | None | rows_unknown | — |
| `NoeBoodjeh` | `ccNoeBoodjeh` | None | dict، rows_unknown | — |
| `NoeVosolAzMoshtary` | `ccNoeVosolAzMoshtary` | None | dict، rows_unknown | — |
| `OutBoxEventItems` | `؟` | None | rows_unknown | — |
| `ReportEstandardNum` | `ccReportEstandardNum` | None | rows_unknown | — |
| `SazmanForoshControlMoavagh` | `ccSazmanForoshControlMoavagh` | None | effective_dated، rows_unknown | — |
| `SazmanForoshRialKharid` | `ccSazmanForoshRialKharid` | None | effective_dated، rows_unknown | — |
| `SazmanForosh_TaminKonandeh` | `؟` | None | rows_unknown | — |
| `SystemConfig` | `؟` | None | rows_unknown | — |
| `ZaribNoeMoshtary` | `ccZaribNoeMoshtary` | None | rule، rows_unknown | ضریب نوع مشتری — ضریب را کدنویسی نکن، از اینجا بخوان. |
| `ZaribZakhirehYekDarHezar` | `؟` | None | rule، effective_dated، rows_unknown | — |
| `ZaribZakhirehYekDarHezarForosh` | `ccZaribZakhirehYekDarHezarForosh` | None | rule، effective_dated، rows_unknown | — |

