---
title: "Cum setați valoarea implicită pentru proprietatea C# sau C# proprietate auto implementată"
description: "În acest tutorial vom învăța 4 moduri diferite de a seta valoarea implicită pentru proprietățile C# folosind exemple simple"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# proprietățile sau proprietățile implementate automat sunt utilizate pe scară largă în clasele noastre în locul câmpurilor, adică al variabilelor.  

Proprietățile autoimplementate sunt introduse în C# 3.0.

În acest tutorial vom învăța 4 moduri diferite de a seta o valoare implicită pentru proprietățile C# folosind exemple simple.

1. Utilizarea inițializatorilor de proprietăți automate în C# 6
2. Atribuirea valorii implicite în constructor
3. Utilizarea C# Property Setter
4. Utilizare `DefaultValue` Attribute &amp;&amp; Property Setter

Putem asuma valoarea implicită ca valoare inițială a proprietății în C#.

## Metoda 1 : Utilizarea inițializatorilor de proprietăți automate în C# 6

În C# 6 putem declara proprietatea auto-implementată și seta valoarea implicită într-o declarație pe o singură linie.

Sintaxa este

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
În mod implicit, proprietățile de tip șir de caractere vor avea valoarea `null`. Prin utilizarea declarației în linie C# 6, stabilim valoarea implicită ca șir de caractere gol. 

## Metoda 2: Atribuiți valoarea implicită în constructor

În versiunile mai vechi ale C#, C# 5 și inferioare, este o bună practică să setați valorile implicite ale proprietăților C# în constructorul clasei.

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

## Metoda 3: Utilizarea C# Property Setter 

Putem utiliza C# property setter pentru a atribui o valoare implicită proprietăților implementate automat.

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

## metoda 4: Utilizarea `DefaultValue` Attribute &amp;&amp;&amp; Property Setter

În exemplul de mai sus, am creat o variabilă privată și i-am atribuit o valoare implicită. 

În loc de aceasta, putem utiliza atributul `DefaultValue` pentru a atribui o valoare implicită.

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

Nu uitați că ** atributul`DefaultValue` funcționează numai cu property setter.** 

Codul de mai jos nu va atribui o valoare implicită proprietății. Valoarea implicită este în continuare `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Dacă folosiți atributul `DefaultValue`, trebuie să utilizați property setter.


## Rezumat

Dacă utilizați C# 6, utilizați declarația in-line pentru a seta valoarea implicită a proprietăților C#, în caz contrar, setați valoarea implicită în constructor. 








