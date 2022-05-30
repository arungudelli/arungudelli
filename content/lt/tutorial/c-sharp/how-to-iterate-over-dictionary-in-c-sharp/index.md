+++
title="8 būdai, kaip C# kalba sudaryti ciklą/iteruoti žodyno rakto ir vertės poras"
summary="C# foreach ciklo naudojimas yra paprasčiausias ir aiškiausias būdas iteruoti žodyno raktų vertes C# kalba."
keywords=["ciklas žodyne C#, iteruoti žodyną c#, ciklas žodyno raktai, ciklas žodyno reikšmės"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Norėdami iteruoti žodyno rakto ir vertės poras C#, naudokite šiuos metodus

1. Naudojant C# `foreach` ciklą
2. Iteruoti tik C# žodyno raktus
3. Iteruoti tik per C# žodyno reikšmes
4. Naudojant `Deconstruct` iš `KeyValuePair<TKey,TValue>` c# 7
5. `Deconstruct` ir `discards` naudojimas C# 7 
6. `Deconstruct` rakto ir vertės poros naudojimas senesnėse C# versijose
7. Funkcijos `dictionary.ElementAt()` ir ciklo `for` naudojimas
8. Naudojant C# `dictionary.AsParallel().ForAll()` 

Kad geriau suprastumėte, panagrinėkime pavyzdį 

Sukūriau pavyzdinį žodyną naudodamas `C#` for ciklą

Pažvelkite į toliau pateiktą `C#` žodyną

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## 1 sprendimas: naudojant `C# foreach` ciklą

Naudojant `C# foreach` kilpą yra paprasčiausias ir aiškiausias būdas iteruoti žodyno raktų reikšmes C# kalba.

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

Pirmiau pateiktame `foreach` cikle `dictionary` kintamasis turės `KeyValuePair<TKey, TValue>` tipą 

Galime lengvai pasiekti `Key` ir `Value` tipo `KeyValuePair` savybes.

## 2 sprendimas: Iteriuokite tik per C# žodyno raktus

Jei norite pertraukti ciklą tik per žodyno raktus, naudokite C# žodyno `dictionary.Keys` savybę.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## 3 sprendimas: Iteriuokite tik per C# žodyno reikšmes

Jei norite iteruoti tik žodyno vertes, naudokite C# žodyno `dictionary.Values` savybę.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## 4 sprendimas: naudodami `Deconstruct()` iš `KeyValuePair<TKey,TValue>` c# 7

Dekonstruktoriai įdiegti C# 7.0 versijoje.
 
O jei naudojate .NET Core 2.0+ programos `KeyValuePair<TKey, TValue>` tipas turės `Deconstruct()` metodą.

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

Norėdami pasiekti žodyno rakto ir vertės porą, naudokite `Deconstruct()` tipo `KeyValuePair` funkciją.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## 5 sprendimas: `Deconstruct` ir `discards` naudojimas C# 7 

Nuo C# 7.0 versijos C# palaiko išmetimus 

Atmetimai yra vietos kintamieji, kurie sąmoningai nenaudojami taikomajame kode 

Dažnai jie vadinami `_` kintamaisiais.

Discards yra ne kas kita, kaip nepriskirti kintamieji, jie neturi reikšmės.

Žodyne, jei norime cikle įrašyti tik raktus, galime pasinaudoti išmetimo kintamaisiais.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Panašiai, jei norite naudoti tik žodyno reikšmes.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## 6 sprendimas: `Deconstruct` rakto ir vertės poros senesnėse C# versijose


Senesnėse C# versijose struct KeyValuePair neturi `Deconstruct()` funkcijos (C# 4.7.2 žemiau) 

Taigi, jei norite naudoti `Deconstruct()` rakto vertės porai cikle, yra apėjimo būdas 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Dažniausiai šio metodo nenaudosime, tačiau jį žinoti verta.

## 7 sprendimas: naudojant `dictionary.ElementAt()` funkciją ir `for` ciklą

Galime naudoti paprastą `for` ciklą, kad iteruotume po žodyno rakto ir vertės poras.

Galime pasiekti `KeyValuePair` reikšmes pagal žodyno indeksą naudodami `dictionary.ElementAt()` funkciją.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Vėlgi tai nėra geras būdas ciklui per žodyną, nes `ElementAt()` funkcija turės `O(n)`, o aukščiau turime `for` ciklą, todėl laiko sudėtingumas bus `O(n^2)` 

Dideliuose žodynuose tai turės įtakos našumui.

Jei norite gauti žodyno rakto ir vertės poros indeksą, naudokite šį metodą 

Neįsivaizduoju nė vieno realaus naudojimo atvejo, kai būtų naudojamas žodyno indeksas 

## 8 sprendimas: naudojant C# `dictionary.AsParallel().ForAll()`

Jei turite didelį žodyną, galime pasinaudoti lygiagrečiosios kalbos integruotos užklausos (LINQ) užklausa, naudodami `ParallelEnumerable.AsParallel` plėtinio metodą žodynui ir vykdydami užklausą `ParallelEnumerable.ForAll` metodu.

Užklausa suskirsto šaltinį į užduotis, kurios vykdomos asinchroniškai keliuose srautuose

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Geriausias būdas sudaryti žodyno ciklą C# kalba 

Nors turime daugybę būdų, kaip iteruoti žodyno raktų reikšmes, pirmenybę teikiame paprastam foreach ciklui 

O jei norite ciklo tik C# žodyno raktai arba vertės, naudokite `dictionary.Keys` arba `dictionary.Values`, užuot iteravę visą žodyną 







