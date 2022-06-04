+++
title="How to Get `int` value from `Enum` in C# with examples"
summary="To get `int` value from `enum` in C#, cast the enum variable to integer."
keywords=["int value from enum in C#,Convert string to enum in C#"
]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To get `int` value from `enum` in C#, cast the `enum` variable to integer.

{{%toc%}}

## Solution 1: Use Type cast to get `int` value from `enum`

The default underlying type for `enums` in C# is `Int`.

So we can type cast the `enum` to `int` to get the integer value from enum in C#.

We will take an example to understand it further.

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
```

Now we will cast enum values to integer values.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Solution 2: Use `Convert.ToInt32()` method to get the integer value from enum

Or we can use `Convert.ToInt32()` to method to convert an `enum` to integer as shown below.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Get the `enum` value of different underlying types

`Enums` in C# can have different underlying types. 

If C# enum is declared as a `uint`, `long`, or `ulong` we should cast it to the corresponding type of the `enum`.

Consider the below example of `Stars` enum, which has a type `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```