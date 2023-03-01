---
title: "Kā iestatīt noklusējuma vērtību C# īpašībai vai C# automātiski īstenotajai īpašībai"
description: "Šajā pamācībā mēs uzzināsim 4 dažādus veidus, kā iestatīt noklusējuma vērtību C# īpašībām, izmantojot vienkāršus piemērus"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# īpašības vai automātiski īstenotās īpašības tiek plaši izmantotas mūsu klasēs lauku, t.i., mainīgo vietā.  

Automātiski īstenotās īpašības ir ieviestas C# 3.0 versijā.

Šajā pamācībā mēs uzzināsim 4 dažādus veidus, kā iestatīt noklusējuma vērtību C# īpašībām, izmantojot vienkāršus piemērus.

1. Automātisko īpašību inicializatoru izmantošana C# 6
2. Noklusējuma vērtības piešķiršana konstruktorā
3. Izmantojot C# īpašību iestatītāju
4. Izmantojot `DefaultValue` Atribūtu &amp;&amp;īpašības iestatītāju

Mēs varam pieņemt noklusējuma vērtību kā īpašības sākotnējo vērtību C#.

## 1. metode : Automātisko īpašību inicializatoru izmantošana C# 6

Programmā C# 6 mēs varam deklarēt automātiski implementētu īpašību un iestatīt noklusējuma vērtību vienas rindas deklarācijā.

Sintakse ir šāda

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Pēc noklusējuma virknes īpašībām būs `null` vērtība, Izmantojot C# 6 rindu deklarāciju, mēs iestatām noklusējuma vērtību kā tukšu virkni. 

## Metode: Noklusējuma vērtības piešķiršana konstruktorā

Vecākajās C#, C# 5 un jaunākajās versijās ir laba prakse klases konstruktorā noteikt C# īpašību noklusējuma vērtības.

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

## Metode: Izmantojot C# īpašību iestatītāju 

Mēs varam izmantot C# īpašību iestatītāju, lai piešķirtu noklusējuma vērtību automātiski ieviestajām īpašībām.

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

## metode: Izmantojot `DefaultValue` atribūtu &amp;&amp; īpašību iestatītāju

Iepriekš minētajā piemērā mēs esam izveidojuši privātu mainīgo un piešķīruši tam noklusējuma vērtību. 

Tā vietā mēs varam izmantot atribūtu `DefaultValue`, lai piešķirtu noklusējuma vērtību.

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

Atcerieties, ka **`DefaultValue` atribūts darbojas tikai ar īpašību iestatītāju** 

Tālāk norādītais kods īpašībai nepiešķirs noklusējuma vērtību. Noklusējuma vērtība joprojām ir `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Ja izmantojat atribūtu `DefaultValue`, jums jāizmanto īpašību iestatītājs.


## Kopsavilkums

Ja jūs izmantojat C# 6, izmantojiet rindu deklarāciju, lai iestatītu noklusējuma vērtību C# īpašībām, citādi noklusējuma vērtību iestatiet konstruktorā. 








