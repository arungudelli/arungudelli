---
title: "How toenumerate C#enum"
description: " Different ways toenumerate C#enum with examples."
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`C#` 言語ではEnumが広く使われています。 

そして、enumerateenum in`C#` の4つの方法があります。 

1.`C# Enum.GetValues()` を .Net 5 以上で使用する。
2.古い.Netのバージョンで`C# Enum.GetValues()` を使用する。
3.`C# Enum.GetNames()` を使用して、enum enum の名前を文字列として消去する。
4.使用方法`Linq`

さらに理解するために例を見てみましょう。 

まず、C#の `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

があります。 `enum`は、さまざまなタイプのロギングレベルを表します。

今度は、enumerate のさまざまな方法について見ていきます。 `C# enum`.

## `C# Enum.GetValues()` .Net 5 以上で Generic メソッドを使用する

`.Net` の最新版、すなわち`.Net 5` 以上を使用している場合、`Enum.GetValues` メソッドに汎用版を使用して、enumを消去することができます。 `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

新しい汎用版`Enum.GetValues` は、enum の値の配列を返します。 

さらに、`for` または`foreach` ステートメントを使用して、名前をリストアップすることができます。 `C# enum`の名前をリストアップすることができます。 

配列は型を含んでいるので `enum`を含むので、`ToString()` メソッドを使って文字列に変換する必要があります。

## 古いバージョンの.Netでは、`C# Enum.GetValues()` 。

古いバージョンの`.Net` では、`Enum.GetValues()` メソッドで利用できるジェネリックメソッドがありません。 

`Enum.GetValues()` メソッドにパラメータとして`typeof()` enum を渡す必要があります。 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
そしてそれは`System.Array` 型のenum 値を返し、さらに`foreach` ステートメントを使って `C# enum`の名前をループすることができます。

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

もし、`IEnumerable` の結果が欲しいなら、さらに`Enum.GetValues()` メソッドをキャストすればよい。

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## `C# Enum.GetNames()` を使ってenumを消すenum 名前を文字列にする 

`C# Enum.GetValues()` メソッドはenum 型の配列を返します。 

そのため、enum の名前を文字列に変換してからコンソールに出力しています。

`C# Enum.GetNames()` メソッドを使うと、enumerateenum の名前を文字列として出力できるので、文字列に変換する必要はありません。

`.Net 5` 以上をお使いの方は、汎用関数`C# Enum.GetNames()` をお使いください。

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

古いバージョンでは、`typeof()` enum パラメータを渡す必要があります。

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

もし、enumの名前を文字列で表示したい場合は、`C# Enum.GetNames()` メソッドを使用することができます。

## 使用方法`Linq`

`Linq forEach` メソッドを使用すると、C#enum を`Enum.GetValues()` と`Enum.GetNames()` メソッドの助けを借りて、enumerate することができます。

`.Net 5` 以上では、以下のコードスニペットを使用してください。

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

古いバージョンでは

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## 概要

enum このチュートリアルでは、C# で`Enum.GetValues()` と`Enum.GetNames()` メソッドを使ってenumを作成することを学びました。










