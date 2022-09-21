+++
title   ="Kako pridobiti vrednost `int` iz `Enum` v jeziku C# s primeri"
summary ="Če želite dobiti vrednost `int` iz `enum` v C#, spremenljivko enum pretvorite v celo število."
keywords=["Vrednost int iz enuma v C#,Pretvori niz v enum v C#"]
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

Če želite dobiti vrednost `int` iz `enum` v jeziku C#, spremenljivko `enum` pretvorite v celo število.

{{%toc%}}

## Rešitev 1: Uporabite Type cast, da dobite vrednost `int` iz `enum`

Privzeta osnovna vrsta za `enums` v jeziku C# je `Int`.

Zato lahko `enum` tipsko castnemo v `int`, da dobimo celoštevilsko vrednost iz enuma v C#.

Za nadaljnje razumevanje si bomo ogledali primer.

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

Zdaj bomo vrednosti enumov pretvorili v celoštevilske vrednosti.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Rešitev 2: Za pridobitev celoštevilske vrednosti iz enuma uporabite metodo `Convert.ToInt32()` 

Lahko pa uporabimo tudi metodo `Convert.ToInt32()` to za pretvorbo `enum` v celo število, kot je prikazano spodaj.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Pridobite vrednost `enum` različnih osnovnih tipov

`Enums` v jeziku C# imajo lahko različne osnovne tipe 

Če je C# enum deklariran kot `uint`, `long` ali `ulong`, ga moramo kastirati na ustrezen tip `enum`.

Upoštevajte spodnji primer enuma `Stars`, ki ima tip `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```