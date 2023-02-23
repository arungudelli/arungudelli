---
title: " 3 façons différentes de boucler une liste C#"
description: "Différentes façons de boucler une liste C# avec des exemples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` sont l'une des structures de données les plus utilisées dans le langage C#. 

L'itération sur la liste `List<T>` et effectuer des opérations sur les éléments d'une liste sont des opérations assez courantes dans nos projets quotidiens.

Pour boucler une liste en C#, nous pouvons utiliser 3 méthodes différentes.

1. En utilisant l'instruction C# `foreach`.
2. En utilisant la méthode C# `List.ForEach`.
3. Utilisation d'une boucle for simple.

Prenons un exemple pour mieux comprendre. 

Tout d'abord, nous allons créer une simple liste C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Maintenant, nous allons voir différentes façons de boucler une liste C#.

## Utilisation de l'instruction C# `foreach` 

L'utilisation de l'instruction `foreach` pour boucler une liste C# est une méthode largement utilisée.

De plus, nous pouvons effectuer n'importe quelle opération sur les éléments de la liste.

Dans l'exemple ci-dessous, j'ai créé une liste de chaînes de caractères.

Puis j'ai bouclé cette liste en utilisant `foreach` et j'ai ensuite imprimé les éléments de la liste sur la console.

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

Nous allons maintenant créer une liste d'objets et les boucler en utilisant l'instruction `foreach`.

Nous avons défini une classe `Person` et créé une liste avec deux éléments de personne.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nous pouvons maintenant utiliser l'instruction `foreach` pour boucler la liste d'objets.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## En utilisant la méthode C# `List.ForEach` 

`List<T>.ForEach` exécute la méthode `action` donnée sur chaque élément de la liste.

Elle accepte `Action<T>` paramètre délégué. 

L'exemple suivant parcourt en boucle la liste d'objets à l'aide de la méthode `Action<T>` délégué.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Utilisation de l'instruction `for` 

Nous pouvons utiliser l'ancienne instruction `for` pour boucler une liste C#, si vous souhaitez effectuer une action sur les éléments de la liste en fonction de l'index. 

Sinon, restez-en à `foreach` ou aux méthodes `List<T>.ForEach()` méthodes.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Résumé

Dans ce tutoriel, nous avons appris à boucler une liste en C# à l'aide des instructions `foreach`, `List<T.ForEach` et `for`.










