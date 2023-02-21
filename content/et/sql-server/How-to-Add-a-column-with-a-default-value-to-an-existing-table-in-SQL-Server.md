---
title: "Kuidas lisada SQL Serveris olemasolevasse tabelisse vaikeväärtusega veerg"
description: "SQL serveris, et lisada olemasolevasse tabelisse vaikeväärtusega veerg, kasutage 'ALTER' tabeli 'ADD' veeru nime 'NULL/NOT NULL' piirangut 'DEFAULT' väärtusega."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

SQL serveris, et lisada olemasolevasse tabelisse vaikeväärtusega veerg, kasutage `ALTER` tabelis `ADD` veeru nimi koos `NULL/NOT NULL` piiranguga `DEFAULT` väärtusega.

Allpool esitatud SQL serveri päringu süntaksiga saab lisada olemasolevasse tabelisse vaikeväärtusega veeru.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Vaatame selle täpsemaks mõistmiseks läbi ühe näite.

## Olemasolevatele kirjetele vaikeväärtusega mittetäidetava veeru lisamine

Võtame SQL-serveri tabeli `Employee` ja kui soovime lisada miinimumpalga veeru vaikeväärtusega `1000USD`, kasutame alljärgnevat päringut.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Ülaltoodud päring lisab tabelisse `Employee` uue veeru `MINIMUM_WAGE` ja täidab olemasolevate ridade veeru vaikeväärtusega, st `1000`. 

Kuna me oleme lisanud `NOT NULL` piirangu.

Kui te ei lisa `NOT NULL` piirangut, on kõik olemasolevad read `NULL` ja `DEFAULT` esitatud väärtus ei mõjuta. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Kõik `MINIMUM_WAGE` veeru väärtused on `NULL`.

Te peate lisama `DEFAULT` väärtuse, kui lisate `NOT NULL` piirangu, kui tabel ei ole tühi. 

Näiteks kui tabel `Employee` ei ole tühi ja kui te lisate uue veeru koos `NOT NULL` piiranguga, siis tekib viga.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Ülaltoodud SQL-serveri päring tekitab olemasolevasse tabelisse uue veeru lisamisel alljärgneva vea.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Kui tabel `Employee` on tühi. 

Ülaltoodud SQL-serveri päring lisab uue veeru ilma probleemideta.

## Nullable veeru lisamine vaikeväärtusega olemasolevatele kirjetele

Kui soovite lisada nullitava veeru vaikeväärtusega olemasolevatele kirjetele, peate kasutama sql-avalduses `WITH VALUES`.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Ülaltoodud päringuga lisatakse SQL-serveri tabelisse nullitav veerg, millel on olemasolevate kirjete jaoks vaikeväärtus.

Kui see juhendaja on õppinud lisama nii nullable kui ka non nullable veergu sql serveri tabelisse vaikeväärtusega kõigi olemasolevate kirjete jaoks.

