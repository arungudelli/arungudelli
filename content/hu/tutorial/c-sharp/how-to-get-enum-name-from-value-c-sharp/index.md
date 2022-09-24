
+++
title="Hogyan lehet a enum nevet az értékből C# nyelven"
summary="Kétféleképpen lehet a enum nevet az értékből C# nyelven 1. A C# `Enum.GetName()` használata és a enum érték paraméterként történő átadása a név kinyeréséhez. 2. 2. A enum értéket a enumeration taggá konvertáljuk a casting segítségével, majd használjuk a `ToString()` módszert."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


A enum egyik népszerű felhasználási esete a enum név kinyerése az értékéből.

Vegyünk egy valós példát, általában a enum értékeket tároljuk az adatbázisban, azaz csak egész értékeket tárolunk 

A enum érték adatbázisból való kiolvasása után pedig vissza kell konvertálnunk azt a enum névre.

A enum nevet kétféleképpen kaphatjuk meg az értékből C# nyelven** 

{{%toc%}}

## 1. megoldás: A `Enum.GetName()`

A C# `Enum.GetName()` függvény két paramétert vesz fel: enum típus és érték, és visszaadja a enum nevet.

Vegyünk egy példát a `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Most a enum értéket átadjuk a `Enum.GetName()` értéknek, hogy megkapjuk a enum nevet 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Ha a C# `.Net 6` verziót használja, akkor csak a enum értéket(cast to enum) adhatja át a `Enum.GetName()` metódusnak.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Megoldás 2: Típusöntés használata

Egy másik módja az, hogy, Convert enum értéket a enumeration tag segítségével casting, majd használja `ToString()` módszer.

Ez egy egyszerű módszer, amely nem használ semmilyen `C# Enum` beépített függvényt.

Először konvertáljuk a enum értéket a enumeration taggá, majd használjuk a `ToString()` módszert.

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

## Összefoglaló

Ebben a bemutatóban megtanultuk a enum név értékének különböző módjait c# nyelven 

1. A enum típus és érték paraméterek átadásával a `Enum.GetName()` metódusnak
2. És a megfelelő enum típushoz való típusátadással 
