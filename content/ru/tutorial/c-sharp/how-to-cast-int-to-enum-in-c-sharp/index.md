+++
title   ="Как привести `int` к `enum` в C#"
summary ="Чтобы привести `int` к `enum` в C#, явно приведите переменную `enum` к целому числу."
keywords=["int to enum in C#, cast int to enum in C#"]
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

Чтобы привести `int` к `enum` в C#, явно приведите переменную `enum` к целому числу.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Решение 1: Использование явного приведения типа переменной `enum` 

Давайте рассмотрим пример, чтобы понять это дальше.

У нас есть тип `enum` под названием `Days`, который представляет дни недели, начиная с понедельника.

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

Но существует проблема с приведенным выше ** преобразованием`int` в `enum` **.

Что если значение `int` не существует в переменной C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Это не приведет к возникновению исключения.

Поэтому лучше проверить, существует ли значение `int` в `Enum`, прежде чем приводить его к целому числу.

## Проверьте, существует или нет целое число в переменной `enum` 

Чтобы получить все целочисленные значения в C# `Enum`, мы можем использовать метод `Enum.GetValues`.

Преобразуйте их в список C#, чтобы с помощью метода `list.Contains()` проверить, существует ли данное целое число в переменной `enum`.

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
Мы можем использовать метод `Enum.IsDefined()`, чтобы проверить, существует ли преобразованное целочисленное значение в данном типе `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Решение 2: Используйте метод `Enum.ToObject()` 

Мы можем использовать метод `Enum.ToObject()`, чтобы преобразовать значение `int` в `enum` в C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





