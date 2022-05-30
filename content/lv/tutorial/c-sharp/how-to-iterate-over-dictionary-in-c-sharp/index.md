+++
title="8 veidi, kā veidot cilpas/iterēt vārdnīcas atslēgu/vērtību pārus C# valodā"
summary="Izmantojot C# foreach cilpu, tas ir vienkāršākais un vienkāršākais veids, kā C# programmā iterēt vārdnīcas atslēgu vērtības."
keywords=["cilpa vārdnīca C#, iterēt vārdnīcu c#, cilpa vārdnīcas atslēgas, cilpa vārdnīcas vērtības"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Lai iterētu vārdnīcas atslēgu un vērtību pārus C#, izmantojiet šādas metodes

1. Izmantojot C# `foreach` cilpu
2. Iterēt tikai pār C# vārdnīcas atslēgām
3. Iterēt tikai pār C# vārdnīcas vērtībām
4. Izmantojot `Deconstruct` no `KeyValuePair<TKey,TValue>` programmā C# 7
5. `Deconstruct` un `discards` izmantošana C# 7 
6. `Deconstruct` atslēgas un vērtības pāra izveide vecākās C# versijās
7. Izmantojot `dictionary.ElementAt()` funkciju un `for` cilpu
8. Izmantojot C# `dictionary.AsParallel().ForAll()` 

Izskatīsim piemēru, lai to labāk izprastu 

Esmu izveidojis vārdnīcas paraugu, izmantojot `C#` for cilpu

Aplūkojiet zemāk redzamo vārdnīcu `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## 1. risinājums: Izmantojot `C# foreach` cilpu

Izmantojot `C# foreach` cilpu, tas ir vienkāršākais un vienkāršākais veids, kā C# pārlūkot vārdnīcas atslēgas vērtības.

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

Mainīgajam `dictionary` iepriekš minētajā `foreach` cilpā būs `KeyValuePair<TKey, TValue>` tips 

Mēs varam viegli piekļūt `Key` &amp; `Value` tipa `KeyValuePair` īpašībām.

## 2. risinājums: Iterēt tikai pār C# vārdnīcas atslēgām

Ja vēlaties cilpot tikai pa vārdnīcas atslēgām, izmantojiet C# vārdnīcas īpašību `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

### 3. risinājums: Iterējiet tikai pār C# vārdnīcas vērtībām

Ja vēlaties iterēt tikai vārdnīcas vērtības, izmantojiet C# vārdnīcas īpašību `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

### 4. risinājums: Izmantojot `Deconstruct()` no `KeyValuePair<TKey,TValue>` programmā C# 7

Dekonstruktori ir ieviesti C# 7.0 versijā.
 
Un, ja jūs izmantojat .NET Core 2.0+ lietojumprogrammu `KeyValuePair<TKey, TValue>` tipam būs `Deconstruct()` metode.

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

Lai piekļūtu vārdnīcas atslēgas un vērtības pārim, izmantojiet `Deconstruct()` tipa `KeyValuePair` funkciju.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## 5. risinājums: `Deconstruct` un `discards` izmantošana C# 7 

Sākot ar C# 7.0 versiju, C# atbalsta atmetumus 

Atmetumi ir vietvārdu mainīgie, kas lietojumprogrammas kodā tiek tīši neizmantoti 

Bieži vien tos dēvē par apakšsvītras `_` mainīgajiem.

Atmetumi nav nekas cits kā nepiešķirti mainīgie, tiem nav vērtības.

Ja vārdnīcā vēlamies cilpot tikai atslēgas, varam izmantot atmetuma mainīgos.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Līdzīgi, ja vēlaties izmantot tikai vārdnīcas vērtības.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## 6. risinājums: `Deconstruct` atslēgu un vērtību pāru vecākās C# versijās


Struktūrai KeyValuePair nav funkcijas `Deconstruct()` vecākās C# versijās (C# 4.7.2 zemāk) 

Tāpēc, ja vēlaties izmantot `Deconstruct()`, lai veidotu atslēgu un vērtību pāru cilpas, ir risinājums, kā to apiet 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Lielākajā daļā gadījumu mēs šo metodi neizmantosim, bet ir labi to zināt.

## 7. risinājums: Izmantojot `dictionary.ElementAt()` funkciju un `for` cilpu

Mēs varam izmantot vienkāršu `for` cilpu, lai iterētu pa vārdnīcas atslēgu un vērtību pāriem.

Mēs varam piekļūt `KeyValuePair` vērtībām pēc vārdnīcas indeksa, izmantojot `dictionary.ElementAt()` funkciju.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Tas atkal nav labs veids, kā veikt cilpu pa vārdnīcu, jo `ElementAt()` funkcijai būs `O(n)` un mums ir `for` cilpa iepriekš, tāpēc laika sarežģītība būs `O(n^2)` 

Lielu vārdnīcu gadījumā tas ietekmēs veiktspēju.

Ja vēlaties iegūt vārdnīcas atslēgas un vērtības pāru indeksu, izmantojiet šo metodi 

Es nedomāju par nevienu reālu lietošanas gadījumu, kad tiks izmantots vārdnīcas indekss 

## 8. risinājums: Izmantojot C# `dictionary.AsParallel().ForAll()`

Ja jums ir liela vārdnīca, mēs varam izmantot paralēlo valodas integrēto vaicājumu (LINQ), izmantojot `ParallelEnumerable.AsParallel` paplašinājuma metodi vārdnīcai un izpildot vaicājumu, izmantojot `ParallelEnumerable.ForAll` metodi.

Vaicājums sadala avotu uzdevumos, kas tiek izpildīti asinhroni vairākos pavedienos

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Labākais veids, kā veidot cilpu vārdnīcā programmā C# 

Lai gan mums ir vairāki veidi, kā iterēt pa vārdnīcas atslēgas vērtībām, dodam priekšroku vienkāršai foreach cilpei 

Un, ja vēlaties izmantot tikai C# vārdnīcas atslēgas vai vērtības, izmantojiet `dictionary.Keys` vai `dictionary.Values`, nevis iterēt visu vārdnīcu 







