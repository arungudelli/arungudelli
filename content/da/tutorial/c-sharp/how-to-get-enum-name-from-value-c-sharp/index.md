
+++
title="Sådan får du enum navn fra værdi i C#"
summary="Der er to måder at få enum navn fra værdi i C# 1. Brug C# `Enum.GetName()` og send enum værdi som parameter for at få navnet. 2. Konverter enum værdi til enumeration member ved hjælp af casting og brug derefter `ToString()` metoden."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


En af de populære anvendelser af enum er at få enum navnet fra dets værdi.

I et eksempel fra den virkelige verden vil vi generelt gemme enum -værdier i databasen, dvs. vi vil kun gemme heltalsværdier 

Og efter at have læst enum -værdien fra databasen skal vi konvertere den tilbage til dens enum -navn.

Der er **to måder at få enum navn fra værdi i C#** 

{{%toc%}}

## Løsning 1: Brug af `Enum.GetName()`

C# `Enum.GetName()` funktionen tager to parametre enum type og værdi og returnerer enum navnet.

Tag et eksempel på `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Nu skal vi sende værdien enum til `Enum.GetName()` for at få navnet enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Hvis du bruger C# `.Net 6` -versionen, kan du kun sende enum -værdien (kastet til enum) til `Enum.GetName()` -metoden.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Løsning 2: Brug af type casting

En anden måde er at konvertere enum -værdien til enum-elementet ved hjælp af casting og derefter bruge `ToString()` -metoden.

Dette er en enkel måde, som ikke bruger nogen `C# Enum` indbyggede funktioner.

Først konverteres enum -værdien til enumeration-elementet, og derefter anvendes `ToString()` -metoden.

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

## Resumé

I denne tutorial lærte vi forskellige måder at få enum name value i c# 

1. Ved at sende enum type- og værdiparametre til `Enum.GetName()` -metoden
2. Og ved at bruge type casting til den tilsvarende enum type 
