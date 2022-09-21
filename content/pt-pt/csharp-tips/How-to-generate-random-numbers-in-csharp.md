
---
title: "Como gerar números aleatórios em C#"
description: "Diferentes formas de gerar números aleatórios em C# com exemplos simples."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Os números aleatórios são amplamente utilizados em Jogos Digitais, Amostragem Estatística, Criptografia, computações em física estatística, análise numérica, comunicações via rádio e jogos de casino como a roda da roleta, etc 

Podemos **utilizar `Random` classe para Gerar Números Aleatórios em C#***.

## O que é `C# Random` Classe?

`C# Random` classe é um gerador de números pseudo-aleatórios, que é um algoritmo que gera uma sequência de números que satisfazem certos requisitos estatísticos de aleatoriedade.

Esta classe tem 5 métodos `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` e `NextSingle()` 

Dependendo do tipo de Número i.e., `int`,`long` etc., podemos utilizar o método correspondente.

Passemos em revista os exemplos para o compreender melhor 

## Gerar número inteiro aleatório em C# 

Passos para gerar um número inteiro aleatório em C# 

1. Classe de números aleatórios instantâneos.
2. Utilizar o método `Random.Next()` para devolver um número inteiro aleatório entre `Int32.MinValue` e `Int32.MaxValue`.

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

### Gerar um inteiro aleatório entre os valores mínimo e máximo

`Random.Next()` tem um método sobrecarregado, que aceita valores mínimos e máximos como parâmetros que geram um número inteiro aleatório entre os valores dados.

Para gerar números aleatórios entre 100 e 1000 utilize o código abaixo

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

## Gerar número longo aleatório(Int64) em C# 

Para gerar um número longo aleatório, ou seja, `Int64` em C#, utilize o método `Random.NextInt64()` que devolve um número `Int64` aleatório entre `Int64.MinValue` e `Int64.MaxValue`.

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

### Gerar número longo aleatório(Int64) em Given Range

Semelhante a `Random.Next()`, `Random.NextInt64()` tem um método sobrecarregado, que aceita Gama, ou seja, valores mínimos e máximos como parâmetros que devolvem um número `Int64` aleatório entre eles.

Para gerar números aleatórios entre 100000 e 200000 utilize o código abaixo

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

Os números aleatórios gerados não são completamente aleatórios porque é utilizado um algoritmo matemático para os seleccionar, mas são suficientemente bons para a maioria dos casos do mundo real.

## Evitar duplicações ao gerar números aleatórios

Se estiver a inicializar mais do que uma classe `new Random()` 

Poderá obter duplicações de números aleatórios. (Aplicação multi-tarefa)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Por isso é melhor inicializar apenas uma instância de classe `Random()`, e utilizá-la em toda a aplicação.

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
Se quiser gerar séries de números aleatórios, em ambiente multi-tarefa utilize o método acima.

## Usando criptográfico `C# RandomNumberGenerator`

Se quiser gerar números aleatórios verdadeiramente únicos, pode fazer uso da classe `RandomNumberGenerator` que faz parte da biblioteca `System.Security.Cryptography`.

Esta classe gera um número aleatório criptograficamente seguro e adequado para a criação de uma senha aleatória.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Podemos também passar o alcance para o método `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Usando `C# RNGCryptoServiceProvider` classe

Esta classe está obsoleta agora, Não use este método.

`RNGCryptoServiceProvider` implementa um gerador criptográfico de números aleatórios (RNG) utilizando a implementação fornecida pelo fornecedor do serviço criptográfico (CSP).

Utilize o código abaixo para criar um número aleatório com a classe ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Resumo

Neste tutorial aprendemos diferentes formas de gerar números aleatórios em C# com exemplos simples.

















