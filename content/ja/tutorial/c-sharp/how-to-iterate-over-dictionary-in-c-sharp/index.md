+++
title="C#で辞書のキーと値のペアをループ/反復処理する8つの方法"
summary="C#のforeachループを使用することは、C#で辞書のキー値を繰り返し処理する最もシンプルでわかりやすい方法です。"
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]].
type='post'（ポスト
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['管理者']
[イメージ図］
focal_point=''です。
プレビューのみ=false
+++

C#で辞書のキーと値のペアを繰り返し処理するには、次のメソッドを使用します。

1.C# の`foreach` ループを使用する
2.C#の辞書のキーのみを繰り返し処理
3.C#の辞書の値のみを繰り返し処理
4.の`Deconstruct` を使用する。 `KeyValuePair<TKey,TValue>`をC# 7で使用
5.C# 7 で`Deconstruct` と`discards` を使用する。 
6. `Deconstruct` 古いバージョンのC#でキーと値のペアの
7.`dictionary.ElementAt()` 関数と`for` ループの使用
8.C# の使用`dictionary.AsParallel().ForAll()` 

さらに理解を深めるために、例題を見てみましょう。 

`C#` for loop を使って、サンプル辞書を作成しました。

以下の`C#` 辞書を見てください。

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{%toc%}}

## 解決策 1:`C# foreach` のループを使う

`C# foreach` ループを使用することは、C# で辞書のキー値を反復処理する最も簡単でわかりやすい方法です。

```
foreach (var dictionary in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", dictionary.Key, dictionary.Value);
}

//OUTPUT

dictionary key is key1 and value is value1
dictionary key is key2 and value is value2
dictionary key is key3 and value is value3
dictionary key is key4 and value is value4
dictionary key is key5 and value is value5
```

上記の`foreach` ループの`dictionary` 変数には `KeyValuePair<TKey, TValue>`型になります。 

`KeyValuePair` 型の`Key` と`Value` のプロパティに簡単にアクセスすることができます。

## 解決策2：C#の辞書のキーにのみ繰り返し処理を行う

辞書のキーだけをループさせたい場合は、C#の辞書`dictionary.Keys` プロパティを使用します。

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## 解決策3: C#の辞書の値だけを繰り返し処理する

辞書の値のみを繰り返し処理したい場合は、C#の辞書`dictionary.Values` プロパティを使用します。

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## 解決策4:`Deconstruct()` を使用する。 `KeyValuePair<TKey,TValue>`を使う

C# 7.0バージョンからデコンストラクタが導入されました。
 
また、.NET Core 2.0+ Applicationを使用している場合、? `KeyValuePair<TKey, TValue>`型は`Deconstruct()` メソッドを持つことになります。

```
public readonly struct KeyValuePair<TKey, TValue>
{
        private readonly TKey key;

        private readonly TValue value;

        private readonly int _dummyPrimitive;

        public TKey Key
        {
            get
            {
                throw null;
            }
        }

        public TValue Value
        {
            get
            {
                throw null;
            }
        }

        public KeyValuePair(TKey key, TValue value)
        {
            throw null;
        }

        [EditorBrowsable(EditorBrowsableState.Never)]
        public void Deconstruct(out TKey key, out TValue value)
        {
            throw null;
        }

        public override string ToString()
        {
            throw null;
        }
}
```

辞書のキーと値のペアにアクセスするには、`KeyValuePair` タイプの`Deconstruct()` 関数を使用します。

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## 解決策5：C# 7で`Deconstruct` と`discards` を使用する。 

C# 7.0から、C#はディスカードに対応しました。 

ディスカードとは、アプリケーションコードで意図的に使用されないプレースホルダ変数のことです。 

しばしば、アンダースコア（`_` ）変数と呼ばれます。

ディスカードは何も割り当てられていない変数であり、値を持ちません。

辞書の中でKeyだけをループさせたい場合、捨て変数が利用できます。

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
同様に、辞書の値だけを使いたい場合にも、捨て変数が使えます。

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## 解決策6:`Deconstruct` 古いバージョンのC#でキーと値のペアを作成する。


古いバージョンの C# では、KeyValuePair 構造体に`Deconstruct()` 関数がありません（C# 4.7.2 以下）。 

そのため、`Deconstruct()` を使ってキーバリューペアをループさせたい場合は、回避策があります。 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

ほとんどの場合、この方法を使うことはないでしょうが、知っておくとよいでしょう。

## 解決策7:`dictionary.ElementAt()` 関数と`for` ループを使う

シンプルな`for` ループを使って、辞書のキーと値のペアを繰り返し処理することができます。

`dictionary.ElementAt()` 関数を使って、辞書のインデックスで`KeyValuePair` の値にアクセスできる。

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

なぜなら、`ElementAt()` 関数は`O(n)` を持ち、上記の`for` ループがあるので、時間計算量は`O(n^2)` になってしまうからです。 

大規模な辞書の場合、これは性能に影響を与えるだろう。

もし、Dictionaryのキーと値のペアのインデックスを取得したい場合は、このメソッドを使用してください。 

実際の使用例では、ディクショナリのインデックスを使用することはないと思われます。 

## 解決策8: C#を使う`dictionary.AsParallel().ForAll()`

大きな辞書がある場合、辞書に`ParallelEnumerable.AsParallel` 拡張メソッドを使用して、`ParallelEnumerable.ForAll` メソッドでクエリを実行することで、LINQ（Parallel Language Integrated Query）クエリを利用することができます。

このクエリは，ソースを複数のスレッドで非同期に実行されるタスクに分割します

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## C#で辞書をループさせる最適な方法 

辞書のキー値を反復処理する方法は複数ありますが、単純なforeachループを使用することをお勧めします。 

また、C#の辞書のキーや値のみをループさせたい場合は、辞書全体を反復するのではなく、`dictionary.Keys` または`dictionary.Values` を使用します。 







