+++
title   ="Kuidas saada `int` väärtust `Enum` -st C# keeles koos näidetega"
summary ="Et saada `int` väärtust `enum` -st C# keeles, valage enum-muutuja täisarvuks."
keywords=["int väärtus enum'ist C# keeles,Convert string to enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Et saada `int` väärtus `enum` -st C#-s, valage `enum` muutuja täisarvuks.

{{%toc%}}

## Lahendus 1: Kasutage Type cast'i, et saada `int` väärtus muutujast `enum`

Vaikimisi aluseks olev tüüp `enums` on C# keeles `Int`.

Seega saame C#-is tüübistada `enum` tüübi `int` jaoks, et saada täisarvuline väärtus enum'ist.

Võtame näite, et seda paremini mõista.

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

Nüüd teisendame enumi väärtused täisarvulisteks väärtusteks.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Lahendus 2: Kasutame meetodit `Convert.ToInt32()`, et saada enum'ist täisarvuline väärtus

Või me võime kasutada `Convert.ToInt32()` to meetodit, et teisendada `enum` täisarvuks, nagu allpool näidatud.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Get the `enum` value of different underlying types (saada erinevate aluseks olevate tüüpide väärtused)

`Enums` c#-s võivad olla erinevad alusvaraks olevad tüübid 

Kui C# enum on deklareeritud kui `uint`, `long` või `ulong`, siis peaksime selle valama vastavale tüübile `enum`.

Vaadakem alljärgnevat näidet `Stars` enum, mille tüüp on `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```