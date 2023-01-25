+++
title   ="2 ways to convert/cast int to enum in C#"
summary ="Există 2 moduri de a transforma int în enum în C# 1. Folosind C# explicit type casting. 2. 2. Folosind metoda Enum.ToObject()."

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


Există două moduri de a converti sau de a transforma `int` în `enum` în C#

1. Folosind C# explicit type casting.
2. Utilizarea metodei `Enum.ToObject()` 

{{%toc%}}

## Soluția 1: Utilizarea distribuției explicite a tipurilor în C#

Modul simplu de a converti `int` în `enum` în C# este de a utiliza turnarea explicită a tipului.

Să parcurgem un exemplu pentru a înțelege mai bine acest lucru.

Avem un tip `enum` tip numit `LogLevel`, care reprezintă diferite niveluri de jurnalizare.

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

Castingul explicit se face prin plasarea indicativului `enum` în paranteze în fața valorii `int`.

Dar există o problemă cu **C# `int` de mai sus, care se referă la `enum` conversie**.

Ce se întâmplă dacă valoarea `int` nu există în variabila C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Nu se va arunca nicio excepție.

Așadar, este mai bine să verificați dacă valoarea `int` există în `C# Enum` înainte de a o transforma în număr întreg.

## Verificați dacă un întreg există sau nu în `C# enum` variabila

Pentru a obține toate valorile întregi din `C# Enum`, putem utiliza metoda `Enum.GetValues`.

Să le convertim în lista `C#`, astfel încât să putem folosi metoda `list.Contains()` pentru a verifica dacă numărul întreg dat există în `enum` variabilă.

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
Putem utiliza metoda `Enum.IsDefined()` pentru a verifica dacă valoarea întreagă convertită există în variabila dată `enum` tip.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Soluția 2: Utilizați metoda `Enum.ToObject()` 

Putem utiliza metoda `C# Enum.ToObject()`, pentru a converti valoarea `int` în `enum` în C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





