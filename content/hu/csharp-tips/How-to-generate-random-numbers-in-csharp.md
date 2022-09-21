
---
title: "Hogyan generáljunk véletlen számokat C# nyelven"
description: "A véletlen számok generálásának különböző módjai C# nyelven egyszerű példákkal."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


A véletlen számokat széles körben használják a digitális játékokban, a statisztikai mintavételezésben, a kriptográfiában, a statisztikai fizikában, a numerikus elemzésben, a rádiós kommunikációban és a kaszinójátékokban, például a rulettkerékben stb 

Véletlenszámok generálására C# nyelven **használhatjuk a `Random` osztályt**.

## Mi az a `C# Random` osztály?

`C# Random` osztály egy pszeudo-véletlenszám-generátor, amely egy olyan algoritmus, amely olyan számsorozatot generál, amely megfelel bizonyos statisztikai követelményeknek a véletlenszerűség tekintetében.

Ennek az osztálynak 5 metódusa van: `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` és `NextSingle()` 

A szám típusától függően, azaz a `int`,`long` stb. számok típusától függően használhatjuk a megfelelő módszert.

Nézzük át a példákat a további megértéshez 

## Véletlen egész szám generálása C# nyelven 

Véletlen egész szám generálásának lépései C# nyelven 

1. Minősítsük a véletlen szám osztályt.
2. A `Random.Next()` metódus segítségével a `Int32.MinValue` és a `Int32.MaxValue` közötti véletlen egész számot adja vissza.

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

### Véletlen egész szám generálása a minimális és maximális értékek között

`Random.Next()` rendelkezik egy túlterhelt metódussal, amely paraméterként elfogadja a minimum és maximum értékeket, és a megadott értékek között egy véletlen egész számot generál.

A 100 és 1000 közötti véletlen számok generálásához használja az alábbi kódot

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

## Véletlen hosszú szám(Int64) generálása C# nyelven 

A véletlen hosszú szám generálásához, azaz a `Int64` C# nyelven, használja a `Random.NextInt64()` módszert, amely a `Int64.MinValue` és a `Int64.MaxValue` közötti véletlenszerű `Int64` számot adja vissza.

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

### Véletlen hosszú szám (Int64) generálása adott tartományban

Hasonlóan a `Random.Next()`, a `Random.NextInt64()`, rendelkezik egy túlterhelt metódussal, amely elfogadja a Range, azaz a minimális és maximális értékeket paraméterként, amely egy véletlenszerű `Int64` számot ad vissza ezek között.

A 100000 és 200000 közötti véletlen számok generálásához használjuk az alábbi kódot

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

A generált véletlen számok nem teljesen véletlenszerűek, mivel egy matematikai algoritmus segítségével választjuk ki őket, de a legtöbb valós esethez elég jók.

## Duplikátumok elkerülése a véletlenszámok generálásakor

Ha egynél több `new Random()` osztályt inicializálunk 

Duplikált véletlenszámokat kaphatsz. (Többszálú alkalmazás)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Ezért jobb, ha csak egy `Random()` osztálypéldányt inicializálunk, és azt használjuk az egész alkalmazásban.

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
Ha véletlen számok sorozatát szeretné generálni, többszálas környezetben használja a fenti módszert.

## Kriptográfiai `C# RandomNumberGenerator`

Ha valóban egyedi véletlen számokat akarsz generálni, használhatod a `RandomNumberGenerator` osztályt, amely a `System.Security.Cryptography` könyvtár része.

Ez az osztály kriptográfiailag biztonságos véletlen számot generál, és alkalmas véletlen jelszó létrehozására.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

A `RandomNumberGenerator` metódusnak tartományt is átadhatunk.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## A `C# RNGCryptoServiceProvider` osztály használata

Ez az osztály már elavult, ne használd ezt a módszert.

`RNGCryptoServiceProvider` kriptográfiai véletlenszám-generátort (RNG) valósít meg a kriptográfiai szolgáltató (CSP) által biztosított implementációval.

Az alábbi kód segítségével hozzon létre véletlen számot a ` C# RNGCryptoServiceProvider` osztállyal.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Összefoglaló

Ebben a bemutatóban megtanultuk a véletlen számok generálásának különböző módjait C# nyelven, egyszerű példákon keresztül.

















