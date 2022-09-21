
---
title: "Cum se generează numere aleatoare în C#"
description: " Diferite moduri de a genera numere aleatoare în C# cu exemple simple."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Numerele aleatoare sunt utilizate pe scară largă în jocurile digitale, eșantionarea statistică, criptografia, calculele în fizica statistică, analiza numerică, comunicațiile radio și jocurile de cazinou, cum ar fi roata de ruletă etc 

Putem **utiliza clasa `Random` pentru a genera numere aleatoare în C#**.

## Ce este clasa `C# Random`?

`C# Random` clasa  este un generator de numere pseudo-aleatoare, care este un algoritm care generează o secvență de numere care îndeplinesc anumite cerințe statistice pentru aleatorism.

Această clasă are 5 metode `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` și `NextSingle()` 

În funcție de tipul de număr, adică `int`,`long` etc., putem utiliza metoda corespunzătoare.

Să parcurgem exemplele pentru a o înțelege mai bine 

## Generarea unui număr întreg aleatoriu în C# 

Pași pentru a genera numere întregi aleatorii în C# 

1. Instanțiați clasa numerelor aleatoare.
2. Utilizați metoda `Random.Next()` pentru a returna un număr întreg aleatoriu între `Int32.MinValue` și `Int32.MaxValue`.

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

### Generează un număr întreg aleatoriu între valorile minime și maxime

`Random.Next()` are o metodă supraîncărcată, care acceptă valorile minime și maxime ca parametri și care generează un număr întreg aleatoriu între valorile date.

Pentru a genera numere aleatoare între 100 și 1000, utilizați codul de mai jos

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

## Generarea unui număr lung aleatoriu (Int64) în C# 

Pentru a genera un număr lung aleatoriu, adică `Int64` în C#, utilizați metoda `Random.NextInt64()` care returnează un număr aleatoriu `Int64` între `Int64.MinValue` și `Int64.MaxValue`.

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

### Generarea unui număr lung aleatoriu (Int64) în intervalul dat

Similar cu `Random.Next()`, `Random.NextInt64()` are o metodă supraîncărcată, care acceptă ca parametrii intervalul, adică valorile minimă și maximă, și care returnează un număr aleatoriu `Int64` între acestea.

Pentru a genera numere aleatoare între 100000 și 200000, utilizați codul de mai jos

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

Numerele aleatoare generate nu sunt complet aleatoare, deoarece pentru a le selecta se folosește un algoritm matematic, dar sunt suficient de bune pentru majoritatea cazurilor din lumea reală.

## Evitarea dublurilor în timpul generării numerelor aleatoare

Dacă inițializați mai mult de o clasă `new Random()` 

S-ar putea să obțineți numere aleatoare duplicate. (Aplicație cu mai multe fire)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Prin urmare, este mai bine să inițializați o singură instanță a clasei `Random()` și să o utilizați în întreaga aplicație.

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
Dacă doriți să generați serii de numere aleatoare, în mediul multithread, utilizați metoda de mai sus.

## Utilizarea criptogramei `C# RandomNumberGenerator`

Dacă doriți să generați numere aleatoare cu adevărat unice, puteți utiliza clasa `RandomNumberGenerator`, care face parte din biblioteca `System.Security.Cryptography`.

Această clasă generează un număr aleatoriu sigur din punct de vedere criptografic și potrivit pentru crearea unei parole aleatoare.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Putem, de asemenea, să transmitem intervalul la metoda `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Utilizarea clasei `C# RNGCryptoServiceProvider` 

Această clasă este învechită acum, nu folosiți această metodă.

`RNGCryptoServiceProvider` implementează un generator de numere aleatoare (RNG) criptografic utilizând implementarea furnizată de furnizorul de servicii criptografice (CSP).

Utilizați codul de mai jos pentru a crea un număr aleatoriu cu clasa ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Rezumat

În acest tutorial am învățat diferite moduri de a genera numere aleatoare în C# cu exemple simple.

















