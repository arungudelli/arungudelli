+++
title   ="2 ways to convert/cast int toenum in C#"
summary ="There are 2 ways To cast int toenum in C# 1.C# の明示的な型キャストを使用する。 2.Enum.ToObject()メソッドを使用する。"

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


`int` を変換またはキャストするには、2つの方法があります。 `enum`C# で

1.C#の明示的な型変換を使用する。
2.`Enum.ToObject()` メソッドを使用する

{{%toc%}}

## 解決策1：C#の明示的な型キャスティングを利用する

C#で`int` を `enum`に変換する簡単な方法は、明示的な型キャスティングを使用することです。

例を見て、さらに理解を深めましょう。

私たちは、 という型を持っています。 `enum``LogLevel`という型があり、これはロギングの異なるレベルを表します。

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

明示的なキャスティングを行うには `enum`の型を括弧で囲んで，`int` の値の前に置くことによって行われます。

しかし、上記の **C#`int` への変換には問題があります。 `enum`変換**に問題があります。

もし、`int` の値が C#`Enum` の変数に存在しない場合はどうなるのでしょうか？

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

例外はスローされません。

ですから、`int` の値を整数にキャストする前に、`C# Enum` に存在するかどうかをチェックする方がよいでしょう。

## に整数が存在するかどうかをチェックする。 `C# enum`変数

`C# Enum` にあるすべての整数値を取得するには、`Enum.GetValues` メソッドを使用します。

それらを`C#` のリストに変換し、`list.Contains()` メソッドで与えられた整数が変数に存在するかどうかをチェックします。 `enum`変数に存在するかどうかを調べることができます。

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
`Enum.IsDefined()` メソッドを使って，変換された整数値が与えられた型に存在するかどうかをチェックすることができます。 `enum`型に存在するかどうかを調べることができます。  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 解決策2：`Enum.ToObject()` メソッドを使用する

`C# Enum.ToObject()` メソッドを使用し、`int` の値を `enum`に変換することができます。

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





