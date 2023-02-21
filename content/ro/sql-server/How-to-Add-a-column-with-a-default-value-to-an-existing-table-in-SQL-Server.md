---
title: "Cum să adăugați o coloană cu o valoare implicită la o tabelă existentă în SQL Server"
description: "În SQL server, pentru a adăuga o coloană cu o valoare implicită la o tabelă existentă, utilizați 'ALTER' Table 'ADD' numele coloanei cu constrângerea 'NULL/NOT NULL' cu valoarea 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

În SQL Server, pentru a adăuga o coloană cu o valoare implicită la un tabel existent, utilizați `ALTER` Numele coloanei din tabelul `ADD` cu constrângerea `NULL/NOT NULL` și valoarea `DEFAULT`.

Pentru a adăuga o coloană cu valoare implicită în tabelul existent, se poate utiliza sintaxa de interogare SQL Server de mai jos.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Să trecem printr-un exemplu pentru a înțelege mai bine.

## Adăugarea unei coloane Non-Nullable cu valoare implicită pentru înregistrările existente

Luați în considerare o tabelă `Employee` în SQL server și, dacă dorim să adăugăm o coloană de salariu minim cu valoare implicită ca `1000USD`, utilizați interogarea de mai jos.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Interogarea de mai sus va adăuga o nouă coloană `MINIMUM_WAGE` în tabelul `Employee` și va completa coloana din rândurile existente cu valoarea implicită, adică `1000`. 

Deoarece am adăugat constrângerea `NOT NULL`.

Dacă nu adăugați constrângerea `NOT NULL`, toate rândurile existente vor fi `NULL`, iar valoarea `DEFAULT` furnizată nu va avea niciun impact. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Toate valorile coloanei `MINIMUM_WAGE` vor fi `NULL`.

Trebuie să adăugați valoarea `DEFAULT` dacă adăugați constrângerea `NOT NULL` dacă tabelul nu este gol. 

De exemplu, dacă tabelul `Employee` nu este gol și dacă adăugați o nouă coloană cu constrângerea `NOT NULL`, se va produce o eroare.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Interogarea serverului sql de mai sus va genera eroarea de mai jos la adăugarea unei noi coloane în tabelul existent.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Dacă tabelul `Employee` este gol. 

Interogarea SQL Server de mai sus va adăuga o nouă coloană fără probleme.

## Adăugarea unei coloane Nullable cu valoare implicită pentru înregistrările existente

Dacă doriți să adăugați o coloană "nullable" cu valoare implicită pentru înregistrările existente, trebuie să utilizați `WITH VALUES` în declarația sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Interogarea de mai sus va adăuga o coloană "nullable" în tabelul serverului sql cu valoarea implicită pentru înregistrările existente.

În acest tutorial am învățat să adăugăm o coloană atât coloane care nu pot fi anulate, cât și coloane care nu pot fi anulate, în tabelul serverului sql cu o valoare implicită pentru toate înregistrările existente.

