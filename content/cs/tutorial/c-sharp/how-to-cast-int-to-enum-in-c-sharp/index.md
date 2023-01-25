+++
title   ="2 způsoby převodu/cast int na enum v jazyce C#"
summary ="Existují 2 způsoby, jak cast int na enum v jazyce C# 1. Pomocí explicitního odlitku typu v jazyce C#. 2. 2. Pomocí metody Enum.ToObject()."

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


Existují 2 způsoby převodu nebo obsazení `int` na `enum` v jazyce C#

1. Pomocí explicitního odlitku typu v jazyce C#.
2. Použití metody `Enum.ToObject()` 

{{%toc%}}

## Řešení 1: Použití explicitního přiřazení typu v jazyce C#

Jednoduchý způsob, jak převést `int` na `enum` v jazyce C# je použití explicitního typování.

Projděme si příklad, abychom jej blíže pochopili.

Máme `enum` typ nazvaný `LogLevel`, který představuje různé úrovně protokolování.

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

Explicitní obsazení se provádí umístěním příznaku `enum` typu v závorce před hodnotou `int`.

Existuje však problém s výše uvedeným **C# `int` na `enum` převodu**.

Co když hodnota `int` v proměnné C# `Enum` neexistuje?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Nevyhodí to žádnou výjimku.

Proto je lepší před převedením na celé číslo zkontrolovat, zda hodnota `int` existuje v `C# Enum`.

## Zkontrolujte, zda celé číslo existuje nebo ne v `C# enum` proměnné

Pro získání všech celočíselných hodnot v proměnné `C# Enum` můžeme použít metodu `Enum.GetValues`.

Převedeme je na seznam `C#`, abychom mohli pomocí metody `list.Contains()` zkontrolovat, zda dané celé číslo existuje v daném seznamu `enum` proměnné.

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
Můžeme použít metodu `Enum.IsDefined()`, abychom zkontrolovali, zda převedená celočíselná hodnota existuje v daném `enum` typu.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Řešení 2: Použijte metodu `Enum.ToObject()` 

Můžeme použít metodu `C# Enum.ToObject()` a převést hodnotu `int` na hodnotu `enum` v jazyce C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





