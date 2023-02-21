---
title: "Come aggiungere una colonna con valore predefinito a una tabella esistente in SQL Server"
description: "In SQL server, per aggiungere una colonna con valore predefinito a una tabella esistente, utilizzate il comando 'ALTER' Tabella 'ADD' nome colonna con vincolo 'NULL/NOT NULL' con valore 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

In SQL server, per aggiungere una colonna con valore predefinito a una tabella esistente, utilizzare la tabella `ALTER` Nome colonna `ADD` con vincolo `NULL/NOT NULL` con valore `DEFAULT`.

Per aggiungere una colonna con valore predefinito a una tabella esistente si può utilizzare la seguente sintassi di query sql server.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Vediamo un esempio per capire meglio.

## Aggiunta di una colonna non annullabile con valore predefinito per i record esistenti

Consideriamo una tabella `Employee` in SQL server e se vogliamo aggiungere la colonna salario minimo con il valore predefinito `1000USD`, utilizziamo la seguente query.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

La query di cui sopra aggiungerà una nuova colonna `MINIMUM_WAGE` nella tabella `Employee` e riempirà la colonna nelle righe esistenti con il valore predefinito, cioè `1000`. 

Poiché abbiamo aggiunto il vincolo `NOT NULL`.

Se non si aggiunge il vincolo `NOT NULL`, tutte le righe esistenti saranno `NULL` e il valore `DEFAULT` fornito non avrà alcun impatto. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Tutti i valori della colonna `MINIMUM_WAGE` saranno `NULL`.

È necessario aggiungere il valore `DEFAULT` se si aggiunge il vincolo `NOT NULL` se la tabella non è vuota. 

Per esempio, se la tabella `Employee` non è vuota e si aggiunge una nuova colonna con il vincolo `NOT NULL`, viene generato un errore.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

La query sql server di cui sopra genera il seguente errore durante l'aggiunta di una nuova colonna alla tabella esistente.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Se la tabella `Employee` è vuota. 

La query sql server di cui sopra aggiungerà una nuova colonna senza alcun problema.

## Aggiunta di una colonna Nullable con valore predefinito per i record esistenti

Se si desidera aggiungere una colonna nullable con valore predefinito per i record esistenti, è necessario utilizzare `WITH VALUES` nell'istruzione sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

La query precedente aggiungerà una colonna nullable alla tabella sql server con il valore predefinito per i record esistenti.

In questo tutorial abbiamo imparato ad aggiungere una colonna sia nullable che non nullable alla tabella sql server con il valore predefinito per tutti i record esistenti.

