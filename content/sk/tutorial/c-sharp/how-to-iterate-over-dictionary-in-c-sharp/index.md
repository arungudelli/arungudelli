+++
title="8 spôsobov, ako v jazyku C# vytvoriť cyklus/iteráciu dvojíc kľúč-hodnota slovníka"
summary="Použitie cyklu foreach v jazyku C# je najjednoduchší a najpriamejší spôsob iterácie hodnôt kľúčov slovníka v jazyku C#."
keywords=["cyklus slovníka v jazyku C#, iterácia slovníka c#, cyklus kľúčov slovníka, cyklus hodnôt slovníka"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[obrázok]
focal_point=''
preview_only=false
+++

Na iteráciu dvojíc kľúč-hodnota slovníka v jazyku C# použite nasledujúce metódy

1. Pomocou cyklu C# `foreach` 
2. Iterovať len nad kľúčmi slovníka C#
3. Iterovať len nad hodnotami slovníka C#
4. Použitie `Deconstruct` z `KeyValuePair<TKey,TValue>` v jazyku C# 7
5. Používanie `Deconstruct` a `discards` v jazyku C# 7 
6. `Deconstruct` dvojice kľúč-hodnota v starších verziách jazyka C#
7. Použitie funkcie `dictionary.ElementAt()` a slučky `for` 
8. Používanie funkcie `dictionary.AsParallel().ForAll()` v jazyku C# 

Prejdime si príklad, aby sme ho lepšie pochopili 

Vytvoril som ukážkový slovník pomocou `C#` for cyklu

Pozrite sa na nižšie uvedený slovník `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Riešenie 1: Použitie slučky `C# foreach` 

Použitie slučky `C# foreach` je najjednoduchší a najpriamočiarejší spôsob iterácie cez hodnoty kľúčov slovníka v jazyku C#.

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

Premenná `dictionary` vo vyššie uvedenom cykle `foreach` bude mať `KeyValuePair<TKey, TValue>` typ 

K vlastnostiam `Key` &amp; `Value` typu `KeyValuePair` môžeme ľahko pristupovať.

## Riešenie 2: Iterujte len nad kľúčmi slovníka C#

Ak chcete cyklovať len nad kľúčmi slovníka, použite vlastnosť C# slovníka `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Riešenie 3: Iterujte len nad hodnotami slovníka C#

Ak chcete iterovať len nad slovníkovými hodnotami, použite vlastnosť C# dictionary `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Riešenie 4: Použitie `Deconstruct()` z `KeyValuePair<TKey,TValue>` v jazyku C# 7

Dekonštruktory sú zavedené vo verzii C# 7.0.
 
A ak používate aplikáciu .NET Core 2.0+ `KeyValuePair<TKey, TValue>` typ bude mať metódu `Deconstruct()`.

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

Na prístup k dvojici kľúč - hodnota slovníka použite funkciu `Deconstruct()` typu `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Riešenie 5: Použitie `Deconstruct` a `discards` v jazyku C# 7 

Počnúc verziou C# 7.0 podporuje jazyk C# odhadzovanie 

Discards sú zástupné premenné, ktoré sa v aplikačnom kóde zámerne nepoužívajú 

Často sa označujú ako premenné s podčiarkovníkom `_`.

Discards nie sú nič iné ako nepriradené premenné, nemajú žiadnu hodnotu.

Ak chceme v slovníku zacykliť len Kľúče, môžeme využiť vyraďovacie premenné.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Podobne, ak chcete použiť len hodnoty slovníka.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Riešenie 6: `Deconstruct` dvojice kľúč hodnota v starších verziách jazyka C#


Štruktúra KeyValuePair nemá v starších verziách jazyka C# funkciu `Deconstruct()`. (C# 4.7.2 nižšie) 

Ak teda chcete použiť `Deconstruct()` na zacyklenie dvojice kľúč - hodnota, existuje riešenie 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Vo väčšine prípadov túto metódu nebudeme používať, ale je dobré to vedieť.

## Riešenie 7: Použitie funkcie `dictionary.ElementAt()` a cyklu `for` 

Na iteráciu cez dvojice kľúč-hodnota slovníka môžeme použiť jednoduchý cyklus `for`.

K hodnotám `KeyValuePair` môžeme pristupovať pomocou indexu slovníka pomocou funkcie `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Opäť to nie je dobrý spôsob na prechádzanie slovníka, pretože funkcia `ElementAt()` bude mať `O(n)` a my máme vyššie `for` slučku, takže časová zložitosť bude `O(n^2)` 

Pri veľkých slovníkoch to bude mať vplyv na výkon.

Ak chcete získať index dvojice kľúč hodnota slovníka, použite túto metódu 

Nenapadá ma žiadny prípad použitia v reálnom svete, kde by sa použil index slovníka 

## Riešenie 8: Použitie jazyka C# `dictionary.AsParallel().ForAll()`

Ak máme veľký slovník, môžeme využiť dotaz LINQ (Parallel Language Integrated Query) tak, že na slovníku použijeme metódu rozšírenia `ParallelEnumerable.AsParallel` a dotaz vykonáme pomocou metódy `ParallelEnumerable.ForAll`.

Dotaz rozdelí zdroj na úlohy, ktoré sa vykonávajú asynchrónne na viacerých vláknach

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Najlepší spôsob, ako vytvoriť cyklus slovníka v jazyku C# 

Aj keď máme viacero spôsobov, ako iterovať cez hodnoty kľúčov slovníka, uprednostňujeme použitie jednoduchého cyklu foreach 

A ak chcete v C# zacykliť iba kľúče alebo hodnoty slovníka, použite `dictionary.Keys` alebo `dictionary.Values` namiesto iterácie celého slovníka 







