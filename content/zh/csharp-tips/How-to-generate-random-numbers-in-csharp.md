
---
title: "如何在C#中生成随机数"
description: "在C#中生成随机数的不同方法和简单的例子。"
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


随机数广泛用于数字游戏、统计取样、密码学、统计物理学的计算、数值分析、无线电通信和轮盘等赌场游戏。 

我们可以**使用`Random` 类来生成C#中的随机数**。

## 什么是`C# Random` 类？

`C# Random` 类是一个伪随机数生成器，它是一种算法，可以生成符合某些随机性统计要求的数字序列。

这个类有5个方法`Next()`,`NextInt64()`,`NextBytes()`,`NextDouble()` 和`NextSingle()` 。 

根据数字的类型，即`int` 、`long` 等，我们可以使用相应的方法。

让我们通过这些例子来进一步了解它。 

## 在C#中生成随机整数 

在C#中生成随机整数的步骤 

1.实例化随机数类。
2.使用`Random.Next()` 方法来返回`Int32.MinValue` 和`Int32.MaxValue` 之间的随机整数。

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

### 生成最小值和最大值之间的随机整数

`Random.Next()` 有一个重载方法，它接受最小值和最大值作为参数，在给定值之间生成一个随机的整数。

要生成100到1000之间的随机数，请使用下面的代码

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

## 在C#中生成随机的长数字(Int64) 

要在C#中生成随机长数，即`Int64` ，请使用`Random.NextInt64()` 方法，该方法返回`Int64.MinValue` 和`Int64.MaxValue` 之间的随机数`Int64` 。

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

### 在给定范围内生成随机长数(Int64)

与`Random.Next()` 相似，`Random.NextInt64()` 有一个重载方法，它接受Range，即最小值和最大值作为参数，返回它们之间的一个随机`Int64` 。

要生成100000到200000之间的随机数，请使用下面的代码

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

生成的随机数不是完全随机的，因为使用了一种数学算法来选择它们，但它们对于大多数现实世界的情况来说是足够好的。

## 在生成随机数时避免重复

如果你要初始化一个以上的`new Random()` 类。 

你可能会得到重复的随机数。(多线程的应用程序)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

所以最好只初始化一个`Random()` 类实例，并在整个应用程序中使用它。

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
如果你想生成一系列的随机数，在多线程环境中使用上述方法。

## 使用密码学`C# RandomNumberGenerator`

如果你想生成真正唯一的随机数，你可以使用`RandomNumberGenerator` ，该类是`System.Security.Cryptography` 库的一部分。

这个类可以生成一个加密安全的随机数，并适用于创建一个随机密码。

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

我们也可以将范围传递给`RandomNumberGenerator` 方法。

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## 使用`C# RNGCryptoServiceProvider` 类

这个类现在已经过时了，不要再使用这个方法。

`RNGCryptoServiceProvider` 使用加密服务提供商（CSP）提供的实现，实现一个加密的随机数发生器（RNG）。

使用下面的代码用` C# RNGCryptoServiceProvider` 类创建一个随机数。

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## 摘要

在本教程中，我们通过简单的例子学习了在C#中生成随机数的不同方法。

















