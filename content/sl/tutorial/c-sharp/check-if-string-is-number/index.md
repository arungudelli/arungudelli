+++
title="Kako preveriti, ali je niz število v jeziku C#"
summary="Postopki za preverjanje, ali je niz število v jeziku c# 1. Deklarirajte celoštevilsko spremenljivko. 2.Podajte niz metodam `int.TryParse()` ali `double.TryParse()` s spremenljivko `out`. 3.Če je niz število, bo metoda `TryParse` vrnila true. In dodeli vrednost deklarirani vrednosti celega števila `out`."
keywords=["preverjanje, ali je niz število v jeziku C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Koraki za preverjanje, ali je niz število v jeziku C#

1. Razglasite spremenljivko s celim številom.
2. Podajte niz metodam `int.TryParse()` ali `double.TryParse()` s spremenljivko `out`.
3. Če je niz število, bo metoda `TryParse` vrnila true. In dodeli vrednost deklarirani celoštevilski vrednosti `out`.

{{%toc%}}

## Preverite, ali je niz število ali ne v jeziku C# 

Na primer, imamo spremenljivko z nizom "123" in če želite preveriti, ali je številka, uporabite spodnjo kodo C#.

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

Od C# 7 naprej lahko spremenljivko [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) deklariramo v sami metodi TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Težava zgornje metode `int.TryParse` je, da ne more preveriti negativnih vrednosti številskih nizov.

## Preverjanje negativnih števil v nizu v jeziku C# 

Za preverjanje negativnih vrednosti številskih nizov lahko uporabimo metodo C# `double.TryParse()`.

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

## Najboljši način za preverjanje, ali je niz število v C# 

Za preverjanje, ali je niz število, vedno uporabite metodo `double.TryParse()`, saj lahko preveri tako pozitivna kot negativna števila.