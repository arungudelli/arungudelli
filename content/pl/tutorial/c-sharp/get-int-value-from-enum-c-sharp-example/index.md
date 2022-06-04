+++
title   ="Jak uzyskać wartość `int` z `Enum` w C# z przykładami"
summary ="Aby uzyskać wartość `int` z `enum` w C#, zamień zmienną enum na liczbę całkowitą."
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

Aby uzyskać wartość `int` z `enum` w C#, zamień zmienną `enum` na liczbę całkowitą.

{{%toc%}}

## Rozwiązanie 1: Użyj rzutowania typu, aby uzyskać wartość `int` z `enum`

Domyślnym typem bazowym dla `enums` w C# jest `Int`.

Możemy więc zamienić typ `enum` na `int`, aby uzyskać wartość całkowitą z enum w C#.

Aby lepiej to zrozumieć, posłużymy się przykładem.

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

Teraz zamienimy wartości wyliczeniowe na wartości całkowite.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Rozwiązanie 2: Użyj metody `Convert.ToInt32()`, aby uzyskać wartość całkowitą z enum

Możemy też użyć metody `Convert.ToInt32()` to do konwersji wartości `enum` na liczbę całkowitą, jak pokazano poniżej.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Uzyskaj wartość `enum` dla różnych typów bazowych

`Enums` w języku C# mogą mieć różne typy bazowe 

Jeśli w języku C# enum jest zadeklarowane jako `uint`, `long`, lub `ulong`, powinniśmy rzutować je na odpowiadający im typ `enum`.

Rozważmy poniższy przykład enum `Stars`, które ma typ `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```