---
title: "Jak zapętlić/wyliczyć C# enum"
description: "Różne sposoby zapętlenia lub wyliczenia C# enum z przykładami"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enum są szeroko stosowane w języku `C#`. 

I istnieją 4 sposoby zapętlenia lub wyliczenia enum w `C#`. 

1. Używanie `C# Enum.GetValues()` w .Net 5 i wyżej.
2. Używanie `C# Enum.GetValues()` w starszych wersjach .Net.
3. Używanie `C# Enum.GetNames()` do wyliczania nazw enum jako ciągów.
4. Używanie `Linq`

Przejdźmy przez przykład, aby zrozumieć to dalej. 

Najpierw stworzymy w C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` reprezentujący różne rodzaje poziomów logowania.

Teraz zobaczymy różne sposoby wyliczania `C# enum`.

## Używanie metody `C# Enum.GetValues()` Generic w .Net 5 i wyżej

Jeśli używasz najnowszej wersji `.Net`, tzn. `.Net 5` i wyżej, możesz użyć wersji generycznej dla metody `Enum.GetValues` do zapętlenia `C# enum`.

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

Nowa generyczna wersja `Enum.GetValues` zwraca tablicę wartości enum. 

I dalej możemy użyć `for` lub `foreach` deklaracji, aby wyliczyć `C# enum`. 

Ponieważ tablica zawiera typ `enum` musimy ją przekonwertować na łańcuch przy pomocy metody `ToString()`.

## Używanie `C# Enum.GetValues()` w starszych wersjach .Net.

W starszych wersjach `.Net` nie ma dostępnej metody generycznej dla metody `Enum.GetValues()`. 

Musisz przekazać enum `typeof()` jako parametr do metody `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Zwraca ona wartości enum typu `System.Array` i dalej możemy użyć instrukcji `foreach` do zapętlenia enum w C#.

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

Jeśli chcemy uzyskać wynik `IEnumerable`, możemy dalej rzucić metodę `Enum.GetValues()`.

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

## Użycie `C# Enum.GetNames()` do wyliczania nazw enum jako ciągów znaków 

`C# Enum.GetValues()` metoda zwraca tablicę typów enum. 

Dlatego właśnie przekonwertowaliśmy wartości enum na ciąg przed wydrukowaniem ich w konsoli.

Za pomocą metody `C# Enum.GetNames()` możemy wyliczyć nazwy enum jako łańcuchy, dzięki czemu nie jest wymagana ich konwersja na łańcuchy.

Jeśli używasz `.Net 5` i wyżej, możesz użyć funkcji generycznej `C# Enum.GetNames()`.

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

W starszych wersjach musimy przekazać parametr enum `typeof()`.

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

Jeśli więc chcemy zapętlić nazwy enum jako ciągi znaków możemy użyć metody `C# Enum.GetNames()`.

## Użycie `Linq`

Możemy użyć metody `Linq forEach` do wyliczenia C# enum, z pomocą metod `Enum.GetValues()` i `Enum.GetNames()`.

Na stronie `.Net 5` i wyżej użyj poniższego fragmentu kodu.

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

W starszych wersjach

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

## Podsumowanie

W tym tutorialu nauczyliśmy się zapętlać enum w C# za pomocą metody `Enum.GetValues()` oraz `Enum.GetNames()`.










