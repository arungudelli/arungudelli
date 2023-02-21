---
title: "Como adicionar uma coluna com um valor por defeito a uma tabela existente no SQL Server"
description: "No SQL Server, Para adicionar uma coluna com um valor por defeito a uma tabela existente use o nome da coluna 'ALTER' Tabela 'ADD' com a restrição 'NULL/NOT NULL' com o valor 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

No servidor SQL, Para adicionar uma coluna com um valor por defeito a uma tabela existente, utilizar `ALTER` Tabela `ADD` nome da coluna com o constrangimento `NULL/NOT NULL` com o valor `DEFAULT`.

Abaixo da sintaxe de consulta do servidor sql pode ser usada para adicionar uma coluna com o valor padrão na tabela existente.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Passemos por um exemplo para o compreender melhor.

## Acréscimo de uma coluna Não-Nulável com valor por defeito para registos existentes

Considere uma tabela `Employee` no servidor SQL, e se quisermos adicionar uma coluna de salário mínimo com valor por defeito como `1000USD`, utilize a consulta abaixo.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

A consulta acima referida acrescentará uma nova coluna `MINIMUM_WAGE` na tabela `Employee` e preencherá a coluna nas linhas existentes com o valor por defeito, ou seja, `1000`. 

Porque acrescentámos `NOT NULL` constrangimento.

Se não adicionar `NOT NULL`, todas as linhas existentes serão `NULL` e o valor `DEFAULT` fornecido não terá qualquer impacto. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Todos os valores da coluna `MINIMUM_WAGE` serão `NULL`.

É necessário acrescentar o valor `DEFAULT` se acrescentar a restrição `NOT NULL` se a tabela não estiver vazia. 

Por exemplo, se a tabela `Employee` não estiver vazia, e se adicionar uma nova coluna com o constrangimento `NOT NULL`, irá lançar um erro.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

A consulta do servidor sql acima irá lançar o erro abaixo enquanto se adiciona uma nova coluna à tabela existente.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Se a tabela `Employee` estiver vazia. 

A consulta do servidor sql acima referida acrescentará uma nova coluna sem qualquer problema.

## Acrescentar uma coluna Nullable com valor por defeito para registos existentes

Se quiser adicionar uma coluna nula com valor por defeito para registos existentes, terá de utilizar `WITH VALUES` na declaração sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

A consulta acima referida adicionará uma coluna nula à tabela do servidor sql com o valor por defeito para os registos existentes.

Se este tutorial aprendemos a adicionar uma coluna de colunas tanto nulas como não nulas à tabela do servidor sql com valor por defeito para todos os registos existentes.

