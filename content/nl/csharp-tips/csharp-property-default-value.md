---
title: "Hoe standaardwaarde instellen op C# property of C# automatisch geïmplementeerde property"
description: "In deze tutorial leren we 4 verschillende manieren om standaardwaarde in te stellen op C# properties aan de hand van eenvoudige voorbeelden"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# properties of automatisch geïmplementeerde eigenschappen worden veel gebruikt in onze klassen in plaats van velden, d.w.z. variabelen.  

Automatisch geïmplementeerde eigenschappen zijn geïntroduceerd in C# 3.0.

In deze tutorial leren we 4 verschillende manieren om standaardwaarden in te stellen op C# properties aan de hand van eenvoudige voorbeelden.

1. Automatisch geïmplementeerde eigenschappen gebruiken in C# 6
2. Standaardwaarde toewijzen in de constructor
3. C# Property Setter gebruiken
4. Met `DefaultValue` Attribute &amp;&amp; Property Setter

We kunnen standaardwaarde aannemen als initiële waarde van eigenschap in C#.

## Methode 1: Automatische Property Initializers gebruiken in C# 6

In C# 6 kunnen we de automatisch geïmplementeerde eigenschap declareren en de standaardwaarde instellen in een enkele regel declaratie.

De syntaxis is

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Standaard hebben string-eigenschappen de waarde `null`. Door C# 6 in-line declaratie te gebruiken, stellen we de standaardwaarde in als lege string. 

## Methode 2: Standaardwaarde toewijzen in de constructor

In de oudere versies van C#, C# 5 en lager is het een goede gewoonte om standaardwaarden voor C# eigenschappen in te stellen in de constructor van de klasse.

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

## Methode 3: Gebruik van C# Property Setter 

We kunnen gebruik maken van C# property setter om een standaardwaarde toe te wijzen aan automatisch geïmplementeerde eigenschappen.

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

## methode 4: Gebruik van `DefaultValue` Attribute &amp;&amp; Property Setter

In het bovenstaande voorbeeld hebben we een private variabele aangemaakt en een standaardwaarde toegekend. 

In plaats daarvan kunnen we het attribuut `DefaultValue` gebruiken om een standaardwaarde toe te wijzen.

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

Denk eraan **`DefaultValue` attribuut werkt alleen met property setter.** 

De onderstaande code kent geen standaardwaarde toe aan de eigenschap. De standaardwaarde is nog steeds `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Als u `DefaultValue` attribuut gebruikt, moet u property setter gebruiken.


## Samenvatting

Als u C# 6 gebruikt, gebruik dan een in-line declaratie om de standaardwaarde in te stellen op C# eigenschappen, anders stelt u de standaardwaarde in in de constructor. 








