---
title: " 3 modi diversi per eseguire il loop di una lista in C#"
description: "Diversi modi per eseguire il loop di una lista in C# con esempi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` sono una delle strutture dati più utilizzate nel linguaggio C#. 

L'iterazione su un elenco `List<T>` ed eseguire alcune operazioni sugli elementi dell'elenco sono abbastanza comuni nei nostri progetti quotidiani.

Per eseguire un ciclo su un elenco in C# possiamo utilizzare 3 modi diversi.

1. Utilizzando l'istruzione C# `foreach`.
2. Utilizzando il metodo C# `List.ForEach`.
3. Utilizzo di un semplice ciclo for.

Vediamo un esempio per capire meglio. 

Per prima cosa creeremo un semplice elenco in C#.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Ora vedremo diversi modi per eseguire il loop di un elenco in C#.

## Utilizzando l'istruzione C# `foreach` 

L'uso dell'istruzione `foreach` per eseguire il loop di un elenco in C# è un metodo molto utilizzato.

Inoltre, è possibile eseguire qualsiasi operazione sugli elementi dell'elenco.

Nell'esempio seguente ho creato un elenco di stringhe.

Quindi ho eseguito un ciclo su tale elenco utilizzando `foreach` e stampando gli elementi dell'elenco sulla console.

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

Ora creeremo un elenco di oggetti e li metteremo in loop utilizzando l'istruzione `foreach`.

Abbiamo definito una classe `Person` e creato un elenco con due elementi persona.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Ora possiamo usare l'istruzione `foreach` per scorrere l'elenco di oggetti.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Utilizzando il metodo C# `List.ForEach` 

`List<T>.ForEach` esegue il metodo `action` su ciascun elemento della lista.

Accetta `Action<T>` un parametro delegato. 

L'esempio seguente scorre l'elenco di oggetti utilizzando il metodo `Action<T>` delegato.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Utilizzando l'istruzione `for` 

È possibile utilizzare l'istruzione legacy `for` per eseguire il loop di un elenco in C#, se si desidera eseguire un'azione sugli elementi dell'elenco in base all'indice. 

Altrimenti, utilizzare i metodi `foreach` o `List<T>.ForEach()` metodi.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Riepilogo

In questo tutorial abbiamo imparato come eseguire il loop di una lista in C# utilizzando le istruzioni `foreach`, `List<T.ForEach` e `for`.










