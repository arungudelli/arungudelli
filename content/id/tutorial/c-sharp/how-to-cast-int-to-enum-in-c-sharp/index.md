+++
title   ="2 cara untuk mengkonversi/mengubah int menjadi enum di C#"
summary ="Ada 2 cara untuk mengubah int menjadi enum di C# 1. Menggunakan casting tipe eksplisit C#. 2. 2. Menggunakan metode Enum.ToObject()."

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Ada 2 cara untuk mengubah atau meng-cast `int` ke `enum` di C#

1. Menggunakan pengecoran tipe eksplisit C#.
2. Menggunakan metode `Enum.ToObject()` 

{{%toc%}}

## Solusi 1: Menggunakan pengecoran tipe eksplisit C#

Cara sederhana untuk mengonversi `int` ke `enum` di C# adalah dengan menggunakan pengecoran tipe eksplisit.

Mari kita lihat sebuah contoh untuk memahaminya lebih lanjut.

Kita memiliki sebuah `enum` bernama `LogLevel`, yang merepresentasikan berbagai tingkat penebangan.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Pengecoran eksplisit dilakukan dengan menempatkan `enum` dalam tanda kurung di depan nilai `int`.

Tetapi ada masalah dengan **C# di atas `int` untuk `enum` konversi**.

Bagaimana jika nilai `int` tidak ada dalam variabel C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Ini tidak akan melemparkan pengecualian apa pun.

Jadi, lebih baik untuk memeriksa apakah nilai `int` ada di `C# Enum` sebelum meng-cast-nya ke bilangan bulat.

## Memeriksa apakah sebuah bilangan bulat ada atau tidak dalam `C# enum` variabel

Untuk mendapatkan semua nilai integer dalam `C# Enum` kita dapat menggunakan metode `Enum.GetValues`.

Ubahlah menjadi list `C#`, sehingga kita dapat menggunakan metode `list.Contains()` untuk memeriksa apakah bilangan bulat yang diberikan ada dalam `enum` variabel.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Kita dapat menggunakan metode `Enum.IsDefined()` untuk memeriksa apakah nilai integer yang dikonversi ada dalam variabel `enum` yang diberikan.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solusi 2: Gunakan metode `Enum.ToObject()` 

Kita dapat menggunakan metode `C# Enum.ToObject()`, mengubah nilai `int` menjadi `enum` dalam bahasa C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





