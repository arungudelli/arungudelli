---
title: "Hinzufügen einer Spalte mit einem Standardwert zu einer bestehenden Tabelle in SQL Server"
description: "Um eine Spalte mit einem Standardwert zu einer bestehenden Tabelle hinzuzufügen, verwenden Sie 'ALTER' Table 'ADD' column name with 'NULL/NOT NULL' constraint with 'DEFAULT' value."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

In SQL Server, Um eine Spalte mit einem Standardwert zu einer bestehenden Tabelle hinzuzufügen, verwenden Sie `ALTER` Tabelle `ADD` Spaltenname mit `NULL/NOT NULL` Einschränkung mit `DEFAULT` Wert.

Die folgende SQL-Server-Abfragesyntax kann verwendet werden, um eine Spalte mit dem Standardwert in die vorhandene Tabelle einzufügen.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Lassen Sie uns ein Beispiel durchgehen, um es besser zu verstehen.

## Hinzufügen einer nicht-nullbaren Spalte mit Standardwert für vorhandene Datensätze

Nehmen wir eine Tabelle `Employee` im SQL Server, und wenn wir die Spalte Mindestlohn mit dem Standardwert `1000USD` hinzufügen möchten, verwenden Sie die folgende Abfrage.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Die obige Abfrage fügt eine neue Spalte `MINIMUM_WAGE` in der Tabelle `Employee` hinzu und füllt die Spalte in den vorhandenen Zeilen mit dem Standardwert, d. h. `1000`. 

Weil wir die Einschränkung `NOT NULL` hinzugefügt haben.

Wenn Sie die Einschränkung `NOT NULL` nicht hinzufügen, werden alle vorhandenen Zeilen `NULL` sein und der Wert `DEFAULT` wird keine Auswirkungen haben. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Alle `MINIMUM_WAGE` Spaltenwerte werden `NULL` sein.

Sie müssen den Wert `DEFAULT` hinzufügen, wenn Sie die Einschränkung `NOT NULL` hinzufügen, wenn die Tabelle nicht leer ist. 

Wenn zum Beispiel die Tabelle `Employee` nicht leer ist und Sie eine neue Spalte mit der Einschränkung `NOT NULL` hinzufügen, wird ein Fehler ausgegeben.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Die obige Sql-Server-Abfrage wird den unten stehenden Fehler beim Hinzufügen einer neuen Spalte zu der vorhandenen Tabelle auslösen.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Wenn die Tabelle `Employee` leer ist. 

Die obige Sql-Server-Abfrage fügt eine neue Spalte ohne Probleme hinzu.

## Hinzufügen einer nullbaren Spalte mit Standardwert für vorhandene Datensätze

Wenn Sie eine löschbare Spalte mit einem Standardwert für bestehende Datensätze hinzufügen möchten, müssen Sie `WITH VALUES` in der SQL-Anweisung verwenden.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Die obige Abfrage fügt der Sql-Server-Tabelle eine löschbare Spalte mit dem Standardwert für vorhandene Datensätze hinzu.

Wenn dieses Tutorial haben wir gelernt, eine Spalte sowohl nullable und nicht nullable Spalten in die Sql-Server-Tabelle mit Standardwert für alle vorhandenen Datensätze hinzufügen.

