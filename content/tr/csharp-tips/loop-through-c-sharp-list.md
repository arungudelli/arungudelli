---
title: " bir C# Listesinde döngü yapmanın 3 farklı yolu"
description: "Örneklerle C# listesinde döngü yapmanın farklı yolları"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` c# dilinde en çok kullanılan veri yapılarından biridir. 

Üzerinde yineleme `List<T>` ve liste elemanları üzerinde bazı işlemler yapmak, günlük projelerimizde oldukça yaygındır.

C#'ta bir liste üzerinde döngü yapmak için 3 farklı yol kullanabiliriz.

1. C# `foreach` deyimini kullanma.
2. C# `List.ForEach` yöntemini kullanma.
3. Basit for döngüsü kullanarak.

Bunu daha iyi anlamak için bir örnek üzerinden gidelim. 

İlk olarak basit bir C# listesi oluşturacağız.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Şimdi bir C# Listesini döngüye sokmanın farklı yollarını göreceğiz.

## C# `foreach` deyimini kullanma

Bir C# listesini döngüye sokmak için `foreach` deyimini kullanmak yaygın olarak kullanılan bir yöntemdir.

Ve ayrıca liste elemanları üzerinde herhangi bir işlem gerçekleştirebiliriz.

Aşağıdaki örnekte dizelerden oluşan bir liste oluşturdum.

Daha sonra bu listeyi `foreach` kullanarak döngüye sokun ve liste öğelerini konsola yazdırın.

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

Şimdi bir nesne listesi oluşturacağız ve `foreach` deyimini kullanarak bunları döngüye sokacağız.

Bir `Person` sınıfı tanımlandı ve iki kişi öğesi içeren bir liste oluşturuldu.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Şimdi nesne listesinde döngü yapmak için `foreach` deyimini kullanabiliriz.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## C# `List.ForEach` yöntemini kullanma

`List<T>.ForEach` yöntemi, Listenin her bir öğesi üzerinde verilen `action` adresini gerçekleştirir.

Kabul eder `Action<T>` temsilci parametresi. 

Aşağıdaki örnek, nesne listesinde döngü kullanarak `Action<T>` delege.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## `for` ifadesini kullanma

İndekse bağlı olarak liste elemanları üzerinde herhangi bir eylem gerçekleştirmek istiyorsanız, bir C# listesi üzerinde döngü yapmak için eski `for` deyimini kullanabiliriz. 

Aksi takdirde `foreach` veya `List<T>.ForEach()` yöntemler.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Özet

Bu eğitimde, `foreach`, `List<T.ForEach` ve `for` deyimlerini kullanarak C#'ta bir liste üzerinde nasıl döngü yapılacağını öğrendik.










