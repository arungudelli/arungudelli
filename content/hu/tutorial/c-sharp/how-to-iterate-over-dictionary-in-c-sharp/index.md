+++
title="8 módja a szótár kulcs-érték párok ciklusának/iterálásának C#-ban"
summary="A C# foreach ciklus használata a legegyszerűbb és legegyszerűbb módja a szótárkulcsértékek iterálásának C# nyelven."
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

A szótár kulcs-érték párosainak iterálásához C# nyelven a következő módszereket használhatjuk

1. C# `foreach` ciklus használata
2. Csak C# szótárkulcsokon való ismétlés
3. Csak a C# szótár értékein való ismétlés
4. A `Deconstruct` használata `KeyValuePair<TKey,TValue>` a C# 7-ben
5. A `Deconstruct` és a `discards` használata a C# 7-ben 
6. `Deconstruct` kulcs-érték pár használata régebbi C# verziókban
7. A `dictionary.ElementAt()` függvény és a `for` ciklus használata
8. A C# `dictionary.AsParallel().ForAll()` használata 

Nézzünk végig egy példát, hogy jobban megértsük 

Létrehoztam egy példaszótárat a `C#` for ciklus segítségével

Nézze meg az alábbi `C#` szótárat

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## 1. megoldás: A `C# foreach` loop használata

A `C# foreach` ciklus használata a legegyszerűbb és legegyszerűbb módja a szótárkulcsok értékein való iterációnak C# nyelven.

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

A `dictionary` változó a fenti `foreach` ciklusban a változónak a következő értéke lesz `KeyValuePair<TKey, TValue>` type 

Könnyen hozzáférhetünk a `Key` &amp; `Value` tulajdonságaihoz a `KeyValuePair` típushoz.

## 2. megoldás: Csak a C# szótárkulcsok felett végzett ismétlés

Ha csak a szótárkulcsok felett akarunk ciklusozni, használjuk a C# szótár `dictionary.Keys` tulajdonságát.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## 3. megoldás: Csak a C# szótár értékein való ismétlés

Ha csak a szótári értékeken szeretne iterálni, használja a C# szótár `dictionary.Values` tulajdonságát.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## 4. megoldás: A `Deconstruct()` of `KeyValuePair<TKey,TValue>` c# 7-ben

A dekonstruktorok a C# 7.0 verziójában kerültek bevezetésre.
 
Ha pedig a .NET Core 2.0+ alkalmazást használja, akkor a `KeyValuePair<TKey, TValue>` típusnak lesz `Deconstruct()` metódusa.

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

A szótár kulcs-érték párjának eléréséhez használja a `KeyValuePair` típus `Deconstruct()` függvényét.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## 5. megoldás: A `Deconstruct` és a `discards` használata C# 7 nyelven 

A C# 7.0-tól kezdődően a C# támogatja az eldobásokat 

A discards olyan helyőrző változók, amelyeket szándékosan nem használnak fel az alkalmazáskódban 

Gyakran nevezik őket aláhúzással `_` változóknak.

A discards nem más, mint a hozzárendelés nélküli változók, nincs értékük.

A szótárban, ha csak a Kulcsokat akarjuk loopolni, akkor használhatjuk a discard változókat.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Hasonlóképpen, ha csak szótári értékeket szeretnénk használni.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## 6. megoldás: `Deconstruct` kulcs-érték páros régebbi C# verziókban


A struct KeyValuePair nem rendelkezik `Deconstruct()` funkcióval a C# régebbi verzióiban (C# 4.7.2 alatt).(C# 4.7.2) 

Ha tehát a `Deconstruct()` funkciót szeretné használni a kulcsértékpárok hurokba rendezésére, akkor van egy megoldás 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Az esetek többségében nem fogjuk használni ezt a módszert, de jó tudni.

## 7. megoldás: A `dictionary.ElementAt()` függvény és a `for` ciklus használata

Egyszerű `for` ciklus segítségével végigjárhatjuk a szótár kulcs-érték párosait.

A `KeyValuePair` értékeket a `dictionary.ElementAt()` függvény segítségével a szótár indexe alapján érhetjük el.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Ismét nem jó módja a szótárban való ciklusozásnak, mert a `ElementAt()` függvénynek `O(n)` lesz, és fentebb van `for` ciklusunk, így az időbonyolultság `O(n^2)` lesz 

Nagy szótárak esetén ez teljesítménybeli következményekkel jár.

Ha a Dictionary kulcs-érték párok indexét szeretné megkapni, használja ezt a módszert 

Nem tudok olyan valós felhasználási esetre gondolni, ahol a szótár indexét használnánk 

## 8. megoldás: C# használata `dictionary.AsParallel().ForAll()`

Ha nagy szótárral rendelkezünk, akkor kihasználhatjuk a párhuzamos nyelvi integrált lekérdezést (LINQ), ha a `ParallelEnumerable.AsParallel` bővítési metódust használjuk a szótárra, és a lekérdezést a `ParallelEnumerable.ForAll` metódus segítségével hajtjuk végre.

A lekérdezés a forrást feladatokra bontja, amelyek aszinkron módon, több szálon kerülnek végrehajtásra

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## A szótár ciklusának legjobb módja C# nyelven 

Annak ellenére, hogy többféleképpen is végig tudunk menni a szótár kulcsértékein, inkább az egyszerű foreach hurkot használjuk 

Ha pedig csak a C# szótár kulcsát vagy értékét akarjuk hurokba zárni, használjuk a `dictionary.Keys` vagy a `dictionary.Values` címet, ahelyett, hogy a teljes szótárat iterálnánk 







