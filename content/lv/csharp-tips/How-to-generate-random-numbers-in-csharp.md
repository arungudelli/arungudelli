
---
title: "Kā ģenerēt nejaušus skaitļus programmā C#"
description: "Dažādi veidi, kā ģenerēt nejaušus skaitļus programmā C#, un vienkārši piemēri."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Nejaušus skaitļus plaši izmanto digitālajās spēlēs, statistiskajā izlasē, kriptogrāfijā, statistiskās fizikas aprēķinos, skaitliskā analīzē, radiosakariem un kazino spēlēs, piemēram, ruletes ritenī u. c 

Mēs varam **izmantot `Random` klasi, lai ģenerētu nejaušus skaitļus C#**.

## Kas ir `C# Random` klase?

`C# Random` šī klase ir pseidogadījuma skaitļu ģenerators, kas ir algoritms, kurš ģenerē skaitļu secību, kas atbilst noteiktām nejaušības statistiskajām prasībām.

Šai klasei ir 5 metodes `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` un `NextSingle()` 

Atkarībā no skaitļa veida, t. i., `int`,`long` u. c., mēs varam izmantot attiecīgo metodi.

Izskatīsim piemērus, lai to izprastu sīkāk 

## Ģenerēt nejaušu veselu skaitli C# valodā 

Soļi, kā ģenerēt nejaušu veselu skaitli programmā C# 

1. Instancējiet nejaušo skaitļu klasi.
2. Izmantojiet `Random.Next()` metodi, lai atgrieztu nejaušu veselu skaitli starp `Int32.MinValue` un `Int32.MaxValue`.

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

#### Ģenerē nejaušu veselu skaitli starp minimālo un maksimālo vērtību

`Random.Next()` ir pārslogota metode, kas kā parametrus pieņem minimālo un maksimālo vērtību un ģenerē nejaušu veselu skaitli starp dotajām vērtībām.

Lai ģenerētu nejaušus skaitļus no 100 līdz 1000, izmantojiet turpmāk norādīto kodu

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

## Ģenerēt nejaušu garu skaitli(Int64) programmā C# 

Lai ģenerētu nejaušu garu skaitli, t. i., `Int64` C#, izmantojiet `Random.NextInt64()` metodi, kas atgriež nejaušu `Int64` skaitli starp `Int64.MinValue` un `Int64.MaxValue`.

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

#### Ģenerēt nejaušu garu skaitli(Int64) dotajā diapazonā

Līdzīgi kā `Random.Next()`, `Random.NextInt64()` ir pārslogota metode, kas kā parametrus pieņem diapazonu, t. i., minimālo un maksimālo vērtību, un atgriež nejaušu `Int64` skaitli starp tām.

Lai ģenerētu nejaušus skaitļus no 100000 līdz 200000, izmantojiet turpmāk norādīto kodu

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

Ģenerētie nejaušie skaitļi nav pilnīgi nejauši, jo to atlasē tiek izmantots matemātisks algoritms, taču tie ir pietiekami labi lielākajā daļā reālās pasaules gadījumu.

## Izvairīšanās no dublēšanās nejaušo skaitļu ģenerēšanas laikā

Ja tiek inicializēta vairāk nekā viena `new Random()` klase 

Var rasties nejaušo skaitļu dublēšanās. (Daudzpavedienu lietojumprogramma)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Tāpēc labāk ir inicializēt tikai vienu `Random()` klases gadījumu un izmantot to visā lietojumprogrammā.

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
Ja vēlaties ģenerēt nejaušo skaitļu sērijas, daudzpavedienu vidē izmantojiet iepriekš minēto metodi.

## Izmantojot kriptogrāfisko `C# RandomNumberGenerator`

Ja vēlaties ģenerēt patiesi unikālus nejaušus skaitļus, varat izmantot `RandomNumberGenerator` klasi, kas ir daļa no `System.Security.Cryptography` bibliotēkas.

Šī klase ģenerē kriptogrāfiski drošus nejaušus skaitļus un ir piemērota nejaušas paroles izveidei.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Metodei `RandomNumberGenerator` mēs varam nodot arī diapazonu.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Izmantojot `C# RNGCryptoServiceProvider` klasi

Šī klase tagad ir novecojusi, Neizmantojiet šo metodi.

`RNGCryptoServiceProvider` implementē kriptogrāfisku nejaušo skaitļu ģeneratoru (RNG), izmantojot kriptogrāfijas pakalpojumu sniedzēja (CSP) nodrošināto implementāciju.

Izmantojiet tālāk sniegto kodu, lai izveidotu nejaušus skaitļus, izmantojot ` C# RNGCryptoServiceProvider` klasi.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Kopsavilkums

Šajā pamācībā mēs uzzinājām dažādus veidus, kā ģenerēt nejaušus skaitļus C# ar vienkāršiem piemēriem.

















