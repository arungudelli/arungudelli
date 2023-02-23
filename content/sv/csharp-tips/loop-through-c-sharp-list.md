---
title: " 3 olika sätt att slinga genom en C#-lista"
description: "Olika sätt att slinga genom en C#-lista med exempel"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` är en av de mest använda datastrukturerna i C#-språket. 

Att iterera över `List<T>` och utföra vissa operationer på listelement är ganska vanligt i våra dagliga projekt.

För att loopa genom en lista i C# kan vi använda tre olika sätt.

1. Genom att använda C# `foreach`.
2. Med hjälp av C# `List.ForEach` -metoden.
3. Användning av en enkel for-slinga.

Låt oss gå igenom ett exempel för att förstå det bättre. 

Först skapar vi en enkel C#-lista.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nu kommer vi att se olika sätt att slinga en C#-lista.

## Med hjälp av C# `foreach` 

Att använda `foreach` -angivelsen för att slinga en C#-lista är en mycket använd metod.

Dessutom kan vi utföra vilken operation som helst på listelementen.

I exemplet nedan har jag skapat en lista med strängar.

Sedan loopar jag listan med hjälp av `foreach` och skriver ut listelementen på konsolen.

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

Nu ska vi skapa en lista med objekt och slinga dem med hjälp av `foreach`.

Vi definierade en klass `Person` och skapade en lista med två personelement.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nu kan vi använda `foreach` -anvisningen för att gå igenom en lista med objekt.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Använda C# `List.ForEach` -metoden

`List<T>.ForEach` metoden `action` utför den angivna åtgärden på varje element i listan.

Den accepterar `Action<T>` en delegatparameter. 

Följande exempel visar en loop genom listan med objekt med hjälp av `Action<T>` delegat.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Användning av `for` 

Vi kan använda det gamla uttalandet `for` för att slinga oss igenom en C#-lista om du vill utföra någon åtgärd på listelementen baserat på indexet. 

Annars kan du använda `foreach` eller `List<T>.ForEach()` metoder.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Sammanfattning

I den här handledningen lärde vi oss hur man loopar genom en lista i C# med hjälp av `foreach`, `List<T.ForEach` och `for`.










