+++
title   ="2 sätt att konvertera/casta int till enum i C#"
summary ="Det finns 2 sätt att casta int till enum i C# 1. Genom att använda explicit typcasting i C#. 2. Genom att använda metoden Enum.ToObject()."

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


Det finns två sätt att konvertera eller kasta `int` till `enum` i C#

1. Genom att använda explicit typcasting i C#.
2. Användning av `Enum.ToObject()` -metoden

{{%toc%}}

## Lösning 1: Användning av explicit type casting i C#

Det enkla sättet att konvertera `int` till `enum` i C# är att använda explicit type casting.

Låt oss gå igenom ett exempel för att förstå det närmare.

Vi har en `enum` typ som heter `LogLevel`, som representerar olika nivåer av loggning.

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

Explicit casting görs genom att placera `enum` typ inom parentes framför värdet `int`.

Men det finns ett problem med ovanstående **C# `int` till `enum` konvertering**.

Vad händer om värdet `int` inte finns i variabeln C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Det kommer inte att skapa något undantag.

Det är alltså bättre att kontrollera om värdet `int` finns i `C# Enum` innan det kastas till ett heltal.

## Kontrollera om ett heltal finns eller inte i `C# enum` variabeln

För att få fram alla heltalsvärden i `C# Enum` kan vi använda metoden `Enum.GetValues`.

Konvertera dem till listan `C#` så att vi kan använda metoden `list.Contains()` för att kontrollera om det givna heltalet finns i variabeln `enum` variabel.

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
Vi kan använda metoden `Enum.IsDefined()` för att kontrollera om det konverterade heltalsvärdet finns i den givna variabeln `enum` typ.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Lösning 2: Använd metoden `Enum.ToObject()` 

Vi kan använda metoden `C# Enum.ToObject()` och omvandla värdet `int` till `enum` i C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





