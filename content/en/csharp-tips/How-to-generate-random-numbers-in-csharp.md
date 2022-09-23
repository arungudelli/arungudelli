---
title: "How to Generate Random Numbers (integers or long) in C#"
description: "Different ways to generate random numbers (integers or long) in C# with simple examples."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---


Random numbers are widely used in Digital games, Statistical Sampling, Cryptography, computations in statistical physics,numerical analysis,Radio communications and casino games like Roulette wheel etc. 

We can **use `Random` class to Generate Random Numbers in C#**.

## What is  `C# Random` Class?

`C# Random` class is a pseudo-random number generator, which is an algorithm that generates a sequence of numbers that meet certain statistical requirements for randomness.

This class has 5 methods `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` and `NextSingle()`. 

Depending upon on the type of Number i.e., `int`,`long` etc we can use corresponding method.

Let's go through the examples to understand it further. 

## Generate Random integer in C# 

Steps to generate Random integer in C# 

1. Instantiate random number class.
2. Use `Random.Next()` method to return random integer between `Int32.MinValue` and `Int32.MaxValue`.

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

### Generate Random integer between minimum and maximum values

`Random.Next()` has an overloaded method, which accepts minimum and maximum values as parameters which generates a random integer between the given values.

To generate random numbers between 100 to 1000 use the below code

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

## Generate Random long number(Int64) in C# 

To generate Random long number i.e, `Int64` in C#, Use `Random.NextInt64()` method which returns random `Int64` number between `Int64.MinValue` and `Int64.MaxValue`.

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

### Generate Random long number(Int64) in Given Range

Similar to `Random.Next()`, `Random.NextInt64()` has an overloaded method, which accepts Range i.e., minimum and maximum values as parameters which returns a random `Int64` number between them.

To generate random numbers between 100000 to 200000 use the below code

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

The generated random numbers are not completely random because a mathematical algorithm is used to select them, but they are good enough for most of the real world cases.

## Avoiding duplicates while generating random numbers

If you are initializing more than one `new Random()` class. 

You might get duplicates random numbers. (Multithreaded application)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

So it's better to initialize only one `Random()` class instance, and use it across the application.

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
If you want to generate series of random numbers, in multithreaded environment use above method.

## Using cryptographic `C# RandomNumberGenerator`

If you want to generate truly unique random numbers you can make use of `RandomNumberGenerator` class which is part of `System.Security.Cryptography` library.

This class generates a cryptographically secure random number and suitable for creating a random password.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

We can also pass range to the `RandomNumberGenerator` method.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Using `C# RNGCryptoServiceProvider` class

This class is obsolete now, Don't use this method.

`RNGCryptoServiceProvider` implements a cryptographic Random Number Generator (RNG) using the implementation provided by the cryptographic service provider (CSP).

Use the below code create a random number with the ` C# RNGCryptoServiceProvider` class.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Summary

In this tutorial we learnt different ways to generate random numbers in C# with simple examples.

















