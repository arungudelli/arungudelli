---
title: "Sådan tilføjes en kolonne med en standardværdi til en eksisterende tabel i SQL Server"
description: "Hvis du vil tilføje en kolonne med en standardværdi til en eksisterende tabel i SQL Server, skal du bruge 'ALTER' Table 'ADD' kolonnenavn med 'NULL/NOT NULL' begrænsning med 'DEFAULT' værdi."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Hvis du vil tilføje en kolonne med en standardværdi til en eksisterende tabel i SQL Server, skal du bruge `ALTER` Table `ADD` column name with `NULL/NOT NULL` constraint with `DEFAULT` value.

Nedenstående SQL Server-forespørgselssyntaks kan bruges til at tilføje en kolonne med standardværdien i den eksisterende tabel.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Lad os gennemgå et eksempel for at forstå det yderligere.

## Tilføjelse af en kolonne, der ikke kan annulleres, med standardværdi for eksisterende poster

Overvej en `Employee` tabel i SQL server, og hvis vi ønsker at tilføje kolonnen minimumsløn med standardværdi som `1000USD`, skal du bruge nedenstående forespørgsel.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Ovenstående forespørgsel tilføjer en ny kolonne `MINIMUM_WAGE` i tabellen `Employee` og udfylder kolonnen i eksisterende rækker med standardværdien, dvs. `1000`. 

Fordi vi har tilføjet begrænsningen `NOT NULL`.

Hvis du ikke tilføjer `NOT NULL` begrænsningen, vil alle eksisterende rækker være `NULL`, og den angivne `DEFAULT` -værdi vil ikke have nogen virkning. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Alle kolonneværdierne i `MINIMUM_WAGE` vil være `NULL`.

Du skal tilføje `DEFAULT` -værdien, hvis du tilføjer `NOT NULL` -begrænsningen, hvis tabellen ikke er tom. 

Hvis f.eks. tabellen `Employee` ikke er tom, og du tilføjer en ny kolonne med begrænsningen `NOT NULL`, vil der opstå en fejl.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Ovenstående sql server forespørgsel vil kaste nedenstående fejl, mens du tilføjer en ny kolonne til den eksisterende tabel.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Hvis tabellen `Employee` er tom. 

Ovenstående sql server forespørgsel vil tilføje en ny kolonne uden problemer.

## Tilføjelse af en kolonne, der kan annulleres, med standardværdi for eksisterende poster

Hvis du ønsker at tilføje en nullable kolonne med standardværdi for eksisterende poster, skal du bruge `WITH VALUES` i sql-angivelsen.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Ovenstående forespørgsel vil tilføje en nullable kolonne til SQL-servertabellen med standardværdien for eksisterende poster.

I denne tutorial har vi lært at tilføje en kolonne både nullable og non nullable kolonner til sql server tabellen med standardværdi for alle eksisterende poster.

