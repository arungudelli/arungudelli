
+++
title="Ako získať názov enum z hodnoty v jazyku C#"
summary="Existujú dva spôsoby, ako získať názov enum z hodnoty v jazyku C# 1. Použite C# `Enum.GetName()` a odovzdajte enum hodnotu ako parameter na získanie mena. 2. 2. Konvertovať hodnotu enum na enumeration member pomocou castingu a potom použiť metódu `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Jedným z populárnych prípadov použitia enum je získanie enum názvu z jeho hodnoty.

Uvažujme reálny príklad, vo všeobecnosti budeme v databáze ukladať hodnoty enum. Teda budeme ukladať len celočíselné hodnoty 

A po načítaní hodnoty enum z databázy ju musíme previesť späť na jej názov enum.

Existujú **dva spôsoby, ako získať názov enum z hodnoty v jazyku C#** 

{{%toc%}}

## Riešenie 1: Použitie `Enum.GetName()`

C# `Enum.GetName()` funkcia prijíma dva parametre enum typ a hodnotu a vracia názov enum.

Vezmime si príklad `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Teraz odovzdáme hodnotu enum enumu `Enum.GetName()`, aby sme získali názov enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Ak používate verziu C# `.Net 6`, môžete metóde `Enum.GetName()` odovzdať iba hodnotu enum (cast na enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Riešenie 2: Použitie typového kastingu

Ďalším spôsobom je, Konvertovať hodnotu enum na enumeration member pomocou castingu a potom použiť metódu `ToString()`.

Ide o jednoduchý spôsob, ktorý nevyužíva žiadne vstavané funkcie `C# Enum`.

Najprv prekonvertujte hodnotu enum na enumeration member a potom použite metódu `ToString()`.

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

## Zhrnutie

V tomto návode sme sa naučili rôzne spôsoby, ako získať hodnotu názvu enum v jazyku c# 

1. Pomocou odovzdania parametrov typu enum a hodnoty metóde `Enum.GetName()` 
2. A pomocou typového kastingu na zodpovedajúci typ enum 
