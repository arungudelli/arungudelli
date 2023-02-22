---
title: "Kā veidot cilpas/skaitīt C# enum"
description: "Dažādi veidi, kā veidot cilpas vai uzskaitīt C# enum ar piemēriem"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumus plaši izmanto `C#` valodā. 

Un ir 4 veidi, kā `C#`. 

1. `C# Enum.GetValues()` izmantošana .Net 5 un jaunākās versijās.
2. Izmantojot `C# Enum.GetValues()` vecākās .Net versijās.
3. Izmantojot `C# Enum.GetNames()`, lai uzskaitītu enum nosaukumus kā virknes.
4. Izmantojot `Linq`

Izskatīsim piemēru, lai to labāk izprastu. 

Vispirms izveidosim C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` ir attēloti dažādi mežistrādes līmeņu veidi.

Tagad mēs apskatīsim dažādus veidus, kā uzskaitīt `C# enum`.

## `C# Enum.GetValues()` vispārīgās metodes izmantošana .Net 5 un jaunākās versijās

Ja izmantojat jaunāko `.Net` versiju, t. i., `.Net 5` un jaunāku versiju, varat izmantot vispārīgo versiju `Enum.GetValues` metodei, lai veiktu cilpu caur `C# enum`.

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

Jaunā vispārīgā `Enum.GetValues` versija atgriež enuma vērtību masīvu. 

Un tālāk mēs varam izmantot `for` vai `foreach` paziņojumus, lai uzskaitītu `C# enum`. 

Tā kā masīvs satur `enum` tipu, mums tas jāpārveido virknē, izmantojot `ToString()` metodi.

## Izmantojot `C# Enum.GetValues()` vecākās .Net versijās.

Vecākajās `.Net` versijās `Enum.GetValues()` metodei nav pieejama vispārīga metode. 

Jums ir jānodod `typeof()` enum kā parametrs `Enum.GetValues()` metodei. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Un tā atgriež `System.Array` tipa enuma vērtības, un tālāk mēs varam izmantot `foreach` izteikumu, lai veiktu ciklu caur C# enumu.

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

Ja vēlaties `IEnumerable` rezultātu, mēs varam tālāk izmantot `Enum.GetValues()` metodi.

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

## Izmantojot `C# Enum.GetNames()`, lai uzskaitītu enumu nosaukumus kā virknes 

`C# Enum.GetValues()` metode atgriež enumu tipu masīvu. 

Tāpēc mēs pārvēršam enumu vērtības virknē, pirms tās izdrukāt konsoles ekrānā.

Izmantojot `C# Enum.GetNames()` metodi, mēs varam uzskaitīt enumu nosaukumus kā virknes, lai tos nevajadzētu konvertēt virknēs.

Ja izmantojat `.Net 5` un augstāk, varat izmantot vispārīgo `C# Enum.GetNames()` funkciju.

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

Vecākajās versijās mums ir jānogādā `typeof()` enum parametrs.

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

Tātad, ja vēlaties, lai enumu nosaukumi būtu kā virknes, varam izmantot `C# Enum.GetNames()` metodi.

## Izmantojot `Linq`

Mēs varam izmantot `Linq forEach` metodi, lai uzskaitītu C# enumus, izmantojot `Enum.GetValues()` un `Enum.GetNames()` metodes.

Izmantojot `.Net 5` un augstāk, izmantojiet zemāk redzamo koda fragmentu.

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

Vecākās versijās

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

## Kopsavilkums

Šajā pamācībā mēs uzzinājām, kā C# programmā izveidot cilpu caur enum, izmantojot `Enum.GetValues()` un `Enum.GetNames()` metodi.










