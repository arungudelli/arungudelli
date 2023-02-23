---
title: " 3 různé způsoby zacyklení seznamu v jazyce C#"
description: "Různé způsoby zacyklení seznamu v jazyce C# s příklady"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` jsou jednou z nejpoužívanějších datových struktur v jazyce C#. 

Iterace nad `List<T>` a provádění některých operací nad prvky seznamu jsou v našich každodenních projektech zcela běžné.

K procházení seznamu v jazyce C# můžeme použít tři různé způsoby.

1. Pomocí příkazu C# `foreach`.
2. Pomocí metody C# `List.ForEach`.
3. Použití jednoduché smyčky for.

Projděme si příklad, abychom mu lépe porozuměli. 

Nejprve vytvoříme jednoduchý seznam v jazyce C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nyní si ukážeme různé způsoby, jak vytvořit smyčku v seznamu C#.

## Použití příkazu C# `foreach` 

Použití příkazu `foreach` k zacyklení seznamu v jazyce C# je široce používanou metodou.

A dále můžeme nad prvky seznamu provádět libovolné operace.

V následujícím příkladu jsem vytvořil seznam řetězců.

Poté jsem tento seznam zacyklil pomocí `foreach` a dále jsem prvky seznamu vypsal na konzoli.

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

Nyní vytvoříme seznam objektů a zacyklíme jej pomocí příkazu `foreach`.

Definovali jsme třídu `Person` a vytvořili seznam se dvěma prvky person.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nyní můžeme pomocí příkazu `foreach` procházet seznamem objektů.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Použití metody C# `List.ForEach` 

`List<T>.ForEach` metoda provede zadaný `action` na každém prvku Seznamu.

Přijímá `Action<T>` parametr delegát. 

Následující příklad prochází seznam objektů ve smyčce pomocí `Action<T>` delegáta.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Použití příkazu `for` 

Pokud chceme na základě indexu provést nějakou akci s prvky seznamu, můžeme k procházení seznamu v jazyce C# použít starší příkaz `for`. 

V opačném případě zůstaňte u `foreach` nebo `List<T>.ForEach()` metodami.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Shrnutí

V tomto tutoriálu jsme se naučili, jak v jazyce C# zacyklit seznam pomocí příkazů `foreach`, `List<T.ForEach` a `for`.










