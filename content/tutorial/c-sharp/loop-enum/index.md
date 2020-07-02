+++
title="How to loop enum values in C#"
summary="Steps to loop enum values in C# 1.Use C# Enum.GetValues() method to get all possible values of Enum.2.Then, enumerate or loop the enum values using foreach or for loop."
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

Steps to loop enum values in C#

1. Use C# Enum.GetValues() method to get all possible values of Enum.
2. Then, enumerate or loop the enum values using foreach or for loop. 

{{%toc%}}

## Loop Enum Values in C# 

We will take an example to understand it further.

I have created a Days enum as shown below.

```
public enum Days
{
        Monday=1,
        Tuesday=2,
        Wednesday=3,
        Thursday=4,
        Friday=5,
        Saturday=6,
        Sunday=7
}
```

First we will get all possible values of the enum in C# using Enum.GetValues() method 

```
 var days = Enum.GetValues((typeof(Days)));
```

Now we will loop through enum values in C# and print them in console using foreach loop

```
foreach (Days day in (Days[])days)
{
    Console.WriteLine(day);
}

Output:

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

```

Casting to Array is not necessary but it does give some performance benefit.

And to loop all enum integer values we can use Enum.GetHashCode() method

```
foreach (Days day in (Days[])days)
{
 Console.WriteLine(day.GetHashCode());
}

Output:
1 
2
3
4
5
6
7
```

Or we can simply cast the enum to appropriate type i.e, (int)day.

[Get int value from Enum](https://www.arungudelli.com/tutorial/c-sharp/get-int-value-from-enum-c-sharp-example/)

## Loop Enum Names in C# 

To get all possible enum names in c# we can use Enum.GetNames() methods as shown below

```
var daysNames = Enum.GetNames(typeof(Days));
```

Enum.GetNames() method will return list of strings which contain all enum names.
We can loop them further to know all possible enum names.
