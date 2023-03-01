---
title: "如何为C# 属性或C# 自动实现的属性设置默认值"
description: "在本教程中，我们将通过简单的例子学习为C# 属性设置默认值的4种不同方法"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# 属性或自动实现的属性在我们的类中广泛使用，以代替字段，即变量。  

自动实现的属性是在C# 3.0中引入的。

在本教程中，我们将通过简单的例子学习4种不同的方法来为C# 属性设置默认值。

1.在C# 6中使用自动属性初始化器
2.在构造函数中分配默认值
3.使用C# 属性设置器
4.使用`DefaultValue` Attribute &amp;&amp; Property Setter

我们可以在C# 中假设默认值作为属性的初始值。

## 方法1：在C# 6中使用自动属性初始化器

在C# 6中，我们可以在单行声明中声明自动实现的属性并设置默认值。

其语法是

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
默认情况下，字符串属性会有`null` ，通过使用C# 6的行内声明，我们将默认值设置为空字符串。 

## 方法2：在构造函数中指定默认值

在旧版本的C# 、C# 5及以下版本中，在类的构造函数中设置C# 属性的默认值是一个好的做法。

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

## 方法3：使用C# 属性设置器 

我们可以利用C# 属性设置器来为自动实现的属性分配一个默认值。

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

## 方法4：使用`DefaultValue` Attribute &amp;&amp; Property Setter

在上面的例子中，我们创建了一个私有变量并分配了一个默认值。 

相反，我们可以使用`DefaultValue` 属性来分配默认值。

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

记住 **`DefaultValue` 属性只适用于属性设置器。** 

下面的代码不会为该属性分配默认值。默认值仍然是`null` 。

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
如果你使用`DefaultValue` 属性，你必须使用属性设置器。


## 摘要

如果你使用C# 6，使用行内声明为C# 属性设置默认值，否则就在构造函数中设置默认值。 








