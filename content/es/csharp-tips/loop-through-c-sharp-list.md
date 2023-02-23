---
title: " 3 maneras diferentes de recorrer una lista en C#"
description: "Diferentes maneras de recorrer una lista en C# con ejemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` son una de las estructuras de datos más utilizadas en el lenguaje C#. 

Iterar sobre la `List<T>` y realizar algunas operaciones sobre los elementos de la lista son, bastante comunes en nuestros proyectos diarios.

Para recorrer una lista en C# podemos utilizar 3 formas diferentes.

1. Usando la sentencia C# `foreach`.
2. Usando el método C# `List.ForEach`.
3. Usando un simple bucle for.

Veamos un ejemplo para entenderlo mejor. 

Primero crearemos una lista simple en C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Ahora vamos a ver diferentes maneras de bucle de una lista de C #.

## Usando la sentencia C# `foreach` 

Usar la sentencia `foreach` para hacer un bucle en una lista de C# es un método ampliamente utilizado.

Y además podemos realizar cualquier operación sobre los elementos de la lista.

En el siguiente ejemplo he creado una lista de cadenas.

A continuación, un bucle que la lista utilizando `foreach` y además la impresión de los elementos de la lista en la consola.

```csharp
///Method to Loop C# list
void loopList()
{
   List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};
   
   foreach (string lang in languages)
   {
        Console.WriteLine(lang);
   }
}
```

Ahora vamos a crear una lista de objetos y un bucle utilizando `foreach` declaración.

Definimos una clase `Person` y creamos una lista con dos elementos persona.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Ahora podemos utilizar la sentencia `foreach` para recorrer la lista de objetos.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Usando el método C# `List.ForEach` 

`List<T>.ForEach` realiza la operación `action` en cada elemento de la lista.

Acepta el parámetro `Action<T>` parámetro delegado. 

El siguiente ejemplo recorre la lista de objetos utilizando `Action<T>` delegado.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Utilizando la sentencia `for` 

Podemos utilizar la sentencia `for` para recorrer una lista en C#, si queremos realizar alguna acción sobre los elementos de la lista basándonos en el índice. 

En caso contrario, utilice `foreach` o los métodos `List<T>.ForEach()` métodos.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Resumen

En este tutorial hemos aprendido cómo recorrer una lista en C# utilizando las sentencias `foreach`, `List<T.ForEach` y `for`.










