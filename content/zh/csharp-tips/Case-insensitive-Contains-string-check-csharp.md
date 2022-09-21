
---
title: "C#不区分大小写的字符串包含检查"
description: "在本教程中，我们学习了在C#中进行不区分大小写的字符串包含检查的不同方法。"
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---



在本教程中，我们将学习在C#中进行不区分大小写的字符串包含检查的不同方法。 

这看起来是一个简单的问题，但是默认的C#`string.Contains()` 方法是区分大小写的。 

而如果字符串不是英语语言，即对于其他语言，我们不能直接比较文本的大小写不敏感。 

两个字符串应该在同一文化中，我们应该知道语言文化。

大多数情况下，我们只比较英语语言的字符串。

## 方法1：使用C#`string.IndexOf()` 方法。

我们可以使用C#`string.IndexOf()` 方法来做不分大小写的字符串包含检查。

`IndexOf()` 该方法接受`StringComparison.OrdinalIgnoreCase` 参数，该参数指定了要使用的字符搜索类型。

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## 方法2：在.Net 5+ &amp; .NET Core 2.0+中使用`string.Contains()` 方法。

在最新版本的dot net中，即在.Net Core 2.0+和.Net 5+中。`string.Contains()` 方法有一个重载方法，它接受`StringComparison` 参数。

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## 方法3：使用`Regex.IsMatch()` 方法

我们可以使用正则表达式来做不区分大小写的包含字符串检查。

如果你熟悉`Regex` ，使用`Regex.IsMatch()` 方法，并通过`RegexOptions.IgnoreCase` 参数来检查不区分大小写。 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## 方法4：使用`.ToUpper()` &amp;`.ToLower()`

如果字符串是英文，并且性能不是问题，我们可以将两个字符串转换成相同的大小写，然后进行字符串包含检查。

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C#对大小写不敏感的其他语言的包含检查

大小写不敏感是与语言有关的。 

例如，在英语中，`I` 是`i` 的大写版本。

而在土耳其语中，`i` 的大写版本是陌生的字符`İ` 。

为了进行不区分大小写的字符串检查，我们需要使用`CultureInfo` 对象。


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

我已经为土耳其语创建了`CultureInfo` 对象。并使用`CompareInfo` 比较这两个字符串，如下所示。

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## 做不区分大小写的包含字符串检查的最佳方法

如果你使用的是最新版本的`.Net` ，请使用`string.Contains()` 方法。

否则坚持使用`string.IndexOf()` 方法。

不要选择`.ToUpper()` 或`To.Lower()` 方法，因为它们可能导致性能问题。

对其他语言的字符串使用`CultureInfo` 对象。

