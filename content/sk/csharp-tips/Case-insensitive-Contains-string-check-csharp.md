
---
title: "C# Kontrola reťazca Contains bez ohľadu na veľkosť písmen"
description: "V tomto tutoriáli sa naučíme rôzne spôsoby, ako v jazyku C# vykonať kontrolu reťazca contains bez rozlišovania veľkých a malých písmen"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


V tomto tutoriáli sa naučíme rôzne spôsoby, ako v jazyku C# vykonať kontrolu reťazca obsahuje bez ohľadu na veľkosť písmen 

Vyzerá to ako jednoduchý problém, ale predvolená metóda C# `string.Contains()` rozlišuje veľkosť písmen 

A ak reťazec nie je v slovenčine, t. j. v prípade iných jazykov, nemôžeme priamo porovnávať text bez ohľadu na veľkosť písmen 

Oba reťazce by mali byť v rovnakej kultúre a My by sme mali poznať kultúru jazyka.

Väčšinou budeme porovnávať reťazce len v anglickom jazyku.

## Metóda 1: Použitie metódy C# `string.IndexOf()`.

Na vykonanie kontroly reťazca obsahuje bez ohľadu na veľkosť písmen môžeme použiť metódu C# `string.IndexOf()`.

`IndexOf()` metóda prijíma parameter `StringComparison.OrdinalIgnoreCase`, ktorý určuje typ vyhľadávania, ktorý sa má použiť pre znaky.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metóda 2: Použitie metódy `string.Contains()` v prostredí .Net 5+ a .NET Core 2.0+

V najnovších verziách dot net, t. j. v .Net Core 2.0+ a .Net 5+. Metóda `string.Contains()` má preťaženú metódu, ktorá prijíma parameter `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metóda 3: Použitie metódy `Regex.IsMatch()` 

Na kontrolu reťazca contains bez rozlišovania veľkosti písmen môžeme použiť regulárne výrazy.

Ak poznáte metódu `Regex`, použite metódu `Regex.IsMatch()` a na kontrolu nerozlišovania veľkých a malých písmen odovzdajte parameter `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metóda 4: Použitie `.ToUpper()` &amp `.ToLower()`

Ak sú reťazce v anglickom jazyku a výkon nie je problém, môžeme oba reťazce previesť na rovnaké veľké a malé písmená a potom vykonať kontrolu reťazca obsahuje.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Kontrola Contains bez zohľadnenia veľkosti písmen pre iné jazyky

Necitlivosť na veľkosť písmen závisí od jazyka 

Napríklad v angličtine `I` je verzia `i` s veľkými písmenami.

Zatiaľ čo v tureckom jazyku je veľkým písmenom verzia `i` neznámy znak `İ`.

Ak chceme vykonať kontrolu reťazca bez rozlišovania veľkých a malých písmen, musíme použiť objekt `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Vytvoril som objekt `CultureInfo` pre turecký jazyk. A porovnal som oba reťazce pomocou `CompareInfo`, ako je uvedené nižšie.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Najlepší spôsob, ako vykonať kontrolu reťazca Contains bez ohľadu na veľkosť písmen

Ak používate najnovšiu verziu `.Net`, použite metódu `string.Contains()`.

V opačnom prípade zostaňte pri metóde `string.IndexOf()`.

Nepreferujte metódu `.ToUpper()` alebo `To.Lower()`, pretože môžu viesť k problémom s výkonom.

Pre reťazce iných jazykov použite objekt `CultureInfo`.

