---
title: " 3 rôzne spôsoby zacyklenia zoznamu C#"
description: "Rôzne spôsoby zacyklenia zoznamu C# s príkladmi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` sú jednou z najpoužívanejších dátových štruktúr v jazyku C#. 

Iterovanie nad `List<T>` a vykonávanie niektorých operácií nad prvkami zoznamu sú v našich každodenných projektoch pomerne bežné.

Na cyklovanie cez zoznam v jazyku C# môžeme použiť 3 rôzne spôsoby.

1. Pomocou príkazu C# `foreach`.
2. Pomocou metódy C# `List.ForEach`.
3. Použitie jednoduchého cyklu for.

Prejdime si príklad, aby sme ho lepšie pochopili. 

Najprv vytvoríme jednoduchý zoznam v jazyku C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Teraz si ukážeme rôzne spôsoby, ako vytvoriť cyklus v zozname C#.

## Použitie príkazu C# `foreach` 

Použitie príkazu `foreach` na zacyklenie zoznamu v jazyku C# je široko používaná metóda.

A ďalej môžeme nad prvkami zoznamu vykonávať ľubovoľné operácie.

V nasledujúcom príklade som vytvoril zoznam reťazcov.

Potom tento zoznam zacyklím pomocou `foreach` a ďalej vypíšem prvky zoznamu na konzolu.

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

Teraz vytvoríme zoznam objektov a zacyklíme ho pomocou príkazu `foreach`.

Definovali sme triedu `Person` a vytvorili zoznam s dvoma prvkami osôb.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Teraz môžeme použiť príkaz `foreach` na prechádzanie zoznamu objektov.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Použitie metódy C# `List.ForEach` 

`List<T>.ForEach` metóda vykoná zadaný `action` na každom prvku zoznamu.

Prijíma `Action<T>` parameter delegáta. 

Nasledujúci príklad prechádza zoznam objektov v slučke pomocou `Action<T>` delegáta.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Použitie príkazu `for` 

Ak chceme vykonať nejakú akciu s prvkami zoznamu na základe indexu, môžeme na prechádzanie zoznamu v jazyku C# použiť starší príkaz `for`. 

V opačnom prípade zostaňte pri `foreach` alebo `List<T>.ForEach()` metódami.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Zhrnutie

V tomto učebnom texte sme sa naučili, ako v jazyku C# prechádzať cyklom cez zoznam pomocou príkazov `foreach`, `List<T.ForEach` a `for`.










