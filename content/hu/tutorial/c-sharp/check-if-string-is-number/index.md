+++
title="Hogyan ellenőrizhetjük, hogy egy karakterlánc egy szám-e C# nyelven"
summary="Lépések annak ellenőrzéséhez, hogy egy karakterlánc szám-e c# nyelven 1.Deklaráljunk egy egész szám változót. 2.Adjuk át a stringet a `int.TryParse()` vagy a `double.TryParse()` metódusoknak a `out` változóval. 3.Ha a string egy szám, a `TryParse` metódus true-t fog visszaadni. És értéket rendel a deklarált egész szám `out` értékéhez."
keywords=["check if a string is number in C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Lépések annak ellenőrzéséhez, hogy egy karakterlánc szám-e C# nyelven

1. Deklaráljunk egy egész szám változót.
2. Adjuk át a stringet a `int.TryParse()` vagy a `double.TryParse()` metódusoknak a `out` változóval.
3. Ha a string egy szám, a `TryParse` metódus true-t ad vissza. És értéket rendel a deklarált egész számhoz `out` értéket.

{{%toc%}}

## Annak ellenőrzése, hogy egy karakterlánc szám-e vagy sem C# nyelven 

Például van egy "123" string változó, és ha ellenőrizni akarjuk, hogy szám-e, akkor használjuk az alábbi C# kódot.

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

A C# 7-től kezdődően a TryParse metódusban is deklarálhatjuk az [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) változót.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

A fenti `int.TryParse` módszerrel az a probléma, hogy nem tudja ellenőrizni a negatív string számértékeket.

## Negatív string szám ellenőrzése C# nyelven 

A negatív stringszám értékek ellenőrzésére használhatjuk a C# `double.TryParse()` módszert.

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

## A legjobb módja annak, hogy ellenőrizzük, hogy a string szám-e C# nyelven 

Mindig a `double.TryParse()` módszert használjuk annak ellenőrzésére, hogy egy karakterlánc szám-e, mivel ez a módszer pozitív és negatív számokat is képes érvényesíteni.