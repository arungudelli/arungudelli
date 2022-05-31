+++
title="Jak zkontrolovat, zda je řetězec číslo v jazyce C#"
summary="Kroky pro kontrolu, zda je řetězec číslo v jazyce C# 1. Deklarujte celočíselnou proměnnou. 2.Předejte řetězec metodám `int.TryParse()` nebo `double.TryParse()` pomocí proměnné `out`. 3.Pokud je řetězec číslo, metoda `TryParse` vrátí true. A přiřadí hodnotu deklarovanému celému číslu `out`."
keywords=["kontrola, zda je řetězec číslo v jazyce C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Kroky pro kontrolu, zda je řetězec číslo v jazyce C#

1. Deklarujte celočíselnou proměnnou.
2. Předejte řetězec metodám `int.TryParse()` nebo `double.TryParse()` pomocí proměnné `out`.
3. Pokud je řetězec číslo, metoda `TryParse` vrátí true. A přiřadí hodnotu deklarovanému celému číslu `out`.

{{%toc%}}

## Kontrola, zda je řetězec číslo, nebo ne v jazyce C# 

Například máme řetězcovou proměnnou "123" a pokud chcete zkontrolovat, zda je číselná, použijte následující kód v jazyce C#.

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

Od C# 7 můžeme proměnnou [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) deklarovat přímo v metodě TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Problémem výše uvedené metody `int.TryParse` je, že neumí kontrolovat záporné hodnoty řetězcových čísel.

## Kontrola záporného řetězcového čísla v jazyce C# 

Pro kontrolu záporných hodnot řetězcových čísel můžeme použít metodu C# `double.TryParse()`.

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

## Nejlepší způsob, jak v jazyce C# zkontrolovat, zda je řetězec číslo 

Pro kontrolu, zda je řetězec číslo, vždy používejte metodu `double.TryParse()`, protože dokáže ověřit kladná i záporná čísla.