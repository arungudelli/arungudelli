---
title: "Как добавить столбец со значением по умолчанию к существующей таблице в SQL Server"
description: "В SQL server для добавления столбца со значением по умолчанию к существующей таблице используйте 'ALTER' Table 'ADD' column name with 'NULL/NOT NULL' constraint with 'DEFAULT' value."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

В SQL-сервере для добавления столбца со значением по умолчанию в существующую таблицу используйте `ALTER` Таблица `ADD` имя столбца с ограничением `NULL/NOT NULL` со значением `DEFAULT`.

Приведенный ниже синтаксис запроса sql server может быть использован для добавления столбца со значением по умолчанию в существующую таблицу.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Давайте рассмотрим пример, чтобы лучше понять это.

## Добавление не нулевого столбца со значением по умолчанию для существующих записей

Рассмотрим таблицу `Employee` в SQL-сервере, и если мы хотим добавить столбец минимальной заработной платы со значением по умолчанию `1000USD`, используйте следующий запрос.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Приведенный выше запрос добавит новый столбец `MINIMUM_WAGE` в таблицу `Employee` и заполнит столбец в существующих строках значением по умолчанию, т.е. `1000`. 

Поскольку мы добавили ограничение `NOT NULL`.

Если вы не добавите ограничение `NOT NULL`, все существующие строки будут `NULL`, а значение `DEFAULT` не будет иметь никакого влияния. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Все значения столбца `MINIMUM_WAGE` будут `NULL`.

Вам нужно добавить значение `DEFAULT`, если вы добавляете ограничение `NOT NULL`, если таблица не пуста. 

Например, если таблица `Employee` не пуста, и если вы добавите новый столбец с ограничением `NOT NULL`, это приведет к ошибке.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Приведенный выше запрос sql server выдаст следующую ошибку при добавлении нового столбца в существующую таблицу.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Если таблица `Employee` пуста. 

Приведенный выше запрос sql server добавит новый столбец без каких-либо проблем.

## Добавление нулевого столбца со значением по умолчанию для существующих записей

Если вы хотите добавить нулевой столбец со значением по умолчанию для существующих записей, вам необходимо использовать `WITH VALUES` в sql-запросе.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Приведенный выше запрос добавит в таблицу sql server nullable столбец со значением по умолчанию для существующих записей.

В этом учебнике мы научились добавлять столбцы, как нулевые, так и не нулевые, в таблицу sql server со значением по умолчанию для всех существующих записей.

