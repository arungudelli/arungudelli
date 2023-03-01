---
title: "Jak nastavit výchozí hodnotu vlastnosti C# nebo C# automaticky implementované vlastnosti"
description: "V tomto tutoriálu se naučíme 4 různé způsoby nastavení výchozí hodnoty vlastnosti C# na jednoduchých příkladech"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# vlastnosti nebo automaticky implementované vlastnosti se v našich třídách hojně používají místo polí, tj. proměnných.  

Automaticky implementované vlastnosti jsou zavedeny v C# 3.0.

V tomto tutoriálu se na jednoduchých příkladech naučíme 4 různé způsoby, jak nastavit výchozí hodnotu C# vlastnostem.

1. Používání automaticky spouštěných inicializátorů vlastností v C# 6
2. Přiřazení výchozí hodnoty v konstruktoru
3. Použití nastavovače vlastností C# 
4. Použití `DefaultValue` Atribut &amp;&amp; Property Setter

Jako počáteční hodnotu vlastnosti můžeme předpokládat výchozí hodnotu v C#.

## Metoda 1 : Použití automatických inicializátorů vlastností v C# 6

V C# 6 můžeme deklarovat automaticky implementovanou vlastnost a nastavit výchozí hodnotu v jednořádkové deklaraci.

Syntaxe je následující

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Ve výchozím nastavení bude mít řetězcová vlastnost hodnotu `null`, Pomocí řádkové deklarace C# 6 nastavujeme výchozí hodnotu jako prázdný řetězec. 

## Metoda 2: Přiřazení výchozí hodnoty v konstruktoru

Ve starších verzích C#, C# 5 a nižších je dobrým zvykem nastavit výchozí hodnoty vlastností C# v konstruktoru třídy.

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

## Metoda 3: Použití nastavovače vlastností C# 

K přiřazení výchozí hodnoty automaticky implementovaným vlastnostem můžeme využít setter vlastností C#.

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

## metoda 4: Použití `DefaultValue` Attribute &amp;&amp; Property Setter

Ve výše uvedeném příkladu jsme vytvořili soukromou proměnnou a přiřadili jí výchozí hodnotu. 

Místo toho můžeme k přiřazení výchozí hodnoty použít atribut `DefaultValue`.

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

Nezapomeňte, že ** atribut`DefaultValue` funguje pouze s nastavovačem vlastností.** 

Níže uvedený kód nepřiřadí vlastnosti výchozí hodnotu. Výchozí hodnota je stále `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Pokud používáte atribut `DefaultValue`, musíte použít property setter.


## Shrnutí

Pokud používáte C# 6, použijte in-line deklaraci pro nastavení výchozí hodnoty vlastností C#. V opačném případě nastavte výchozí hodnotu v konstruktoru. 








