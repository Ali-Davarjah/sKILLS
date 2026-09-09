# موجودیت‌ها، دامنه به دامنه

برای هر دامنه: جدول مرجع، ستون‌های لازم، **دانه‌ی هر سطر**، و آنچه اسم جدول نمی‌گوید.

پیشوند اسکیما لازم است: `[Global].[TableName]`.

<!-- TODO --> برای هر جدولِ مهم یک جمله نقش بنویس و دانه‌اش را مشخص کن.

---

## موقت و میراث — منبع حقیقت نیست

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Taghvim_old` | `ID` | None | legacy، rows_unknown | تقویم — نسخه‌ی قدیمی. |

---

## ساختار سازمانی — مرکز، منطقه، حوزه، لاین

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Markaz` | `ccMarkaz` | None | tree، hub_target، rows_unknown، anchor | مرکز — ۱۳۱ ارجاع، بیشترش از HumanResource. |
| `MarkazPakhsh` | `ccMarkazPakhsh` | None | hub_target، rows_unknown، anchor | مرکز پخش — **پرارجاع‌ترین جدولِ کلِ دیتابیس** (۱۸۴ ارجاع). |
| `Houzeh` | `ccHouzeh` | None | dict، rows_unknown | حوزه |
| `MantaghehPakhsh` | `ccMantaghehPakhsh` | None | rows_unknown | منطقه پخش |
| `MantaghehForosh` | `ccMantaghehForosh` | None | rows_unknown | منطقه فروش — ۷۴ ارجاع، تقریباً همه از Sales. |
| `NoeVahedForosh` | `ccNoeVahedForosh` | None | dict، rows_unknown | نوع واحد فروش — ۴۵ ارجاع |
| `MantaghehAnbarPakhsh` | `ccMantaghehAnbarPakhsh` | None | dict، rows_unknown | — |
| `MarkazSazmanForosh` | `ccMarkazSazmanForosh` | None | rows_unknown | مرکز × لاین فروش |
| `NoeMarkazPakhsh` | `ccNoeMarkazPakhsh` | None | dict، rows_unknown | — |
| `SazmanForosh` | `ccSazmanForosh` | None | rows_unknown | لاین فروش — ۴۹ ارجاع. |
| `Bakhsh` | `ccBakhsh` | None | dict، rows_unknown | — |
| `MarkazSazmanForoshSakhtarForosh` | `ccMarkazSazmanForoshSakhtarForosh` | None | rows_unknown | مرکز × لاین × ساختار فروش |
| `MoavenatSazmanForosh` | `ccMoavenatSazmanForosh` | None | dict، rows_unknown | — |
| `NoeMarkazPakhshBakhsh` | `ccNoeMarkazPakhshBakhsh` | None | dict، rows_unknown | — |
| `SakhtarForosh` | `ccSakhtarForosh` | None | rows_unknown | ساختار فروش |
| `Darajeh` | `ccDarajeh` | None | rows_unknown | درجه |
| `Holding` | `ccHolding` | None | dict، rows_unknown | — |
| `HouzehForosh` | `ccHouzehForosh` | None | rows_unknown | حوزه فروش |
| `MarkazHistory` | `ccMarkazHistory` | None | legacy، effective_dated، rows_unknown | — |
| `MarkazPakhshMahal` | `ccMarkazPakhsh` | None | rows_unknown | — |
| `MarkazPakhshShomarehHesab` | `ccMarkazPakhsh` | None | rows_unknown | — |
| `MarkazPakhsh_NoeMarkazPakhshBakhsh` | `ccMarkazPakhsh_NoeMarkazPakhshBakhsh` | None | rows_unknown | — |
| `Markaz_ShahrMarkazi` | `ccMarkaz_ShahrMarkazi` | None | rows_unknown | — |
| `ShobeBankMarkazPakhsh` | `؟` | None | rows_unknown | — |
| `ShobeBankShahr` | `؟` | None | dict، rows_unknown | — |
| `VaziatHoghooghi` | `ccVaziatHoghooghi` | None | rows_unknown | — |

---

## اشخاص

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Afrad` | `ccAfrad` | None | sensitive، hub_target، rows_unknown، anchor | شخص — **مرجعِ هویتِ کلِ دیتابیس** (۹۶ ارجاع از همه‌ی اسکیماها). |
| `NoeAfrad` | `ccNoeAfrad` | None | dict، rows_unknown | — |
| `ModirMantaghehForosh` | `ccModirMantaghehForosh` | None | rows_unknown | — |
| `ModirSakhtarForosh` | `ccModirSakhtarForosh` | None | rows_unknown | — |
| `ModirSazmanForosh` | `ccModirSazmanForosh` | None | rows_unknown | — |
| `AfradAddress` | `ccAfrad` | None | effective_dated، rows_unknown | — |
| `AfradGoroh` | `ccAfrad` | None | rows_unknown | گروه‌بندی اشخاص |

---

## تقویم

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Mah` | `؟` | None | dict، rows_unknown | — |
| `RoozHafteh` | `ccRoozHafteh` | None | dict، rows_unknown | — |
| `Taghvim` | `ID` | None | rows_unknown، anchor | تقویم شمسی شرکت — مبنای هر منطقِ تاریخی در کلِ دیتابیس. |
| `TaghvimTatil` | `ccTaghvimTatil` | None | rows_unknown | تعطیلات تقویم |
| `TaghvimTatilManabeEnsani` | `ccTaghvimTatilManabeEnsani` | None | rows_unknown | تعطیلات منابع انسانی |

---

## گروه‌بندی چندریخت

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Goroh` | `ccGoroh` | None | tree، rows_unknown، anchor | گروه‌بندیِ **چندریخت** — یک جدول برای ده‌ها تاکسونومیِ متفاوت. |
| `GorohMantaghehForosh` | `ccGorohMantaghehForosh` | None | dict، rows_unknown | — |
| `GorohMahsol` | `ccGorohMahsol` | None | dict، rows_unknown | — |
| `GorohMantaghehVahedForosh` | `ccGorohMantaghehVahedForosh` | None | effective_dated، dict، rows_unknown | — |
| `GorohSort` | `ccGoroh` | None | dict، rows_unknown | — |
| `Goroh_CodeingKala` | `ccGoroh_CodeingKala` | None | effective_dated، rows_unknown | — |

---

## بانک، حساب و محل پرداخت

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `BankShobeh` | `ccBankShobeh` | None | rows_unknown | — |
| `ShomarehHesab` | `ccShomarehHesab` | None | sensitive، rows_unknown | شماره حساب بانکی — ۳۸ ارجاع، بیشترش از Treasury. |
| `Bank` | `ccBank` | None | rows_unknown | بانک |
| `NoeHesab` | `ccNoeHesab` | None | dict، rows_unknown | — |
| `BankPosition` | `ccBankShobehPosition` | None | rows_unknown | — |
| `BankShobehAfrad` | `ccBankShobeh` | None | rows_unknown | — |
| `MahalePardakht` | `ccMahalePardakht` | None | dict، rows_unknown | — |
| `PosShomarehHesab` | `ccPosShomarehHesab` | None | rows_unknown | — |
| `ShomarehHesabTaghirat` | `ccShomarehHesabTaghirat` | None | sensitive، rows_unknown | — |

---

## مکان و آدرس

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `Address` | `ccAddress` | None | rows_unknown | آدرس |
| `Mahal` | `ccMahal` | None | tree، rows_unknown | — |
| `Border` | `ccBorder` | None | dict، rows_unknown | — |
| `MahalRotbeh` | `ccMahalRotbeh` | None | rows_unknown | — |
| `Mahal_CodePosti` | `ccMahal_CodePosti` | None | rows_unknown | — |
| `Mahal_PishShomarehTel` | `ccMahal_PishShomarehTel` | None | rows_unknown | — |
| `Mahal_Zone` | `؟` | None | rows_unknown | — |
| `MarzKhorojAzKeshvar` | `ccMarzKhorojAzKeshvar` | None | rows_unknown | — |

---

## تصویر و پیوست

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `NoePhoto` | `ccNoePhoto` | None | dict، rows_unknown | — |
| `Photo` | `ccPhoto` | None | sensitive، rows_unknown | مخزن تصویر/پیوست — ۴۹ ارجاع. |
| `NoePhotoNoeAfrad` | `ccNoeAfrad` | None | dict، rows_unknown | — |
| `PhotoSize` | `ccPhotoSize` | None | rows_unknown | — |

---

## شرکت و تولید

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `SherkathayeTarafGharardad` | `ccSherkathayeTarafGharardad` | None | tree، rows_unknown | — |
| `AnbarPakhshShahr` | `ccAnbarPakhshShahr` | None | rows_unknown | — |
| `Karkhaneh` | `ccKarkhaneh` | None | dict، rows_unknown | — |
| `SalonTolid` | `ccSalonTolid` | None | dict، rows_unknown | — |
| `SherkathayeTarafGharardad_Noe` | `ccSherkathayeTarafGharardad_Noe` | None | dict، rows_unknown | — |
| `SherkathayeTarafGharardad_System` | `ccSherkathayeTarafGharardad_System` | None | dict، rows_unknown | — |
| `TolidCodeAutoMatic` | `ccTolidCodeAutoMatic` | None | status_header، rows_unknown | — |
| `AnbarPakhshShahrSatr` | `ccAnbarPakhshShahrSatr` | None | detail، rows_unknown | — |
| `Company` | `ccCompany` | None | rows_unknown | — |
| `DamayeNegahdari` | `ccDamayeNegahdari` | None | rows_unknown | — |
| `Depo` | `ccDepo` | None | rows_unknown | — |
| `KhatTolid` | `ccKhatTolid` | None | dict، rows_unknown | — |
| `LevelTolid` | `ccLevelTolid` | None | tree، rows_unknown | — |
| `SherkathayeTarafGharardad_SystemLink` | `ccSherkathayeTarafGharardad_SystemLink` | None | effective_dated، rows_unknown | — |
| `TolidCodeAutoMaticSatr` | `ccTolidCodeAutoMaticSatr` | None | detail، status_header، rows_unknown | — |

---

## پیکربندی، نوع و قاعده

| جدول | کلید | سطر | نشانه‌ها | نقش |
|---|---|---:|---|---|
| `AeenNameh` | `ccAeenNameh` | None | rule، status_header، rows_unknown | — |
| `AeenNameh_NoeTabaghehBandi` | `ccAeenNameh_NoeTabaghehBandi` | None | rule، dict، rows_unknown | — |
| `AeenNameh_VahedSazmani` | `ccAeenNameh_VahedSazmani` | None | rule، rows_unknown | — |
| `NoeAddress` | `ccNoeAddress` | None | dict، rows_unknown | — |
| `AeenNameh_DorehBaznegari` | `ccAeenNameh_DorehBaznegari` | None | rule، dict، rows_unknown | — |
| `AeenNameh_NoeAfrad` | `ccAeenNameh_NoeAfrad` | None | rule، dict، rows_unknown | — |
| `AeenNameh_Onvan` | `ccAeenNameh_Onvan` | None | rule، rows_unknown | — |
| `Config_TolidCodeAutoMatic` | `ccConfig_TolidCodeAutoMatic` | None | config، status_header، dict، rows_unknown | — |
| `NoeCompany` | `ccNoeCompany` | None | dict، rows_unknown | — |
| `NoeKarbariMarkaz` | `ccNoeKarbariMarkaz` | None | dict، rows_unknown | — |
| `NoeMoghayeratSystem` | `ccNoeMoghayeratSystem` | None | dict، rows_unknown | — |
| `NoeSenfMoshtary` | `ccNoeSenfMoshtary` | None | dict، rows_unknown | — |
| `AeenNamehSatr` | `ccAeenNamehSatr` | None | detail، rule، rows_unknown | — |
| `AeenNamehSystem` | `ccAeenNamehSystem` | None | rule، rows_unknown | — |
| `AeenNameh_SazmanForosh` | `ccAeenNameh_SazmanForosh` | None | rule، rows_unknown | — |
| `AeenNameh_VahedsazmaniPost` | `ccAeenNameh_Post` | None | rule، rows_unknown | — |
| `Config_Madarek` | `ccConfig_Madarek` | None | config، attachment، status_header، rows_unknown | — |
| `Config_Page` | `ccConfig_Page` | None | config، rows_unknown | — |
| `ElatOdat` | `ccElatOdat` | None | reason_dict، dict، rows_unknown | علتِ برگشت/ردِ عمومی — ۶۴ ارجاع. |
| `Govahinameh` | `ccGovahinameh` | None | rows_unknown | — |
| `MessageInbox` | `Id` | None | rows_unknown | — |
| `MoghayeratSystem` | `ccMoghayeratSystem` | None | rows_unknown | — |
| `NoeAddressNoeAfrad` | `ccNoeAfrad` | None | dict، rows_unknown | — |
| `NoeEtebar` | `ccNoeEtebar` | None | dict، rows_unknown | — |
| `NoeKerayeHaml` | `ccNoeKerayeHaml` | None | dict، rows_unknown | — |
| `NoeMohasebehEtebar` | `ccNoeMohasebehEtebar` | None | dict، rows_unknown | — |
| `NoeMoshtaryModatVosol` | `ccNoeMoshtaryModatVosol` | None | dict، rows_unknown | — |
| `NoeSenfMoshtarySakhtarForosh` | `ccNoeSenfMoshtarySakhtarForosh` | None | dict، rows_unknown | — |
| `NoeShakhsiat` | `ccNoeShakhsiat` | None | dict، rows_unknown | — |
| `NoeSys` | `ccNoeSys` | None | dict، rows_unknown | — |
| `NoeTatili` | `ccNoeTatili` | None | dict، rows_unknown | — |
| `NoeVasile` | `ccNoeVasile` | None | status_header، dict، rows_unknown | — |
| `NoeVasilehNaghlieh` | `ccNoeVasilehNaghlieh` | None | status_header، dict، rows_unknown | — |
| `OutBoxEventItems` | `؟` | None | rows_unknown | — |
| `SotooheGozaresheSarane` | `؟` | None | rows_unknown | — |
| `SystemConfig` | `ccSystemConfig` | None | rows_unknown | — |
| `VahedPool` | `ccVahedPool` | None | dict، rows_unknown | — |
| `voice_menu_company_name` | `؟` | None | rows_unknown | — |

