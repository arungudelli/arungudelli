---
title: "Kako dodati stolpec s privzeto vrednostjo v obstoječo tabelo v strežniku SQL Server"
description: "V strežniku SQL Server za dodajanje stolpca s privzeto vrednostjo v obstoječo tabelo uporabite 'ALTER' Tabela 'ADD' Ime stolpca z omejitvijo 'NULL/NOT NULL' z vrednostjo 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

V strežniku SQL Server za dodajanje stolpca s privzeto vrednostjo v obstoječo tabelo uporabite `ALTER` tabelo `ADD` ime stolpca z omejitvijo `NULL/NOT NULL` z vrednostjo `DEFAULT`.

Za dodajanje stolpca s privzeto vrednostjo v obstoječo tabelo lahko uporabite spodnjo sintakso poizvedbe strežnika sql.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Za boljše razumevanje si oglejmo primer.

## Dodajanje stolpca, ki ga ni mogoče izničiti, s privzeto vrednostjo za obstoječe zapise

Razmislite o tabeli `Employee` v strežniku SQL, in če želimo dodati stolpec minimalne plače s privzeto vrednostjo kot `1000USD`, uporabite spodnjo poizvedbo.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Zgornja poizvedba bo v tabelo `Employee` dodala nov stolpec `MINIMUM_WAGE` in stolpec v obstoječih vrsticah zapolnila s privzeto vrednostjo, tj. `1000`. 

Ker smo dodali omejitev `NOT NULL`.

Če ne dodate omejitve `NOT NULL`, bodo vse obstoječe vrstice `NULL` in podana vrednost `DEFAULT` ne bo imela nobenega vpliva. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Vse vrednosti stolpca `MINIMUM_WAGE` bodo `NULL`.

Če dodate omejitev `NOT NULL`, morate dodati vrednost `DEFAULT`, če tabela ni prazna. 

Na primer, če tabela `Employee` ni prazna in če dodate nov stolpec z omejitvijo `NOT NULL`, se bo vrgla napaka.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Zgornja poizvedba strežnika sql bo med dodajanjem novega stolpca v obstoječo tabelo vrgla spodnjo napako.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Če je tabela `Employee` prazna. 

Zgornja poizvedba za strežnik sql bo brez težav dodala nov stolpec.

## Dodajanje stolpca, ki ga je mogoče izničiti, s privzeto vrednostjo za obstoječe zapise

Če želite dodati ničelni stolpec s privzeto vrednostjo za obstoječe zapise, morate v izjavi sql uporabiti `WITH VALUES`.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Zgornja poizvedba bo v tabelo strežnika sql dodala stolpec, ki ga je mogoče izničiti, s privzeto vrednostjo za obstoječe zapise.

V tem učbeniku smo se naučili, kako v tabelo strežnika sql dodati stolpec, ki ga je mogoče izničiti in ga ni mogoče izničiti, s privzeto vrednostjo za vse obstoječe zapise.

