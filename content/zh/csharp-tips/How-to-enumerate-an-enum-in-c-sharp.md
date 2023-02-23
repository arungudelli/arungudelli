---
title: "如何enumerate C#enum"
description: " enum erate C#的不同方法enum ，并举例说明。"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums在`C#` 语言中被广泛使用。 

在enumerateenum ，有4种方法可以在`C#` 。 

1.在.Net 5及以上版本中使用`C# Enum.GetValues()` 。
2.在旧的.Net版本中使用`C# Enum.GetValues()` 。
3.使用`C# Enum.GetNames()` ，将enum，将enum 的名称作为字符串。
4.使用`Linq`

让我们通过一个例子来进一步了解它。 

首先，我们将创建一个C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

该 `enum`代表不同类型的日志级别。

现在我们将看到不同的方式来enumerate the `C# enum`.

## 在.Net 5及以上版本中使用`C# Enum.GetValues()` 通用方法

如果你使用最新版本的`.Net` ，即`.Net 5` 及以上版本，你可以使用通用版本的`Enum.GetValues` 方法来enumerate the 。 `C# enum`.

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

新的通用版本的`Enum.GetValues` 返回数组的enum 值。 

此外，我们还可以使用`for` 或`foreach` 语句来列出 `C# enum`名称。 

由于数组包含 `enum`类型，我们需要使用`ToString()` 方法将其转换为字符串。

## 在旧的.Net版本中使用`C# Enum.GetValues()` 。

在旧版本的`.Net` ，没有可用的通用方法，`Enum.GetValues()` 方法。 

你需要把`typeof()` enum 作为一个参数传给`Enum.GetValues()` 方法。 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
它返回enum 类型的值`System.Array` ，然后我们可以使用`foreach` 语句来循环浏览这些 `C# enum`名称。

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

## 使用`C# Enum.GetNames()` ，将enum，将enum ，将名字作为字符串。 

`C# Enum.GetValues()` 方法返回数组的enum 类型。 

这就是为什么我们在将enum 名称打印在控制台之前将其转换为字符串。

使用`C# Enum.GetNames()` 方法，我们可以将enumerateenum 名称作为字符串，这样就不需要将它们转换为字符串。

如果你使用的是`.Net 5` 及以上，你可以使用通用的`C# Enum.GetNames()` 函数。

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

在旧版本中，我们需要传递`typeof()` enum 参数。

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

因此，如果你想把enumerate names作为字符串，我们可以使用`C# Enum.GetNames()` 方法。

## 使用`Linq`

我们可以使用`Linq forEach` 方法来enumerate C#enum ，在`Enum.GetValues()` 和`Enum.GetNames()` 方法的帮助下。

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

在本教程中，我们学习了在C#中使用`Enum.GetValues()` 和`Enum.GetNames()` 方法，enumerateenum 。










