
---
title: "Sådan genereres tilfældige tal i C#"
description: "Forskellige måder at generere tilfældige tal i C# på med enkle eksempler."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Tilfældige tal anvendes i vid udstrækning i digitale spil, statistisk stikprøveudtagning, kryptografi, beregninger inden for statistisk fysik, numerisk analyse, radiokommunikation og kasinospil som roulettehjul osv 

Vi kan **bruge `Random` klassen til at generere tilfældige tal i C#**.

## Hvad er `C# Random` klassen?

`C# Random` klassen er en pseudo-tilfældig talgenerator, som er en algoritme, der genererer en sekvens af tal, der opfylder visse statistiske krav til tilfældighed.

Denne klasse har 5 metoder `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` og `NextSingle()` 

Afhængigt af typen af tal, dvs. `int`,`long` osv. kan vi anvende den tilsvarende metode.

Lad os gennemgå eksemplerne for at forstå det yderligere 

## Generer tilfældigt heltal i C# 

Trin til at generere tilfældige hele tal i C# 

1. Instantiér klassen for tilfældige tal.
2. Brug metoden `Random.Next()` til at returnere et tilfældigt heltal mellem `Int32.MinValue` og `Int32.MaxValue`.

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

#### Generer et tilfældigt heltal mellem minimum- og maksimumværdier

`Random.Next()` har en overbelastet metode, der accepterer minimum- og maksimumværdier som parametre, og som genererer et tilfældigt heltal mellem de givne værdier.

For at generere tilfældige tal mellem 100 og 1000 anvendes nedenstående kode

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

## Generer et tilfældigt langt tal (Int64) i C# 

For at generere et tilfældigt langt tal, dvs. `Int64` i C#, skal du bruge `Random.NextInt64()` -metoden, som returnerer et tilfældigt `Int64` -tal mellem `Int64.MinValue` og `Int64.MaxValue`.

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

#### Generer tilfældigt langt nummer(Int64) i det givne interval

I lighed med `Random.Next()` har `Random.NextInt64()` en overbelastet metode, som accepterer Range, dvs. minimum- og maksimumværdier som parametre, og som returnerer et tilfældigt `Int64` -tal mellem disse værdier.

For at generere tilfældige tal mellem 100000 og 200000 skal du bruge nedenstående kode

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

De genererede tilfældige tal er ikke helt tilfældige, fordi der anvendes en matematisk algoritme til at vælge dem, men de er gode nok til de fleste tilfælde i den virkelige verden.

## Undgå dubletter under generering af tilfældige tal

Hvis du initialiserer mere end én `new Random()` klasse 

Du kan få dubletter af tilfældige tal. (Flertrådet program)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Så det er bedre at initialisere kun én `Random()` klasseinstans og bruge den i hele programmet.

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
Hvis du ønsker at generere serier af tilfældige tal i et miljø med flere tråde, skal du bruge ovenstående metode.

## Brug af kryptografiske `C# RandomNumberGenerator`

Hvis du ønsker at generere helt unikke tilfældige tal, kan du bruge klassen `RandomNumberGenerator`, som er en del af biblioteket `System.Security.Cryptography`.

Denne klasse genererer et kryptografisk sikkert tilfældigt tal og er velegnet til at skabe et tilfældigt kodeord.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Vi kan også sende en rækkevidde til metoden `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Brug af klassen `C# RNGCryptoServiceProvider` 

Denne klasse er forældet nu, brug ikke denne metode.

`RNGCryptoServiceProvider` implementerer en kryptografisk tilfældig talgenerator (RNG) ved hjælp af den implementering, der leveres af den kryptografiske tjenesteudbyder (CSP).

Brug nedenstående kode til at oprette et tilfældigt tal med klassen ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Resumé

I denne tutorial lærte vi forskellige måder at generere tilfældige tal i C# på med enkle eksempler.

















