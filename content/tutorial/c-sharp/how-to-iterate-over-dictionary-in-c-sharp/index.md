+++
title="How to iterate dictionary key value pairs in C#"
summary="There are Two ways To get enum name from value in C# 1. Use C# Enum.GetName() and pass enum value as parameter to get the name.2. Convert enum value to the enumeration member using casting and then use ToString() method."
keywords=["get enum name from value c#"]
type='post'
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To iterate dictionary key value pairs in C# use the following methods

1. Using C# `foreach` loop
2. Iterate over C# dictionary keys only
3. Iterate over C# dictionary values only
2. Using `Deconstruct` of `KeyValuePair<TKey,TValue>` in C# 7
3. `Deconstruct` of key value pair in older C# versions
4. Using `dictionary.ElementAt()` function and `for` loop
5. Iterate over C# dictionary keys only
6. Iterate over C# dictionary values only
7. Using C# `dictionary.AsParallel().ForAll()` 

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

If you want to loop over only dictionary keys use the C# dictionary `.Keys` property.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("Key is {0}",key);
}
```

## Solution 3: Iterate over C# dictionary values only

If you want to iterate over only dictionary Values use the C# dictionary `.Values` property.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("Value is {0}", value);
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


