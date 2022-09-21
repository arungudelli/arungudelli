+++
title   ="Hoe `int` te casten naar `enum` in C#"
summary ="Om `int` te casten naar `enum` in C#, type expliciet de `enum` variabele naar integer."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Om `int` te casten naar `enum` in C#, type expliciet cast de `enum` variabele naar integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Oplossing 1: Gebruik expliciete type casting van `enum` variabele

Laten we een voorbeeld bekijken om het verder te begrijpen.

We hebben een `enum` type met de naam `Days`, dat weekdagen vanaf maandag voorstelt.

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

Maar er is een probleem met de bovenstaande **`int` naar `enum` conversie**.

Wat als de `int` waarde niet bestaat in de C# `Enum` variabele?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Er zal geen uitzondering worden gemaakt.

Het is dus beter om te controleren of de `int` waarde bestaat in `Enum` alvorens het te casten naar het gehele getal.

## Controleer of een integer bestaat of niet in `enum` variabele

Om alle integer waarden in C# `Enum` te krijgen kunnen we de `Enum.GetValues` methode gebruiken.

Converteer ze naar C# lijst, zodat we `list.Contains()` methode kunnen gebruiken om te controleren of het gegeven gehele getal bestaat in `enum` variabele.

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
We kunnen de `Enum.IsDefined()` methode gebruiken om te controleren of de geconverteerde gehele waarde bestaat in het gegeven `enum` type.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Oplossing 2: gebruik `Enum.ToObject()` methode

We kunnen `Enum.ToObject()` methode gebruiken, om `int` waarde om te zetten naar `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





