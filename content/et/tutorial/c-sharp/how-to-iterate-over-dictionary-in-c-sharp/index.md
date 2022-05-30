+++
title="8 viisi, kuidas loopida/iterata sõnastiku võtmeväärtuspaare C# keeles"
summary="C# foreach-silmuse kasutamine on lihtsaim ja sirgjoonelisim viis sõnastiku võtmeväärtuste üle iteratsiooniks C# keeles."
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

Sõnastiku võtmeväärtuspaaride iteratsiooniks C# keeles kasuta järgmisi meetodeid

1. Kasutades C# `foreach` loop
2. Iteratsioon ainult C# sõnastiku võtmete üle
3. Iteratsioon ainult C# sõnastiku väärtuste üle
4. Kasutades `Deconstruct` of `KeyValuePair<TKey,TValue>` c# keeles 7
5. Kasutades `Deconstruct` ja `discards` C# 7 keeles 
6. `Deconstruct` võtmeväärtuse paari kasutamine vanemates C# versioonides
7. `dictionary.ElementAt()` funktsiooni ja `for` tsükli kasutamine
8. C# `dictionary.AsParallel().ForAll()` kasutamine 

Käime läbi ühe näite, et seda paremini mõista 

Olen loonud näidissõnastiku, kasutades `C#` for loop'i

Vaadake alljärgnevat `C#` sõnastikku

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Lahendus 1: Kasutades `C# foreach` loop

Kasutades `C# foreach` loop on lihtsaim ja sirgjoonelisim viis sõnastiku võtmeväärtuste üle itereerimiseks C# keeles.

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

Muutuja `dictionary` ülaltoodud `foreach` tsüklis on muutuja `KeyValuePair<TKey, TValue>` tüüp 

Me saame hõlpsasti ligi `Key` &amp; `Value` omadustele `KeyValuePair` tüübile.

## Lahendus 2: Iteratsioon ainult C# sõnastiku võtmete üle

Kui soovite loopida ainult sõnastiku võtmete üle, kasutage C# sõnastiku `dictionary.Keys` omadust.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Lahendus 3: Iteratsioon ainult C# sõnastiku väärtuste üle

Kui soovite itereerida ainult sõnastiku väärtuste üle, kasutage C# sõnastiku `dictionary.Values` omadust.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Lahendus 4: Kasutades `Deconstruct()` of `KeyValuePair<TKey,TValue>` c#-s 7

Dekonstruktorid on kasutusele võetud C# 7.0 versioonis.
 
Ja kui te kasutate .NET Core 2.0+ rakendust, siis on `KeyValuePair<TKey, TValue>` tüübil on `Deconstruct()` meetod.

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

Sõnastiku võtmeväärtuspaarile juurdepääsuks kasutage `Deconstruct()` funktsiooni `KeyValuePair` tüübi .

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Lahendus 5: `Deconstruct` ja `discards` kasutamine C# 7-s 

Alates C# 7.0-st toetab C# loobumisi 

Discards on paigutusmuutujad, mis on rakenduskoodis tahtlikult kasutamata 

Sageli nimetatakse neid allkriipsu `_` muutujateks.

Discards ei ole midagi muud kui määramata muutujad, neil ei ole väärtust.

Sõnastikus, kui tahame loopida ainult võtmeid, saame kasutada discard-muutujaid.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Samamoodi, kui soovite kasutada ainult sõnastiku väärtusi.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Lahendus 6: `Deconstruct` võtmeväärtuspaar vanemates C# versioonides


Struktuuril KeyValuePair ei ole C# vanemates versioonides funktsiooni `Deconstruct()`. (C# 4.7.2 allpool) 

Nii et kui soovite kasutada `Deconstruct()` võtmeväärtuspaaride loopimiseks, siis on olemas lahendus 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Enamasti me seda meetodit ei kasuta, kuid seda on hea teada.

## Lahendus 7: `dictionary.ElementAt()` funktsiooni ja `for` tsükli kasutamine

Me võime kasutada lihtsat `for` loop'i, et itereerida üle sõnastiku võtmeväärtuspaaride.

Saame juurdepääsu `KeyValuePair` väärtustele sõnastiku indeksi abil, kasutades funktsiooni `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Jällegi ei ole see hea viis läbi sõnastiku loopida, sest `ElementAt()` funktsioonil on `O(n)` ja meil on `for` loop eespool, nii et ajakomplekssus on `O(n^2)` 

Suurte sõnastike puhul on see mõju jõudlusele.

Kui soovite saada Dictionary võtmeväärtuspaaride indeksit, kasutage seda meetodit 

Ma ei tea ühtegi reaalset kasutusjuhtumit, kus kasutatakse sõnastiku indeksit 

## Lahendus 8: C# kasutamine `dictionary.AsParallel().ForAll()`

Kui teil on suur sõnastik, saame kasutada paralleelset keelega integreeritud päringut (LINQ) päringut, kasutades `ParallelEnumerable.AsParallel` laiendusmeetodit sõnastikule ja sooritades päringu meetodi `ParallelEnumerable.ForAll` abil.

Päring jaotab allika ülesanneteks, mida täidetakse asünkroonselt mitmes niidis

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Parim viis sõnastiku loopimiseks C# keeles 

Kuigi meil on mitu võimalust sõnastiku võtmeväärtuste üle iteratsiooniks, eelistame kasutada lihtsat foreach loop'i 

Ja kui soovite loop ainult C# sõnastiku võtmed või väärtused kasutada `dictionary.Keys` või `dictionary.Values` asemel iterating kogu sõnastik 







