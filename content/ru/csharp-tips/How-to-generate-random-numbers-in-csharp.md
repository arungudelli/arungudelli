
---
title: "Как генерировать случайные числа в C#"
description: "Различные способы генерации случайных чисел в C# с простыми примерами."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Случайные числа широко используются в цифровых играх, статистической выборке, криптографии, вычислениях в статистической физике, численном анализе, радиосвязи и играх казино, таких как рулетка и т.д 

Мы можем **использовать класс `Random` для генерации случайных чисел в C#**.

## Что такое класс `C# Random`?

`C# Random` class - это генератор псевдослучайных чисел, который представляет собой алгоритм, генерирующий последовательность чисел, отвечающих определенным статистическим требованиям к случайности.

Этот класс имеет 5 методов `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` и `NextSingle()` 

В зависимости от типа числа, т.е. `int`,`long` и т.д., мы можем использовать соответствующий метод.

Давайте рассмотрим примеры, чтобы понять это дальше 

## Генерация случайного целого числа в C# 

Шаги для генерации случайного целого числа в C# 

1. Инстанцируйте класс случайных чисел.
2. Используйте метод `Random.Next()`, чтобы вернуть случайное целое число между `Int32.MinValue` и `Int32.MaxValue`.

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

### Генерируем случайное целое число между минимальным и максимальным значениями

`Random.Next()` имеет перегруженный метод, принимающий в качестве параметров минимальное и максимальное значения, который генерирует случайное целое число между заданными значениями.

Для генерации случайных чисел от 100 до 1000 используйте следующий код

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

## Генерация случайного длинного числа(Int64) в C# 

Для генерации случайного длинного числа `Int64` в C# используйте метод `Random.NextInt64()`, который возвращает случайное число `Int64` между `Int64.MinValue` и `Int64.MaxValue`.

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

### Генерирование случайного длинного числа(Int64) в заданном диапазоне

Как и `Random.Next()`, `Random.NextInt64()` имеет перегруженный метод, который принимает Range, т.е. минимальное и максимальное значения в качестве параметров, и возвращает случайное число `Int64` между ними.

Для генерации случайных чисел в диапазоне от 100000 до 200000 используйте следующий код

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

Сгенерированные случайные числа не являются полностью случайными, поскольку для их выбора используется математический алгоритм, но они достаточно хороши для большинства реальных случаев.

## Избегание дубликатов при генерации случайных чисел

Если вы инициализируете более одного класса `new Random()` 

Вы можете получить дубликаты случайных чисел. (Многопоточное приложение)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Поэтому лучше инициализировать только один экземпляр класса `Random()` и использовать его во всем приложении.

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
Если вы хотите генерировать серию случайных чисел, в многопоточной среде используйте вышеуказанный метод.

## Использование криптографических `C# RandomNumberGenerator`

Если вы хотите генерировать действительно уникальные случайные числа, вы можете воспользоваться классом `RandomNumberGenerator`, который является частью библиотеки `System.Security.Cryptography`.

Этот класс генерирует криптографически защищенное случайное число и подходит для создания случайного пароля.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Мы также можем передать диапазон в метод `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Использование класса `C# RNGCryptoServiceProvider` 

Этот класс уже устарел, не используйте этот метод.

`RNGCryptoServiceProvider` реализует криптографический генератор случайных чисел (ГСЧ), используя реализацию, предоставленную поставщиком криптографических услуг (CSP).

Используйте приведенный ниже код для создания случайного числа с помощью класса ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Summary

В этом уроке мы изучили различные способы генерации случайных чисел в C# на простых примерах.

















