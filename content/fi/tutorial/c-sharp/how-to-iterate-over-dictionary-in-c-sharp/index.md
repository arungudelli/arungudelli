+++
title="8 tapaa silmukoida/toistaa sanakirjan avain-arvopareja C#:ssa"
summary="C#:n foreach-silmukan käyttäminen on yksinkertaisin ja suoraviivaisin tapa kerrata sanakirjan avainarvoja C#:ssa."
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

Voit iteroida sanakirjan avain-arvopareja C#:ssa seuraavilla metodeilla

1. Käyttämällä C# `foreach` -silmukkaa
2. Vain C#-sanakirjan avainten toistaminen
3. Iteroi vain C#-sanakirjan arvojen yli
4. Käyttämällä `Deconstruct` of `KeyValuePair<TKey,TValue>` c# 7:ssä
5. `Deconstruct` ja `discards` käyttäminen C# 7:ssä 
6. `Deconstruct` avain-arvoparin käyttäminen vanhemmissa C#-versioissa
7. `dictionary.ElementAt()` -funktion ja `for` -silmukan käyttäminen
8. C#:n `dictionary.AsParallel().ForAll()` käyttäminen 

Käydään läpi esimerkki sen ymmärtämiseksi paremmin 

Olen luonut esimerkkisanakirjan käyttäen `C#` for-silmukkaa

Katso alla olevaa `C#` sanakirjaa

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Ratkaisu 1: `C# foreach` silmukan käyttö

 `C# foreach` -silmukan käyttäminen on yksinkertaisin ja suoraviivaisin tapa kerrata sanakirjan avainarvoja C#:ssa.

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

Edellä olevassa `foreach` -silmukassa muuttujalla `dictionary` on seuraavat arvot `KeyValuePair<TKey, TValue>` type 

Voimme helposti käyttää `Key` &amp; `Value` ominaisuuksien `KeyValuePair` tyyppiä.

## Ratkaisu 2: Toistetaan vain C#-sanakirjan avainten yli

Jos haluat kierrättää vain sanakirjan avaimia, käytä C#-sanakirjan `dictionary.Keys` -ominaisuutta.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Ratkaisu 3: Toista vain C#-sanakirjan arvojen yli

Jos haluat iteroida vain sanakirjan arvojen yli, käytä C#-sanakirjan `dictionary.Values` -ominaisuutta.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Ratkaisu 4: Käyttämällä `Deconstruct()` of `KeyValuePair<TKey,TValue>` c# 7:ssä

Dekonstruktorit on otettu käyttöön C# 7.0 -versiossa.
 
Ja jos käytät .NET Core 2.0+ -sovellusta `KeyValuePair<TKey, TValue>` tyypillä on `Deconstruct()` -metodi.

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

Voit käyttää sanakirjan avain-arvoparia käyttämällä `Deconstruct()` -tyypin `KeyValuePair` funktiota.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Ratkaisu 5: `Deconstruct` ja `discards` käyttäminen C# 7:ssä 

C# 7.0:sta alkaen C# tukee hylkäämistä 

Discardit ovat paikanpitäjämuuttujia, joita ei tarkoituksella käytetä sovelluskoodissa 

Niihin viitataan usein nimellä underscore `_` muuttujat.

Discardit ovat pelkkiä määrittelemättömiä muuttujia, eikä niillä ole arvoa.

Jos sanakirjassa halutaan silmukoida vain Avaimia, voimme käyttää discard-muuttujia.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Samoin jos haluat käyttää vain sanakirjan arvoja.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Ratkaisu 6: `Deconstruct` avain-arvopari vanhemmissa C#-versioissa


Struct KeyValuePair -rakenteella ei ole `Deconstruct()` -funktiota vanhemmissa C#-versioissa (C# 4.7.2 alla) 

Jos siis haluat käyttää `Deconstruct()` -funktiota avainarvoparien silmukointiin, on olemassa kiertotie 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Useimmissa tapauksissa emme käytä tätä menetelmää, mutta se on hyvä tietää.

## Ratkaisu 7: `dictionary.ElementAt()` -funktion ja `for` -silmukan käyttö

Voimme käyttää yksinkertaista `for` -silmukkaa kerrata sanakirjan avain-arvopareja.

Voimme käyttää `KeyValuePair` arvoja sanakirjan indeksin avulla `dictionary.ElementAt()` -funktiolla.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Tämäkään ei ole hyvä tapa silmukoida sanakirjan läpi, koska `ElementAt()` funktiolla on `O(n)` ja meillä on `for` silmukka edellä, joten ajan monimutkaisuus on `O(n^2)` 

Suurissa sanakirjoissa se vaikuttaa suorituskykyyn.

Jos haluat saada indeksin sanakirjan avain-arvopareista, käytä tätä menetelmää 

En keksi yhtään todellista käyttötapausta, jossa sanakirjan indeksiä käytettäisiin 

## Ratkaisu 8: C#:n käyttö `dictionary.AsParallel().ForAll()`

Jos sinulla on suuri sanakirja, voimme hyödyntää LINQ-kyselyä (Parallel Language Integrated Query) käyttämällä `ParallelEnumerable.AsParallel` -laajennusmetodia sanakirjassa ja suorittamalla kyselyn `ParallelEnumerable.ForAll` -metodilla.

Kysely jakaa lähteen tehtäviin, jotka suoritetaan asynkronisesti useissa säikeissä

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Paras tapa kiertää sanakirjaa C#:ssä 

Vaikka meillä on useita tapoja käydä läpi sanakirjan avainarvoja, käytämme mieluummin yksinkertaista foreach-silmukkaa 

Ja jos haluat silmukoida vain C#-sanakirjan avaimia tai arvoja, käytä `dictionary.Keys` tai `dictionary.Values` koko sanakirjan iteroinnin sijasta 







