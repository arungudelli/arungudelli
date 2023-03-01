---
title: "Kuidas määrata vaikimisi väärtus C# omadusele või C# automaatselt rakendatud omadusele"
description: "Selles õpetuses õpime 4 erinevat viisi, kuidas määrata vaikimisi väärtus C# omadustele, kasutades lihtsaid näiteid"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# omadusi või auto implementeeritud omadusi kasutatakse meie klassides laialdaselt väljade ehk muutujate asemel.  

Automaatselt rakendatud omadused on kasutusele võetud C# 3.0.

Selles õpetuses õpime 4 erinevat viisi, kuidas määrata C# omadustele vaikeväärtus lihtsate näidete abil.

1. Automaatsete omaduste initsiaatorite kasutamine C# 6-s
2. Vaikeväärtuse määramine konstruktoris
3. Kasutades C# Property Setter
4. Kasutades `DefaultValue` Atribuut &amp;&amp; Property Setter

Me võime võtta vaikimisi väärtuse omaduse algväärtuseks C#.

## Meetod 1 : Automaatsete omaduste initsiaatorite kasutamine C# 6-s

In C# 6 saame deklareerida automaatse initsiaatori omaduse ja määrata vaikeväärtuse ühe rea deklaratsiooniga.

Süntaks on järgmine

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Vaikimisi on stringi omaduste väärtus `null`, Kasutades C# 6 in-line deklaratsiooni, seame vaikimisi väärtuseks tühja stringi. 

## Meetod 2: määrame vaikeväärtuse konstruktoris

Vanemates versioonides C#, C# 5 ja allapoole on hea tava määrata C# omaduste vaikeväärtused klassi konstruktoris.

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

## Meetod 3: Kasutades C# Property Setter'i 

Me võime kasutada C# omaduse määrajat, et määrata automaatselt rakendatud omadustele vaikeväärtus.

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

## meetod: `DefaultValue` atribuutide &amp;&amp; omaduste määraja kasutamine

Ülaltoodud näites oleme loonud privaatse muutuja ja määranud talle vaikimisi väärtuse. 

Selle asemel võime kasutada `DefaultValue` atribuuti, et määrata vaikeväärtus.

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

Pea meeles **`DefaultValue` atribuut töötab ainult koos omaduse määrajaga.** 

Allpool olev kood ei määra omadusele vaikeväärtust. Vaikeväärtus on ikkagi `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Kui kasutate `DefaultValue` atribuuti, peate kasutama omaduse määrajat.


## Kokkuvõte

Kui kasutate C# 6, kasutage in-line deklaratsiooni, et määrata vaikeväärtus C# omadustele, muidu määrake vaikeväärtus konstruktoris. 








