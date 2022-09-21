
---
title: "C# Vérification insensible à la casse de la chaîne de caractères contains"
description: "Dans ce tutoriel, nous apprenons différentes façons de faire une vérification insensible à la casse des chaînes de caractères en C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Dans ce tutoriel, nous apprenons différentes façons de vérifier si une chaîne de caractères est sensible à la casse et contient une chaîne de caractères en C# 

Cela semble être un problème simple, mais la méthode par défaut de C# `string.Contains()` est sensible à la casse 

Et si la chaîne n'est pas en langue anglaise, c'est-à-dire pour d'autres langues, nous ne pouvons pas comparer directement le texte en respectant la casse 

Les deux chaînes de caractères doivent être dans la même culture et nous devons connaître la culture de la langue.

La plupart du temps, nous comparons des chaînes de caractères en anglais uniquement.

## Méthode 1 : Utilisation de la méthode C# `string.IndexOf()`.

Nous pouvons utiliser la méthode C# `string.IndexOf()` pour vérifier la présence de chaînes de caractères sans tenir compte de la casse.

`IndexOf()` la méthode accepte le paramètre `StringComparison.OrdinalIgnoreCase`, qui spécifie le type de recherche à utiliser pour les caractères.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Méthode 2 : Utilisation de la méthode `string.Contains()` dans .Net 5+ &amp; .NET Core 2.0+

Dans les dernières versions de dot net, c'est-à-dire dans .Net Core 2.0+ et .Net 5+. La méthode `string.Contains()` possède une méthode surchargée qui accepte le paramètre `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Méthode 3 : Utilisation de la méthode `Regex.IsMatch()` 

Nous pouvons utiliser des expressions régulières pour effectuer une vérification insensible à la casse des chaînes de caractères.

Si vous êtes familier avec `Regex`, utilisez la méthode `Regex.IsMatch()` et pour vérifier la sensibilité à la casse, passez le paramètre `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Méthode 4 : Utilisation de `.ToUpper()` &amp `.ToLower()`

Si les chaînes sont en anglais et que la performance n'est pas un problème, nous pouvons convertir les deux chaînes à la même casse puis effectuer la vérification de la présence de chaînes.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check for other languages (vérification du contenu sans tenir compte de la casse pour les autres langues)

L'insensibilité à la casse dépend de la langue 

Par exemple, en langue anglaise, `I` est la version en majuscules de `i`.

Alors que dans la langue turque, la version en majuscules de `i` est le caractère inconnu `İ`.

Pour vérifier la chaîne de caractères sans tenir compte de la casse, nous devons utiliser l'objet `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

J'ai créé l'objet `CultureInfo` pour la langue turque. Et j'ai comparé les deux chaînes de caractères en utilisant `CompareInfo` comme indiqué ci-dessous.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Meilleur moyen de vérifier les chaînes de caractères sans tenir compte de la casse

Si vous utilisez la dernière version de `.Net`, utilisez la méthode `string.Contains()`.

Sinon, utilisez la méthode `string.IndexOf()`.

Ne préférez pas les méthodes `.ToUpper()` ou `To.Lower()` car elles peuvent entraîner des problèmes de performance.

Utilisez l'objet `CultureInfo` pour les chaînes de caractères des autres langues.

