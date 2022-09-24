
+++
title="Hur får man fram enum namn från ett värde i C#"
summary="Det finns två sätt att få fram enum namn från ett värde i C# 1. Använd C# `Enum.GetName()` och skicka enum -värdet som parameter för att få fram namnet. 2. 2. Konvertera enum -värdet till enumeration member med hjälp av casting och använd sedan `ToString()` -metoden."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Ett av de populära användningsområdena för enum är att hämta enum -namnet från dess värde.

Om vi tar ett exempel från den verkliga världen kommer vi i allmänhet att lagra enum -värden i databasen, dvs. vi kommer endast att lagra heltalsvärden 

Efter att ha läst enum -värdet från databasen måste vi omvandla det tillbaka till dess enum -namn.

Det finns **två sätt att få fram enum namn från värde i C#** 

{{%toc%}}

## Lösning 1: Användning av `Enum.GetName()`

C# `Enum.GetName()` funktionen tar två parametrar enum type och value och returnerar enum name.

Ta ett exempel på `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Nu ska vi skicka värdet enum till `Enum.GetName()` för att få namnet enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Om du använder C# `.Net 6` -versionen kan du bara skicka enum -värdet (kastat till enum) till `Enum.GetName()` -metoden.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Lösning 2: Användning av typcasting

Ett annat sätt är att konvertera värdet enum till enumeration member med hjälp av casting och sedan använda `ToString()` -metoden.

Detta är ett enkelt sätt som inte använder några `C# Enum` inbyggda funktioner.

Konvertera först enum -värdet till enumeration member och använd sedan `ToString()` -metoden.

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

## Sammanfattning

I den här handledningen har vi lärt oss olika sätt att få fram enum name value i c# 

1. Genom att skicka enum typ- och värdeparametrar till `Enum.GetName()` -metoden
2. Och genom att använda type casting till motsvarande enum -typ 
