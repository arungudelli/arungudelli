+++
title   ="2 viisi, kuidas konverteerida / casta int to enum in C#"
summary ="On 2 viisi, kuidas casta int to enum in C# 1. Kasutades C# eksplitsiitset tüübi valimist. 2. Kasutades meetodit Enum.ToObject()."

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


On 2 võimalust, kuidas teisendada või valada `int` to `enum` c# keeles

1. Kasutades C# selgesõnalist tüübi valimist.
2. Kasutades `Enum.ToObject()` meetodit

{{%toc%}}

## Lahendus 1: C# selgesõnalise tüübi valimise kasutamine

Lihtne viis konverteerida `int` `enum` c# keeles on kasutada selgesõnalist tüübivahetust.

Vaatame läbi näite, et seda paremini mõista.

Meil on olemas `enum` tüüp nimega `LogLevel`, mis esindab erinevaid logimise tasemeid.

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

Eksplitsiitne valimine toimub paigutades `enum` tüüp sulgudes `int` väärtuse ette.

Kuid ülaltoodud **C# `int` puhul on probleemiks, et `enum` teisendamisega**.

Mis siis, kui `int` väärtust ei ole C# `Enum` muutujas olemas?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

See ei tekita ühtegi erandit.

Seega on parem kontrollida, kas `int` väärtus on olemas aadressil `C# Enum`, enne kui see täisarvuks valatakse.

## Kontrollida, kas täisarv on olemas või mitte `C# enum` muutuja

Kõigi täisarvuliste väärtuste saamiseks `C# Enum` saame kasutada `Enum.GetValues` meetodit.

Konverteerida need `C#` loendiks, et saaksime kasutada `list.Contains()` meetodit, et kontrollida, kas antud täisarv on olemas `enum` muutuja.

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
Me saame kasutada `Enum.IsDefined()` meetodit, et kontrollida, kas teisendatud täisarvu väärtus on olemas antud muutujas `enum` tüüpi.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Lahendus 2: Kasutage `Enum.ToObject()` meetodit

Me võime kasutada `C# Enum.ToObject()` meetodit, teisendada `int` väärtust `enum` c# keeles.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





