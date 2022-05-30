+++
title="8 τρόποι επανάληψης/επανάληψης ζευγών τιμών κλειδιών λεξικού σε C#"
summary="Η χρήση του βρόχου foreach της C# είναι ο απλούστερος και πιο άμεσος τρόπος επανάληψης των τιμών κλειδιών λεξικού στη C#."
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

Για να επαναλάβετε ζεύγη τιμών κλειδιών λεξικού σε C# χρησιμοποιήστε τις ακόλουθες μεθόδους

1. Χρήση βρόχου C# `foreach` 
2. Επανάληψη μόνο σε κλειδιά λεξικού της C#
3. Επανάληψη μόνο σε τιμές λεξικού C#
4. Χρήση του `Deconstruct` του `KeyValuePair<TKey,TValue>` σε C# 7
5. Χρήση των `Deconstruct` και `discards` σε C# 7 
6. `Deconstruct` του ζεύγους τιμών κλειδιών σε παλαιότερες εκδόσεις της C#
7. Χρήση της συνάρτησης `dictionary.ElementAt()` και του βρόχου `for` 
8. Χρήση της C# `dictionary.AsParallel().ForAll()` 

Ας δούμε ένα παράδειγμα για να το κατανοήσουμε καλύτερα 

Έχω δημιουργήσει ένα δείγμα λεξικού χρησιμοποιώντας `C#` for loop

Ρίξτε μια ματιά στο παρακάτω λεξικό `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Λύση 1: Χρήση του βρόχου `C# foreach` 

Η χρήση του βρόχου `C# foreach` είναι ο απλούστερος και πιο άμεσος τρόπος για την επανάληψη των τιμών κλειδιών του λεξικού στη C#.

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

Η μεταβλητή `dictionary` στον παραπάνω βρόχο `foreach` θα έχει `KeyValuePair<TKey, TValue>` type 

Μπορούμε εύκολα να έχουμε πρόσβαση στις ιδιότητες `Key` &amp; `Value` του τύπου `KeyValuePair`.

## Λύση 2: Επανάληψη μόνο στα κλειδιά του λεξικού C#

Αν θέλετε να κάνετε επανάληψη μόνο πάνω από τα κλειδιά του λεξικού, χρησιμοποιήστε την ιδιότητα `dictionary.Keys` του λεξικού C#.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Λύση 3: Επανάληψη μόνο στις τιμές του λεξικού C#

Αν θέλετε να κάνετε επανάληψη μόνο σε τιμές λεξικού, χρησιμοποιήστε την ιδιότητα `dictionary.Values` του λεξικού C#.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Λύση 4: Χρήση του `Deconstruct()` της `KeyValuePair<TKey,TValue>` σε C# 7

Οι αποδομητές εισάγονται στην έκδοση C# 7.0.
 
Και αν χρησιμοποιείτε την εφαρμογή .NET Core 2.0+ η `KeyValuePair<TKey, TValue>` τύπος θα διαθέτει τη μέθοδο `Deconstruct()`.

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

Για να αποκτήσετε πρόσβαση στο ζεύγος τιμών κλειδιών του λεξικού χρησιμοποιήστε τη συνάρτηση `Deconstruct()` του τύπου `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Λύση 5: Χρήση των `Deconstruct` και `discards` σε C# 7 

Ξεκινώντας από την C# 7.0, η C# υποστηρίζει απορρίψεις 

Οι discards είναι μεταβλητές τοποθέτησης που δεν χρησιμοποιούνται σκόπιμα στον κώδικα της εφαρμογής 

Συχνά αναφέρονται ως μεταβλητές με υπογράμμιση `_`.

Οι discards δεν είναι τίποτα άλλο παρά οι μη ανατεθείσες μεταβλητές, δεν έχουν τιμή.

Στο λεξικό αν θέλετε να κάνετε βρόχο μόνο για τα Keys, μπορούμε να κάνουμε χρήση των μεταβλητών discard.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Ομοίως, αν θέλετε να χρησιμοποιήσετε μόνο τις τιμές του λεξικού.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Λύση 6: `Deconstruct` του ζεύγους τιμών κλειδιών σε παλαιότερες εκδόσεις της C#


Η δομή struct KeyValuePair δεν διαθέτει τη λειτουργία `Deconstruct()` σε παλαιότερες εκδόσεις της C#.(C# 4.7.2 παρακάτω) 

Έτσι, αν θέλετε να χρησιμοποιήσετε τη λειτουργία `Deconstruct()` για να κάνετε βρόχο σε ζεύγη τιμών κλειδιών υπάρχει μια λύση 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Στις περισσότερες περιπτώσεις δεν θα χρησιμοποιήσουμε αυτή τη μέθοδο, αλλά είναι καλό να το γνωρίζετε.

## Λύση 7: Χρήση της συνάρτησης `dictionary.ElementAt()` και του βρόχου `for` 

Μπορούμε να χρησιμοποιήσουμε τον απλό βρόχο `for` για να επαναλάβουμε τα ζεύγη κλειδιών-τιμών του λεξικού.

Μπορούμε να αποκτήσουμε πρόσβαση στις τιμές `KeyValuePair` με δείκτη λεξικού χρησιμοποιώντας τη συνάρτηση `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Και πάλι δεν είναι ένας καλός τρόπος για να κάνουμε βρόχο στο λεξικό, επειδή η συνάρτηση `ElementAt()` θα έχει `O(n)` και έχουμε `for` βρόχο παραπάνω, οπότε η χρονική πολυπλοκότητα θα είναι `O(n^2)` 

Σε μεγάλα λεξικά θα έχει επιπτώσεις στην απόδοση.

Αν θέλετε να πάρετε το δείκτη των ζευγών τιμών κλειδιών του λεξικού χρησιμοποιήστε αυτή τη μέθοδο 

Δεν μπορώ να σκεφτώ καμία περίπτωση χρήσης στον πραγματικό κόσμο όπου θα χρησιμοποιηθεί το ευρετήριο του λεξικού 

## Λύση 8: Χρήση της C# `dictionary.AsParallel().ForAll()`

Αν έχουμε ένα μεγάλο λεξικό, μπορούμε να κάνουμε χρήση του ερωτήματος Parallel Language Integrated Query (LINQ) χρησιμοποιώντας τη μέθοδο επέκτασης `ParallelEnumerable.AsParallel` στο λεξικό και εκτελώντας το ερώτημα με τη μέθοδο `ParallelEnumerable.ForAll`.

Το ερώτημα χωρίζει την πηγή σε εργασίες που εκτελούνται ασύγχρονα σε πολλαπλά νήματα

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Ο καλύτερος τρόπος για να κάνετε βρόχο στο λεξικό στην C# 

Παρόλο που έχουμε πολλαπλούς τρόπους για να επαναλάβουμε τις τιμές κλειδιών ενός λεξικού, προτιμάμε να χρησιμοποιούμε τον απλό βρόχο foreach 

Και αν θέλετε να κάνετε βρόχο μόνο για τα κλειδιά ή τις τιμές του λεξικού C# χρησιμοποιήστε το `dictionary.Keys` ή το `dictionary.Values` αντί να κάνετε επανάληψη ολόκληρου του λεξικού 







