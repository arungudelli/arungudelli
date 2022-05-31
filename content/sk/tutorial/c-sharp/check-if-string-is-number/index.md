+++
title="Ako skontrolovať, či je reťazec číslo v jazyku C#"
summary="Kroky na kontrolu, či je reťazec číslo v jazyku C# 1. Deklarovať celočíselnú premennú. 2.Pomocou premennej `out` odovzdajte reťazec metódam `int.TryParse()` alebo `double.TryParse()`. 3.Ak je reťazec číslo, metóda `TryParse` vráti true. A priradí hodnotu deklarovanej celočíselnej premennej `out`."
keywords=["kontrola, či je reťazec číslo v jazyku C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Kroky na kontrolu, či je reťazec číslo v jazyku C#

1. Deklarovanie celočíselnej premennej.
2. Pomocou premennej `out` odovzdajte reťazec metódam `int.TryParse()` alebo `double.TryParse()`.
3. Ak je reťazec číslo, metóda `TryParse` vráti true. A priradí hodnotu deklarovanej celočíselnej premennej `out`.

{{%toc%}}

## Kontrola, či je reťazec číslo alebo nie v jazyku C# 

Napríklad máme reťazcovú premennú "123" a ak chcete skontrolovať, či je to číslo, použite nasledujúci kód v jazyku C#.

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

Od C# 7 môžeme deklarovať premennú [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) v samotnej metóde TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Problémom uvedenej metódy `int.TryParse` je, že nedokáže kontrolovať záporné hodnoty reťazcových čísel.

## Kontrola záporného reťazcového čísla v jazyku C# 

Na kontrolu záporných hodnôt reťazcového čísla môžeme použiť metódu C# `double.TryParse()`.

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

## Najlepší spôsob, ako skontrolovať, či je reťazec číslo v jazyku C# 

Na overenie, či je reťazec číslo, vždy použite metódu `double.TryParse()`, pretože dokáže overiť kladné aj záporné čísla.