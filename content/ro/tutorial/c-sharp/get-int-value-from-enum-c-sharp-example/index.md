+++
title   ="Cum să obțineți valoarea `int` din `Enum` în C# cu exemple"
summary ="Pentru a obține valoarea `int` din `enum` în C#, transformați variabila enum în întreg."
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

Pentru a obține valoarea `int` din `enum` în C#, transformați variabila `enum` în întreg.

{{%toc%}}

## Soluția 1: Utilizați Type cast pentru a obține valoarea `int` din `enum`

Tipul de bază implicit pentru `enums` în C# este `Int`.

Astfel, putem face type cast de la `enum` la `int` pentru a obține valoarea întreagă din enum în C#.

Vom lua un exemplu pentru a înțelege mai bine acest lucru.

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

Acum vom transforma valorile enum în valori întregi.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Soluția 2: Utilizați metoda `Convert.ToInt32()` pentru a obține valoarea întreagă din enum

Sau putem utiliza metoda `Convert.ToInt32()` to pentru a converti un `enum` în număr întreg, așa cum se arată mai jos.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Obțineți valoarea `enum` a diferitelor tipuri de bază

`Enums` în C# pot avea diferite tipuri de bază 

În cazul în care enum-ul C# este declarat ca fiind `uint`, `long` sau `ulong`, trebuie să îl transformăm în tipul corespunzător din `enum`.

Luați în considerare exemplul de mai jos al enumului `Stars`, care are un tip `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```