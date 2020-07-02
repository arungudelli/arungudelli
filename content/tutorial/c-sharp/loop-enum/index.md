+++
title="How to loop or get enum names and values in C#"
summary="Steps to loop or get enum names & values in C# 1.Use C# Enum.GetValues() method to get all possible values of Enum.2.Then, enumerate or loop the enum values using foreach or for loop."
keywords="['loop enum c#','enumarate enum in c#']"
type='post'
date='2020-07-01T18:08:51+0000'
lastmod='2020-07-01T18:08:51+0000'
draft='false'
authors=['admin']
[image]
caption='How to loop enum values in C#'
focal_point=''
preview_only=false
+++

Steps to loop or get enum names and values in C#

1. Use C# Enum.GetValues() method to get all possible values of Enum.
2. And to get all names of enum entries Use C# Enum.GetNames().
2. Then, enumerate or loop the C# enum names or values using foreach or for loop. 

{{%toc%}}

## Loop or Get Enum Values using C# Enum.GetValues() 

We will take an example to understand it further.

I have created a Log level enum which contains ERROR,WARN,INFO and DEBUG levels as shown below.

```
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

First we will get all possible values of the enum in C# using Enum.GetValues() method 

```
 var enumValues = Enum.GetValues((typeof(LogLevel)));
```

Now we will loop through enum values in C# and print them in console using foreach loop

```
foreach (LogLevel enumValue in (LogLevel[])enumValues)
{
    Console.WriteLine(enumValue);
}

Output:

ERROR 
WARN 
INFO 
DEBUG

```

Casting to Array is not necessary but it does give some performance benefit.

And further to loop all enum integer values we can use Enum.GetHashCode() method

```
foreach (LogLevel enumValue in (LogLevel[])enumValues)
{
    Console.WriteLine(enumValue.GetHashCode());
    //or
    //Console.WriteLine((int)enumValue);
}

Output:
1 
2
3
4
```

Or we can simply cast the enum to appropriate type i.e, (int)enumValue.

[Get int value from Enum](https://www.arungudelli.com/tutorial/c-sharp/get-int-value-from-enum-c-sharp-example/)

Further we can use C# linq to get values of C# enum as shown below 

```
var enumValues = Enum.GetValues(typeof(LogLevel))
                .Cast<LogLevel>()
                .OrderBy(value =>(int)value);

```

## Loop or Get Enum Names using C# Enum.GetNames() 

To get all possible enum names in c# we can use Enum.GetNames() method as shown below

```
var enumNames = Enum.GetNames((typeof(LogLevel)));
```

Enum.GetNames() method will return list of strings which contain all enum names.
We can loop them further to know all possible enum names.

```
foreach (string enumName in enumNames)
{
    Console.WriteLine(enumName);
}
```

