---
title: " 3 különböző módja a C# listán való ciklusozásnak"
description: "C# lista ciklusozásának különböző módjai példákkal"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` a C# nyelv egyik leggyakrabban használt adatszerkezete. 

A listán való ismétlés `List<T>` és bizonyos műveletek végrehajtása a lista elemein, elég gyakori a mindennapi projektjeinkben.

A listán való végighaladáshoz a C# nyelvben 3 különböző módszert használhatunk.

1. A C# `foreach` utasítás használatával.
2. C# `List.ForEach` módszerrel.
3. Egyszerű for ciklus használata.

Nézzünk végig egy példát, hogy jobban megértsük. 

Először is létrehozunk egy egyszerű C# listát.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Most megnézzük a C# lista hurkolásának különböző módjait.

## A C# `foreach` utasítás használata

A `foreach` utasítás használata egy C# lista ciklusba hurkolásához széles körben használt módszer.

A továbbiakban pedig bármilyen műveletet elvégezhetünk a lista elemein.

Az alábbi példában egy stringekből álló listát hoztam létre.

Ezután a listát a `foreach` segítségével végigfutattam, majd a lista elemeit a konzolon kiírtam.

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

Most létrehozunk egy objektumokból álló listát, és a `foreach` utasítás segítségével hurkot készítünk belőlük.

Definiáltunk egy `Person` osztályt, és létrehoztunk egy listát két személy elemmel.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Most a `foreach` utasítással végighaladhatunk az objektumok listáján.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## A C# `List.ForEach` módszer használata

`List<T>.ForEach` metódus a List minden egyes elemén végrehajtja a megadott `action` értéket.

Elfogadja `Action<T>` delegate paramétert. 

A következő példa az objektumok listáján való végighaladásra használja a `Action<T>` delegate.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## A `for` utasítás használata

Az örökölt `for` utasítást használhatjuk egy C# listán való végighaladásra, ha az index alapján bármilyen műveletet szeretnénk végrehajtani a lista elemein. 

Egyébként maradjunk a `foreach` vagy a `List<T>.ForEach()` módszerekhez.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Összefoglaló

Ebben a bemutatóban megtanultuk, hogyan lehet egy listán végighaladni C# nyelven a `foreach`, `List<T.ForEach` és `for` utasítás segítségével.










