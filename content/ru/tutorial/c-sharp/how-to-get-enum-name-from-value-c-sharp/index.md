
+++
title="Как получить имя enum из значения в C#"
summary="Есть два способа получить имя enum из значения в C# 1. Использовать C# `Enum.GetName()` и передать значение enum в качестве параметра для получения имени. 2. Преобразовать значение enum в член enumс помощью кастинга, а затем использовать метод `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Одним из популярных случаев использования enum является получение имени enum из его значения.

Рассмотрим пример из реального мира, обычно мы храним в базе данных значения enum, т.е. только целочисленные значения 

И после чтения значения enum из базы данных мы должны преобразовать его обратно в его имя enum.

Существует **два способа получить имя enum из значения в C#** 

{{%toc%}}

## Решение 1: Использование `Enum.GetName()`

C# `Enum.GetName()` функция принимает два параметра enum тип и значение и возвращает имя enum.

Возьмем пример `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Теперь мы передадим значение enum в `Enum.GetName()`, чтобы получить имя enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Если вы используете версию C# `.Net 6`, вы можете передать методу `Enum.GetName()` только значение enum (приведенное к enum).

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Решение 2: Использование приведения типов

Другой способ заключается в том, чтобы преобразовать значение enum в член enumс помощью приведения, а затем использовать метод `ToString()`.

Это простой способ, который не использует никаких `C# Enum` встроенных функций.

Сначала преобразуйте значение enum в член enumeration, а затем используйте метод `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Резюме

В этом уроке мы изучили различные способы получения значения имени enum в c# 

1. Передавая enum параметры типа и значения в метод `Enum.GetName()` 
2. И используя приведение типа к соответствующему типу enum 
