
+++
title="如何在C#中从值中获得enum 名称"
summary="有两种方法在C#中从值中获得enum 名称 1.使用C#`Enum.GetName()` 并将enum 的值作为参数来获取名称。 2.使用铸造法将enum 值转换为enum命名成员，然后使用`ToString()` 方法。"
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


enum 的一个流行用例是从它的值中获取enum 的名称。

考虑一个现实世界的例子，通常我们会在数据库中存储enum 。也就是说，我们将只存储整数值。 

从数据库中读取enum 值后，我们必须将其转换回它的enum 名称。

在C#中，有**种方法可以从值中获得enum 的名称**。 

{{%toc%}}

## 解决方案1：使用`Enum.GetName()`

C#`Enum.GetName()` 函数接收两个参数enum 类型和值，并返回enum 名称。

以`LogLevel` Enum为例

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

现在我们将把enum 的值传递给`Enum.GetName()` ，以获得enum 的名称。 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

如果你使用的是C#`.Net 6` 版本，你可以只把enum 的值（投到enum ）传给`Enum.GetName()` 方法。

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## 解决方案2：使用类型转换

另一种方法是，使用铸造法将enum 的值转换为enum命名成员，然后使用`ToString()` 方法。

这是一个简单的方法，不使用任何`C# Enum` 的内置函数。

首先将enum 值转换为enum命名成员，然后使用`ToString()` 方法。

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## 摘要

在本教程中，我们学习了在c#中获取enum 名称值的不同方法。 

1.通过将enum 的类型和值参数传递给`Enum.GetName()` 方法。
2.并通过使用类型转换到相应的enum 类型。 
