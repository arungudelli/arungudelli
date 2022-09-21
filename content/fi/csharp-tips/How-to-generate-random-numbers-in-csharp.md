
---
title: "Miten luoda satunnaislukuja C#:ssa"
description: "Eri tapoja luoda satunnaislukuja C#:ssa yksinkertaisten esimerkkien avulla."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Satunnaislukuja käytetään laajalti digitaalisissa peleissä, tilastollisessa näytteenotossa, kryptografiassa, tilastollisessa fysiikassa, numeerisessa analyysissä, radioviestinnässä ja kasinopeleissä, kuten rulettipyörässä jne 

Voimme **käyttää `Random` -luokkaa satunnaislukujen tuottamiseen C#:ssä**.

## Mikä on `C# Random` -luokka?

`C# Random` luokka on pseudosattumanumerogeneraattori, joka on algoritmi, joka tuottaa numerosarjan, joka täyttää tietyt satunnaisuutta koskevat tilastolliset vaatimukset.

Tällä luokalla on 5 metodia `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` ja `NextSingle()` 

Riippuen numeron tyypistä eli `int`,`long` jne. voimme käyttää vastaavaa menetelmää.

Käydään läpi esimerkkejä, jotta ymmärrämme sen paremmin 

## Satunnaisen kokonaisluvun luominen C#:ssä 

Vaiheet satunnaisen kokonaisluvun luomiseksi C#:ssa 

1. Ota käyttöön satunnaislukuluokka.
2. Palauta `Random.Next()` -metodilla satunnainen kokonaisluku väliltä `Int32.MinValue` ja `Int32.MaxValue`.

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

### Luo satunnainen kokonaisluku minimi- ja maksimiarvojen väliltä

`Random.Next()` on ylikuormitettu metodi, joka hyväksyy parametreina minimi- ja maksimiarvot ja tuottaa satunnaisen kokonaisluvun annettujen arvojen väliltä.

Voit luoda satunnaislukuja väliltä 100-1000 käyttämällä alla olevaa koodia

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

## Luo satunnainen pitkä numero (Int64) C#:ssä 

Jos haluat luoda satunnaisen pitkän numeron eli `Int64` C#:ssa, käytä `Random.NextInt64()` -metodia, joka palauttaa satunnaisen `Int64` -numeron `Int64.MinValue` ja `Int64.MaxValue` väliltä.

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

### Luo satunnainen pitkä luku (Int64) annetulla alueella

Samoin kuin `Random.Next()`, `Random.NextInt64()` on ylikuormitettu metodi, joka hyväksyy Range- eli minimi- ja maksimiarvot parametreina ja palauttaa satunnaisen `Int64` -luvun näiden arvojen väliltä.

Voit luoda satunnaislukuja välillä 100000-200000 käyttämällä alla olevaa koodia

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

Generoidut satunnaisluvut eivät ole täysin satunnaisia, koska niiden valintaan käytetään matemaattista algoritmia, mutta ne riittävät hyvin useimpiin reaalimaailman tapauksiin.

## Kaksoiskappaleiden välttäminen satunnaislukuja luotaessa

Jos alustat useamman kuin yhden `new Random()` -luokan 

Saatat saada päällekkäisiä satunnaislukuja. (Monisäikeinen sovellus)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

On siis parempi alustaa vain yksi `Random()` -luokan instanssi ja käyttää sitä koko sovelluksessa.

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
Jos haluat luoda satunnaislukusarjoja monisäikeisessä ympäristössä, käytä edellä mainittua menetelmää.

## Kryptografisen `C# RandomNumberGenerator`

Jos haluat luoda todella uniikkeja satunnaislukuja, voit käyttää `RandomNumberGenerator` -luokkaa, joka on osa `System.Security.Cryptography` -kirjastoa.

Tämä luokka tuottaa salakirjoituksellisesti turvallisen satunnaisluvun, joka soveltuu satunnaisen salasanan luomiseen.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Voimme myös välittää alueen `RandomNumberGenerator` -menetelmälle.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Luokan `C# RNGCryptoServiceProvider` käyttäminen

Tämä luokka on nyt vanhentunut, älä käytä tätä menetelmää.

`RNGCryptoServiceProvider` toteuttaa kryptografisen satunnaislukugeneraattorin (Random Number Generator, RNG) käyttäen kryptografisen palveluntarjoajan (CSP) tarjoamaa toteutusta.

Käytä alla olevaa koodia luodaksesi satunnaisluvun ` C# RNGCryptoServiceProvider` -luokan avulla.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Yhteenveto

Tässä opetusohjelmassa opimme erilaisia tapoja luoda satunnaislukuja C#:lla yksinkertaisten esimerkkien avulla.

















