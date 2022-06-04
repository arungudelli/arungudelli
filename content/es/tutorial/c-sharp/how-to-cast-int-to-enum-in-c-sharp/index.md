+++
title   ="Cómo convertir `int` en `enum` en C#"
summary ="Para fundir `int` a `enum` en C#, fundir explícitamente la variable `enum` a entero"
keywords=["int a enum en C#,cast int a enum en C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Para convertir `int` en `enum` en C#, escriba explícitamente la variable `enum` en un número entero.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Solución 1: Usar el casting de tipo explícito de la variable `enum` 

Veamos un ejemplo para entenderlo mejor.

Tenemos un tipo `enum` llamado `Days`, que representa los días de la semana a partir del lunes.

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

int dayInteger = 6;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//Monday
```

Pero hay un problema con la conversión de`int` a `enum`.

¿Qué pasa si el valor `int` no existe en la variable C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

No lanzará ninguna excepción.

Así que es mejor comprobar si el valor de `int` existe en `Enum` antes de convertirlo en un entero.

## Comprobar si un entero existe o no en la variable `enum` 

Para obtener todos los valores enteros en C# `Enum` podemos utilizar el método `Enum.GetValues`.

Convertirlos en una lista de C#, de modo que podamos utilizar el método `list.Contains()` para comprobar si el entero dado existe en la variable `enum`.

```
var intValue = 100;
var enumValues = Enum.GetValues(typeof(Days)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
  Console.WriteLine("We can Cast int to Enum");  
   Days day = (Days) intValue;
}else{
  Console.WriteLine("Cannot Cast int to Enum");
}

```
Podemos utilizar el método `Enum.IsDefined()` para comprobar si el valor entero convertido existe en el tipo dado `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solución 2: Utilizar el método `Enum.ToObject()` 

Podemos utilizar el método `Enum.ToObject()`, para convertir el valor de `int` en `enum` en C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





