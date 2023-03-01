---
title: "Jak ustawić wartość domyślną dla C# właściwości lub C# automatycznie zaimplementowanej właściwości"
description: "W tym poradniku poznamy 4 różne sposoby ustawiania wartości domyślnej dla C# właściwości na prostych przykładach"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# właściwości lub autoimplementowane właściwości są powszechnie używane w naszych klasach zamiast pól, czyli zmiennych.  

Właściwości autoimplementowane zostały wprowadzone w C# 3.0.

W tym tutorialu poznamy 4 różne sposoby ustawiania wartości domyślnej dla właściwości C# na prostych przykładach.

1. Używanie inicjalizatorów właściwości automatycznych w C# 6
2. Przypisanie wartości domyślnej w konstruktorze
3. Używanie C# Ustawiacza właściwości
4. Użycie `DefaultValue` Ustawianie atrybutów i właściwości

Możemy przyjąć wartość domyślną jako wartość początkową właściwości w C#.

## Metoda 1: Użycie autoinicjalizatorów właściwości w C# 6

W C# 6 możemy zadeklarować auto-implementowaną właściwość i ustawić wartość domyślną w deklaracji w jednej linii.

Składnia to

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Domyślnie właściwości łańcuchowe będą miały wartość `null`, Używając C# 6 w deklaracji liniowej, Ustawiamy wartość domyślną jako pusty ciąg. 

## Metoda 2: Przypisanie wartości domyślnej w konstruktorze

W starszych wersjach C#, C# 5 i niższych dobrą praktyką jest ustawianie wartości domyślnych właściwości C# w konstruktorze klasy.

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

## Metoda 3: Użycie C# Ustawiacza właściwości 

Możemy skorzystać z C# property setter, aby przypisać domyślną wartość do automatycznie zaimplementowanych właściwości.

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

## metoda 4: Użycie `DefaultValue` Attribute &amp;&amp; Property Setter

W powyższym przykładzie utworzyliśmy zmienną prywatną i przypisaliśmy jej wartość domyślną. 

Zamiast tego możemy użyć atrybutu `DefaultValue` do przypisania wartości domyślnej.

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

Pamiętaj **`DefaultValue` atrybut działa tylko z ustawiaczem właściwości.** 

Poniższy kod nie przypisze wartości domyślnej do właściwości. Domyślną wartością jest nadal `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Jeśli używasz atrybutu `DefaultValue` musisz użyć property setter.


## Podsumowanie

Jeśli używasz C# 6 użyj deklaracji in-line aby ustawić wartość domyślną właściwościom C# w przeciwnym razie ustaw wartość domyślną w konstruktorze. 








