---
title: "How to Set default value to C# property or C# auto implemented property"
description: "In this tutorial we will learn 4 different ways to set default value to C# properties using simple examples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# properties or auto implemented properties are widely used in our classes in place of fields i.e., variables.  

Auto implemented properties are introduced in C# 3.0.

In this tutorial we will learn 4 different ways to set default value to C# properties using simple examples.

1. Using Auto-Property Initializers in C# 6
2. Assign default value in constructor
3. Using C# Property Setter
4. Using `DefaultValue` Attribute && Property Setter

We can assume default value as initial value of property in C#.

## Method 1 : Using Auto-Property Initializers in C# 6

In C# 6 we can declare the auto-implemented property and set default value in a single line declaration.

The syntax is

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
By default string properties will have `null` value, By using C# 6 in-line declaration, We are setting the default value as empty string. 

## Method 2: Assign default value in constructor

In the older versions of C#, C# 5 and below it's a good practice to set default values of C# properties in the constructor of the class.

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

## Method 3: Using C# Property Setter 

We can make use of C# property setter to assign a default value to auto implemented properties.

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

## method 4: Using `DefaultValue` Attribute && Property Setter

In the above example we have created a private variable and assigned a default value. 

Instead of that we can use `DefaultValue` attribute to assign default value.

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

Remember **`DefaultValue` attribute only works with property setter.** 

The below code will not assign default value to the property. The default value is still `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
If you are using `DefaultValue` attribute you must use property setter.


## Summary

If you are using C# 6 use in-line declaration to set default value to C# properties other wise set default value in the constructor. 








