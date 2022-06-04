+++
title   ="Как да получите стойността на `int` от `Enum` в C# с примери"
summary ="За да получите стойността на `int` от `enum` в C#, превърнете променливата enum в цяло число."
keywords=["Стойност int от enum в C#,Конвертиране на низ в enum в C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

За да получите стойността на `int` от `enum` в C#, превърнете променливата `enum` в цяло число.

{{%toc%}}

## Решение 1: Използвайте Type cast, за да получите стойността на `int` от `enum`

Основният тип по подразбиране за `enums` в C# е `Int`.

Така че можем да направим type cast на `enum` към `int`, за да получим целочислена стойност от enum в C#.

Ще разгледаме един пример, за да го разберем по-добре.

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

Сега ще превърнем стойностите на enum в целочислени стойности.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Решение 2: Използвайте метода `Convert.ToInt32()`, за да получите целочислена стойност от enum

Или можем да използваме метода `Convert.ToInt32()` to, за да преобразуваме `enum` в цяло число, както е показано по-долу.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Получаване на стойността на `enum` на различни основни типове

`Enums` в C# могат да имат различни основни типове 

Ако C# енумът е деклариран като `uint`, `long` или `ulong`, трябва да го превърнем в съответния тип на `enum`.

Разгледайте примера по-долу за енум `Stars`, който има тип `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```