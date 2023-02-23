---
title: " 3 formas diferentes de fazer um loop através de uma lista C#"
description: "Formas diferentes de fazer loop através de uma lista C# com exemplos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` são uma das estruturas de dados mais utilizadas na linguagem C#. 

Iterating over the `List<T>` e a realização de algumas operações sobre elementos da lista são, bastante comuns nos nossos projectos diários.

Para percorrer uma lista em C# podemos usar 3 maneiras diferentes.

1. Usando a declaração C# `foreach`.
2. Usando o método C# `List.ForEach`.
3. Usando simples para loop.

Passemos por um exemplo para o compreender melhor. 

Primeiro vamos criar uma lista C# simples.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Agora veremos diferentes formas de fazer o loop de uma lista C#.

## Usando a declaração C# `foreach` 

A utilização da declaração `foreach` para fazer o laço de uma lista C# é um método amplamente utilizado.

E além disso, podemos realizar qualquer operação dos elementos da lista.

No exemplo abaixo, criei uma lista de cordas.

Em seguida, fazer o looping dessa lista utilizando `foreach` e imprimir os elementos da lista na consola.

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

Agora, vamos criar uma lista de objectos e fazer um laço com eles usando a declaração `foreach`.

Definiu uma classe `Person` e criou uma lista com dois elementos pessoais.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Agora podemos usar a declaração `foreach` para percorrer a lista de objectos.

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

`List<T>.ForEach` executa o método dado em `action` em cada elemento da Lista.

Aceita `Action<T>` parâmetro do delegado. 

O seguinte exemplo de loop através da lista de objectos usando `Action<T>` delegar.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Usando a declaração `for` 

Podemos utilizar o legado `for` para percorrer uma lista C#, se quiser realizar qualquer acção sobre os elementos da lista com base no índice. 

Caso contrário, ficar com `foreach` ou `List<T>.ForEach()` métodos.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Resumo

Neste tutorial aprendemos, como percorrer uma lista em C# usando `foreach`, `List<T.ForEach` e `for` declaração.










