+++
title   ="2 maneras de convertir/cast int a enum en C#"
summary ="Hay 2 maneras Para cast int a enum en C# 1. Usando la conversión explícita de tipos en C#. 2. 2. Usando el método Enum.ToObject()"

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Hay 2 maneras Para convertir o cast `int` a `enum` en C#

1. Usando la conversión explícita de tipos en C#.
2. Usando el método `Enum.ToObject()` 

{{%toc%}}

## Solución 1: Usando el casting de tipos explícito de C#

La forma más sencilla de convertir `int` a `enum` en C# es utilizar la conversión explícita de tipos.

Veamos un ejemplo para entenderlo mejor.

Tenemos un tipo `enum` llamado `LogLevel`, que representa diferentes niveles de registro.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

El reparto explícito se realiza colocando el tipo `enum` entre paréntesis delante del valor `int`.

Pero hay un problema con el anterior **C# `int` a `enum` conversión**.

¿Qué pasa si el valor `int` no existe en la variable C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

No se lanzará ninguna excepción.

Así que es mejor comprobar si el valor `int` existe en `C# Enum` antes de convertirlo en un entero.

## Comprueba si existe o no un entero en `C# enum` variable

Para obtener todos los valores enteros en `C# Enum` podemos utilizar el método `Enum.GetValues`.

Convertirlos a la lista `C#`, para que podamos utilizar el método `list.Contains()` para comprobar si el entero dado existe en `enum` en la variable.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Podemos usar el método `Enum.IsDefined()` para comprobar si el valor entero convertido existe en el tipo dado `enum` dado.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solución 2: Utilice el método `Enum.ToObject()` 

Podemos utilizar el método `C# Enum.ToObject()`, convertir el valor de `int` a `enum` en C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





