---
title: "Kako nastaviti privzeto vrednost za lastnost C# ali C# samodejno implementirano lastnost"
description: "V tem učbeniku se bomo naučili 4 različne načine za nastavitev privzete vrednosti za lastnosti C# z uporabo preprostih primerov"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# lastnosti ali samodejno implementirane lastnosti se v naših razredih pogosto uporabljajo namesto polj, tj. spremenljivk.  

Samodejno implementirane lastnosti so uvedene v C# 3.0.

V tem učbeniku se bomo s preprostimi primeri naučili 4 različne načine za nastavitev privzete vrednosti lastnosti C#.

1. Uporaba samodejnih inicializatorjev lastnosti v C# 6
2. Dodelitev privzete vrednosti v konstruktorju
3. Uporaba nastavljalnika lastnosti C# 
4. Uporaba `DefaultValue` Attribute &amp;&amp; Property Setter

Kot začetno vrednost lastnosti lahko privzamemo privzeto vrednost v C#.

## Metoda 1 : Uporaba samodejnih inicializatorjev lastnosti v C# 6

V C# 6 lahko deklariramo samodejno implementirano lastnost in določimo privzeto vrednost v deklaraciji v eni sami vrstici.

Sintaksa je

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Po privzetem bodo lastnosti nizov imele `null` vrednost, Z uporabo C# 6 deklaracije v vrstici nastavimo privzeto vrednost kot prazen niz. 

## Metoda 2: Dodelitev privzete vrednosti v konstruktorju

V starejših različicah C#, C# 5 in nižjih je dobra praksa, da privzete vrednosti lastnosti C# določimo v konstruktorju razreda.

```csharp
class Product 
{
    public string Name { get; set; }
    public Product()
    {
        Name = "";
    }
}
```

## Metoda 3: Uporaba nastavljalnika lastnosti C# 

Za dodelitev privzete vrednosti samodejno implementiranim lastnostim lahko uporabimo C# property setter.

```csharp
class Product 
{
    private string _name = "";
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

## metoda 4: Uporaba `DefaultValue` Attribute &amp;&amp; Property Setter

V zgornjem primeru smo ustvarili zasebno spremenljivko in ji dodelili privzeto vrednost. 

Namesto tega lahko za dodelitev privzete vrednosti uporabimo atribut `DefaultValue`.

```csharp
class Product 
{
    private string _name;

    [DefaultValue("")]
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

Ne pozabite, da ** atribut`DefaultValue` deluje samo z nastavljalnikom lastnosti.** 

Spodnja koda lastnosti ne bo dodelila privzete vrednosti. Privzeta vrednost je še vedno `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Če uporabljate atribut `DefaultValue`, morate uporabiti nastavljalnik lastnosti.


## Povzetek

Če uporabljate C# 6, uporabite vrstično deklaracijo za nastavitev privzete vrednosti lastnosti C#. V nasprotnem primeru nastavite privzeto vrednost v konstruktorju. 








