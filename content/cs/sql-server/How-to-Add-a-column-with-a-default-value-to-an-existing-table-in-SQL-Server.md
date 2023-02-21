---
title: "Jak přidat sloupec s výchozí hodnotou do existující tabulky v SQL Serveru"
description: "Chcete-li přidat sloupec s výchozí hodnotou do existující tabulky, použijte v SQL Serveru příkaz 'ALTER' Table 'ADD' column name with 'NULL/NOT NULL' constraint with 'DEFAULT' value."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

V SQL serveru Chcete-li přidat sloupec s výchozí hodnotou do existující tabulky, použijte tabulku `ALTER` Název sloupce `ADD` s omezením `NULL/NOT NULL` s hodnotou `DEFAULT`.

Níže uvedenou syntaxi dotazu serveru sql lze použít k přidání sloupce s výchozí hodnotou do existující tabulky.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Projděme si příklad, abychom mu lépe porozuměli.

## Přidání nenulovatelného sloupce s výchozí hodnotou pro existující záznamy

Uvažujme tabulku `Employee` v serveru SQL, a pokud chceme přidat sloupec minimální mzda s výchozí hodnotou jako `1000USD`, použijte následující dotaz.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Výše uvedený dotaz přidá do tabulky `Employee` nový sloupec `MINIMUM_WAGE` a sloupec v existujících řádcích vyplní výchozí hodnotou, tj. `1000`. 

Protože jsme přidali omezení `NOT NULL`.

Pokud omezení `NOT NULL` nepřidáte, všechny existující řádky budou `NULL` a zadaná hodnota `DEFAULT` nebude mít žádný vliv. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Všechny hodnoty sloupce `MINIMUM_WAGE` budou mít hodnotu `NULL`.

Pokud přidáte omezení `NOT NULL`, musíte přidat hodnotu `DEFAULT`, pokud tabulka není prázdná. 

Například pokud tabulka `Employee` není prázdná a pokud přidáte nový sloupec s omezením `NOT NULL`, vyhodí to chybu.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Výše uvedený dotaz na server sql při přidávání nového sloupce do existující tabulky vyhodí níže uvedenou chybu.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Pokud je tabulka `Employee` prázdná. 

Výše uvedený dotaz na server sql přidá nový sloupec bez problémů.

## Přidání sloupce Nullable s výchozí hodnotou pro existující záznamy

Pokud chcete přidat nulovatelný sloupec s výchozí hodnotou pro existující záznamy, musíte v příkazu sql použít adresu `WITH VALUES`.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Výše uvedený dotaz přidá do tabulky sql serveru nulovatelný sloupec s výchozí hodnotou pro existující záznamy.

V tomto návodu jsme se naučili přidat do tabulky sql serveru sloupec nulovatelný i nenulovatelný s výchozí hodnotou pro všechny existující záznamy.

