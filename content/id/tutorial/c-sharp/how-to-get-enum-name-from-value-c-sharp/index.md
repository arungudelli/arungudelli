
+++
title="Cara mendapatkan nama enum dari nilai di C#"
summary="Ada Dua cara Untuk mendapatkan nama enum dari nilai di C# 1. Gunakan C# `Enum.GetName()` dan berikan nilai enum sebagai parameter untuk mendapatkan nama. 2. Mengkonversi nilai enum ke anggota enumerasi menggunakan casting dan kemudian gunakan metode `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Salah satu kasus penggunaan enum yang populer adalah untuk mendapatkan nama enum dari nilainya.

Pertimbangkan contoh dunia nyata, umumnya kita akan menyimpan nilai enum dalam basis data. yaitu, kita hanya akan menyimpan nilai integer 

Dan setelah membaca nilai enum dari data base, kita harus mengubahnya kembali ke nama enum.

Ada **dua cara untuk mendapatkan nama enum dari nilai di C#** 

{{%toc%}}

## Solusi 1: Menggunakan `Enum.GetName()`

C # `Enum.GetName()` fungsi mengambil dua parameter enum jenis dan nilai dan mengembalikan enum nama.

Ambil contoh `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Sekarang kita akan mengoper nilai enum ke `Enum.GetName()` untuk mendapatkan nama enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Jika Anda menggunakan versi C# `.Net 6`, Anda dapat mengoper hanya nilai enum (cast ke enum) ke metode `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Solusi 2: Menggunakan pengecoran tipe

Cara lain adalah dengan, Mengkonversi nilai enum ke anggota enumerasi menggunakan casting dan kemudian menggunakan metode `ToString()`.

Ini adalah cara sederhana yang tidak menggunakan fungsi bawaan `C# Enum`.

Pertama-tama konversikan nilai enum ke anggota erasi enumdan kemudian gunakan metode `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Ringkasan

Dalam tutorial ini kita belajar berbagai cara untuk mendapatkan nilai nama enum di c# 

1. Dengan melewatkan enum tipe dan parameter nilai ke metode `Enum.GetName()` 
2. Dan dengan menggunakan type casting ke tipe enum yang sesuai 
