---
title: "SQL Server'da mevcut bir tabloya varsayılan değere sahip bir sütun nasıl eklenir"
description: "SQL server'da, mevcut bir tabloya varsayılan değere sahip bir sütun eklemek için 'ALTER' Tablosu 'ADD' sütun adını 'DEFAULT' değeri ile 'NULL/NOT NULL' kısıtlaması ile kullanın."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

SQL server'da, mevcut bir tabloya varsayılan değere sahip bir sütun eklemek için `ALTER` Tablo `ADD` sütun adı ile `NULL/NOT NULL` kısıtlamasını ve `DEFAULT` değerini kullanın.

Mevcut tabloya varsayılan değere sahip bir sütun eklemek için aşağıdaki sql server sorgu sözdizimi kullanılabilir.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Bunu daha iyi anlamak için bir örnek üzerinden gidelim.

## Mevcut kayıtlar için varsayılan değere sahip Nullable olmayan bir sütun ekleme

SQL server'da bir `Employee` tablosu düşünün ve varsayılan değeri `1000USD` olan asgari ücret sütunu eklemek istiyorsak aşağıdaki sorguyu kullanın.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Yukarıdaki sorgu `Employee` tablosuna yeni bir `MINIMUM_WAGE` sütunu ekleyecek ve mevcut satırlardaki sütunu varsayılan değerle, yani `1000` ile dolduracaktır. 

Çünkü `NOT NULL` kısıtlamasını ekledik.

 `NOT NULL` kısıtlamasını eklemezseniz, mevcut tüm satırlar `NULL` olacaktır ve sağlanan `DEFAULT` değerinin hiçbir etkisi olmayacaktır. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Tüm `MINIMUM_WAGE` sütun değerleri `NULL` olacaktır.

Tablo boş değilse `NOT NULL` kısıtını eklerseniz `DEFAULT` değerini eklemeniz gerekir. 

Örneğin, `Employee` tablosu boş değilse ve `NOT NULL` kısıtlaması ile yeni bir sütun eklerseniz hata verir.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Yukarıdaki sql server sorgusu, mevcut tabloya yeni sütun eklerken aşağıdaki hatayı verecektir.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

 `Employee` tablosu boşsa. 

Yukarıdaki sql server sorgusu herhangi bir sorun olmadan yeni bir sütun ekleyecektir.

## Mevcut kayıtlar için varsayılan değere sahip Nullable sütun ekleme

Mevcut kayıtlar için varsayılan değere sahip nullable bir sütun eklemek istiyorsanız, sql deyiminde `WITH VALUES` adresini kullanmanız gerekir.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Yukarıdaki sorgu, sql server tablosuna mevcut kayıtlar için varsayılan değere sahip nullable bir sütun ekleyecektir.

Bu eğitimde sql server tablosuna hem nullable hem de nullable olmayan sütunları mevcut tüm kayıtlar için varsayılan değerle eklemeyi öğrendik.

