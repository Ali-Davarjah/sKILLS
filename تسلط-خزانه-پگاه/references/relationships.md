# اتصال‌ها، واژگان مشترک، و تله‌ها

```
اگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB
```

**هیچ‌کدام اثبات‌شده نیست** — این اسکیما کلید خارجی ندارد.

## مرکزهای ثقل

| موجودیت | ارجاع ورودی | نقش |
|---|---:|---|
| `DariaftPardakht` | 25 | سندِ دریافت/پرداخت — **مرکز ثقلِ این اسکیما** (۲۵ ارجاع ورودی). |
| `EjazehPardakhtFaktor` | 14 | اجازه پرداخت فاکتور — **دروازه‌ی خروجِ پول و پرارجاع‌ترین پل به بقیه‌ی اسکیماها**. |
| `DariaftPardakhtPPC` | 10 | همان سند، **ثبت‌شده روی دستگاه همراه** — ۹ ستون بیشتر. |
| `EjazehPardakhtPishPardakht` | 8 | اجازه پرداختِ پیش‌پرداخت. |
| `Boodjeh` | 7 | بودجه — اجازه پرداخت به آن گره می‌خورد. |
| `MahaleVariz` | 7 | محل واریز |
| `Tankhah` | 6 | تنخواه — گردشِ وجهِ در اختیار. |
| `TankhahDar` | 4 | نگه‌دارنده‌ی تنخواه |
| `KartBank` | 4 | کارت بانکی |
| `Sandogh` | 3 | صندوق — به تفکیک مرکز پخش. |
| `DariaftPardakhtVazeiat` | 3 | تاریخچه‌ی وضعیت سند — **و مبلغ هم دارد**. |
| `ManbaDP` | 2 | — |
| `SandoghMarkazi` | 2 | صندوق مرکزی — گردشِ تجمیعی. |
| `AeenNamehElamiehBank` | 1 | — |
| `DariaftPardakhtDarkhastFaktor` | 1 | — |

## ارجاع‌های بیرونی

| `cc` | تکرار | تفسیر |
|---|---:|---|
| `ccMarkazPakhsh` | 35 | ✔ `Global.MarkazPakhsh` |
| `ccUser` | 31 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccShomarehHesab` | 23 | ✔ `Global.ShomarehHesab` |
| `ccMarkaz` | 23 | ✔ `Global.Markaz` |
| `ccMarkazAnbar` | 17 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazForosh` | 15 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccDarkhastFaktor` | 14 | ✔ `Sales.DarkhastFaktor` |
| `ccMarkazSazmanForoshSakhtarForosh` | 13 | ✔ `Global.MarkazSazmanForoshSakhtarForosh` |
| `ccMoshtary` | 12 | ✔ `Sales.Moshtary` |
| `ccElatOdat` | 11 | ✔ `Global.ElatOdat` |
| `ccSazmanForosh` | 9 | ✔ `Global.SazmanForosh` |
| `ccUserSabegheh` | 9 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccBankSanad` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccSakhtarForosh` | 8 | ✔ `Global.SakhtarForosh` |
| `ccAfradErsalKonandeh` | 8 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfrad` | 8 | ✔ `Global.Afrad` |
| `ccBank` | 7 | ✔ `Global.Bank` |
| `ccPhoto` | 7 | ✔ `Global.Photo` |
| `ccForoshandeh` | 6 | ✔ `Sales.Foroshandeh` |
| `ccvTafsily1` | 5 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccNoeMoshtary` | 5 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccKardex` | 5 | ✔ `Warehouse.Kardex` |
| `ccTafkikJoze` | 5 | ✔ `Sales.TafkikJoze` |
| `ccHesab3` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccHesab4` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradTahsildar` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccDariaftPardakhtLink` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccUserSabtKonandeh` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccTaminKonandeh` | 4 | ✔ `Purchase.TaminKonandeh` |
| `ccAfradMamorVosol` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradMamorPakhsh` | 4 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccHesab0` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccHesab1` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccHesab2` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccHesab7` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccNoeHesabSanad` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccShahrCheck` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccCodeHesabMoeen` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccDorehMaly` | 3 | ✔ `FinancialAccounting.DorehMaly` |
| `ccBrand` | 3 | ✔ `Amargar.Brand` |

✔ یعنی جدولِ هم‌نام در آن اسکیما **وجود دارد**. مقصد قطعی
است؛ خوردنِ ستون‌ها هنوز آزمونِ یتیم می‌خواهد.

## تله‌ها

`python scripts/map.py traps` همه را می‌دهد. خلاصه:

- دوقلو: **6** جفت
- سطرِ با پدرِ غیرمنتظره: **0**
- ناسازگاری نوع: **1**
- عرضِ ناسازگار: **19**
- جدول با ستون مرده: **0**

## فهرست کامل اتصال‌ها

| مبدأ | ستون | مقصد |
|---|---|---|
| `AeenNamehElamiehBank1` | `ccAeenNamehElamiehBank` | `AeenNamehElamiehBank` |
| `ArshiveCheck` | `ccDariaftPardakht` | `DariaftPardakht` |
| `BestankaryMoshtary` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Boodjeh_Hesab` | `ccBoodjeh` | `Boodjeh` |
| `Boodjeh_RizMarkaz` | `ccBoodjeh` | `Boodjeh` |
| `Config_VazeiatNaghd` | `ccBoodjeh` | `Boodjeh` |
| `Config_VazeiatNaghd` | `ccMahaleVariz` | `MahaleVariz` |
| `DariaftPardakht` | `ccMahaleVariz` | `MahaleVariz` |
| `DariaftPardakht` | `ccManbaDP` | `ManbaDP` |
| `DariaftPardakht` | `ccSandogh` | `Sandogh` |
| `DariaftPardakhtBargashty` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtBargashtyPPC` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `DariaftPardakhtDarkhastFaktor` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtDarkhastFaktorPPC` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtDarkhastFaktorPPC` | `ccDariaftPardakhtDarkhastFaktor` | `DariaftPardakhtDarkhastFaktor` |
| `DariaftPardakhtDarkhastFaktorppc_Tmp` | `ccDariaftPardakhtppc` | `DariaftPardakhtPPC` |
| `DariaftPardakhtElamiehBankPPC` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `DariaftPardakhtFaktorZayeat` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtFaktorZayeatPPC` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtPPC` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtPPC` | `ccMahaleVariz` | `MahaleVariz` |
| `DariaftPardakhtPPC` | `ccManbaDP` | `ManbaDP` |
| `DariaftPardakhtPPC` | `ccSandogh` | `Sandogh` |
| `DariaftPardakhtPPC_BargashtBodjeh` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `DariaftPardakhtPPC_Photo` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `DariaftPardakhtVazeiat` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtVazeiatPPC` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakhtVazeiatPPC` | `ccDariaftPardakhtVazeiat` | `DariaftPardakhtVazeiat` |
| `DariaftPardakhtVazeiatPPC_Photo` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `DariaftPardakht_Afrad` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakht_MahaleVariz` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DariaftPardakht_MahaleVariz` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `DariaftPardakht_MahaleVariz` | `ccMahaleVariz` | `MahaleVariz` |
| `DariaftPardakht_Photo` | `ccDariaftPardakht` | `DariaftPardakht` |
| `DastehCheck` | `ccNoeDastehCheck` | `NoeDastehCheck` |
| `DastehCheckBarg` | `ccDastehCheck` | `DastehCheck` |
| `DastehCheckTankhah` | `ccShomarehHesabTankhah` | `ShomarehHesabTankhah` |
| `EjazehPardakhtFaktor` | `ccBoodjeh` | `Boodjeh` |
| `EjazehPardakhtFaktor` | `ccTankhah` | `Tankhah` |
| `EjazehPardakhtFaktor` | `ccTankhahDar` | `TankhahDar` |
| `EjazehPardakhtFaktorPhoto` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakhtFaktorSatr` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakhtFaktor_MoshakhasatAmval` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakhtFaktor_MoshakhasatAmval` | `ccEjazehPardakhtFaktorSatr` | `EjazehPardakhtFaktorSatr` |
| `EjazehPardakhtMoshakhasatSheba` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakhtPishPardakht` | `ccBoodjeh` | `Boodjeh` |
| `EjazehPardakhtPishPardakht` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakhtPishPardakht` | `ccKartBank` | `KartBank` |
| `EjazehPardakhtPishPardakht` | `ccTankhah` | `Tankhah` |
| `EjazehPardakhtPishPardakht` | `ccTankhahDar` | `TankhahDar` |
| `EjazehPardakhtPishPardakhtPhoto` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `EjazehPardakhtPishPardakhtSatr` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `EjazehPardakhtPishPardakht_MoshakhasatSheba` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `EjazehPardakht_BedehyPersonel` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakht_PishPardakht_ForSanad` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakht_PishPardakht_ForSanad` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `EjazehPardakht_PishPardakht_ForSanad` | `ccKartBank` | `KartBank` |
| `EjazehPardakht_PishPardakht_ForSanad` | `ccKartBankEjazehPardakhtFaktor` | `KartBankEjazehPardakhtFaktor` |
| `EjazehPardakht_PishPardakht_ForSanad` | `ccTankhah` | `Tankhah` |
| `EjazehPardakht_TmpKartBankEjazehPardakht` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakht_ZamanVazeiat` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `EjazehPardakht_ZamanVazeiat` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `ElamiehBedehkari` | `ccNoeElamiehBedehkari` | `NoeElamiehBedehkari` |
| `ElamiehBedehkariSatr` | `ccElamiehBedehkari` | `ElamiehBedehkari` |
| `ElamiehBedehkariSatr` | `ccNoeAfradElamiehBedehkari` | `NoeAfradElamiehBedehkari` |
| `ItemPishbiniSatr` | `ccItemPishbini` | `ItemPishbini` |
| `KartBankEjazehPardakhtFaktor` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `KartBankEjazehPardakhtFaktor` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `KartBankEjazehPardakhtFaktor` | `ccKartBank` | `KartBank` |
| `KartBankVazeiat` | `ccKartBank` | `KartBank` |
| `LinkMoghayeratVosolCheck` | `ccDariaftPardakht` | `DariaftPardakht` |
| `List_DPV_ForDelete` | `ccDariaftPardakhtVazeiat` | `DariaftPardakhtVazeiat` |
| `MahaleVariz_CodeNoeVosol` | `ccMahaleVariz` | `MahaleVariz` |
| `MoghayeratBankSatr` | `ccMoghayeratBank` | `MoghayeratBank` |
| `PardakhtElectronic` | `ccDariaftPardakht` | `DariaftPardakht` |
| `PardakhtElectronic` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `Sabegheh_DariaftPardakhtPPC` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Sabegheh_DariaftPardakhtPPC` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `Sabegheh_DariaftPardakhtPPC` | `ccSandogh` | `Sandogh` |
| `Sabegheh_EjazehPardakhtFaktor` | `ccBoodjeh` | `Boodjeh` |
| `Sabegheh_EjazehPardakhtFaktor` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `Sabegheh_EjazehPardakhtFaktor` | `ccTankhah` | `Tankhah` |
| `Sabegheh_EjazehPardakhtFaktor` | `ccTankhahDar` | `TankhahDar` |
| `SandoghMarkazi` | `ccMahaleDariaftPardakht` | `MahaleDariaftPardakht` |
| `SandoghMarkaziSatr` | `ccBoodjeh` | `Boodjeh` |
| `SandoghMarkaziSatr` | `ccSandoghMarkazi` | `SandoghMarkazi` |
| `SandoghMarkazi_KharidDeyn` | `ccSandoghMarkazi` | `SandoghMarkazi` |
| `TamdidTasviehMoavaghat` | `ccDariaftPardakht` | `DariaftPardakht` |
| `TamdidTasviehMoavaghat_Photo` | `ccTamdidTasviehMoavaghat` | `TamdidTasviehMoavaghat` |
| `Tankhah` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `Tankhah` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `Tankhah` | `ccTankhahDar` | `TankhahDar` |
| `TankhahDariaftPardakht` | `ccTankhah` | `Tankhah` |
| `TankhahPhoto` | `ccTankhah` | `Tankhah` |
| `TashilatSatr` | `ccTashilat` | `Tashilat` |
| `TasviehMoavaghat_Boodjeh` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Tmp_AsnadVagozari` | `ccdariaftPardakht` | `DariaftPardakht` |
| `Tmp_Bestankari` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Tmp_ChackBargashti` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Tmp_ChackBargashti` | `ccMahaleVariz` | `MahaleVariz` |
| `Tmp_DariaftPardakhtppc` | `ccDariaftPardakhtPPC` | `DariaftPardakhtPPC` |
| `Tmp_MoshtaryBestankar` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Tmp_MoshtaryNegEslahat` | `ccDariaftPardakht` | `DariaftPardakht` |
| `Tmp_SuratHesabVosolCheckByExcel` | `ccMahaleVariz` | `MahaleVariz` |
| `Tmp_TasviehEjazehPardakhtByKartBank` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `Tmp_TasviehEjazehPardakhtByKartBank` | `ccEjazehPardakhtPishPardakht` | `EjazehPardakhtPishPardakht` |
| `Tmp_TasviehNaghesFaktorByPishPardakht` | `ccEjazehPardakhtFaktor` | `EjazehPardakhtFaktor` |
| `Tmp_rptCheckBargashty` | `ccDariaftPardakht` | `DariaftPardakht` |
| `VAsnadMoshtarianBeTafkikForoshandeh` | `ccDariaftPardakht` | `DariaftPardakht` |
| `VAsnadMoshtarianBeTafkikForoshandeh` | `ccDariaftPardakhtVazeiat` | `DariaftPardakhtVazeiat` |
