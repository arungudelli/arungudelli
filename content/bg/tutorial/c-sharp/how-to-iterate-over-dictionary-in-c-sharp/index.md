+++
title="8 начина за циклиране/повторение на двойки ключ-стойност в речника в C#"
summary="Използването на цикъла foreach в C# е най-простият и ясен начин за итерация на ключови стойности на речник в C#."
keywords=["цикъл на речник в C#, итерация на речник c#, цикъл на ключове на речник, цикъл на стойности на речник"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

За итерация на двойки ключ-стойност в речника в C# използвайте следните методи

1. Използване на цикъл в C# `foreach` 
2. Итериране само над ключове на речника в C#
3. Итерация само над стойности на речника C#
4. Използване на `Deconstruct` на `KeyValuePair<TKey,TValue>` в C# 7
5. Използване на `Deconstruct` и `discards` в C# 7 
6. `Deconstruct` на двойка ключ-стойност в по-стари версии на C#
7. Използване на функцията `dictionary.ElementAt()` и цикъла `for` 
8. Използване на `dictionary.AsParallel().ForAll()` в C# 

Нека разгледаме един пример, за да го разберем по-добре 

Създадох примерен речник, като използвах `C#` for loop

Разгледайте речника по-долу `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Решение 1: Използване на цикъл `C# foreach` 

Използването на цикъл `C# foreach` е най-простият и ясен начин за итериране на ключови стойности на речника в C#.

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

Променливата `dictionary` в горния цикъл `foreach` ще има `KeyValuePair<TKey, TValue>` type 

Можем лесно да получим достъп до `Key` и `Value` свойствата на `KeyValuePair` type.

## Решение 2: Итерация само над ключовете на речника на C#

Ако искате да направите цикъл само над ключовете на речника, използвайте свойството на C# речника `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Решение 3: Итервюирайте само над стойностите на C# речника

Ако искате да итерирате само над речникови стойности, използвайте свойството C# dictionary `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Решение 4: Използване на `Deconstruct()` на `KeyValuePair<TKey,TValue>` в C# 7

Деконструкторите са въведени във версия 7.0 на C#.
 
И ако използвате .NET Core 2.0+ приложение `KeyValuePair<TKey, TValue>` типът ще има метод `Deconstruct()`.

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

За да получите достъп до двойката ключ-стойност на речника, използвайте функцията `Deconstruct()` на типа `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Решение 5: Използване на `Deconstruct` и `discards` в C# 7 

От версия 7.0 на C#, C# поддържа изхвърляния 

Discards са заместващи променливи, които умишлено не се използват в кода на приложението 

Често те се наричат променливи с подчертаване `_`.

Discards не са нищо друго освен неприсвоени променливи, те нямат стойност.

В речника, ако искаме да зациклим само Ключове, можем да използваме променливите за отхвърляне.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
По същия начин, ако искате да използвате само стойности в речника.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Решение 6: `Deconstruct` на двойка ключ-стойност в по-старите версии на C#


Структурата KeyValuePair няма функция `Deconstruct()` в по-старите версии на C# (C# 4.7.2 по-долу) 

Така че, ако искате да използвате `Deconstruct()`, за да зациклите двойки ключове стойност, има заобиколно решение 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

В повечето случаи няма да използваме този метод, но е добре да го знаете.

## Решение 7: Използване на функцията `dictionary.ElementAt()` и цикъла `for` 

Можем да използваме прост цикъл `for`, за да итерираме по двойките ключ-стойност в речника.

Можем да осъществим достъп до стойностите `KeyValuePair` чрез индекса на речника, като използваме функцията `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Отново това не е добър начин за циклично преминаване през речника, защото функцията `ElementAt()` ще има `O(n)`, а ние имаме `for` цикъл по-горе, така че времевата сложност ще бъде `O(n^2)` 

При големи речници това ще се отрази на производителността.

Ако искате да получите индекса на двойките ключ-стойност в речника, използвайте този метод 

Не се сещам за нито един случай на употреба в реалния свят, при който ще се използва индекс на речник 

## Решение 8: Използване на C# `dictionary.AsParallel().ForAll()`

Ако разполагате с голям речник, можем да се възползваме от паралелната заявка LINQ (Parallel Language Integrated Query), като използваме метода за разширение `ParallelEnumerable.AsParallel` върху речника и изпълним заявката с помощта на метода `ParallelEnumerable.ForAll`.

Запитването разделя източника на задачи, които се изпълняват асинхронно на няколко нишки

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Най-добрият начин за създаване на цикъл на речника в C# 

Въпреки че имаме много начини да преглеждаме ключовите стойности на речника, предпочитаме да използваме простия цикъл foreach 

А ако искате да направите цикъл само за ключовете или стойностите на речника на C#, използвайте `dictionary.Keys` или `dictionary.Values`, вместо да итерирате целия речник 







