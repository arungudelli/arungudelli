---
title: "Come impostare il valore predefinito della proprietà C# o della proprietà C# implementata automaticamente"
description: "In questo tutorial impareremo 4 modi diversi per impostare il valore predefinito delle proprietà C# utilizzando semplici esempi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# le proprietà o le proprietà auto implementate sono ampiamente utilizzate nelle nostre classi al posto dei campi, cioè delle variabili.  

Le proprietà auto implementate sono state introdotte in C# 3.0.

In questo tutorial impareremo 4 modi diversi per impostare un valore predefinito alle proprietà di C#, utilizzando semplici esempi.

1. Usare gli inizializzatori di proprietà automatiche in C# 6
2. Assegnare il valore predefinito nel costruttore
3. Utilizzo del setter di proprietà in C# 
4. Utilizzo di `DefaultValue` Attribute &amp;&amp; Property Setter

Possiamo assumere il valore predefinito come valore iniziale della proprietà in C#.

## Metodo 1: Utilizzo degli inizializzatori automatici di proprietà in C# 6

In C# 6 possiamo dichiarare la proprietà auto-implementata e impostare il valore predefinito in una sola riga di dichiarazione.

La sintassi è

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Per impostazione predefinita, le proprietà stringa hanno il valore `null`. Utilizzando la dichiarazione in linea di C# 6, impostiamo il valore predefinito come stringa vuota. 

## Metodo 2: Assegnare il valore predefinito nel costruttore

Nelle vecchie versioni di C#, C# 5 e inferiori, è buona norma impostare i valori predefiniti delle proprietà C# nel costruttore della classe.

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

## Metodo 3: Utilizzo del setter di proprietà C# 

Possiamo utilizzare il setter di proprietà C# per assegnare un valore predefinito alle proprietà implementate automaticamente.

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

## metodo 4: Utilizzo di `DefaultValue` Attribute &amp;&amp; Property Setter

Nell'esempio precedente abbiamo creato una variabile privata e assegnato un valore predefinito. 

Al suo posto possiamo usare l'attributo `DefaultValue` per assegnare un valore predefinito.

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

Ricordate ** L'attributo`DefaultValue` funziona solo con i setter di proprietà ** 

Il codice seguente non assegnerà il valore predefinito alla proprietà. Il valore predefinito è ancora `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Se si utilizza l'attributo `DefaultValue`, è necessario utilizzare un setter di proprietà.


## Riepilogo

Se si utilizza C# 6, utilizzare la dichiarazione in linea per impostare il valore predefinito delle proprietà di C#, altrimenti impostare il valore predefinito nel costruttore. 








