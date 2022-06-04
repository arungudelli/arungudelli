+++
title   ="Hoe `int` waarde te krijgen van `Enum` in C# met voorbeelden"
summary ="Om `int` waarde te krijgen van `enum` in C#, zet je de enum variabele om in integer."
keywords=["int value from enum in C#,Convert string to enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Om `int` waarde van `enum` in C# te krijgen, cast de `enum` variabele naar integer.

{{%toc%}}

## Oplossing 1: Gebruik Type cast om `int` waarde te krijgen van `enum`

Het standaard onderliggende type voor `enums` in C# is `Int`.

Dus we kunnen type cast gebruiken van `enum` naar `int` om de integer waarde van enum in C# te krijgen.

We zullen een voorbeeld nemen om het verder te begrijpen.

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
```

Nu zullen we enum waarden casten naar gehele getallen.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Oplossing 2: Gebruik `Convert.ToInt32()` methode om de integer waarde van enum te krijgen

Of we kunnen de `Convert.ToInt32()` to methode gebruiken om een `enum` om te zetten naar een geheel getal zoals hieronder getoond.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Verkrijg de `enum` waarde van verschillende onderliggende types

`Enums` in C# kunnen verschillende onderliggende types hebben 

Als C# enum wordt gedeclareerd als `uint`, `long`, of `ulong` moeten we het casten naar het overeenkomstige type van de `enum`.

Beschouw het onderstaande voorbeeld van `Stars` enum, die een type `long` heeft.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```