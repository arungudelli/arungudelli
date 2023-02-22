---
title: "How to loop/enumerate C# enum"
description: "C#のenumをループさせたり列挙するさまざまな方法と例"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

enumは、`C#` 言語で広く使われています。 

そして、`C#` でenumをループまたは列挙する4つの方法があります。 

1.`C# Enum.GetValues()` を .Net 5 &amp; above で使用する。
2.古い.Netバージョンで`C# Enum.GetValues()` を使用する。
3.`C# Enum.GetNames()` を使用して、列挙名を文字列として列挙する。
4.使用方法`Linq`

さらに理解するために例を見てみましょう。 

まず、C#の`enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

`enum` は、さまざまなタイプのロギングレベルを表します。

ここで、`C# enum` を列挙するさまざまな方法を見てみましょう。

## `C# Enum.GetValues()` .Net 5 &amp; above の Generic メソッドの使用

`.Net` の最新バージョン、つまり`.Net 5` 以降を使用している場合、`Enum.GetValues` メソッドにジェネリックバージョンを使用して、`C# enum` をループさせることができます。

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

新しいジェネリック版`Enum.GetValues` は，enum 値の配列を返します。 

そしてさらに、`for` または`foreach` ステートメントを使用して、`C# enum` を列挙することができます。 

配列は`enum` 型を含んでいるので、`ToString()` メソッドを使って文字列に変換する必要があります。

## 古いバージョンの.Netでは、`C# Enum.GetValues()` を使用します。

古いバージョンの`.Net` では、`Enum.GetValues()` メソッドで利用できるジェネリックメソッドがありません。 

`Enum.GetValues()` メソッドにパラメータとして`typeof()` enum を渡す必要があります。 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
そして、`System.Array` 型の enum 値を返します。さらに、`foreach` ステートメントを使用して、C# enum をループすることができます。

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

もし、`IEnumerable` の結果が欲しければ、さらに`Enum.GetValues()` メソッドをキャストすればよい。

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

## `C# Enum.GetNames()` を使って、文字列としての列挙名を列挙する。 

`C# Enum.GetValues()` メソッドは enum 型の配列を返します。 

そのため、コンソールに表示する前にenumの値を文字列に変換しています。

`C# Enum.GetNames()` メソッドを使用すると、enum の名前を文字列として列挙することができるので、文字列に変換する必要はありません。

`.Net 5` 以上をお使いの場合は、汎用関数`C# Enum.GetNames()` をお使いください。

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

そのため、enum 名を文字列としてループさせたい場合は、`C# Enum.GetNames()` メソッドを使用することができます。

## 使用方法`Linq`

C#のenumを列挙するには、`Enum.GetValues()` と`Enum.GetNames()` メソッドの助けを借りて、`Linq forEach` メソッドを使用します。

`.Net 5` 以上では、以下のコード・スニペットを使用してください。

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

このチュートリアルでは、`Enum.GetValues()` と`Enum.GetNames()` メソッドを使用して、C# で enum をループ処理することを学びました。










