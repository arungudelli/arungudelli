---
title: "Schleifen/Aufzählung von C# enum"
description: "Verschiedene Möglichkeiten zur Schleifenbildung oder Aufzählung von C# enum mit Beispielen"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums sind in der Sprache `C#` weit verbreitet. 

Und es gibt 4 Möglichkeiten, Schleife oder enumerate enum in `C#`. 

1. Verwendung von `C# Enum.GetValues()` in .Net 5 &amp; höher.
2. Verwendung von `C# Enum.GetValues()` in älteren .Net-Versionen.
3. Verwendung von `C# Enum.GetNames()` zum Aufzählen von Aufzählungsnamen als Strings.
4. Verwendung von `Linq`

Lassen Sie uns ein Beispiel durchgehen, um es besser zu verstehen. 

Zuerst werden wir eine C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

Die `enum` stellt verschiedene Arten von Protokollierungsstufen dar.

Jetzt werden wir verschiedene Möglichkeiten sehen, die `C# enum` aufzuzählen.

## Verwendung der Methode `C# Enum.GetValues()` Generic in .Net 5 und höher

Wenn Sie die neueste Version von `.Net` verwenden, d.h. `.Net 5` und höher, können Sie die generische Version für die Methode `Enum.GetValues` verwenden, um eine Schleife durch die `C# enum` zu ziehen.

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

Die neue generische Version von `Enum.GetValues` gibt das Array der Enum-Werte zurück. 

Außerdem können wir die Anweisungen `for` oder `foreach` verwenden, um die `C# enum` aufzuzählen. 

Da das Array den Typ `enum` enthält, müssen wir es mit der Methode `ToString()` in einen String umwandeln.

## Verwendung von `C# Enum.GetValues()` in älteren .Net-Versionen.

In den älteren Versionen von `.Net` gibt es keine generische Methode für die Methode `Enum.GetValues()`. 

Sie müssen `typeof()` enum als Parameter an die Methode `Enum.GetValues()` übergeben. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Sie gibt Enum-Werte des Typs `System.Array` zurück und wir können die `foreach` -Anweisung verwenden, um eine Schleife durch das C#-Enum zu ziehen.

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

Wenn Sie `IEnumerable` Ergebnis wollen, können wir weiter casten die `Enum.GetValues()` Methode.

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

## Verwendung von `C# Enum.GetNames()` zur Aufzählung von Aufzählungsnamen als Strings 

`C# Enum.GetValues()` methode gibt Array von Aufzählungstypen zurück. 

Deshalb haben wir die Enum-Werte in Strings umgewandelt, bevor wir sie auf der Konsole ausgeben.

Mit der Methode `C# Enum.GetNames()` können wir die Enum-Namen als Strings aufzählen, so dass es nicht erforderlich ist, sie in Strings umzuwandeln.

Wenn Sie `.Net 5` und höher verwenden, können Sie die generische Funktion `C# Enum.GetNames()` verwenden.

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

In den älteren Versionen müssen wir den Parameter `typeof()` enum übergeben.

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

Wenn Sie also Enum-Namen als Strings in einer Schleife verwenden möchten, können wir die Methode `C# Enum.GetNames()` verwenden.

## Verwendung von `Linq`

Wir können die Methode `Linq forEach` verwenden, um C# enum mit Hilfe der Methoden `Enum.GetValues()` und `Enum.GetNames()` aufzuzählen.

In `.Net 5` und höher verwenden Sie den folgenden Codeausschnitt.

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

In den älteren Versionen

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

## Zusammenfassung

In diesem Tutorial haben wir gelernt, in C# mit der Methode `Enum.GetValues()` und `Enum.GetNames()` eine Schleife durch enum zu ziehen.










