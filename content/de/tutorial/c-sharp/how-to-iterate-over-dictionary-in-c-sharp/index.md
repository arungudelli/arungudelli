+++
title="8 Möglichkeiten zur Schleifenbildung/Iteration von Wörterbuch-Schlüsselwertpaaren in C#"
summary="Die Verwendung der C# foreach-Schleife ist der einfachste und unkomplizierteste Weg, um über Wörterbuch-Schlüsselwerte in C# zu iterieren."
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]
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

Um Wörterbuch-Schlüssel-Wert-Paare in C# zu iterieren, verwenden Sie die folgenden Methoden

1. C# `foreach` Schleife verwenden
2. Iterieren Sie nur über C#-Wörterbuchschlüssel
3. Iterieren Sie nur über C#-Wörterbuchwerte
4. Verwendung von `Deconstruct` von `KeyValuePair<TKey,TValue>` in C# 7
5. Verwendung von `Deconstruct` und `discards` in C# 7 
6. `Deconstruct` von Schlüssel-Wert-Paar in älteren C#-Versionen
7. Verwendung der Funktion `dictionary.ElementAt()` und der Schleife `for` 
8. Verwendung von C# `dictionary.AsParallel().ForAll()` 

Lassen Sie uns ein Beispiel durchgehen, um es besser zu verstehen 

Ich habe ein Beispielwörterbuch mit `C#` for loop erstellt

Werfen Sie einen Blick auf das folgende `C#` Wörterbuch

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Lösung 1: `C# foreach` Schleife verwenden

Die `C# foreach` -Schleife ist der einfachste und unkomplizierteste Weg, um in C# über Wörterbuchschlüsselwerte zu iterieren.

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

Die Variable `dictionary` in der obigen `foreach` Schleife hat `KeyValuePair<TKey, TValue>` typ 

Wir können leicht auf die Eigenschaften `Key` und `Value` des Typs `KeyValuePair` zugreifen.

## Lösung 2: Iterieren Sie nur über C#-Wörterbuchschlüssel

Wenn Sie nur die Wörterbuchschlüssel durchlaufen wollen, verwenden Sie die C#-Wörterbuch-Eigenschaft `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Lösung 3: Iterieren Sie nur über C#-Wörterbuchwerte

Wenn Sie nur über Wörterbuchwerte iterieren möchten, verwenden Sie die C#-Wörterbuch-Eigenschaft `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Lösung 4: Verwendung von `Deconstruct()` von `KeyValuePair<TKey,TValue>` in C# 7

Dekonstruktoren werden in der Version C# 7.0 eingeführt.
 
Und wenn Sie .NET Core 2.0+ Anwendung verwenden, wird der `KeyValuePair<TKey, TValue>` typ wird `Deconstruct()` Methode haben.

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

Für den Zugriff auf das Schlüssel-Wert-Paar des Wörterbuchs verwenden Sie die Funktion `Deconstruct()` vom Typ `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Lösung 5: Verwendung von `Deconstruct` und `discards` in C# 7 

Beginnend mit C# 7.0 unterstützt C# Verwerfungen 

Discards sind Platzhaltervariablen, die im Anwendungscode absichtlich nicht verwendet werden 

Oft werden sie als Unterstrich `_` Variablen bezeichnet.

Discards sind nichts anderes als die nicht zugewiesenen Variablen, sie haben keinen Wert.

Wenn Sie im Wörterbuch nur Schlüssel in eine Schleife einfügen möchten, können Sie auf Variablen mit Verwerfungen zurückgreifen.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Ähnlich verhält es sich, wenn Sie nur Wörterbuchwerte verwenden möchten.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Lösung 6: `Deconstruct` von Schlüssel-Wert-Paar in älteren C#-Versionen


Die Struktur KeyValuePair verfügt in älteren Versionen von C# nicht über die Funktion `Deconstruct()`. (C# 4.7.2 unten) 

Wenn Sie also `Deconstruct()` verwenden möchten, um Schlüssel-Wert-Paare zu schleifen, gibt es einen Workaround 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

In den meisten Fällen werden wir diese Methode nicht verwenden, aber es ist gut zu wissen.

## Lösung 7: Verwendung der Funktion `dictionary.ElementAt()` und der Schleife `for` 

Wir können eine einfache `for` -Schleife verwenden, um über Schlüssel-Wert-Paare des Wörterbuchs zu iterieren.

Mit der Funktion `dictionary.ElementAt()` können wir über den Wörterbuchindex auf die Werte von `KeyValuePair` zugreifen.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Auch dies ist kein guter Weg, um eine Schleife durch das Wörterbuch zu machen, denn die Funktion `ElementAt()` hat `O(n)` und wir haben `for` Schleife oben, so dass die Zeitkomplexität `O(n^2)` sein wird 

Bei großen Wörterbüchern wird dies Auswirkungen auf die Leistung haben.

Wenn Sie den Index von Wörterbuch-Schlüssel-Wert-Paaren erhalten möchten, verwenden Sie diese Methode 

Mir fällt kein realer Anwendungsfall ein, bei dem der Wörterbuchindex verwendet wird 

## Lösung 8: Mit C# `dictionary.AsParallel().ForAll()`

Wenn Sie ein großes Wörterbuch haben, können wir die LINQ-Abfrage (Parallel Language Integrated Query) nutzen, indem wir die Erweiterungsmethode `ParallelEnumerable.AsParallel` auf das Wörterbuch anwenden und die Abfrage mit der Methode `ParallelEnumerable.ForAll` ausführen.

Die Abfrage unterteilt die Quelle in Aufgaben, die asynchron auf mehreren Threads ausgeführt werden

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Der beste Weg, das Wörterbuch in C# in einer Schleife laufen zu lassen 

Obwohl wir mehrere Möglichkeiten haben, über ein Wörterbuch Schlüsselwerte zu iterieren, bevorzugen mit einfachen foreach-Schleife 

Und wenn Sie Schleife nur C# Wörterbuch Schlüssel oder Werte verwenden `dictionary.Keys` oder `dictionary.Values` anstelle von Iteration gesamte Wörterbuch wollen 







