---
title: " 3 forskellige måder at gennemløbe en C#-liste på"
description: "Forskellige måder at gennemløbe en C#-liste på med eksempler"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` er en af de mest anvendte datastrukturer i C#-sproget. 

Iteration over den `List<T>` og udføre nogle operationer på listeelementer er ret almindelige i vores daglige projekter.

For at gennemløbe en liste i C# kan vi bruge 3 forskellige måder.

1. Brug af C# `foreach` statement.
2. Ved hjælp af C# `List.ForEach` metoden.
3. Brug af simpel for loop.

Lad os gennemgå et eksempel for at forstå det yderligere. 

Først vil vi oprette en simpel C#-liste.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nu vil vi se forskellige måder at lave en C#-liste som loop på.

## Brug af C# `foreach` statement

Brug af `foreach` -erklæringen til at loop en C#-liste er en meget anvendt metode.

Desuden kan vi udføre enhver operation på listeelementerne.

I nedenstående eksempel har jeg oprettet en liste med strenge.

Derefter sløjfes denne liste ved hjælp af `foreach` og derefter udskrives listeelementerne på konsollen.

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

Nu vil vi oprette en liste over objekter og lave en løkke af dem ved hjælp af `foreach`.

Definerede en `Person` klasse og oprettede en liste med to personelementer.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nu kan vi bruge `foreach` -erklæringen til at gennemløbe listen over objekter.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Brug af C# `List.ForEach` -metoden

`List<T>.ForEach` metode udfører den angivne `action` på hvert element i listen.

Den accepterer `Action<T>` en delegeret parameter. 

Følgende eksempel gennemløber listen af objekter ved hjælp af `Action<T>` delegat.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Brug af `for` -erklæringen

Vi kan bruge den gamle `for` -erklæring til at gennemløbe en C#-liste, hvis du ønsker at udføre en handling på listeelementerne baseret på indekset. 

Ellers skal du holde dig til `foreach` eller `List<T>.ForEach()` metoder.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Resumé

I denne tutorial lærte vi, hvordan man gennemløber en liste i C# ved hjælp af `foreach`, `List<T.ForEach` og `for` statement.










