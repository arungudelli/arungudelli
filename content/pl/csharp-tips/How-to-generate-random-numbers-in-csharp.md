
---
title: "How to Generate Random Numbers in C#"
description: "Różne sposoby generowania liczb losowych w C# z prostymi przykładami."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Liczby losowe są szeroko stosowane w grach cyfrowych, próbkowaniu statystycznym, kryptografii, obliczeniach w fizyce statystycznej, analizie numerycznej, komunikacji radiowej i grach kasynowych takich jak koło ruletki itp 

Możemy **używać klasy `Random` do generowania liczb losowych w C#**.

## Czym jest klasa `C# Random`?

`C# Random` klasa jest generatorem liczb pseudolosowych, czyli algorytmem, który generuje ciąg liczb spełniających pewne statystyczne wymagania dotyczące losowości.

Klasa ta posiada 5 metod `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` oraz `NextSingle()` 

W zależności od typu liczby, np. `int`,`long` itd. możemy użyć odpowiedniej metody.

Przejdźmy przez przykłady, aby zrozumieć to dalej 

## Generowanie losowej liczby całkowitej w C# 

Kroki do wygenerowania losowej liczby całkowitej w C# 

1. Zainicjuj klasę liczb losowych.
2. Użyj metody `Random.Next()` aby zwrócić losową liczbę całkowitą pomiędzy `Int32.MinValue` a `Int32.MaxValue`.

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

### Wygeneruj losową liczbę całkowitą pomiędzy wartością minimalną i maksymalną

`Random.Next()` posiada przeciążoną metodę, która przyjmuje jako parametry wartości minimalną i maksymalną, która generuje losową liczbę całkowitą pomiędzy podanymi wartościami.

Aby wygenerować losowe liczby pomiędzy 100 a 1000 użyj poniższego kodu

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

## Generowanie losowej długiej liczby(Int64) w C# 

Aby wygenerować Losową liczbę długą, tj. `Int64` w C#, użyj metody `Random.NextInt64()`, która zwraca losową liczbę `Int64` pomiędzy `Int64.MinValue` a `Int64.MaxValue`.

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

### Generowanie losowej liczby długiej (Int64) w podanym zakresie

Podobnie jak `Random.Next()`, `Random.NextInt64()` ma przeciążoną metodę, która akceptuje Range, tj. wartości minimalne i maksymalne jako parametry, które zwracają losową `Int64` liczbę pomiędzy nimi.

Aby wygenerować losowe liczby pomiędzy 100000 a 200000 użyj poniższego kodu

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

Wygenerowane liczby losowe nie są całkowicie losowe, ponieważ do ich wyboru używany jest algorytm matematyczny, ale są one wystarczająco dobre dla większości przypadków w świecie rzeczywistym.

## Unikanie duplikatów podczas generowania liczb losowych

Jeśli inicjalizujesz więcej niż jedną klasę `new Random()` 

Możesz otrzymać zduplikowane liczby losowe. (Aplikacja wielowątkowa)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Więc lepiej jest zainicjować tylko jedną instancję klasy `Random()` i używać jej w całej aplikacji.

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
Jeśli chcesz wygenerować serię liczb losowych, w środowisku wielowątkowym użyj powyższej metody.

## Użycie kryptografii `C# RandomNumberGenerator`

Jeśli chcesz wygenerować naprawdę unikalne liczby losowe możesz skorzystać z klasy `RandomNumberGenerator`, która jest częścią biblioteki `System.Security.Cryptography`.

Klasa ta generuje kryptograficznie bezpieczne liczby losowe i nadaje się do tworzenia losowego hasła.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Możemy również przekazać zakres do metody `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Użycie klasy `C# RNGCryptoServiceProvider` 

Ta klasa jest teraz przestarzała, Nie używaj tej metody.

`RNGCryptoServiceProvider` implementuje kryptograficzny generator liczb losowych (RNG) przy użyciu implementacji dostarczonej przez dostawcę usług kryptograficznych (CSP).

Użyj poniższego kodu utwórz liczbę losową za pomocą klasy ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Streszczenie

W tym tutorialu poznaliśmy różne sposoby generowania liczb losowych w C# na prostych przykładach.

















