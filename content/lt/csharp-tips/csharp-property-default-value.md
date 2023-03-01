---
title: "Kaip nustatyti numatytąją reikšmę C# savybei arba C# automatiškai įgyvendintai savybei"
description: "Šioje pamokoje sužinosime 4 skirtingus būdus, kaip nustatyti numatytąją reikšmę C# savybėms naudojant paprastus pavyzdžius"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# savybės arba automatiškai įgyvendintos savybės plačiai naudojamos mūsų klasėse vietoj laukų, t. y. kintamųjų.  

Automatiškai įgyvendintos savybės pradėtos naudoti C# 3.0 versijoje.

Šioje pamokoje, remdamiesi paprastais pavyzdžiais, sužinosime 4 skirtingus būdus, kaip C# savybėms nustatyti numatytąją reikšmę.

1. Automatiškai nustatomų savybių iniciatorių naudojimas C# 6
2. Numatytosios reikšmės priskyrimas konstruktoriuje
3. Naudojant C# savybių nustatinėtoją
4. Naudojant `DefaultValue` atributų ir savybių nustatymą

Pradine savybės verte galime laikyti numatytąją reikšmę C#.

## 1 metodas : automatinių savybių iniciatorių naudojimas C# 6

Svetainėje C# 6 galime deklaruoti automatiškai įgyvendinamą savybę ir nustatyti numatytąją reikšmę vienos eilutės deklaracijoje.

Sintaksė yra tokia

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Pagal numatytuosius nustatymus eilutės savybė turės `null` reikšmę, Naudodami C# 6 eilutės deklaraciją, nustatome numatytoji reikšmė yra tuščia eilutė. 

## 2 būdas: priskirti numatytąją reikšmę konstruktoriuje

Senesnėse C#, C# 5 ir vėlesnėse versijose gera praktika yra klasės konstruktoriuje nustatyti numatytąsias C# savybių reikšmes.

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

## 3 būdas: naudojant C# savybių nustatinėtoją 

Norėdami priskirti numatytąją reikšmę automatiškai įdiegtoms savybėms, galime pasinaudoti C# savybių nustatinėtoju.

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

## 4 būdas: `DefaultValue` atributų ir savybių nustatinėtojo naudojimas

Pirmiau pateiktame pavyzdyje sukūrėme privatų kintamąjį ir priskyrėme numatytąją reikšmę. 

Vietoj to galime naudoti `DefaultValue` atributą, kad priskirtume numatytąją reikšmę.

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

Atminkite, kad **`DefaultValue` atributas veikia tik su savybių nustatymu.** 

Toliau pateiktas kodas nepriskirs savybės numatytoji reikšmė. Numatytoji reikšmė vis tiek bus `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Jei naudojate atributą `DefaultValue`, turite naudoti savybės nustatymą.


## Apibendrinimas

Jei naudojate C# 6, naudokite eilutinę deklaraciją, kad nustatytumėte numatytąją reikšmę C# savybėms, kitu atveju numatytąją reikšmę nustatykite konstruktoriuje. 








