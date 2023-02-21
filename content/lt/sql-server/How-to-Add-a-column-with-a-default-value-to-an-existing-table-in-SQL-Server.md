---
title: "Kaip į esamą lentelę pridėti stulpelį su numatytąja reikšme SQL serveryje"
description: "Norėdami į esamą lentelę pridėti stulpelį su numatytąja reikšme, SQL serveryje naudokite 'ALTER' lentelę 'ADD' stulpelio pavadinimą su apribojimu 'NULL/NOT NULL' ir reikšme 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

SQL serveryje norėdami į esamą lentelę įtraukti stulpelį su numatytąja reikšme, naudokite `ALTER` lentelę `ADD` stulpelio pavadinimą su `NULL/NOT NULL` apribojimu ir `DEFAULT` reikšme.

Toliau pateikta SQL serverio užklausos sintaksė gali būti naudojama norint į esamą lentelę įtraukti stulpelį su numatytąja reikšme.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Kad geriau suprastumėte, panagrinėkime pavyzdį.

## Nenulinio stulpelio su numatytąja reikšme pridėjimas esamiems įrašams

Panagrinėkime `Employee` lentelę SQL serveryje, ir jei norime pridėti minimalaus darbo užmokesčio stulpelį su numatytąja reikšme `1000USD`, naudokite toliau pateiktą užklausą.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Pateikta užklausa į `Employee` lentelę pridės naują stulpelį `MINIMUM_WAGE` ir užpildys esamų eilučių stulpelį numatytąja reikšme, t. y. `1000`. 

Kadangi pridėjome `NOT NULL` apribojimą.

Jei nepridėsite `NOT NULL` apribojimo, visos esamos eilutės bus `NULL`, o pateikta `DEFAULT` reikšmė neturės jokios įtakos. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Visų `MINIMUM_WAGE` stulpelių reikšmės bus `NULL`.

Jei pridedate `NOT NULL` apribojimą, jei lentelė nėra tuščia, turite pridėti `DEFAULT` reikšmę. 

Pavyzdžiui, jei `Employee` lentelė nėra tuščia ir jei pridėsite naują stulpelį su `NOT NULL` apribojimu, bus išmesta klaida.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Pridedant naują stulpelį į esamą lentelę, aukščiau pateikta sql serverio užklausa iškels toliau nurodytą klaidą.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Jei `Employee` lentelė yra tuščia. 

Pateikta sql serverio užklausa be jokių problemų pridės naują stulpelį.

## Nulinio stulpelio su numatytąja reikšme pridėjimas esamiems įrašams

Jei norite pridėti nulinį stulpelį su numatytoji reikšme esamiems įrašams, sql užklausoje turite naudoti `WITH VALUES`.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Pateikta užklausa į sql serverio lentelę pridės nullable stulpelį su numatytąja reikšme esamiems įrašams.

Šioje pamokoje išmokome į sql serverio lentelę pridėti nulinį ir nenulinį stulpelį su numatytąja reikšme visiems esamiems įrašams.

