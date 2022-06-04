+++
title   ="Hogyan szerezhetünk `int` értéket a `Enum` oldalról C# nyelven példákkal"
summary ="A `int` értékének kinyerése a `enum` -ből C# nyelven, az enum változót egész számra kell átváltoztatni."
keywords=["int érték enumból C#-ban,Convert string to enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To get `int` value from `enum` in C#, cast the `enum` variable to integer.

{{%toc%}}

## 1. megoldás: Type cast segítségével a `int` értéket a következőből kapjuk meg `enum`

A `enums` alapértelmezett típusa C#-ban a `Int`.

Így a `enum` -t a `int` típusba típusátvétellel egész szám értéket kaphatunk az enumból a C#-ban.

A további megértéshez vegyünk egy példát.

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

Most az enum értékeket fogjuk egész számokká alakítani.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## 2. megoldás: A `Convert.ToInt32()` metódus segítségével egész értéket kapunk az enumból

Vagy használhatjuk a `Convert.ToInt32()` to metódust a `enum` egész számmá alakításához, ahogy az alábbiakban látható.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## A `enum` értékének kinyerése különböző mögöttes típusok esetén

`Enums` c#-ban különböző mögöttes típusok lehetnek 

Ha a C# enumot `uint`, `long`, vagy `ulong` -ként deklaráljuk, akkor a `enum` megfelelő típusára kell castolnunk.

Tekintsük az alábbi példát a `Stars` enumra, amelynek típusa `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```