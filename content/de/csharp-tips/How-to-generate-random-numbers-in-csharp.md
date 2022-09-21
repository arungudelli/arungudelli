
---
title: "Generierung von Zufallszahlen in C#"
description: "Verschiedene Möglichkeiten zur Generierung von Zufallszahlen in C# mit einfachen Beispielen."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Zufallszahlen sind weit verbreitet in digitalen Spielen, statistische Stichproben, Kryptographie, Berechnungen in der statistischen Physik, numerische Analyse, Funkkommunikation und Casino-Spiele wie Roulette-Rad usw. verwendet 

Wir können **die Klasse `Random` verwenden, um Zufallszahlen in C#** zu generieren.

## Was ist die Klasse `C# Random`?

`C# Random` die Klasse  ist ein Pseudo-Zufallszahlengenerator, d. h. ein Algorithmus, der eine Folge von Zahlen erzeugt, die bestimmte statistische Anforderungen an die Zufälligkeit erfüllen.

Diese Klasse hat 5 Methoden `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` und `NextSingle()` 

Je nach Art der Zahl, d. h. `int`,`long` usw., können wir die entsprechende Methode verwenden.

Schauen wir uns die Beispiele an, um sie besser zu verstehen 

## Zufällige Ganzzahl in C# generieren 

Schritte zum Erzeugen einer zufälligen Ganzzahl in C# 

1. Instanziieren Sie die Zufallszahlen-Klasse.
2. Verwenden Sie die Methode `Random.Next()`, um eine zufällige ganze Zahl zwischen `Int32.MinValue` und `Int32.MaxValue` zu erhalten.

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

### Generieren Sie eine zufällige ganze Zahl zwischen dem minimalen und dem maximalen Wert

`Random.Next()` verfügt über eine überladene Methode, die Mindest- und Höchstwerte als Parameter akzeptiert und eine zufällige ganze Zahl zwischen den angegebenen Werten erzeugt.

Um Zufallszahlen zwischen 100 und 1000 zu erzeugen, verwenden Sie den folgenden Code

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

## Generate Random long number(Int64) in C# 

Um eine zufällige lange Zahl, d.h. `Int64`, in C# zu erzeugen, verwenden Sie die Methode `Random.NextInt64()`, die eine zufällige Zahl `Int64` zwischen `Int64.MinValue` und `Int64.MaxValue` zurückgibt.

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

### Generieren Sie eine zufällige lange Zahl (Int64) in einem bestimmten Bereich

Ähnlich wie `Random.Next()` verfügt `Random.NextInt64()` über eine überladene Methode, die Range, d.h. Minimal- und Maximalwerte als Parameter akzeptiert und eine zufällige `Int64` Zahl zwischen diesen Werten zurückgibt.

Um Zufallszahlen zwischen 100000 und 200000 zu erzeugen, verwenden Sie den folgenden Code

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

Die generierten Zufallszahlen sind nicht völlig zufällig, da ein mathematischer Algorithmus verwendet wird, um sie auszuwählen, aber sie sind gut genug für die meisten Fälle in der realen Welt.

## Vermeidung von Duplikaten bei der Generierung von Zufallszahlen

Wenn Sie mehr als eine `new Random()` Klasse initialisieren 

Sie könnten doppelte Zufallszahlen erhalten. (Multithreading-Anwendung)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Es ist daher besser, nur eine Instanz der Klasse `Random()` zu initialisieren und diese in der gesamten Anwendung zu verwenden.

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
Wenn Sie in einer Multithreading-Umgebung eine Reihe von Zufallszahlen erzeugen möchten, verwenden Sie die obige Methode.

## Verwendung kryptographischer `C# RandomNumberGenerator`

Wenn Sie wirklich eindeutige Zufallszahlen erzeugen wollen, können Sie die Klasse `RandomNumberGenerator` verwenden, die Teil der Bibliothek `System.Security.Cryptography` ist.

Diese Klasse generiert eine kryptografisch sichere Zufallszahl und eignet sich für die Erstellung eines Zufallspassworts.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Wir können auch einen Bereich an die Methode `RandomNumberGenerator` übergeben.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Verwendung der Klasse `C# RNGCryptoServiceProvider` 

Diese Klasse ist jetzt veraltet, verwenden Sie diese Methode nicht.

`RNGCryptoServiceProvider` implementiert einen kryptografischen Zufallszahlengenerator (RNG) unter Verwendung der vom Kryptodienstanbieter (CSP) bereitgestellten Implementierung.

Verwenden Sie den folgenden Code, um eine Zufallszahl mit der Klasse ` C# RNGCryptoServiceProvider` zu erstellen.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Zusammenfassung

In diesem Tutorial haben wir anhand einfacher Beispiele gelernt, wie man in C# Zufallszahlen erzeugt.

















