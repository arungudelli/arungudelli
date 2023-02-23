---
title: " 3 dažādi veidi, kā veidot cilpas C# sarakstā"
description: "Dažādi veidi, kā veidot cilpas C# sarakstā ar piemēriem"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` ir viena no visbiežāk izmantotajām datu struktūrām C# valodā. 

Iterēšana pār `List<T>` un dažu darbību veikšana ar saraksta elementiem ir diezgan bieži sastopama mūsu ikdienas projektos.

Lai veiktu cilpu caur sarakstu C# valodā, varam izmantot 3 dažādus veidus.

1. Izmantojot C# `foreach` izteikumu.
2. Izmantojot C# `List.ForEach` metodi.
3. Izmantojot vienkāršu for cilpu.

Lai to labāk izprastu, aplūkosim piemēru. 

Vispirms izveidosim vienkāršu C# sarakstu.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Tagad mēs aplūkosim dažādus veidus, kā veidot cilpas C# sarakstā.

## Izmantojot C# `foreach` izteikumu

Izmantojot `foreach` izteikumu, lai veidotu cilpu C# sarakstā, ir plaši izmantota metode.

Tālāk mēs varam veikt jebkuru operāciju ar saraksta elementiem.

Zemāk dotajā piemērā es esmu izveidojis virkņu sarakstu.

Pēc tam izveidoju cilpu šajā sarakstā, izmantojot `foreach`, un tālāk izdrukāju saraksta elementus konsoles ekrānā.

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

Tagad mēs izveidosim objektu sarakstu un izveidosim to cilpu, izmantojot `foreach` paziņojumu.

Definējām klasi `Person` un izveidojām sarakstu ar diviem personas elementiem.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Tagad mēs varam izmantot `foreach` izteikumu, lai veiktu cilpu caur objektu sarakstu.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Izmantojot C# `List.ForEach` metodi

`List<T>.ForEach` metode izpilda doto `action` katram saraksta elementam.

Tā pieņem `Action<T>` deleģēto parametru. 

Tālāk dotajā piemērā cilpa caur objektu sarakstu, izmantojot `Action<T>` delegātu.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Izmantojot `for` paziņojumu

Mēs varam izmantot mantoto `for` izteikumu, lai veiktu cilpu caur C# sarakstu, ja vēlaties veikt kādu darbību ar saraksta elementiem, pamatojoties uz indeksu. 

Pretējā gadījumā izmantojiet `foreach` vai `List<T>.ForEach()` metodēm.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Kopsavilkums

Šajā pamācībā mēs uzzinājām, kā C# programmā izveidot cilpu sarakstā, izmantojot `foreach`, `List<T.ForEach` un `for` paziņojumu.










