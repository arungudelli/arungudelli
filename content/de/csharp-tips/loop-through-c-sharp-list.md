---
title: " 3 verschiedene Möglichkeiten, durch eine C#-Liste zu schleifen"
description: "Verschiedene Möglichkeiten, C#-Liste mit Beispielen zu schleifen"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` sind eine der am häufigsten verwendeten Datenstrukturen in der Sprache C#. 

Das Iterieren über die `List<T>` und die Durchführung einiger Operationen auf Listenelementen sind in unseren täglichen Projekten durchaus üblich.

Um durch eine Liste in C# Schleife können wir 3 verschiedene Möglichkeiten verwenden.

1. Mit C# `foreach` Anweisung.
2. Mit der C# `List.ForEach` Methode.
3. Verwendung einer einfachen for-Schleife.

Lassen Sie uns ein Beispiel durchgehen, um es besser zu verstehen. 

Zuerst werden wir eine einfache C#-Liste erstellen.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nun werden wir verschiedene Möglichkeiten sehen, eine C#-Liste in eine Schleife zu bringen.

## Mit C# `foreach` Anweisung

Die `foreach` -Anweisung ist eine weit verbreitete Methode, um eine C#-Liste in einer Schleife laufen zu lassen.

Außerdem können wir jede beliebige Operation an den Listenelementen durchführen.

In dem folgenden Beispiel habe ich eine Liste von Strings erstellt.

Dann wird diese Liste mit `foreach` in einer Schleife durchlaufen und die Listenelemente werden auf der Konsole ausgegeben.

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

Jetzt werden wir eine Liste von Objekten erstellen und sie mit der Anweisung `foreach` in einer Schleife durchlaufen.

Definieren Sie eine Klasse `Person` und erstellen Sie eine Liste mit zwei Personenelementen.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Jetzt können wir die Anweisung `foreach` verwenden, um eine Schleife durch die Liste der Objekte zu ziehen.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Verwendung der C#-Methode `List.ForEach` 

`List<T>.ForEach` methode führt die angegebene `action` für jedes Element der Liste aus.

Sie akzeptiert `Action<T>` delegat-Parameter. 

Das folgende Beispiel führt eine Schleife durch die Liste der Objekte mit `Action<T>` delegat.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Verwendung der Anweisung `for` 

Wir können die Legacy-Anweisung `for` verwenden, um eine C#-Liste in einer Schleife zu durchlaufen, wenn Sie eine beliebige Aktion auf den Listenelementen basierend auf dem Index durchführen möchten. 

Ansonsten bleiben Sie bei `foreach` oder `List<T>.ForEach()` methoden.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Zusammenfassung

In diesem Tutorial haben wir gelernt, wie man in C# mit den Anweisungen `foreach`, `List<T.ForEach` und `for` eine Liste in einer Schleife durchläuft.










