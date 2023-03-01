---
title: "Cómo establecer el valor por defecto a C# propiedad o C# auto implementado propiedad"
description: "En este tutorial vamos a aprender 4 maneras diferentes para establecer el valor por defecto a C# propiedades utilizando ejemplos sencillos"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# las propiedades o propiedades auto implementadas son ampliamente utilizadas en nuestras clases en lugar de campos, es decir, variables.  

Las propiedades auto implementadas se introdujeron en C# 3.0.

En este tutorial vamos a aprender 4 maneras diferentes de establecer el valor predeterminado de C# propiedades utilizando ejemplos sencillos.

1. Uso de Inicializadores Automáticos de Propiedades en C# 6
2. Asignar valor por defecto en el constructor
3. Utilización del definidor de propiedades C# 
4. Usando `DefaultValue` Attribute &amp;&amp; Property Setter

Podemos asumir el valor por defecto como valor inicial de la propiedad en C#.

## Método 1 : Usando Inicializadores Automáticos de Propiedades en C# 6

En C# 6 podemos declarar la propiedad auto-implementada y establecer el valor por defecto en una sola línea de declaración.

La sintaxis es

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Por defecto, las propiedades de cadena tendrán el valor `null`, utilizando C# 6 declaración en línea, estamos estableciendo el valor por defecto como cadena vacía. 

## Método 2: Asignar valor por defecto en el constructor

En las versiones anteriores de C#, C# 5 e inferiores es una buena práctica establecer los valores por defecto de las propiedades C# en el constructor de la clase.

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

## Método 3: Utilizar el definidor de propiedades C# 

Podemos hacer uso de C# property setter para asignar un valor por defecto a las propiedades auto implementadas.

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

En el ejemplo anterior hemos creado una variable privada y le hemos asignado un valor por defecto. 

En lugar de eso podemos usar el atributo `DefaultValue` para asignar un valor por defecto.

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

Recuerde **`DefaultValue` atributo sólo funciona con la propiedad setter.** 

El código de abajo no asignará valor por defecto a la propiedad. El valor por defecto sigue siendo `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Si está utilizando el atributo `DefaultValue` debe utilizar la propiedad setter.


## Resumen

Si utiliza C# 6, utilice la declaración en línea para establecer el valor predeterminado de las propiedades de C#. De lo contrario, establezca el valor predeterminado en el constructor. 








