+++
title   ="Jak získat hodnotu `int` z `Enum` v jazyce C# s příklady"
summary ="Chcete-li získat hodnotu `int` z `enum` v jazyce C#, předveďte proměnnou enum na celé číslo."
keywords=["Hodnota int z enum v C#,Převést řetězec na enum v C#"]
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

Chcete-li získat hodnotu `int` z `enum` v jazyce C#, proveďte cast proměnné `enum` na celé číslo.

{{%toc%}}

## Řešení 1: Pro získání hodnoty `int` z adresy použijte typové obsazení `enum`

Výchozí základní typ pro `enums` v jazyce C# je `Int`.

Můžeme tedy provést type cast `enum` na `int`, abychom získali celočíselnou hodnotu z enumu v C#.

Pro bližší pochopení si uvedeme příklad.

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

Nyní budeme hodnoty enumů převádět na celočíselné hodnoty.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Řešení 2: Použijte metodu `Convert.ToInt32()` pro získání celočíselné hodnoty z enumu

Nebo můžeme použít metodu `Convert.ToInt32()` to pro převod `enum` na celé číslo, jak je uvedeno níže.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Získání hodnoty `enum` různých základních typů

`Enums` v jazyce C# mohou mít různé základní typy 

Pokud je C# enum deklarován jako `uint`, `long` nebo `ulong`, měli bychom jej předat na odpovídající typ `enum`.

Uvažujme níže uvedený příklad enumu `Stars`, který má typ `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```