+++
title   ="2 maneiras de converter/castar int para enum em C#"
summary ="Há 2 maneiras de moldar int para enum em C# 1. Usando a fundição do tipo explícito em C#. 2. Usando o método Enum.ToObject()"

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

1. Usando fundição de tipo explícito C#.
2. Usando o método `Enum.ToObject()` 

{{%toc%}}

## Solução 1: Usando fundição de tipo explícito C#

A forma simples de converter `int` para `enum` em C# é a utilização de fundição de tipo explícito.

Passemos por um exemplo para o compreender melhor.

Temos um `enum` tipo chamado `LogLevel`, que representa diferentes níveis de exploração madeireira.

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

Fundição explícita feita através da colocação do `enum` escreva entre parênteses em frente do valor `int`.

Mas há um problema com **C# `int` para `enum` conversão**.

E se o valor `int` não existir na variável C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Não irá lançar qualquer excepção.

Por isso é melhor verificar se o valor `int` existe em `C# Enum` antes de o lançar para o inteiro.

## Verificar se existe ou não um número inteiro em `C# enum` variável

Para obter todos os valores inteiros em `C# Enum`, podemos utilizar o método `Enum.GetValues`.

Convertê-los para a lista `C#`, para que possamos utilizar o método `list.Contains()` para verificar se o número inteiro em questão existe em `enum` variável.

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
Podemos utilizar o método `Enum.IsDefined()` para verificar se existe um valor inteiro convertido no dado `enum` tipo.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solução 2: Utilizar o método `Enum.ToObject()` 

Podemos usar o método `C# Enum.ToObject()`, converter o valor `int` para `enum` em C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





