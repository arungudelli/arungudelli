+++
title   ="Ako získať hodnotu `int` z `Enum` v jazyku C# s príkladmi"
summary ="Ak chcete získať hodnotu `int` z `enum` v jazyku C#, odovzdajte premennú enum na celé číslo."
keywords=["int value from enum in C#,Convert string to enum in C#"]
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

Ak chcete získať hodnotu `int` z `enum` v jazyku C#, prehoďte premennú `enum` na celé číslo.

{{%toc%}}

## Riešenie 1: Použite typ cast na získanie hodnoty `int` z `enum`

Predvolený základný typ pre `enums` v jazyku C# je `Int`.

Takže môžeme typ cast `enum` na `int`, aby sme získali celočíselnú hodnotu z enumu v C#.

Pre bližšie pochopenie si uvedieme príklad.

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

Teraz budeme hodnoty enumov premieňať na celočíselné hodnoty.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Riešenie 2: Na získanie celočíselnej hodnoty z enumu použite metódu `Convert.ToInt32()` 

Alebo môžeme použiť metódu `Convert.ToInt32()` to na prevod `enum` na celé číslo, ako je uvedené nižšie.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Získanie hodnoty `enum` rôznych základných typov

`Enums` v jazyku C# môžu mať rôzne základné typy 

Ak je enum v jazyku C# deklarovaný ako `uint`, `long` alebo `ulong`, mali by sme ho odovzdať na príslušný typ `enum`.

Uvažujme nasledujúci príklad enumu `Stars`, ktorý má typ `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```