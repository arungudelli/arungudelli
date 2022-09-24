
+++
title="How to getenum name from value in C#"
summary="There are Two ways To getenum name from value in C# 1.C#を使い、 。C#`Enum.GetName()` を使用し、enum の値をパラメータとして渡して名前を取得します。 2.enum の値をキャストでenumのエレーションメンバーに変換し、`ToString()` メソッドを使用する。"
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


enum のよくある使用例として、値からenum の名前を取得するものがあります。

実世界の例を考えてみましょう。一般的には、enum の値をデータベースに保存します。つまり、整数値のみを保存します。 

そして、データベースからenum の値を読み取った後、それをenum の名前に変換する必要があります。

C#で値からenum 名を取得する方法は2つあります**。 

{{%toc%}}

## 解決策1`Enum.GetName()`

C#`Enum.GetName()` 関数は、2つのパラメータenum 型と値を取り、enum 名を返します。

`LogLevel` Enumを例とする。

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

では、enum の値を`Enum.GetName()` に渡して、enum の名前を取得することにします。 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

C#版`.Net 6` を使っている場合は、enum の値（enum にキャスト）だけを`Enum.GetName()` メソッドに渡すことができます。

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## 解決策2：型キャストを利用する

もうひとつの方法は、enum の値をキャストでenumの変換メンバーに変換し、`ToString()` メソッドを使用する方法です。

この方法は、`C# Enum` の組み込み関数を使用しないシンプルな方法です。

まず、enum の値をenumeration メンバに変換し、`ToString()` メソッドを使用します。

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## まとめ

このチュートリアルでは、C#でenum の名前の値を取得するさまざまな方法について学びました。 

1.`Enum.GetName()` メソッドにenum 型と値のパラメータを渡すことによって
2.そして、それを対応するenum 型に型キャストすることによって。 
