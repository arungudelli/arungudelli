---
title: "Ako nastaviť predvolenú hodnotu vlastnosti C# alebo C# automaticky implementovanej vlastnosti"
description: "V tomto návode sa naučíme 4 rôzne spôsoby nastavenia predvolenej hodnoty vlastnosti C# pomocou jednoduchých príkladov"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# vlastnosti alebo automaticky implementované vlastnosti sa v našich triedach široko používajú namiesto polí, t. j. premenných.  

Automaticky implementované vlastnosti sú zavedené v C# 3.0.

V tomto učebnom texte sa na jednoduchých príkladoch naučíme 4 rôzne spôsoby nastavenia predvolenej hodnoty pre vlastnosti C#.

1. Používanie inicializátorov automaticky nastavovaných vlastností v C# 6
2. Priradenie predvolenej hodnoty v konštruktore
3. Použitie nastavovača vlastností C# 
4. Použitie `DefaultValue` Attribute &amp;&amp; Property Setter

Ako počiatočnú hodnotu vlastnosti môžeme predpokladať predvolenú hodnotu v C#.

## Metóda 1 : Použitie automatických inicializátorov vlastností v C# 6

V C# 6 môžeme deklarovať automaticky implementovanú vlastnosť a nastaviť jej predvolenú hodnotu v deklarácii na jednom riadku.

Syntax je

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Štandardne budú mať reťazcové vlastnosti hodnotu `null`, Použitím riadkovej deklarácie C# 6 nastavujeme štandardnú hodnotu ako prázdny reťazec. 

## Metóda 2: Priradenie predvolenej hodnoty v konštruktore

V starších verziách C#, C# 5 a nižších je dobrým zvykom nastaviť predvolené hodnoty vlastností C# v konštruktore triedy.

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

## Metóda 3: Použitie nastavovača vlastností C# 

Na priradenie predvolenej hodnoty automaticky implementovaným vlastnostiam môžeme využiť nastavovač vlastností C#.

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

## metóda 4: Použitie `DefaultValue` Attribute &amp;&amp; Property Setter

V uvedenom príklade sme vytvorili súkromnú premennú a priradili jej predvolenú hodnotu. 

Namiesto toho môžeme na priradenie predvolenej hodnoty použiť atribút `DefaultValue`.

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

Pamätajte si, že ** atribút`DefaultValue` funguje len s nastavovačom vlastností.** 

Nižšie uvedený kód nepriradí vlastnosti predvolenú hodnotu. Predvolená hodnota je stále `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Ak používate atribút `DefaultValue`, musíte použiť nastavovač vlastnosti.


## Zhrnutie

Ak používate C# 6, použite in-line deklaráciu na nastavenie predvolenej hodnoty vlastností C#. V opačnom prípade nastavte predvolenú hodnotu v konštruktore. 








