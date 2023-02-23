---
title: "Kako enumerate C# enum"
description: " Različni načini enumerate C# enum s primeri"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumi se pogosto uporabljajo v jeziku `C#`. 

In obstajajo 4 načini za enumerate enum v `C#`. 

1. Uporaba `C# Enum.GetValues()` v okolju .Net 5 in novejšem.
2. Uporaba `C# Enum.GetValues()` v starejših različicah .Net.
3. Uporaba `C# Enum.GetNames()` za enumerate enum imen kot nizov.
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

Spletna stran `enum` predstavljajo različne vrste ravni beleženja.

Zdaj si bomo ogledali različne načine za enum`C# enum`.

## Uporaba `C# Enum.GetValues()` Generične metode v .Net 5 in novejših različicah

Če uporabljate najnovejšo različico `.Net`, tj. `.Net 5` in novejšo, lahko uporabite generično različico za metodo `Enum.GetValues`, da enumerate `C# enum`.

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

Nova splošna različica `Enum.GetValues` vrne polje vrednosti enum. 

Nadalje lahko uporabimo izjave `for` ali `foreach` za seznam `C# enum` imen. 

Ker polje vsebuje `enum` vrsto, jo moramo pretvoriti v niz z uporabo metode `ToString()`.

## Uporaba metode `C# Enum.GetValues()` v starejših različicah .Net.

V starejših različicah `.Net` za metodo `Enum.GetValues()` ni na voljo generične metode. 

Metodi `Enum.GetValues()` morate kot parameter posredovati `typeof()` enum . 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
In ta vrne enum vrednosti tipa `System.Array`, v nadaljevanju pa lahko uporabimo izjavo `foreach` za kroženje po zanki skozi `C# enum` imena.

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

Če želimo rezultat `IEnumerable`, lahko dodatno uporabimo metodo `Enum.GetValues()`.

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

## Uporaba `C# Enum.GetNames()` za enumeratiranje enum imen kot nizov 

`C# Enum.GetValues()` metoda vrne polje enum tipov. 

Zato smo imena enum pretvorili v niz, preden smo jih natisnili v konzolo.

Z uporabo metode `C# Enum.GetNames()` lahko enumeraturiramo imena enum kot nize, tako da jih ni treba pretvoriti v nize.

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

V starejših različicah moramo posredovati parameter `typeof()` enum .

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

Če torej želimo en enumerate imena kot nize, lahko uporabimo metodo `C# Enum.GetNames()`.

## Uporaba `Linq`

 `Linq forEach` lahko uporabimo metodo enumerate C# enum, s pomočjo metod `Enum.GetValues()` in `Enum.GetNames()`.

V spletni strani `.Net 5` in višjih uporabite spodnji del kode.

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

V tem učbeniku smo se naučili enumerate enum v C# z uporabo metod `Enum.GetValues()` in `Enum.GetNames()`.










