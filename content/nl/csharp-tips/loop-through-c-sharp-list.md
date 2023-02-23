---
title: " 3 verschillende manieren om door een C# lijst te lussen"
description: "Verschillende manieren om een C# lijst te lussen met voorbeelden"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` zijn een van de meest gebruikte datastructuren in de C# taal. 

Itereren over de `List<T>` en het uitvoeren van enkele operaties op lijstelementen zijn heel gewoon in onze dagelijkse projecten.

Om door een lijst te lussen in C# kunnen we 3 verschillende manieren gebruiken.

1. Met behulp van C# `foreach` statement.
2. C# `List.ForEach` methode gebruiken.
3. Eenvoudige for-lus gebruiken.

Laten we een voorbeeld bekijken om het verder te begrijpen. 

Eerst maken we een eenvoudige C# lijst.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nu zullen we verschillende manieren zien om een C# lijst te lussen.

## C# `foreach` statement gebruiken

Het gebruik van `foreach` statement om een C# lijst te lussen is een veelgebruikte methode.

En verder kunnen we elke bewerking op de lijstelementen uitvoeren.

In het onderstaande voorbeeld heb ik een lijst van strings gemaakt.

Vervolgens loop ik die lijst met `foreach` en druk ik de lijstelementen af op de console.

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

Nu zullen we een lijst van objecten maken en ze doorlussen met behulp van `foreach` statement.

We definiëren een klasse `Person` en maken een lijst met twee persoonselementen.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nu kunnen we het `foreach` statement gebruiken om door de lijst van objecten te lussen.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## C# `List.ForEach` methode gebruiken

`List<T>.ForEach` voert de methode `action` de opgegeven uit op elk element van de Lijst.

Het accepteert `Action<T>` gedelegeerde parameter. 

Het volgende voorbeeld doorloopt de lijst van objecten met behulp van `Action<T>` delegeren.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Met behulp van `for` verklaring

We kunnen het statement `for` gebruiken om door een C#-lijst te lussen, als u een actie wilt uitvoeren op de lijstelementen op basis van de index. 

Gebruik anders `foreach` of `List<T>.ForEach()` methoden.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Samenvatting

In deze tutorial hebben we geleerd hoe we in C# door een lijst kunnen lopen met behulp van `foreach`, `List<T.ForEach` en `for`.










