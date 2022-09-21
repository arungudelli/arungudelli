+++
title   ="如何在C#中从`Enum` 中获取`int` 的值，并举例说明"
summary ="要想在C#中从`enum` ，获得`int` 的值，将枚举变量转换为整数。"
keywords=["在C#中从enum中获取int值，在C#中将字符串转换成enum"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

要在C#中从`enum` 中获得`int` 的值，请将`enum` 变量转换为整数。

{{%toc%}}

##解决方案1：使用类型转换来从`int` 值。`enum`

在C#中，`enums` 的默认基本类型是`Int` 。

所以我们可以将`enum` 类型转换为`int` ，以便在C#中从枚举中获得整数值。

我们将通过一个例子来进一步了解它。

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

现在，我们将把枚举值转换成整数值。

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

##解决方案2：使用`Convert.ToInt32()` 方法从枚举中获取整数值

或者我们可以使用`Convert.ToInt32()` to 方法将`enum` 转换为整数，如下所示。

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## 获取不同底层类型的`enum` 值

`Enums` 在C#中可以有不同的底层类型。 

如果C#枚举被声明为`uint`,`long`, 或`ulong` ，我们应该将其投递到相应的类型中，即`enum` 。

考虑下面的例子：`Stars` 枚举，它的类型是`long` 。

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```