+++
title   ="2 manieren om int te converteren/castten naar enum in C#"
summary ="Er zijn 2 manieren om int te casten naar enum in C# 1. Met behulp van C# explicit type casting. 2. 2. Met behulp van Enum.ToObject() methode."

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


Er zijn 2 manieren om `int` te converteren of te casten naar `enum` in C#

1. Met behulp van C# explicit type casting.
2. Met behulp van `Enum.ToObject()` methode

{{%toc%}}

## Oplossing 1: C# explicit type casting gebruiken

De eenvoudige manier om `int` te converteren naar `enum` in C# is door expliciete type casting te gebruiken.

Laten we een voorbeeld bekijken om het verder te begrijpen.

We hebben een `enum` type genaamd `LogLevel`, dat verschillende niveaus van logging vertegenwoordigt.

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

Expliciete casting vindt plaats door het `enum` type tussen haakjes voor de `int` waarde te plaatsen.

Maar er is een probleem met bovenstaande **C# `int` naar `enum` conversie**.

Wat als de `int` waarde niet bestaat in de C# `Enum` variabele?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Het zal geen uitzondering gooien.

Het is dus beter om te controleren of de `int` waarde bestaat in `C# Enum` alvorens deze te casten naar een geheel getal.

## Controleren of een geheel getal bestaat of niet in `C# enum` variabele

Om alle gehele getallen in `C# Enum` te krijgen, kunnen we de methode `Enum.GetValues` gebruiken.

Zet ze om in lijst `C#`, zodat we methode `list.Contains()` kunnen gebruiken om te controleren of het gegeven gehele getal bestaat in `enum` variabele.

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
We kunnen de methode `Enum.IsDefined()` gebruiken om te controleren of het geconverteerde gehele getal bestaat in het gegeven `enum` type.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Oplossing 2: Gebruik de methode `Enum.ToObject()` 

We kunnen de methode `C# Enum.ToObject()` gebruiken om de waarde `int` te converteren naar `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





