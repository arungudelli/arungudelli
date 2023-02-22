---
title: "Jak zacyklit/vyčíslit výčet v jazyce C#"
description: "Různé způsoby zacyklení nebo vyčíslení výčtu v jazyce C# s příklady"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumy jsou v jazyce `C#` hojně využívány. 

A existují 4 způsoby, jak zacyklit nebo vyjmenovat enum v `C#`. 

1. Použití `C# Enum.GetValues()` v .Net 5 a vyšších verzích.
2. Použití `C# Enum.GetValues()` ve starších verzích .Net.
3. Použití adresy `C# Enum.GetNames()` k výčtu názvů výčtů jako řetězců.
4. Použití adresy `Linq`

Projděme si příklad, abychom jej lépe pochopili. 

Nejprve vytvoříme v jazyce C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` představuje různé typy úrovní protokolování.

Nyní si ukážeme různé způsoby výčtu `C# enum`.

## Použití obecné metody `C# Enum.GetValues()` v prostředí .Net 5 a vyšším

Pokud používáte nejnovější verzi `.Net`, tj. `.Net 5` a vyšší, můžete použít generickou verzi pro metodu `Enum.GetValues` k procházení smyčky `C# enum`.

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

Nová generická verze metody `Enum.GetValues` vrací pole výčtových hodnot. 

A dále můžeme použít příkazy `for` nebo `foreach` pro výčet `C# enum`. 

Protože pole obsahuje typ `enum`, musíme jej převést na řetězec pomocí metody `ToString()`.

## Použití `C# Enum.GetValues()` ve starších verzích .Net.

Ve starších verzích `.Net` není k dispozici obecná metoda pro metodu `Enum.GetValues()`. 

Metodě `Enum.GetValues()` musíte jako parametr předat enum `typeof()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
A ta vrací enumové hodnoty typu `System.Array` a dále můžeme použít příkaz `foreach` k procházení enumů v jazyce C#.

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

Pokud chceme výsledek `IEnumerable`, můžeme dále provést cast metody `Enum.GetValues()`.

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

## Použití `C# Enum.GetNames()` k výčtu názvů enum jako řetězců 

`C# Enum.GetValues()` metoda vrací pole enumových typů. 

Proto jsme hodnoty enumů před vypsáním do konzoly převedli na řetězec.

Pomocí metody `C# Enum.GetNames()` můžeme názvy enumů vypsat jako řetězce, takže je není nutné převádět na řetězce.

Pokud používáte `.Net 5` a vyšší, můžete použít obecnou funkci `C# Enum.GetNames()`.

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

Ve starších verzích musíme předat parametr `typeof()` enum.

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

Pokud tedy chceme jména enumů zacyklit jako řetězce, můžeme použít metodu `C# Enum.GetNames()`.

## Použití adresy `Linq`

 `Linq forEach` můžeme použít metodu `Enum.GetValues()` a `Enum.GetNames()` pro výčet enumů v jazyce C#.

V `.Net 5` a vyšších použijte níže uvedený úryvek kódu.

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

Ve starších verzích

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

## Souhrn

V tomto tutoriálu jsme se naučili procházet smyčkou enum v jazyce C# pomocí metod `Enum.GetValues()` a `Enum.GetNames()`.










