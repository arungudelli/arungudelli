
---
title: "C# Kontrola řetězce Contains bez ohledu na velikost písmen"
description: "V tomto tutoriálu se naučíme různé způsoby, jak v jazyce C# provádět kontrolu řetězce contains bez rozlišení velikosti písmen."

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


V tomto tutoriálu se naučíme různé způsoby, jak provést kontrolu řetězce obsahuje bez ohledu na velikost písmen v jazyce C# 

Vypadá to jako jednoduchý problém, ale výchozí metoda C# `string.Contains()` rozlišuje malá a velká písmena 

A pokud řetězec není v češtině, tj. pro jiné jazyky, nemůžeme porovnávat text bez rozlišení velikosti písmen přímo 

Oba řetězce by měly být ve stejné kultuře a My bychom měli znát kulturu jazyka.

Většinou budeme porovnávat řetězce pouze v anglickém jazyce.

## Metoda 1: Použití metody C# `string.IndexOf()`.

Pro kontrolu řetězce obsahuje bez rozlišení velikosti písmen můžeme použít metodu C# `string.IndexOf()`.

`IndexOf()` metoda přijímá parametr `StringComparison.OrdinalIgnoreCase`, který určuje typ vyhledávání, který se má použít pro znaky.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metoda 2: Použití metody `string.Contains()` v sítích .Net 5+ a .NET Core 2.0+

V nejnovějších verzích dot net, tj. v .Net Core 2.0+ a .Net 5+. Metoda `string.Contains()` má přetíženou metodu, která přijímá parametr `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metoda 3: Použití metody `Regex.IsMatch()` 

Pro kontrolu řetězce contains bez rozlišení velikosti písmen můžeme použít regulární výrazy.

Pokud znáte metodu `Regex`, použijte metodu `Regex.IsMatch()` a pro kontrolu nerozlišování velkých a malých písmen předejte parametr `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metoda 4: Použití `.ToUpper()` &amp `.ToLower()`

Pokud jsou řetězce v anglickém jazyce a výkon není problém, můžeme oba řetězce převést na stejná velká a malá písmena a poté provést kontrolu řetězce obsahuje.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Kontrola obsahuje bez ohledu na velikost písmen pro ostatní jazyky

Necitlivost na malá a velká písmena je závislá na jazyce 

Například v angličtině `I` je velkých písmen verze `i`.

Zatímco v tureckém jazyce je velkým písmenem verze `i` neznámý znak `İ`.

Abychom mohli provést kontrolu řetězce bez rozlišení velikosti písmen, musíme použít objekt `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Vytvořil jsem objekt `CultureInfo` pro turečtinu. A porovnal jsem oba řetězce pomocí `CompareInfo`, jak je uvedeno níže.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Nejlepší způsob, jak provést kontrolu řetězce Contains bez ohledu na velikost písmen

Pokud používáte nejnovější verzi `.Net`, použijte metodu `string.Contains()`.

V opačném případě se držte metody `string.IndexOf()`.

Nedávejte přednost metodě `.ToUpper()` nebo `To.Lower()`, protože mohou vést k problémům s výkonem.

Pro řetězce jiných jazyků použijte objekt `CultureInfo`.

