---
title: " 3 moduri diferite de a face buclă printr-o listă C#"
description: "Diferite moduri de a face buclă în lista C# cu exemple"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` sunt una dintre cele mai utilizate structuri de date în limbajul C#. 

Iterarea peste `List<T>` și efectuarea unor operații asupra elementelor listei sunt, destul de frecvente în proiectele noastre zilnice.

Pentru a parcurge în buclă o listă în C# putem utiliza 3 moduri diferite.

1. Folosind declarația C# `foreach`.
2. Folosind metoda C# `List.ForEach`.
3. Utilizarea unei bucle for simple.

Să parcurgem un exemplu pentru a înțelege mai bine. 

Mai întâi vom crea o listă simplă în C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Acum vom vedea diferite moduri de a crea bucle într-o listă C#.

## Utilizarea declarației C# `foreach` 

Utilizarea instrucțiunii `foreach` pentru a face o buclă într-o listă C# este o metodă utilizată pe scară largă.

Și mai departe putem efectua orice operație asupra elementelor listei.

În exemplul de mai jos am creat o listă de șiruri de caractere.

Apoi am rulat lista în buclă folosind `foreach` și apoi am imprimat elementele listei pe consolă.

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

Acum vom crea o listă de obiecte și le vom pune în buclă folosind instrucțiunea `foreach`.

Am definit o clasă `Person` și am creat o listă cu două elemente persoană.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Acum putem utiliza instrucțiunea `foreach` pentru a parcurge în buclă lista de obiecte.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Utilizarea metodei C# `List.ForEach` 

`List<T>.ForEach` execută metoda `action` dată pentru fiecare element al listei.

Metoda acceptă `Action<T>` un parametru delegat. 

Exemplul următor parcurge în buclă lista de obiecte folosind `Action<T>` delegat.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Utilizarea declarației `for` 

Putem utiliza instrucțiunea legacy `for` pentru a parcurge în buclă o listă C#, dacă doriți să efectuați orice acțiune asupra elementelor listei pe baza indicelui. 

În caz contrar, rămâneți la `foreach` sau `List<T>.ForEach()` metode.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Rezumat

În acest tutorial am învățat cum să facem o buclă printr-o listă în C# folosind declarațiile `foreach`, `List<T.ForEach` și `for`.










