---
title: "Ako pridať stĺpec s predvolenou hodnotou do existujúcej tabuľky v SQL Serveri"
description: "Ak chcete pridať stĺpec s predvolenou hodnotou do existujúcej tabuľky, použite v SQL Serveri funkciu 'ALTER' Tabuľka 'ADD' Názov stĺpca s obmedzením 'NULL/NOT NULL' s hodnotou 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

V SQL serveri na pridanie stĺpca s predvolenou hodnotou do existujúcej tabuľky použite `ALTER` Table `ADD` názov stĺpca s obmedzením `NULL/NOT NULL` s hodnotou `DEFAULT`.

Na pridanie stĺpca s predvolenou hodnotou do existujúcej tabuľky možno použiť nasledujúcu syntax dotazu servera sql.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Prejdime si príklad, aby sme ho lepšie pochopili.

## Pridanie nenulovateľného stĺpca s predvolenou hodnotou pre existujúce záznamy

Uvažujme tabuľku `Employee` v serveri SQL a ak chceme pridať stĺpec minimálnej mzdy s predvolenou hodnotou ako `1000USD`, použite nasledujúci dotaz.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Uvedený dotaz pridá nový stĺpec `MINIMUM_WAGE` do tabuľky `Employee` a vyplní stĺpec v existujúcich riadkoch predvolenou hodnotou, t. j. `1000`. 

Pretože sme pridali obmedzenie `NOT NULL`.

Ak nepridáte obmedzenie `NOT NULL`, všetky existujúce riadky budú `NULL` a zadaná hodnota `DEFAULT` nebude mať žiadny vplyv. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Všetky hodnoty stĺpca `MINIMUM_WAGE` budú `NULL`.

Ak pridáte obmedzenie `NOT NULL`, musíte pridať hodnotu `DEFAULT`, ak tabuľka nie je prázdna. 

Napríklad ak tabuľka `Employee` nie je prázdna a ak pridáte nový stĺpec s obmedzením `NOT NULL`, vyhodí to chybu.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Vyššie uvedený dotaz na server sql pri pridávaní nového stĺpca do existujúcej tabuľky vyhodí nižšie uvedenú chybu.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Ak je tabuľka `Employee` prázdna. 

Vyššie uvedený dotaz na server sql pridá nový stĺpec bez akýchkoľvek problémov.

## Pridanie stĺpca Nullable s predvolenou hodnotou pre existujúce záznamy

Ak chcete pridať nulovateľný stĺpec s predvolenou hodnotou pre existujúce záznamy, musíte v sql príkaze použiť `WITH VALUES`.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Vyššie uvedený dotaz pridá do tabuľky sql servera nulovateľný stĺpec s predvolenou hodnotou pre existujúce záznamy.

V tomto návode sme sa naučili pridať stĺpec nulovateľný aj nenulovateľný do tabuľky sql servera s predvolenou hodnotou pre všetky existujúce záznamy.

