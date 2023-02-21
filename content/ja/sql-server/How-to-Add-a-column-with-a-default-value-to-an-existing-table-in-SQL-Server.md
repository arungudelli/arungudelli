---
title: "SQL Serverで既存のテーブルにデフォルト値を持つ列を追加する方法"
description: "SQL Serverでは、既存のテーブルにデフォルト値を持つ列を追加するには、 'ALTER' Table 'ADD' column name with 'NULL/NOT NULL' constraint with 'DEFAULT' valueを使用してください。"
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

SQLサーバーで、既存のテーブルにデフォルト値を持つカラムを追加するには、`ALTER` テーブル`ADD` カラム名、`NULL/NOT NULL` 制約、`DEFAULT` 値を指定します。

以下のSQLサーバーのクエリシンタックスは、既存のテーブルにデフォルト値を持つ列を追加するために使用することができます。

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

例を見て、さらに理解しましょう。

## 既存レコードにデフォルト値を持つNon-Nullableカラムを追加する

SQLサーバの`Employee` テーブルを考えて、我々は`1000USD` 、以下のクエリを使用して、デフォルト値で最低賃金列を追加したい場合。

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

上記のクエリは、`Employee` テーブルに新しい列`MINIMUM_WAGE` を追加し、既存の行の列をデフォルト値、すなわち`1000` で埋めます。 

なぜなら、`NOT NULL` 制約を追加しているからです。

`NOT NULL` 制約を追加しない場合、既存の行はすべて`NULL` になり、提供された`DEFAULT` 値は何の影響も与えません。 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

`MINIMUM_WAGE` 列の値はすべて`NULL` になります。

テーブルが空でない場合、`NOT NULL` 制約を追加すると、`DEFAULT` 値を追加する必要があります。 

例えば、`Employee` テーブルが空でない場合、`NOT NULL` 制約を使用して新しいカラムを追加すると、エラーが発生します。

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

上記のSQLサーバーのクエリは、既存のテーブルに新しいカラムを追加する際に、以下のエラーをスローします。

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

`Employee` テーブルが空である場合。 

上記のsql serverクエリは、問題なく新しいカラムを追加します。

## 既存レコードのデフォルト値を持つNullableカラムの追加

既存のレコードにデフォルト値を持つNullableカラムを追加したい場合、SQL文の中で`WITH VALUES` 。

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

上記のクエリは、既存のレコードのデフォルト値を持つNULL可能なカラムをSQL Serverテーブルに追加します。

このチュートリアルの場合、我々はすべての既存のレコードのデフォルト値でSQL Serverのテーブルにnullableとnon nullable列の両方を追加することを学びました。

