---
title: "Jak enumerate C# enum"
description: " Różne sposoby enumerate C# enum z przykładami"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumy są szeroko stosowane w języku `C#`. 

I są 4 sposoby enumerate enum w `C#`. 

1. Używanie `C# Enum.GetValues()` w .Net 5 i wyżej.
2. Używanie `C# Enum.GetValues()` w starszych wersjach .Net.
3. Używanie `C# Enum.GetNames()` do enumerate enum names as strings.
4. Używanie strony `Linq`

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

Strona `enum` reprezentuje różne typy poziomów logowania.

Teraz zobaczymy różne sposoby na enumerate the `C# enum`.

## Używanie `C# Enum.GetValues()` metody Generic w .Net 5 i wyżej

Jeżeli używasz najnowszej wersji `.Net`, tzn. `.Net 5` i wyżej możesz użyć wersji generycznej dla metody `Enum.GetValues` do enumerate the `C# enum`.

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

I dalej możemy użyć `for` lub `foreach` do wypisania nazw `C# enum` nazwy. 

Ponieważ tablica zawiera `enum` typ, musimy przekonwertować go na ciąg znaków za pomocą metody `ToString()`.

## Użycie `C# Enum.GetValues()` w starszych wersjach .Net.

W starszych wersjach `.Net` nie ma dostępnej metody generycznej dla metody `Enum.GetValues()`. 

Musisz przekazać `typeof()` enum jako parametr do metody `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Metoda ta zwraca wartości typu enum `System.Array` i dalej możemy użyć instrukcji `foreach` do zapętlenia nazw `C# enum` nazwy.

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

## Użycie `C# Enum.GetNames()` do enumeracji enum nazw jako ciągów znaków 

`C# Enum.GetValues()` metoda zwraca tablicę typów enum. 

Dlatego właśnie przekonwertowaliśmy enum nazwy na stringi przed wypisaniem ich w konsoli.

Za pomocą metody `C# Enum.GetNames()` możemy enumerować nazwy enum jako łańcuchy, dzięki czemu nie jest wymagane konwertowanie ich na łańcuchy.

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

W starszych wersjach musimy przekazać parametr `typeof()` enum .

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

Jeśli więc chcemy en enumerate names as strings możemy użyć metody `C# Enum.GetNames()`.

## Użycie `Linq`

Możemy użyć metody `Linq forEach` do enumerate C# enum, z pomocą metod `Enum.GetValues()` i `Enum.GetNames()`.

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

W tym tutorialu nauczyliśmy się enumerować enum w C# za pomocą metody `Enum.GetValues()` oraz `Enum.GetNames()`.










