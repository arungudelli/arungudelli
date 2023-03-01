---
title: "Cara Mengatur nilai default untuk properti C# atau C# properti yang diimplementasikan secara otomatis"
description: "Dalam tutorial ini kita akan mempelajari 4 cara berbeda untuk mengatur nilai default ke properti C# menggunakan contoh sederhana"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# properti atau properti yang diimplementasikan secara otomatis banyak digunakan di kelas kita sebagai pengganti field, yaitu variabel.  

Properti yang diimplementasikan secara otomatis diperkenalkan di C# 3.0.

Dalam tutorial ini kita akan mempelajari 4 cara berbeda untuk mengatur nilai default ke properti C# menggunakan contoh sederhana.

1. Menggunakan Inisialisasi Properti Otomatis di C# 6
2. Menetapkan nilai default dalam konstruktor
3. Menggunakan C# Pengatur Properti
4. Menggunakan `DefaultValue` Atribut &amp;&amp; Penyetel Properti

Kita dapat mengasumsikan nilai default sebagai nilai awal properti di C#.

## Metode 1: Menggunakan Inisialisasi Properti Otomatis di C# 6

Dalam C# 6 kita dapat mendeklarasikan properti yang diimplementasikan secara otomatis dan menetapkan nilai default dalam satu baris deklarasi.

Sintaksnya adalah

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Secara default properti string akan memiliki nilai `null`, Dengan menggunakan C# 6 deklarasi in-line, Kami menetapkan nilai default sebagai string kosong. 

## Metode 2: Menetapkan nilai default dalam konstruktor

Pada versi yang lebih lama dari C#, C# 5 dan di bawahnya, merupakan praktik yang baik untuk menetapkan nilai default dari properti C# di konstruktor kelas.

```csharp
class Product 
{
    public string Name { get; set; }
    public Product()
    {
        Name = "";
    }
}
```

## Metode 3: Menggunakan C# Pengatur Properti 

Kita dapat menggunakan pengatur properti C# untuk menetapkan nilai default ke properti yang diimplementasikan secara otomatis.

```csharp
class Product 
{
    private string _name = "";
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

## metode 4: Menggunakan `DefaultValue` Atribut &amp;&amp; Pengatur Properti

Pada contoh di atas, kita telah membuat variabel privat dan menetapkan nilai default. 

Selain itu, kita dapat menggunakan atribut `DefaultValue` untuk menetapkan nilai default.

```csharp
class Product 
{
    private string _name;

    [DefaultValue("")]
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

Ingat ** Atribut`DefaultValue` hanya berfungsi dengan pengatur properti.** 

Kode di bawah ini tidak akan menetapkan nilai default ke properti. Nilai defaultnya tetap `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Jika Anda menggunakan atribut `DefaultValue`, Anda harus menggunakan pengatur properti.


## Ringkasan

Jika Anda menggunakan C# 6 gunakan deklarasi in-line untuk menetapkan nilai default ke properti C#. Jika tidak, tetapkan nilai default di konstruktor. 








