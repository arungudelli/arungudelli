+++
title   ="如何在C#中把`int` 转换成`enum` "
summary ="要在C#中把`int` 投入到`enum` ，显式地把`enum` 变量投到整数。"
keywords=["在C#中把int转为枚举，在C#中把int转为枚举"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

要在C#中把`int` 转换成`enum` ，明确地输入把`enum` 变量转换成整数。

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

##解决方案1：使用`enum` 变量的显式类型转换

让我们通过一个例子来进一步了解它。

我们有一个名为`Days` 的`enum` 类型，它表示从星期一开始的工作日。

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

但是，上述**`int` 到`enum` 的转换有一个问题**。

如果`int` 的值不存在于C#的`Enum` 变量中，怎么办？

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

它不会抛出任何异常。

`Enum` 因此，在将其转换为整数之前，最好先检查`int` 中是否存在该值。

## 检查`enum` 变量中是否存在一个整数

为了获得C#`Enum` 中的所有整数值，我们可以使用`Enum.GetValues` 方法。

将它们转换成C#列表，这样我们就可以使用`list.Contains()` 方法来检查给定的整数是否存在于`enum` 变量中。

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
我们可以使用`Enum.IsDefined()` 方法来检查转换后的整数值是否存在于给定的`enum` 类型中。  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


##解决方案2：使用`Enum.ToObject()` 方法

我们可以使用`Enum.ToObject()` 方法，在C#中把`int` 值转换为`enum` 。

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





