
---
title: "Hoe willekeurige getallen genereren in C#"
description: "Verschillende manieren om willekeurige getallen te genereren in C# met eenvoudige voorbeelden."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Willekeurige getallen worden veel gebruikt in digitale spellen, statistische steekproeven, cryptografie, berekeningen in de statistische natuurkunde, numerieke analyse, radiocommunicatie en casinospellen zoals het Roulettewiel enz 

We kunnen **de klasse `Random` gebruiken om willekeurige getallen in C# te genereren**.

## Wat is de klasse `C# Random`?

`C# Random` class is een pseudo-willekeurige getallengenerator, een algoritme dat een reeks getallen genereert die voldoen aan bepaalde statistische eisen voor willekeurigheid.

Deze klasse heeft 5 methodes `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` en `NextSingle()` 

Afhankelijk van het type nummer, `int`,`long` enz. kunnen we de overeenkomstige methode gebruiken.

Laten we de voorbeelden doornemen om het verder te begrijpen 

## Willekeurig geheel getal genereren in C# 

Stappen om Willekeurig geheel getal in C# te genereren 

1. Installeer de klasse voor willekeurige getallen.
2. Gebruik de methode `Random.Next()` om een willekeurig geheel getal tussen `Int32.MinValue` en `Int32.MaxValue` te genereren.

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

### Genereer willekeurig geheel getal tussen minimum en maximum waarden

`Random.Next()` heeft een overbelaste methode die minimum- en maximumwaarden als parameters accepteert en een willekeurig geheel getal tussen de opgegeven waarden genereert.

Gebruik de volgende code om willekeurige getallen tussen 100 en 1000 te genereren

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

## Willekeurig lang nummer(Int64) genereren in C# 

 `Int64` Om een willekeurig lang getal, `Int64`, te genereren in C#, gebruik je de methode `Random.NextInt64()` die een willekeurig getal tussen `Int64.MinValue` en `Int64.MaxValue` teruggeeft.

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

### Willekeurig lang getal (Int64) in gegeven bereik genereren

Vergelijkbaar met `Random.Next()` heeft `Random.NextInt64()` een overbelaste methode, die Bereik, d.w.z. minimum en maximum waarden als parameters accepteert en een willekeurig `Int64` getal daartussen teruggeeft.

Gebruik de volgende code om willekeurige getallen tussen 100000 en 200000 te genereren

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

De gegenereerde willekeurige getallen zijn niet volledig willekeurig omdat een wiskundig algoritme wordt gebruikt om ze te selecteren, maar ze zijn goed genoeg voor de meeste gevallen in de echte wereld.

## Vermijden van duplicaten bij het genereren van willekeurige getallen

Als u meer dan één klasse `new Random()` initialiseert 

Krijg je misschien dubbele willekeurige getallen. (Multithreaded applicatie)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Het is dus beter om slechts één instantie van de klasse `Random()` te initialiseren, en die in de hele toepassing te gebruiken.

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
Als u reeksen willekeurige getallen wilt genereren, gebruik dan de bovenstaande methode in een multithreaded omgeving.

## Gebruik van cryptografische `C# RandomNumberGenerator`

Als u echt unieke willekeurige getallen wilt genereren, kunt u gebruik maken van de klasse `RandomNumberGenerator`, die deel uitmaakt van de bibliotheek `System.Security.Cryptography`.

Deze klasse genereert een cryptografisch veilig willekeurig getal en is geschikt voor het maken van een willekeurig wachtwoord.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

We kunnen ook een bereik doorgeven aan de methode `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## De klasse `C# RNGCryptoServiceProvider` gebruiken

Deze klasse is nu verouderd, gebruik deze methode niet.

`RNGCryptoServiceProvider` implementeert een cryptografische Random Number Generator (RNG) met behulp van de implementatie van de cryptografische dienstverlener (CSP).

Gebruik de onderstaande code om een willekeurig getal te maken met de klasse ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Samenvatting

In deze tutorial hebben we verschillende manieren geleerd om willekeurige getallen te genereren in C# met eenvoudige voorbeelden.

















