# درون‌نگری — استخراج نقشه از دیتابیس زنده

هدف این بخش: پر کردن پوشه‌ی `raw/` که `build_map.py` می‌خواند.

> **`DECLARE` ننویس.** `run_query` یک دستور می‌پذیرد که با `SELECT` یا `WITH`
> شروع شود. پارامتر را با `params` بساز.

> **خروجی در ۵۰۰ سطر بریده می‌شود، بی‌صدا.** این مهم‌ترین محدودیتِ عملی این
> کار است: یک اسکیمای ۴۰۰ جدولی چند هزار سطر ستون دارد. بخش ۲ راهش را
> می‌گوید. اگر این را جدی نگیری، نقشه‌ای می‌سازی که **ستون‌هایش ناقص است و
> هیچ خطایی هم نمی‌دهد**.

---

## ۰.۰ میان‌بر: کلِ دیتابیس را یک‌بار بگیر

اگر می‌توانی خروجی را به فایل بدهی (SSMS → Results to File، یا اکسل)، این
**یک کوئری** جای کل بخش‌های ۱ تا ۲ را می‌گیرد و مهم‌تر از آن، **ارجاع‌های
بین‌اسکیمایی را قابلِ حل می‌کند**:

```sql
SELECT c.TABLE_CATALOG, c.TABLE_SCHEMA, c.TABLE_NAME, c.COLUMN_NAME,
       c.ORDINAL_POSITION, c.DATA_TYPE, c.CHARACTER_MAXIMUM_LENGTH,
       c.NUMERIC_PRECISION, c.NUMERIC_SCALE, c.IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS AS c
ORDER BY c.TABLE_SCHEMA, c.TABLE_NAME, c.ORDINAL_POSITION;
```

بعد:

```bash
python scripts/build_map.py --inventory inventory.tsv --schema Sales --out schema.json
```

سه برتری نسبت به مسیرِ اسکیما‌به‌اسکیما:

- **سقف ۵۰۰ سطر بی‌اثر می‌شود** چون از `run_query` رد نمی‌شود.
- **۲۳٪ ارجاع‌هایی که مقصدشان در اسکیمای دیگری است حل می‌شوند** — بدون فهرست
  کامل، اینها «حل‌نشده» می‌مانند.
- یک بار می‌گیری، برای هر ۱۸ اسکیما استفاده می‌کنی.

> **ولی این کوئری ویوها را هم می‌آورد** (۲۵٪ اشیای این دیتابیس). بخش ۱ را
> هم بگیر تا `build_map.py` بداند کدام واقعاً جدول است؛ وگرنه از روی نام
> (`vXxx`/`V_Xxx`) حدس می‌زند.

## ۰. کدام اسکیماها وجود دارند

اول این. ممکن است اسمی که کاربر گفته اسکیما نباشد، یا دقیقاً همان نباشد.

```sql
SELECT s.name AS schema_name, COUNT(t.object_id) AS tedad_jadval
FROM sys.schemas AS s
LEFT JOIN sys.tables AS t ON t.schema_id = s.schema_id
GROUP BY s.name
HAVING COUNT(t.object_id) > 0
ORDER BY tedad_jadval DESC;
```

نتیجه‌ی واقعی روی `PegahAI`: ۱۸ اسکیما، از `Sales` با ۵۷۰ شیء تا
`OfficeAutomation` با یکی.

> **تله‌ی اول، و همه در آن می‌افتند:** `WHERE name LIKE 'Sales%'` روی
> `sys.tables` **هیچ‌چیز برنمی‌گرداند**، چون `Sales` نامِ اسکیماست نه پیشوندِ
> نامِ جدول. `sys.tables.name` فقط نام جدول را دارد. همیشه با
> `SCHEMA_NAME(schema_id) = '<Schema>'` فیلتر کن.

## ۱. جدول‌ها و تعداد سطر → `raw/tables.json`

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT t.name AS [table], SUM(p.rows) AS [rows]
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
JOIN sys.partitions AS p
  ON p.object_id = t.object_id AND p.index_id IN (0, 1)
CROSS JOIN params AS pr
WHERE s.name = pr.eskima
GROUP BY t.name
ORDER BY t.name;
```

`sys.partitions.rows` تقریبی است ولی برای «خالی است یا نه» و «بزرگ است یا
کوچک» کافی است و **بی‌نهایت ارزان‌تر از `COUNT(*)`** روی هر جدول است.

اگر جدول‌ها از ۵۰۰ بیشتر شدند، با حرف اول تکه‌تکه کن:

```sql
  WHERE s.name = pr.eskima AND t.name >= 'A' AND t.name < 'M'
```

> **`sys.tables` عمدی است، نه `INFORMATION_SCHEMA.TABLES`.** اولی فقط جدول
> می‌دهد؛ دومی ویو را هم می‌آورد. در این دیتابیس ۲۵٪ اشیا ویو است، پس این
> تفاوت یک‌چهارمِ نقشه را عوض می‌کند.

## ۲. ستون‌ها → `raw/columns.json`

**شکل فشرده — یک سطر به ازای هر جدول.** این کارِ اصلی است چون زیر سقف ۵۰۰
می‌ماند:

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT c.TABLE_NAME AS [table],
       STRING_AGG(CONCAT(c.COLUMN_NAME, ':', c.DATA_TYPE, ':', c.IS_NULLABLE),
                  '|') WITHIN GROUP (ORDER BY c.ORDINAL_POSITION) AS cols
FROM INFORMATION_SCHEMA.COLUMNS AS c
CROSS JOIN params AS p
WHERE c.TABLE_SCHEMA = p.eskima
GROUP BY c.TABLE_NAME
ORDER BY c.TABLE_NAME;
```

`build_map.py` هر دو شکل را می‌فهمد — فشرده (`cols`) و سطر‌به‌سطر
(`column`/`type`/`nullable`).

**اگر `STRING_AGG` نبود** (SQL Server پیش از ۲۰۱۷):

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT c.TABLE_NAME AS [table],
       STUFF((SELECT '|' + c2.COLUMN_NAME + ':' + c2.DATA_TYPE + ':' + c2.IS_NULLABLE
              FROM INFORMATION_SCHEMA.COLUMNS AS c2
              WHERE c2.TABLE_SCHEMA = c.TABLE_SCHEMA
                AND c2.TABLE_NAME = c.TABLE_NAME
              ORDER BY c2.ORDINAL_POSITION
              FOR XML PATH('')), 1, 1, '') AS cols
FROM INFORMATION_SCHEMA.COLUMNS AS c
CROSS JOIN params AS p
WHERE c.TABLE_SCHEMA = p.eskima
GROUP BY c.TABLE_SCHEMA, c.TABLE_NAME
ORDER BY c.TABLE_NAME;
```

**اگر خودِ رشته‌ها بریده شدند** (جدولِ خیلی پهن)، برگرد به شکل سطر‌به‌سطر و
با بازه‌ی حرفِ اول تکه کن:

```sql
WITH params AS (SELECT N'Sales' AS eskima, N'A' AS az, N'D' AS ta)
SELECT c.TABLE_NAME AS [table], c.COLUMN_NAME AS [column],
       c.DATA_TYPE AS [type], c.IS_NULLABLE AS nullable,
       c.ORDINAL_POSITION AS pos
FROM INFORMATION_SCHEMA.COLUMNS AS c
CROSS JOIN params AS p
WHERE c.TABLE_SCHEMA = p.eskima
  AND c.TABLE_NAME >= p.az AND c.TABLE_NAME < p.ta
ORDER BY c.TABLE_NAME, c.ORDINAL_POSITION;
```

> **بعد از هر تکه، تعداد سطرِ برگشتی را بشمار.** اگر دقیقاً ۵۰۰ بود، تقریباً
> حتماً بریده شده — بازه را کوچک‌تر کن. **۵۰۰ عددِ گِردی نیست که تصادفی
> دربیاید.**

## ۳. کلیدهای اصلی → `raw/pks.json`

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT t.name AS [table], col.name AS [column], ic.key_ordinal AS ordinal
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
JOIN sys.key_constraints AS kc
  ON kc.parent_object_id = t.object_id AND kc.type = 'PK'
JOIN sys.index_columns AS ic
  ON ic.object_id = kc.parent_object_id AND ic.index_id = kc.unique_index_id
JOIN sys.columns AS col
  ON col.object_id = ic.object_id AND col.column_id = ic.column_id
CROSS JOIN params AS p
WHERE s.name = p.eskima
ORDER BY t.name, ic.key_ordinal;
```

کلید اصلیِ اعلام‌نشده خطا نیست — `build_map.py` آن‌وقت `cc<TableName>` را
حدس می‌زند و در خروجی همان می‌ماند.

## ۴. کلیدهای خارجی → `raw/fks.json`

**مهم‌ترین کوئری این مجموعه.** اگر جواب بدهد، بخش بزرگی از نقشه از حدس به
اثبات می‌رود.

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT OBJECT_NAME(fkc.parent_object_id)            AS parent,
       pc.name                                      AS parent_col,
       OBJECT_SCHEMA_NAME(fkc.referenced_object_id) AS ref_schema,
       OBJECT_NAME(fkc.referenced_object_id)        AS ref,
       rc.name                                      AS ref_col
FROM sys.foreign_key_columns AS fkc
JOIN sys.columns AS pc
  ON pc.object_id = fkc.parent_object_id AND pc.column_id = fkc.parent_column_id
JOIN sys.columns AS rc
  ON rc.object_id = fkc.referenced_object_id
 AND rc.column_id = fkc.referenced_column_id
CROSS JOIN params AS p
WHERE OBJECT_SCHEMA_NAME(fkc.parent_object_id) = p.eskima
ORDER BY parent, parent_col;
```

سه حالت، و هرکدام معنیِ متفاوتی دارد:

| نتیجه | یعنی |
|---|---|
| خالی | روابط در کدِ برنامه‌اند. همه‌چیز حدس است — اسکیل باید صریح بگوید. |
| کم (زیر ۲۰٪ یال‌ها) | بخشی اثبات‌شده. `findings.md` تفکیک می‌کند. |
| پر | نقشه را با آن بسنج. **هرجا اختلاف بود، کلید خارجی درست است.** |

> حالت سوم بخشِ «کلید خارجی با نام‌گذاری نمی‌خواند» را در `findings.md` پر
> می‌کند و **آن گران‌بهاترین خروجیِ کل این کار است**: جایی که قرارداد
> نام‌گذاری می‌شکند، دقیقاً جایی است که یک عاملِ بی‌خبر کوئری غلط می‌نویسد.

## ۵. آخرین تاریخ هر جدول → `raw/dates.json` (اختیاری)

برای جدول‌های دوقلو لازم می‌شود: تعداد سطر می‌گوید کدام بزرگ‌تر است، تاریخ
می‌گوید کدام **هنوز زنده** است.

```sql
SELECT 'PersonelMamoriat' AS [table], 'FromDate' AS [column],
       MAX(FromDate) AS max_value
FROM [HumanResource].[PersonelMamoriat]
UNION ALL
SELECT 'PersonelMamuryat', 'FromDate', MAX(FromDate)
FROM [HumanResource].[PersonelMamuryat];
```

این را **بعد از** اجرای اول `build_map.py` بزن، چون تازه آن‌وقت می‌دانی
کدام جفت‌ها مشکوک‌اند.

## ۶. ذخیره‌ی نتیجه در `raw/`

خروجی `run_query` را با `kind='python'` بنویس:

```python
import json, io, os
os.makedirs("raw", exist_ok=True)
rows = [ ... ]     # همان چیزی که run_query برگرداند
with io.open("raw/tables.json", "w", encoding="utf-8") as fh:
    json.dump(rows, fh, ensure_ascii=False)
```

نام کلیدها مهم نیست — `build_map.py` هم `table`/`TABLE_NAME`/`name` را
می‌فهمد و هم `rows`/`row_count`.

## ۷. ساخت نقشه

```bash
python scripts/build_map.py raw/ --schema Sales --out schema.json
```

بعد **`findings.md` را بخوان.** هرچه ماشین نتوانست تصمیم بگیرد آنجاست:
دامنه‌ها، نقش‌ها، دوقلوها، ارجاع‌های بیرونی.

## ۸. دامنه‌ها

اجرای اول همه را `other` می‌گذارد و خوشه‌های پیشنهادی را در `findings.md`
می‌نویسد. یک `domains.json` بساز:

```json
{
  "hoghogh": {"label": "حقوق و دستمزد", "match": ["^Pardakht", "Hoghogh"]},
  "karkard": {"label": "کارکرد و شیفت",  "match": ["Karkard", "^Shift"]}
}
```

و دوباره بزن:

```bash
python scripts/build_map.py raw/ --schema Sales --domains domains.json --out schema.json
```

`match` عبارت منظم است و **ترتیب مهم است** — اولین تطبیق برنده است.

## ۹. اعتبارسنجی — این مرحله اختیاری نیست

نقشه تا اینجا **ادعا** است. این بخش آن را به **دانش** تبدیل می‌کند.

### ۹.۱ ارجاعِ یتیم — مهم‌ترین آزمون یک یال

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT COUNT(*) AS kol,
       SUM(CASE WHEN p.ccTarget IS NULL THEN 1 ELSE 0 END) AS yatim
FROM [Sales].[SourceTable] AS c
LEFT JOIN [Sales].[TargetTable] AS p ON p.ccTarget = c.ccTarget
WHERE c.ccTarget IS NOT NULL;
```

| نسبت یتیم | تفسیر |
|---|---|
| ۰٪ | یال درست است. `confidence` را به `CONFIRMED` ببر و بنویس با چه چیزی. |
| کم (زیر ۱٪) | یال درست است، داده کمی ناسازگار. در گزارش بگو. |
| زیاد | **یال احتمالاً غلط است.** مقصد را عوض کن یا `LOW` بگذار. |
| ۱۰۰٪ | یال قطعاً غلط است. حذفش کن. |

**این را دست‌کم روی ۱۰ یالِ پرکاربرد بزن** — آنهایی که در جواب‌های واقعی
استفاده می‌شوند. یالی که تست نشده، حدس است، هرچقدر هم نامش بخواند.

### ۹.۲ دانه — قبل از اینکه اسکیل چیزی جمع بزند

```sql
WITH params AS (SELECT N'Sales' AS eskima)
SELECT COUNT(*) AS satr, COUNT(DISTINCT ccKey) AS kelid,
       CAST(COUNT(*) AS decimal(18,2)) / NULLIF(COUNT(DISTINCT ccKey), 0) AS nesbat
FROM [Sales].[Table];
```

`nesbat > 1` یعنی جدول به ازای هر کلید چند سطر دارد — و هر `SUM` بدون
`DISTINCT` چند برابر می‌شود.

### ۹.۳ دوقلوها

تعداد سطر **و** آخرین تاریخِ هر دو را بگیر (بخش ۵). عدد می‌گوید کدام
پرکارتر است؛ **نمی‌گوید کدام مرجع است** — آن را باید بپرسی.

### ۹.۴ کدهای وضعیت

```sql
SELECT CodeVazeiat, COUNT(*) AS tedad
FROM [Sales].[SomeTransaction]
GROUP BY CodeVazeiat ORDER BY tedad DESC;
```

توزیع را کنارِ دیکشنری `X_CodeVazeiat` بگذار. کدی که ۹۰٪ سطرها را دارد
معمولاً «تأییدشده/نهایی» است — ولی **این را تأیید بگیر، حدس نزن**.

## ۱۰. آنچه در `schema.json` باید عوض شود بعد از اعتبارسنجی

- `meta.verified_against_live_db` → `true`
- یال‌های تست‌شده → `confidence: "CONFIRMED"` با یادداشتِ نتیجه‌ی تست
- `meta.version` → تاریخ امروز
- جدول «اندازه‌ها» در `references/queries.md` اسکیلِ ساخته‌شده
