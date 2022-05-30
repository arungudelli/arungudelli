+++
title="8 способов циклов/итераций пар ключ-значение словаря в C#"
summary="Использование цикла foreach в C# является самым простым и понятным способом итерации ключевых значений словаря в C#."
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Для итерации пар ключ-значение словаря в C# используйте следующие методы

1. Использование цикла C# `foreach` 
2. Итерация только по ключам словаря C#
3. Итерация только над значениями словаря C#
4. Использование `Deconstruct` из `KeyValuePair<TKey,TValue>` в C# 7
5. Использование `Deconstruct` и `discards` в C# 7 
6. `Deconstruct` пары ключ-значение в старых версиях C#
7. Использование функции `dictionary.ElementAt()` и цикла `for` 
8. Использование C# `dictionary.AsParallel().ForAll()` 

Давайте рассмотрим пример, чтобы понять это дальше 

Я создал пример словаря с помощью цикла for `C#` 

Взгляните на приведенный ниже словарь `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Решение 1: Использование цикла `C# foreach` 

Использование цикла `C# foreach` - это самый простой и понятный способ итерации значений ключей словаря в C#.

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

Переменная `dictionary` в приведенном выше цикле `foreach` будет иметь `KeyValuePair<TKey, TValue>` тип 

Мы можем легко получить доступ к свойствам `Key` и `Value` типа `KeyValuePair`.

## Решение 2: Итерация только по ключам словаря C#

Если вы хотите перебирать только ключи словаря, используйте свойство словаря C# `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Решение 3: Итерация только над значениями словаря C#

Если вы хотите перебирать только значения словаря, используйте свойство словаря C# `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Решение 4: Использование `Deconstruct()` из `KeyValuePair<TKey,TValue>` в C# 7

Деконструкторы появились в версии C# 7.0.
 
И если вы используете приложение .NET Core 2.0+, тип `KeyValuePair<TKey, TValue>` тип будет иметь метод `Deconstruct()`.

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

Для доступа к паре ключ-значение словаря используйте функцию `Deconstruct()` типа `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Решение 5: Использование `Deconstruct` и `discards` в C# 7 

Начиная с версии C# 7.0, C# поддерживает отбрасывание 

Отбрасываемые переменные - это переменные-заполнители, которые намеренно не используются в коде приложения 

Часто их называют переменными с подчеркиванием `_`.

Отбрасываемые переменные - это не что иное, как неназначенные переменные, у них нет значения.

В словаре, если нужно перебрать только ключи, можно использовать отбрасываемые переменные.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Аналогично, если вы хотите использовать только значения словаря.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Решение 6: `Deconstruct` пары ключ-значение в старых версиях C#


Структура KeyValuePair не имеет функции `Deconstruct()` в старых версиях C#. (C# 4.7.2 ниже) 

Поэтому если вы хотите использовать `Deconstruct()` для цикла пар ключ-значение, есть обходной путь 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

В большинстве случаев мы не будем использовать этот метод, но знать его полезно.

## Решение 7: Использование функции `dictionary.ElementAt()` и цикла `for` 

Мы можем использовать простой цикл `for` для перебора пар ключ-значение словаря.

Мы можем получить доступ к значениям `KeyValuePair` по индексу словаря с помощью функции `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Опять же, это не лучший способ циклического просмотра словаря, потому что функция `ElementAt()` будет иметь `O(n)`, а у нас есть `for` цикл выше, поэтому временная сложность будет `O(n^2)` 

В больших словарях это будет иметь последствия для производительности.

Если вы хотите получить индекс пар ключ-значение словаря, используйте этот метод 

Я не представляю ни одного реального случая, где бы использовался индекс словаря 

## Решение 8: Использование C# `dictionary.AsParallel().ForAll()`

Если у вас большой словарь, мы можем воспользоваться запросом Parallel Language Integrated Query (LINQ), используя метод расширения `ParallelEnumerable.AsParallel` на словаре и выполнив запрос с помощью метода `ParallelEnumerable.ForAll`.

Запрос разбивает источник на задачи, которые выполняются асинхронно на нескольких потоках

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Лучший способ зацикливания словаря в C# 

Несмотря на то, что у нас есть несколько способов перебора значений ключей словаря, мы предпочитаем использовать простой цикл foreach 

А если вы хотите перебрать только ключи или значения словаря C#, используйте `dictionary.Keys` или `dictionary.Values` вместо итерации всего словаря 







