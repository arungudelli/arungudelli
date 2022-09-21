
---
title: "Cara Membuat Angka Acak di C#"
description: "Berbagai cara untuk menghasilkan angka acak di C# dengan contoh-contoh sederhana."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Bilangan acak banyak digunakan dalam permainan Digital, Sampling Statistik, Kriptografi, perhitungan dalam fisika statistik, analisis numerik, komunikasi radio dan permainan kasino seperti roda Roulette dll 

Kita dapat **menggunakan kelas `Random` untuk Menghasilkan Angka Acak di C#**.

## Apa itu Kelas `C# Random`?

`C# Random` class  adalah pseudo-random number generator, yaitu sebuah algoritma yang menghasilkan urutan angka yang memenuhi persyaratan statistik tertentu untuk keacakan.

Kelas ini memiliki 5 metode `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` dan `NextSingle()` 

Tergantung pada jenis bilangan yaitu, `int`,`long` dll kita dapat menggunakan metode yang sesuai.

Mari kita lihat contoh-contohnya untuk memahaminya lebih lanjut 

## Hasilkan bilangan bulat acak di C# 

Langkah-langkah untuk menghasilkan bilangan bulat Acak di C# 

1. Instansiasi kelas bilangan acak.
2. Gunakan metode `Random.Next()` untuk mengembalikan bilangan bulat acak antara `Int32.MinValue` dan `Int32.MaxValue`.

```csharp

var randomInteger = new Random();

randomInteger.Next();
randomInteger.Next();
randomInteger.Next();
randomInteger.Next();
randomInteger.Next(); 


/* OUTPUT : 
2027076668
1095111085
535874255
1973884472
430547700
*/
```

### Hasilkan bilangan bulat acak antara nilai minimum dan maksimum

`Random.Next()` memiliki metode overloaded, yang menerima nilai minimum dan maksimum sebagai parameter yang menghasilkan bilangan bulat acak antara nilai yang diberikan.

Untuk menghasilkan bilangan acak antara 100 sampai 1000 gunakan kode di bawah ini

```csharp
Console.WriteLine("Five random integers between 100 and 1000");

for (int counter = 0; counter <= 4; counter++)
    Console.WriteLine("{0}", randomNumber.Next(100, 1000));

/* OUTPUT:
Five random integers between 100 and 1000
904
853
554
290
614
*/
```

## Hasilkan angka panjang acak (Int64) di C# 

Untuk menghasilkan angka panjang acak yaitu, `Int64` di C #, Gunakan metode `Random.NextInt64()` yang mengembalikan angka `Int64` acak antara `Int64.MinValue` dan `Int64.MaxValue`.

```csharp

var RandomInt64 = new Random();

RandomInt64.NextInt64();
RandomInt64.NextInt64();
RandomInt64.NextInt64();
RandomInt64.NextInt64();
RandomInt64.NextInt64(); 


/* OUTPUT : 
5200810282391000059
6501337495320049889
6318562423063201438
3733878081804548122
8421209223603063849
*/
```

### Hasilkan angka panjang acak (Int64) dalam Rentang yang Diberikan

Mirip dengan `Random.Next()`, `Random.NextInt64()` memiliki metode overloaded, yang menerima Range yaitu, nilai minimum dan maksimum sebagai parameter yang mengembalikan angka `Int64` acak di antara mereka.

Untuk menghasilkan angka acak antara 100000 hingga 200000 gunakan kode di bawah ini

```csharp

var RandomInt64 = new Random();


Console.WriteLine("Five random integers between 100000 and 200000");

for (int counter = 0; counter <= 4; counter++)
    Console.WriteLine("{0}", RandomInt64.NextInt64(100000, 200000));

/* OUTPUT:
Five random long Int64 numbers between 100000 and 200000
144220
194475
185075
159433
136542
*/
```

Angka acak yang dihasilkan tidak sepenuhnya acak karena algoritma matematika digunakan untuk memilihnya, tetapi cukup baik untuk sebagian besar kasus dunia nyata.

## Menghindari duplikat saat menghasilkan nomor acak

Jika Anda menginisialisasi lebih dari satu kelas `new Random()` 

Anda mungkin akan mendapatkan duplikat angka acak. (Aplikasi multithreaded)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Jadi lebih baik menginisialisasi hanya satu instance kelas `Random()`, dan menggunakannya di seluruh aplikasi.

```csharp
//Function to generate unique random number using `Random()` class

private static readonly Random randomInstance = new Random();

public static int GenerateRandomNumber(int min, int max)
{
    lock(randomInstance) // synchronize
    {
        return randomInstance.Next(min, max);
    }
}
```
Jika Anda ingin menghasilkan serangkaian angka acak, dalam lingkungan multithreaded gunakan metode di atas.

## Menggunakan kriptografi `C# RandomNumberGenerator`

Jika Anda ingin menghasilkan angka acak yang benar-benar unik, Anda dapat menggunakan kelas `RandomNumberGenerator` yang merupakan bagian dari pustaka `System.Security.Cryptography`.

Kelas ini menghasilkan angka acak yang aman secara kriptografi dan cocok untuk membuat password acak.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Kita juga dapat mengoper range ke metode `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Menggunakan kelas `C# RNGCryptoServiceProvider` 

Kelas ini sudah usang sekarang, Jangan gunakan metode ini.

`RNGCryptoServiceProvider` mengimplementasikan sebuah cryptographic Random Number Generator (RNG) menggunakan implementasi yang disediakan oleh penyedia layanan kriptografi (CSP).

Gunakan kode di bawah ini untuk membuat nomor acak dengan kelas ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Ringkasan

Dalam tutorial ini kita belajar berbagai cara untuk menghasilkan angka acak di C# dengan contoh-contoh sederhana.

















