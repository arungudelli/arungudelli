---
title: "Kako narediti zanko ali naštevanje C# enum"
description: "Različni načini zanke ali naštevanja C# enum s primeri"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumi se pogosto uporabljajo v jeziku `C#`. 

In obstajajo 4 načini, kako narediti zanko ali našteti enum v `C#`. 

1. Uporaba `C# Enum.GetValues()` v .Net 5 in novejših različicah.
2. Uporaba `C# Enum.GetValues()` v starejših različicah .Net.
3. Uporaba `C# Enum.GetNames()` za naštevanje imen enumov kot nizov.
4. Uporaba `Linq`

Za boljše razumevanje si oglejmo primer. 

Najprej bomo ustvarili program C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` predstavlja različne vrste nivojev beleženja.

Zdaj si bomo ogledali različne načine naštevanja `C# enum`.

## Uporaba generične metode `C# Enum.GetValues()` v .Net 5 in novejših različicah

Če uporabljate najnovejšo različico `.Net`, tj. `.Net 5` in višje, lahko uporabite generično različico za metodo `Enum.GetValues`, s katero se v zanki prebijete skozi `C# enum`.

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

Nova generična različica metode `Enum.GetValues` vrne polje vrednosti enumov. 

 `C# enum`V nadaljevanju lahko za naštevanje uporabimo stavke `for` ali `foreach`. 

Ker polje vsebuje tip `enum`, ga moramo pretvoriti v niz z uporabo metode `ToString()`.

## Uporaba `C# Enum.GetValues()` v starejših različicah .Net.

V starejših različicah `.Net` za metodo `Enum.GetValues()` ni na voljo generične metode. 

Metodi `Enum.GetValues()` morate kot parameter posredovati enum `typeof()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
In ta vrne vrednosti enuma tipa `System.Array`, v nadaljevanju pa lahko uporabimo stavek `foreach`, da naredimo zanko skozi enum C#.

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

Če želite rezultat `IEnumerable`, lahko metodo `Enum.GetValues()` še dodatno izdelamo.

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

## Uporaba `C# Enum.GetNames()` za naštevanje imen enumov kot nizov 

`C# Enum.GetValues()` metoda vrne polje tipov enumov. 

Zato smo vrednosti enumov pretvorili v niz, preden smo jih natisnili v konzolo.

Z metodo `C# Enum.GetNames()` lahko naštejemo imena enumov kot nize, tako da jih ni treba pretvoriti v nize.

Če uporabljate `.Net 5` in višje, lahko uporabite splošno funkcijo `C# Enum.GetNames()`.

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

V starejših različicah moramo posredovati parameter `typeof()` enum.

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

Če torej želimo imena enumov v obliki nizov, lahko uporabimo metodo `C# Enum.GetNames()`.

## Uporaba `Linq`

 `Linq forEach` lahko uporabimo metodo za naštevanje C# enumov s pomočjo metod `Enum.GetValues()` in `Enum.GetNames()`.

V `.Net 5` in višje uporabite spodnji del kode.

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

V starejših različicah

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

## Povzetek

V tem učbeniku smo se naučili, kako z metodo `Enum.GetValues()` in `Enum.GetNames()` zaciklirati enum v jeziku C#.










