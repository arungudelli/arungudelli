---
title: "Comment définir une valeur par défaut pour la propriété C# ou la propriété C# auto implémentée"
description: "Dans ce tutoriel, nous apprendrons 4 façons différentes de définir une valeur par défaut pour les propriétés C# en utilisant des exemples simples"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# les propriétés ou les propriétés implémentées automatiquement sont largement utilisées dans nos classes à la place des champs, c'est-à-dire des variables.  

Les propriétés implémentées automatiquement ont été introduites dans C# 3.0.

Dans ce tutoriel, nous allons apprendre 4 façons différentes de définir la valeur par défaut des propriétés de C# en utilisant des exemples simples.

1. Utilisation des initialisateurs de propriétés automatiques dans C# 6
2. Attribuer une valeur par défaut dans le constructeur
3. Utilisation du Property Setter de C# 
4. Utilisation de `DefaultValue` Attribut &amp;&amp; Property Setter

Nous pouvons prendre la valeur par défaut comme valeur initiale de la propriété dans C#.

## Méthode 1 : Utilisation d'initialisateurs de propriétés automatiques dans C# 6

Dans C# 6, nous pouvons déclarer la propriété auto-implémentée et définir la valeur par défaut en une seule ligne de déclaration.

La syntaxe est la suivante

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
Par défaut, les propriétés de type chaîne auront la valeur `null`. En utilisant la déclaration en ligne de C# 6, nous définissons la valeur par défaut comme une chaîne vide. 

## Méthode 2 : Attribuer une valeur par défaut dans le constructeur

Dans les anciennes versions de C#, C# 5 et moins, il est recommandé de définir les valeurs par défaut des propriétés de C# dans le constructeur de la classe.

```csharp
class Product 
{
    public string Name { get; set; }
    public Product()
    {
        Name = "";
    }
}
```

## Méthode 3 : Utilisation du paramètre de propriété C# 

Nous pouvons utiliser le paramètre de propriété C# pour attribuer une valeur par défaut aux propriétés implémentées automatiquement.

```csharp
class Product 
{
    private string _name = "";
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

## méthode 4 : Utilisation de `DefaultValue` Attribute &amp;&amp; Property Setter

Dans l'exemple ci-dessus, nous avons créé une variable privée et lui avons attribué une valeur par défaut. 

Au lieu de cela, nous pouvons utiliser l'attribut `DefaultValue` pour attribuer une valeur par défaut.

```csharp
class Product 
{
    private string _name;

    [DefaultValue("")]
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

Rappelez-vous que ** l'attribut`DefaultValue` ne fonctionne qu'avec le setter de propriété.** 

Le code ci-dessous n'attribuera pas de valeur par défaut à la propriété. La valeur par défaut est toujours `null`.

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
Si vous utilisez l'attribut `DefaultValue`, vous devez utiliser le setter de propriété.


## Résumé

Si vous utilisez C# 6, utilisez la déclaration en ligne pour définir la valeur par défaut des propriétés C#, sinon définissez la valeur par défaut dans le constructeur. 








