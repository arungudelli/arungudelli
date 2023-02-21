---
title: "如何在SQL Server中为现有的表添加默认值的列"
description: "在SQL服务器中，要为现有的表添加默认值的列，请使用'ALTER'表'ADD'列名与'NULL/NOT NULL'约束与'DEFALULT'值。"
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

在SQL服务器中，要在一个现有的表中添加一个带有默认值的列，请使用`ALTER` 表`ADD` 列名和`NULL/NOT NULL` 约束和`DEFAULT` 值。

下面的SQL服务器查询语法可以用来在现有的表中添加一个带有默认值的列。

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

让我们通过一个例子来进一步了解它。

## 为现有记录添加一个具有默认值的非空列

考虑到SQL服务器中的一个`Employee` 表，如果我们想添加默认值为`1000USD` 的最低工资列，使用下面的查询。

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

上述查询将在`Employee` 表中添加一个新的列`MINIMUM_WAGE` ，并在现有行中用默认值填充该列，即`1000` 。 

因为我们已经添加了`NOT NULL` 的约束条件。

如果你不添加`NOT NULL` 约束，所有现有的行将是`NULL` ，提供的`DEFAULT` 值将没有影响。 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

所有的`MINIMUM_WAGE` 列的值将是`NULL` 。

如果你在表不是空的情况下添加`NOT NULL` 约束，你需要添加`DEFAULT` 值。 

例如，如果`Employee` 表不是空的，如果你用`NOT NULL` 约束添加一个新的列，就会产生错误。

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

上面的sql server查询在向现有的表添加新的列时将会出现以下错误。

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

如果`Employee` 表是空的。 

上面的sql server查询将添加一个新的列，没有任何问题。

## 为现有的记录添加一个具有默认值的Nullable列

如果你想为现有记录添加一个默认值为空的列，你需要在sql语句中使用`WITH VALUES` 。

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

上面的查询将在sql server表中添加一个对现有记录有默认值的可忽略列。

在本教程中，我们已经学会了在sql server表中添加一个可归零和不可归零的列，并为所有现有记录添加默认值。

