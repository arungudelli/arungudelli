
+++
title="Kuidas saada enum nimi väärtusest C#"
summary="On kaks võimalust saada enum nimi väärtusest C# 1. Kasutage C# `Enum.GetName()` ja andke parameetrina üle enum väärtus, et saada nimi. 2. Konverteerida enum väärtus enumerationi liikmeks, kasutades casting'i ja seejärel kasutada `ToString()` meetodit."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Üks populaarsemaid enum kasutusviise on enum nime saamine selle väärtusest.

Võtame reaalse näite, üldiselt salvestame andmebaasis enum väärtusi, st salvestame ainult täisarvu väärtusi 

Pärast enum väärtuse lugemist andmebaasist tuleb see teisendada tagasi enum nimeks.

On **kaks võimalust, kuidas saada enum nimi väärtusest C#** 

{{%toc%}}

## Lahendus 1: Kasutades `Enum.GetName()`

C# `Enum.GetName()` funktsioon võtab kaks parameetrit enum tüüp ja väärtus ning tagastab enum nime.

Võtame näiteks `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Nüüd edastame enum väärtuse `Enum.GetName()`, et saada enum nimi 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Kui te kasutate C# `.Net 6` versiooni, siis võite edastada `Enum.GetName()` meetodile ainult enum väärtuse (cast to enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Lahendus 2: tüübi valimine

Teine võimalus on, Convert enum väärtus enumeration liige kasutades casting ja seejärel kasutada `ToString()` meetodit.

See on lihtne viis, mis ei kasuta ühtegi `C# Enum` sisseehitatud funktsiooni.

Kõigepealt teisendatakse enum väärtus enumeration liikme väärtuseks ja seejärel kasutatakse `ToString()` meetodit.

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

## Kokkuvõte

Selles õpetuses õppisime erinevaid viise, kuidas saada enum nime väärtust c# keeles 

1. Andes enum tüübi ja väärtuse parameetrid meetodile `Enum.GetName()` 
2. Ja kasutades tüübi valimist vastavaks enum tüübiks 
