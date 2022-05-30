+++
title="8 moduri de a buclă/iterare a perechilor cheie-valoare din dicționar în C#"
summary="Utilizarea buclei foreach C# este cea mai simplă și directă modalitate de a itera peste valorile cheie ale dicționarului în C#."
keywords=["bucla dicționar în C#, iterați dicționarul c#, bucla chei dicționar, bucla valori dicționar"]]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[imagine]
focal_point=''
preview_only=false
+++

Pentru a itera perechile cheie-valoare ale dicționarului în C#, utilizați următoarele metode

1. Folosind C# `foreach` loop
2. Iterați numai peste cheile dicționarului C#
3. Iterare numai peste valorile dicționarului C#
4. Utilizarea `Deconstruct` de `KeyValuePair<TKey,TValue>` în C# 7
5. Folosind `Deconstruct` și `discards` în C# 7 
6. `Deconstruct` a perechii cheie-valoare în versiunile mai vechi ale C#
7. Utilizarea funcției `dictionary.ElementAt()` și a buclei `for` 
8. Utilizarea C# `dictionary.AsParallel().ForAll()` 

Haideți să parcurgem un exemplu pentru a înțelege mai bine 

Am creat un exemplu de dicționar folosind `C#` pentru bucla for loop

Aruncați o privire la dicționarul `C#` de mai jos

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Soluția 1: Utilizarea buclei `C# foreach` 

Utilizarea buclei `C# foreach` este cea mai simplă și directă modalitate de a itera peste valorile cheie ale dicționarului în C#.

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

Variabila `dictionary` din bucla `foreach` de mai sus va avea `KeyValuePair<TKey, TValue>` tip 

Putem accesa cu ușurință proprietățile `Key` și `Value` din tipul `KeyValuePair`.

## Soluția 2: Iterați numai peste cheile dicționarului C#

Dacă doriți să treceți în buclă doar peste cheile dicționarului, utilizați proprietatea `dictionary.Keys` a dicționarului C#.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Soluția 3: Iterați numai peste valorile dicționarului C#

Dacă doriți să iterați numai peste valorile dicționarului, utilizați proprietatea dicționar C# `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Soluția 4: Utilizarea `Deconstruct()` a `KeyValuePair<TKey,TValue>` în C# 7

Deconstructori sunt introduși în versiunea C# 7.0.
 
Iar dacă utilizați aplicația .NET Core 2.0+ Application the `KeyValuePair<TKey, TValue>` type va avea metoda `Deconstruct()`.

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

Pentru a accesa perechea cheie-valoare a dicționarului, utilizați funcția `Deconstruct()` a tipului `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Soluția 5: Utilizarea `Deconstruct` și `discards` în C# 7 

Începând cu C# 7.0, C# acceptă discards 

Discards sunt variabile de tip placeholder care sunt intenționat neutilizate în codul aplicației 

Adesea, acestea sunt denumite variabile cu subliniere `_`.

Discards nu sunt altceva decât variabilele neatribuite, ele nu au o valoare.

În dicționar, dacă doriți să faceți o buclă doar cu chei, putem folosi variabilele discard.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
În mod similar, dacă doriți să folosiți doar valorile din dicționar.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Soluția 6: `Deconstruct` de pereche cheie-valoare în versiunile mai vechi de C#


Struct KeyValuePair nu are funcția `Deconstruct()` în versiunile mai vechi de C# (C# 4.7.2 de mai jos) 

Așadar, dacă doriți să utilizați `Deconstruct()` pentru a buclăni perechile cheie-valoare, există o soluție de rezolvare 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

În cele mai multe cazuri nu vom folosi această metodă, dar este bine de știut.

## Soluția 7: Utilizarea funcției `dictionary.ElementAt()` și a buclei `for` 

Putem folosi o simplă buclă `for` pentru a parcurge perechile cheie-valoare din dicționar.

Putem accesa valorile `KeyValuePair` prin indexul dicționarului folosind funcția `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Din nou, nu este o modalitate bună de a face o buclă prin dicționar, deoarece funcția `ElementAt()` va avea `O(n)`, iar noi avem o buclă `for` mai sus, astfel încât complexitatea timpului va fi `O(n^2)` 

În cazul dicționarelor mari, acest lucru va avea implicații asupra performanței.

Dacă doriți să obțineți indexul perechilor cheie-valoare din dicționar, utilizați această metodă 

Nu mă gândesc la niciun caz de utilizare în lumea reală în care să fie folosit un index de dicționar 

## Soluția 8: Utilizarea C# `dictionary.AsParallel().ForAll()`

Dacă aveți un dicționar mare, putem utiliza interogarea LINQ (Parallel Language Integrated Query) folosind metoda de extensie `ParallelEnumerable.AsParallel` pe dicționar și executând interogarea prin metoda `ParallelEnumerable.ForAll`.

Interogarea partiționează sursa în sarcini care sunt executate asincron pe mai multe fire de execuție

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Cea mai bună modalitate de a face o buclă a dicționarului în C# 

Chiar dacă avem mai multe moduri de a itera peste valorile cheie ale unui dicționar, preferăm să folosim o simplă buclă foreach 

Iar dacă doriți să buclați doar cheile sau valorile dicționarului C#, utilizați `dictionary.Keys` sau `dictionary.Values` în loc să iterați întregul dicționar 







