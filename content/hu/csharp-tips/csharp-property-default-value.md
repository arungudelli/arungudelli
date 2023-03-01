---
title: "Hogyan kell beállítani az alapértelmezett értéket a C# tulajdonságra vagy a C# automatikusan végrehajtott tulajdonságra"
description: "Ebben a bemutatóban 4 különböző módon tanuljuk meg az alapértelmezett érték beállítását a C# tulajdonságokra egyszerű példák segítségével"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# a tulajdonságok vagy auto implementált tulajdonságok széles körben használatosak az osztályainkban a mezők, azaz a változók helyett.  

Az auto implementált tulajdonságok a C# 3.0-ban kerültek bevezetésre.

Ebben a bemutatóban egyszerű példákon keresztül megtanuljuk a C# tulajdonságok alapértelmezett értékének beállításának 4 különböző módját.

1. Automatikus tulajdonság-inicializátorok használata a C# 6-ban
2. Alapértelmezett érték hozzárendelése a konstruktorban
3. A C# Property Setter használata
4. A `DefaultValue` Attribute &amp;&amp; Property Setter használata

A C# tulajdonság kezdeti értékeként alapértelmezett értéket vehetünk fel.

## 1. módszer : Automatikus tulajdonság inicializáló használata a C# 6-ban

A C# 6-ban egyetlen soros deklarációban deklarálhatjuk az automatikusan bevezetett tulajdonságot és beállíthatjuk az alapértelmezett értéket.

A szintaxis a következő

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Alapértelmezés szerint a string tulajdonságok értéke `null` lesz, A C# 6 soron belüli deklaráció használatával az alapértelmezett értéket üres stringként állítjuk be. 

## 2. módszer: Alapértelmezett érték hozzárendelése a konstruktorban

A C#, C# 5 és az alatti régebbi verziókban jó gyakorlat a C# tulajdonságok alapértelmezett értékének beállítása az osztály konstruktorában.

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

## 3. módszer: A C# Property Setter használata 

Használhatjuk a C# property setter-t, hogy alapértelmezett értéket rendeljünk az automatikusan megvalósított tulajdonságokhoz.

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

## 4. módszer: A `DefaultValue` attribútum &amp;&amp; Property Setter használata

A fenti példában létrehoztunk egy privát változót és hozzárendeltünk egy alapértelmezett értéket. 

Ehelyett használhatjuk a `DefaultValue` attribútumot az alapértelmezett érték hozzárendeléséhez.

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

Ne feledje ** A`DefaultValue` attribútum csak a tulajdonságok beállításával működik. ** 

Az alábbi kód nem rendel alapértelmezett értéket a tulajdonsághoz. Az alapértelmezett érték továbbra is a `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Ha a `DefaultValue` attribútumot használja, akkor használnia kell a property setter-t.


## Összefoglaló

Ha a C# 6-ot használja, használjon in-line deklarációt a C# tulajdonságok alapértelmezett értékének beállításához, máskülönben a konstruktorban állítsa be az alapértelmezett értéket. 








