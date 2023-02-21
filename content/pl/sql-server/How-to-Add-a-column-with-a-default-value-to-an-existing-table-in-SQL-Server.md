---
title: "Jak dodać kolumnę z wartością domyślną do istniejącej tabeli w SQL Server"
description: "W SQL server, Aby dodać kolumnę z wartością domyślną do istniejącej tabeli użyj 'ALTER' Table 'ADD' nazwa kolumny z ograniczeniem 'NULL/NOT NULL' z wartością 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

W SQL Server, aby dodać kolumnę z wartością domyślną do istniejącej tabeli użyj `ALTER` Tabela `ADD` nazwa kolumny z `NULL/NOT NULL` ograniczenie z `DEFAULT` wartość.

Poniżej składnia zapytania serwera sql może być użyta do dodania kolumny z wartością domyślną w istniejącej tabeli.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Przejdźmy przez przykład, aby zrozumieć to dalej.

## Dodanie kolumny Non-Nullable z wartością domyślną dla istniejących rekordów

Rozważmy tabelę `Employee` w serwerze SQL, i jeśli chcemy dodać kolumnę płacy minimalnej z wartością domyślną jako `1000USD`, użyj poniższego zapytania.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Powyższe zapytanie doda nową kolumnę `MINIMUM_WAGE` w tabeli `Employee` i wypełni kolumnę w istniejących wierszach wartością domyślną tj. `1000`. 

Ponieważ dodaliśmy ograniczenie `NOT NULL`.

Jeśli nie dodamy ograniczenia `NOT NULL`, wszystkie istniejące wiersze będą miały wartość `NULL`, a podana wartość `DEFAULT` nie będzie miała żadnego wpływu. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Wszystkie wartości kolumny `MINIMUM_WAGE` będą miały wartość `NULL`.

Musisz dodać wartość `DEFAULT` jeśli dodajesz ograniczenie `NOT NULL` jeśli tabela nie jest pusta. 

Na przykład, jeśli tabela `Employee` nie jest pusta, a jeśli dodasz nową kolumnę z ograniczeniem `NOT NULL`, wyrzuci błąd.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Powyższe zapytanie do serwera sql wyrzuci poniższy błąd podczas dodawania nowej kolumny do istniejącej tabeli.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Jeśli tabela `Employee` jest pusta. 

Powyższe zapytanie do serwera sql doda nową kolumnę bez żadnych problemów.

## Dodanie kolumny Nullable z wartością domyślną dla istniejących rekordów

Jeśli chcesz dodać kolumnę nullable z wartością domyślną dla istniejących rekordów, musisz użyć `WITH VALUES` w instrukcji sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Powyższe zapytanie doda kolumnę nullable do tabeli serwera sql z wartością domyślną dla istniejących rekordów.

Jeśli w tym tutorialu nauczyliśmy się dodawać kolumnę zarówno nullable jak i non nullable colums do tabeli serwera sql z wartością domyślną dla wszystkich istniejących rekordów.

