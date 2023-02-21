---
title: "Hoe voeg je een kolom met een standaardwaarde toe aan een bestaande tabel in SQL Server"
description: "Om een kolom met een standaardwaarde toe te voegen aan een bestaande tabel gebruik je 'ALTER' Table 'ADD' kolomnaam met 'NULL/NOT NULL' constraint met 'DEFAULT' waarde."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Om in SQL server een kolom met een standaardwaarde aan een bestaande tabel toe te voegen, gebruikt u `ALTER` Table `ADD` column name with `NULL/NOT NULL` constraint with `DEFAULT` value.

Onderstaande sql-server query syntaxis kan worden gebruikt om een kolom met de standaardwaarde toe te voegen aan de bestaande tabel.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Laten we een voorbeeld doornemen om het verder te begrijpen.

## Een niet-nulbare kolom toevoegen met standaardwaarde voor bestaande records

Overweeg een `Employee` tabel in SQL server, en als we een minimum loon kolom willen toevoegen met standaard waarde als `1000USD`, gebruik dan de onderstaande query.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

De bovenstaande query voegt een nieuwe kolom `MINIMUM_WAGE` toe aan de tabel `Employee` en vult de kolom in bestaande rijen met de standaardwaarde `1000`. 

Omdat we de beperking `NOT NULL` hebben toegevoegd.

Als u de beperking `NOT NULL` niet toevoegt, zijn alle bestaande rijen `NULL` en heeft de waarde `DEFAULT` geen invloed. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Alle `MINIMUM_WAGE` kolomwaarden zullen `NULL` zijn.

U moet `DEFAULT` waarde toevoegen als u `NOT NULL` constraint als de tabel niet leeg is. 

Als bijvoorbeeld de tabel `Employee` niet leeg is, en u voegt een nieuwe kolom toe met de beperking `NOT NULL`, krijgt u een foutmelding.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

De bovenstaande sql server query geeft de onderstaande foutmelding bij het toevoegen van een nieuwe kolom aan de bestaande tabel.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Als de tabel `Employee` leeg is. 

De bovenstaande sql server query zal zonder problemen een nieuwe kolom toevoegen.

## Een vervulbare kolom toevoegen met standaardwaarde voor bestaande records

Als je een nulbare kolom met standaardwaarde voor bestaande records wilt toevoegen, moet je `WITH VALUES` gebruiken in de sql verklaring.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

De bovenstaande query zal een nullable kolom toevoegen aan de sql server tabel met de standaardwaarde voor bestaande records.

In deze tutorial hebben we geleerd om een kolom toe te voegen, zowel nullable en niet-nullable colums aan de sql server tabel met standaard waarde voor alle bestaande records.

