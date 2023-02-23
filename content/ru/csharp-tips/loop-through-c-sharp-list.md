---
title: " 3 различных способа циклического просмотра списка на C#"
description: "Различные способы циклического просмотра списка на C# с примерами"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` являются одной из наиболее используемых структур данных в языке C#. 

Итерация по списку `List<T>` и выполнение некоторых операций над элементами списка - довольно частое явление в наших повседневных проектах.

Чтобы выполнить цикл по списку в C#, мы можем использовать 3 различных способа.

1. С помощью оператора C# `foreach`.
2. Используя метод C# `List.ForEach`.
3. Использование простого цикла for.

Давайте рассмотрим пример для дальнейшего понимания. 

Сначала мы создадим простой список на языке C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Теперь мы рассмотрим различные способы зацикливания списка C#.

## Использование оператора C# `foreach` 

Использование оператора `foreach` для зацикливания списка в C# является широко распространенным методом.

В дальнейшем мы можем выполнять любые операции над элементами списка.

В приведенном ниже примере я создал список строк.

Затем зациклил этот список с помощью `foreach` и вывел элементы списка на консоль.

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

Теперь мы создадим список объектов и зациклим их с помощью оператора `foreach`.

Определили класс `Person` и создали список с двумя элементами person.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Теперь мы можем использовать оператор `foreach` для циклического просмотра списка объектов.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Используя метод C# `List.ForEach` 

`List<T>.ForEach` метод выполняет заданный `action` над каждым элементом списка List.

Он принимает `Action<T>` параметр делегата. 

В следующем примере выполняется цикл по списку объектов с использованием `Action<T>` делегата.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Использование оператора `for` 

Мы можем использовать унаследованный оператор `for` для циклического просмотра списка C#, если вы хотите выполнить какое-либо действие над элементами списка на основе индекса. 

В противном случае используйте `foreach` или `List<T>.ForEach()` методы.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Резюме

В этом уроке мы узнали, как выполнить цикл по списку в C#, используя операторы `foreach`, `List<T.ForEach` и `for`.










