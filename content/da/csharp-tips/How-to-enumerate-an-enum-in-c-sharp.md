---
title: "Sådan enumerate C# enum"
description: " Forskellige måder at enumerate C# enum med eksempler"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums er meget udbredt i `C#` sproget. 

Og der er 4 måder at enumerate enum i `C#`. 

1. Brug af `C# Enum.GetValues()` i .Net 5 og derover.
2. Brug af `C# Enum.GetValues()` i ældre .Net-versioner.
3. Brug af `C# Enum.GetNames()` til enumerate enum navne som strenge.
4. Brug af `Linq`

Lad os gennemgå et eksempel for at forstå det nærmere. 

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

The `enum` repræsenterer forskellige typer af logningsniveauer.

Nu vil vi se forskellige måder at enumerate the `C# enum`.

## Brug af `C# Enum.GetValues()` Generisk metode i .Net 5 og derover

Hvis du bruger den nyeste version af `.Net`, dvs. `.Net 5` og derover, kan du bruge den generiske version af `Enum.GetValues` -metoden til at enumerate den `C# enum`.

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

Den nye generiske version af `Enum.GetValues` returnerer arrayet af enum -værdier. 

Desuden kan vi bruge `for` eller `foreach` til at opstille en liste over de `C# enum` navne. 

Da arrayet indeholder de `enum` type, skal vi konvertere den til en streng ved hjælp af `ToString()` -metoden.

## Brug af `C# Enum.GetValues()` i ældre .Net-versioner.

I de ældre versioner af `.Net` er der ingen generisk metode til rådighed for `Enum.GetValues()` -metoden. 

Du skal sende `typeof()` enum som en parameter til `Enum.GetValues()` -metoden. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Og den returnerer enum værdier af typen `System.Array` og yderligere kan vi bruge `foreach` -erklæringen til at gennemløbe `C# enum` navne.

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

Hvis du vil have `IEnumerable` resultatet, kan vi yderligere kaste `Enum.GetValues()` metoden.

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

## Brug af `C# Enum.GetNames()` til enumerate enum navne som strenge 

`C# Enum.GetValues()` metoden returnerer et array af enum typer. 

Derfor konverterede vi enum navne til strenge, før vi udskrev dem i konsollen.

Ved hjælp af `C# Enum.GetNames()` metoden kan vi enumerate enum navne som strenge, så det ikke er nødvendigt at konvertere dem til strenge.

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

I de ældre versioner skal vi sende `typeof()` enum parameteren.

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

Så hvis du ønsker at enumerate navne som strenge, kan vi bruge `C# Enum.GetNames()` metoden.

## Brug af `Linq`

Vi kan bruge `Linq forEach` metoden til at enumerate C# enum, ved hjælp af `Enum.GetValues()` og `Enum.GetNames()` metoderne.

I `.Net 5` og derover kan du bruge nedenstående kodestump.

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

I denne tutorial har vi lært at enumerate enum i C# ved hjælp af `Enum.GetValues()` og `Enum.GetNames()` metoden.










