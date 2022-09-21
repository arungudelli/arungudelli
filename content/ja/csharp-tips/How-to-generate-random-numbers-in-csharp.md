
---
title: "C# で乱数を生成する方法"
description: "C# で乱数を生成するさまざまな方法を、簡単な例とともに紹介します。"
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


乱数は、デジタルゲーム、統計サンプリング、暗号、統計物理学の計算、数値解析、無線通信、ルーレットのようなカジノゲームなどで広く使われています。 

C#で乱数を生成するには、`Random` クラスを使用します**。

##`C# Random` クラスとは？

`C# Random` クラスは擬似乱数生成器であり、乱数に関する一定の統計的要件を満たした数列を生成するアルゴリズムです。

このクラスは、5つのメソッド`Next()`,`NextInt64()`,`NextBytes()`,`NextDouble()`,`NextSingle()` を持っています。 

`int`,`long` など、数値の種類に応じて、対応するメソッドを使用することができます。

例を見て、さらに理解を深めましょう。 

## C#でランダムな整数を生成する 

C#でランダムな整数を生成する手順 

1.乱数クラスのインスタンス化
2.`Random.Next()` メソッドを使用して、`Int32.MinValue` と`Int32.MaxValue` の間の乱数整数を返す。

```csharp

var randomInteger = new Random();

randomInteger.Next();
randomInteger.Next();
randomInteger.Next();
randomInteger.Next();
randomInteger.Next(); 


/* OUTPUT : 
2027076668
1095111085
535874255
1973884472
430547700
*/
```

### 最小値と最大値の間のランダムな整数を生成する

`Random.Next()` はオーバーロードされたメソッドを持ち、最小値と最大値をパラメータとして受け取り、与えられた値の間のランダムな整数を生成します。

100から1000までの乱数を生成するには、次のコードを使用します。

```csharp
Console.WriteLine("Five random integers between 100 and 1000");

for (int counter = 0; counter <= 4; counter++)
    Console.WriteLine("{0}", randomNumber.Next(100, 1000));

/* OUTPUT:
Five random integers between 100 and 1000
904
853
554
290
614
*/
```

## C# で長い乱数(Int64)を生成する。 

`Int64` `Random.NextInt64()` メソッドを使用すると、`Int64.MinValue` と`Int64.MaxValue` の間のランダムな`Int64` 番号が返されます。

```csharp

var RandomInt64 = new Random();

RandomInt64.NextInt64();
RandomInt64.NextInt64();
RandomInt64.NextInt64();
RandomInt64.NextInt64();
RandomInt64.NextInt64(); 


/* OUTPUT : 
5200810282391000059
6501337495320049889
6318562423063201438
3733878081804548122
8421209223603063849
*/
```

### 与えられた範囲内のランダムな長さ(Int64)の数を生成する

`Random.Next()` と同様に、`Random.NextInt64()` にもオーバーロードされたメソッドがあり、Range すなわち最小値と最大値をパラメータとして受け取り、それらの間のランダムな`Int64` 数を返します。

100000から200000の間の乱数を生成するには、次のコードを使用します。

```csharp

var RandomInt64 = new Random();


Console.WriteLine("Five random integers between 100000 and 200000");

for (int counter = 0; counter <= 4; counter++)
    Console.WriteLine("{0}", RandomInt64.NextInt64(100000, 200000));

/* OUTPUT:
Five random long Int64 numbers between 100000 and 200000
144220
194475
185075
159433
136542
*/
```

生成された乱数は、数学的アルゴリズムを用いて選択されているため、完全なランダムではありませんが、現実のほとんどのケースで十分な性能を発揮します。

## 乱数生成時の重複の回避

もし、複数の`new Random()` クラスを初期化している場合。 

乱数の重複が発生する可能性がある。(マルチスレッドアプリケーション)

```csharp
var randomOne = new Random();
var randomTwo = new Random(); // Don't do this
```

そのため、`Random()` クラスのインスタンスは1つだけ初期化し、アプリケーション全体で使用するのがよいでしょう。

```csharp
//Function to generate unique random number using `Random()` class

private static readonly Random randomInstance = new Random();

public static int GenerateRandomNumber(int min, int max)
{
    lock(randomInstance) // synchronize
    {
        return randomInstance.Next(min, max);
    }
}
```
もし、マルチスレッド環境で一連の乱数を生成したい場合は、上記の方法を使用してください。

## 暗号を使う`C# RandomNumberGenerator`

本当にユニークな乱数を生成したい場合は、`System.Security.Cryptography` ライブラリの一部である`RandomNumberGenerator` クラスを使用することができます。

このクラスは暗号学的に安全な乱数を生成し、ランダムなパスワードの生成に 適しています。

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(Int32.MaxValue);

```

また、`RandomNumberGenerator` メソッドに range を渡すことができます。

```csharp
var randomNumber= RandomNumberGenerator.GetInt32(2000,5000);

```

##`C# RNGCryptoServiceProvider` クラスの使用

このクラスはもう古いので、このメソッドは使わないでください。

`RNGCryptoServiceProvider` は、暗号化サービスプロバイダ (CSP) が提供する実装を使用して、暗号化乱数生成器 (RNG) を実装します。

以下のコードで、` C# RNGCryptoServiceProvider` クラスを使用して乱数を生成してください。

```csharp
using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
{
   byte[] randomNumber = new byte[4];//4 for int32
   rng.GetBytes(randomNumber);
   int value = BitConverter.ToInt32(randomNumber, 0);
}
```

## 概要

このチュートリアルでは、C#で乱数を生成するさまざまな方法を、簡単な例を使って学びました。

















