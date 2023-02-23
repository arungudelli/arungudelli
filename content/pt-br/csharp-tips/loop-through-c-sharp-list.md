---
title: " 3 maneiras diferentes de fazer loop através de uma lista C#"
description: "maneiras diferentes de fazer loop através de uma lista C# com exemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` são uma das estruturas de dados mais utilizadas na linguagem C#. 

Iterating over the `List<T>` e realizar algumas operações em elementos de lista são, bastante comuns em nossos projetos diários.

Para percorrer uma lista em C#, podemos usar 3 maneiras diferentes.

1. Usando a declaração C# `foreach`.
2. Usando o método C# `List.ForEach`.
3. Usando simples para loop.

Vamos passar por um exemplo para entendê-lo melhor. 

Primeiro vamos criar uma lista C# simples.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Agora veremos diferentes maneiras de fazer loop em uma lista C#.

## Usando a declaração C# `foreach` 

O uso da declaração `foreach` para fazer o loop de uma lista C# é um método amplamente utilizado.

E além disso, podemos realizar qualquer operação dos elementos da lista.

No exemplo abaixo, eu criei uma lista de cordas.

Em seguida, fazer o looping dessa lista usando `foreach` e imprimir ainda mais os elementos da lista no console.

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

Agora, criaremos uma lista de objetos e os faremos circular usando a declaração `foreach`.

Definiu uma classe `Person` e criou uma lista com dois elementos pessoais.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Agora podemos usar a declaração `foreach` para fazer um loop através da lista de objetos.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Usando o método C# `List.ForEach` 

`List<T>.ForEach` realiza o método dado em `action` em cada elemento da Lista.

Ele aceita `Action<T>` parâmetro do delegado. 

O seguinte exemplo de loop através da lista de objetos usando `Action<T>` delegada.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Usando a declaração `for` 

Podemos usar o legado `for` para fazer um loop através de uma lista C#, se você quiser realizar qualquer ação nos elementos da lista com base no índice. 

Caso contrário, fique com `foreach` ou `List<T>.ForEach()` métodos.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Sumário

Neste tutorial aprendemos, como fazer loop através de uma lista em C# usando `foreach`, `List<T.ForEach` e `for` declaração.










