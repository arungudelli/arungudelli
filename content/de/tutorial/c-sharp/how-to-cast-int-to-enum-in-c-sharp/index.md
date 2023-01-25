+++
title   ="2 ways to convert/cast int to enum in C#"
summary ="There are 2 ways To cast int to enum in C# 1. Mit C# expliziten Typ Casting. 2. Mit der Methode Enum.ToObject()."

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Es gibt 2 Möglichkeiten zum Konvertieren oder Casting `int` zu `enum` in C#

1. Mit C# explizites Typ-Casting.
2. Verwendung der Methode `Enum.ToObject()` 

{{%toc%}}

## Lösung 1: Explizites Typ-Casting in C# verwenden

Der einfache Weg, um `int` in `enum` in C# zu konvertieren, ist die Verwendung von explizitem Type Casting.

Lassen Sie uns ein Beispiel durchgehen, um es besser zu verstehen.

Wir haben einen `enum` typ namens `LogLevel`, der verschiedene Ebenen der Protokollierung darstellt.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Das explizite Casting erfolgt durch Einfügen des `enum` typ in Klammern vor den Wert `int` gesetzt wird.

Aber es gibt ein Problem mit der obigen **C# `int` zu `enum` umwandlung**.

Was ist, wenn der Wert `int` nicht in der C#-Variable `Enum` vorhanden ist?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Es wird keine Ausnahme ausgelöst.

Es ist also besser zu prüfen, ob der Wert `int` in `C# Enum` existiert, bevor er in eine Ganzzahl umgewandelt wird.

## Prüfen Sie, ob ein Integer-Wert existiert oder nicht in `C# enum` variable

Um alle Integer-Werte in `C# Enum` zu erhalten, können wir die Methode `Enum.GetValues` verwenden.

Konvertieren Sie sie in die Liste `C#`, so dass wir mit der Methode `list.Contains()` prüfen können, ob die angegebene ganze Zahl in der `enum` variable existiert.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Wir können die Methode `Enum.IsDefined()` verwenden, um zu prüfen, ob der konvertierte Integer-Wert im angegebenen `enum` typ.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Lösung 2: Verwenden Sie die Methode `Enum.ToObject()` 

Wir können die Methode `C# Enum.ToObject()` verwenden, um den Wert `int` in `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





