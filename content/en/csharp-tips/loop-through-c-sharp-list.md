---
title: "3 different ways to loop through a C# List"
description: "Different ways to loop C# list with examples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` are one of the most used data structure in C# language. 

Iterating over the `List<T>` and performing some operations on list elements are, quite common in our daily projects.

To loop through a list in C# we can use 3 different ways.

1. Using C# `foreach` statement.
2. Using C# `List.ForEach` method.
3. Using simple for loop.

Let's go through an example to understand it further. 

First we will create a simple C# list.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Now we will see different ways to loop a C# List.

## Using C# `foreach` statement

Using `foreach` statement to loop a C# list is widely used method.

And further we can perform any operation on the list elements.

In the below example I have created a list of strings.

Then looping that list using `foreach` and further printing the list elements on the console.

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

Now we will create a list of objects and loop them using `foreach` statement.

Defined a `Person` class and created a list with two person elements.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Now we can use `foreach` statement to loop through list of objects.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Using C# `List.ForEach` method

`List<T>.ForEach` method performs the given `action` on each element of the List.

It accepts `Action<T>` delegate parameter. 

The following example loop through the list of objects using `Action<T>` delegate.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Using `for` statement

We can use legacy `for` statement to loop through a C# list, if you want to perform any action on the list elements based on the index. 

Otherwise stick with `foreach` or `List<T>.ForEach()` methods.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Summary

In this tutorial we learnt, how to loop through a list in C# using `foreach`, `List<T.ForEach` and `for` statement.










