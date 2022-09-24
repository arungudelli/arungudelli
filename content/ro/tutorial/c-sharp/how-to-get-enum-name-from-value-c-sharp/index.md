
+++
title="Cum să obțineți numele enum din valoare în C#"
summary="Există două moduri de a obține numele enum din valoare în C# 1. Utilizați C# `Enum.GetName()` și treceți valoarea enum ca parametru pentru a obține numele. 2. 2. Convertiți valoarea enum în membrul enumeration folosind casting și apoi utilizați metoda `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Unul dintre cazurile populare de utilizare a enum este obținerea numelui enum din valoarea sa.

Să luăm un exemplu din lumea reală: în general, vom stoca valorile enum în baza de date, adică vom stoca numai valori întregi 

Și după ce citim valoarea enum din baza de date, trebuie să o convertim înapoi în numele enum.

Există **două moduri de a obține numele enum din valoare în C#** 

{{%toc%}}

## Soluția 1: Folosind `Enum.GetName()`

C# `Enum.GetName()` funcția ia doi parametri enum tip și valoare și returnează numele enum.

Să luăm un exemplu de `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Acum vom trece valoarea enum la `Enum.GetName()` pentru a obține numele enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Dacă utilizați versiunea C# `.Net 6`, puteți trece doar valoarea enum (transformată în enum) în metoda `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Soluția 2: Utilizarea turnării tipurilor

O altă modalitate este de a converti valoarea enum în membrul de tip enumfolosind turnarea și apoi de a utiliza metoda `ToString()`.

Aceasta este o metodă simplă care nu utilizează nicio funcție integrată `C# Enum`.

Mai întâi se convertește valoarea enum în membrul enumeration și apoi se utilizează metoda `ToString()`.

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

## Rezumat

În acest tutorial am învățat diferite moduri de a obține valoarea numelui enum în c# 

1. Prin trecerea parametrilor enum type și value la metoda `Enum.GetName()` 
2. Și prin utilizarea tipului de turnare în tipul corespunzător enum 
