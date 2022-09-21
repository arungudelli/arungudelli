+++
title="Как да проверим дали даден низ е число в C#"
summary="Стъпки за проверка дали даден низ е число в C# 1.Декларирайте променлива с цяло число. 2.Предайте низ на методите `int.TryParse()` или `double.TryParse()` с помощта на променливата `out`. 3.Ако низът е число, методът `TryParse` ще върне true. И присвоява стойност на декларираната стойност на цялото число `out`."
keywords=["проверка дали даден низ е число в C#"]
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

Стъпки за проверка дали даден низ е число в C#

1. Декларирайте променлива с цяло число.
2. Предайте низ на методите `int.TryParse()` или `double.TryParse()` с променливата `out`.
3. Ако символният низ е число, методът `TryParse` ще върне true. И присвоява стойност на декларираната стойност на цялото число `out`.

{{%toc%}}

## Проверка дали даден низ е число или не в C# 

Например имаме променлива низ "123" и ако искате да проверите дали е число, използвайте следния код на C#.

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

От C# 7 нататък можем да декларираме променлива [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) в самия метод TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Проблемът на горния метод `int.TryParse` е, че не може да проверява за отрицателни стойности на символни числа.

## Проверка за отрицателно число в низ в C# 

За да проверим за отрицателни стойности на символен низ, можем да използваме метода на C# `double.TryParse()`.

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

## Най-добрият начин да проверите дали низът е число в C# 

Винаги използвайте метода `double.TryParse()`, за да проверите дали даден низ е число, тъй като той може да проверява както положителни, така и отрицателни числа.