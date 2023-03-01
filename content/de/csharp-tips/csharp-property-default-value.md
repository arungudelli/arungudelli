---
title: "Wie man den Standardwert für die Eigenschaft C# oder die automatisch implementierte Eigenschaft C# festlegt"
description: "In diesem Tutorial lernen wir anhand einfacher Beispiele 4 verschiedene Möglichkeiten kennen, den Standardwert für die Eigenschaften C# festzulegen"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# eigenschaften oder automatisch implementierte Eigenschaften werden in unseren Klassen häufig anstelle von Feldern, d.h. Variablen, verwendet.  

Automatisch implementierte Eigenschaften wurden in C# 3.0 eingeführt.

In diesem Tutorial werden wir anhand einfacher Beispiele 4 verschiedene Möglichkeiten kennenlernen, wie man C# Eigenschaften einen Standardwert zuweisen kann.

1. Verwendung von Auto-Eigenschaftsinitialisierern in C# 6
2. Standardwert im Konstruktor zuweisen
3. Verwendung von C# Property Setter
4. Verwendung von `DefaultValue` Attribute &amp;&amp; Property Setter

Wir können den Standardwert als Anfangswert der Eigenschaft in C# übernehmen.

## Methode 1: Verwendung von Auto-Eigenschaftsinitialisierern in C# 6

In C# 6 können wir die automatisch implementierte Eigenschaft deklarieren und den Standardwert in einer einzigen Zeile festlegen.

Die Syntax lautet

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Standardmäßig haben String-Eigenschaften den Wert `null`. Durch die Verwendung der Inline-Deklaration C# 6 setzen wir den Standardwert als leeren String. 

## Methode 2: Standardwert im Konstruktor zuweisen

In den älteren Versionen von C#, C# 5 und darunter ist es eine gute Praxis, Standardwerte für C# Eigenschaften im Konstruktor der Klasse festzulegen.

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

## Methode 3: Verwendung von C# Property Setter 

Wir können C# property setter verwenden, um den automatisch implementierten Eigenschaften einen Standardwert zuzuweisen.

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

## methode 4: Verwendung von `DefaultValue` Attribute &amp;&amp; Property Setter

Im obigen Beispiel haben wir eine private Variable erstellt und einen Standardwert zugewiesen. 

Stattdessen können wir das Attribut `DefaultValue` verwenden, um einen Standardwert zuzuweisen.

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

Denken Sie daran, dass das Attribut`DefaultValue` nur mit Property Setter funktioniert 

Der folgende Code weist der Eigenschaft keinen Standardwert zu. Der Standardwert ist immer noch `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Wenn Sie das Attribut `DefaultValue` verwenden, müssen Sie den Property Setter benutzen.


## Zusammenfassung

Wenn Sie C# 6 verwenden, verwenden Sie eine Inline-Deklaration, um einen Standardwert für C# Eigenschaften zu setzen, andernfalls setzen Sie den Standardwert im Konstruktor. 








