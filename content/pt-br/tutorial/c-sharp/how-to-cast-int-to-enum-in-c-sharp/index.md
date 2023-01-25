+++
title   ="2 maneiras de converter/castar int para enum em C#"
summary ="Há 2 maneiras de moldar int para enum em C# 1. Usando C# fundição do tipo explícito. 2. Usando o método Enum.ToObject()"

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Há 2 maneiras de converter ou fundir `int` para `enum` em C#

1. Usando fundição do tipo C# explícito.
2. Usando o método `Enum.ToObject()` 

{{%toc%}}

## Solução 1: Usando fundição tipo C# explícita

A maneira simples de converter `int` para `enum` em C# é usar fundição de tipo explícito.

Vamos passar por um exemplo para entendê-lo melhor.

Nós temos um `enum` tipo chamado `LogLevel`, que representa diferentes níveis de extração.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Fundição explícita feita através da colocação do `enum` digite entre parênteses em frente ao valor `int`.

Mas há um problema com **C# `int` para `enum` conversão**.

E se o valor `int` não existir na variável C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Ele não abrirá nenhuma exceção.

Portanto, é melhor verificar se o valor `int` existe em `C# Enum` antes de lançá-lo ao número inteiro.

## Verifique se um número inteiro existe ou não em `C# enum` variável

Para obter todos os valores inteiros em `C# Enum`, podemos usar o método `Enum.GetValues`.

Convertê-los para a lista `C#`, para que possamos usar o método `list.Contains()` para verificar se o número inteiro em questão existe em `enum` variável.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Podemos usar o método `Enum.IsDefined()` para verificar se existe um valor inteiro convertido no `enum` tipo.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solução 2: Usar o método `Enum.ToObject()` 

Podemos usar o método `C# Enum.ToObject()`, converter o valor `int` para `enum` em C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





