
---
title: "Come generare numeri casuali in C#"
description: "Diversi modi per generare numeri casuali in C# con semplici esempi."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


I numeri casuali sono ampiamente utilizzati nei giochi elettronici, nel campionamento statistico, nella crittografia, nei calcoli di fisica statistica, nell'analisi numerica, nelle comunicazioni radio e nei giochi di casinò come la roulette, ecc 

Possiamo **usare la classe `Random` per generare numeri casuali in C#**.

## Che cos'è la classe `C# Random`?

`C# Random` la classe  è un generatore di numeri pseudocasuali, ovvero un algoritmo che genera una sequenza di numeri che soddisfano determinati requisiti statistici di casualità.

Questa classe ha 5 metodi `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` e `NextSingle()` 

A seconda del tipo di numero, cioè `int`,`long` ecc. possiamo utilizzare il metodo corrispondente.

Vediamo gli esempi per capire meglio 

## Generare numeri interi casuali in C# 

Passi per generare numeri interi casuali in C# 

1. Istanziare la classe dei numeri casuali.
2. Utilizzare il metodo `Random.Next()` per restituire un numero intero casuale compreso tra `Int32.MinValue` e `Int32.MaxValue`.

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

### Genera un intero casuale tra i valori minimo e massimo

`Random.Next()` ha un metodo sovraccaricato che accetta come parametri i valori minimo e massimo e genera un intero casuale tra i valori indicati.

Per generare numeri casuali compresi tra 100 e 1000, utilizzare il codice seguente

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

## Generare un numero casuale lungo(Int64) in C# 

Per generare un numero lungo casuale, cioè `Int64` in C#, utilizzare il metodo `Random.NextInt64()` che restituisce un numero casuale `Int64` compreso tra `Int64.MinValue` e `Int64.MaxValue`.

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

### Generare un numero lungo casuale (Int64) in un intervallo dato

Simile a `Random.Next()`, `Random.NextInt64()` ha un metodo sovraccaricato, che accetta come parametri Range, ossia i valori minimo e massimo, e restituisce un numero casuale `Int64` compreso tra questi.

Per generare numeri casuali compresi tra 100000 e 200000, utilizzare il codice seguente

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

I numeri casuali generati non sono completamente casuali, perché viene utilizzato un algoritmo matematico per selezionarli, ma sono sufficienti per la maggior parte dei casi reali.

## Evitare i duplicati durante la generazione di numeri casuali

Se si inizializza più di una classe `new Random()` 

Si potrebbero ottenere numeri casuali duplicati. (Applicazione multithread)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Quindi è meglio inizializzare una sola istanza della classe `Random()` e utilizzarla in tutta l'applicazione.

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
Se si desidera generare una serie di numeri casuali, in un ambiente multithread, utilizzare il metodo sopra descritto.

## Utilizzando la crittografia `C# RandomNumberGenerator`

Se si vogliono generare numeri casuali veramente unici, si può utilizzare la classe `RandomNumberGenerator`, che fa parte della libreria `System.Security.Cryptography`.

Questa classe genera un numero casuale crittograficamente sicuro e adatto alla creazione di una password casuale.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Possiamo anche passare un intervallo al metodo `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Utilizzo della classe `C# RNGCryptoServiceProvider` 

Questa classe è ormai obsoleta, non utilizzare questo metodo.

`RNGCryptoServiceProvider` implementa un generatore di numeri casuali (RNG) crittografico utilizzando l'implementazione fornita dal fornitore di servizi crittografici (CSP).

Utilizzare il codice seguente per creare un numero casuale con la classe ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Riepilogo

In questa esercitazione abbiamo imparato diversi modi per generare numeri casuali in C# con semplici esempi.

















