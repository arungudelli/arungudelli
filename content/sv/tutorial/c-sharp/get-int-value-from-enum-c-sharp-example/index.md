+++
title   ="Hur man hämtar värdet `int` från `Enum` i C# med exempel"
summary ="Om du vill få fram `int` -värdet från `enum` i C#, kastar du enum-variabeln till heltal."
keywords=["int-värde från enum i C#,Konvertera sträng till enum i C#"]
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

Om du vill få fram `int` -värdet från `enum` i C#, kastar du `enum` -variabeln till heltal.

{{%toc%}}

## Lösning 1: Använd Type cast för att få fram `int` -värdet från `enum`

Den underliggande standardtypen för `enums` i C# är `Int`.

Så vi kan typkasta `enum` till `int` för att få ett heltalsvärde från enum i C#.

Vi tar ett exempel för att förstå det ytterligare.

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

Nu ska vi omvandla enumvärden till heltalsvärden.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Lösning 2: Använd `Convert.ToInt32()` -metoden för att få ett heltalsvärde från enum

Eller så kan vi använda `Convert.ToInt32()` to-metoden för att konvertera `enum` till heltal enligt nedan.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Hämta `enum` -värdet för olika underliggande typer

`Enums` i C# kan ha olika underliggande typer 

Om C# enum deklareras som `uint`, `long` eller `ulong` ska vi kasta det till motsvarande typ av `enum`.

Se nedanstående exempel på `Stars` enum, som har typen `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```