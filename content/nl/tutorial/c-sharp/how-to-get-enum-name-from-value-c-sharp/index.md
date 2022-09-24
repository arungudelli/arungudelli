
+++
title="Hoe krijg ik enum naam van waarde in C#"
summary="Er zijn twee manieren om enum naam van waarde in C# 1. te krijgen. Gebruik C# `Enum.GetName()` en geef enum waarde door als parameter om de naam te krijgen. 2. 2. Converteer enum waarde naar het enumeration lid met behulp van casting en gebruik dan `ToString()` methode."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Een van de populaire toepassingen van enum is het verkrijgen van de naam enum uit zijn waarde.

Beschouw een voorbeeld uit de echte wereld: in het algemeen slaan we enum waarden op in de database, d.w.z. we slaan alleen gehele waarden op 

En na het lezen van de enum waarde uit de database moeten we die terug converteren naar de naam enum.

Er zijn **twee manieren om in C# enum naam uit waarde te halen** 

{{%toc%}}

## Oplossing 1: Met behulp van `Enum.GetName()`

C# `Enum.GetName()` functie neemt twee parameters enum type en waarde en geeft de enum naam terug.

Neem een voorbeeld van `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Nu zullen we de waarde enum doorgeven aan de `Enum.GetName()` om de naam enum te krijgen 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Als u de C# `.Net 6` versie gebruikt, kunt u alleen de enum waarde (gecast naar enum) doorgeven aan de `Enum.GetName()` methode.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Oplossing 2: Type casting gebruiken

Een andere manier is, enum waarde converteren naar het enumeration lid met behulp van casting en dan `ToString()` methode gebruiken.

Dit is een eenvoudige manier die geen gebruik maakt van `C# Enum` ingebouwde functies.

Converteer eerst enum waarde naar het enumeration lid en gebruik dan `ToString()` methode.

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

## Samenvatting

In deze tutorial hebben we verschillende manieren geleerd om enum naamwaarde te krijgen in c# 

1. Door enum type en waarde parameters door te geven aan de methode `Enum.GetName()` 
2. En door type casting te gebruiken naar corresponderend enum type 
