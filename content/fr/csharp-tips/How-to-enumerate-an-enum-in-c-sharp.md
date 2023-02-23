---
title: "Comment enumerate C# enum"
description: " Différentes façons de enumerate C# enum avec des exemples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Les Enums sont largement utilisés dans le langage `C#`. 

Il existe 4 façons d'utiliser enumerate enum dans `C#`. 

1. Utilisation de `C# Enum.GetValues()` dans .Net 5 et plus.
2. Utilisation de `C# Enum.GetValues()` dans les anciennes versions de .Net.
3. Utilisation de `C# Enum.GetNames()` pour enumerater les noms enum en tant que chaînes de caractères.
4. Utilisation de `Linq`

Prenons un exemple pour mieux comprendre. 

Tout d'abord, nous allons créer un fichier C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

Le site `enum` représente différents types de niveaux de journalisation.

Nous allons maintenant voir différentes manières de enumerate the `C# enum`.

## Utilisation de la méthode générique `C# Enum.GetValues()` dans .Net 5 et plus

Si vous utilisez la dernière version de `.Net`, c'est-à-dire `.Net 5` et plus, vous pouvez utiliser la version générique de la méthode `Enum.GetValues` pour enumerate the `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

La nouvelle version générique de `Enum.GetValues` renvoie le tableau des valeurs de enum. 

Et nous pouvons utiliser les instructions `for` ou `foreach` pour lister les noms `C# enum` noms. 

Comme le tableau contient le type `enum` nous devons le convertir en chaîne de caractères en utilisant la méthode `ToString()`.

## Utilisation de `C# Enum.GetValues()` dans les anciennes versions de .Net.

Dans les anciennes versions de `.Net`, il n'y a pas de méthode générique disponible pour la méthode `Enum.GetValues()`. 

Vous devez passer `typeof()` enum comme paramètre à la méthode `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Celle-ci renvoie enum valeurs de type `System.Array` et nous pouvons ensuite utiliser l'instruction `foreach` pour parcourir les noms en boucle `C# enum` noms.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Si vous souhaitez obtenir le résultat `IEnumerable`, nous pouvons utiliser la méthode `Enum.GetValues()`.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## Utilisation de `C# Enum.GetNames()` pour enumériger enum noms en chaînes de caractères 

`C# Enum.GetValues()` la méthode renvoie un tableau de types enum. 

C'est pourquoi nous avons converti les noms enum en chaînes de caractères avant de les imprimer dans la console.

En utilisant la méthode `C# Enum.GetNames()`, nous pouvons enumerater les noms enum en tant que chaînes de caractères, de sorte qu'il n'est pas nécessaire de les convertir en chaînes de caractères.

Si vous utilisez `.Net 5` et plus, vous pouvez utiliser la fonction générique `C# Enum.GetNames()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Dans les anciennes versions, nous devons passer le paramètre `typeof()` enum .

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

 enumAinsi, si vous souhaitez obtenir des noms sous forme de chaînes de caractères, vous pouvez utiliser la méthode `C# Enum.GetNames()`.

## En utilisant `Linq`

Nous pouvons utiliser la méthode `Linq forEach` pour enumerate C# enum, avec l'aide des méthodes `Enum.GetValues()` et `Enum.GetNames()`.

À partir de `.Net 5`, utilisez l'extrait de code ci-dessous.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

Dans les versions plus anciennes

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Résumé

Dans ce tutoriel, nous avons appris à créer enumerate enum en C# en utilisant les méthodes `Enum.GetValues()` et `Enum.GetNames()`.










