+++
title="8 načinov za ustvarjanje zanke/teratiranja parov ključ-vrednost v slovarju v jeziku C#"
summary="Uporaba zanke foreach v jeziku C# je najpreprostejši in enostaven način za iteracijo nad vrednostmi ključev slovarja v jeziku C#."
keywords=["zanka slovar v C#, iteriranje slovarja c#, zanka ključi slovarja, zanka vrednosti slovarja"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[slika]
focal_point=''
preview_only=false
+++

Za iteracijo parov ključ-vrednost slovarja v jeziku C# uporabite naslednje metode

1. Uporaba zanke v jeziku C# `foreach` 
2. Iterirajte samo nad ključi slovarja C#
3. Iterirajte samo nad vrednostmi slovarja C#
4. Uporaba `Deconstruct` `KeyValuePair<TKey,TValue>` v C# 7
5. Uporaba `Deconstruct` in `discards` v C# 7 
6. `Deconstruct` para ključ-vrednost v starejših različicah C#
7. Uporaba funkcije `dictionary.ElementAt()` in zanke `for` 
8. Uporaba funkcije `dictionary.AsParallel().ForAll()` v jeziku C# 

Za boljše razumevanje si oglejmo primer 

Vzorec slovarja sem ustvaril z uporabo `C#` for zanke

Oglejte si spodnji slovar `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Rešitev 1: Uporaba zanke `C# foreach` 

Uporaba zanke `C# foreach` je najpreprostejši in enostaven način za iteracijo po vrednostih ključev slovarja v jeziku C#.

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

Spremenljivka `dictionary` v zgornji `foreach` zanki bo imela `KeyValuePair<TKey, TValue>` tip 

Enostavno lahko dostopamo do lastnosti `Key` in `Value` tipa `KeyValuePair`.

## Rešitev 2: Iterirajte samo nad ključi slovarja C#

Če želite narediti zanko samo nad ključi slovarja, uporabite lastnost slovarja C# `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Rešitev 3: Iterirajte samo nad vrednostmi slovarja C#

Če želite iterirati samo nad vrednostmi slovarja, uporabite lastnost slovarja C# `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Rešitev 4: Uporaba `Deconstruct()` `KeyValuePair<TKey,TValue>` v jeziku C# 7

Dekonstruktorji so uvedeni v različici C# 7.0.
 
Če uporabljate aplikacijo .NET Core 2.0+ `KeyValuePair<TKey, TValue>` bo tip imel metodo `Deconstruct()`.

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

Za dostop do para ključ-vrednost slovarja uporabite funkcijo `Deconstruct()` tipa `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Rešitev 5: Uporaba `Deconstruct` in `discards` v jeziku C# 7 

Od različice C# 7.0 dalje program C# podpira zavržke 

Zavrnitve so nadomestne spremenljivke, ki se v aplikacijski kodi namenoma ne uporabljajo 

Pogosto se imenujejo podčrtanke `_` spremenljivke.

Zavrnjene spremenljivke niso nič drugega kot nepripisane spremenljivke in nimajo vrednosti.

Če želimo v slovarju zapeti samo ključe, lahko uporabimo spremenljivke zavržkov.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Podobno velja, če želite uporabiti samo vrednosti slovarja.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Rešitev 6: `Deconstruct` para ključ-vrednost v starejših različicah C#


Struct KeyValuePair nima funkcije `Deconstruct()` v starejših različicah C# (C# 4.7.2 spodaj) 

Če torej želite uporabiti `Deconstruct()` za kroženje parov ključ-vrednost, obstaja obvoznica 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

V večini primerov te metode ne bomo uporabljali, vendar je dobro vedeti.

## Rešitev 7: Uporaba funkcije `dictionary.ElementAt()` in zanke `for` 

Za iteracijo po parih ključ-vrednost slovarja lahko uporabimo preprosto `for` zanko.

Do vrednosti `KeyValuePair` lahko dostopamo z indeksom slovarja z uporabo funkcije `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Spet to ni dober način kroženja po slovarju, saj bo funkcija `ElementAt()` imela `O(n)` in zgoraj imamo `for` zanko, zato bo časovna zahtevnost `O(n^2)` 

Pri velikih slovarjih bo to vplivalo na zmogljivost.

Če želite dobiti indeks parov ključ-vrednost slovarja, uporabite to metodo 

Ne poznam nobenega primera uporabe v resničnem svetu, kjer bi se uporabil indeks slovarja 

## Rešitev 8: Uporaba C# `dictionary.AsParallel().ForAll()`

Če imamo velik slovar, lahko uporabimo poizvedbo LINQ (Parallel Language Integrated Query) tako, da na slovarju uporabimo razširitveno metodo `ParallelEnumerable.AsParallel` in poizvedbo izvedemo z metodo `ParallelEnumerable.ForAll`.

Poizvedba razdeli vir na naloge, ki se izvajajo asinhrono na več niti

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Najboljši način za ustvarjanje zanke v slovarju v jeziku C# 

Čeprav imamo na voljo več načinov za iteracijo po vrednostih ključev slovarja, raje uporabimo preprosto zanko foreach 

In če želite v zanko vstaviti samo ključe ali vrednosti slovarja C#, uporabite `dictionary.Keys` ali `dictionary.Values`, namesto da iterirate po celotnem slovarju 







