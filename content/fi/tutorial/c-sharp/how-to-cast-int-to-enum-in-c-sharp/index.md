+++
title   ="Kuinka `int` valetaan `enum`:ksi C#:ssa"
summary ="Jos haluat castata `int` muotoon `enum` C#:ssa, kirjoita nimenomaisesti tyyppi cast `enum` muuttuja kokonaisluvuksi."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Jos haluat castata `int` muotoon `enum` C#:ssa, kirjoita nimenomaisesti cast `enum` -muuttuja kokonaisluvuksi.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Ratkaisu 1: Muuttujan `enum` nimenomaisen tyypinvalinnan käyttäminen

Käydään läpi esimerkki, jotta asia ymmärretään paremmin.

Meillä on `enum` -tyyppi nimeltään `Days`, joka edustaa maanantaista alkavia viikonpäiviä.

```
public enum Days
{
        Monday,  
        Tuesday,  
        Wednesday,  
        Thursday,  
        Friday,  
        Saturday,  
        Sunday
}

int dayInteger = 6;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//Monday
```

Mutta edellä mainitussa **`int`:n muuntamisessa `enum`:ksi** on ongelma.

Mitä jos `int` arvoa ei ole olemassa C# `Enum` -muuttujassa?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Se ei aiheuta poikkeusta.

On siis parempi tarkistaa, onko `int` -arvo olemassa osoitteessa `Enum`, ennen kuin se heitetään kokonaisluvuksi.

## Tarkista, onko kokonaisluku olemassa `enum` -muuttujassa vai ei

Saadaksemme kaikki kokonaislukuarvot C# `Enum` -muuttujasta voimme käyttää `Enum.GetValues` -menetelmää.

Muunnetaan ne C#-luetteloksi, jotta voimme käyttää `list.Contains()` -metodia tarkistaaksemme, onko annettu kokonaisluku olemassa `enum` -muuttujassa.

```
var intValue = 100;
var enumValues = Enum.GetValues(typeof(Days)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
  Console.WriteLine("We can Cast int to Enum");  
   Days day = (Days) intValue;
}else{
  Console.WriteLine("Cannot Cast int to Enum");
}

```
Voimme käyttää `Enum.IsDefined()` -menetelmää tarkistaaksemme, onko muunnettu kokonaislukuarvo olemassa annetussa `enum` -tyypissä.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Ratkaisu 2: Käytä `Enum.ToObject()` -menetelmää

Voimme käyttää `Enum.ToObject()` -metodia, muuntaa `int` -arvon `enum` -arvoksi C#:ssa.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





