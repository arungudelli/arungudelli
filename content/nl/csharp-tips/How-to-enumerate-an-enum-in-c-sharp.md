---
title: "Hoe enumereren C# enum"
description: " Verschillende manieren om enumereren C# enum met voorbeelden"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums worden veel gebruikt in `C#` taal. 

En er zijn 4 manieren om enumerate enum in `C#`. 

1. `C# Enum.GetValues()` gebruiken in .Net 5 en hoger.
2. `C# Enum.GetValues()` gebruiken in oudere .Net versies.
3. Gebruik van `C# Enum.GetNames()` om enumerate enum namen als strings.
4. Gebruik van `Linq`

Laten we een voorbeeld doornemen om het verder te begrijpen. 

Eerst maken we een C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

De `enum` staat voor verschillende soorten logboekniveaus.

Nu zullen we verschillende manieren zien om de enumerate van de `C# enum`.

## `C# Enum.GetValues()` Generieke methode te gebruiken in .Net 5 &amp; hoger

Als u de laatste versie van `.Net` gebruikt, d.w.z. `.Net 5` en hoger, kunt u de generieke versie van de `Enum.GetValues` methode gebruiken om enumde `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

De nieuwe generieke versie van `Enum.GetValues` geeft de array van enum waarden terug. 

En verder kunnen we de verklaringen `for` of `foreach` gebruiken om de `C# enum` namen. 

Aangezien de array het `enum` type bevat, moeten we het converteren naar de string met de methode `ToString()`.

## Gebruik `C# Enum.GetValues()` in oudere .Net versies.

In de oudere versies van `.Net` is er geen generieke methode beschikbaar voor de methode `Enum.GetValues()`. 

U moet `typeof()` enum als parameter doorgeven aan de methode `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
En het geeft enum waarden terug van het type `System.Array` en verder kunnen we `foreach` statement gebruiken om door de `C# enum` namen.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Als u een `IEnumerable` resultaat wilt, kunnen we de methode `Enum.GetValues()` verder casten.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## `C# Enum.GetNames()` gebruiken om enumerate enum namen als strings te gebruiken 

`C# Enum.GetValues()` geeft de methode een array van enum types. 

Daarom hebben we enum namen geconverteerd naar string voordat we ze afdrukken in de console.

Met de methode `C# Enum.GetNames()` kunnen we enumeren enum namen als strings, zodat het niet nodig is ze te converteren naar strings.

Als u `.Net 5` en hoger gebruikt, kunt u de generieke functie `C# Enum.GetNames()` gebruiken.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

In de oudere versies moeten we de parameter `typeof()` enum doorgeven.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Dus als u en enumnamen als strings wilt gebruiken, kunnen we de methode `C# Enum.GetNames()` gebruiken.

## Met behulp van `Linq`

We kunnen `Linq forEach` methode gebruiken om enumerate C# enum, met behulp van `Enum.GetValues()` en `Enum.GetNames()` methoden.

Gebruik in `.Net 5` en hoger het onderstaande codefragment.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

In de oudere versies

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Samenvatting

In deze tutorial hebben we geleerd om enumerate enum in C# met behulp van `Enum.GetValues()` en `Enum.GetNames()` methode.










