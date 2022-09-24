
+++
title="Wie bekommt man enum Name von Wert in C#"
summary="Es gibt zwei Möglichkeiten, enum Name von Wert in C# 1. Verwenden Sie C# `Enum.GetName()` und übergeben Sie enum value als Parameter, um den Namen zu erhalten. 2. Konvertieren Sie enum Wert in die enumeration Mitglied mit Casting und verwenden Sie dann `ToString()` Methode."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Einer der beliebtesten Anwendungsfälle von enum ist es, den enum Namen aus seinem Wert zu erhalten.

Betrachten wir ein Beispiel aus der realen Welt, so werden wir im Allgemeinen enum Werte in der Datenbank speichern, d.h. wir werden nur Integer-Werte speichern 

Nachdem wir den Wert enum aus der Datenbank gelesen haben, müssen wir ihn wieder in seinen Namen enum umwandeln.

Es gibt **zwei Möglichkeiten, den enum Namen aus dem Wert in C#** zu erhalten 

{{%toc%}}

## Lösung 1: Mit `Enum.GetName()`

C# `Enum.GetName()` Funktion nimmt zwei Parameter enum Typ und Wert und gibt den enum Namen zurück.

Nehmen Sie ein Beispiel für `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Jetzt werden wir den Wert enum an `Enum.GetName()` übergeben, um den Namen enum zu erhalten 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Wenn Sie die C#-Version `.Net 6` verwenden, können Sie nur den Wert enum (in enum umgewandelt) an die Methode `Enum.GetName()` übergeben.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Lösung 2: Typ-Casting verwenden

Eine andere Möglichkeit besteht darin, den Wert enum mittels Casting in das Element enumzu konvertieren und dann die Methode `ToString()` zu verwenden.

Dies ist ein einfacher Weg, der keine `C# Enum` eingebauten Funktionen verwendet.

Konvertieren Sie zunächst den Wert enum in das Element enumeration und verwenden Sie dann die Methode `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Zusammenfassung

In diesem Tutorial haben wir gelernt, verschiedene Möglichkeiten, um enum Name Wert in c # 

1. Durch die Übergabe von enum Typ- und Wertparameter an die Methode `Enum.GetName()` 
2. Und durch Typ-Casting auf den entsprechenden enum Typ 
