---
title: "Kā pievienot kolonnu ar noklusējuma vērtību esošai tabulai SQL serverī"
description: "SQL serverī, lai pievienotu kolonnu ar noklusējuma vērtību esošai tabulai, izmantojiet 'ALTER' tabula 'ADD' kolonnas nosaukums ar 'NULL/NOT NULL' ierobežojumu ar 'DEFAULT' vērtību."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

SQL serverī, lai esošai tabulai pievienotu kolonnu ar noklusējuma vērtību, izmantojiet `ALTER` Tabulas `ADD` kolonnas nosaukumu ar `NULL/NOT NULL` ierobežojumu ar `DEFAULT` vērtību.

Lai esošajā tabulā pievienotu kolonnu ar noklusējuma vērtību, var izmantot tālāk norādīto sql servera vaicājuma sintaksi.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Aplūkosim piemēru, lai to labāk izprastu.

## Nenolicējamas kolonnas pievienošana ar noklusējuma vērtību esošajiem ierakstiem

Aplūkojiet SQL servera tabulu `Employee`, un, ja mēs vēlamies pievienot minimālās algas sleju ar noklusējuma vērtību `1000USD`, izmantojiet tālāk sniegto vaicājumu.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Iepriekš minētais vaicājums pievienos jaunu sleju `MINIMUM_WAGE` tabulā `Employee` un aizpildīs esošo rindu sleju ar noklusējuma vērtību, t. i., `1000`. 

Tā kā mēs esam pievienojuši `NOT NULL` ierobežojumu.

Ja nepievienosiet ierobežojumu `NOT NULL`, visas esošās rindas būs `NULL`, un `DEFAULT` norādītajai vērtībai nebūs nekādas ietekmes. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Visu `MINIMUM_WAGE` kolonnu vērtības būs `NULL`.

Jums ir jāpievieno `DEFAULT` vērtība, ja pievienojat `NOT NULL` ierobežojumu, ja tabula nav tukša. 

Piemēram, ja tabula `Employee` nav tukša un ja jūs pievienojat jaunu kolonnu ar ierobežojumu `NOT NULL`, tiks pieļauta kļūda.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Iepriekš minētais sql servera vaicājums, pievienojot jaunu kolonnu esošajai tabulai, izraisīs šādu kļūdu.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Ja `Employee` tabula ir tukša. 

Iepriekš minētais sql servera vaicājums bez problēmām pievienos jaunu kolonnu.

## Nulējamas kolonnas pievienošana ar noklusējuma vērtību esošajiem ierakstiem

Ja vēlaties pievienot nullei pakļautu kolonnu ar noklusējuma vērtību esošajiem ierakstiem, sql izteikumā jāizmanto `WITH VALUES`.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Iepriekš minētais vaicājums pievienos sql servera tabulai nullable kolonnu ar noklusējuma vērtību esošajiem ierakstiem.

Šajā pamācībā mēs esam iemācījušies pievienot sql servera tabulai gan nullable, gan non nullable kolonnas ar noklusējuma vērtību visiem esošajiem ierakstiem.

