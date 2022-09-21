+++
title="如何在C#中检查一个字符串是否是一个数字"
summary="在c#中检查一个字符串是否是一个数字的步骤 1.声明一个整数变量。 2.用`out` 变量将字符串传递给`int.TryParse()` 或`double.TryParse()` 方法。 3.如果字符串是一个数字，`TryParse` 方法将返回true。并为声明的整数`out` 值赋值。"
keywords=["在C#中检查一个字符串是否是数字"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

在C#中检查一个字符串是否为数字的步骤

1.声明一个整数变量。
2.用`out` 变量将字符串传递给`int.TryParse()` 或`double.TryParse()` 方法。
3.如果字符串是一个数字，`TryParse` 方法将返回true。并为声明的整数`out` 值赋值。

{{%toc%}}

## 在C#中检查一个字符串是否是一个数字 

例如，我们有一个字符串变量 "123"，如果你想检查它是否是数字，请使用下面的C#代码。

```
var stringNumber = "123";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is true and numericValue=123

var stringNumber = "123P";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is false and numericValue=0 default value

```

从C#7开始，我们可以在TryParse方法本身声明[out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/)变量。

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

上述`int.TryParse` 方法的问题是它不能检查负的字符串数字值。

## 在C#中检查负的字符串数字 

为了检查负的字符串值，我们可以使用C#的`double.TryParse()` 方法。

```
var negativeString = "-123";
double number;
if(double.TryParse(negativeString,out number)){
   if (number > 0){

   }else{
       //negative number 
   }   
}
```

## 在C#中检查字符串是否为数字的最佳方法 

总是使用`double.TryParse()` 方法来检查一个字符串是否是数字，因为它可以验证正数和负数。