+++
title   ="Как да превърнем `int` в `enum` в C#"
summary ="За да превърнете `int` в `enum` в C#, изрично въведете cast на променливата `enum` в integer."
keywords=["int to enum in C#,cast int to enum in C#"]
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

За да превърнете `int` в `enum` в C#, изрично въведете cast на променливата `enum` в integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Решение 1: Използване на изрично присвояване на типа на променливата `enum` 

Нека разгледаме един пример, за да го разберем по-добре.

Имаме тип `enum`, наречен `Days`, който представя дните от седмицата, започващи от понеделник.

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

Но има проблем с горното ** преобразуване на`int` в `enum` **.

Какво става, ако стойността `int` не съществува в променливата `Enum` на C#?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Това няма да доведе до изключение.

Затова е по-добре да проверите дали стойността `int` съществува в `Enum`, преди да я превърнете в цяло число.

## Проверете дали в променливата `enum` съществува цяло число или не

За да получим всички целочислени стойности в C# `Enum`, можем да използваме метода `Enum.GetValues`.

Конвертираме ги в списък на C#, за да можем да използваме метода `list.Contains()`, за да проверим дали дадено цяло число съществува в променливата `enum`.

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
Можем да използваме метода `Enum.IsDefined()`, за да проверим дали преобразуваната целочислена стойност съществува в дадения тип `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Решение 2: Използвайте метода `Enum.ToObject()` 

Можем да използваме метода `Enum.ToObject()`, да преобразуваме стойността на `int` в `enum` в C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





