+++
title="Sådan kontrolleres det, om en streng er et tal i C#"
summary="Trin til at kontrollere, om en streng er et tal i c# 1.Deklarere en heltalsvariabel. 2.Overfør streng til `int.TryParse()` eller `double.TryParse()` metoder med `out` variabel. 3.Hvis strengen er et tal `TryParse` metoden returnerer sandt. Og tildeler værdi til den erklærede hele talværdi `out` værdi."
keywords=["check om en streng er et tal i C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Trin til at kontrollere, om en streng er et tal i C#

1. Deklarér en heltalsvariabel.
2. Overfør strengen til metoderne `int.TryParse()` eller `double.TryParse()` med variablen `out`.
3. Hvis strengen er et tal, returnerer `TryParse` metoden true. Og tildeler værdi til den erklærede hele talværdi `out` værdi.

{{%toc%}}

## Kontroller, om en streng er et tal eller ej i C# 

Vi har f.eks. en strengvariabel "123", og hvis du vil kontrollere, om den er numerisk, skal du bruge nedenstående C#-kode.

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

Fra C# 7 og fremefter kan vi erklære [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) variablen i selve TryParse-metoden.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Problemet med ovenstående `int.TryParse` -metode er, at den ikke kan kontrollere negative stringtalværdier.

## Kontrol af negative stringtal i C# 

For at kontrollere for negative stringtalværdier kan vi bruge C# `double.TryParse()` -metoden.

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

## Bedste måde at kontrollere, om en streng er et tal i C# 

Brug altid metoden `double.TryParse()` til at kontrollere, om en streng er et tal, fordi den kan validere både positive og negative tal.