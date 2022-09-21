
---
title: "C#'ta Rastgele Sayı Üretme"
description: "Basit örneklerle C#'ta rastgele sayı üretmenin farklı yolları."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Rastgele sayılar Dijital oyunlarda, İstatistiksel Örneklemede, Kriptografide, istatistiksel fizik hesaplamalarında, sayısal analizde, Radyo iletişiminde ve Rulet tekerleği gibi kumarhane oyunlarında yaygın olarak kullanılmaktadır 

C#'da Rastgele Sayılar Üretmek için ** `Random` sınıfını kullanabiliriz**.

## `C# Random` Sınıfı nedir?

`C# Random` sınıfı, rastgelelik için belirli istatistiksel gereksinimleri karşılayan bir dizi sayı üreten bir algoritma olan sözde rastgele sayı üretecidir.

Bu sınıfın `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` ve `NextSingle()` olmak üzere 5 yöntemi vardır 

Sayı türüne bağlı olarak, yani `int`,`long` vb. ilgili yöntemi kullanabiliriz.

Bunu daha iyi anlamak için örnekler üzerinden gidelim 

## C#'ta Rastgele tamsayı üretme 

C#'ta Rastgele tamsayı oluşturma adımları 

1. Rastgele sayı sınıfını başlatın.
2. `Int32.MinValue` ve `Int32.MaxValue` arasında rastgele tamsayı döndürmek için `Random.Next()` yöntemini kullanın.

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

### Minimum ve maksimum değerler arasında Rastgele tamsayı oluşturun

`Random.Next()` minimum ve maksimum değerleri parametre olarak kabul eden ve verilen değerler arasında rastgele bir tamsayı üreten aşırı yüklenmiş bir yönteme sahiptir.

100-1000 arasında rastgele sayılar üretmek için aşağıdaki kodu kullanın

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

## C#'ta Rastgele uzun sayı(Int64) üretme 

C#'ta Rastgele uzun sayı yani `Int64` oluşturmak için, `Int64.MinValue` ve `Int64.MaxValue` arasında rastgele `Int64` sayısı döndüren `Random.NextInt64()` yöntemini kullanın.

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

### Verilen Aralıkta Rastgele uzun sayı(Int64) üret

 `Random.Next()`'a benzer şekilde, `Random.NextInt64()` 'un da parametre olarak Aralık yani minimum ve maksimum değerleri kabul eden ve bunlar arasında rastgele bir `Int64` sayısı döndüren aşırı yüklenmiş bir yöntemi vardır.

100000 ile 200000 arasında rastgele sayılar üretmek için aşağıdaki kodu kullanın

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

Oluşturulan rastgele sayılar tamamen rastgele değildir, çünkü bunları seçmek için matematiksel bir algoritma kullanılır, ancak gerçek dünya durumlarının çoğu için yeterince iyidirler.

## Rastgele sayılar üretirken yinelemelerden kaçınma

Birden fazla `new Random()` sınıfı başlatıyorsanız 

Rastgele sayıların kopyalarını alabilirsiniz. (Çok iş parçacıklı uygulama)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Bu nedenle, yalnızca bir `Random()` sınıf örneğini başlatmak ve uygulama genelinde kullanmak daha iyidir.

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
Rastgele sayılar serisi oluşturmak istiyorsanız, çok iş parçacıklı ortamda yukarıdaki yöntemi kullanın.

## Kriptografik kullanma `C# RandomNumberGenerator`

Gerçekten benzersiz rastgele sayılar üretmek istiyorsanız, `System.Security.Cryptography` kütüphanesinin bir parçası olan `RandomNumberGenerator` sınıfından yararlanabilirsiniz.

Bu sınıf kriptografik olarak güvenli rastgele bir sayı üretir ve rastgele bir parola oluşturmak için uygundur.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Ayrıca aralığı `RandomNumberGenerator` yöntemine de aktarabiliriz.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## `C# RNGCryptoServiceProvider` sınıfını kullanma

Bu sınıf artık kullanılmıyor, bu yöntemi kullanmayın.

`RNGCryptoServiceProvider` kriptografik hizmet sağlayıcı (CSP) tarafından sağlanan uygulamayı kullanarak bir kriptografik Rastgele Sayı Üreticisi (RNG) uygular.

Aşağıdaki kodu kullanarak ` C# RNGCryptoServiceProvider` sınıfı ile rastgele bir sayı oluşturun.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Özet

Bu eğitimde C#'ta rastgele sayı üretmenin farklı yollarını basit örneklerle öğrendik.

















