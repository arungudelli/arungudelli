+++
title="8 ways to loop/iterate dictionary key value pairs in C#"
summary="Using C# foreach loop is the simplest and straightforward way to iterate over dictionary key values in C#."
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]
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

To iterate dictionary key value pairs in C# use the following methods

1. Using C# `foreach` loop
2. Iterate over C# dictionary keys only
3. Iterate over C# dictionary values only
4. Using `Deconstruct` of `KeyValuePair<TKey,TValue>` in C# 7
5. Using `Deconstruct` and `discards` in C# 7 
6. `Deconstruct` of key value pair in older C# versions
7. Using `dictionary.ElementAt()` function and `for` loop
8. Using C# `dictionary.AsParallel().ForAll()` 

Let's go through an example to understand it further. 

I have created a sample dictionary using `C#` for loop

Have a look at the below `C#` dictionary

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Solution 1: Using `C# foreach` loop

Using `C# foreach` loop is the simplest and straightforward way to iterate over dictionary key values in C#.

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

The `dictionary` variable in above `foreach` loop will have `KeyValuePair<TKey, TValue>` type. 

We can easily access `Key` & `Value` properties of `KeyValuePair` type.

## Solution 2: Iterate over C# dictionary keys only

If you want to loop over only dictionary keys use the C# dictionary `dictionary.Keys` property.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Solution 3: Iterate over C# dictionary values only

If you want to iterate over only dictionary Values use the C# dictionary `dictionary.Values` property.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Solution 4: Using `Deconstruct()` of `KeyValuePair<TKey,TValue>` in C# 7

Deconstructors are introduced in C# 7.0 version.
 
And if you are using .NET Core 2.0+ Application the `KeyValuePair<TKey, TValue>` type will have `Deconstruct()` method.

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

To access the key value pair of dictionary use the `Deconstruct()` function of `KeyValuePair` type.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Solution 5: Using `Deconstruct` and `discards` in C# 7 

Starting with C# 7.0, C# supports discards. 

Discards are placeholder variables that are intentionally unused in application code. 

Often they referred as underscore `_` variables.

Discards are nothing but the unassigned variables, they don't have a value.

In the dictionary if you want to loop only Keys, we can make use of discard variables.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Similarly if you want use only dictionary values.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Solution 6: `Deconstruct` of key value pair in older C# versions


The struct KeyValuePair does not have `Deconstruct()` function in older versions of C#.(C# 4.7.2 below) 

So if you want to use `Deconstruct()` to loop key value pairs there is a workaround. 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Most of the cases we won't be using this method, but it's good to know.

## Solution 7: Using `dictionary.ElementAt()` function and `for` loop

We can use simple `for` loop to iterate over dictionary key value pairs.

We can access the `KeyValuePair` values by dictionary index using `dictionary.ElementAt()` function.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Again it's not a good way to loop through dictionary, because `ElementAt()` function will have `O(n)` and we have `for` loop above so the time complexity will be `O(n^2)`. 

In large dictionaries it will have performance implications.

If you want to get the index of Dictionary key value pairs use this method. 

I don't think of any real world use case where dictionary index will be used. 

## Solution 8: Using C# `dictionary.AsParallel().ForAll()`

If you have a large dictionary, we can make use of Parallel Language Integrated Query (LINQ) query by using the `ParallelEnumerable.AsParallel` extension method on the dictionary and executing the query by using the `ParallelEnumerable.ForAll` method.

The query partitions the source into tasks that are executed asynchronously on multiple threads

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Best way to loop the dictionary in C# 

Even though we have multiple ways to iterate over a dictionary key values, prefer using simple foreach loop. 

And if you want loop only C# dictionary Keys or Values use `dictionary.Keys` or `dictionary.Values` instead of iterating entire dictionary. 







