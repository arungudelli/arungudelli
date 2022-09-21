---
title: "C# Case insensitive Contains string check"
description: "In this tutorial we learn different ways to do case insensitive string contains check in C#"
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---


In this tutorial we learn different ways to do case insensitive string contains check in C#. 

It looks like a simple problem, but the default C# `string.Contains()` method is case sensitive. 

And if the string is not in English language i.e., for other languages, we can't compare text case insensitive directly. 

The both strings should be in same culture and We should know the language culture.

Most of the times we will compare strings in English language only.

## Method 1: Using C# `string.IndexOf()` method.

We can use C# `string.IndexOf()` Method to do case insensitive string contains check.

`IndexOf()` method accepts `StringComparison.OrdinalIgnoreCase` parameter, which specify the type of search to use for the characters.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Method 2: Using `string.Contains()` method in .Net 5+ & .NET Core 2.0+

In latest versions of dot net, i.e., in .Net Core 2.0+ and .Net 5+. The `string.Contains()` method has an overloaded method which accepts `StringComparison` parameter.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Method 3: Using `Regex.IsMatch()` method

We can use regular expressions to do case insensitive contains string check.

If you are familiar with `Regex`, Use `Regex.IsMatch()` method and to check for case insensitive pass `RegexOptions.IgnoreCase` parameter. 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Method 4: Using `.ToUpper()` & `.ToLower()`

If the strings are in English language and the performance is not an issue, we can convert both string to same case then do the string contains check.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check for other languages

Case insensitivity is language dependent. 

For example, in the English language `I` is the upper case version of `i`.

Whereas in the Turkish language upper case version of `i` is the unfamiliar character `İ`.

To do the case insensitive string check we need to use `CultureInfo` object.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

I have created `CultureInfo` object for turkish language. And compared both strings using `CompareInfo` as shown below.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Best way to do Case insensitive Contains string check

If you are using latest version of `.Net` use `string.Contains()` method.

Otherwise stick with `string.IndexOf()` method.

Do not prefer `.ToUpper()` or `To.Lower()` method as they may lead to performance problems.

Use `CultureInfo` object for other languages strings.

