+++
title   ="2 начина за конвертиране/превръщане на int в enum в C#"
summary ="Има 2 начина за превръщане на int в enum в C# 1. Използване на явното хвърляне на типове в C#. 2. Използване на метода Enum.ToObject()."

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


Има 2 начина за преобразуване или превръщане на `int` в `enum` в C#

1. Използване на явното присвояване на типа в C#.
2. Използване на метода `Enum.ToObject()` 

{{%toc%}}

## Решение 1: Използване на изрично присвояване на типове в C#

Простият начин за преобразуване на `int` в `enum` в езика C# е да се използва изрично избиране на типа.

Нека разгледаме един пример, за да го разберем по-добре.

Имаме `enum` тип, наречен `LogLevel`, който представлява различни нива на регистриране.

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

Явното хвърляне се извършва чрез поставяне на `enum` тип в скоби пред стойността на `int`.

Но има проблем с горното **C# `int` към `enum` преобразуване**.

Какво става, ако стойността `int` не съществува в променливата C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Това няма да доведе до изключение.

Затова е по-добре да проверите дали стойността `int` съществува в `C# Enum`, преди да я превърнете в цяло число.

## Проверете дали цяло число съществува или не в `C# enum` променливата

За да получим всички целочислени стойности в `C# Enum`, можем да използваме метода `Enum.GetValues`.

Конвертираме ги в списък `C#`, за да можем да използваме метода `list.Contains()`, за да проверим дали даденото цяло число съществува в `enum` променлива.

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
Можем да използваме метода `Enum.IsDefined()`, за да проверим дали преобразуваната целочислена стойност съществува в дадената `enum` тип.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Решение 2: Използвайте метода `Enum.ToObject()` 

Можем да използваме метода `C# Enum.ToObject()`, като преобразуваме стойността на `int` в `enum` в C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





