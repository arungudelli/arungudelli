+++
title   ="2 способа преобразовать/привести int к enum в C#"
summary ="Есть 2 способа Привести int к enum в C# 1. Использование явного приведения типов в C#. 2. Использование метода Enum.ToObject()."

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


Существует 2 способа преобразования или приведения `int` в `enum` в C#

1. Использование явного приведения типов в C#.
2. Использование метода `Enum.ToObject()` 

{{%toc%}}

## Решение 1: Использование явного приведения типов в C#

Простой способ преобразования `int` в `enum` в C# является использование явного приведения типов.

Давайте рассмотрим пример, чтобы понять это подробнее.

У нас есть `enum` тип `LogLevel`, который представляет различные уровни протоколирования.

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

Явное приведение выполняется путем помещения `enum` тип в круглых скобках перед значением `int`.

Но существует проблема с приведенным выше **C# `int` в `enum` преобразование**.

Что если значение `int` не существует в переменной C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Это не приведет к возникновению исключения.

Поэтому лучше проверить, существует ли значение `int` в `C# Enum`, прежде чем приводить его к целому числу.

## Проверьте, существует или нет целое число в `C# enum` переменная

Чтобы получить все целочисленные значения в `C# Enum`, мы можем использовать метод `Enum.GetValues`.

Преобразуйте их в список `C#`, чтобы с помощью метода `list.Contains()` проверить, существует ли данное целое число в переменной `enum` переменной.

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
Мы можем использовать метод `Enum.IsDefined()`, чтобы проверить, существует ли преобразованное целочисленное значение в данном `enum` типе.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Решение 2: Используйте метод `Enum.ToObject()` 

Мы можем использовать метод `C# Enum.ToObject()`, чтобы преобразовать значение `int` в значение `enum` в C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





