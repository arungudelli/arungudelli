
---
title: "Kaip generuoti atsitiktinius skaičius C# kalba"
description: "Įvairūs atsitiktinių skaičių generavimo būdai C# kalba su paprastais pavyzdžiais."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Atsitiktiniai skaičiai plačiai naudojami skaitmeniniuose žaidimuose, statistinėse imtyse, kriptografijoje, statistinės fizikos skaičiavimuose, skaitinėje analizėje, radijo ryšio priemonėse ir kazino žaidimuose, pvz., ruletės rate ir kt 

Atsitiktiniams skaičiams generuoti C#** galime **panaudoti `Random` klasę.

## Kas yra `C# Random` klasė?

`C# Random` klasė yra pseudo-atsitiktinių skaičių generatorius, t. y. algoritmas, generuojantis skaičių seką, atitinkančią tam tikrus statistinius atsitiktinumo reikalavimus.

Ši klasė turi 5 metodus: `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` ir `NextSingle()` 

Priklausomai nuo skaičiaus tipo, t. y. `int`,`long` ir t. t., galime naudoti atitinkamą metodą.

Peržiūrėkime pavyzdžius, kad geriau juos suprastume 

## Atsitiktinio sveikojo skaičiaus generavimas C# kalba 

Atsitiktinio sveikojo skaičiaus generavimo žingsniai C# kalba 

1. Įstatykite atsitiktinių skaičių klasę.
2. Naudokite `Random.Next()` metodą, kad grąžintumėte atsitiktinį sveikąjį skaičių tarp `Int32.MinValue` ir `Int32.MaxValue`.

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

#### Generuoti atsitiktinį sveikąjį skaičių tarp mažiausios ir didžiausios vertės

`Random.Next()` turi perkrautą metodą, kuris priima mažiausią ir didžiausią vertes kaip parametrus ir generuoja atsitiktinį sveiką skaičių tarp nurodytų verčių.

Norėdami generuoti atsitiktinius skaičius nuo 100 iki 1000, naudokite toliau pateiktą kodą

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

## Atsitiktinio ilgo skaičiaus(Int64) generavimas C# 

Norėdami sugeneruoti atsitiktinį ilgąjį skaičių, t. y. `Int64`, C# kalba, naudokite `Random.NextInt64()` metodą, kuris grąžina atsitiktinį `Int64` skaičių tarp `Int64.MinValue` ir `Int64.MaxValue`.

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

#### Generuoti atsitiktinį ilgąjį skaičių(Int64) duotame intervale

Panašiai kaip `Random.Next()`, `Random.NextInt64()` turi perkrovimo metodą, kuris kaip parametrus priima Range, t. y. mažiausią ir didžiausią reikšmes, ir grąžina atsitiktinį `Int64` skaičių tarp jų.

Norėdami generuoti atsitiktinius skaičius nuo 100000 iki 200000, naudokite toliau pateiktą kodą

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

Sugeneruoti atsitiktiniai skaičiai nėra visiškai atsitiktiniai, nes jiems parinkti naudojamas matematinis algoritmas, tačiau jie yra pakankamai geri daugeliu realaus pasaulio atvejų.

## Atsitiktinių skaičių dublikatų vengimas generuojant atsitiktinius skaičius

Jei inicializuojate daugiau nei vieną `new Random()` klasę 

Galite gauti atsitiktinių skaičių dubliavimąsi. (Daugiagijinė programa)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Todėl geriau inicializuoti tik vieną `Random()` klasės egzempliorių ir naudoti jį visoje programoje.

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
Jei norite generuoti atsitiktinių skaičių serijas, daugiagrandinėje aplinkoje naudokite pirmiau pateiktą metodą.

## Naudojant kriptografinį `C# RandomNumberGenerator`

Jei norite generuoti tikrai unikalius atsitiktinius skaičius, galite pasinaudoti `RandomNumberGenerator` klase, kuri yra `System.Security.Cryptography` bibliotekos dalis.

Ši klasė generuoja kriptografiškai saugų atsitiktinį skaičių ir tinka atsitiktiniam slaptažodžiui sukurti.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Metodui `RandomNumberGenerator` taip pat galime perduoti diapazoną.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Naudojant `C# RNGCryptoServiceProvider` klasę

Ši klasė jau paseno, nenaudokite šio metodo.

`RNGCryptoServiceProvider` įgyvendina kriptografinį atsitiktinių skaičių generatorių (RNG), naudodamas kriptografinių paslaugų teikėjo (CSP) pateiktą realizaciją.

Naudodami toliau pateiktą kodą sukurkite atsitiktinį skaičių naudodami ` C# RNGCryptoServiceProvider` klasę.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Apibendrinimas

Šioje pamokoje išmokome įvairių atsitiktinių skaičių generavimo būdų C# kalba, pateikdami paprastus pavyzdžius.

















