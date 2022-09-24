
+++
title="How to get enum name from value in C#"
summary="There are Two ways To get enum name from value in C# 1. Use C# `Enum.GetName()` and pass enum value as parameter to get the name. 2. Convert enum value to the enumeration member using casting and then use `ToString()` method."
date='2022-03-16T00:00:00+0000'
lastmod='2022-09-23T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


One of the popular use case of enum is to get enum name from it's value.

Consider a real world example, generally we will store enum values in the data base. i.e, we will store only integer values. 

And after reading the enum value from the data base we have to convert it back to it's enum name.

There are **two ways to get enum name from value in C#** 

{{%toc%}}

## Solution 1: Using `Enum.GetName()`

C# `Enum.GetName()` function takes two parameters enum type and value and returns the enum name.

Take an example of `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Now we will pass enum value to the `Enum.GetName()` to get the enum name. 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

If you are using C# `.Net 6` version, you can pass only enum value(cast to enum) to the `Enum.GetName()` method.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Solution 2: Using type casting

Another way is to, Convert enum value to the enumeration member using casting and then use `ToString()` method.

This is a simple way which does not use any `C# Enum` built-in functions.

First convert enum value to the enumeration member and then use `ToString()` method.

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

## Summary

In this tutorial we learnt different ways to get enum name value in c#. 

1. By passing enum type and value parameters to the `Enum.GetName()` method
2. And by using type casting it to corresponding enum type. 
