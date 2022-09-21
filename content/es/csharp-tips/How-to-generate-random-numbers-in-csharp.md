
---
title: "Cómo generar números aleatorios en C#"
description: "Diferentes formas de generar números aleatorios en C# con ejemplos sencillos."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Los números aleatorios son ampliamente utilizados en juegos digitales, muestreo estadístico, criptografía, cálculos en física estadística, análisis numérico, comunicaciones de radio y juegos de casino como la ruleta, etc 

Podemos **utilizar la clase `Random` para generar números aleatorios en C#**.

## ¿Qué es la clase `C# Random`?

`C# Random` la clase  es un generador de números pseudo-aleatorios, que es un algoritmo que genera una secuencia de números que cumplen ciertos requisitos estadísticos de aleatoriedad.

Esta clase tiene 5 métodos `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` y `NextSingle()` 

Dependiendo del tipo de número, es decir, `int`,`long` etc podemos utilizar el método correspondiente.

Vamos a ver los ejemplos para entenderlo mejor 

## Generar un número entero aleatorio en C# 

Pasos para generar un entero aleatorio en C# 

1. Instanciar la clase de números aleatorios.
2. Utilice el método `Random.Next()` para devolver un número entero aleatorio entre `Int32.MinValue` y `Int32.MaxValue`.

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

### Generar un entero aleatorio entre los valores mínimo y máximo

`Random.Next()` tiene un método sobrecargado, que acepta los valores mínimo y máximo como parámetros que genera un entero aleatorio entre los valores dados.

Para generar números aleatorios entre 100 y 1000 utilice el siguiente código

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

## Generar números largos aleatorios(Int64) en C# 

Para generar un número largo aleatorio, es decir, `Int64` en C#, utilice el método `Random.NextInt64()` que devuelve un número aleatorio `Int64` entre `Int64.MinValue` y `Int64.MaxValue`.

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

### Generar un número largo aleatorio (Int64) en un rango dado

De forma similar a `Random.Next()`, `Random.NextInt64()` tiene un método sobrecargado, que acepta Range, es decir, los valores mínimo y máximo como parámetros que devuelven un número aleatorio `Int64` entre ellos.

Para generar números aleatorios entre 100000 y 200000 utilice el siguiente código

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

Los números aleatorios generados no son completamente aleatorios porque se utiliza un algoritmo matemático para seleccionarlos, pero son lo suficientemente buenos para la mayoría de los casos del mundo real.

## Evitar los duplicados al generar números aleatorios

Si estás inicializando más de una clase `new Random()` 

Podrías obtener números aleatorios duplicados. (Aplicación multihilo)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Así que es mejor inicializar sólo una instancia de la clase `Random()`, y utilizarla en toda la aplicación.

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
Si quieres generar series de números aleatorios, en un entorno multihilo utiliza el método anterior.

## Usando la criptografía `C# RandomNumberGenerator`

Si quieres generar números aleatorios realmente únicos puedes hacer uso de la clase `RandomNumberGenerator` que forma parte de la biblioteca `System.Security.Cryptography`.

Esta clase genera un número aleatorio criptográficamente seguro y adecuado para crear una contraseña aleatoria.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

También podemos pasar el rango al método `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Usando la clase `C# RNGCryptoServiceProvider` 

Esta clase es obsoleta ahora, no use este método.

`RNGCryptoServiceProvider` implementa un generador de números aleatorios (RNG) criptográfico utilizando la implementación proporcionada por el proveedor de servicios criptográficos (CSP).

Utilice el siguiente código para crear un número aleatorio con la clase ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Resumen

En este tutorial hemos aprendido diferentes formas de generar números aleatorios en C# con ejemplos sencillos.

















