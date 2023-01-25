+++
title   ="2 tapaa muuntaa/castata int muotoon enum in C#"
summary ="On 2 tapaa castata int muotoon enum in C# 1. Käyttämällä C#:n eksplisiittistä tyypinvalintaa. 2. Käyttämällä Enum.ToObject()-menetelmää."

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


On 2 tapaa muuntaa tai valaa `int` muotoon `enum` c#:ssa

1. Käyttämällä C#:n eksplisiittistä tyyppivalintaa.
2. `Enum.ToObject()` -menetelmän käyttäminen

{{%toc%}}

## Ratkaisu 1: C#:n eksplisiittisen tyypinvalinnan käyttäminen

Yksinkertainen tapa muuntaa `int` muotoon `enum` c#-kielellä on käyttää eksplisiittistä tyypinvalintaa.

Käydään läpi esimerkki sen ymmärtämiseksi tarkemmin.

Meillä on `enum` tyyppi nimeltään `LogLevel`, joka edustaa eri kirjaustasoja.

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

Eksplisiittinen valu tehdään sijoittamalla `enum` tyyppi sulkeisiin `int` arvon eteen.

Mutta on olemassa ongelma, kun edellä **C# `int` to `enum` muuntamisessa**.

Entä jos `int` -arvoa ei ole olemassa C# `Enum` -muuttujassa?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Se ei aiheuta poikkeusta.

On siis parempi tarkistaa, onko `int` -arvo olemassa osoitteessa `C# Enum`, ennen kuin se valetaan kokonaisluvuksi.

## Tarkista, onko kokonaisluku olemassa vai ei `C# enum` muuttujassa

Saadaksemme kaikki kokonaislukuarvot muuttujasta `C# Enum` voimme käyttää `Enum.GetValues` -menetelmää.

Muunnetaan ne `C#` -luetteloksi, jotta voimme käyttää `list.Contains()` -menetelmää tarkistaaksemme, onko annettu kokonaisluku olemassa muuttujassa `enum` muuttuja.

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
Voimme käyttää `Enum.IsDefined()` -menetelmää tarkistaaksemme, onko muunnettu kokonaislukuarvo olemassa annetussa muuttujassa `enum` tyyppi.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Ratkaisu 2: Käytä `Enum.ToObject()` -menetelmää

Voimme käyttää `C# Enum.ToObject()` -menetelmää, muuntaa `int` arvon muotoon `enum` c#-kielellä.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





