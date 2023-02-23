---
title: " 3 различни начина за зацикляне на списък на C#"
description: "Различни начини за зацикляне на списък на C# с примери"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` са една от най-използваните структури от данни в езика C#. 

Итерирането над `List<T>` и извършването на някои операции върху елементите на списъка са доста често срещани в ежедневните ни проекти.

За да преминем през списък в C#, можем да използваме три различни начина.

1. Използване на оператора C# `foreach`.
2. Използване на метода C# `List.ForEach`.
3. Използване на прост цикъл for.

Нека разгледаме един пример, за да го разберем по-добре. 

Първо ще създадем прост списък на C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Сега ще видим различни начини за създаване на цикъл в списък на C#.

## Използване на оператора C# `foreach` 

Използването на декларацията `foreach` за циклиране на C# списък е широко използван метод.

Освен това можем да извършваме всякакви операции върху елементите на списъка.

В примера по-долу съм създал списък от низове.

След това зациклих този списък, използвайки `foreach`, и отпечатвам елементите на списъка на конзолата.

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

Сега ще създадем списък от обекти и ще ги зациклим, като използваме оператора `foreach`.

Дефинирахме клас `Person` и създадохме списък с два елемента на човек.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Сега можем да използваме оператора `foreach`, за да прегледаме списъка с обекти.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Използване на метода C# `List.ForEach` 

`List<T>.ForEach` методът изпълнява зададеното `action` върху всеки елемент от списъка.

Той приема `Action<T>` делегатски параметър. 

Следващият пример извършва цикъл през списъка от обекти, като използва `Action<T>` делегат.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Използване на изявление `for` 

Можем да използваме наследения оператор `for`, за да направим цикъл в списък на C#, ако искаме да извършим някакво действие върху елементите на списъка въз основа на индекса. 

В противен случай се придържайте към `foreach` или `List<T>.ForEach()` методи.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Резюме

В този урок научихме как да извършим цикъл в списък на C#, като използваме инструкциите `foreach`, `List<T.ForEach` и `for`.










