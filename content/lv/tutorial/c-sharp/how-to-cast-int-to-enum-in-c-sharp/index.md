+++
title   ="2 veidi, kā konvertēt/pārvērst int uz enum programmā C#"
summary ="Ir 2 veidi, kā konvertēt int uz enum programmā C# 1. Izmantojot C# tiešo tipa atveidi. 2. 2. Izmantojot metodi Enum.ToObject()."

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


Ir 2 veidi, kā konvertēt vai atveidot `int` uz `enum` programmā C#

1. Izmantojot C# tiešo tipa atveidi.
2. Izmantojot `Enum.ToObject()` metodi

{{%toc%}}

## Risinājums Nr. 1: Izmantojot C# tiešo tipa atveidi

Vienkāršs veids, kā konvertēt `int` uz `enum` c# valodā ir izmantot tiešo tipa atveidi.

Lai to labāk izprastu, aplūkosim piemēru.

Mums ir `enum` tips ar nosaukumu `LogLevel`, kas apzīmē dažādus žurnālu reģistrēšanas līmeņus.

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

Skaidrā kastēšana tiek veikta, ievietojot `enum` tips iekavās pirms `int` vērtības.

Bet ir problēma ar iepriekš minēto **C# `int` uz `enum` konvertēšanu**.

Ko darīt, ja C# `Enum` mainīgajā nav `int` vērtības?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Izņēmums netiks mests.

Tāpēc labāk ir pārbaudīt, vai `int` vērtība eksistē `C# Enum` pirms tās pārrēķināšanas uz veselu skaitli.

## Pārbaudiet, vai vesels skaitlis pastāv vai ne `C# enum` mainīgajā

Lai iegūtu visas veselu skaitļu vērtības mainīgajā `C# Enum`, mēs varam izmantot `Enum.GetValues` metodi.

Pārvērst tās `C#` sarakstā, lai mēs varētu izmantot `list.Contains()` metodi, lai pārbaudītu, vai dotais veslais skaitlis pastāv `enum` mainīgajā.

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
Mēs varam izmantot `Enum.IsDefined()` metodi, lai pārbaudītu, vai konvertētā veselā skaitļa vērtība eksistē dotajā sarakstā `enum` tipā.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 2. risinājums: Izmantojiet `Enum.ToObject()` metodi

Mēs varam izmantot `C# Enum.ToObject()` metodi, konvertēt `int` vērtību uz `enum` c# valodā.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





