
+++
title="Как да получа enum име от стойност в C#"
summary="Има два начина за получаване на enum име от стойност в C# 1. Използвайте C# `Enum.GetName()` и подайте enum стойност като параметър, за да получите името. 2. Конвертирайте enum стойността в enumерационен член, като използвате casting, и след това използвайте `ToString()` метода."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Един от популярните случаи на използване на enum е получаването на enum име от неговата стойност.

Разгледайте един пример от реалния свят, като цяло в базата данни ще съхраняваме enum стойности, т.е. ще съхраняваме само целочислени стойности 

И след като прочетем стойността enum от базата данни, трябва да я преобразуваме обратно в нейното име enum.

Съществуват **два начина за получаване на enum име от стойност в C#** 

{{%toc%}}

## Решение 1: Използване на `Enum.GetName()`

C# функцията `Enum.GetName()` приема два параметъра enum type и value и връща името enum.

Да вземем за пример `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Сега ще предадем стойността enum на `Enum.GetName()`, за да получим името enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Ако използвате C# версия на `.Net 6`, можете да подадете само enum стойност (cast to enum) на метода `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Решение 2: Използване на хвърляне на типове

Друг начин е да, Конвертирате enum стойност в enumчлен на ерация, като използвате леене на тип, и след това използвате `ToString()` метод.

Това е прост начин, при който не се използват никакви вградени функции на `C# Enum`.

Първо конвертирайте enum стойността в enumeration member и след това използвайте `ToString()` метода.

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

## Обобщение

В този урок научихме различни начини за получаване на стойност на име enum в c# 

1. Чрез предаване на параметрите enum type и value на метода `Enum.GetName()` 
2. И чрез използване на type casting към съответния enum тип 
