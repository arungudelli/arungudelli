---
title: "Comment ajouter une colonne avec une valeur par défaut à une table existante dans SQL Server"
description: "Dans SQL Server, pour ajouter une colonne avec une valeur par défaut à une table existante, utilisez 'ALTER' Table 'ADD' nom de colonne avec contrainte 'NULL/NOT NULL' avec valeur 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Dans le serveur SQL, pour ajouter une colonne avec une valeur par défaut à une table existante, utilisez la table `ALTER`. Nom de la colonne `ADD` avec la contrainte `NULL/NOT NULL` et la valeur `DEFAULT`.

La syntaxe de requête SQL Server ci-dessous peut être utilisée pour ajouter une colonne avec une valeur par défaut dans une table existante.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Prenons un exemple pour mieux comprendre.

## Ajout d'une colonne non-nullable avec une valeur par défaut pour les enregistrements existants

Considérons une table `Employee` dans le serveur SQL, et si nous voulons ajouter une colonne de salaire minimum avec une valeur par défaut comme `1000USD`, utilisez la requête ci-dessous.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

La requête ci-dessus ajoutera une nouvelle colonne `MINIMUM_WAGE` dans la table `Employee` et remplira la colonne dans les lignes existantes avec la valeur par défaut, c'est-à-dire `1000`. 

Parce que nous avons ajouté la contrainte `NOT NULL`.

Si vous n'ajoutez pas la contrainte `NOT NULL`, toutes les lignes existantes seront `NULL` et la valeur `DEFAULT` fournie n'aura aucun impact. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Toutes les valeurs de la colonne `MINIMUM_WAGE` seront `NULL`.

Vous devez ajouter la valeur `DEFAULT` si vous ajoutez la contrainte `NOT NULL` si la table n'est pas vide. 

Par exemple, si la table `Employee` n'est pas vide et que vous ajoutez une nouvelle colonne avec la contrainte `NOT NULL`, une erreur se produira.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

La requête sql server ci-dessus lancera l'erreur suivante en ajoutant une nouvelle colonne à la table existante.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Si la table `Employee` est vide. 

La requête sql server ci-dessus ajoutera une nouvelle colonne sans aucun problème.

## Ajout d'une colonne Nullable avec une valeur par défaut pour les enregistrements existants

Si vous voulez ajouter une colonne nullable avec une valeur par défaut pour les enregistrements existants, vous devez utiliser `WITH VALUES` dans la requête sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

La requête ci-dessus ajoutera une colonne nullable à la table du serveur sql avec la valeur par défaut pour les enregistrements existants.

Dans ce tutoriel, nous avons appris à ajouter une colonne nullable et non nullable à la table sql server avec une valeur par défaut pour tous les enregistrements existants.

