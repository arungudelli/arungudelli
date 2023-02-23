---
title: "Como enumerar C# enum"
description: " Diferentes formas de enumerar C# enum com exemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Os enums são amplamente utilizados na língua `C#`. 

E há 4 maneiras de enumerate enum em `C#`. 

1. Usando `C# Enum.GetValues()` em .Net 5 e acima.
2. Usando `C# Enum.GetValues()` em versões .Net mais antigas.
3. Usando `C# Enum.GetNames()` a enumerguer nomes enum como cordas.
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

Agora veremos diferentes formas de enumerguer o `C# enum`.

## Usando `C# Enum.GetValues()` Método genérico em .Net 5 e acima

Se estiver a utilizar a última versão de `.Net`, ou seja, `.Net 5` e acima pode utilizar a versão genérica para o método `Enum.GetValues` para enumerate the `C# enum`.

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

A nova versão genérica de `Enum.GetValues` devolve o conjunto de valores enum. 

Além disso, podemos utilizar `for` ou `foreach` para listar as declarações `C# enum` nomes. 

Uma vez que a matriz contém o `enum` tipo, precisamos de o converter para a corda usando o método `ToString()`.

## Usando `C# Enum.GetValues()` em versões .Net mais antigas.

Nas versões mais antigas de `.Net` não há nenhum método genérico disponível para o método `Enum.GetValues()`. 

É necessário passar `typeof()` enum como parâmetro para o método `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
E devolve enum valores do tipo `System.Array` e, além disso, podemos usar a declaração `foreach` para fazer um loop através do `C# enum` nomes.

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

## Usando `C# Enum.GetNames()` a enumerguer nomes enum como cordas 

`C# Enum.GetValues()` método retorna matriz de tipos enum. 

É por isso que convertemos os nomes enum em cadeia antes de os imprimirmos na consola.

Usando o método `C# Enum.GetNames()` podemos enumerguer nomes enum como cordas, para que não seja necessário convertê-los em cordas.

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

Nas versões mais antigas, precisamos de passar o parâmetro `typeof()` enum .

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

Por isso, se quiserem em enumerguer nomes como cordas, podemos utilizar o método `C# Enum.GetNames()`.

## Usando `Linq`

Podemos utilizar o método `Linq forEach` para enumerate C# enum, com a ajuda dos métodos `Enum.GetValues()` e `Enum.GetNames()`.

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

Neste tutorial, aprendemos a enumerar enum em C# usando o método `Enum.GetValues()` e `Enum.GetNames()`.










