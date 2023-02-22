---
title: "Hoe C# enum te lussen/op te sommen"
description: "Verschillende manieren om C# enum te lussen of op te sommen met voorbeelden"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums worden veel gebruikt in de taal `C#`. 

En er zijn 4 manieren om enum te lussen of op te sommen in `C#`. 

1. `C# Enum.GetValues()` gebruiken in .Net 5 en hoger.
2. `C# Enum.GetValues()` gebruiken in oudere .Net versies.
3. `C# Enum.GetNames()` gebruiken om enumnamen als strings op te sommen.
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

De `enum` vertegenwoordigt verschillende soorten logging niveaus.

Nu zullen we verschillende manieren zien om de `C# enum` op te sommen.

## Gebruik van `C# Enum.GetValues()` Generieke methode in .Net 5 &amp; hoger

Als u de laatste versie van `.Net` gebruikt, d.w.z. `.Net 5` en hoger, kunt u de generieke versie gebruiken voor de methode `Enum.GetValues` om door de `C# enum` te lussen.

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

De nieuwe generieke versie van `Enum.GetValues` geeft de array van enumwaarden terug. 

En verder kunnen we `for` of `foreach` statements gebruiken om de `C# enum` op te sommen. 

Aangezien het array het type `enum` bevat, moeten we het converteren naar de string met de methode `ToString()`.

## Gebruik van `C# Enum.GetValues()` in oudere .Net versies.

In de oudere versies van `.Net` is er geen generieke methode beschikbaar voor de methode `Enum.GetValues()`. 

U moet `typeof()` enum als parameter doorgeven aan `Enum.GetValues()` methode. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
En het geeft enumwaarden terug van het type `System.Array` en verder kunnen we `foreach` statement gebruiken om door het C# enum te lussen.

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

Als u het resultaat `IEnumerable` wilt, kunnen we de methode `Enum.GetValues()` verder casten.

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

## `C# Enum.GetNames()` gebruiken om enumnamen als strings op te sommen 

`C# Enum.GetValues()` methode geeft array van enum types terug. 

Daarom hebben we enumwaarden geconverteerd naar string voordat we ze in de console afdrukken.

Met de methode `C# Enum.GetNames()` kunnen we enumnamen als strings opsommen, zodat het niet nodig is ze naar strings te converteren.

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

In de oudere versies moeten we `typeof()` enum parameter doorgeven.

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

Dus als u enum-namen als strings wilt lussen, kunt u de methode `C# Enum.GetNames()` gebruiken.

## Met behulp van `Linq`

We kunnen `Linq forEach` methode gebruiken om C# enum op te sommen, met behulp van `Enum.GetValues()` en `Enum.GetNames()` methoden.

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

In deze tutorial hebben we geleerd om door enum te lussen in C# met behulp van `Enum.GetValues()` en `Enum.GetNames()` methode.










