# موجودیت‌ها، دامنه به دامنه

برای هر دامنه: جدول مرجع، ستون‌های لازم، **دانه‌ی هر سطر**، و آنچه اسم جدول نمی‌گوید.

پیشوند اسکیما لازم است: `[Treasury].[TableName]`.

<!-- TODO --> برای هر جدولِ مهم یک جمله نقش بنویس و دانه‌اش را مشخص کن.

---

## گزارش، آرشیو و جدول موقت — منبع حقیقت نیست

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `ArshiveCheck` | `ccArshiveCheck` | None | status_header، rows_unknown | — |
| `List_DPV_ForDelete` | `؟` | None | rows_unknown | — |
| `MoeenHesabMoshtaryKol_Archive` | `ID` | None | archive_check، rows_unknown | — |
| `MojodySandogh_Arshiv` | `ccMojodySandogh_Arshiv` | None | archive_check، rows_unknown | — |
| `Sabegheh_DariaftPardakhtPPC` | `؟` | None | status_header، rows_unknown | — |
| `Sabegheh_EjazehPardakhtFaktor` | `ccEjazehPardakhtFaktor` | None | status_header، ledger، rows_unknown | — |
| `TMP_BodjehYekDarHeazar` | `؟` | None | legacy، rows_unknown | — |
| `TarikhJobManual` | `؟` | None | rows_unknown | — |
| `TmpMoghayeratSuratHesabBanki` | `؟` | None | ledger، rows_unknown | — |
| `TmpSuratHesabVosolCheck` | `ccSuratHesab` | None | status_header، ledger، rows_unknown | — |
| `Tmp_AsnadDariafty` | `؟` | None | legacy، status_header، rows_unknown | — |
| `Tmp_AsnadVagozari` | `؟` | None | legacy، status_header، rows_unknown | — |
| `Tmp_Bestankari` | `ID` | None | legacy، rows_unknown | — |
| `Tmp_Bestankary` | `؟` | None | legacy، rows_unknown | — |
| `Tmp_ChackBargashti` | `ccTmp_ChackBargashti` | None | legacy، status_header، rows_unknown | — |
| `Tmp_DariaftPardakhtppc` | `ID` | None | legacy، rows_unknown | — |
| `Tmp_DataPishbini` | `ID` | None | legacy، rows_unknown | — |
| `Tmp_KartBank` | `؟` | None | legacy، sensitive، rows_unknown | — |
| `Tmp_MoshtaryBestankar` | `ID` | None | legacy، rows_unknown | — |
| `Tmp_MoshtaryNegEslahat` | `ccMoshtary` | None | legacy، rows_unknown | — |
| `Tmp_RptKartBank` | `ccRptKartBank` | None | legacy، sensitive، rows_unknown | — |
| `Tmp_SuratHesabVosolCheckByExcel` | `ccTmp_SuratHesabVosolCheckByExcel` | None | legacy، status_header، sensitive، rows_unknown | — |
| `Tmp_SuratHesabVosolCheckByExcel_Json` | `ccTmp_SuratHesabVosolCheckByExcel_Json` | None | legacy، sensitive، rows_unknown | — |
| `Tmp_TasviehEjazehPardakhtByKartBank` | `ID` | None | legacy، ledger، rows_unknown | — |
| `Tmp_TasviehNaghesFaktorByPishPardakht` | `ccRow` | None | legacy، rows_unknown | — |
| `Tmp_rptCheckBargashty` | `ccRpt` | None | legacy، status_header، rows_unknown | — |
| `VAsnadMoshtarianBeTafkikForoshandeh` | `ccDariaftPardakht` | None | status_header، rows_unknown | — |
| `tmpReportAmalKardSandogh` | `ccRpt` | None | rows_unknown | — |
| `tmp_MoghayeratMoeenMoshtaryKol` | `ID` | None | legacy، rows_unknown | — |

---

## دریافت و پرداخت — سندِ مرکزی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `DariaftPardakht` | `ccDariaftPardakht` | None | status_header، tree، hub_target، rows_unknown، anchor | سندِ دریافت/پرداخت — **مرکز ثقلِ این اسکیما** (۲۵ ارجاع ورودی). |
| `DariaftPardakhtPPC` | `ccDariaftPardakhtPPC` | None | status_header، hub_target، rows_unknown | همان سند، **ثبت‌شده روی دستگاه همراه** — ۹ ستون بیشتر. |
| `DariaftPardakhtVazeiat` | `ccDariaftPardakhtVazeiat` | None | status_history، status_header، rows_unknown | تاریخچه‌ی وضعیت سند — **و مبلغ هم دارد**. |
| `ManbaDP` | `ccManbaDP` | None | dict، rows_unknown | — |
| `DariaftPardakhtDarkhastFaktor` | `ccDariaftPardakhtDarkhastFaktor` | None | status_header، rows_unknown | — |
| `MahaleDariaftPardakht` | `ccMahaleDariaftPardakht` | None | dict، rows_unknown | — |
| `DariaftPardakhtBargashty` | `ccDariaftPardakhtBargashty` | None | status_header، tree، rows_unknown | — |
| `DariaftPardakhtBargashtyPPC` | `ccDariaftPardakhtBargashtyPPC` | None | rows_unknown | — |
| `DariaftPardakhtDarkhastFaktorPPC` | `ccDariaftPardakhtDarkhastFaktor` | None | status_header، rows_unknown | — |
| `DariaftPardakhtDarkhastFaktorppc_Tmp` | `؟` | None | rows_unknown | — |
| `DariaftPardakhtElamiehBankPPC` | `ccDariaftPardakhtElamiehBank` | None | rows_unknown | — |
| `DariaftPardakhtFaktorZayeat` | `ccDariaftPardakhtFaktorZayeat` | None | status_header، rows_unknown | — |
| `DariaftPardakhtFaktorZayeatPPC` | `ccDariaftPardakhtFaktorZayeatPPC` | None | status_header، rows_unknown | — |
| `DariaftPardakhtPPC_BargashtBodjeh` | `ccDariaftPardakhtPPC` | None | rows_unknown | — |
| `DariaftPardakhtPPC_Photo` | `ccPhoto` | None | attachment، rows_unknown | — |
| `DariaftPardakhtVazeiatPPC` | `ccDariaftPardakht` | None | status_header، rows_unknown | — |
| `DariaftPardakhtVazeiatPPC_Photo` | `ccPhoto` | None | attachment، rows_unknown | — |
| `DariaftPardakht_Afrad` | `ccDariaftPardakht` | None | rows_unknown | — |
| `DariaftPardakht_MahaleVariz` | `ccDariaftPardakhtPPC_MahaleVariz` | None | rows_unknown | — |
| `DariaftPardakht_NoeVazeiat` | `ccDariaftPardakht_NoeVazeiat` | None | status_header، dict، rows_unknown | — |
| `DariaftPardakht_Photo` | `؟` | None | attachment، rows_unknown | — |
| `MandehAvalSalDariaftPardakht` | `؟` | None | status_header، rows_unknown | مانده اول سال |
| `NoeDariaftPardakht` | `؟` | None | dict، rows_unknown | — |
| `PishbinidariaftPardakht` | `ccPishbinidariaftPardakht` | None | ledger، rows_unknown | — |

---

## اجازه پرداخت

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `EjazehPardakhtFaktor` | `ccEjazehPardakhtFaktor` | None | status_header، ledger، hub_target، rows_unknown، anchor | اجازه پرداخت فاکتور — **دروازه‌ی خروجِ پول و پرارجاع‌ترین پل به بقیه‌ی اسکیماها**. |
| `EjazehPardakhtPishPardakht` | `ccEjazehPardakhtPishPardakht` | None | status_header، ledger، rows_unknown | اجازه پرداختِ پیش‌پرداخت. |
| `EjazehPardakhtFaktorSatr` | `ccEjazehPardakhtFaktorSatr` | None | detail، ledger، rows_unknown | سطرِ تخصیصِ حسابداری — بده/بستان روی کدهای حساب. |
| `EjazehPardakhtElatOdat` | `ccElatOdat` | None | reason_dict، dict، rows_unknown | — |
| `EjazehPardakhtFaktorPhoto` | `ccEjazehPardakhtFaktor_Photo` | None | rows_unknown | — |
| `EjazehPardakhtFaktorVazeiat` | `ccEjazehPardakhtFaktorVazeiat` | None | status_header، rows_unknown | — |
| `EjazehPardakhtFaktor_ModatPardakht` | `ccEjazehPardakhtFaktor_ModatPardakht` | None | rows_unknown | — |
| `EjazehPardakhtFaktor_MoshakhasatAmval` | `ccAmvalSatr_EjazehFaktorSatr` | None | rows_unknown | — |
| `EjazehPardakhtMoshakhasatSheba` | `؟` | None | sensitive، rows_unknown | — |
| `EjazehPardakhtPishPardakhtPhoto` | `ccPhoto` | None | rows_unknown | — |
| `EjazehPardakhtPishPardakhtSatr` | `ccEjazehPardakhtPishPardakhtSatr` | None | detail، ledger، rows_unknown | — |
| `EjazehPardakhtPishPardakht_MoshakhasatSheba` | `ccEjazehPardakhtPishPardakht_MoshakhasatSheba` | None | sensitive، rows_unknown | — |
| `EjazehPardakht_BedehyPersonel` | `ccBedehyPersonel` | None | ledger، rows_unknown | — |
| `EjazehPardakht_NoeBedehyPersonel` | `ccNoeBedehy` | None | rows_unknown | — |
| `EjazehPardakht_PishPardakht_ForSanad` | `ccTable` | None | rows_unknown | — |
| `EjazehPardakht_TmpKartBankEjazehPardakht` | `ccTmpKartBankEjazehPardakht` | None | rows_unknown | — |
| `EjazehPardakht_ZamanVazeiat` | `ccEjazehPardakht_ZamanVazeiat` | None | status_header، rows_unknown | — |

---

## تنخواه

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Tankhah` | `ccTankhah` | None | status_header، ledger، rows_unknown | تنخواه — گردشِ وجهِ در اختیار. |
| `TankhahDar` | `ccTankhahDar` | None | effective_dated، rows_unknown | نگه‌دارنده‌ی تنخواه |
| `ShomarehHesabTankhah` | `ccShomarehHesabTankhah` | None | rows_unknown | — |
| `DarsadTankhahMarkazPakhsh` | `ccMarkazPakhsh` | None | rows_unknown | — |
| `DastehCheckTankhah` | `ccDastehCheckTankhah` | None | rows_unknown | — |
| `SaghfTankhah` | `ccSaghfTankhah` | None | rule، rows_unknown | سقف تنخواه |
| `TankhahDariaftPardakht` | `ccTankhahDariaftPardakht` | None | rows_unknown | — |
| `TankhahPhoto` | `ccTankhah` | None | rows_unknown | — |
| `TankhahVazeiat` | `ccTankhahVazeiat` | None | status_header، dict، rows_unknown | — |

---

## صندوق

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Sandogh` | `ccSandogh` | None | rows_unknown | صندوق — به تفکیک مرکز پخش. |
| `SandoghMarkazi` | `ccSandoghMarkazi` | None | rows_unknown | صندوق مرکزی — گردشِ تجمیعی. |
| `KhazanehDar` | `ccKhazanehDar` | None | effective_dated، rows_unknown | — |
| `SandoghMarkaziSatr` | `ccSandoghMarkaziSatr` | None | detail، rows_unknown | — |
| `SandoghMarkazi_CodeNoeVosol` | `ccSandoghMarkazi_CodeNoeVosol` | None | rows_unknown | — |
| `SandoghMarkazi_KharidDeyn` | `ccSandoghMarkazi_KharidDeyn` | None | rows_unknown | — |

---

## چک و سفته

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `DastehCheck` | `ccDastehCheck` | None | rows_unknown | دسته‌چک — بازه‌ی سریال و برگ‌های مانده. |
| `NoeDastehCheck` | `ccNoeDastehCheck` | None | dict، rows_unknown | — |
| `Config_VosolCheck` | `ccConfig_VosolCheck` | None | config، dict، rows_unknown | — |
| `DastehCheckBarg` | `ccDastehCheckBarg` | None | rows_unknown | — |
| `ElatOdatVazeiatCheckNamayandegan` | `ccElateOdat` | None | reason_dict، dict، rows_unknown | — |
| `LinkMoghayeratVosolCheck` | `ccMoghayeratLink` | None | rows_unknown | — |
| `NoeCheckMoshtary` | `ccNoeCheckMoshtary` | None | dict، rows_unknown | — |
| `Sabt_Check` | `ccSabtCheck` | None | rows_unknown | — |
| `Sabt_FishBanki` | `ccSabt_FishBanki` | None | rows_unknown | — |
| `Sabt_Naghd` | `ccSabt_Naghd` | None | rows_unknown | — |
| `Sabt_NoeVosolMovaghat` | `ccSabt_NoeVosolMovaghat` | None | rows_unknown | — |
| `Safteh` | `ccSafteh` | None | rows_unknown | سفته |

---

## وصول و تحصیل

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `CodeNoeVosol` | `؟` | None | rows_unknown | — |
| `Config_NoeVosolMojaze_Faktor` | `ccConfig_NoeVosolMojaze_Faktor` | None | config، status_header، rows_unknown | — |
| `Config_NoeVosolMojaze_Moshtary` | `ccConfig_NoeVosolMojaze_Moshtary` | None | config، status_header، rows_unknown | — |
| `Config_VosolFaktor` | `ccConfig_VosolFaktor` | None | config، rows_unknown | — |
| `ElatOdatVosol` | `ccElatOdat` | None | reason_dict، dict، rows_unknown | — |
| `ElatOdatVosol_CodeNoeVosol` | `ccElat` | None | reason_dict، dict، rows_unknown | — |
| `MahaleVariz_CodeNoeVosol` | `ccMahaleVariz_CodeNoeVosol` | None | rows_unknown | — |
| `NoeMoghayeratVosol` | `؟` | None | dict، rows_unknown | — |
| `NoeVosolMojaze_Faktor` | `ccNoeVosolMojaze_Faktor` | None | status_header، dict، rows_unknown | — |
| `NoeVosolMojaze_Moshtary` | `ccNoeVosolMojaze_Moshtary` | None | status_header، dict، rows_unknown | — |
| `OdatTafkikMamorPakhsh_PPC` | `ccOdatTafkik` | None | rows_unknown | — |
| `TaaedVosolTablet` | `ccTaaedVosolTablet` | None | rows_unknown | — |
| `Tahsildar` | `ccTahsildar` | None | rows_unknown | تحصیل‌دار — مسئولِ وصول. |
| `VorodKhorojMamorPakhsh_FromTablet` | `ccVorodKhoroj` | None | rows_unknown | — |
| `VosolFaktor_Position` | `ccVosolFaktor_Position` | None | rows_unknown | — |

---

## بودجه و پیش‌بینی

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Boodjeh` | `ccBoodjeh` | None | rows_unknown | بودجه — اجازه پرداخت به آن گره می‌خورد. |
| `ItemPishbini` | `ccItemPishbini` | None | rows_unknown | — |
| `Boodjeh_Hesab` | `ccBoodjeh_Hesab` | None | rows_unknown | — |
| `Boodjeh_RizMarkaz` | `ccBoodjeh_Rizmarkaz` | None | effective_dated، rows_unknown، end_date_not_null | — |
| `ItemNaghdinegi_CodeHesab` | `ccitemNaghdinegi_CodeHesab` | None | rows_unknown | — |
| `ItemPishbiniSatr` | `ccItemPishbiniSatr` | None | detail، rows_unknown | — |
| `Pishbini` | `ccPishbini` | None | rows_unknown | — |

---

## مغایرت بانکی و اعلامیه

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `AeenNamehElamiehBank` | `ccAeenNamehElamiehBank` | None | rule، rows_unknown | — |
| `ElamiehBedehkari` | `ccElamiehBedehkari` | None | status_header، rows_unknown | اعلامیه بدهکاری |
| `MoghayeratBank` | `ccMoghayeratBank` | None | effective_dated، rows_unknown، end_date_not_null | مغایرت‌گیری بانکی — بازه‌دار. |
| `NoeAfradElamiehBedehkari` | `ccNoeAfradElamiehBedehkari` | None | dict، rows_unknown | — |
| `NoeElamiehBedehkari` | `ccNoeElamiehBedehkari` | None | dict، rows_unknown | — |
| `AeenNamehElamiehBank1` | `ccAeenNamehElamiehBank` | None | rule، rows_unknown | — |
| `AeenNamehElamiehBank_ShobehBank` | `ccMarkazPakhsh` | None | rule، rows_unknown | — |
| `ElamiehBedehkariSatr` | `ccElamiehBedehkariSatr` | None | detail، rows_unknown | — |
| `MoghayeratBankSatr` | `ccMoghayeratBankSatr` | None | detail، ledger، rows_unknown | — |

---

## بانک، کارت و محل واریز

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `MahaleVariz` | `ccMahaleVariz` | None | rows_unknown | محل واریز |
| `KartBank` | `ccKartBank` | None | status_header، ledger، tree، rows_unknown | کارت بانکی |
| `KartBankEjazehPardakhtFaktor` | `ccKartBankEjazehPardakhtFaktor` | None | rows_unknown | — |
| `BestankariRoozMoshtary` | `ccBestankariRoozMoshtary` | None | rows_unknown | — |
| `BestankaryMoshtary` | `؟` | None | rows_unknown | — |
| `KartBankNoeAmalKard` | `ccKartBankNoeAmalKard` | None | ledger، rows_unknown | — |
| `KartBankVazeiat` | `ccKartBankVazeiat` | None | status_history، status_header، rows_unknown | — |
| `PardakhtElectronic` | `ccPardakhtElectronic` | None | rows_unknown | پرداخت الکترونیک |

---

## تسویه معوقات و تمدید

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `TamdidTasviehMoavaghat` | `ccTamdidTasviehMoavaghat` | None | status_header، rows_unknown | — |
| `TamdidTasviehMoavaghat_ElatOdat` | `ccElatOdat` | None | reason_dict، dict، rows_unknown | — |
| `TamdidTasviehMoavaghat_Photo` | `ccTamdidTasviehMoavaghat` | None | attachment، rows_unknown | — |
| `TasviehMoavaghatSatr_Boodjeh` | `ccTasviehMoavaghatSatrBoodjeh` | None | status_header، rows_unknown | — |
| `TasviehMoavaghat_Boodjeh` | `ccTasviehMoavaghatBoodjeh` | None | status_header، rows_unknown | — |
| `TasviehMoavaghat_BoodjehElat` | `ccElat` | None | rows_unknown | — |
| `TasviehMoavaghat_NoeTarafHesab` | `ccNoeTarafHesab` | None | rows_unknown | — |

---

## تسهیلات

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Tashilat` | `ccTashilat` | None | status_header، rows_unknown | تسهیلات (وام بانکی) |
| `TashilatSatr` | `ccTashilatSatr` | None | detail، rows_unknown | — |

---

## پیکربندی و مرجع

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Config_ControlEtebar_NoeMoshtary` | `ccConfig_ControlEtebar_NoeMoshtary` | None | config، status_header، rows_unknown | — |
| `Config_DirKard_Tajil` | `ccConfig_DirKard_Tajil` | None | config، status_header، rows_unknown | — |
| `Config_DirkardOrTajil` | `ccConfig_DirkardOrTajil` | None | config، effective_dated، rows_unknown | — |
| `Config_EtelaatMali_SazmanForosh` | `ccConfig_EtelaatMali_SazmanForosh` | None | config، status_header، rows_unknown | — |
| `Config_VazeiatNaghd` | `ccConfig_VazeiatNaghd` | None | config، rows_unknown | — |
| `ControlEtebar_NoeMoshtary` | `ccControlEtebar_NoeMoshtary` | None | status_header، rows_unknown | — |
| `SystemConfig` | `ccMarkazPakhsh` | None | rows_unknown | — |

