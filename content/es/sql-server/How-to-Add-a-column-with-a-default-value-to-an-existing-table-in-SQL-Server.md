---
title: "Como Añadir una columna con un valor por defecto a una tabla existente en SQL Server"
description: "En SQL server, Para añadir una columna con un valor por defecto a una tabla existente use 'ALTER' Tabla 'ADD' nombre de columna con 'NULL/NOT NULL' restricción con 'DEFAULT' valor."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

En SQL Server, para añadir una columna con un valor por defecto a una tabla existente utilice `ALTER` Tabla `ADD` nombre de la columna con `NULL/NOT NULL` restricción con `DEFAULT` valor.

A continuación la sintaxis de consulta sql server se puede utilizar para agregar una columna con el valor predeterminado en la tabla existente.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Veamos un ejemplo para entenderlo mejor.

## Añadir una columna Non-Nullable con valor por defecto para los registros existentes

Consideremos una tabla `Employee` en SQL server, y si queremos añadir la columna de salario mínimo con valor por defecto como `1000USD`, utilice la siguiente consulta.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

La consulta anterior añadirá una nueva columna `MINIMUM_WAGE` en la tabla `Employee` y rellena la columna en las filas existentes con el valor por defecto es decir, `1000`. 

Porque hemos añadido la restricción `NOT NULL`.

Si no se añade la restricción `NOT NULL`, todas las filas existentes serán `NULL` y el valor `DEFAULT` proporcionado no tendrá ningún impacto. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Todos los valores de la columna `MINIMUM_WAGE` serán `NULL`.

Debe añadir el valor `DEFAULT` si añade la restricción `NOT NULL` si la tabla no está vacía. 

Por ejemplo, si la tabla `Employee` no está vacía y añade una nueva columna con la restricción `NOT NULL`, se producirá un error.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

La consulta sql server anterior arrojará el siguiente error al añadir una nueva columna a la tabla existente.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Si la tabla `Employee` está vacía. 

La consulta sql server anterior añadirá una nueva columna sin ningún problema.

## Añadir una columna Nullable con valor por defecto para registros existentes

Si desea añadir una columna anulable con valor por defecto para los registros existentes, debe utilizar `WITH VALUES` en la sentencia sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

La consulta anterior añadirá una columna anulable a la tabla sql server con el valor predeterminado para los registros existentes.

Si este tutorial hemos aprendido a añadir una columna tanto nullable y no nullable colums a la tabla sql server con valor por defecto para todos los registros existentes.

