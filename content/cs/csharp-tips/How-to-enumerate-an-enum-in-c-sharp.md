---
title: "Jak enumerate C# enum"
description: " Různé způsoby enumerate C# enum s příklady"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumy jsou v jazyce `C#` hojně využívány. 

A existují 4 způsoby, jak enumerate enum v `C#`. 

1. Použití `C# Enum.GetValues()` v prostředí .Net 5 a vyšším.
2. Použití `C# Enum.GetValues()` ve starších verzích .Net.
3. Použití `C# Enum.GetNames()` k enumerate enum names as strings.
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

Na stránkách `enum` představuje různé typy úrovní protokolování.

Nyní se podíváme na různé způsoby, jak enumerate the `C# enum`.

## Použití `C# Enum.GetValues()` Generické metody v .Net 5 a vyšších verzích

Pokud používáte nejnovější verzi `.Net`, tj. `.Net 5` a vyšší, můžete použít generickou verzi pro `Enum.GetValues` metodu enumerate `C# enum`.

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

Nová obecná verze `Enum.GetValues` vrací pole hodnot enum. 

A dále můžeme pomocí příkazů `for` nebo `foreach` vypsat tzv `C# enum` jmen. 

Protože pole obsahuje `enum` typ, musíme jej převést na řetězec pomocí metody `ToString()`.

## Pomocí `C# Enum.GetValues()` ve starších verzích .Net.

Ve starších verzích `.Net` není k dispozici obecná metoda pro metodu `Enum.GetValues()`. 

Metodě `Enum.GetValues()` musíte jako parametr předat `typeof()` enum . 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
A ta vrací hodnoty enum typu `System.Array` a dále můžeme pomocí příkazu `foreach` procházet ve smyčce tyto hodnoty `C# enum` jmen.

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

Pokud chceme výsledek `IEnumerable`, můžeme dále provést obsazení metody `Enum.GetValues()`.

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

## Použití `C# Enum.GetNames()` k enumerate enum names jako řetězce 

`C# Enum.GetValues()` metoda vrací pole typů enum. 

Proto jsme enum jména před vypsáním do konzoly převedli na řetězec.

Pomocí metody `C# Enum.GetNames()` můžeme enumerovat enum jména jako řetězce, takže je není nutné převádět na řetězce.

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

Ve starších verzích musíme předat parametr `typeof()` enum .

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

Pokud tedy chceme enumerovat jména jako řetězce, můžeme použít metodu `C# Enum.GetNames()`.

## Použití `Linq`

 `Linq forEach` můžeme použít metodu enumerate C# enum, pomocí metod `Enum.GetValues()` a `Enum.GetNames()`.

V `.Net 5` a výše použijte níže uvedený úryvek kódu.

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

V tomto tutoriálu jsme se naučili enumerovat enum v jazyce C# pomocí metod `Enum.GetValues()` a `Enum.GetNames()`.










