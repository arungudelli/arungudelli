+++
title="How to cast int to enum in C#"
summary="Casting int to enum in C#"
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2021-02-10T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To cast int to enum in C# use the below single line C# code

```
SampleEnum sample = (SampleEnum)IntVariable;
```

Let's go through an example to understand it further.

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

But there is a problem with above **int to enum casting**, what if the int value does not exists in the C# Enum variable?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

It will not throw any exception.

So it's better to check if the int value exists in Enum before casting it to the Enum.

To get the all integer values in C# Enum we can use `Enum.GetValues` method.

```
var intValue = 100;
var enumValues = Enum.GetValues(typeof(Days)).Cast<int>().ToList();

if(enumValues.Contains(100)){
  Console.WriteLine("We can Cast int to Enum");  
   Days day = (Days) intValue;
}else{
  Console.WriteLine("Cannot Cast int to Enum");
}

```





