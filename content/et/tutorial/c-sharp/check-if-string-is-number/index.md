+++
title="Kuidas kontrollida, kas string on number C# keeles"
summary="Sammud, et kontrollida, kas string on number c#-s 1.Deklareeri täisarvuline muutuja. 2.Andke string üle `int.TryParse()` või `double.TryParse()` meetoditele koos `out` muutujaga. 3.Kui string on number `TryParse` meetod tagastab true. Ja omistab väärtuse deklareeritud täisarvu `out` väärtusele."
keywords=["kontrollida, kas string on number C# keeles"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Sammud, et kontrollida, kas string on number C# keeles

1. Deklareerige täisarvuline muutuja.
2. Anda string üle `int.TryParse()` või `double.TryParse()` meetoditele koos `out` muutujaga.
3. Kui string on arv `TryParse` meetod tagastab true. Ja omistab deklareeritud täisarvu `out` väärtuse.

{{%toc%}}

## Kontrollida, kas string on number või mitte C# keeles 

Näiteks on meil string-muutuja "123" ja kui soovite kontrollida, kas see on numbriline, siis kasutage alljärgnevat C# koodi.

```
var stringNumber = "123";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is true and numericValue=123

var stringNumber = "123P";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is false and numericValue=0 default value

```

Alates C# 7-st saame me deklareerida [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) muutuja TryParse meetodis ise.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Probleem ülaltoodud `int.TryParse` meetodi puhul on see, et see ei saa kontrollida negatiivseid stringi numbrite väärtusi.

## Negatiivse stringi numbri kontrollimine C# keeles 

Negatiivsete stringarvude väärtuste kontrollimiseks saame kasutada C# `double.TryParse()` meetodit.

```
var negativeString = "-123";
double number;
if(double.TryParse(negativeString,out number)){
   if (number > 0){

   }else{
       //negative number 
   }   
}
```

## Parim viis kontrollida, kas string on number C# keeles 

Kasutage alati meetodit `double.TryParse()`, et kontrollida, kas string on number, sest see saab kontrollida nii positiivseid kui ka negatiivseid numbreid.