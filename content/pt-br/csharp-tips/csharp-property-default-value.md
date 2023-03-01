---
title: "Como definir o valor padrão para C# propriedade ou C# propriedade implementada automaticamente"
description: "Neste tutorial aprenderemos 4 maneiras diferentes de definir o valor padrão para C# propriedades usando exemplos simples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# propriedades ou propriedades implementadas automaticamente são amplamente utilizadas em nossas classes no lugar de campos, ou seja, variáveis.  

As propriedades auto implementadas são introduzidas em C# 3.0.

Neste tutorial, aprenderemos 4 maneiras diferentes de definir o valor padrão para as propriedades C# usando exemplos simples.

1. Usando Auto-Property Initializers em C# 6
2. Atribuir valor padrão no construtor
3. Usando C# Property Setter
4. Usando `DefaultValue` Attribute &amp;&amp; Property Setter

Podemos assumir o valor padrão como valor inicial da propriedade em C#.

## Método 1 : Usando Auto-Property Initializers em C# 6

Em C# 6 podemos declarar a propriedade auto-implementada e definir o valor padrão em uma declaração de linha única.

A sintaxe é

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Por padrão, as propriedades da string terão o valor `null`, Ao usar C# 6 declaração em linha, estamos definindo o valor padrão como string vazia. 

## Método 2: Atribuir valor padrão no construtor

Nas versões anteriores de C#, C# 5 e abaixo é uma boa prática definir valores padrão de propriedades de C# no construtor da classe.

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

## Método 3: Usando C# Property Setter 

Podemos fazer uso de C# property setter para atribuir um valor padrão às propriedades implementadas automaticamente.

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

## método 4: Usando `DefaultValue` Attribute &amp;&amp; Property Setter

No exemplo acima, criamos uma variável privada e atribuímos um valor padrão. 

Em vez disso, podemos usar o atributo `DefaultValue` para atribuir valor padrão.

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

Lembrar **`DefaultValue` atributo só funciona com o property setter.** 

O código abaixo não atribuirá valor padrão ao imóvel. O valor padrão ainda é `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Se você estiver usando o atributo `DefaultValue`, você deve usar o property setter.


## Sumário

Se você estiver usando C# 6 use a declaração em linha para definir o valor padrão para C# propriedades, outros valores padrão no construtor. 








