
---
title: "Como gerar números aleatórios em C#"
description: "Diferentes maneiras de gerar números aleatórios em C# com exemplos simples."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Os números aleatórios são amplamente utilizados em jogos digitais, amostragem estatística, criptografia, cálculos em física estatística, análise numérica, comunicação via rádio e jogos de cassino como roda de roleta, etc 

Podemos **utilizar a classe `Random` para gerar números aleatórios em C#***.

## O que é `C# Random` Classe?

`C# Random` a classe é um gerador de números pseudo-aleatórios, que é um algoritmo que gera uma seqüência de números que satisfazem certos requisitos estatísticos de aleatoriedade.

Esta classe tem 5 métodos `Next()`, `NextInt64()`,`NextBytes()`, `NextDouble()` e `NextSingle()` 

Dependendo do tipo de Número, ou seja, `int`,`long` etc., podemos usar o método correspondente.

Vamos analisar os exemplos para entendê-los melhor 

## Gerar número inteiro aleatório em C# 

Passos para gerar um número inteiro aleatório em C# 

1. Classe de números aleatórios instantâneos.
2. Utilize o método `Random.Next()` para retornar inteiros aleatórios entre `Int32.MinValue` e `Int32.MaxValue`.

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

### Gerar um inteiro aleatório entre valores mínimos e máximos

`Random.Next()` tem um método sobrecarregado, que aceita valores mínimos e máximos como parâmetros que geram um número inteiro aleatório entre os valores dados.

Para gerar números aleatórios entre 100 e 1000, use o código abaixo

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

Para gerar um número longo aleatório, ou seja, `Int64` em C#, use o método `Random.NextInt64()` que retorna um número `Int64` aleatório entre `Int64.MinValue` e `Int64.MaxValue`.

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

Similar a `Random.Next()`, `Random.NextInt64()` tem um método sobrecarregado, que aceita Faixa, ou seja, valores mínimos e máximos como parâmetros que retornam um número `Int64` aleatório entre eles.

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

Os números aleatórios gerados não são completamente aleatórios porque um algoritmo matemático é usado para selecioná-los, mas eles são suficientemente bons para a maioria dos casos do mundo real.

## Evitando duplicatas ao gerar números aleatórios

Se você estiver inicializando mais de uma classe `new Random()` 

Você pode receber duplicatas de números aleatórios. (Aplicação multithreaded)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

Portanto, é melhor inicializar apenas uma instância da classe `Random()`, e utilizá-la em toda a aplicação.

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
Se você quiser gerar séries de números aleatórios, em ambiente multi-tarefa, use o método acima.

## Usando criptográfico `C# RandomNumberGenerator`

Se você quiser gerar números aleatórios verdadeiramente únicos, você pode fazer uso da classe `RandomNumberGenerator` que faz parte da biblioteca `System.Security.Cryptography`.

Esta classe gera um número aleatório criptograficamente seguro e adequado para a criação de uma senha aleatória.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

Também podemos passar o alcance para o método `RandomNumberGenerator`.

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

## Usando `C# RNGCryptoServiceProvider` classe

Esta classe está obsoleta agora, não use este método.

`RNGCryptoServiceProvider` implementa um gerador de números aleatórios criptográficos (RNG) utilizando a implementação fornecida pelo fornecedor de serviços criptográficos (CSP).

Use o código abaixo para criar um número aleatório com a classe ` C# RNGCryptoServiceProvider`.

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## Resumo

Neste tutorial aprendemos diferentes maneiras de gerar números aleatórios em C# com exemplos simples.

















