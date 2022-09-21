
---
title: "Ako generovať náhodné čísla v jazyku C#"
description: "Rôzne spôsoby generovania náhodných čísel v jazyku C# s jednoduchými príkladmi."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Náhodné čísla sa široko používajú v digitálnych hrách, štatistickom vzorkovaní, kryptografii, výpočtoch v štatistickej fyzike, numerickej analýze, rádiovej komunikácii a kasínových hrách, ako je ruleta atď 

Na generovanie náhodných čísel v jazyku C# môžeme **použiť triedu `Random` **.

## Čo je trieda `C# Random`?

`C# Random` trieda je generátor pseudonáhodných čísel, čo je algoritmus, ktorý generuje postupnosť čísel, ktoré spĺňajú určité štatistické požiadavky na náhodnosť.

Táto trieda má 5 metód `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` a `NextSingle()` 

V závislosti od typu čísla, t. j. `int`,`long` atď. môžeme použiť príslušnú metódu.

Prejdime si príklady, aby sme ich lepšie pochopili 

## Generovanie náhodného celého čísla v jazyku C# 

Kroky na generovanie náhodného celého čísla v jazyku C# 

1. Vytvorte inštanciu triedy náhodných čísel.
2. Použite metódu `Random.Next()` na vrátenie náhodného celého čísla medzi `Int32.MinValue` a `Int32.MaxValue`.

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

### Generovanie náhodného celého čísla medzi minimálnou a maximálnou hodnotou

`Random.Next()` má preťaženú metódu, ktorá prijíma ako parametre minimálne a maximálne hodnoty a generuje náhodné celé číslo medzi danými hodnotami.

Na generovanie náhodných čísel medzi 100 a 1000 použite nasledujúci kód

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

## Generovanie náhodného dlhého čísla(Int64) v jazyku C# 

Ak chcete vygenerovať náhodné dlhé číslo, t. j. `Int64` v jazyku C#, použite metódu `Random.NextInt64()`, ktorá vráti náhodné číslo `Int64` medzi `Int64.MinValue` a `Int64.MaxValue`.

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

### Generovanie náhodného dlhého čísla(Int64) v danom rozsahu

Podobne ako `Random.Next()`, `Random.NextInt64()` má preťaženú metódu, ktorá ako parametre prijíma Range, t. j. minimálnu a maximálnu hodnotu, ktorá vráti náhodné `Int64` číslo medzi nimi.

Na generovanie náhodných čísel v rozsahu 100000 až 200000 použite nasledujúci kód

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

Vygenerované náhodné čísla nie sú úplne náhodné, pretože na ich výber sa používa matematický algoritmus, ale sú dostatočne dobré pre väčšinu reálnych prípadov.

## Vyhýbanie sa duplicitám pri generovaní náhodných čísel

Ak inicializujete viac ako jednu triedu `new Random()` 

Mohli by ste získať duplicitné náhodné čísla. (Viacvláknová aplikácia)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Preto je lepšie inicializovať iba jednu inštanciu triedy `Random()` a používať ju v celej aplikácii.

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
Ak chcete generovať sériu náhodných čísel, vo viacvláknovom prostredí použite vyššie uvedenú metódu.

## Použitie kryptografického `C# RandomNumberGenerator`

Ak chcete generovať skutočne jedinečné náhodné čísla, môžete využiť triedu `RandomNumberGenerator`, ktorá je súčasťou knižnice `System.Security.Cryptography`.

Táto trieda generuje kryptograficky bezpečné náhodné číslo a je vhodná na vytvorenie náhodného hesla.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Metóde `RandomNumberGenerator` môžeme odovzdať aj rozsah.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Použitie triedy `C# RNGCryptoServiceProvider` 

Táto trieda je už zastaraná, nepoužívajte túto metódu.

`RNGCryptoServiceProvider` implementuje kryptografický generátor náhodných čísel (RNG) pomocou implementácie, ktorú poskytuje poskytovateľ kryptografických služieb (CSP).

Pomocou nižšie uvedeného kódu vytvorte náhodné číslo pomocou triedy ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Zhrnutie

V tomto tutoriáli sme sa naučili rôzne spôsoby generovania náhodných čísel v jazyku C# na jednoduchých príkladoch.

















