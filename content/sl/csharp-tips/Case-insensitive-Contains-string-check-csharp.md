
---
title: "C# Preverjanje niza Contains brez upoštevanja velikosti črk"
description: "V tem učbeniku se naučimo različnih načinov preverjanja nizov contains v jeziku C#, ki ne upošteva velikih in malih črk."

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


V tem učbeniku se naučimo različnih načinov za preverjanje verige vsebuje v jeziku C#, pri katerih ni občutljiv na velikost črk 

Zdi se, da gre za preprost problem, vendar je privzeta metoda C# `string.Contains()` občutljiva na velike in male črke 

In če niz ni v angleškem jeziku, tj. za druge jezike, ne moremo neposredno primerjati besedila brez upoštevanja velikosti črk 

Oba niza morata biti v isti kulturi in poznati moramo jezikovno kulturo.

Največkrat bomo primerjali nize samo v angleškem jeziku.

### Metoda 1: Uporaba metode C# `string.IndexOf()`.

Uporabimo lahko metodo C# `string.IndexOf()` za preverjanje vsebnosti nizov brez upoštevanja velikosti črk.

`IndexOf()` metoda sprejema parameter `StringComparison.OrdinalIgnoreCase`, ki določa vrsto iskanja, ki naj se uporabi za znake.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metoda 2: Uporaba metode `string.Contains()` v .Net 5+ in .NET Core 2.0+

V najnovejših različicah dot net, tj. v .Net Core 2.0+ in .Net 5+. Metoda `string.Contains()` ima preobremenjeno metodo, ki sprejme parameter `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metoda 3: Uporaba metode `Regex.IsMatch()` 

Z uporabo regularnih izrazov lahko preverimo, ali niz vsebuje velikost črk ni občutljiv na velikost črk.

Če poznate metodo `Regex`, uporabite metodo `Regex.IsMatch()` in za preverjanje neobčutljivosti velikosti prenesite parameter `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metoda 4: Uporaba `.ToUpper()` &amp `.ToLower()`

Če sta niza v angleškem jeziku in zmogljivost ni problematična, lahko oba niza pretvorimo v enake velikosti in nato preverimo, ali niz vsebuje.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Preverjanje vsebnosti brez upoštevanja velikosti črk za druge jezike

Neobčutljivost na velikost je odvisna od jezika 

Na primer, v angleškem jeziku je `I` različica `i` z velikimi črkami.

Medtem ko je v turškem jeziku velika črka različice `i` neznani znak `İ`.

Za preverjanje niza brez upoštevanja velikosti črk moramo uporabiti predmet `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Za turški jezik sem ustvaril objekt `CultureInfo`. Oba niza sem primerjal z uporabo `CompareInfo`, kot je prikazano spodaj.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Najboljši način za preverjanje niza Contains brez upoštevanja velikosti črk

Če uporabljate najnovejšo različico `.Net`, uporabite metodo `string.Contains()`.

V nasprotnem primeru se držite metode `string.IndexOf()`.

Ne uporabljajte raje metod `.ToUpper()` ali `To.Lower()`, saj lahko povzročita težave pri delovanju.

Za nize v drugih jezikih uporabite predmet `CultureInfo`.

