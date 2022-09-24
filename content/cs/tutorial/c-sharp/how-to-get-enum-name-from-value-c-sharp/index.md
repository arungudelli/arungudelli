
+++
title="Jak získat název enum z hodnoty v jazyce C#"
summary="Existují dva způsoby, jak získat název enum z hodnoty v jazyce C# 1. Použijte C# `Enum.GetName()` a předejte enum hodnotu jako parametr pro získání jména. 2. 2. Převést enum hodnotu na enumerační člen pomocí castingu a poté použít metodu `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Jedním z oblíbených případů použití enum je získání enum jména z jeho hodnoty.

Uvažujme reálný příklad, obecně budeme v databázi ukládat hodnoty enum. Tj. budeme ukládat pouze celočíselné hodnoty 

A po načtení hodnoty enum z databáze ji musíme převést zpět na její název enum.

Existují **dva způsoby, jak v jazyce C# získat z hodnoty enum název** 

{{%toc%}}

## Řešení 1: Pomocí `Enum.GetName()`

C# `Enum.GetName()` funkce přijímá dva parametry enum typ a hodnotu a vrací název enum.

Vezměme si příklad `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Nyní předáme hodnotu enum enmu `Enum.GetName()`, abychom získali název enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Pokud používáte verzi `.Net 6` v jazyce C#, můžete metodě `Enum.GetName()` předat pouze hodnotu enum (cast na enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Řešení 2: Použití typového odlitku

Dalším způsobem je, Převést hodnotu enum na enumeration member pomocí castingu a poté použít metodu `ToString()`.

Jedná se o jednoduchý způsob, který nevyužívá žádné vestavěné funkce `C# Enum`.

Nejprve převedeme hodnotu enum na člen enumeration a poté použijeme metodu `ToString()`.

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

## Shrnutí

V tomto tutoriálu jsme se naučili různé způsoby, jak získat hodnotu názvu enum v jazyce c# 

1. Předáním parametrů typu a hodnoty enum metodě `Enum.GetName()` 
2. A pomocí typového odlitku na odpovídající typ enum 
