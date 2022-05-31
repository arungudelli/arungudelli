+++
title="Kaip patikrinti, ar eilutė yra skaičius, naudojant C#"
summary="Žingsniai, kaip patikrinti, ar eilutė yra skaičius C# kalba 1. Deklaruokite sveikojo skaičiaus kintamąjį. 2.Perduokite eilutę `int.TryParse()` arba `double.TryParse()` metodams su `out` kintamuoju. 3.Jei eilutė yra skaičius, `TryParse` metodas grąžins true. Ir priskiria reikšmę deklaruotai sveikojo skaičiaus `out` reikšmei."
keywords=["Patikrinti, ar eilutė yra skaičius C# kalba"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Žingsniai, kaip patikrinti, ar eilutė yra skaičius C# kalba

1. Deklaruokite sveikojo skaičiaus kintamąjį.
2. Perduokite eilutę `int.TryParse()` arba `double.TryParse()` metodams su `out` kintamuoju.
3. Jei eilutė yra skaičius, `TryParse` metodas grąžins true. Ir priskiria reikšmę deklaruotai sveikojo skaičiaus `out` reikšmei.

{{%toc%}}

## Patikrinkite, ar eilutė yra skaičius, ar ne, C# kalba 

Pavyzdžiui, turime eilutės kintamąjį "123" ir jei norite patikrinti, ar jis yra skaičius, naudokite toliau pateiktą C# kodą.

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

Nuo C# 7 galime deklaruoti kintamąjį [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) pačiame TryParse metode.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Pirmiau pateikto `int.TryParse` metodo problema yra ta, kad jis negali patikrinti neigiamų eilutės skaičių reikšmių.

## Neigiamo eilutės skaičiaus tikrinimas C# 

Norėdami patikrinti, ar yra neigiamų eilutės skaičių reikšmių, galime naudoti C# `double.TryParse()` metodą.

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

## Geriausias būdas patikrinti, ar eilutė yra skaičius C# 

Norėdami patikrinti, ar eilutė yra skaičius, visada naudokite `double.TryParse()` metodą, nes juo galima patikrinti ir teigiamus, ir neigiamus skaičius.