
---
title: "Jak generovat náhodná čísla v jazyce C#"
description: "Různé způsoby generování náhodných čísel v jazyce C# s jednoduchými příklady."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Náhodná čísla se široce používají v digitálních hrách, statistickém vzorkování, kryptografii, výpočtech ve statistické fyzice, numerické analýze, rádiové komunikaci a kasinových hrách, jako je ruleta atd 

Ke generování náhodných čísel v jazyce C#** můžeme **použít třídu `Random`.

## Co je to třída `C# Random`?

`C# Random` třída je generátor pseudonáhodných čísel, což je algoritmus, který generuje posloupnost čísel, jež splňují určité statistické požadavky na náhodnost.

Tato třída má 5 metod `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` a `NextSingle()` 

V závislosti na typu čísla, tj. `int`,`long` atd. můžeme použít odpovídající metodu.

Projděme si příklady, abychom je dále pochopili 

## Generování náhodného celého čísla v jazyce C# 

Kroky pro generování náhodného celého čísla v jazyce C# 

1. Instanciujte třídu náhodných čísel.
2. Použijte metodu `Random.Next()` pro vrácení náhodného celého čísla mezi `Int32.MinValue` a `Int32.MaxValue`.

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

### Generování náhodného celého čísla mezi minimální a maximální hodnotou

`Random.Next()` má přetíženou metodu, která přijímá jako parametry minimální a maximální hodnotu a generuje náhodné celé číslo mezi danými hodnotami.

Pro generování náhodných čísel mezi 100 a 1000 použijte následující kód

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

## Generování náhodného dlouhého čísla(Int64) v jazyce C# 

Chcete-li vygenerovat náhodné dlouhé číslo, tj. `Int64` v jazyce C#, použijte metodu `Random.NextInt64()`, která vrátí náhodné číslo `Int64` mezi `Int64.MinValue` a `Int64.MaxValue`.

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

### Generování náhodného dlouhého čísla(Int64) v daném rozsahu

Podobně jako `Random.Next()`, `Random.NextInt64()` má přetíženou metodu, která jako parametry přijímá Range, tj. minimální a maximální hodnotu, a vrací náhodné `Int64` číslo mezi nimi.

Pro generování náhodných čísel v rozsahu 100000 až 200000 použijte následující kód

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

Vygenerovaná náhodná čísla nejsou zcela náhodná, protože k jejich výběru je použit matematický algoritmus, ale pro většinu případů v reálném světě jsou dostatečně dobrá.

## Vyhnutí se duplicitám při generování náhodných čísel

Pokud inicializujete více než jednu třídu `new Random()` 

Mohlo by dojít k duplicitě náhodných čísel. (Vícevláknová aplikace)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Proto je lepší inicializovat pouze jednu instanci třídy `Random()` a používat ji v celé aplikaci.

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
Pokud chcete generovat sérii náhodných čísel, použijte ve vícevláknovém prostředí výše uvedenou metodu.

## Použití kryptografického `C# RandomNumberGenerator`

Pokud chcete generovat skutečně unikátní náhodná čísla, můžete využít třídu `RandomNumberGenerator`, která je součástí knihovny `System.Security.Cryptography`.

Tato třída generuje kryptograficky bezpečná náhodná čísla a hodí se pro vytvoření náhodného hesla.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Metodě `RandomNumberGenerator` můžeme také předat rozsah.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Použití třídy `C# RNGCryptoServiceProvider` 

Tato třída je již zastaralá, tuto metodu nepoužívejte.

`RNGCryptoServiceProvider` implementuje kryptografický generátor náhodných čísel (RNG) pomocí implementace poskytnuté poskytovatelem kryptografických služeb (CSP).

Pomocí níže uvedeného kódu vytvořte náhodné číslo pomocí třídy ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Shrnutí

V tomto tutoriálu jsme se na jednoduchých příkladech naučili různé způsoby generování náhodných čísel v jazyce C#.

















