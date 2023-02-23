---
title: " 3 različni načini kroženja po seznamu C#"
description: "Različni načini kroženja po seznamu C# s primeri"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` so ena izmed najbolj uporabljenih podatkovnih struktur v jeziku C#. 

Iteriranje nad `List<T>` in izvajanje nekaterih operacij na elementih seznama sta precej pogosta v naših vsakodnevnih projektih.

Za kroženje po seznamu v jeziku C# lahko uporabimo tri različne načine.

1. Z uporabo stavka C# `foreach`.
2. Uporaba metode C# `List.ForEach`.
3. Uporaba preproste zanke for.

Za boljše razumevanje si oglejmo primer. 

Najprej bomo ustvarili preprost seznam v jeziku C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Sedaj bomo videli različne načine kroženja po zanki v seznamu C#.

## Uporaba izjave C# `foreach` 

Uporaba stavka `foreach` za ustvarjanje zanke v seznamu C# je pogosto uporabljena metoda.

Poleg tega lahko na elementih seznama izvajamo poljubne operacije.

V spodnjem primeru sem ustvaril seznam nizov.

Nato sem ta seznam zacikliral z uporabo `foreach` in elemente seznama natisnil na konzolo.

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

Zdaj bomo ustvarili seznam predmetov in jih zaciklirali z uporabo izjave `foreach`.

Definirali smo razred `Person` in ustvarili seznam z dvema elementoma oseb.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Zdaj lahko uporabimo izjavo `foreach` za kroženje po seznamu predmetov.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Uporaba metode C# `List.ForEach` 

`List<T>.ForEach` metoda izvede dan `action` na vsakem elementu seznama.

Sprejme `Action<T>` parameter delegata. 

V naslednjem zgledu je zazankanje po seznamu predmetov z uporabo `Action<T>` delegata.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Uporaba izjave `for` 

Če želite na podlagi indeksa izvesti kakršno koli akcijo na elementih seznama, lahko za kroženje po seznamu v jeziku C# uporabimo starejši stavek `for`. 

V nasprotnem primeru se držite `foreach` ali `List<T>.ForEach()` metodami.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Povzetek

V tem učbeniku smo se naučili, kako v jeziku C# z uporabo stavkov `foreach`, `List<T.ForEach` in `for` narediti zanko skozi seznam.










