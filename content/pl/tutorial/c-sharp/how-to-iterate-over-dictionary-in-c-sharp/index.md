+++
title="8 sposobów na zapętlanie/iterację po parach wartości kluczy słownikowych w C#"
summary="Użycie pętli foreach w C# jest najprostszym i bezpośrednim sposobem iteracji po wartościach kluczy słownikowych w C#."
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

Aby iterować pary klucz-wartość słownika w języku C#, należy użyć następujących metod

1. Używając pętli C# `foreach` 
2. Iteracja tylko po kluczach słownika C#
3. Iteracja tylko po wartościach słownika języka C#
4. Using `Deconstruct` of `KeyValuePair<TKey,TValue>` w C# 7
5. Użycie `Deconstruct` i `discards` w C# 7 
6. `Deconstruct` pary klucz-wartość w starszych wersjach języka C#
7. Używanie funkcji `dictionary.ElementAt()` i pętli `for` 
8. Używanie języka C# `dictionary.AsParallel().ForAll()` 

Aby lepiej to zrozumieć, prześledźmy przykład 

Utworzyłem przykładowy słownik, używając `C#` pętli for

Spójrz na poniższy słownik `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Rozwiązanie 1: Użycie pętli `C# foreach` 

Użycie pętli `C# foreach` jest najprostszym i najprostszym sposobem iteracji po wartościach kluczy słownikowych w języku C#.

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

Zmienna `dictionary` w powyższej pętli `foreach` będzie miała `KeyValuePair<TKey, TValue>` type 

Możemy łatwo uzyskać dostęp do właściwości `Key` i `Value` typu `KeyValuePair`.

## Rozwiązanie 2: Iteracja tylko po kluczach słownika C#

Jeśli chcesz wykonać pętlę tylko po kluczach słownika, użyj właściwości `dictionary.Keys` słownika C#.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Rozwiązanie 3: Iteracja tylko nad wartościami słownika C#

Jeśli chcesz iterować tylko po wartościach słownikowych, użyj właściwości C# dictionary `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Rozwiązanie 4: Użycie `Deconstruct()` of `KeyValuePair<TKey,TValue>` w języku C# 7

Dekonstruktory zostały wprowadzone w wersji C# 7.0.
 
Jeśli używasz aplikacji .NET Core 2.0+, typ `KeyValuePair<TKey, TValue>` typ będzie miał metodę `Deconstruct()`.

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

Aby uzyskać dostęp do pary klucz-wartość słownika, należy użyć funkcji `Deconstruct()` typu `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Rozwiązanie 5: Użycie `Deconstruct` i `discards` w C# 7 

Począwszy od wersji C# 7.0, język C# obsługuje odrzuty 

Odrzuty to zmienne zastępcze, które są celowo nieużywane w kodzie aplikacji 

Często określa się je jako zmienne z podkreśleniem `_`.

Odrzuty to nic innego jak nieprzypisane zmienne, które nie mają wartości.

W słowniku, jeśli chcemy zapętlić tylko klucze, możemy skorzystać ze zmiennych odrzucających.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Podobnie, jeśli chcemy używać tylko wartości słownika.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Rozwiązanie 6: `Deconstruct` pary klucz-wartość w starszych wersjach C#


Struktura struct KeyValuePair nie posiada funkcji `Deconstruct()` w starszych wersjach języka C#.(C# 4.7.2 poniżej) 

Jeśli więc chcesz użyć `Deconstruct()` do zapętlenia par wartości kluczy, istnieje obejście tego problemu 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

W większości przypadków nie będziemy używać tej metody, ale dobrze jest o tym wiedzieć.

## Rozwiązanie 7: Użycie funkcji `dictionary.ElementAt()` i pętli `for` 

Do iteracji po parach wartości kluczy słownika możemy użyć prostej pętli `for`.

Możemy uzyskać dostęp do wartości `KeyValuePair` poprzez indeks słownika, używając funkcji `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Ponownie nie jest to dobry sposób na zapętlenie słownika, ponieważ funkcja `ElementAt()` będzie miała `O(n)`, a my mamy `for` pętlę powyżej, więc złożoność czasowa wyniesie `O(n^2)` 

W przypadku dużych słowników będzie to miało wpływ na wydajność.

Jeśli chcesz uzyskać indeks par wartości kluczy słownika, użyj tej metody 

Nie przypominam sobie żadnego przypadku użycia w świecie rzeczywistym, w którym indeks słownika byłby używany 

## Rozwiązanie 8: Użycie języka C# `dictionary.AsParallel().ForAll()`

Jeśli mamy duży słownik, możemy skorzystać z zapytania LINQ (Parallel Language Integrated Query), używając metody rozszerzenia `ParallelEnumerable.AsParallel` na słowniku i wykonując zapytanie metodą `ParallelEnumerable.ForAll`.

Zapytanie dzieli źródło na zadania, które są wykonywane asynchronicznie na wielu wątkach

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Najlepszy sposób na zapętlenie słownika w C# 

Mimo że mamy wiele sposobów na iterację po wartościach kluczy słownika, preferujemy użycie prostej pętli foreach 

A jeśli chcesz zapętlić tylko klucze lub wartości słownika C#, użyj `dictionary.Keys` lub `dictionary.Values` zamiast iterować po całym słowniku 







