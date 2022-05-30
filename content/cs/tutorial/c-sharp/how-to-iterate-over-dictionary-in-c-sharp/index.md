+++
title="8 způsobů, jak v jazyce C# vytvořit smyčku/iterovat dvojice klíč-hodnota slovníku"
summary="Použití smyčky foreach v jazyce C# je nejjednodušší a přímočarý způsob iterace hodnot klíčů slovníku v jazyce C#."
klíčová slova=["smyčka slovníku v C#, iterace slovníku c#, smyčka klíčů slovníku, smyčka hodnot slovníku"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Pro iteraci dvojic klíč-hodnota slovníku v jazyce C# použijte následující metody

1. Pomocí smyčky v jazyce C# `foreach` 
2. Iterace pouze nad klíči slovníku C#
3. Iterovat pouze nad hodnotami slovníku C#
4. Použití `Deconstruct` z `KeyValuePair<TKey,TValue>` v C# 7
5. Použití `Deconstruct` a `discards` v jazyce C# 7 
6. `Deconstruct` dvojice klíč-hodnota ve starších verzích jazyka C#
7. Použití funkce `dictionary.ElementAt()` a smyčky `for` 
8. Použití funkce `dictionary.AsParallel().ForAll()` v jazyce C# 

Projděme si příklad, abychom jej lépe pochopili 

Vytvořil jsem ukázkový slovník pomocí `C#` for cyklu

Podívejte se na níže uvedený slovník `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Řešení 1: Použití smyčky `C# foreach` 

Použití smyčky `C# foreach` je nejjednodušší a nejpřímočařejší způsob iterace přes hodnoty klíčů slovníku v jazyce C#.

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

Proměnná `dictionary` ve výše uvedeném cyklu `foreach` bude mít hodnotu `KeyValuePair<TKey, TValue>` typ 

K vlastnostem `Key` &amp; `Value` typu `KeyValuePair` můžeme snadno přistupovat.

## Řešení 2: Iterace pouze nad klíči slovníku C#

Pokud chcete procházet ve smyčce pouze klíče slovníku, použijte vlastnost slovníku C# `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Řešení 3: Iterujte pouze nad hodnotami slovníku C#

Pokud chcete iterovat pouze nad slovníkovými hodnotami, použijte vlastnost C# dictionary `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Řešení 4: Použití `Deconstruct()` z `KeyValuePair<TKey,TValue>` v jazyce C# 7

Dekonstruktory jsou zavedeny ve verzi C# 7.0.
 
A pokud používáte aplikaci .NET Core 2.0+ `KeyValuePair<TKey, TValue>` typ bude mít metodu `Deconstruct()`.

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

Pro přístup k dvojici klíč-hodnota slovníku použijte funkci `Deconstruct()` typu `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Řešení 5: Použití `Deconstruct` a `discards` v jazyce C# 7 

Počínaje verzí C# 7.0 podporuje jazyk C# odhazování 

Discardy jsou zástupné proměnné, které se v kódu aplikace záměrně nepoužívají 

Často se označují jako proměnné s podtržítkem `_`.

Discards nejsou nic jiného než nepřiřazené proměnné, nemají žádnou hodnotu.

Pokud chceme ve slovníku zacyklit pouze Klíče, můžeme využít odhazovací proměnné.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Podobně pokud chceme použít pouze hodnoty slovníku.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Řešení 6: `Deconstruct` dvojice klíč-hodnota ve starších verzích jazyka C#


Struct KeyValuePair nemá ve starších verzích jazyka C# funkci `Deconstruct()` (C# 4.7.2 níže) 

Pokud tedy chcete použít `Deconstruct()` pro zacyklení dvojic klíčů a hodnot, existuje řešení 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Ve většině případů tuto metodu nebudeme používat, ale je dobré ji znát.

## Řešení 7: Použití funkce `dictionary.ElementAt()` a smyčky `for` 

K iteraci nad dvojicemi klíč-hodnota slovníku můžeme použít jednoduchou smyčku `for`.

K hodnotám `KeyValuePair` můžeme přistupovat pomocí indexu slovníku pomocí funkce `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Opět to není dobrý způsob, jak procházet slovník, protože funkce `ElementAt()` bude mít `O(n)` a my máme výše `for` smyčku, takže časová složitost bude `O(n^2)` 

U velkých slovníků to bude mít dopad na výkon.

Pokud chcete získat index dvojic klíč-hodnota slovníku, použijte tuto metodu 

Nenapadá mě žádný reálný případ použití, kdy by se index slovníku používal 

## Řešení 8: Použití jazyka C# `dictionary.AsParallel().ForAll()`

Pokud máme k dispozici velký slovník, můžeme využít dotazu LINQ (Parallel Language Integrated Query) tak, že na slovníku použijeme rozšiřující metodu `ParallelEnumerable.AsParallel` a dotaz provedeme pomocí metody `ParallelEnumerable.ForAll`.

Dotaz rozdělí zdroj na úlohy, které se provádějí asynchronně ve více vláknech

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Nejlepší způsob, jak zacyklit slovník v jazyce C# 

I když máme více způsobů, jak iterovat přes hodnoty klíčů slovníku, raději použijte jednoduchý cyklus foreach 

A pokud chcete zacyklit pouze klíče nebo hodnoty slovníku C#, použijte místo iterace celého slovníku `dictionary.Keys` nebo `dictionary.Values` 







