---
title: "Como definir o valor por defeito para C# propriedade ou C# propriedade implementada automaticamente"
description: "Neste tutorial aprenderemos 4 formas diferentes de definir o valor por defeito para C# propriedades usando exemplos simples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# propriedades ou propriedades auto implementadas são amplamente utilizadas nas nossas classes em vez de campos, ou seja, variáveis.  

As propriedades auto implementadas são introduzidas em C# 3.0.

Neste tutorial iremos aprender 4 formas diferentes de definir o valor por defeito para C# propriedades usando exemplos simples.

1. Usando Auto-Property Initializers em C# 6
2. Atribuir valor por defeito no construtor
3. Usando C# Property Setter
4. Usando `DefaultValue` Attribute &amp;&amp; Property Setter

Podemos assumir o valor por defeito como valor inicial da propriedade em C#.

## Método 1 : Usando Auto-Property Initializers em C# 6

Em C# 6 podemos declarar a propriedade auto-implementada e definir o valor por defeito numa declaração de linha única.

A sintaxe é

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Por defeito as propriedades da string terão o valor `null`, Ao utilizar a declaração em linha C# 6, Estamos a definir o valor por defeito como string vazia. 

## Método 2: Atribuir valor por defeito no construtor

Nas versões mais antigas de C#, C# 5 e abaixo é uma boa prática definir valores padrão de propriedades de C# no construtor da classe.

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

Podemos fazer uso de C# property setter para atribuir um valor por defeito às propriedades auto implementadas.

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

No exemplo acima, criámos uma variável privada e atribuímos-lhe um valor por defeito. 

Em vez disso, podemos utilizar o atributo `DefaultValue` para atribuir um valor por defeito.

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

Lembre-se **`DefaultValue` atributo só funciona com o property setter.** 

O código abaixo não atribuirá valor por defeito ao imóvel. O valor por defeito continua a ser `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Se estiver a utilizar o atributo `DefaultValue` deve utilizar o property setter.


## Resumo

Se estiver a utilizar C# 6 utilize a declaração em linha para definir o valor por defeito para C# propriedades, outros valores por defeito sensatos no construtor. 








