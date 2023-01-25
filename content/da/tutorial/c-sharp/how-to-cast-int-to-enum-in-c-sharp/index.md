+++
title   ="2 måder at konvertere/kaste int til enum i C#"
summary ="Der er 2 måder at kaste int til enum i C# 1. Ved hjælp af C# eksplicit type casting. 2. 2. Ved hjælp af Enum.ToObject() metoden."

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


Der er 2 måder At konvertere eller kaste `int` til `enum` i C#

1. Ved hjælp af eksplicit type casting i C#.
2. Brug af metoden `Enum.ToObject()` 

{{%toc%}}

## Løsning 1: Brug af C# eksplicit type casting

Den enkle måde at konvertere `int` til `enum` i C# er at bruge eksplicit type casting.

Lad os gennemgå et eksempel for at forstå det nærmere.

Vi har en `enum` type kaldet `LogLevel`, som repræsenterer forskellige niveauer af logning.

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

Eksplicit casting foretages ved at placere `enum` type i parentes foran værdien `int`.

Men der er et problem med ovenstående **C# `int` til `enum` konvertering**.

Hvad hvis `int` -værdien ikke findes i C# `Enum` -variablen?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Det vil ikke give nogen undtagelse.

Så det er bedre at kontrollere, om `int` -værdien findes i `C# Enum`, før den omformes til et heltal.

## Kontroller, om der findes et heltal eller ej i `C# enum` variabel

For at få alle de hele talværdier i `C# Enum` kan vi bruge `Enum.GetValues` -metoden.

Konverter dem til en liste på `C#`, så vi kan bruge metoden `list.Contains()` til at kontrollere, om det givne heltal findes i `enum` variabel.

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
Vi kan bruge `Enum.IsDefined()` metoden til at kontrollere, om den konverterede hele talværdi findes i den givne `enum` type.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Løsning 2: Brug `Enum.ToObject()` metoden

Vi kan bruge `C# Enum.ToObject()` metoden, konvertere `int` værdien til `enum` i C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





