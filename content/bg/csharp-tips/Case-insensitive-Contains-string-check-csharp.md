
---
title: "C# Проверка на низа Contains без отчитане на регистрите"
description: "В този урок ще научим различни начини за извършване на проверка на съдържащ се низ без отчитане на малки и големи букви в C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


В този урок научаваме различни начини за извършване на проверка на съдържащ се низ без отчитане на регистрите в C# 

Изглежда като прост проблем, но методът по подразбиране на C# `string.Contains()` е чувствителен към малки и големи букви 

И ако низът не е на български език, т.е. за други езици, не можем да сравняваме текста без отчитане на големината на буквите директно 

Двата низа трябва да са в една и съща култура и ние трябва да знаем езиковата култура.

В повечето случаи ще сравняваме низове само на английски език.

## Метод 1: Използване на метода C# `string.IndexOf()`.

Можем да използваме метода C# `string.IndexOf()`, за да направим проверка на съдържащите се в низа низове, без да се отчитат регистрите.

`IndexOf()` методът приема параметър `StringComparison.OrdinalIgnoreCase`, който указва типа на търсене, който да се използва за символите.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Метод 2: Използване на метода `string.Contains()` в .Net 5+ и .NET Core 2.0+

В последните версии на dot net, т.е. в .Net Core 2.0+ и .Net 5+. Методът `string.Contains()` има претоварен метод, който приема параметър `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Метод 3: Използване на метода `Regex.IsMatch()` 

Можем да използваме регулярни изрази, за да направим проверка на съдържащите се низове без значение на регистъра.

Ако сте запознати с `Regex`, използвайте метода `Regex.IsMatch()` и за проверка за нечувствителност на регистъра подайте параметъра `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Метод 4: Използване на `.ToUpper()` &amp `.ToLower()`

Ако низовете са на английски език и производителността не е проблем, можем да конвертираме двата низа в един и същи падеж, след което да направим проверка за наличие на низ.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Проверка на съдържания без отчитане на регистъра за други езици

Нечувствителността към малки и големи букви зависи от езика 

Например в английския език `I` е версия на `i` с главни букви.

Докато в турския език версията с главни букви на `i` е непознатият символ `İ`.

За да извършим проверка на низ без значение на големината на буквите, трябва да използваме обекта `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Създадох обект `CultureInfo` за турския език. И сравних двата низа с помощта на `CompareInfo`, както е показано по-долу.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Най-добрият начин за извършване на проверка на съдържащите се низове без отчитане на регистрите

Ако използвате последната версия на `.Net`, използвайте метода `string.Contains()`.

В противен случай се придържайте към метода `string.IndexOf()`.

Не предпочитайте методите `.ToUpper()` или `To.Lower()`, тъй като те могат да доведат до проблеми с производителността.

Използвайте обекта `CultureInfo` за низове на други езици.

