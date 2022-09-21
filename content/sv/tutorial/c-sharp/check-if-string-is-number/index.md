+++
title="Hur man kontrollerar om en sträng är ett nummer i C#"
summary="Steg för att kontrollera om en sträng är ett tal i c# 1.Deklarera en heltalsvariabel. 2.Skicka strängen till metoderna `int.TryParse()` eller `double.TryParse()` med variabeln `out`. 3.Om strängen är ett tal kommer `TryParse` -metoden att returnera true. Och tilldelar värdet till det deklarerade heltalsvärdet `out` värde."
keywords=["kontrollera om en sträng är ett nummer i C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Steg för att kontrollera om en sträng är ett tal i C#

1. Deklarera en heltalsvariabel.
2. Skicka strängen till metoderna `int.TryParse()` eller `double.TryParse()` med variabeln `out`.
3. Om strängen är ett tal kommer metoden `TryParse` att återge true. Och tilldelar värdet till det deklarerade heltalsvärdet `out` värde.

{{%toc%}}

## Kontrollera om en sträng är ett tal eller inte i C# 

Vi har till exempel en strängvariabel "123" och om du vill kontrollera om den är numerisk kan du använda nedanstående C#-kod.

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

Från och med C# 7 kan vi deklarera variabeln [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) i själva TryParse-metoden.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Problemet med ovanstående `int.TryParse` -metod är att den inte kan kontrollera negativa strängnummervärden.

## Kontroll av negativa strängnummer i C# 

För att kontrollera negativa strängnummervärden kan vi använda C# `double.TryParse()` -metoden.

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

## Bästa sättet att kontrollera om strängen är ett nummer i C# 

Använd alltid metoden `double.TryParse()` för att kontrollera om en sträng är ett tal, eftersom den kan godkänna både positiva och negativa tal.