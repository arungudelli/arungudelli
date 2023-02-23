---
title: " 3 różne sposoby na zapętlenie listy w C#"
description: "Różne sposoby zapętlania listy w C# z przykładami"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` są jedną z najczęściej używanych struktur danych w języku C#. 

Iterowanie nad `List<T>` oraz wykonywanie pewnych operacji na elementach listy są, dość często spotykane w naszych codziennych projektach.

Aby zapętlić listę w C# możemy użyć 3 różnych sposobów.

1. Używając instrukcji C# `foreach`.
2. Używając metody C# `List.ForEach`.
3. Użycie prostej pętli for.

Przejdźmy przez przykład, aby zrozumieć to dalej. 

Najpierw stworzymy prostą listę w języku C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Teraz zobaczymy różne sposoby na zapętlenie listy w C#.

## Używając instrukcji C# `foreach` 

Użycie instrukcji `foreach` do zapętlenia listy w C# jest szeroko stosowaną metodą.

Ponadto możemy wykonywać dowolne operacje na elementach listy.

W poniższym przykładzie utworzyłem listę ciągów znaków.

Następnie zapętliłem tę listę używając `foreach` i dalej wypisałem elementy listy na konsoli.

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

Teraz stworzymy listę obiektów i zapętlimy ją używając instrukcji `foreach`.

Zdefiniowaliśmy klasę `Person` i stworzyliśmy listę z dwoma elementami osobowymi.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Teraz możemy użyć instrukcji `foreach` do zapętlenia listy obiektów.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Używając metody C# `List.ForEach` 

`List<T>.ForEach` metoda wykonuje podane `action` na każdym elemencie Listy.

Przyjmuje ona `Action<T>` parametr delegata. 

Poniższy przykład zapętla listę obiektów przy użyciu `Action<T>` delegata.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Użycie instrukcji `for` 

Możemy użyć legacy `for` statement do zapętlenia listy w C#, jeśli chcemy wykonać dowolną akcję na elementach listy na podstawie indeksu. 

W przeciwnym razie trzymaj się `foreach` lub `List<T>.ForEach()` metody.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Podsumowanie

W tym tutorialu dowiedzieliśmy się, jak zapętlić listę w C# używając instrukcji `foreach`, `List<T.ForEach` oraz `for`.










