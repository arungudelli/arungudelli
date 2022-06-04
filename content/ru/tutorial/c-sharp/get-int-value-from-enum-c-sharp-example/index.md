+++
title   ="Как получить значение `int` из `Enum` в C# с примерами"
summary ="Чтобы получить значение `int` из `enum` в C#, приведите переменную enum к целому числу."
keywords=["int value from enum in C#,Convert string to enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Чтобы получить значение `int` из `enum` в C#, приведите переменную `enum` к целому числу.

{{%toc%}}

## Решение 1: Используйте приведение типа для получения значения `int` из `enum`

Базовым типом по умолчанию для `enums` в C# является `Int`.

Поэтому мы можем привести тип `enum` к `int`, чтобы получить целочисленное значение из перечисления в C#.

Для дальнейшего понимания мы рассмотрим пример.

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

Теперь мы будем приводить значения перечислений к целочисленным значениям.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Решение 2: Используйте метод `Convert.ToInt32()` для получения целочисленного значения из enum

Или мы можем использовать метод `Convert.ToInt32()` to для преобразования `enum` в целое число, как показано ниже.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Получение значения `enum` различных базовых типов

`Enums` в C# могут иметь различные базовые типы 

Если в C# перечисление объявлено как `uint`, `long`, или `ulong`, мы должны привести его к соответствующему типу `enum`.

Рассмотрим следующий пример перечисления `Stars`, которое имеет тип `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```