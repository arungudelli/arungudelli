---
title: "Så här lägger du till en kolumn med ett standardvärde till en befintlig tabell i SQL Server"
description: "Om du vill lägga till en kolumn med ett standardvärde till en befintlig tabell använder du ALTER Table, ADD, kolumnnamn med begränsningen NULL/NOT NULL och DEFAULT-värdet i SQL Server."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Om du vill lägga till en kolumn med ett standardvärde i en befintlig tabell i SQL Server använder du `ALTER` Table `ADD` column name with `NULL/NOT NULL` constraint with `DEFAULT` value.

Nedanstående syntax för SQL-serverfrågor kan användas för att lägga till en kolumn med standardvärde i en befintlig tabell.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Låt oss gå igenom ett exempel för att förstå det ytterligare.

## Lägga till en kolumn som inte kan nollställas med standardvärde för befintliga poster

Tänk på en tabell `Employee` i SQL Server, och om vi vill lägga till kolumnen minimilön med standardvärdet `1000USD`, använd nedanstående fråga.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Ovanstående fråga lägger till en ny kolumn `MINIMUM_WAGE` i tabellen `Employee` och fyller kolumnen i befintliga rader med standardvärdet, dvs. `1000`. 

Eftersom vi har lagt till begränsningen `NOT NULL`.

Om du inte lägger till begränsningen `NOT NULL` kommer alla befintliga rader att vara `NULL` och det angivna värdet `DEFAULT` har ingen inverkan. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Alla kolumnvärden i `MINIMUM_WAGE` kommer att vara `NULL`.

Du måste lägga till `DEFAULT` -värdet om du lägger till `NOT NULL` -begränsningen om tabellen inte är tom. 

Om t.ex. tabellen `Employee` inte är tom och du lägger till en ny kolumn med begränsningen `NOT NULL` kommer det att uppstå ett fel.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Ovanstående sql-serverfråga ger nedanstående fel när du lägger till en ny kolumn i den befintliga tabellen.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Om tabellen `Employee` är tom. 

Ovanstående sql-serverfråga lägger till en ny kolumn utan problem.

## Lägga till en kolumn som kan upphävas med standardvärde för befintliga poster

Om du vill lägga till en kolumn som inte kan ogiltigförklaras med standardvärde för befintliga poster måste du använda `WITH VALUES` i sql-utdraget.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Ovanstående fråga kommer att lägga till en kolumn som kan upphävas i SQL-serverns tabell med standardvärdet för befintliga poster.

I den här handledningen har vi lärt oss att lägga till en kolumn, både nullable och non nullable, i SQL-serverns tabell med ett standardvärde för alla befintliga poster.

