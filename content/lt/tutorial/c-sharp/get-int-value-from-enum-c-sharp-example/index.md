+++
title   ="Kaip gauti `int` reikšmę iš `Enum` C# kalba su pavyzdžiais"
summary ="Norėdami gauti `int` reikšmę iš `enum` C# kalba, paverskite sąrašo kintamąjį sveikuoju skaičiumi."
keywords=["Int reikšmė iš enum C#, Konvertuoti eilutę į enum C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Norėdami gauti `int` reikšmę iš `enum` in C#, `enum` kintamąjį paverskite sveikuoju skaičiumi.

{{%toc%}}

## 1 sprendimas: naudokite Type cast, kad gautumėte `int` reikšmę iš `enum`

Numatytasis pagrindinis `enums` tipas C# kalboje yra `Int`.

Taigi, norėdami gauti sveikojo skaičiaus reikšmę iš C# enumo, galime `enum` tipą pakeisti į `int`.

Kad geriau suprastume, pateiksime pavyzdį.

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

Dabar enum reikšmes paversime sveikųjų skaičių reikšmėmis.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## 2 sprendimas: Naudokite `Convert.ToInt32()` metodą, kad iš enum gautumėte sveikojo skaičiaus reikšmę

Arba galime naudoti `Convert.ToInt32()` to metodą, kad konvertuotume `enum` į sveiką skaičių, kaip parodyta toliau.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Gauti skirtingų pagrindinių tipų `enum` reikšmę

`Enums` c# gali turėti skirtingus pagrindinius tipus 

Jei C# enumas deklaruojamas kaip `uint`, `long` arba `ulong`, turėtume jį paversti atitinkamu `enum` tipu.

Panagrinėkime toliau pateiktą `Stars` enumo pavyzdį, kuris turi tipą `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```