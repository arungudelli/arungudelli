---
title: "Cara enumerate C# enum"
description: " Berbagai cara untuk enumerate C# enum dengan contoh"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enum digunakan secara luas dalam bahasa `C#`. 

Dan ada 4 cara untuk enumerate enum di `C#`. 

1. Menggunakan `C# Enum.GetValues()` di .Net 5 ke atas.
2. Menggunakan `C# Enum.GetValues()` di versi .Net yang lebih lama.
3. Menggunakan `C# Enum.GetNames()` untuk enummembuat nama enum sebagai string.
4. Menggunakan `Linq`

Mari kita lihat sebuah contoh untuk memahaminya lebih lanjut. 

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

Tingkat penebangan `enum` mewakili berbagai jenis tingkat penebangan.

Sekarang kita akan melihat berbagai cara untuk enumerate `C# enum`.

## Menggunakan `C# Enum.GetValues()` Metode umum di .Net 5 &amp; di atas

Jika Anda menggunakan versi terbaru dari `.Net`, yaitu, `.Net 5` dan di atasnya, Anda dapat menggunakan versi generik untuk metode `Enum.GetValues` untuk enumerate file `C# enum`.

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

Dan selanjutnya kita bisa menggunakan pernyataan `for` atau `foreach` untuk mendaftarkan `C# enum` nama. 

Karena larik tersebut berisi tipe `enum` kita perlu mengonversinya menjadi string menggunakan metode `ToString()`.

## Menggunakan `C# Enum.GetValues()` di versi .Net yang lebih lama.

Pada versi lama `.Net` tidak ada metode generik yang tersedia untuk metode `Enum.GetValues()`. 

Anda harus mengoper `typeof()` enum sebagai parameter ke metode `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Dan mengembalikan nilai enum dengan tipe `System.Array` dan selanjutnya kita dapat menggunakan pernyataan `foreach` untuk mengulang `C# enum` nama.

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

## Menggunakan `C# Enum.GetNames()` untuk enummembuat nama enum sebagai string 

`C# Enum.GetValues()` metode mengembalikan array dari tipe enum. 

Itulah mengapa kami mengubah nama enum menjadi string sebelum mencetaknya di konsol.

Dengan menggunakan metode `C# Enum.GetNames()` kita dapat enummembuat nama enum sebagai string, sehingga tidak perlu mengonversinya menjadi string.

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

Pada versi yang lebih lama, kita perlu memasukkan parameter `typeof()` enum .

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

Jadi, jika Anda ingin membuat enumnama sebagai string, kita dapat menggunakan metode `C# Enum.GetNames()`.

## Menggunakan `Linq`

Kita dapat menggunakan metode `Linq forEach` untuk enummembuat C# enum, dengan bantuan metode `Enum.GetValues()` dan `Enum.GetNames()`.

Pada `.Net 5` dan di atasnya gunakan potongan kode di bawah ini.

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

Dalam tutorial ini kita belajar untuk enummembuat enum dalam bahasa C# menggunakan metode `Enum.GetValues()` dan `Enum.GetNames()`.










