+++
title   ="2 načina za pretvorbo/cast int v enum v jeziku C#"
summary ="V jeziku C# sta 2 načina za cast int v enum 1. Z uporabo eksplicitnega ujemanja tipov v jeziku C#. 2. 2. Uporaba metode Enum.ToObject()."

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


Obstajata 2 načina za pretvorbo ali kastiranje `int` v `enum` v jeziku C#

1. Z uporabo eksplicitnega ujemanja tipov v jeziku C#.
2. Uporaba metode `Enum.ToObject()` 

{{%toc%}}

## Rešitev 1: Uporaba eksplicitnega uvajanja tipov v jeziku C#

Preprost način za pretvorbo `int` v `enum` v jeziku C# je uporaba eksplicitnega ujemanja tipov.

Za boljše razumevanje si oglejmo primer.

Imamo `enum` tip, imenovan `LogLevel`, ki predstavlja različne ravni beleženja.

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

Izrecno ujemanje se izvede tako, da se postavi `enum` tipa v oklepaju pred vrednostjo `int`.

Vendar pa obstaja težava z zgornjim **C# `int` na `enum` pretvorbo**.

Kaj če vrednost `int` ne obstaja v spremenljivki C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Ne bo vrgel nobene izjeme.

Zato je bolje preveriti, ali vrednost `int` obstaja v `C# Enum`, preden jo pretvorimo v celo število.

## Preverite, ali celo število obstaja ali ne v `C# enum` spremenljivki

Za pridobitev vseh celoštevilskih vrednosti v spremenljivki `C# Enum` lahko uporabimo metodo `Enum.GetValues`.

Pretvorimo jih v seznam `C#`, tako da lahko z metodo `list.Contains()` preverimo, ali dano celo število obstaja v `enum` spremenljivki.

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
Uporabimo lahko metodo `Enum.IsDefined()`, da preverimo, ali pretvorjena celoštevilska vrednost obstaja v danem `enum` tipu.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Rešitev 2: Uporabite metodo `Enum.ToObject()` 

Uporabimo lahko metodo `C# Enum.ToObject()` in pretvorimo vrednost `int` v `enum` v jeziku C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





