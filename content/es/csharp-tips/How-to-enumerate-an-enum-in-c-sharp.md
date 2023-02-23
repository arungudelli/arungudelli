---
title: "Cómo enumerar C# enum"
description: " Diferentes formas de enumerar C# enum con ejemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Los Enums son ampliamente utilizados en el lenguaje `C#`. 

Y hay 4 maneras de enumerate enum en `C#`. 

1. Usando `C# Enum.GetValues()` en .Net 5 y superiores.
2. Usando `C# Enum.GetValues()` en versiones anteriores de .Net.
3. Uso de `C# Enum.GetNames()` para enumerar nombres de enum como cadenas.
4. Utilización de `Linq`

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

La dirección `enum` representa diferentes tipos de niveles de registro.

Ahora veremos diferentes formas de enumerar el `C# enum`.

## Usando `C# Enum.GetValues()` Método genérico en .Net 5 y superiores

Si está utilizando la última versión de `.Net`, es decir, `.Net 5` y superiores puede utilizar la versión genérica para el método `Enum.GetValues` para enumerar el `C# enum`.

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

La nueva versión genérica de `Enum.GetValues` devuelve la matriz de valores enum. 

Y además podemos usar las sentencias `for` o `foreach` para listar los `C# enum` nombres. 

Como el array contiene el tipo `enum` necesitamos convertirlo a cadena usando el método `ToString()`.

## Usando `C# Enum.GetValues()` en versiones antiguas de .Net.

En las versiones anteriores de `.Net` no hay ningún método genérico disponible para el método `Enum.GetValues()`. 

Es necesario pasar `typeof()` enum como parámetro al método `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Y devuelve enum valores de tipo `System.Array` y además podemos utilizar `foreach` declaración de bucle a través de la `C# enum` nombres.

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

## Usando `C# Enum.GetNames()` para enumerar nombres enum como cadenas 

`C# Enum.GetValues()` devuelve una matriz de tipos enum. 

Por eso convertimos los nombres enum a cadena antes de imprimirlos en la consola.

Usando el método `C# Enum.GetNames()` podemos enumerar los nombres de enum como cadenas, por lo que no es necesario convertirlos a cadenas.

Si utiliza `.Net 5` y superiores, puede utilizar la función genérica `C# Enum.GetNames()`.

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

En las versiones anteriores tenemos que pasar `typeof()` enum parámetro.

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

Así que si quieres en enumerar nombres como cadenas podemos usar el método `C# Enum.GetNames()`.

## Utilizando `Linq`

Podemos utilizar el método `Linq forEach` para enumerar C# enum, con la ayuda de los métodos `Enum.GetValues()` y `Enum.GetNames()`.

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

En este tutorial hemos aprendido a enumerar enum en C# utilizando los métodos `Enum.GetValues()` y `Enum.GetNames()`.










