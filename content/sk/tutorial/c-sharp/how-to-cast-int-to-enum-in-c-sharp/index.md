+++
title   ="2 spôsoby konverzie/prevodu int na enum v jazyku C#"
summary ="Existujú 2 spôsoby prevodu int na enum v jazyku C# 1. Použitie explicitného typového castingu v jazyku C#. 2. 2. Použitie metódy Enum.ToObject()."

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


Existujú 2 spôsoby konverzie alebo obsadenia `int` na `enum` v jazyku C#

1. Pomocou explicitného typového zápisu v jazyku C#.
2. Použitie metódy `Enum.ToObject()` 

{{%toc%}}

## Riešenie 1: Použitie explicitného typového kastingu jazyka C#

Jednoduchý spôsob konverzie `int` na `enum` v jazyku C# je použitie explicitného typového kastingu.

Prejdime si príklad, aby sme ho lepšie pochopili.

Máme `enum` typ s názvom `LogLevel`, ktorý predstavuje rôzne úrovne protokolovania.

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

Explicitné obsadzovanie sa vykonáva umiestnením príkazu `enum` typu v zátvorkách pred hodnotou `int`.

Existuje však problém s vyššie uvedeným **C# `int` na `enum` konverzii**.

Čo ak hodnota `int` v premennej C# `Enum` neexistuje?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Nevyhodí to žiadnu výnimku.

Preto je lepšie skontrolovať, či hodnota `int` existuje v `C# Enum`, skôr než ju prevediete na celé číslo.

## Skontrolujte, či celé číslo existuje alebo nie v `C# enum` premennej

Na získanie všetkých celočíselných hodnôt v premennej `C# Enum` môžeme použiť metódu `Enum.GetValues`.

Prevedieme ich na zoznam `C#`, aby sme mohli pomocou metódy `list.Contains()` skontrolovať, či dané celé číslo existuje v `enum` premennej.

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
Metódu `Enum.IsDefined()` môžeme použiť na kontrolu, či konvertovaná celočíselná hodnota existuje v danej `enum` type.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Riešenie 2: Použite metódu `Enum.ToObject()` 

Môžeme použiť metódu `C# Enum.ToObject()`, previesť hodnotu `int` na `enum` v jazyku C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





