+++
title="8 manieren om dictionary key value paren te itereren in C#"
summary="Met behulp van C# foreach loop is de eenvoudigste en eenvoudige manier om te itereren over dictionary key values in C#."
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]
type="post
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='vals'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Om dictionary key value paren te itereren in C# gebruik je de volgende methodes

1. Met behulp van C# `foreach` loop
2. Itereren over alleen C#-woordenboeksleutels
3. Alleen over C#-waarden van woordenboeken lopen
4. Gebruik `Deconstruct` van `KeyValuePair<TKey,TValue>` in C# 7
5. Gebruik van `Deconstruct` en `discards` in C# 7 
6. `Deconstruct` van sleutel-waardepaar in oudere C#-versies
7. Gebruik van `dictionary.ElementAt()` functie en `for` lus
8. Gebruik van C# `dictionary.AsParallel().ForAll()` 

Laten we een voorbeeld bekijken om het verder te begrijpen 

Ik heb een voorbeeldwoordenboek gemaakt met `C#` for loop

Kijk eens naar het onderstaande `C#` woordenboek

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Oplossing 1: Gebruik `C# foreach` loop

Het gebruik van `C# foreach` loop is de eenvoudigste manier om de sleutelwaarden van een woordenboek te doorlopen in C#.

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

De `dictionary` variabele in bovenstaande `foreach` lus heeft `KeyValuePair<TKey, TValue>` type 

We kunnen gemakkelijk toegang krijgen tot `Key` &amp; `Value` eigenschappen van `KeyValuePair` type.

## Oplossing 2: Itereer alleen over C# woordenboeksleutels

Als je alleen over de sleutels van een woordenboek wilt lopen, gebruik dan de C# dictionary `dictionary.Keys` eigenschap.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Oplossing 3: Itereer alleen over C# woordenboekwaarden

Als je alleen over woordenboekwaarden wilt itereren, gebruik dan de C# dictionary `dictionary.Values` eigenschap.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Oplossing 4: Gebruik `Deconstruct()` van `KeyValuePair<TKey,TValue>` in C# 7

Deconstructors zijn geïntroduceerd in C# 7.0 versie.
 
En als u .NET Core 2.0+ applicatie gebruikt zal het `KeyValuePair<TKey, TValue>` type zal `Deconstruct()` methode hebben.

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

Om toegang te krijgen tot het sleutel-waardepaar van het woordenboek gebruik je de `Deconstruct()` functie van het `KeyValuePair` type.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Oplossing 5: Gebruik `Deconstruct` en `discards` in C# 7 

Vanaf C# 7.0 ondersteunt C# discards 

Discards zijn placeholder variabelen die opzettelijk niet gebruikt worden in applicatie code 

Vaak worden ze aangeduid als underscore `_` variabelen.

Discards zijn niets anders dan de niet-toegewezen variabelen, ze hebben geen waarde.

In het woordenboek kunnen we gebruik maken van discard variabelen als we alleen sleutels in een lus willen plaatsen.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Evenzo als je alleen dictionary waarden wilt gebruiken.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Oplossing 6: `Deconstruct` van key value pair in oudere C# versies


Het struct KeyValuePair heeft geen `Deconstruct()` functie in oudere versies van C#.(C# 4.7.2 hieronder) 

Dus als je `Deconstruct()` wilt gebruiken om key value paren te lussen is er een workaround 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

In de meeste gevallen zullen we deze methode niet gebruiken, maar het is goed om te weten.

## Oplossing 7: Gebruik van `dictionary.ElementAt()` functie en `for` lus

We kunnen een eenvoudige `for` lus gebruiken om te itereren over dictionary key value paren.

We kunnen toegang krijgen tot de `KeyValuePair` waarden door de woordenboekindex te gebruiken met de `dictionary.ElementAt()` functie.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Opnieuw is het geen goede manier om door het woordenboek te lopen, omdat `ElementAt()` functie `O(n)` zal hebben en wij `for` lus hierboven hebben, zodat de tijdcomplexiteit `O(n^2)` zal zijn 

In grote woordenboeken zal dit gevolgen hebben voor de prestaties.

Als je de index van sleutel-waardeparen van een woordenboek wilt krijgen, gebruik dan deze methode 

Ik kan me geen gebruikssituatie in de echte wereld voorstellen waar een woordenboekindex zal worden gebruikt 

## Oplossing 8: Met behulp van C# `dictionary.AsParallel().ForAll()`

Als je een groot woordenboek hebt, kunnen we gebruik maken van Parallel Language Integrated Query (LINQ) query door de `ParallelEnumerable.AsParallel` extension method te gebruiken op het woordenboek en de query uit te voeren met behulp van de `ParallelEnumerable.ForAll` method.

De query verdeelt de bron in taken die asynchroon op meerdere threads worden uitgevoerd

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Beste manier om het woordenboek te lussen in C# 

Hoewel we meerdere manieren hebben om te itereren over de sleutelwaarden van een woordenboek, verkiezen we het gebruik van een eenvoudige foreach lus 

En als je alleen C# woordenboek sleutels of waarden wilt luseren gebruik dan `dictionary.Keys` of `dictionary.Values` in plaats van het hele woordenboek te itereren 







