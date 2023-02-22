---
title: "How to loop/enumerate C# enum"
description: "Different ways to loop or enumerate C# enum with examples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enums are widely used in `C#` language. 

And there are 4 ways to loop or enumerate enum in `C#`. 

1. Using `C# Enum.GetValues()` in .Net 5 & above.
2. Using `C# Enum.GetValues()` in older .Net versions.
3. Using `C# Enum.GetNames()` to enumerate enum names as strings.
4. Using `Linq`

Let's go through an example to understand it further. 

First we will create a C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

The `enum` represents different types of logging levels.

Now we will see different ways to enumerate the `C# enum`.

## Using `C# Enum.GetValues()` Generic method in .Net 5 & above

If you are using latest version of `.Net` , i.e., `.Net 5` and above you can use generic version for the `Enum.GetValues` method to loop through the `C# enum`.

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

The new generic version of `Enum.GetValues` returns the array of enum values. 

And further we can use `for` or `foreach` statements to enumerate the `C# enum`. 

As the array contains the `enum` type we need to convert it to the string using `ToString()` method.

## Using `C# Enum.GetValues()` in older .Net versions.

In the older versions of `.Net` there is no generic method available for `Enum.GetValues()` method. 

You need to pass `typeof()` enum as a parameter to `Enum.GetValues()` method. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
And it returns enum values of type `System.Array` and further we can use `foreach` statement to loop through the C# enum.

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

If you want `IEnumerable` result, we can further cast the `Enum.GetValues()` method.

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

## Using `C# Enum.GetNames()` to enumerate enum names as strings 

`C# Enum.GetValues()` method returns array of enum types. 

That's why we converted enum values to string before printing them in the console.

Using `C# Enum.GetNames()` method we can enumerate enum names as strings, so that it's not required to convert them to strings.

If you are using `.Net 5` & above, You can use generic `C# Enum.GetNames()` function.

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

In the older versions we need to pass `typeof()` enum parameter.

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

So If you want to loop enum names as strings we can use `C# Enum.GetNames()` method.

## Using `Linq`

We can use `Linq forEach` method to enumerate C# enum, with the help of `Enum.GetValues()` and `Enum.GetNames()` methods.

In `.Net 5` and above use the below code snippet.

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

In the older versions

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

## Summary

In this tutorial we learnt to loop through enum in C# using `Enum.GetValues()` and `Enum.GetNames()` method.










