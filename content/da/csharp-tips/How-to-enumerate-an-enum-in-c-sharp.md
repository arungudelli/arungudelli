---
title: "Sådan laver du loop/optælling af C# enum"
description: "Forskellige måder at lave loop eller optælling af C# enum på med eksempler"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums er meget udbredt i `C#` sproget. 

Og der er 4 måder at loop eller opregne enum på i `C#`. 

1. Brug af `C# Enum.GetValues()` i .Net 5 og derover.
2. Brug af `C# Enum.GetValues()` i ældre .Net-versioner.
3. Brug af `C# Enum.GetNames()` til at opregne enum-navne som strenge.
4. Brug af `Linq`

Lad os gennemgå et eksempel for at forstå det yderligere. 

Først opretter vi en C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` repræsenterer forskellige typer logningsniveauer.

Nu vil vi se forskellige måder at opregne `C# enum` på.

## Brug af `C# Enum.GetValues()` Generisk metode i .Net 5 og derover

Hvis du bruger den nyeste version af `.Net`, dvs. `.Net 5` og derover, kan du bruge den generiske version af `Enum.GetValues` -metoden til at gennemløbe `C# enum`.

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

Den nye generiske version af `Enum.GetValues` returnerer arrayet af enum-værdier. 

Desuden kan vi bruge `for` - eller `foreach` -meddelelser til at opregne `C# enum`. 

Da arrayet indeholder typen `enum`, skal vi konvertere det til en streng ved hjælp af `ToString()` -metoden.

## Brug af `C# Enum.GetValues()` i ældre .Net-versioner.

I de ældre versioner af `.Net` er der ingen generisk metode til rådighed for `Enum.GetValues()` -metoden. 

Du skal sende `typeof()` enum som en parameter til `Enum.GetValues()` -metoden. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Og den returnerer enumværdier af typen `System.Array`, og vi kan bruge `foreach` -erklæringen til at gennemløbe C#-enummet.

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

Hvis du vil have `IEnumerable` -resultatet, kan vi yderligere kaste `Enum.GetValues()` -metoden.

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

## Brug af `C# Enum.GetNames()` til at opregne enum-navne som strenge 

`C# Enum.GetValues()` metoden returnerer et array af enum-typer. 

Derfor konverterede vi enum-værdierne til strenge, før vi udskrev dem i konsollen.

Ved hjælp af metoden `C# Enum.GetNames()` kan vi opregne enum-navne som strenge, så det ikke er nødvendigt at konvertere dem til strenge.

Hvis du bruger `.Net 5` og derover, kan du bruge den generiske `C# Enum.GetNames()` -funktion.

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

I de ældre versioner skal vi sende `typeof()` enum-parameteren.

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

Så hvis du ønsker at sløjfe enum-navne som strenge, kan vi bruge `C# Enum.GetNames()` -metoden.

## Brug af `Linq`

Vi kan bruge `Linq forEach` -metoden til at opregne C#-enum ved hjælp af `Enum.GetValues()` - og `Enum.GetNames()` -metoderne.

I `.Net 5` og derover skal du bruge nedenstående kodestump.

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

I de ældre versioner

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

## Resumé

I denne tutorial lærte vi at gennemløbe enum i C# ved hjælp af `Enum.GetValues()` og `Enum.GetNames()` metoden.










