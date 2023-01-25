+++
title   ="在C#中，有2种方法可以将int转换/cast到enum "
summary ="在C#中，有2种方法可以将int转换成enum 1.使用C#显式类型转换。 2.使用Enum.ToObject()方法。"

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


有2种方法可以将`int` 转换为 `enum`在C#中

1.使用C#显式类型转换。
2.使用`Enum.ToObject()` 方法

{{%toc%}}

## 解决方案1：使用C#显式类型铸造

将`int` 转换为 `enum`的简单方法是使用显式类型转换。

让我们通过一个例子来进一步了解它。

我们有一个 `enum`类型叫做`LogLevel` ，它代表不同级别的日志。

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

明确的铸造是通过将 `enum`类型放在`int` 值前面的括号里。

但是上述**C#`int` 到**的转换有一个问题。 `enum`转换**。

如果`int` 的值在C#`Enum` 变量中不存在怎么办？

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

它不会抛出任何异常。

`C# Enum` 因此，在将其转换为整数之前，最好先检查`int` 中是否存在该值。

## 检查一个整数是否存在于 `C# enum`变量

要获得`C# Enum` 中的所有整数值，我们可以使用`Enum.GetValues` 方法。

将它们转换成`C#` 列表，这样我们就可以使用`list.Contains()` 方法来检查给定的整数是否存在于 `enum`变量中。

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
我们可以使用`Enum.IsDefined()` 方法来检查转换后的整数值是否存在于给定的 `enum`类型中是否存在。  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 解决方案2：使用`Enum.ToObject()` 方法

我们可以使用`C# Enum.ToObject()` 方法，将`int` 值转换为 `enum`在C#中。

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





