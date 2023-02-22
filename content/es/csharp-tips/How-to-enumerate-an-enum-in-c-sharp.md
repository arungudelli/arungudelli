---
title: "Cómo hacer un bucle/enumerar un enum en C#"
description: "Diferentes formas de hacer un bucle o enumerar un enum en C# con ejemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Los enums son ampliamente utilizados en el lenguaje `C#`. 

Y hay 4 maneras de bucle o enumerar enum en `C#`. 

1. Usando `C# Enum.GetValues()` en .Net 5 y superiores.
2. Usando `C# Enum.GetValues()` en versiones anteriores de .Net.
3. Usando `C# Enum.GetNames()` para enumerar nombres de enum como cadenas.
4. Uso de `Linq`

Veamos un ejemplo para entenderlo mejor. 

Primero crearemos un archivo C `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` que representa diferentes tipos de niveles de registro.

Ahora veremos diferentes formas de enumerar el `C# enum`.

## Usando `C# Enum.GetValues()` Método genérico en .Net 5 y superiores

Si está utilizando la última versión de `.Net`, es decir, `.Net 5` y superiores puede utilizar la versión genérica para el método `Enum.GetValues` para realizar un bucle a través de `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

La nueva versión genérica de `Enum.GetValues` devuelve el array de valores enum. 

Además, podemos utilizar las sentencias `for` o `foreach` para enumerar el `C# enum`. 

Como el array contiene el tipo `enum` necesitamos convertirlo a cadena usando el método `ToString()`.

## Usando `C# Enum.GetValues()` en versiones antiguas de .Net.

En las versiones anteriores de `.Net` no hay ningún método genérico disponible para el método `Enum.GetValues()`. 

Es necesario pasar `typeof()` enum como parámetro al método `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Y devuelve valores de enum de tipo `System.Array` y además podemos utilizar `foreach` declaración de bucle a través de la C # enum.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Si desea `IEnumerable` resultado, podemos lanzar más el método `Enum.GetValues()`.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## Usando `C# Enum.GetNames()` para enumerar nombres de enum como cadenas 

`C# Enum.GetValues()` devuelve un array de tipos de enum. 

Por eso convertimos los valores enum a cadena antes de imprimirlos en la consola.

Usando el método `C# Enum.GetNames()` podemos enumerar nombres de enum como cadenas, por lo que no es necesario convertirlos a cadenas.

Si está utilizando `.Net 5` o superior, puede utilizar la función genérica `C# Enum.GetNames()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

En las versiones anteriores tenemos que pasar `typeof()` parámetro enum.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Así que si desea bucle nombres enum como cadenas podemos utilizar `C# Enum.GetNames()` método.

## Usando `Linq`

Podemos usar el método `Linq forEach` para enumerar enum C#, con la ayuda de los métodos `Enum.GetValues()` y `Enum.GetNames()`.

En `.Net 5` y superiores utilice el siguiente fragmento de código.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

En las versiones anteriores

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Resumen

En este tutorial hemos aprendido a recorrer un enum en C# utilizando los métodos `Enum.GetValues()` y `Enum.GetNames()`.










