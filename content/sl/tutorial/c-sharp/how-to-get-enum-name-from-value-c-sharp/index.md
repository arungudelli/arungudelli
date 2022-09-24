
+++
title="Kako iz vrednosti v jeziku C# pridobiti ime enum"
summary=" V jeziku C# lahko iz vrednosti pridobite ime enum na dva načina 1. Za pridobitev imena uporabite C# `Enum.GetName()` in kot parameter posredujete vrednost enum. 2. 2. Pretvorite vrednost enum v enumeration member z uporabo casting in nato uporabite metodo `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Eden od priljubljenih primerov uporabe metode enum je pridobivanje imena enum iz njene vrednosti.

Če upoštevamo primer iz resničnega sveta, bomo na splošno v podatkovni bazi shranili vrednosti enum. To pomeni, da bomo shranili samo celoštevilske vrednosti 

In ko preberemo vrednost enum iz baze podatkov, jo moramo pretvoriti nazaj v njeno ime enum.

V jeziku C# obstajata **dva načina za pridobivanje imena enum iz vrednosti** 

{{%toc%}}

## Rešitev 1: Uporaba `Enum.GetName()`

C# `Enum.GetName()` funkcija sprejme dva parametra enum tip in vrednost ter vrne enum ime.

Vzemimo primer `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Zdaj bomo vrednost enum posredovali `Enum.GetName()`, da bi dobili ime enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Če uporabljate različico C# `.Net 6`, lahko metodi `Enum.GetName()` posredujete samo vrednost enum (cast to enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Rešitev 2: Uporaba tipskega kastinga

Drug način je, da pretvorite enum vrednost v enumeration member z uporabo casting in nato uporabite `ToString()` metodo.

To je preprost način, ki ne uporablja nobenih vgrajenih funkcij `C# Enum`.

Najprej pretvorite vrednost enum v član enumeration in nato uporabite metodo `ToString()`.

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

## Povzetek

V tem učbeniku smo se naučili različnih načinov za pridobitev vrednosti imena enum v c# 

1. S posredovanjem parametrov enum tipa in vrednosti metodi `Enum.GetName()` 
2. In z uporabo tipovnega kastinga na ustrezen tip enum 
