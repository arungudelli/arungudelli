
---
title: "Hur man genererar slumpmässiga tal i C#"
description: "Olika sätt att generera slumpmässiga tal i C# med enkla exempel."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Slumpmässiga tal används ofta i digitala spel, statistisk provtagning, kryptografi, beräkningar inom statistisk fysik, numerisk analys, radiokommunikation och kasinospel som roulettespel osv 

Vi kan **använda klassen `Random` för att generera slumpmässiga tal i C#**.

## Vad är klassen `C# Random`?

`C# Random` klassen  är en pseudo slumpmässig talgenerator, vilket är en algoritm som genererar en sekvens av tal som uppfyller vissa statistiska krav på slumpmässighet.

Denna klass har 5 metoder `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` och `NextSingle()` 

Beroende på vilken typ av tal, dvs. `int`,`long` osv., kan vi använda motsvarande metod.

Låt oss gå igenom exemplen för att förstå det ytterligare 

## Generera slumpmässigt heltal i C# 

Steg för att generera slumpmässiga heltal i C# 

1. Instantiera klassen för slumpmässiga tal.
2. Använd metoden `Random.Next()` för att returnera ett slumpmässigt heltal mellan `Int32.MinValue` och `Int32.MaxValue`.

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

#### Generera ett slumpmässigt heltal mellan minimi- och maximivärden

`Random.Next()` har en överladdad metod som accepterar minimi- och maximivärden som parametrar och som genererar ett slumpmässigt heltal mellan de givna värdena.

För att generera slumpmässiga tal mellan 100 och 1000 använd följande kod

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

## Generera slumpmässiga långa tal (Int64) i C# 

För att generera ett slumpmässigt långt nummer, dvs. `Int64` i C#, använd metoden `Random.NextInt64()` som returnerar ett slumpmässigt nummer `Int64` mellan `Int64.MinValue` och `Int64.MaxValue`.

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

#### Generera ett slumpmässigt långt nummer (Int64) i ett givet intervall

I likhet med `Random.Next()` har `Random.NextInt64()` en överladdad metod som accepterar Range, dvs. minimi- och maximivärden, som parametrar och som returnerar ett slumpmässigt `Int64` -tal mellan dem.

För att generera slumpmässiga tal mellan 100000 och 200000 använd nedanstående kod

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

De genererade slumpmässiga numren är inte helt slumpmässiga eftersom en matematisk algoritm används för att välja ut dem, men de är tillräckligt bra för de flesta fall i verkligheten.

## Undvika dubbletter vid generering av slumpmässiga nummer

Om du initialiserar mer än en klass `new Random()` 

Du kan få dubbletter av slumpmässiga nummer. (Flertrådig applikation)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Därför är det bättre att initialisera endast en instans av klassen `Random()` och använda den i hela programmet.

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
Om du vill generera serier av slumpmässiga tal i en miljö med flera trådar använder du ovanstående metod.

## Användning av kryptografiska `C# RandomNumberGenerator`

Om du vill generera verkligt unika slumptal kan du använda klassen `RandomNumberGenerator` som ingår i biblioteket `System.Security.Cryptography`.

Denna klass genererar ett kryptografiskt säkert slumpmässigt tal som lämpar sig för att skapa ett slumpmässigt lösenord.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Vi kan också skicka ett intervall till `RandomNumberGenerator` -metoden.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Användning av klassen `C# RNGCryptoServiceProvider` 

Den här klassen är föråldrad, använd inte den här metoden.

`RNGCryptoServiceProvider` implementerar en kryptografisk slumpmässig talgenerator (RNG) med hjälp av den implementering som tillhandahålls av leverantören av kryptografiska tjänster (CSP).

Använd nedanstående kod för att skapa ett slumpmässigt nummer med klassen ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Sammanfattning

I den här handledningen lärde vi oss olika sätt att generera slumpmässiga tal i C# med enkla exempel.

















