+++
title="Cómo comprobar si una cadena es un número en C#"
summary="Pasos para comprobar si una cadena es un número en c# 1.Declarar una variable entera. 2.2.Pasar la cadena a los métodos `int.TryParse()` o `double.TryParse()` con la variable `out`. 3.Si la cadena es un número el método `TryParse` devolverá true. Y asigna el valor al valor entero declarado `out` "
keywords=["comprobar si una cadena es un número en C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Pasos para comprobar si una cadena es un número en C#

1. Declarar una variable entera.
2. Pasar la cadena a los métodos `int.TryParse()` o `double.TryParse()` con la variable `out`.
3. Si la cadena es un número el método `TryParse` devolverá true. Y asigna el valor al valor entero declarado `out`.

{{%toc%}}

## Comprobar si una cadena es un Número o no en C# 

Por ejemplo tenemos una variable de cadena "123" y si quieres comprobar si es numérica utiliza el siguiente código C#.

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

A partir de C# 7 podemos declarar la variable [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) en el propio método TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

El problema con el método anterior `int.TryParse` es que no puede comprobar los valores numéricos de cadena negativos.

## Comprobación de un número de cadena negativo en C# 

Para comprobar los valores negativos de los números de cadena podemos utilizar el método C# `double.TryParse()`.

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

## La mejor manera de comprobar si una cadena es un número en C# 

Utilice siempre el método `double.TryParse()` para comprobar si una cadena es un número, ya que puede validar tanto números positivos como negativos.