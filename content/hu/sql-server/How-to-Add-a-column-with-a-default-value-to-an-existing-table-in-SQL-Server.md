---
title: "Hogyan adjunk hozzá egy oszlopot alapértelmezett értékkel egy meglévő táblához az SQL Serverben"
description: "Az SQL szerverben egy alapértelmezett értékkel rendelkező oszlop hozzáadásához egy meglévő táblához használja az 'ALTER' táblázat 'ADD' oszlop nevét 'NULL/NOT NULL' korlátozással és 'DEFAULT' értékkel."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Az SQL szerverben egy alapértelmezett értékű oszlop hozzáadásához egy meglévő táblához használja a `ALTER` táblázat `ADD` oszlopnevet `NULL/NOT NULL` korlátozással `DEFAULT` értékkel.

Az alábbi sql server lekérdezési szintaxis használható egy alapértelmezett értékkel rendelkező oszlop hozzáadásához a meglévő táblához.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Nézzünk végig egy példát, hogy jobban megértsük.

## Nem nullázható oszlop hozzáadása alapértelmezett értékkel a meglévő rekordokhoz

Tekintsünk egy `Employee` táblát az SQL szerveren, és ha a minimálbér oszlopot alapértelmezett értékkel szeretnénk hozzáadni `1000USD`, akkor az alábbi lekérdezést használjuk.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

A fenti lekérdezés egy új `MINIMUM_WAGE` oszlopot ad hozzá a `Employee` táblához, és a meglévő sorokban lévő oszlopot az alapértelmezett értékkel, azaz `1000`-vel tölti fel. 

Mivel hozzáadtuk a `NOT NULL` korlátozást.

Ha nem adunk hozzá `NOT NULL` korlátozást, akkor az összes meglévő sor `NULL` lesz, és a megadott `DEFAULT` értéknek nem lesz hatása. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Az összes `MINIMUM_WAGE` oszlop értéke `NULL` lesz.

A `DEFAULT` értéket akkor kell hozzáadni, ha a `NOT NULL` megszorítást adja hozzá, ha a táblázat nem üres. 

Például ha a `Employee` tábla nem üres, és ha új oszlopot ad hozzá a `NOT NULL` korlátozással, hibát fog dobni.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

A fenti sql szerver lekérdezés az alábbi hibát dobja ki, miközben új oszlopot ad hozzá a meglévő táblához.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Ha a `Employee` tábla üres. 

A fenti sql szerver lekérdezés minden probléma nélkül hozzáad egy új oszlopot.

## Nullázható oszlop hozzáadása alapértelmezett értékkel a meglévő rekordokhoz

Ha nullázható oszlopot szeretne hozzáadni alapértelmezett értékkel a meglévő rekordokhoz, akkor a `WITH VALUES` címet kell használnia az sql utasításban.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

A fenti lekérdezés egy nullázható oszlopot ad hozzá az sql szerver táblához a meglévő rekordok alapértelmezett értékével.

Ha ez a bemutató megtanultuk, hogy mind nullázható, mind nem nullázható oszlopot adjunk hozzá az sql szerver táblához alapértelmezett értékkel az összes meglévő rekordhoz.

