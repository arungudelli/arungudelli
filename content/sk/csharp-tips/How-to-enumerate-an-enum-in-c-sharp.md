---
title: "Ako enumerate C# enum"
description: " Rôzne spôsoby enumerate C# enum s príkladmi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumy sú v jazyku `C#` široko používané. 

A existujú 4 spôsoby, ako enumerate enum v `C#`. 

1. Používanie `C# Enum.GetValues()` v .Net 5 a vyšších verziách.
2. Použitie `C# Enum.GetValues()` v starších verziách .Net.
3. Použitie `C# Enum.GetNames()` na enumerate enum names as strings.
4. Používanie stránky `Linq`

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

Stránka `enum` predstavuje rôzne typy úrovní protokolovania.

Teraz si ukážeme rôzne spôsoby, ako enumerovať `C# enum`.

## Používanie `C# Enum.GetValues()` Generická metóda v .net 5 a vyšších verziách

Ak používate najnovšiu verziu `.Net`, t. j. `.Net 5` a vyššiu, môžete použiť generickú verziu pre metódu `Enum.GetValues` na enumerate `C# enum`.

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

Nová všeobecná verzia `Enum.GetValues` vracia pole hodnôt enum. 

A ďalej môžeme použiť príkazy `for` alebo `foreach` na vypísanie zoznamu `C# enum` mien. 

Keďže pole obsahuje `enum` typ, musíme ho previesť na reťazec pomocou metódy `ToString()`.

## Použitie adresy `C# Enum.GetValues()` v starších verziách siete .net.

V starších verziách `.Net` nie je k dispozícii generická metóda pre metódu `Enum.GetValues()`. 

Metóde `Enum.GetValues()` musíte ako parameter odovzdať `typeof()` enum . 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
A tá vracia hodnoty enum typu `System.Array` a ďalej môžeme použiť príkaz `foreach` na prechádzanie cyklu cez `C# enum` mien.

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

## Použitie `C# Enum.GetNames()` na enumerate enum mien ako reťazcov 

`C# Enum.GetValues()` metóda vracia pole typov enum. 

Preto sme pred vypísaním v konzole konvertovali enum názvy na reťazec.

Pomocou metódy `C# Enum.GetNames()` môžeme enumerovať názvy enum ako reťazce, takže ich nie je potrebné konvertovať na reťazce.

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

V starších verziách musíme odovzdať parameter `typeof()` enum .

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

Ak teda chceme en enumerovať názvy ako reťazce, môžeme použiť metódu `C# Enum.GetNames()`.

## Použitie `Linq`

 `Linq forEach` môžeme použiť metódu enumerate C# enum, pomocou metód `Enum.GetValues()` a `Enum.GetNames()`.

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

V tomto tutoriáli sme sa naučili enumerovať enum v jazyku C# pomocou metód `Enum.GetValues()` a `Enum.GetNames()`.










