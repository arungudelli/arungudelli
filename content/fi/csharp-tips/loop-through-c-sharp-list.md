---
title: " 3 erilaista tapaa kiertää C#-luettelo"
description: "Eri tapoja kiertää C#-luettelo esimerkkien avulla"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` ovat yksi C#-kielen käytetyimmistä tietorakenteista. 

Toistaminen luettelon `List<T>` ja joidenkin operaatioiden suorittaminen listan elementeillä on melko yleistä päivittäisissä projekteissamme.

Listan läpikäymiseen C#-kielessä voidaan käyttää kolmea eri tapaa.

1. Käyttämällä C#:n `foreach` -lauseketta.
2. Käyttämällä C# `List.ForEach` -menetelmää.
3. Yksinkertaisen for-silmukan käyttö.

Käydään läpi esimerkki sen ymmärtämiseksi tarkemmin. 

Luomme ensin yksinkertaisen C#-luettelon.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Nyt näemme eri tapoja silmukoida C#-listaa.

## C# `foreach` -lausekkeen käyttäminen

 `foreach` -lausekkeen käyttäminen C#-luettelon silmukointiin on laajalti käytetty menetelmä.

Lisäksi voimme suorittaa minkä tahansa operaation listan elementeille.

Alla olevassa esimerkissä olen luonut merkkijonojen luettelon.

Sen jälkeen luettelemme listaa käyttäen `foreach` ja tulostamme listan elementit konsoliin.

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

Nyt luomme luettelon objekteista ja silmukoimme niitä käyttäen `foreach` -lauseketta.

Määritellään luokka `Person` ja luodaan lista, jossa on kaksi henkilöelementtiä.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Nyt voimme käyttää `foreach` -lausetta kiertääksemme objektiluettelon läpi.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## C# `List.ForEach` -menetelmän käyttäminen

`List<T>.ForEach` metodi suorittaa annetun `action` jokaiselle listan elementille.

Se hyväksyy `Action<T>` delegate-parametrin. 

Seuraavassa esimerkissä käydään läpi objektiluettelo käyttäen komentoa `Action<T>` delegate.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Käyttämällä `for` -lauseketta

Voimme käyttää perinteistä `for` -lauseketta C#-luettelon läpikäymiseen, jos haluat suorittaa luettelon elementeille jonkin toiminnon indeksin perusteella. 

Muussa tapauksessa käytetään `foreach` tai `List<T>.ForEach()` menetelmiin.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Yhteenveto

Tässä opetusohjelmassa opimme, miten luettelon läpikäyntiä tehdään C#-kielellä käyttäen `foreach`, `List<T.ForEach` ja `for` -lausekkeita.










