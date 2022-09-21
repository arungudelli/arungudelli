+++
title="8 façons de boucler/itérer des paires clé-valeur de dictionnaire en C#"
summary="L'utilisation de la boucle foreach en C# est le moyen le plus simple et le plus direct d'itérer sur des valeurs de clés de dictionnaire en C#."
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

Pour itérer les paires clé-valeur du dictionnaire en C#, utilisez les méthodes suivantes

1. Utilisation de la boucle C# `foreach` 
2. Itération sur les clés du dictionnaire C# uniquement
3. Itération sur les valeurs du dictionnaire C# uniquement
4. Utilisation de `Deconstruct` de `KeyValuePair<TKey,TValue>` en C# 7
5. Utilisation de `Deconstruct` et `discards` en C# 7 
6. `Deconstruct` de la paire clé-valeur dans les anciennes versions de C#
7. Utilisation de la fonction `dictionary.ElementAt()` et de la boucle `for` 
8. Utilisation de C# `dictionary.AsParallel().ForAll()` 

Prenons un exemple pour mieux comprendre 

J'ai créé un exemple de dictionnaire en utilisant la boucle for `C#` 

Jetez un coup d'oeil au dictionnaire ci-dessous `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Solution 1 : Utilisation de la boucle `C# foreach` 

L'utilisation de la boucle `C# foreach` est le moyen le plus simple et le plus direct d'itérer sur les valeurs des clés d'un dictionnaire en C#.

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

La variable `dictionary` dans la boucle `foreach` ci-dessus sera de `KeyValuePair<TKey, TValue>` type 

Nous pouvons facilement accéder aux propriétés `Key` &amp; `Value` du type `KeyValuePair`.

## Solution 2 : Itérer sur les clés du dictionnaire C# uniquement

Si vous souhaitez effectuer une boucle uniquement sur les clés du dictionnaire, utilisez la propriété `dictionary.Keys` du dictionnaire C#.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Solution 3 : Itération sur les valeurs du dictionnaire C# uniquement

Si vous souhaitez itérer uniquement sur les valeurs du dictionnaire, utilisez la propriété C# dictionary `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Solution 4 : Utilisation de `Deconstruct()` de `KeyValuePair<TKey,TValue>` en C# 7

Les déconstructeurs sont introduits dans la version C# 7.0.
 
Et si vous utilisez l'application .NET Core 2.0+, le type `KeyValuePair<TKey, TValue>` aura la méthode `Deconstruct()`.

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

Pour accéder à la paire clé-valeur du dictionnaire, utilisez la fonction `Deconstruct()` du type `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Solution 5 : Utilisation de `Deconstruct` et `discards` en C# 7 

À partir de C# 7.0, C# prend en charge les rejets 

Les rejets sont des variables de type placeholder qui sont intentionnellement inutilisées dans le code de l'application 

Elles sont souvent appelées variables underscore `_`.

Les discards ne sont rien d'autre que des variables non assignées, elles n'ont pas de valeur.

Dans le dictionnaire, si l'on veut boucler uniquement les clés, on peut utiliser les variables de rejet.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
De même si vous voulez utiliser uniquement les valeurs du dictionnaire.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Solution 6 : `Deconstruct` de la paire clé-valeur dans les anciennes versions de C#


La structure KeyValuePair ne dispose pas de la fonction `Deconstruct()` dans les anciennes versions de C# (C# 4.7.2 ci-dessous) 

Donc, si vous voulez utiliser `Deconstruct()` pour boucler les paires clé-valeur, il existe une solution de contournement 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Dans la plupart des cas, nous n'utiliserons pas cette méthode, mais il est bon de le savoir.

## Solution 7 : Utilisation de la fonction `dictionary.ElementAt()` et de la boucle `for` 

Nous pouvons utiliser la simple boucle `for` pour itérer sur les paires clé-valeur du dictionnaire.

Nous pouvons accéder aux valeurs de `KeyValuePair` par l'index du dictionnaire en utilisant la fonction `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Encore une fois, ce n'est pas une bonne façon de boucler à travers le dictionnaire, parce que la fonction `ElementAt()` aura `O(n)` et nous avons `for` boucle ci-dessus donc la complexité du temps sera `O(n^2)` 

Dans les grands dictionnaires, cela aura des conséquences sur les performances.

Si vous voulez obtenir l'index des paires clé-valeur du dictionnaire, utilisez cette méthode 

Je ne pense pas qu'il y ait un cas d'utilisation réel où l'index du dictionnaire sera utilisé 

## Solution 8 : Utilisation de C# `dictionary.AsParallel().ForAll()`

Si vous avez un grand dictionnaire, nous pouvons utiliser la requête LINQ (Parallel Language Integrated Query) en utilisant la méthode d'extension `ParallelEnumerable.AsParallel` sur le dictionnaire et en exécutant la requête à l'aide de la méthode `ParallelEnumerable.ForAll`.

La requête divise la source en tâches qui sont exécutées de manière asynchrone sur plusieurs threads

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Meilleure façon de boucler le dictionnaire en C# 

Bien que nous ayons plusieurs façons d'itérer sur les valeurs des clés d'un dictionnaire, nous préférons utiliser la simple boucle foreach 

Et si vous voulez boucler uniquement les clés ou les valeurs d'un dictionnaire C#, utilisez `dictionary.Keys` ou `dictionary.Values` au lieu d'itérer sur tout le dictionnaire 







