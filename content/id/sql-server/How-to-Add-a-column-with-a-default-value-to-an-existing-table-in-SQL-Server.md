---
title: "Cara Menambahkan kolom dengan nilai default ke tabel yang ada di SQL Server"
description: "Di SQL server, Untuk menambahkan kolom dengan nilai default ke tabel yang sudah ada, gunakan 'ALTER' Tabel 'TAMBAH' nama kolom dengan batasan 'NULL / BUKAN NULL' dengan nilai 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Di SQL server, Untuk menambahkan kolom dengan nilai default ke tabel yang sudah ada, gunakan `ALTER` Tabel `ADD` nama kolom dengan batasan `NULL/NOT NULL` dengan nilai `DEFAULT`.

Berikut sintaks query sql server yang dapat digunakan untuk menambahkan kolom dengan nilai default pada tabel yang sudah ada.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Mari kita lihat sebuah contoh untuk memahaminya lebih lanjut.

## Menambahkan kolom Non-Nullable dengan nilai default untuk record yang sudah ada

Perhatikan tabel `Employee` di SQL server, dan jika kita ingin menambahkan kolom upah minimum dengan nilai default sebagai `1000USD`, gunakan query di bawah ini.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Query di atas akan menambahkan kolom baru `MINIMUM_WAGE` pada tabel `Employee` dan mengisi kolom pada baris yang sudah ada dengan nilai default, yaitu `1000`. 

Karena kita telah menambahkan constraint `NOT NULL`.

Jika Anda tidak menambahkan constraint `NOT NULL`, semua baris yang ada akan menjadi `NULL` dan nilai `DEFAULT` yang diberikan tidak akan berpengaruh. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Semua nilai kolom `MINIMUM_WAGE` akan menjadi `NULL`.

Anda perlu menambahkan nilai `DEFAULT` jika Anda menambahkan batasan `NOT NULL` jika tabel tidak kosong. 

Sebagai contoh, jika tabel `Employee` tidak kosong, dan jika Anda menambahkan kolom baru dengan constraint `NOT NULL` maka akan terjadi error.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Query sql server di atas akan melemparkan kesalahan di bawah ini saat menambahkan kolom baru ke tabel yang ada.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Jika tabel `Employee` kosong. 

Kueri sql server di atas akan menambahkan kolom baru tanpa masalah.

## Menambahkan kolom Nullable dengan nilai default untuk record yang sudah ada

Jika Anda ingin menambahkan kolom yang dapat dinullkan dengan nilai default untuk record yang sudah ada, Anda perlu menggunakan `WITH VALUES` di dalam pernyataan sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Query di atas akan menambahkan kolom nullable ke tabel sql server dengan nilai default untuk record yang ada.

Pada tutorial ini kita telah belajar untuk menambahkan sebuah kolom baik itu kolom nullable maupun non nullable pada tabel sql server dengan nilai default untuk semua record yang ada.

