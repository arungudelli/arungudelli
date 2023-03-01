---
title: "Kuinka asettaa oletusarvo C# ominaisuuteen tai C# automaattisesti toteutettuun ominaisuuteen"
description: "Tässä opetusohjelmassa opimme 4 eri tapaa asettaa oletusarvo C# ominaisuuksiin yksinkertaisten esimerkkien avulla"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# ominaisuuksia tai automaattisesti toteutettuja ominaisuuksia käytetään yleisesti luokissamme kenttien eli muuttujien sijasta.  

Automaattisesti toteutetut ominaisuudet on otettu käyttöön osoitteessa C# 3.0.

Tässä opetusohjelmassa opettelemme 4 eri tapaa asettaa oletusarvo C# ominaisuuksille yksinkertaisten esimerkkien avulla.

1. Automaattisten ominaisuuksien alustajien käyttäminen C# 6:ssa
2. Oletusarvon määrittäminen konstruktorissa
3. C# -ominaisuuden asettajan käyttäminen
4. Käyttämällä `DefaultValue` Attribuutti &amp;&amp; Ominaisuuden asettaja

Voimme olettaa oletusarvon ominaisuuden alkuarvoksi osoitteessa C#.

## Menetelmä 1 : Automaattisten ominaisuuden alkuarvojen käyttäminen osoitteessa C# 6

 C# 6:ssa voimme ilmoittaa automaattisen ominaisuuden ja asettaa oletusarvon yhdellä rivillä.

Syntaksi on

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Oletusarvoisesti merkkijono-ominaisuuksilla on `null` arvo, Käyttämällä C# 6:n rivi-ilmoitusta, asetamme oletusarvoksi tyhjän merkkijonon. 

## Menetelmä 2: Määritä oletusarvo konstruktorissa

Vanhemmissa versioissa C#, C# 5 ja sitä vanhemmissa versioissa on hyvä käytäntö asettaa C# ominaisuuksien oletusarvot luokan konstruktorissa.

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

## Menetelmä 3: C# ominaisuuksien asettajan käyttäminen 

Voimme käyttää C# -ominaisuuden asettajaa määrittääksemme oletusarvon automaattisesti toteutetuille ominaisuuksille.

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

## menetelmä 4: `DefaultValue` attribuutin &amp;&amp; ominaisuuden asettajan käyttäminen

Yllä olevassa esimerkissä olemme luoneet yksityisen muuttujan ja antaneet sille oletusarvon. 

Sen sijaan voimme käyttää `DefaultValue` -attribuuttia oletusarvon määrittämiseen.

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

Muista **`DefaultValue` attribuutti toimii vain ominaisuuden asettajan kanssa.** 

Alla oleva koodi ei anna ominaisuudelle oletusarvoa. Oletusarvo on edelleen `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Jos käytät `DefaultValue` -attribuuttia, sinun on käytettävä property setteriä.


## Yhteenveto

Jos käytät C# 6 -ominaisuutta, käytä rivi-ilmoitusta asettaaksesi oletusarvon C# -ominaisuuksille, muuten aseta oletusarvo konstruktorissa. 








