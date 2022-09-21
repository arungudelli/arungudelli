+++
title="How to get enum name from value in C#"
summary="There are Two ways To get enum name from value in C# 1. Use C# Enum.GetName() and pass enum value as parameter to get the name.2. Convert enum value to the enumeration member using casting and then use ToString() method."
keywords=["get enum name from value c#"]
type='post'
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

There are Two ways To get enum name from value in C#

1. Use C# Enum.GetName() and pass enum value as parameter to get the name.
2. Convert enum value to the enumeration member using casting and then use ToString() method.

Generally, we will store enum value in the database. So in the code we have to convert integer enum value back to the string name. 

We will take an example to understand it further. 


{{%toc%}}

## Solution 1: Use C# Enum.GetName() to get the enum name from value

C# Enum.GetName() function takes two parameters enumType, value and returns the enum name

Take an example of LogLevel Enum

```
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Now we will pass a value to the Enum.GetName() to get the enum name. 


```
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");
```
Here is the output:

```
The name of enum value : 1 is ERROR
```

If you are using C# .Net 6 version, you can pass only enum value(cast to enum) to the Enum.GetName() method.

```
var enumName6 = Enum.GetName((LogLevel)enumValue);

```

## Solution 2: Use Simple Cast to get the enum name from value

This is a simple way which does not use any C# Enum built-in functions.

First convert enumValue to the enumeration member and then use ToString() method.

```
var enumValue = 2;
//Convert enumValue

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

```

Here is the output

```
The name of enum value : 2 is WARN
```