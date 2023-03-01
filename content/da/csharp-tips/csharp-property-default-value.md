---
title: "Sådan indstiller du standardværdi til C# ejendom eller C# auto implementeret ejendom"
description: "I denne vejledning lærer vi 4 forskellige måder at indstille standardværdi til C# egenskaber ved hjælp af enkle eksempler"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# egenskaber eller auto implementerede egenskaber er meget udbredt i vores klasser i stedet for felter, dvs. variabler.  

Auto implementerede egenskaber blev introduceret i C# 3.0.

I denne tutorial vil vi lære 4 forskellige måder at indstille standardværdi til C# egenskaber på ved hjælp af enkle eksempler.

1. Brug af automatiske egenskabsinitialisatorer i C# 6
2. Tildel standardværdi i konstruktør
3. Brug af C# Property Setter
4. Brug af `DefaultValue` Attribute &amp;&amp; Property Setter

Vi kan antage standardværdien som initialværdi for egenskaben i C#.

## Metode 1 : Brug af automatiske egenskabsinitialisatorer i C# 6

I C# 6 kan vi erklære den auto-implementerede egenskab og indstille standardværdien i en enkelt linje erklæring.

Syntaksen er

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Som standard har string-egenskaberne `null` værdi. Ved at bruge C# 6 in-line-deklaration indstiller vi standardværdien som en tom streng. 

## Metode 2: Tildel standardværdi i konstruktøren

I de ældre versioner af C#, C# 5 og lavere er det en god praksis at angive standardværdier for C# egenskaber i klassens konstruktør.

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

## Metode 3: Brug af C# Property Setter 

Vi kan gøre brug af C# property setter til at tildele en standardværdi til automatisk implementerede egenskaber.

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

## metode 4: Brug af `DefaultValue` Attribute &amp;&amp; Property Setter

I ovenstående eksempel har vi oprettet en privat variabel og tildelt en standardværdi. 

I stedet kan vi bruge attributten `DefaultValue` til at tildele standardværdi.

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

Husk **`DefaultValue` -attributten fungerer kun med property setter.** 

Nedenstående kode tildeler ikke standardværdien til egenskaben. Standardværdien er stadig `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Hvis du bruger attributten `DefaultValue`, skal du bruge egenskabssætteren.


## Resumé

Hvis du bruger C# 6, skal du bruge in-line-deklaration til at indstille standardværdien til C# -egenskaberne, ellers skal du indstille standardværdien i konstruktøren. 








