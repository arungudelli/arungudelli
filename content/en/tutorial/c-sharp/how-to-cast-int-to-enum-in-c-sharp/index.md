+++
title   ="2 ways to convert/cast int to enum in C#"
summary ="There are 2 ways To cast int to enum in C# 1. Using C# explicit type casting. 2. Using Enum.ToObject() method."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


There are 2 ways To convert or cast `int` to `enum` in C#

1. Using C# explicit type casting.
2. Using `Enum.ToObject()` method

{{%toc%}}

## Solution 1: Using C# explicit type casting

The simple way to convert `int` to `enum` in C# is to use explicit type casting.

Let's go through an example to understand it further.

We have an `enum` type called `LogLevel`, which represents different levels of logging.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Explicit casting done by placing the `enum` type in parentheses in front of the `int` value.

But there is a problem with above **C# `int` to `enum` conversion**.

What if the `int` value does not exists in the C# `Enum` variable?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

It will not throw any exception.

So it's better to check if the `int` value exists in `C# Enum` before casting it to the integer.

## Check if an integer exists or not in `C# enum` variable

To get the all integer values in `C# Enum` we can use `Enum.GetValues` method.

Convert them to `C#` list, so that we can use `list.Contains()` method to check if the given integer exist in `enum` variable.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
We can use `Enum.IsDefined()` method to check if converted integer value exist in the given `enum` type.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solution 2: Use `Enum.ToObject()` method

We can use `C# Enum.ToObject()` method, convert `int` value to `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





