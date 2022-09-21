
---
title: "C# 大文字小文字を区別しない 含有文字列チェック"
description: "このチュートリアルでは、C#で大文字小文字を区別しない含有文字列チェックを行うためのさまざまな方法を学びます。"
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---



このチュートリアルでは、C＃で大文字と小文字を区別しない文字列が含まれているチェックを行うためのさまざまな方法を学習します。 

それは簡単な問題のように見えますが、デフォルトのC＃の`string.Contains()` メソッドは、大文字と小文字を区別します。 

そして、文字列が英語でない場合、すなわち、他の言語のために、我々は直接大文字と小文字を区別してテキストを比較することはできません。 

両方の文字列は同じ文化である必要があり、我々は、言語文化を知っている必要があります。

ほとんどの場合、英語だけの文字列を比較することになります。

## 方法1: C#`string.IndexOf()` メソッドを使用する。

C#`string.IndexOf()` メソッドを使用すると、大文字と小文字を区別せずに文字列が含まれているかどうかをチェックすることができます。

`IndexOf()` メソッドは、`StringComparison.OrdinalIgnoreCase` パラメータを受け取ります。これは、文字に対して使用する検索の種類を指定します。

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## 方法2:`string.Contains()` メソッドを .Net 5+ &amp; .NET Core 2.0+ で使用する。

ドットネットの最新バージョン、すなわち.Net Core 2.0+と.Net 5+では、.Net Core 2.0+と.Net 5+では、。`string.Contains()` メソッドにはオーバーロードされたメソッドがあり、`StringComparison` パラメータを受け取ります。

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## 方法3:`Regex.IsMatch()` メソッドを使う

正規表現を使って、大文字小文字を区別しない含有文字列チェックを行うことができます。

`Regex` に慣れている人は`Regex.IsMatch()` メソッドを使い、`RegexOptions.IgnoreCase` パラメータを渡して大文字小文字を区別しないチェックをします。 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## 方法4:`.ToUpper()` &amp;を使う`.ToLower()`

文字列が英語で、パフォーマンスに問題がない場合、両方の文字列を同じケースに変換してから、文字列が含まれているかどうかをチェックすることができます。

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# 大文字小文字を区別しない他の言語での含有率チェック

大文字小文字の区別は言語に依存します。 

例えば、英語では`I` は`i` の大文字バージョンです。

一方、トルコ語では、`i` の大文字バージョンは、見慣れない文字である`İ` 。

大文字小文字を区別しない文字列チェックを行うには、`CultureInfo` オブジェクトを使用する必要があります。


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

私はトルコ語用に`CultureInfo` オブジェクトを作成しました。そして、`CompareInfo` を使って、以下のように両方の文字列を比較しました。

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## 大文字小文字を区別せずに文字列をチェックする最良の方法

最新版の`.Net` を使用している場合は、`string.Contains()` メソッドを使用してください。

そうでない場合は、`string.IndexOf()` の方法をお使いください。

`.ToUpper()` や`To.Lower()` の方法は、パフォーマンスの問題を引き起こす可能性があるため、好まないでください。

他の言語の文字列には、`CultureInfo` オブジェクトを使用してください。

