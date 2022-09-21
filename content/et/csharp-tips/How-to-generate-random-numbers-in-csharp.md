
---
title: "Kuidas genereerida juhuslikke numbreid C# keeles"
description: "Erinevad viisid juhuslike numbrite genereerimiseks C# keeles koos lihtsate näidetega."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Juhuslikke numbreid kasutatakse laialdaselt digitaalsetes mängudes, statistilises proovivõtus, krüptograafias, statistilise füüsika arvutustes, numbrilises analüüsis, raadioside ja kasiinomängudes nagu rulett jne 

Me saame **kasutada `Random` klassi juhuslike numbrite genereerimiseks C#**.

## Mis on `C# Random` klass?

`C# Random` klass on pseudosuhtarvugeneraator, mis on algoritm, mis genereerib numbrite jada, mis vastab teatud statistilistele juhuslikkuse nõuetele.

Sellel klassil on 5 meetodit `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` ja `NextSingle()` 

Sõltuvalt arvu tüübist, st `int`,`long` jne, saame kasutada vastavat meetodit.

Vaatame läbi näited, et seda paremini mõista 

## Juhusliku täisarvu genereerimine C# keeles 

Juhusliku täisarvu genereerimise sammud C# keeles 

1. Instantseeri juhusliku arvu klass.
2. Kasutage meetodit `Random.Next()`, et tagastada juhuslik täisarv vahemikus `Int32.MinValue` ja `Int32.MaxValue`.

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

### Genereeri juhuslik täisarv minimaalse ja maksimaalse väärtuse vahel

`Random.Next()` on ülekoormatud meetod, mis võtab parameetritena vastu minimaalse ja maksimaalse väärtuse, mis genereerib juhusliku täisarvu antud väärtuste vahel.

Juhuslike arvude genereerimiseks vahemikus 100 kuni 1000 kasutage alljärgnevat koodi

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

## Genereeri juhuslik pikk number(Int64) C# keeles 

Et genereerida juhuslik pikk number st, `Int64` in C#, Kasutage `Random.NextInt64()` meetod, mis tagastab juhusliku `Int64` number vahel `Int64.MinValue` ja `Int64.MaxValue`.

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

### Genereeri juhuslik pikk number (Int64) antud vahemikus

Sarnaselt `Random.Next()`, `Random.NextInt64()` on ülekoormatud meetod, mis võtab parameetritena vastu Range, st minimaalse ja maksimaalse väärtuse, mis tagastab juhusliku `Int64` arvu nende vahel.

Juhusliku arvu genereerimiseks vahemikus 100000 kuni 200000 kasutage alljärgnevat koodi

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

Genereeritud juhuslikud numbrid ei ole täiesti juhuslikud, sest nende valimiseks kasutatakse matemaatilist algoritmi, kuid need on enamiku tegelike juhtumite jaoks piisavalt head.

## Duplikaatide vältimine juhuslike numbrite genereerimisel

Kui te initsialiseerite rohkem kui ühte `new Random()` klassi 

Sa võid saada duplikaatseid juhuslikke numbreid. (Mitmesuunaline rakendus)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Seega on parem initsialiseerida ainult üks `Random()` klassi eksemplar ja kasutada seda kogu rakenduses.

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
Kui soovite genereerida rida juhuslikke numbreid, siis kasutage mitmesuunalises keskkonnas ülaltoodud meetodit.

## Krüptograafiliste `C# RandomNumberGenerator`

Kui soovite genereerida tõeliselt unikaalseid juhuslikke numbreid, võite kasutada `RandomNumberGenerator` klassi, mis on osa `System.Security.Cryptography` raamatukogust.

See klass genereerib krüptograafiliselt turvalise juhusliku arvu ja sobib juhusliku parooli loomiseks.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Me võime ka meetodile `RandomNumberGenerator` edastada vahemiku.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Kasutades `C# RNGCryptoServiceProvider` klassi

See klass on nüüdseks vananenud, ärge kasutage seda meetodit.

`RNGCryptoServiceProvider` rakendab krüptograafilise juhusliku numbrigeneraatori (RNG), kasutades krüptograafilise teenusepakkuja (CSP) pakutavat rakendust.

Kasutage alljärgnevat koodi, et luua juhuslik number klassiga ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Kokkuvõte

Selles õpetuses õppisime lihtsate näidete abil erinevaid võimalusi juhuslike numbrite genereerimiseks C# keeles.

















