---
title: " 3 erinevat viisi C# loendi läbimiseks"
description: "Erinevad viisid C# loendi läbimiseks koos näidetega"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` on üks enim kasutatavaid andmestruktuure C# keeles. 

Iteratsioon üle `List<T>` ja mõningate operatsioonide teostamine loendi elementidega on meie igapäevastes projektides üsna tavaline.

Loendi läbimiseks C# keeles saame kasutada 3 erinevat võimalust.

1. Kasutades C# `foreach` avaldust.
2. Kasutades C# `List.ForEach` meetodit.
3. Kasutades lihtsat for-tsüklit.

Vaatame läbi näite, et seda paremini mõista. 

Kõigepealt loome lihtsa C# loendi.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nüüd näeme erinevaid võimalusi C# loendi loopimiseks.

## Kasutades C# `foreach` avaldust

Kasutades `foreach` avaldust C# loendi loopimiseks on laialdaselt kasutatav meetod.

Ja edasi saame teha mis tahes operatsiooni loendi elementidega.

Alljärgnevas näites olen loonud stringide loendi.

Seejärel loopimine selle loendi abil `foreach` ja seejärel loendi elementide printimine konsooli.

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

Nüüd loome objektide loendi ja loopime neid kasutades `foreach` avaldust.

Määratlesime klassi `Person` ja lõime nimekirja kahe isiku elemendiga.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nüüd saame kasutada `foreach` avaldust, et loopida läbi objektide loendi.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Kasutades C# `List.ForEach` meetodit

`List<T>.ForEach` meetod teostab antud `action` igale elemendile Listis.

See võtab vastu `Action<T>` delegate parameetri. 

Järgnev näide teeb looopi läbi objektide loendi, kasutades `Action<T>` delegate.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Kasutades `for` avaldust

Me võime kasutada pärimusavaldust `for` C# loendi läbimiseks, kui soovite teha loendi elementidega mis tahes toiminguid indeksi alusel. 

Muul juhul jääb `foreach` või `List<T>.ForEach()` meetodite juurde.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Kokkuvõte

Selles õpiobjektis õppisime, kuidas loendist läbi käia C# keeles, kasutades `foreach`, `List<T.ForEach` ja `for` avaldust.










