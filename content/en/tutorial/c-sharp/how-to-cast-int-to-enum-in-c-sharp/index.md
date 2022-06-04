+++
title="How to cast `int` to `enum` in C#"
summary="To cast `int` to `enum` in C#, explicitly type cast the `enum` variable to integer."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To cast `int` to `enum` in C#, explicitly type cast the `enum` variable to integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Solution 1: Using explicit type casting of `enum` variable

Let's go through an example to understand it further.

We have an `enum` type called `Days`, which represents week days starting from Monday.

```
public enum Days
{
        Monday,  
        Tuesday,  
        Wednesday,  
        Thursday,  
        Friday,  
        Saturday,  
        Sunday
}

int dayInteger = 6;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//Monday
```

But there is a problem with above **`int` to `enum` conversion**.

What if the `int` value does not exists in the C# `Enum` variable?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

It will not throw any exception.

So it's better to check if the `int` value exists in `Enum` before casting it to the integer.

## Check if an integer exists or not in `enum` variable

To get the all integer values in C# `Enum` we can use `Enum.GetValues` method.

Convert them to C# list, so that we can use `list.Contains()` method to check if the given integer exist in `enum` variable.

```
var intValue = 100;
var enumValues = Enum.GetValues(typeof(Days)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
  Console.WriteLine("We can Cast int to Enum");  
   Days day = (Days) intValue;
}else{
  Console.WriteLine("Cannot Cast int to Enum");
}

```
We can use `Enum.IsDefined()` method to check if converted integer value exist in the given `enum` type.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solution 2: Use `Enum.ToObject()` method

We can use `Enum.ToObject()` method, convert `int` value to `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





