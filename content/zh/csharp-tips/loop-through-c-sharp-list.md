---
title: " 循环浏览C#列表的3种不同方式 循环浏览C#列表的不同方式及示例

"
description: ""
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---`List<T>`是C#语言中最常用的数据结构之一。 

遍历 `List<T>`并对列表元素进行一些操作，这在我们的日常项目中很常见。

在C#中，要循环浏览一个列表，我们可以使用3种不同的方法。

1.使用C#`foreach` 语句。
2.使用C#`List.ForEach` 方法。
3.使用简单的for循环。

让我们通过一个例子来进一步了解它。 

首先，我们将创建一个简单的C#列表。

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

现在我们将看到循环C#列表的不同方法。

## 使用C#`foreach` 语句

使用`foreach` 语句来循环一个C#列表是广泛使用的方法。

而且我们还可以对列表中的元素进行任何操作。

在下面的例子中，我创建了一个字符串的列表。

然后使用`foreach` 循环该列表，并进一步在控制台打印列表元素。

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

现在我们将创建一个对象的列表，并使用`foreach` 语句来循环它们。

定义了一个`Person` 类，并创建了一个有两个人元素的列表。

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

现在我们可以使用`foreach` 语句来循环浏览对象的列表。

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## 使用C#`List.ForEach` 方法

`List<T>.ForEach`方法对List的每个元素执行给定的`action` 。

它接受 `Action<T>`委托参数。 

下面的例子是通过使用 `Action<T>`委托。

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## 使用`for` 语句

如果你想根据索引对列表中的元素进行任何操作，我们可以使用传统的`for` 语句来循环浏览一个C#列表。 

否则请坚持使用`foreach` 或 `List<T>.ForEach()`方法。

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## 摘要

在本教程中，我们学习了如何使用`foreach`,`List<T.ForEach` 和`for` 语句在C#中循环浏览一个列表。










