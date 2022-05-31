+++
title="Kuinka tarkistaa, onko merkkijono numero C#:ssa"
summary="Vaiheet tarkistaa, onko merkkijono on numero c# 1.Declare kokonaislukumuuttuja. 2.Siirrä merkkijono `int.TryParse()` tai `double.TryParse()` metodeihin `out` muuttujan avulla. 3.Jos merkkijono on luku `TryParse` metodi palauttaa true. Ja antaa arvon ilmoitetulle kokonaisluvulle `out` arvo."
keywords=["tarkista onko merkkijono numero C#:ssa"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Vaiheet, joilla tarkistetaan, onko merkkijono numero C#:ssa

1. Ilmoita kokonaislukumuuttuja.
2. Siirrä merkkijono `int.TryParse()` - tai `double.TryParse()` -metodeihin `out` -muuttujan avulla.
3. Jos merkkijono on luku, `TryParse` metodi palauttaa arvon true. Ja antaa arvon ilmoitetulle kokonaisluvulle `out` arvo.

{{%toc%}}

## Tarkista, onko merkkijono numero vai ei C#:ssä 

Meillä on esimerkiksi merkkijonomuuttuja "123", ja jos haluat tarkistaa, onko se numero, käytä alla olevaa C#-koodia.

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

C# 7:stä lähtien voimme ilmoittaa [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) -muuttujan itse TryParse-menetelmässä.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Yllä olevan `int.TryParse` -menetelmän ongelmana on, että se ei voi tarkistaa negatiivisia merkkijonon lukuarvoja.

## Negatiivisen merkkijonon tarkistaminen C#:ssä 

Negatiivisten merkkijonon lukuarvojen tarkistamiseen voidaan käyttää C#:n `double.TryParse()` -menetelmää.

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

## Paras tapa tarkistaa, onko merkkijono numero C#:ssä 

Käytä aina `double.TryParse()` -menetelmää tarkistaaksesi, onko merkkijono luku, koska se voi tarkistaa sekä positiiviset että negatiiviset luvut.