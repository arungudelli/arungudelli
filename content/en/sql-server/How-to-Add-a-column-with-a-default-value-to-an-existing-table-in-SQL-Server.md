---
title: "How to Add a column with a default value to an existing table in SQL Server"
description: "In SQL server, To add a column with a default value to an existing table use 'ALTER' Table 'ADD' column name with 'NULL/NOT NULL' constraint with 'DEFAULT' value."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

In SQL server, To add a column with a default value to an existing table use `ALTER` Table `ADD` column name with `NULL/NOT NULL` constraint with `DEFAULT` value.

Below sql server query syntax can be used to add a column with the default value in the existing table.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Let's go through an example to understand it further.

## Adding a Non-Nullable column with default value for existing records

Consider an `Employee` table in SQL server, and if we want to add minimum wage column with default value as `1000USD`, use the below query.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

The above query will add a new column `MINIMUM_WAGE` in the `Employee` table and fills the column in existing rows with the default value i.e., `1000`. 

Because we have added `NOT NULL` constraint.

If you don't add `NOT NULL` constraint, all the existing rows will be `NULL` and `DEFAULT` value provided will have no impact. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

All the `MINIMUM_WAGE` column values will be `NULL`.

You need to add `DEFAULT` value if you add `NOT NULL` constraint if the table is not empty. 

For example if the `Employee` table is not empty, and if you add a new column with `NOT NULL` constraint it will throw error.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

The above sql server query will throw the below error while adding new column to the existing table.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

If the `Employee` table is empty. 

The above sql server query will add a new column without any issues.

## Adding a Nullable column with default value for existing records

If you want to add a nullable column with default value for existing records, you need to use `WITH VALUES` in the sql statement.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

The above query will add a nullable column to the sql server table with the default value for existing records.

If this tutorial we have learnt to add a column both nullable and non nullable colums to the sql server table with default value for all the existing records.

