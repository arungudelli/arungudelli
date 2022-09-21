+++
title   ="Cómo obtener el valor de `int` de `Enum` en C# con ejemplos"
summary ="Para obtener el valor de `int` desde `enum` en C#, convierte la variable enum en un entero"
keywords=["Valor int de enum en C#,Convertir cadena a enum en C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Para obtener el valor de `int` a partir de `enum` en C#, convierta la variable `enum` en un número entero.

{{%toc%}}

## Solución 1: Usar Type cast para obtener el valor de `int` de `enum`

El tipo subyacente por defecto para `enums` en C# es `Int`.

Así que podemos hacer un type cast de `enum` a `int` para obtener el valor entero del enum en C#.

Vamos a tomar un ejemplo para entenderlo mejor.

```
public enum Days
{
        Monday,  
        Tuesday,  
        Wednesday,  
        Thursday,  
        Friday,  
        Saturday,  
        Sunday
}
```

Ahora vamos a convertir los valores del enum en valores enteros.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Solución 2: Usar el método `Convert.ToInt32()` para obtener el valor entero del enum

O podemos usar el método `Convert.ToInt32()` to para convertir un `enum` a entero como se muestra a continuación.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Obtener el valor de `enum` de diferentes tipos subyacentes

`Enums` en C# puede tener diferentes tipos subyacentes 

Si el enum de C# se declara como `uint`, `long`, o `ulong` debemos lanzarlo al tipo correspondiente del `enum`.

Considere el siguiente ejemplo de `Stars` enum, que tiene un tipo `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```