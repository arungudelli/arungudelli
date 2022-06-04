+++
title   ="Sådan får du `int` -værdien fra `Enum` i C# med eksempler"
summary ="For at få `int` -værdien fra `enum` i C# skal du omdanne enum-variablen til heltal."
keywords=["int-værdi fra enum i C#,Konverter streng til enum i C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

For at få `int` -værdien fra `enum` i C# skal du omdanne `enum` -variablen til et heltal.

{{%toc%}}

## Løsning 1: Brug Type cast til at få `int` -værdien fra `enum`

Den underliggende standardtype for `enums` i C# er `Int`.

Så vi kan typekaste `enum` til `int` for at få den heltalsværdi fra enum i C#.

Vi vil tage et eksempel for at forstå det yderligere.

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

Nu skal vi omdanne enum-værdier til heltalsværdier.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Løsning 2: Brug `Convert.ToInt32()` -metoden til at hente en helhedsværdi fra enum

Eller vi kan bruge `Convert.ToInt32()` to-metoden til at konvertere en `enum` til et heltal som vist nedenfor.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Hent `enum` -værdien af forskellige underliggende typer

`Enums` i C# kan have forskellige underliggende typer 

Hvis C# enum er erklæret som `uint`, `long` eller `ulong` skal vi kaste den til den tilsvarende type af `enum`.

Se nedenstående eksempel på `Stars` enum, som har typen `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```