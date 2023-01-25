+++
title   ="2 ways to convert/cast int to enum in C#"
summary ="There are 2 ways To cast int to enum in C# 1. Używając C# explicit type casting. 2. Używając metody Enum.ToObject()."

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


Istnieją 2 sposoby Aby przekonwertować lub rzucić `int` do `enum` w C#

1. Używając w C# jawnego rzutowania typów.
2. Używanie metody `Enum.ToObject()` 

{{%toc%}}

## Rozwiązanie 1: Użycie rzutowania typu jawnego w C#

Prostym sposobem na konwersję `int` do `enum` w C# jest użycie jawnego rzutowania typów.

Przejdźmy przez przykład, aby zrozumieć to dalej.

Mamy `enum` typ o nazwie `LogLevel`, który reprezentuje różne poziomy logowania.

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

Wyraźne rzutowanie odbywa się poprzez umieszczenie `enum` w nawiasach przed wartością `int`.

Ale jest problem z powyższą **C# `int` to `enum` konwersja**.

Co zrobić, jeżeli wartość `int` nie istnieje w zmiennej C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Nie będzie rzucał żadnego wyjątku.

Więc lepiej sprawdzić, czy wartość `int` istnieje w `C# Enum` przed rzuceniem go na liczbę całkowitą.

## Sprawdź czy liczba całkowita istnieje czy nie w `C# enum` zmiennej

Aby uzyskać wszystkie wartości całkowite w `C# Enum` możemy użyć metody `Enum.GetValues`.

Przekształć je na listę `C#`, abyśmy mogli użyć metody `list.Contains()` do sprawdzenia, czy dana liczba całkowita istnieje w `enum` zmiennej.

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
Możemy użyć metody `Enum.IsDefined()`, aby sprawdzić, czy przekonwertowana wartość całkowita istnieje w danym `enum` typu.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Rozwiązanie 2: Użyj metody `Enum.ToObject()` 

Możemy użyć metody `C# Enum.ToObject()`, aby przekonwertować wartość `int` na `enum` w C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





