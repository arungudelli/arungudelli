
+++
title="Miten saada enum nimi arvosta C#"
summary="On kaksi tapaa saada enum nimi arvosta C# 1. Käytä C# `Enum.GetName()` ja anna parametrina enum arvo saadaksesi nimen. 2. Muunna enum arvo enumeration-jäseneksi käyttämällä castingia ja käytä sitten `ToString()` -metodia."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Yksi enum:n suosituimmista käyttötapauksista on saada enum nimi sen arvosta.

Tarkastellaan reaalimaailman esimerkkiä: yleensä tallennamme tietokantaan enum -arvoja, eli tallennamme vain kokonaislukuarvoja 

Kun olemme lukeneet enum -arvon tietokannasta, meidän on muunnettava se takaisin sen enum -nimeksi.

C#:ssä on **kaksi tapaa saada enum nimi arvosta** 

{{%toc%}}

## Ratkaisu 1: Käyttämällä `Enum.GetName()`

C# `Enum.GetName()` -funktio ottaa kaksi parametria enum tyyppi ja arvo ja palauttaa enum nimen.

Otetaan esimerkki `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Nyt siirretään enum arvo `Enum.GetName()`:lle, jotta saadaan enum nimi 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Jos käytät C# `.Net 6` -versiota, voit siirtää vain enum -arvon (cast to enum) `Enum.GetName()` -metodiin.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Ratkaisu 2: Käyttämällä tyypinvalintaa

Toinen tapa on, Muunna enum arvo enumeration jäseneksi käyttämällä valua ja käytä sitten `ToString()` menetelmää.

Tämä on yksinkertainen tapa, jossa ei käytetä mitään `C# Enum` sisäänrakennettuja funktioita.

Muunna ensin enum arvo enumeration-jäseneksi ja käytä sitten `ToString()` -metodia.

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

## Yhteenveto

Tässä opetusohjelmassa opimme eri tapoja saada enum nimen arvo c#:ssa 

1. Välittämällä enum type- ja value-parametrit `Enum.GetName()` -metodiin
2. Ja käyttämällä tyypinvalintaa vastaavaan enum -tyyppiin 
