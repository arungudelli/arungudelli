---
title: " C#のリストをループする3種類の方法 C#のリストをループする様々な方法（例付き

"
description: ""
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---`List<T>`は、C#言語で最も使用されるデータ構造の1つです。 

リストを繰り返し処理したり `List<T>`を繰り返し実行したり、リスト要素に対して何らかの操作を行うことは、日々のプロジェクトで非常によく行われます。

C#でリストをループ処理するには、3つの異なる方法を使用することができます。

1.C#の`foreach` ステートメントを使用します。
2.C#`List.ForEach` メソッドを使用する。
3.単純なforループを使用する。

例題でさらに理解を深めましょう。 

まず、簡単なC#のリストを作成します。

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

次に、C#のリストをループさせるさまざまな方法について説明します。

## C#の`foreach` ステートメントを使用する

C#のリストをループさせるために`foreach` ステートメントを使用する方法は、広く使用されている方法です。

さらに、リストの要素に対して任意の操作を行うことができます。

以下の例では、文字列のリストを作成しました。

そして、`foreach` を使ってそのリストをループさせ、さらにリストの要素をコンソールに出力しています。

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

今度は、オブジェクトのリストを作成し、`foreach` ステートメントを使用してループさせます。

`Person` クラスを定義し、2人の人物を要素とするリストを作成しました。

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

あとは、`foreach` ステートメントを使用して、オブジェクトのリストをループすることができます。

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## C#`List.ForEach` メソッドを使用する

`List<T>.ForEach`メソッドは、Listの各要素に対して、指定された`action` を実行します。

このメソッドには `Action<T>`デリゲートパラメータを受け取ります。 

次の例では、オブジェクトのリストに対して `Action<T>`を使ってループしています。

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## `for` ステートメントを使用する

C#のリストに対して、インデックスに基づく何らかのアクションを実行したい場合、レガシーな`for` ステートメントを使用してループさせることができます。 

そうでない場合は、`foreach` または `List<T>.ForEach()`メソッドを使います。

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## 概要

このチュートリアルでは、`foreach` 、`List<T.ForEach` 、`for` ステートメントを使用して、C# でリストをループする方法を学びました。










