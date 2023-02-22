---
title: "Como fazer loop/enumerar C# enum"
description: "Diferentes formas de fazer loop/enumerar C# enumerar com exemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Os enums são amplamente utilizados na língua `C#`. 

E há 4 maneiras de fazer loop ou enumerar enumerar em `C#`. 

1. Usando `C# Enum.GetValues()` em .Net 5 e acima.
2. Usando `C# Enum.GetValues()` em versões .Net mais antigas.
3. Usando `C# Enum.GetNames()` para enumerar nomes de enumeração como cordas.
4. Usando `Linq`

Passemos por um exemplo para o compreender melhor. 

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

O `enum` representa diferentes tipos de níveis de exploração madeireira.

Agora vamos ver diferentes formas de enumerar o `C# enum`.

## Usando `C# Enum.GetValues()` Método genérico em .Net 5 e acima

Se estiver a utilizar a última versão de `.Net`, ou seja, `.Net 5` e acima, pode utilizar a versão genérica para o método `Enum.GetValues` para fazer loop através do `C# enum`.

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

A nova versão genérica de `Enum.GetValues` devolve o conjunto de valores de enumeração. 

Além disso, podemos utilizar `for` ou `foreach` para enumerar as declarações `C# enum`. 

Como a matriz contém o tipo `enum`, precisamos de a converter para a string usando o método `ToString()`.

## Usando `C# Enum.GetValues()` em versões .Net mais antigas.

Nas versões mais antigas de `.Net` não há nenhum método genérico disponível para o método `Enum.GetValues()`. 

Tem de passar `typeof()` enum como parâmetro para o método `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
E devolve valores enuméricos do tipo `System.Array` e, além disso, podemos utilizar a declaração `foreach` para fazer o loop através do enum C#.

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

Se quiser o resultado `IEnumerable`, podemos ainda lançar o método `Enum.GetValues()`.

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

`C# Enum.GetValues()` método retorna matriz de tipos de enumeração. 

É por isso que convertemos valores enuméricos em cordel antes de os imprimirmos na consola.

Usando o método `C# Enum.GetNames()` podemos enumerar nomes de enumeração como cordas, para que não seja necessário convertê-los em cordas.

Se estiver a usar `.Net 5` e acima, pode usar a função genérica `C# Enum.GetNames()`.

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

Nas versões mais antigas, precisamos de passar o parâmetro `typeof()` enum.

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

Por isso, se quiser enumerar nomes como cordas, podemos utilizar o método `C# Enum.GetNames()`.

## Usando `Linq`

Podemos utilizar o método `Linq forEach` para enumerar C# enumerar, com a ajuda dos métodos `Enum.GetValues()` e `Enum.GetNames()`.

Em `.Net 5` e acima utilize o código abaixo.

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

## Resumo

Neste tutorial aprendemos a percorrer o enum em C# usando o método `Enum.GetValues()` e `Enum.GetNames()`.










