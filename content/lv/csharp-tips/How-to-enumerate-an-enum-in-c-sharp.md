---
title: "Kā enumerate C# enum"
description: " Dažādi veidi, kā enumerate C# enum ar piemēriem"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumus plaši izmanto `C#` valodā. 

Un ir 4 veidi, kā enumerate enum `C#` . 

1. `C# Enum.GetValues()` izmantošana .Net 5 un jaunākās versijās.
2. Izmantojot `C# Enum.GetValues()` vecākās .Net versijās.
3. Izmantojot `C# Enum.GetNames()`, lai enumerate enum vārdus kā virknes.
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

Portāls `enum` apzīmē dažādus žurnālu veidošanas līmeņus.

Tagad mēs aplūkosim dažādus veidus, kā enumerate `C# enum`.

## Izmantojot `C# Enum.GetValues()` Generic metodi .Net 5 un jaunākās versijās

Ja izmantojat jaunāko `.Net` versiju, t. i., `.Net 5` un jaunāku versiju, varat izmantot vispārīgo versiju `Enum.GetValues` metodei, lai enumeratētu `C# enum`.

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

Jaunā vispārīgā `Enum.GetValues` versija atgriež enum vērtību masīvu. 

Un tālāk mēs varam izmantot `for` vai `foreach` paziņojumus, lai uzskaitītu `C# enum` vārdus. 

Tā kā masīvs satur `enum` tips, mums tas jāpārvērš virknē, izmantojot `ToString()` metodi.

## Izmantojot `C# Enum.GetValues()` vecākās .Net versijās.

Vecākajās `.Net` versijās `Enum.GetValues()` metodei nav pieejama vispārīga metode. 

Jums ir jānodod `typeof()` enum kā parametrs `Enum.GetValues()` metodei. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Un tā atgriež enum tipa `System.Array` vērtības, un tālāk mēs varam izmantot `foreach` izteikumu, lai veiktu cilpu caur `C# enum` vārdus.

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

## Izmantojot `C# Enum.GetNames()`, lai enumeratētu enum vārdus kā virknes 

`C# Enum.GetValues()` metode atgriež enum tipu masīvu. 

Tāpēc mēs konvertējām enum vārdus virknē, pirms tos izdrukāt konsoles ekrānā.

Izmantojot `C# Enum.GetNames()` metodi, mēs varam enumerēt enum vārdus kā virknes, lai tos nevajadzētu konvertēt virknēs.

Ja jūs izmantojat `.Net 5` un augstāk, jūs varat izmantot vispārīgo `C# Enum.GetNames()` funkciju.

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

Vecākajās versijās mums ir jāievada `typeof()` enum parametrs.

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

Tātad, ja jūs vēlaties enumerate vārdus kā virknes, mēs varam izmantot `C# Enum.GetNames()` metodi.

## Izmantojot `Linq`

Mēs varam izmantot `Linq forEach` metodi, lai enumeratētu C# enum, izmantojot `Enum.GetValues()` un `Enum.GetNames()` metodes.

 `.Net 5` un augstāk izmanto zemāk redzamo koda fragmentu.

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

Šajā pamācībā mēs iemācījāmies enumerate enum C# valodā, izmantojot `Enum.GetValues()` un `Enum.GetNames()` metodi.










