---
title: "Como fazer loop/enumerar C# enum"
description: "Diferentes formas de loop ou enumerar C# enumerar com exemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Os enumeros são amplamente utilizados na língua `C#`. 

E há 4 maneiras de loopar ou enumerar enumerar em `C#`. 

1. Usando `C# Enum.GetValues()` em .Net 5 e acima.
2. Usando `C# Enum.GetValues()` em versões .Net mais antigas.
3. Usando `C# Enum.GetNames()` para enumerar nomes de enumeração como cordas.
4. Usando `Linq`

Vamos passar por um exemplo para entendê-lo melhor. 

Primeiro vamos criar um C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

O `enum` representa diferentes tipos de níveis de extração.

Agora veremos diferentes maneiras de enumerar o `C# enum`.

## Usando `C# Enum.GetValues()` Método genérico em .Net 5 e acima

Se você estiver usando a última versão de `.Net`, ou seja, `.Net 5` e acima, você pode usar a versão genérica para o método `Enum.GetValues` para fazer loop através do `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

A nova versão genérica de `Enum.GetValues` retorna o conjunto de valores enuméricos. 

Além disso, podemos usar `for` ou `foreach` para enumerar as declarações `C# enum`. 

Como a matriz contém o tipo `enum`, precisamos convertê-la para a cadeia usando o método `ToString()`.

## Usando `C# Enum.GetValues()` em versões .Net mais antigas.

Nas versões anteriores de `.Net` não há nenhum método genérico disponível para o método `Enum.GetValues()`. 

Você precisa passar `typeof()` enum como parâmetro para o método `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
E retorna valores enuméricos do tipo `System.Array` e, além disso, podemos usar a declaração `foreach` para fazer um loop através do enum C#.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Se você quiser o resultado `IEnumerable`, podemos lançar ainda mais o método `Enum.GetValues()`.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## Usando `C# Enum.GetNames()` para enumerar nomes de enumeração como cordas 

`C# Enum.GetValues()` método retorna array de tipos de enumeração. 

É por isso que convertemos valores enuméricos em cadeia antes de imprimi-los no console.

Usando o método `C# Enum.GetNames()` podemos enumerar nomes de enumeração como cordas, para que não seja necessário convertê-las em cordas.

Se você estiver usando `.Net 5` e acima, você pode usar a função genérica `C# Enum.GetNames()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Nas versões mais antigas, precisamos passar o parâmetro `typeof()` enum.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Portanto, se você quiser enumerar nomes como cordas, podemos usar o método `C# Enum.GetNames()`.

## Usando `Linq`

Podemos usar o método `Linq forEach` para enumerar C# enumerar, com a ajuda dos métodos `Enum.GetValues()` e `Enum.GetNames()`.

Em `.Net 5` e acima, use o trecho de código abaixo.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

Nas versões mais antigas

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Sumário

Neste tutorial aprendemos a percorrer o enumero em C# usando o método `Enum.GetValues()` e `Enum.GetNames()`.










