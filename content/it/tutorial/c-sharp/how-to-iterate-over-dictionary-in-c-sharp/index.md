+++
title="8 modi per eseguire il loop/iterare coppie di valori chiave di dizionari in C#"
summary="L'uso del ciclo foreach in C# è il modo più semplice e diretto per iterare sui valori chiave del dizionario in C#."
keywords=["loop del dizionario in C#, iterare il dizionario in C#, loop delle chiavi del dizionario, loop dei valori del dizionario"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Per iterare le coppie chiave-valore del dizionario in C#, utilizzare i seguenti metodi

1. Utilizzando il ciclo C# `foreach` 
2. Iterare solo sulle chiavi del dizionario C#
3. Iterare solo sui valori del dizionario C#
4. Utilizzo di `Deconstruct` di `KeyValuePair<TKey,TValue>` in C# 7
5. Utilizzo di `Deconstruct` e `discards` in C# 7 
6. `Deconstruct` della coppia chiave-valore nelle versioni precedenti di C#
7. Utilizzo della funzione `dictionary.ElementAt()` e del ciclo `for` 
8. Utilizzo di C# `dictionary.AsParallel().ForAll()` 

Vediamo un esempio per capire meglio 

Ho creato un dizionario di esempio usando il ciclo for di `C#` 

Date un'occhiata al dizionario `C#` qui sotto

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Soluzione 1: Usare il ciclo `C# foreach` 

L'uso del ciclo `C# foreach` è il modo più semplice e diretto per iterare i valori delle chiavi del dizionario in C#.

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

La variabile `dictionary` nel ciclo `foreach` di cui sopra avrà `KeyValuePair<TKey, TValue>` tipo 

Possiamo accedere facilmente alle proprietà `Key` e `Value` del tipo `KeyValuePair`.

## Soluzione 2: Iterare solo sulle chiavi del dizionario C#

Se si desidera eseguire il loop solo sulle chiavi del dizionario, utilizzare la proprietà `dictionary.Keys` del dizionario C#.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Soluzione 3: Iterare solo sui valori del dizionario C#

Se si desidera iterare solo sui valori del dizionario, utilizzare la proprietà `dictionary.Values` del dizionario C#.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Soluzione 4: Utilizzo di `Deconstruct()` di `KeyValuePair<TKey,TValue>` in C# 7

I decostruttori sono stati introdotti nella versione 7.0 di C#.
 
Se si utilizza l'applicazione .NET Core 2.0+, il tipo `KeyValuePair<TKey, TValue>` avrà il metodo `Deconstruct()`.

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

Per accedere alla coppia chiave-valore del dizionario, utilizzare la funzione `Deconstruct()` del tipo `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Soluzione 5: Utilizzo di `Deconstruct` e `discards` in C# 7 

A partire da C# 7.0, C# supporta gli scarti 

Gli scarti sono variabili segnaposto che sono intenzionalmente inutilizzate nel codice dell'applicazione 

Spesso vengono chiamate variabili underscore `_`.

Gli scarti non sono altro che variabili non assegnate, che non hanno un valore.

Nel dizionario, se si desidera eseguire un ciclo solo sulle chiavi, si possono utilizzare le variabili di scarto.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Allo stesso modo, se si vogliono utilizzare solo i valori del dizionario.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Soluzione 6: `Deconstruct` della coppia chiave-valore nelle vecchie versioni di C#


La struct KeyValuePair non ha la funzione `Deconstruct()` nelle versioni più vecchie di C#.(C# 4.7.2 sotto) 

Pertanto, se si desidera utilizzare `Deconstruct()` per eseguire il loop delle coppie chiave-valore, esiste una soluzione 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Nella maggior parte dei casi non utilizzeremo questo metodo, ma è bene saperlo.

## Soluzione 7: Utilizzo della funzione `dictionary.ElementAt()` e del ciclo `for` 

Possiamo usare il semplice ciclo `for` per iterare le coppie chiave-valore del dizionario.

Possiamo accedere ai valori di `KeyValuePair` tramite l'indice del dizionario usando la funzione `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Anche in questo caso non è un buon modo per fare il loop del dizionario, perché la funzione `ElementAt()` avrà `O(n)` e noi abbiamo `for` loop sopra, quindi la complessità temporale sarà `O(n^2)` 

In caso di dizionari di grandi dimensioni, ciò avrà implicazioni sulle prestazioni.

Se si desidera ottenere l'indice delle coppie chiave-valore del dizionario, utilizzare questo metodo 

Non mi viene in mente alcun caso d'uso reale in cui venga utilizzato l'indice del dizionario 

## Soluzione 8: Utilizzo di C# `dictionary.AsParallel().ForAll()`

Se si dispone di un dizionario di grandi dimensioni, è possibile utilizzare la query Parallel Language Integrated Query (LINQ) utilizzando il metodo di estensione `ParallelEnumerable.AsParallel` sul dizionario ed eseguendo la query con il metodo `ParallelEnumerable.ForAll`.

La query suddivide l'origine in task che vengono eseguiti in modo asincrono su più thread

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Il modo migliore per eseguire il loop del dizionario in C# 

Anche se esistono diversi modi per iterare sui valori delle chiavi di un dizionario, preferiamo usare il semplice ciclo foreach 

E se si desidera eseguire il loop solo sulle chiavi o sui valori del dizionario C#, utilizzare `dictionary.Keys` o `dictionary.Values` invece di iterare l'intero dizionario 







