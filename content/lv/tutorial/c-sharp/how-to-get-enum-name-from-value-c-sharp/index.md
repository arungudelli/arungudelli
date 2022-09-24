
+++
title="Kā iegūt enum nosaukumu no vērtības C# valodā"
summary="Ir divi veidi, kā iegūt enum nosaukumu no vērtības C# valodā 1. Izmantojiet C# `Enum.GetName()` un kā parametru nododiet enum vērtību, lai iegūtu nosaukumu. 2. 2. Konvertēt enum vērtību uz enumerācijas locekli, izmantojot kastingu, un pēc tam izmantot `ToString()` metodi."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Viens no populārākajiem enum izmantošanas gadījumiem ir iegūt enum nosaukumu no tā vērtības.

Aplūkojiet reālās pasaules piemēru, parasti datu bāzē mēs glabāsim enum vērtības, t. i., mēs glabāsim tikai veselu skaitļu vērtības 

Un pēc enum vērtības nolasīšanas no datu bāzes mums tā jāpārveido atpakaļ uz enum nosaukumu.

Ir **divi veidi, kā no vērtības iegūt enum nosaukumu C#** 

{{%toc%}}

## Risinājums Nr. 1: Izmantojot `Enum.GetName()`

C# `Enum.GetName()` funkcija pieņem divus parametrus enum tips un vērtība un atgriež enum nosaukumu.

Ņemsim piemēru `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Tagad mēs nodosim enum vērtību `Enum.GetName()`, lai iegūtu enum nosaukumu 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Ja izmantojat C# `.Net 6` versiju, `Enum.GetName()` metodei varat nodot tikai enum vērtību (cast to enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Risinājums Nr. 2: izmantojot tipa atveidi

Cits veids ir, Konvertēt enum vērtību uz enumerācijas locekli, izmantojot kastingu, un pēc tam izmantot `ToString()` metodi.

Šis ir vienkāršs veids, kas neizmanto nevienu `C# Enum` iebūvēto funkciju.

Vispirms konvertējiet enum vērtību uz enumeration member un pēc tam izmantojiet `ToString()` metodi.

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

## Kopsavilkums

Šajā pamācībā mēs uzzinājām dažādus veidus, kā iegūt enum nosaukuma vērtību c# 

1. Nododot enum tipa un vērtības parametrus `Enum.GetName()` metodei
2. Un, izmantojot tipa atveidi, to pārveidojot uz atbilstošo enum tipu 
