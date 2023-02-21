---
title: "Как да добавите колона със стойност по подразбиране към съществуваща таблица в SQL Server"
description: "В SQL Server, за да добавите колона със стойност по подразбиране към съществуваща таблица, използвайте 'ALTER' Таблица 'ADD' Име на колона с ограничение 'NULL/NOT NULL' със стойност 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

В SQL сървър, За да добавите колона със стойност по подразбиране към съществуваща таблица, използвайте `ALTER` Таблица `ADD` Име на колона с ограничение `NULL/NOT NULL` със стойност `DEFAULT`.

За добавяне на колона със стойност по подразбиране в съществуваща таблица може да се използва синтаксисът на заявката по-долу в sql server.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Нека разгледаме един пример, за да го разберем по-добре.

## Добавяне на колона, която не се нулира, със стойност по подразбиране за съществуващи записи

Разгледайте таблица `Employee` в SQL сървър и ако искаме да добавим колона за минимална работна заплата със стойност по подразбиране като `1000USD`, използвайте следната заявка.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Горната заявка ще добави нова колона `MINIMUM_WAGE` в таблицата `Employee` и ще запълни колоната в съществуващите редове със стойността по подразбиране, т.е. `1000`. 

Тъй като сме добавили ограничението `NOT NULL`.

Ако не добавите ограничението `NOT NULL`, всички съществуващи редове ще бъдат `NULL` и предоставената стойност `DEFAULT` няма да окаже влияние. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Всички стойности на колоната `MINIMUM_WAGE` ще бъдат `NULL`.

Трябва да добавите стойност `DEFAULT`, ако добавите ограничение `NOT NULL`, ако таблицата не е празна. 

Например, ако таблицата `Employee` не е празна и ако добавите нова колона с ограничение `NOT NULL`, ще се получи грешка.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Горната заявка на sql сървъра ще хвърли следната грешка, докато добавяте нова колона към съществуващата таблица.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Ако таблицата `Employee` е празна. 

Горната заявка за sql сървър ще добави нова колона без никакви проблеми.

## Добавяне на нулируема колона със стойност по подразбиране за съществуващи записи

Ако искате да добавите нулируема колона със стойност по подразбиране за съществуващи записи, трябва да използвате `WITH VALUES` в sql заявката.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Горната заявка ще добави нулируема колона към таблицата на sql сървъра със стойност по подразбиране за съществуващите записи.

В този урок се научихме да добавяме колони, както нулируеми, така и ненулируеми, към таблицата на sql server със стойност по подразбиране за всички съществуващи записи.

