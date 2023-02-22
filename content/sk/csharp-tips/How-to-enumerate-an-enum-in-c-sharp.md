---
title: "Ako vytvoriť cyklus/výpočet enumov v jazyku C#"
description: "Rôzne spôsoby vytvárania cyklov alebo enumov v jazyku C# s príkladmi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumy sú široko používané v jazyku `C#`. 

A existujú 4 spôsoby, ako zacykliť alebo vymenovať enum v `C#`. 

1. Používanie `C# Enum.GetValues()` v .Net 5 a vyšších verziách.
2. Použitie `C# Enum.GetValues()` v starších verziách .Net.
3. Použitie `C# Enum.GetNames()` na vymenovanie názvov enum ako reťazcov.
4. Používanie adresy `Linq`

Prejdime si príklad, aby sme ho lepšie pochopili. 

Najprv vytvoríme jazyk C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` predstavuje rôzne typy úrovní protokolovania.

Teraz si ukážeme rôzne spôsoby, ako vymenovať `C# enum`.

## Použitie `C# Enum.GetValues()` Generická metóda v .Net 5 a vyšších verziách

Ak používate najnovšiu verziu `.Net`, t. j. `.Net 5` a vyššiu, môžete použiť generickú verziu pre metódu `Enum.GetValues` na prechádzanie `C# enum`.

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

Nová generická verzia metódy `Enum.GetValues` vracia pole hodnôt enumu. 

A ďalej môžeme použiť príkazy `for` alebo `foreach` na vymenovanie `C# enum`. 

Keďže pole obsahuje typ `enum`, musíme ho previesť na reťazec pomocou metódy `ToString()`.

## Použitie `C# Enum.GetValues()` v starších verziách .net.

V starších verziách `.Net` nie je k dispozícii generická metóda pre metódu `Enum.GetValues()`. 

Metóde `Enum.GetValues()` musíte ako parameter odovzdať enum `typeof()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
A tá vracia enumové hodnoty typu `System.Array` a ďalej môžeme použiť príkaz `foreach` na prechádzanie enumov v jazyku C#.

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

Ak chceme výsledok `IEnumerable`, môžeme ďalej obsadiť metódu `Enum.GetValues()`.

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

## Použitie `C# Enum.GetNames()` na vymenovanie názvov enum ako reťazcov 

`C# Enum.GetValues()` metóda vracia pole typov enumov. 

Preto sme hodnoty enumov konvertovali na reťazec pred ich vypísaním do konzoly.

Pomocou metódy `C# Enum.GetNames()` môžeme vyčísliť názvy enumov ako reťazce, takže ich nie je potrebné konvertovať na reťazce.

Ak používate `.Net 5` a vyššie, môžete použiť generickú funkciu `C# Enum.GetNames()`.

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

V starších verziách musíme odovzdať parameter enum `typeof()`.

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

Ak teda chceme názvy enumov zacykliť ako reťazce, môžeme použiť metódu `C# Enum.GetNames()`.

## Použitie adresy `Linq`

 `Linq forEach` môžeme použiť metódu `Enum.GetValues()` a `Enum.GetNames()` na vymenovanie enumov v jazyku C#.

V `.Net 5` a vyššie použite nižšie uvedený úryvok kódu.

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

V starších verziách

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

## Zhrnutie

V tomto návode sme sa naučili prechádzať enum v jazyku C# pomocou metód `Enum.GetValues()` a `Enum.GetNames()`.










