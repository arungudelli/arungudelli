+++
title="8 måder at loop/iterere ordbogsnøgle-værdipar i C#"
summary="Brug af C# foreach loop er den enkleste og mest enkle måde at iterere over ordbogsnøgleværdier i C#."
keywords=["loop ordbog i C#, iterere ordbog c#, loop ordbog nøgler, loop ordbog værdier"]
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

For at iterere ordbogens nøgle-værdipar i C# kan du bruge følgende metoder

1. Brug af C# `foreach` loop
2. Iterér kun over C#-ordbogsnøgler
3. Iterate kun over C#-ordbogens værdier
4. Brug af `Deconstruct` af `KeyValuePair<TKey,TValue>` i C# 7
5. Brug af `Deconstruct` og `discards` i C# 7 
6. `Deconstruct` af nøgle-værdipar i ældre C#-versioner
7. Brug af `dictionary.ElementAt()` -funktionen og `for` loop
8. Brug af C# `dictionary.AsParallel().ForAll()` 

Lad os gennemgå et eksempel for at forstå det nærmere 

Jeg har oprettet en prøveordbog ved hjælp af `C#` for loop

Tag et kig på nedenstående `C#` ordbog

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Løsning 1: Brug af `C# foreach` loop

Brug af `C# foreach` loop er den enkleste og mest enkle og ligetil måde at iterere over ordbogsnøgleværdier i C#.

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

Variablen `dictionary` i ovenstående `foreach` loop vil have `KeyValuePair<TKey, TValue>` type 

Vi kan nemt få adgang til `Key` &amp; `Value` egenskaberne for `KeyValuePair` type.

## Løsning 2: Iterér kun over C#-ordbogsnøgler

Hvis du kun ønsker at gennemløbe over ordbogsnøgler, skal du bruge C#-ordbogen `dictionary.Keys` property.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Løsning 3: Iterér kun over C#-ordbogens værdier

Hvis du kun vil iterere over ordbogsværdier, skal du bruge egenskaben C#-ordbog `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Løsning 4: Brug `Deconstruct()` af `KeyValuePair<TKey,TValue>` i C# 7

Deconstructors er indført i C# 7.0-versionen.
 
Og hvis du bruger .NET Core 2.0+-applikationen, kan `KeyValuePair<TKey, TValue>` type vil have `Deconstruct()` -metoden.

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

For at få adgang til nøgle-værdiparret i ordbogen skal du bruge funktionen `Deconstruct()` af typen `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Løsning 5: Brug af `Deconstruct` og `discards` i C# 7 

Fra og med C# 7.0 understøtter C# discards 

Discards er pladsholdervariabler, der bevidst ikke bruges i programkode 

Ofte kaldes de underscore `_` variabler.

Discards er intet andet end de ikke-tildelte variabler, de har ingen værdi.

I ordbogen, hvis du kun ønsker at sløjfe nøgler, kan vi gøre brug af discard-variabler.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Tilsvarende hvis man kun ønsker at bruge ordbogsværdier.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Løsning 6: `Deconstruct` af nøgle-værdipar i ældre C#-versioner


Struct KeyValuePair har ikke `Deconstruct()` -funktionen i ældre versioner af C# (C# 4.7.2 nedenfor) 

Så hvis du vil bruge `Deconstruct()` til at sløjfe nøgleværdipar, er der en løsning 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

I de fleste tilfælde vil vi ikke bruge denne metode, men det er godt at vide.

## Løsning 7: Brug af `dictionary.ElementAt()` -funktionen og `for` loop

Vi kan bruge en simpel `for` loop til at iterere over ordbogens nøgle-værdipar.

Vi kan få adgang til `KeyValuePair` -værdierne ved hjælp af ordbogsindekset ved hjælp af `dictionary.ElementAt()` -funktionen.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Igen er det ikke en god måde at løbe gennem ordbogen på, fordi `ElementAt()` funktionen vil have `O(n)` og vi har `for` loop ovenfor, så tidskompleksiteten vil være `O(n^2)` 

I store ordbøger vil det have konsekvenser for ydeevnen.

Hvis du vil have indekset for Dictionary key value par, skal du bruge denne metode 

Jeg tror ikke, at der er nogen brugssituation i den virkelige verden, hvor ordbogsindekset vil blive brugt 

## Løsning 8: Brug af C# `dictionary.AsParallel().ForAll()`

Hvis du har en stor ordbog, kan vi gøre brug af LINQ-forespørgsel (Parallel Language Integrated Query) ved at bruge udvidelsesmetoden `ParallelEnumerable.AsParallel` på ordbogen og udføre forespørgslen ved hjælp af `ParallelEnumerable.ForAll` -metoden.

Forespørgslen opdeler kilden i opgaver, der udføres asynkront på flere tråde

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Bedste måde at sløjfe ordbogen på i C# 

Selv om vi har flere måder at iterere over en ordbogs nøgleværdier på, foretrækker vi at bruge en simpel foreach-loop 

Og hvis du kun ønsker at lave en løkke om C#-ordbogsnøgler eller -værdier, skal du bruge `dictionary.Keys` eller `dictionary.Values` i stedet for at iterere hele ordbogen 







