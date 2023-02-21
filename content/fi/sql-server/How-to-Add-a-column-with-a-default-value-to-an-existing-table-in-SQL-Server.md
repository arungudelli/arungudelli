---
title: "Kuinka lisätä sarake, jolla on oletusarvo, olemassa olevaan taulukkoon SQL Serverissä"
description: "SQL-palvelimessa voit lisätä sarakkeen, jolla on oletusarvo, olemassa olevaan taulukkoon käyttämällä 'ALTER'-taulukkoa 'ADD'-sarakkeen nimeä, jossa on 'NULL/NOT NULL'-rajoitus ja 'DEFAULT'-arvo."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

SQL-palvelimessa voit lisätä olemassa olevaan taulukkoon sarakkeen, jolla on oletusarvo, käyttämällä `ALTER` Taulukko `ADD` sarakkeen nimi ja `NULL/NOT NULL` rajoitus, jolla on `DEFAULT` arvo.

Alla olevaa SQL Server -kyselysyntaksia voidaan käyttää oletusarvolla varustetun sarakkeen lisäämiseen olemassa olevaan taulukkoon.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Käydään läpi esimerkki sen ymmärtämiseksi tarkemmin.

## Ei-nollattavissa olevan sarakkeen lisääminen oletusarvolla olemassa oleville tietueille

Tarkastellaan SQL-palvelimen `Employee` -taulukkoa, ja jos haluamme lisätä vähimmäispalkkasarakkeen, jonka oletusarvo on `1000USD`, käytä alla olevaa kyselyä.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Yllä oleva kysely lisää uuden sarakkeen `MINIMUM_WAGE` tauluun `Employee` ja täyttää sarakkeen olemassa olevilla riveillä oletusarvolla eli `1000`. 

Koska olemme lisänneet `NOT NULL` -rajoituksen.

Jos et lisää `NOT NULL` -rajoitusta, kaikki olemassa olevat rivit ovat `NULL`, eikä annetulla `DEFAULT` -arvolla ole vaikutusta. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Kaikki `MINIMUM_WAGE` -sarakkeen arvot ovat `NULL`.

Sinun on lisättävä `DEFAULT` arvo, jos lisäät `NOT NULL` rajoituksen, jos taulukko ei ole tyhjä. 

Jos esimerkiksi `Employee` -taulukko ei ole tyhjä ja jos lisäät uuden sarakkeen `NOT NULL` -rajoituksella, se aiheuttaa virheen.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Yllä oleva sql-palvelinkysely aiheuttaa alla olevan virheen, kun lisätään uusi sarake olemassa olevaan taulukkoon.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Jos taulukko `Employee` on tyhjä. 

Yllä oleva sql-palvelinkysely lisää uuden sarakkeen ongelmitta.

## Nollattavissa olevan sarakkeen lisääminen oletusarvolla olemassa oleville tietueille

Jos haluat lisätä tyhjennettävän sarakkeen, jolla on oletusarvo olemassa oleville tietueille, sinun on käytettävä `WITH VALUES` sql-lauseessa.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Yllä oleva kysely lisää sql-palvelimen taulukkoon tyhjennettävän sarakkeen, jossa on oletusarvo olemassa oleville tietueille.

Jos tässä opetusohjelmassa olemme oppineet lisäämään sql-palvelimen taulukkoon sekä nollattavia että ei-nollattavia sarakkeita oletusarvolla kaikille olemassa oleville tietueille.

