+++
title="8 formas de iterar sobre pares de valores clave de diccionario en C#"
summary="Utilizar el bucle foreach de C# es la forma más sencilla y directa de iterar sobre los valores clave del diccionario en C#."
keywords=["bucle diccionario en C#, iterar diccionario c#, bucle claves diccionario, bucle valores diccionario"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[imagen]
focal_point=''
preview_only=false
+++

Para iterar los pares clave-valor del diccionario en C# utilice los siguientes métodos

1. Usando el bucle de C# `foreach` 
2. Iterar sólo sobre las claves del diccionario de C#
3. Iterar sólo sobre los valores del diccionario de C#
4. Usando `Deconstruct` de `KeyValuePair<TKey,TValue>` en C# 7
5. Uso de `Deconstruct` y `discards` en C# 7 
6. `Deconstruct` del par clave-valor en versiones antiguas de C#
7. Utilizando la función `dictionary.ElementAt()` y el bucle `for` 
8. Usando C# `dictionary.AsParallel().ForAll()` 

Veamos un ejemplo para entenderlo mejor 

He creado un diccionario de ejemplo usando `C#` for loop

Echa un vistazo al siguiente diccionario `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Solución 1: Utilizar el bucle `C# foreach` 

El uso del bucle `C# foreach` es la forma más sencilla y directa de iterar sobre los valores de las claves del diccionario en C#.

```
foreach (var dictionary in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", dictionary.Key, dictionary.Value);
}

//OUTPUT

dictionary key is key1 and value is value1
dictionary key is key2 and value is value2
dictionary key is key3 and value is value3
dictionary key is key4 and value is value4
dictionary key is key5 and value is value5
```

La variable `dictionary` en el bucle anterior `foreach` tendrá `KeyValuePair<TKey, TValue>` tipo 

Podemos acceder fácilmente a las propiedades `Key` y `Value` del tipo `KeyValuePair`.

## Solución 2: Iterar sólo sobre las claves del diccionario C#

Si quieres hacer un bucle sólo sobre las claves del diccionario utiliza la propiedad del diccionario de C# `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Solución 3: Iterar sólo sobre los valores del diccionario C#

Si quiere iterar sólo sobre los valores del diccionario utilice la propiedad del diccionario C# `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Solución 4: Usando `Deconstruct()` de `KeyValuePair<TKey,TValue>` en C# 7

Los deconstructores se introducen en la versión C# 7.0.
 
Y si estás usando la aplicación .NET Core 2.0+ el tipo `KeyValuePair<TKey, TValue>` tendrá el método `Deconstruct()`.

```
public readonly struct KeyValuePair<TKey, TValue>
{
        private readonly TKey key;

        private readonly TValue value;

        private readonly int _dummyPrimitive;

        public TKey Key
        {
            get
            {
                throw null;
            }
        }

        public TValue Value
        {
            get
            {
                throw null;
            }
        }

        public KeyValuePair(TKey key, TValue value)
        {
            throw null;
        }

        [EditorBrowsable(EditorBrowsableState.Never)]
        public void Deconstruct(out TKey key, out TValue value)
        {
            throw null;
        }

        public override string ToString()
        {
            throw null;
        }
}
```

Para acceder al par clave-valor del diccionario utilice la función `Deconstruct()` del tipo `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Solución 5: Uso de `Deconstruct` y `discards` en C# 7 

A partir de C# 7.0, C# soporta descartes 

Los descartes son variables de marcador de posición que no se utilizan intencionadamente en el código de la aplicación 

A menudo se conocen como variables de guión bajo `_`.

Los descartes no son más que las variables no asignadas, no tienen un valor.

En el diccionario si se quiere hacer un bucle sólo de Claves, podemos hacer uso de las variables de descarte.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Del mismo modo si se quiere utilizar sólo los valores del diccionario.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Solución 6: `Deconstruct` de par clave-valor en versiones antiguas de C#


La estructura KeyValuePair no tiene la función `Deconstruct()` en versiones antiguas de C#.(C# 4.7.2 abajo) 

Así que si quieres usar `Deconstruct()` para hacer un bucle de pares clave-valor hay una solución 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

En la mayoría de los casos no usaremos este método, pero es bueno saberlo.

## Solución 7: Usando la función `dictionary.ElementAt()` y el bucle `for` 

Podemos utilizar el simple bucle `for` para iterar sobre los pares clave-valor del diccionario.

Podemos acceder a los valores de `KeyValuePair` por el índice del diccionario utilizando la función `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

De nuevo no es una buena manera de hacer un bucle a través del diccionario, porque la función `ElementAt()` tendrá `O(n)` y nosotros tenemos el bucle `for` arriba por lo que la complejidad de tiempo será `O(n^2)` 

En diccionarios grandes tendrá implicaciones de rendimiento.

Si quieres obtener el índice de los pares clave-valor del diccionario utiliza este método 

No se me ocurre ningún caso de uso en el mundo real en el que se utilice el índice del diccionario 

## Solución 8: Usando C# `dictionary.AsParallel().ForAll()`

Si tenemos un diccionario grande, podemos hacer uso de la consulta integrada en lenguaje paralelo (LINQ) utilizando el método de extensión `ParallelEnumerable.AsParallel` en el diccionario y ejecutando la consulta mediante el método `ParallelEnumerable.ForAll`.

La consulta particiona el origen en tareas que se ejecutan de forma asíncrona en múltiples hilos

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## La mejor manera de hacer un bucle en el diccionario en C# 

Aunque tenemos múltiples formas de iterar sobre los valores de las claves de un diccionario, preferimos usar un simple bucle foreach 

Y si quieres hacer un bucle sólo con las claves o valores del diccionario de C# utiliza `dictionary.Keys` o `dictionary.Values` en lugar de iterar todo el diccionario 







