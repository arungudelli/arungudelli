---
title: "Så här ställer du in standardvärdet för C# -egendomen eller C# autoimplementerad egendom"
description: "I den här handledningen lär vi oss 4 olika sätt att ställa in standardvärdet för C# -egendomen med hjälp av enkla exempel"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# egenskaper eller autoimplementerade egenskaper används ofta i våra klasser i stället för fält, dvs. variabler.  

Autoimplementerade egenskaper infördes i C# 3.0.

I den här handledningen kommer vi att lära oss 4 olika sätt att ställa in standardvärden för C# properties med hjälp av enkla exempel.

1. Användning av automatiska egenskapsinitialiserare i C# 6
2. Tilldela standardvärde i konstruktören
3. Användning av C# Property Setter
4. Användning av `DefaultValue` Attribute &amp;&amp; Property Setter

Vi kan anta standardvärdet som första värde för egenskapen i C#.

## Metod 1 : Användning av automatiska egenskapsinitialiserare i C# 6

I C# 6 kan vi deklarera den automatiskt implementerade egenskapen och ställa in standardvärdet på en enda rad.

Syntaxen är

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Som standard har strängegenskaperna ett värde på `null`. Genom att använda C# 6-deklarationen på en rad ställer vi in standardvärdet som en tom sträng. 

## Metod 2: Tilldela standardvärde i konstruktören

I de äldre versionerna av C#, C# 5 och lägre är det bra att ange standardvärden för C# -egenskaperna i klassens konstruktör.

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

## Metod 3: Användning av C# Property Setter 

Vi kan använda C# property setter för att tilldela ett standardvärde till automatiskt implementerade egenskaper.

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

## metod 4: Användning av `DefaultValue` Attribute &amp;&amp; Property Setter

I exemplet ovan har vi skapat en privat variabel och tilldelat ett standardvärde. 

I stället kan vi använda attributet `DefaultValue` för att tilldela ett standardvärde.

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

Kom ihåg **`DefaultValue` -attributet fungerar endast med egenskapssättare.** 

Koden nedan kommer inte att tilldela egenskapen ett standardvärde. Standardvärdet är fortfarande `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Om du använder attributet `DefaultValue` måste du använda egenskapssättaren.


## Sammanfattning

Om du använder C# 6 använder du in-line-deklaration för att ställa in standardvärdet för C# -egenskaperna, annars ställer du in standardvärdet i konstruktören. 








