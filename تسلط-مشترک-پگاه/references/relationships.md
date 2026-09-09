# اتصال‌ها، واژگان مشترک، و تله‌ها

```
اگر A.ccB هست و جدول B هم هست  →  حدسِ اول:  A.ccB = B.ccB
```

**هیچ‌کدام اثبات‌شده نیست** — این اسکیما کلید خارجی ندارد.

## مرکزهای ثقل

| موجودیت | ارجاع ورودی | نقش |
|---|---:|---|
| `Afrad` | 14 | شخص — **مرجعِ هویتِ کلِ دیتابیس** (۹۶ ارجاع از همه‌ی اسکیماها). |
| `MarkazPakhsh` | 10 | مرکز پخش — **پرارجاع‌ترین جدولِ کلِ دیتابیس** (۱۸۴ ارجاع). |
| `Markaz` | 10 | مرکز — ۱۳۱ ارجاع، بیشترش از HumanResource. |
| `Address` | 5 | آدرس |
| `Goroh` | 4 | گروه‌بندیِ **چندریخت** — یک جدول برای ده‌ها تاکسونومیِ متفاوت. |
| `MantaghehPakhsh` | 4 | منطقه پخش |
| `Houzeh` | 4 | حوزه |
| `Mahal` | 4 | — |
| `AeenNameh` | 3 | — |
| `NoeAfrad` | 3 | — |
| `BankShobeh` | 3 | — |
| `MantaghehForosh` | 3 | منطقه فروش — ۷۴ ارجاع، تقریباً همه از Sales. |
| `NoeVahedForosh` | 3 | نوع واحد فروش — ۴۵ ارجاع |
| `ShomarehHesab` | 3 | شماره حساب بانکی — ۳۸ ارجاع، بیشترش از Treasury. |
| `AeenNameh_VahedSazmani` | 2 | — |

## ارجاع‌های بیرونی

| `cc` | تکرار | تفسیر |
|---|---:|---|
| `ccUser` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradModir` | 3 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccShahr` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMantagheh` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccVahedSazmani` | 2 | ✔ `HumanResource.VahedSazmani` |
| `ccDastehBandyJaizehForosh` | 2 | ✔ `Sales.DastehBandyJaizehForosh` |
| `ccMarkazForosh` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccUserSabegheh` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccNoeMoshtary` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccLink` | 2 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccVahedSazmani_Tanzimkonandeh` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfrad_TanzimKonandeh` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccSystem` | 1 | ✔ `dbo.System` |
| `ccAeenNameh_Post` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccVahedSazmani_Post` | 1 | ✔ `HumanResource.VahedSazmani_Post` |
| `ccShahrTavalod` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccShahrSodor` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazPakhshFaal` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazFaal` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccSazmanForoshFaal` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccSakhtarForoshFaal` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazAnbar` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMoshtary` | 1 | ✔ `Sales.Moshtary` |
| `ccSh` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccHesab3` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccBankShobehPosition` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAfradSystem` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccAddressLatin` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccLink_ElatOdat` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccGorohLink` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccRoot` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `cchesab4` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccBrand` | 1 | ✔ `Amargar.Brand` |
| `ccConfig_CodingKala` | 1 | ✔ `Warehouse.Config_CodingKala` |
| `ccAfradSabegheh` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccLevelTolidLink` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMahalLink` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazPakhshAsli` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMantaghehOld` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |
| `ccMarkazAsli` | 1 | حل‌نشده — در هیچ اسکیمای این دیتابیس نیست |

✔ یعنی جدولِ هم‌نام در آن اسکیما **وجود دارد**. مقصد قطعی
است؛ خوردنِ ستون‌ها هنوز آزمونِ یتیم می‌خواهد.

## تله‌ها

`python scripts/map.py traps` همه را می‌دهد. خلاصه:

- دوقلو: **1** جفت
- سطرِ با پدرِ غیرمنتظره: **0**
- ناسازگاری نوع: **3**
- عرضِ ناسازگار: **3**
- جدول با ستون مرده: **0**

## فهرست کامل اتصال‌ها

| مبدأ | ستون | مقصد |
|---|---|---|
| `AeenNameh` | `ccAeenNameh_DorehBaznegari` | `AeenNameh_DorehBaznegari` |
| `AeenNameh` | `ccAeenNameh_NoeAfrad` | `AeenNameh_NoeAfrad` |
| `AeenNameh` | `ccAeenNameh_NoeTabaghehBandi` | `AeenNameh_NoeTabaghehBandi` |
| `AeenNameh` | `ccAeenNameh_Onvan` | `AeenNameh_Onvan` |
| `AeenNameh` | `ccAeenNameh_VahedSazmani` | `AeenNameh_VahedSazmani` |
| `AeenNameh` | `ccAfrad_SabtKonandeh` | `Afrad` |
| `AeenNamehSatr` | `ccAeenNameh` | `AeenNameh` |
| `AeenNamehSatr` | `ccAfrad_SabtKonandeh` | `Afrad` |
| `AeenNamehSatr` | `ccPhoto` | `Photo` |
| `AeenNameh_Onvan` | `ccAeenNameh_NoeTabaghehBandi` | `AeenNameh_NoeTabaghehBandi` |
| `AeenNameh_Onvan` | `ccAeenNameh_VahedSazmani` | `AeenNameh_VahedSazmani` |
| `AeenNameh_SazmanForosh` | `ccAeenNameh` | `AeenNameh` |
| `AeenNameh_SazmanForosh` | `ccSazmanForosh` | `SazmanForosh` |
| `AeenNameh_VahedsazmaniPost` | `ccAeenNameh` | `AeenNameh` |
| `Afrad` | `ccMarkaz` | `Markaz` |
| `Afrad` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `Afrad` | `ccNoeAfrad` | `NoeAfrad` |
| `Afrad` | `ccSherkathayeTarafGharardad` | `SherkathayeTarafGharardad` |
| `AfradAddress` | `ccAddress` | `Address` |
| `AfradAddress` | `ccAfrad` | `Afrad` |
| `AfradAddress` | `ccNoeAddress` | `NoeAddress` |
| `AfradGoroh` | `ccAfrad` | `Afrad` |
| `AfradGoroh` | `ccGoroh` | `Goroh` |
| `AnbarPakhshShahr` | `ccMarkazSazmanForosh` | `MarkazSazmanForosh` |
| `AnbarPakhshShahrSatr` | `ccAnbarPakhshShahr` | `AnbarPakhshShahr` |
| `BankShobeh` | `ccAddress` | `Address` |
| `BankShobeh` | `ccBank` | `Bank` |
| `BankShobeh` | `ccMarkaz` | `Markaz` |
| `BankShobeh` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `BankShobehAfrad` | `ccAfrad` | `Afrad` |
| `BankShobehAfrad` | `ccBankShobeh` | `BankShobeh` |
| `Company` | `ccAddress` | `Address` |
| `Company` | `ccNoeCompany` | `NoeCompany` |
| `Company` | `ccSherkathayeTarafGharardad` | `SherkathayeTarafGharardad` |
| `Depo` | `ccMantaghehPakhsh` | `MantaghehPakhsh` |
| `GorohMahsol` | `ccGoroh` | `Goroh` |
| `GorohMantaghehForosh` | `ccAfrad` | `Afrad` |
| `GorohMantaghehVahedForosh` | `ccGorohMantaghehForosh` | `GorohMantaghehForosh` |
| `GorohMantaghehVahedForosh` | `ccMantaghehPakhsh` | `MantaghehPakhsh` |
| `GorohMantaghehVahedForosh` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `GorohSort` | `ccGoroh` | `Goroh` |
| `Goroh_CodeingKala` | `ccGoroh` | `Goroh` |
| `Houzeh` | `ccMantaghehPakhsh` | `MantaghehPakhsh` |
| `HouzehForosh` | `ccHouzeh` | `Houzeh` |
| `HouzehForosh` | `ccMantaghehForosh` | `MantaghehForosh` |
| `KhatTolid` | `ccSalonTolid` | `SalonTolid` |
| `MahalRotbeh` | `ccMahal` | `Mahal` |
| `Mahal_CodePosti` | `ccMahal` | `Mahal` |
| `Mahal_PishShomarehTel` | `ccMahal` | `Mahal` |
| `MantaghehForosh` | `ccNoeVahedForosh` | `NoeVahedForosh` |
| `MantaghehPakhsh` | `ccAfrad` | `Afrad` |
| `Markaz` | `ccAddress` | `Address` |
| `Markaz` | `ccAfrad` | `Afrad` |
| `Markaz` | `ccHouzeh` | `Houzeh` |
| `Markaz` | `ccMantaghehAnbarPakhsh` | `MantaghehAnbarPakhsh` |
| `Markaz` | `ccMantaghehForosh` | `MantaghehForosh` |
| `Markaz` | `ccMarkazPakhsh_Old` | `MarkazPakhsh` |
| `Markaz` | `ccNoeKarbariMarkaz` | `NoeKarbariMarkaz` |
| `MarkazHistory` | `ccHouzeh` | `Houzeh` |
| `MarkazHistory` | `ccMantaghehAnbarPakhsh` | `MantaghehAnbarPakhsh` |
| `MarkazHistory` | `ccMantaghehForosh` | `MantaghehForosh` |
| `MarkazHistory` | `ccMarkaz` | `Markaz` |
| `MarkazPakhsh` | `ccAddress` | `Address` |
| `MarkazPakhsh` | `ccAfrad` | `Afrad` |
| `MarkazPakhsh` | `ccHouzeh` | `Houzeh` |
| `MarkazPakhsh` | `ccMantaghehPakhsh` | `MantaghehPakhsh` |
| `MarkazPakhsh` | `ccNoeMarkazPakhsh` | `NoeMarkazPakhsh` |
| `MarkazPakhshMahal` | `ccMahal` | `Mahal` |
| `MarkazPakhshMahal` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `MarkazPakhshShomarehHesab` | `ccMarkaz` | `Markaz` |
| `MarkazPakhshShomarehHesab` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `MarkazPakhshShomarehHesab` | `ccShomarehHesab` | `ShomarehHesab` |
| `MarkazPakhsh_NoeMarkazPakhshBakhsh` | `ccMarkaz` | `Markaz` |
| `MarkazPakhsh_NoeMarkazPakhshBakhsh` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `MarkazPakhsh_NoeMarkazPakhshBakhsh` | `ccNoeMarkazPakhshBakhsh` | `NoeMarkazPakhshBakhsh` |
| `MarkazSazmanForosh` | `ccMarkaz` | `Markaz` |
| `MarkazSazmanForosh` | `ccSazmanForosh` | `SazmanForosh` |
| `MarkazSazmanForoshSakhtarForosh` | `ccAfrad` | `Afrad` |
| `MarkazSazmanForoshSakhtarForosh` | `ccMarkazSazmanForosh` | `MarkazSazmanForosh` |
| `MarkazSazmanForoshSakhtarForosh` | `ccModirMantaghehForosh` | `ModirMantaghehForosh` |
| `MarkazSazmanForoshSakhtarForosh` | `ccSakhtarForosh` | `SakhtarForosh` |
| `Markaz_ShahrMarkazi` | `ccMarkaz` | `Markaz` |
| `MoavenatSazmanForosh` | `ccAfrad` | `Afrad` |
| `ModirMantaghehForosh` | `ccAfrad` | `Afrad` |
| `ModirMantaghehForosh` | `ccModirSakhtarForosh` | `ModirSakhtarForosh` |
| `ModirSakhtarForosh` | `ccAfrad` | `Afrad` |
| `ModirSakhtarForosh` | `ccModirSazmanForosh` | `ModirSazmanForosh` |
| `ModirSazmanForosh` | `ccAfrad` | `Afrad` |
| `ModirSazmanForosh` | `ccMoavenatSazmanForosh` | `MoavenatSazmanForosh` |
| `MoghayeratSystem` | `ccMarkaz` | `Markaz` |
| `MoghayeratSystem` | `ccNoeMoghayeratSystem` | `NoeMoghayeratSystem` |
| `NoeAddressNoeAfrad` | `ccNoeAddress` | `NoeAddress` |
| `NoeAddressNoeAfrad` | `ccNoeAfrad` | `NoeAfrad` |
| `NoeHesab` | `ccBank` | `Bank` |
| `NoeMarkazPakhsh` | `ccNoeVahedForosh` | `NoeVahedForosh` |
| `NoeMarkazPakhshBakhsh` | `ccBakhsh` | `Bakhsh` |
| `NoeMarkazPakhshBakhsh` | `ccNoeMarkazPakhsh` | `NoeMarkazPakhsh` |
| `NoeMarkazPakhshBakhsh` | `ccNoeVahedForosh` | `NoeVahedForosh` |
| `NoePhotoNoeAfrad` | `ccNoeAfrad` | `NoeAfrad` |
| `NoePhotoNoeAfrad` | `ccNoePhoto` | `NoePhoto` |
| `NoeSenfMoshtarySakhtarForosh` | `ccMarkazSazmanForoshSakhtarForosh` | `MarkazSazmanForoshSakhtarForosh` |
| `NoeSenfMoshtarySakhtarForosh` | `ccNoeSenfMoshtary` | `NoeSenfMoshtary` |
| `PosShomarehHesab` | `ccShomarehHesab` | `ShomarehHesab` |
| `SalonTolid` | `ccKarkhaneh` | `Karkhaneh` |
| `SherkathayeTarafGharardad` | `ccSherkathayeTarafGharardad_Noe` | `SherkathayeTarafGharardad_Noe` |
| `SherkathayeTarafGharardad_SystemLink` | `ccSherkathayeTarafGharardad_System` | `SherkathayeTarafGharardad_System` |
| `ShobeBankMarkazPakhsh` | `ccMarkaz` | `Markaz` |
| `ShobeBankMarkazPakhsh` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `ShobeBankMarkazPakhsh` | `ccShomarehHesab` | `ShomarehHesab` |
| `ShomarehHesab` | `ccBankShobeh` | `BankShobeh` |
| `ShomarehHesab` | `ccNoeHesab` | `NoeHesab` |
| `ShomarehHesabTaghirat` | `ccBankShobeh` | `BankShobeh` |
| `ShomarehHesabTaghirat` | `ccNoeHesab` | `NoeHesab` |
| `TaghvimTatil` | `ccMarkaz` | `Markaz` |
| `TaghvimTatil` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `TaghvimTatilManabeEnsani` | `ccMarkazPakhsh` | `MarkazPakhsh` |
| `TolidCodeAutoMatic` | `ccConfig_TolidCodeAutoMatic` | `Config_TolidCodeAutoMatic` |
| `TolidCodeAutoMaticSatr` | `ccTolidCodeAutoMatic` | `TolidCodeAutoMatic` |
