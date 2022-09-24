
+++
title="Como obter enum nome do valor em C#"
summary="Há duas maneiras de obter enum nome do valor em C# 1. Use C# `Enum.GetName()` e passe o valor enum como parâmetro para obter o nome. 2. Converter o valor enum para o membro da geração enumusando o método de fundição e depois usar o método `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Um dos casos de uso popular de enum é obter o nome enum a partir do seu valor.

Considere um exemplo do mundo real, geralmente armazenaremos valores enum no banco de dados, ou seja, armazenaremos apenas valores inteiros 

E após ler o valor enum do banco de dados, temos que convertê-lo de volta ao seu nome enum.

Existem **duas maneiras de obter enum nome do valor em C#*** 

{{%toc%}}

## Solução 1: Usando `Enum.GetName()`

A função C# `Enum.GetName()` toma dois parâmetros enum tipo e valor e retorna o nome enum.

Veja um exemplo de `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Agora vamos passar o valor enum para o `Enum.GetName()` para obter o nome enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Se você estiver usando a versão C# `.Net 6`, você pode passar apenas enum value(cast to enum) para o método `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Solução 2: Usando fundição do tipo

Outra maneira é converter o valor enum para o membro da geração enumusando o método de fundição e depois usar o método `ToString()`.

Esta é uma maneira simples que não utiliza nenhuma função `C# Enum` incorporada.

Primeiro converta o valor enum para o membro da geração enume depois use o método `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Sumário

Neste tutorial aprendemos diferentes maneiras de obter o valor do nome enum em c# 

1. Passando enum tipo e parâmetros de valor para o método `Enum.GetName()` 
2. E usando a fundição do tipo enum correspondente 
