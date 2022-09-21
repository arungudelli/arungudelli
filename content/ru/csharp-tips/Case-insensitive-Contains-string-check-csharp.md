
---
title: "C# Проверка строки Contains без учета регистра"
description: "В этом уроке мы изучим различные способы проверки содержимого строки без учета регистра в C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


В этом руководстве мы изучаем различные способы выполнения нечувствительной к регистру проверки "строка содержит" в C# 

Это выглядит как простая проблема, но метод C# `string.Contains()` по умолчанию чувствителен к регистру 

И если строка не на английском языке, т.е. для других языков, мы не можем сравнивать текст без учета регистра напрямую 

Обе строки должны быть одной культуры, и мы должны знать культуру языка.

Чаще всего мы сравниваем строки только на английском языке.

## Метод 1: Использование метода C# `string.IndexOf()`.

Мы можем использовать метод C# `string.IndexOf()` для проверки содержания строки без учета регистра.

`IndexOf()` метод принимает параметр `StringComparison.OrdinalIgnoreCase`, который определяет тип поиска символов.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Метод 2: Использование метода `string.Contains()` в .Net 5+ &amp; .NET Core 2.0+

В последних версиях dot net, т.е. в .Net Core 2.0+ и .Net 5+. Метод `string.Contains()` имеет перегруженный метод, который принимает параметр `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Метод 3: Использование метода `Regex.IsMatch()` 

Мы можем использовать регулярные выражения для проверки строки contains без учета регистра.

Если вы знакомы с методом `Regex`, используйте метод `Regex.IsMatch()`, а для проверки на нечувствительность к регистру передайте параметр `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Метод 4: Использование `.ToUpper()` &amp `.ToLower()`

Если строки на английском языке и производительность не является проблемой, мы можем преобразовать обе строки в один регистр, а затем выполнить проверку на наличие строк.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Проверка содержимого без учета регистра для других языков

Нечувствительность к регистру зависит от языка 

Например, в английском языке `I` является версией `i`, написанной в верхнем регистре.

В то время как в турецком языке верхним регистром `i` является незнакомый символ `İ`.

Чтобы выполнить проверку строки без учета регистра, нам нужно использовать объект `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Я создал объект `CultureInfo` для турецкого языка. И сравнил обе строки с помощью `CompareInfo`, как показано ниже.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Лучший способ сделать проверку строк Contains без учета регистра

Если вы используете последнюю версию `.Net`, используйте метод `string.Contains()`.

В противном случае используйте метод `string.IndexOf()`.

Не используйте метод `.ToUpper()` или `To.Lower()`, так как они могут привести к проблемам с производительностью.

Для строк других языков используйте объект `CultureInfo`.

