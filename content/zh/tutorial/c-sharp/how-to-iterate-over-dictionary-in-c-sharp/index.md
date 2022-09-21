+++
title="在C#中循环/迭代字典键值对的8种方法"
summary="使用C#的foreach循环是在C#中迭代字典键值的最简单和直接的方法。"
keywords=["C#中的循环字典，迭代字典c#，循环字典键，循环字典值"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

要在C#中遍历字典的键值对，请使用以下方法

1.使用C#`foreach` 循环
2.只对C#字典的键值进行迭代
3.只对C#字典的值进行遍历
4.使用`Deconstruct` 的 `KeyValuePair<TKey,TValue>`在C# 7中使用
5.在C#7中使用`Deconstruct` 和`discards` 
6. `Deconstruct` 在较早的C#版本中使用键值对的
7.使用`dictionary.ElementAt()` 函数和`for` 循环
8.使用C#`dictionary.AsParallel().ForAll()` 

让我们通过一个例子来进一步了解它。 

我使用`C#` for 循环创建了一个样本字典

请看下面的`C#` 词典

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## 解决方案1：使用`C# foreach` 循环

使用`C# foreach` 循环是在C#中迭代字典键值的最简单和直接的方法。

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

在上面的`foreach` 循环中的`dictionary` 变量将具有 `KeyValuePair<TKey, TValue>`类型。 

`KeyValuePair` 我们可以很容易地访问`Key` 和`Value` 类型的属性。

## 解决方案2：只对C#字典的键进行迭代

如果你想只在字典的键上循环，使用C#字典的`dictionary.Keys` 属性。

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## 解决方案3：只在C#字典的值上进行迭代

如果你想只迭代字典中的值，请使用C#字典`dictionary.Values` 属性。

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## 解决方案4：使用`Deconstruct()` of `KeyValuePair<TKey,TValue>`在C# 7中

解构器是在C#7.0版本中引入的。
 
如果你使用的是.NET Core 2.0+应用程序，那么 `KeyValuePair<TKey, TValue>`类型将有`Deconstruct()` 方法。

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

要访问字典的键值对，使用`KeyValuePair` 类型的`Deconstruct()` 函数。

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## 解决方案5：在C#7中使用`Deconstruct` 和`discards` 

从C#7.0开始，C#支持弃权。 

弃权是在应用程序代码中故意不使用的占位变量。 

通常它们被称为下划线`_` 变量。

丢弃物只不过是未分配的变量，它们没有值。

在字典中，如果你想只循环按键，我们可以使用弃权变量。

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
同样地，如果你想只使用字典中的值。

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## 解决方案 6:`Deconstruct` 旧的C#版本中的键值对


在旧版本的C#中，结构KeyValuePair没有`Deconstruct()` 。（C# 4.7.2以下）。 

因此，如果你想使用`Deconstruct()` 循环键值对，有一个变通方法。 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

在大多数情况下，我们不会使用这种方法，但知道这一点很好。

## 解决方案7：使用`dictionary.ElementAt()` 函数和`for` 循环

我们可以使用简单的`for` 循环来迭代字典的键值对。

我们可以使用`dictionary.ElementAt()` 函数通过字典索引访问`KeyValuePair` 值。

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

同样，这也不是一个在字典中循环的好方法，因为`ElementAt()` 函数会有`O(n)` ，而我们在上面有`for` 循环，所以时间复杂度会是`O(n^2)` 。 

在大的字典中，它将产生性能影响。

如果你想获得字典键值对的索引，请使用这个方法。 

我不认为有任何现实世界的用例会用到字典的索引。 

## 解决方案 8: 使用 C#`dictionary.AsParallel().ForAll()`

如果你有一个大的字典，我们可以利用并行语言集成查询(LINQ)查询，在字典上使用`ParallelEnumerable.AsParallel` 扩展方法，通过使用`ParallelEnumerable.ForAll` 方法来执行查询。

该查询将源码划分为任务，在多个线程上异步执行

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## 在C#中循环使用字典的最佳方法 

尽管我们有多种方法来迭代一个字典的键值，但更喜欢使用简单的 foreach 循环。 

如果你只想循环C#字典的键或值，请使用`dictionary.Keys` 或`dictionary.Values` ，而不是迭代整个字典。 







