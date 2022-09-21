+++
title="Как проверить, является ли строка числом в C#"
summary="Как проверить, является ли строка числом в c# 1.Объявление целочисленной переменной. 2.Передайте строку методам `int.TryParse()` или `double.TryParse()` с помощью переменной `out`. 3.Если строка является числом, метод `TryParse` вернет true. И присвоит значение объявленной целочисленной `out` переменной."
keywords=["Проверка, является ли строка числом в C#"]
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

Шаги для проверки того, является ли строка числом в C#

1. Объявите целочисленную переменную.
2. Передайте строку методам `int.TryParse()` или `double.TryParse()` с помощью переменной `out`.
3. Если строка является числом, метод `TryParse` вернет true. И присвоит объявленной целочисленной `out` значение.

{{%toc%}}

## Проверка, является ли строка числом или нет в C# 

Например, у нас есть строковая переменная "123", и если вы хотите проверить, является ли она числовой, используйте приведенный ниже код на C#.

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

Начиная с C# 7 мы можем объявить переменную [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) в самом методе TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Проблема с приведенным выше методом `int.TryParse` заключается в том, что он не может проверить отрицательные значения строковых чисел.

## Проверка отрицательного числа строк в C# 

Для проверки отрицательных значений числа строк мы можем использовать метод C# `double.TryParse()`.

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

## Лучший способ проверить, является ли строка числом в C# 

Для проверки того, является ли строка числом, всегда используйте метод `double.TryParse()`, поскольку он может проверять как положительные, так и отрицательные числа.