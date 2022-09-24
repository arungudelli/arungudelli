
+++
title="Cómo obtener el nombre enum del valor en C#"
summary="Hay dos maneras de obtener el nombre enum del valor en C# 1. Utilice C# `Enum.GetName()` y pase el valor enum como parámetro para obtener el nombre. 2. 2. Convertir el valor de enum al miembro de la eración enumusando el casting y luego usar el método `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Uno de los casos de uso más populares de enum es obtener el nombre de enum a partir de su valor.

Consideremos un ejemplo del mundo real, generalmente almacenaremos valores de enum en la base de datos, es decir, almacenaremos sólo valores enteros 

Y después de leer el valor enum de la base de datos tenemos que convertirlo de nuevo a su nombre enum.

Hay **dos formas de obtener el nombre enum a partir del valor en C#** 

{{%toc%}}

## Solución 1: Usando `Enum.GetName()`

C# `Enum.GetName()` la función toma dos parámetros enum tipo y valor y devuelve el nombre enum.

Tomemos un ejemplo de `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Ahora pasaremos el valor de enum a `Enum.GetName()` para obtener el nombre de enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Si estás usando la versión de C# `.Net 6`, puedes pasar sólo el valor de enum (cast to enum) al método `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Solución 2: Usar el casting de tipos

Otra forma es, convertir el valor de enum al miembro de la eración enumusando el casting y luego usar el método `ToString()`.

Esta es una forma sencilla que no utiliza ninguna función incorporada en `C# Enum`.

Primero convierta el valor de enum en el miembro enumy luego use el método `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Resumen

En este tutorial hemos aprendido diferentes formas de obtener el valor del nombre de enum en c# 

1. Pasando los parámetros de tipo y valor de enum al método `Enum.GetName()` 
2. Y utilizando el casting de tipo a la correspondiente enum tipo 
