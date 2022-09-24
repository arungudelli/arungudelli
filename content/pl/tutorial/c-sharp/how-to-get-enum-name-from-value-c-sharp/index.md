
+++
title="Jak uzyskać enum nazwę z wartości w C#"
summary="Istnieją dwa sposoby, aby uzyskać enum nazwę z wartości w C# 1. Użyj C# `Enum.GetName()` i przekaż wartość enum jako parametr, aby uzyskać nazwę. 2. Przekształć wartość enum do członka eracji enumza pomocą rzutowania, a następnie użyj metody `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Jednym z popularnych przypadków użycia enum jest uzyskanie enum nazwy z jej wartości.

Rozważmy przykład z prawdziwego świata, generalnie będziemy przechowywać wartości enum w bazie danych, tj. Będziemy przechowywać tylko wartości całkowite 

Po odczytaniu wartości enum z bazy danych musimy ją przekonwertować z powrotem na jej nazwę enum.

Istnieją **dwa sposoby uzyskania nazwy enum z wartości w C#** 

{{%toc%}}

## Rozwiązanie 1: Użycie `Enum.GetName()`

C# funkcja `Enum.GetName()` przyjmuje dwa parametry enum typ i wartość i zwraca enum nazwę.

Weźmy przykład `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Teraz przekażemy wartość enum do `Enum.GetName()`, aby uzyskać nazwę enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Jeśli używasz wersji C# `.Net 6`, możesz przekazać tylko wartość enum (cast to enum) do metody `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Rozwiązanie 2: Użycie rzutowania typu

Innym sposobem jest, Konwersja wartości enum do członka eracji enumza pomocą rzutowania, a następnie użycie metody `ToString()`.

Jest to prosty sposób, który nie używa żadnych `C# Enum` wbudowanych funkcji.

Najpierw przekonwertuj wartość enum na członka enumeration, a następnie użyj metody `ToString()`.

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

## Podsumowanie

W tym tutorialu poznaliśmy różne sposoby na uzyskanie wartości enum name w c# 

1. Poprzez przekazanie parametrów typu enum i wartości do metody `Enum.GetName()` 
2. I używając rzutowania typu na odpowiadający mu typ enum 
