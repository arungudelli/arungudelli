---
title: "Cara mengulang/mencacah enum C#"
description: "Berbagai cara untuk mengulang atau mencacah enum C# dengan contoh"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enum digunakan secara luas dalam bahasa `C#`. 

Dan ada 4 cara untuk mengulang atau mencacah enum di `C#`. 

1. Menggunakan `C# Enum.GetValues()` di .Net 5 ke atas.
2. Menggunakan `C# Enum.GetValues()` di versi .Net yang lebih lama.
3. Menggunakan `C# Enum.GetNames()` untuk mencacah nama enum sebagai string.
4. Menggunakan `Linq`

Mari kita lihat sebuah contoh untuk memahaminya lebih jauh. 

Pertama, kita akan membuat sebuah program C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` mewakili berbagai jenis level penebangan.

Sekarang kita akan melihat berbagai cara untuk menghitung `C# enum`.

## Menggunakan `C# Enum.GetValues()` Metode umum di .Net 5 &amp; di atasnya

Jika Anda menggunakan versi terbaru dari `.Net`, yaitu, `.Net 5` dan di atasnya, Anda dapat menggunakan versi umum untuk metode `Enum.GetValues` untuk mengulang melalui `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Versi generik baru dari `Enum.GetValues` mengembalikan larik nilai enum. 

Dan selanjutnya kita dapat menggunakan pernyataan `for` atau `foreach` untuk mencacah `C# enum`. 

Karena larik berisi tipe `enum`, kita perlu mengubahnya menjadi string menggunakan metode `ToString()`.

## Menggunakan `C# Enum.GetValues()` di versi .Net yang lebih lama.

Pada versi lama `.Net` tidak ada metode generik yang tersedia untuk metode `Enum.GetValues()`. 

Anda harus mengoper enum `typeof()` sebagai parameter ke metode `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Dan mengembalikan nilai enum dengan tipe `System.Array` dan selanjutnya kita bisa menggunakan pernyataan `foreach` untuk mengulang enum C#.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Jika Anda menginginkan hasil `IEnumerable`, kita dapat menggunakan metode `Enum.GetValues()`.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## Menggunakan `C# Enum.GetNames()` untuk mencacah nama enum sebagai string 

`C# Enum.GetValues()` metode mengembalikan larik tipe enum. 

Itulah mengapa kita mengubah nilai enum menjadi string sebelum mencetaknya di konsol.

Dengan menggunakan metode `C# Enum.GetNames()` kita dapat mencacah nama enum sebagai string, sehingga tidak perlu mengonversinya menjadi string.

Jika Anda menggunakan `.Net 5` &amp; di atasnya, Anda dapat menggunakan fungsi generik `C# Enum.GetNames()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Pada versi yang lebih lama, kita perlu mengoper parameter enum `typeof()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Jadi, jika Anda ingin mengulang nama enum sebagai string, kita dapat menggunakan metode `C# Enum.GetNames()`.

## Menggunakan `Linq`

Kita bisa menggunakan metode `Linq forEach` untuk mencacah enum C#, dengan bantuan metode `Enum.GetValues()` dan `Enum.GetNames()`.

Pada `.Net 5` dan yang lebih tinggi, gunakan cuplikan kode di bawah ini.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

Di versi yang lebih lama

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Ringkasan

Pada tutorial ini kita belajar perulangan melalui enum di C# menggunakan metode `Enum.GetValues()` dan `Enum.GetNames()`.










