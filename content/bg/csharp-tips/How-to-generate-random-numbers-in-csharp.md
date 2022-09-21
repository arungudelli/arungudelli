
---
title: "Как да генерираме случайни числа в C#"
description: "Различни начини за генериране на случайни числа в C# с прости примери."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Случайните числа се използват широко в цифровите игри, статистическите извадки, криптографията, изчисленията в статистическата физика, числения анализ, радиокомуникациите и казино игрите като рулетка и др 

Можем да **използваме класа `Random` за генериране на случайни числа в C#**.

## Какво представлява класът `C# Random`?

`C# Random` класът е генератор на псевдослучайни числа, който представлява алгоритъм, генериращ последователност от числа, отговарящи на определени статистически изисквания за случайност.

Този клас има 5 метода: `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` и `NextSingle()` 

В зависимост от вида на числото, т.е. `int`,`long` и т.н., можем да използваме съответния метод.

Нека разгледаме примерите, за да ги разберем по-подробно 

## Генериране на случайно цяло число на C# 

Стъпки за генериране на произволно цяло число в C# 

1. Инстанцирайте класа за случайни числа.
2. Използвайте метода `Random.Next()`, за да върнете случайно цяло число между `Int32.MinValue` и `Int32.MaxValue`.

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

### Генериране на случайно цяло число между минималната и максималната стойност

`Random.Next()` има претоварен метод, който приема минимални и максимални стойности като параметри и генерира произволно цяло число между зададените стойности.

За да генерирате случайни числа между 100 и 1000, използвайте следния код

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

## Генериране на случайно дълго число(Int64) в C# 

За да генерирате случайно дълго число, т.е. `Int64` в C#, използвайте метода `Random.NextInt64()`, който връща случайно число `Int64` между `Int64.MinValue` и `Int64.MaxValue`.

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

### Генериране на случайно дълго число(Int64) в даден диапазон

Подобно на `Random.Next()`, `Random.NextInt64()` има претоварен метод, който приема Range, т.е. минимална и максимална стойност като параметри, и връща случайно `Int64` число между тях.

За да генерирате случайни числа между 100000 и 200000, използвайте следния код

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

Генерираните случайни числа не са напълно случайни, тъй като за избора им се използва математически алгоритъм, но те са достатъчно добри за повечето случаи в реалния свят.

## Избягване на дублирания при генериране на случайни числа

Ако инициализирате повече от един клас `new Random()` 

Може да се получат дублиращи се случайни числа. (Многонишково приложение)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Затова е по-добре да инициализирате само една инстанция на класа `Random()` и да я използвате в цялото приложение.

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
Ако искате да генерирате поредица от случайни числа в многонишкова среда, използвайте горния метод.

## Използване на криптографски `C# RandomNumberGenerator`

Ако искате да генерирате наистина уникални случайни числа, можете да използвате класа `RandomNumberGenerator`, който е част от библиотеката `System.Security.Cryptography`.

Този клас генерира криптографски сигурни случайни числа и е подходящ за създаване на случайна парола.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Можем също така да подадем диапазон на метода `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Използване на класа `C# RNGCryptoServiceProvider` 

Този клас вече е остарял, не използвайте този метод.

`RNGCryptoServiceProvider` имплементира криптографски генератор на случайни числа (RNG), като използва реализацията, предоставена от доставчика на криптографски услуги (CSP).

Използвайте кода по-долу, за да създадете случайно число с помощта на класа ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Обобщение

В този урок научихме различни начини за генериране на случайни числа в C# с прости примери.

















