
---
title: "Kako generirati naključne številke v C#"
description: "Različni načini generiranja naključnih številk v C# s preprostimi primeri."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Naključna števila se pogosto uporabljajo v digitalnih igrah, statističnem vzorčenju, kriptografiji, izračunih v statistični fiziki, numerični analizi, radijskih komunikacijah in igralniških igrah, kot je kolo rulete itd 

Za generiranje naključnih številk v jeziku C#** lahko **uporabimo razred `Random`.

## Kaj je razred `C# Random`?

`C# Random` razred je generator psevdonaključnih števil, ki je algoritem, ki generira zaporedje števil, ki izpolnjujejo določene statistične zahteve za naključnost.

Ta razred ima 5 metod `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` in `NextSingle()` 

Glede na vrsto števila, tj. `int`,`long` itd. lahko uporabimo ustrezno metodo.

Preglejmo primere, da jih bomo bolje razumeli 

## Generiranje naključnega celega števila v C# 

Koraki za generiranje naključnega celega števila v C# 

1. Instancirajte razred naključnih števil.
2. Uporabite metodo `Random.Next()`, da vrnete naključno celo število med `Int32.MinValue` in `Int32.MaxValue`.

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

### Ustvari naključno celo število med najmanjšo in največjo vrednostjo

`Random.Next()` ima preobremenjeno metodo, ki kot parametra sprejme najmanjšo in največjo vrednost, ki generira naključno celo število med danima vrednostma.

Za generiranje naključnih števil med 100 in 1000 uporabite spodnjo kodo

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

## Generiranje naključnega dolgega števila(Int64) v C# 

Za generiranje naključnega dolgega števila, tj. `Int64`, v jeziku C# uporabite metodo `Random.NextInt64()`, ki vrne naključno število `Int64` med `Int64.MinValue` in `Int64.MaxValue`.

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

#### Generiranje naključnega dolgega števila(Int64) v danem območju

Podobno kot `Random.Next()`, ima `Random.NextInt64()` preobremenjeno metodo, ki kot parametra sprejme razpon, tj. najmanjšo in največjo vrednost, in vrne naključno `Int64` število med njima.

Za generiranje naključnih števil med 100000 in 200000 uporabite spodnjo kodo

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

Ustvarjene naključne številke niso popolnoma naključne, saj je za njihovo izbiro uporabljen matematični algoritem, vendar so dovolj dobre za večino primerov v resničnem svetu.

## Izogibanje podvajanju pri generiranju naključnih števil

Če inicializirate več kot en razred `new Random()` 

Morda boste dobili podvojena naključna števila. (Večnitna aplikacija)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Zato je bolje inicializirati samo en primerek razreda `Random()` in ga uporabljati v celotni aplikaciji.

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
Če želite v večnitnem okolju ustvariti serijo naključnih številk, uporabite zgornjo metodo.

## Uporaba kriptografske `C# RandomNumberGenerator`

Če želite ustvariti resnično edinstvena naključna števila, lahko uporabite razred `RandomNumberGenerator`, ki je del knjižnice `System.Security.Cryptography`.

Ta razred generira kriptografsko varno naključno število in je primeren za ustvarjanje naključnega gesla.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Metodi `RandomNumberGenerator` lahko posredujemo tudi območje.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Uporaba razreda `C# RNGCryptoServiceProvider` 

Ta razred je zdaj zastarel, ne uporabljajte te metode.

`RNGCryptoServiceProvider` implementira kriptografski generator naključnih števil (RNG) z uporabo implementacije, ki jo zagotovi ponudnik kriptografskih storitev (CSP).

S spodnjo kodo ustvarite naključno število z razredom ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Povzetek

V tem učbeniku smo spoznali različne načine za generiranje naključnih števil v C# s preprostimi primeri.

















