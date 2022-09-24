
+++
title="Kaip gauti enum pavadinimą iš reikšmės C# kalba"
summary="Yra du būdai, kaip gauti enum pavadinimą iš reikšmės C# kalba 1. Naudokite C# `Enum.GetName()` ir kaip parametrą perduokite enum reikšmę, kad gautumėte pavadinimą. 2. 2. Konvertuoti enum reikšmę į enumeration narį naudojant kastingą ir tada naudoti `ToString()` metodą."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Vienas iš populiarių enum naudojimo atvejų - gauti enum vardą iš jo reikšmės.

Panagrinėkime realaus pasaulio pavyzdį, paprastai duomenų bazėje laikysime enum reikšmes, t. y. laikysime tik sveikųjų skaičių reikšmes 

O nuskaitę enum reikšmę iš duomenų bazės turime ją konvertuoti atgal į jos enum vardą.

Yra du būdai, kaip iš reikšmės gauti enum vardą C#** 

{{%toc%}}

## 1 sprendimas: naudojant `Enum.GetName()`

C# `Enum.GetName()` funkcija priima du parametrus enum type ir value ir grąžina enum pavadinimą.

Paimkime pavyzdį `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Dabar perduosime enum reikšmę `Enum.GetName()`, kad gautume enum pavadinimą 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Jei naudojate C# `.Net 6` versiją, `Enum.GetName()` metodui galite perduoti tik enum reikšmę (cast į enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## 2 sprendimas: naudojant tipo atvaizdavimą

Kitas būdas yra, Konvertuoti enum reikšmę į enumeration narį naudojant liejimą ir tada naudoti `ToString()` metodą.

Tai paprastas būdas, kuriam nenaudojamos jokios `C# Enum` integruotos funkcijos.

Pirmiausia konvertuokite enum reikšmę į enumeration member ir tada naudokite `ToString()` metodą.

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

## Santrauka

Šioje pamokoje sužinojome įvairių būdų, kaip gauti enum vardo reikšmę c# kalba 

1. Perduodami enum tipo ir vertės parametrus `Enum.GetName()` metodui
2. Ir naudojant tipo atvaizdavimą į atitinkamą enum tipą 
