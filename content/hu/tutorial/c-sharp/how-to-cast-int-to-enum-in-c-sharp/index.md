+++
title   ="2 módja az int konvertálásának/castolásának a enum címre a C#-ban"
summary ="2 módja van az int-nek a enum címre való castolásának a C#-ban 1. A C# explicit type casting használatával. 2. Az Enum.ToObject() módszer használatával."

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


2 módja van a `int` konvertálásának vagy castolásának `enum` c# nyelven

1. A C# explicit típusöntés használata.
2. A `Enum.ToObject()` módszer használata

{{%toc%}}

## Megoldás 1: C# explicit type casting használata

A `int` egyszerű módon konvertálható `enum` c# nyelven az explicit típusváltás használata.

Nézzünk végig egy példát, hogy jobban megértsük.

Van egy `enum``LogLevel` nevű típusunk, amely a naplózás különböző szintjeit reprezentálja.

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

Az explicit casting a `enum` típus zárójelben a `int` érték elé kerül.

De van egy probléma a fenti **C# `int` to `enum` átalakítás**.

Mi van akkor, ha a `int` érték nem létezik a C# `Enum` változóban?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Nem dob semmilyen kivételt.

Tehát jobb, ha ellenőrizzük, hogy a `int` érték létezik-e a `C# Enum` címen, mielőtt egész számra öntjük.

## Ellenőrizze, hogy egy egész szám létezik-e vagy sem a `C# enum` változóban

A `C# Enum` összes egész szám értékének kinyeréséhez használhatjuk a `Enum.GetValues` módszert.

Konvertáljuk őket a `C#` listába, hogy a `list.Contains()` módszerrel ellenőrizni tudjuk, hogy az adott egész szám létezik-e a változóban `enum` változóban.

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
A `Enum.IsDefined()` módszerrel ellenőrizhetjük, hogy a konvertált egész érték létezik-e az adott változóban `enum` típusban.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Megoldás 2: Használja a `Enum.ToObject()` módszert

Használhatjuk a `C# Enum.ToObject()` módszert, a `int` értéket konvertálhatjuk a következőre `enum` c# nyelven.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





