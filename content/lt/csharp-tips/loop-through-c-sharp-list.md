---
title: " 3 skirtingi ciklo per C# sąrašą sudarymo būdai"
description: "Įvairūs ciklo sudarymo būdai C# sąraše su pavyzdžiais"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` yra viena iš dažniausiai naudojamų duomenų struktūrų C# kalboje. 

Iteravimas per `List<T>` ir atlikti tam tikras operacijas su sąrašo elementais yra gana dažni kasdieniai projektai.

Norėdami sudaryti ciklą per sąrašą C# kalba, galime naudoti 3 skirtingus būdus.

1. Naudodami C# `foreach` komandą.
2. Naudojant C# `List.ForEach` metodą.
3. Naudojant paprastą for ciklą.

Kad geriau suprastumėte, panagrinėkime pavyzdį. 

Pirmiausia sukursime paprastą C# sąrašą.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Dabar pamatysime įvairius C# sąrašo ciklo sudarymo būdus.

## Naudojant C# `foreach` teiginį

Naudojant `foreach` sakinį C# sąrašui cikluoti plačiai naudojamas metodas.

Be to, su sąrašo elementais galime atlikti bet kokią operaciją.

Toliau pateiktame pavyzdyje sukūriau eilučių sąrašą.

Po to šį sąrašą surašiau į ciklą naudodamas `foreach` ir toliau spausdinau sąrašo elementus konsolėje.

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

Dabar sukursime objektų sąrašą ir sudarysime jų ciklą naudodami `foreach` teiginį.

Apibrėžėme `Person` klasę ir sukūrėme sąrašą su dviem asmenimis elementais.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Dabar galime naudoti `foreach` komandą, norėdami cikliškai peržiūrėti objektų sąrašą.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Naudojant C# `List.ForEach` metodą

`List<T>.ForEach` metodas kiekvienam sąrašo elementui atlieka duotą `action` veiksmą.

Jis priima `Action<T>` delegato parametras. 

Toliau pateiktame pavyzdyje ciklas per objektų sąrašą naudojant `Action<T>` delegatą.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Naudojant `for` teiginį

Jei norite atlikti kokį nors veiksmą su sąrašo elementais pagal indeksą, galime naudoti senąjį `for` teiginį, kad per C# sąrašą būtų galima atlikti ciklą. 

Priešingu atveju naudokite `foreach` arba `List<T>.ForEach()` metodais.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Santrauka

Šioje pamokoje sužinojome, kaip C# kalba sudaryti ciklą per sąrašą, naudojant `foreach`, `List<T.ForEach` ir `for` teiginius.










