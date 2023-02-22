---
title: "如何循环/枚举C#枚举"
description: "循环或枚举C#枚举的不同方式及实例"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

在`C#` 语言中，枚举被广泛使用。 

在`C#` ，有4种方法来循环或枚举枚举。 

1.在.Net 5及以上版本中使用`C# Enum.GetValues()` 。
2.在旧的.Net版本中使用`C# Enum.GetValues()` 。
3.使用`C# Enum.GetNames()` ，将枚举名称作为字符串列举。
4.使用`Linq`

让我们通过一个例子来进一步了解它。 

首先，我们将创建一个C#`enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

`enum` ，代表不同类型的日志级别。

现在我们将看到列举`C# enum` 的不同方式。

## 在.Net 5及以上版本中使用`C# Enum.GetValues()` 通用方法

如果你使用最新版本的`.Net` ，即`.Net 5` 及以上版本，你可以使用通用版本的`Enum.GetValues` 方法来循环浏览`C# enum` 。

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

新的通用版本的`Enum.GetValues` ，返回枚举值的数组。 

而进一步我们可以使用`for` 或`foreach` 语句来枚举`C# enum` 。 

由于数组包含`enum` 类型，我们需要使用`ToString()` 方法将其转换为字符串。

## 在旧的.Net版本中使用`C# Enum.GetValues()` 。

在旧版本的`.Net` ，没有可用的通用方法，`Enum.GetValues()` 方法。 

你需要把`typeof()` 枚举作为一个参数传给`Enum.GetValues()` 方法。 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
它返回`System.Array` 类型的枚举值，然后我们可以使用`foreach` 语句在C#的枚举中循环。

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

如果你想要`IEnumerable` 的结果，我们可以进一步使用`Enum.GetValues()` 方法。

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## 使用`C# Enum.GetNames()` ，将枚举名称作为字符串来列举 

`C# Enum.GetValues()` 方法返回枚举类型的数组。 

这就是为什么我们在将枚举值打印在控制台之前将其转换为字符串。

使用`C# Enum.GetNames()` 方法，我们可以将枚举名称作为字符串来列举，这样就不需要将它们转换为字符串。

如果你使用`.Net 5` 及以上，你可以使用通用的`C# Enum.GetNames()` 函数。

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

在旧版本中，我们需要传递`typeof()` 枚举参数。

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

因此，如果你想把枚举名称作为字符串进行循环，我们可以使用`C# Enum.GetNames()` 方法。

## 使用`Linq`

我们可以在`Enum.GetValues()` 和`Enum.GetNames()` 方法的帮助下，使用`Linq forEach` 方法来枚举C#枚举。

在`.Net 5` 及以上版本中使用下面的代码片段。

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

在旧版本中

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## 摘要

在本教程中，我们学习了在C#中使用`Enum.GetValues()` 和`Enum.GetNames()` 方法来循环浏览枚举。










