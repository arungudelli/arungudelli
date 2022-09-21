
---
title: "C# Case insensitive Contains string check"
description: "In deze tutorial leren we verschillende manieren om case insensitive string contains check te doen in C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


In deze tutorial leren we verschillende manieren om case insensitive string contains check te doen in C# 

Het lijkt een eenvoudig probleem, maar de standaard C# `string.Contains()` methode is hoofdlettergevoelig 

En als de string niet in het Engels is, dus voor andere talen, kunnen we de tekst niet direct hoofdlettergevoelig vergelijken 

Beide strings moeten in dezelfde cultuur zijn en we moeten de taalcultuur kennen.

Meestal vergelijken we alleen strings in het Engels.

## Methode 1: C# `string.IndexOf()` methode gebruiken.

We kunnen de C# `string.IndexOf()` methode gebruiken om te controleren of een string hoofdlettergevoelig is.

`IndexOf()` de methode accepteert `StringComparison.OrdinalIgnoreCase` parameter, die aangeeft welk type zoekactie voor de tekens moet worden gebruikt.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Methode 2: `string.Contains()` methode gebruiken in .Net 5+ &amp; .NET Core 2.0+

In de nieuwste versies van dot net, d.w.z. in .Net Core 2.0+ en .Net 5+. De methode `string.Contains()` heeft een overloaded methode die `StringComparison` parameter accepteert.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Methode 3: Methode `Regex.IsMatch()` gebruiken

We kunnen reguliere expressies gebruiken om hoofdletterongevoelige stringcontrole uit te voeren.

Als u bekend bent met `Regex`, gebruikt u de methode `Regex.IsMatch()` en om te controleren op hoofdlettergevoeligheid geeft u de parameter `RegexOptions.IgnoreCase` door 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Methode 4: Gebruik `.ToUpper()` &amp `.ToLower()`

Als de strings in het Engels zijn en de prestaties geen probleem vormen, kunnen we beide strings naar dezelfde hoofdletters converteren en dan de string bevat controle uitvoeren.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check voor andere talen

Hoofdlettergevoeligheid is taalafhankelijk 

Bijvoorbeeld, in de Engelse taal is `I` de hoofdletterversie van `i`.

Terwijl in de Turkse taal de hoofdletterversie van `i` het onbekende teken `İ` is.

Voor de hoofdletterloze stringcontrole moeten we het object `CultureInfo` gebruiken.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Ik heb `CultureInfo` gemaakt voor de Turkse taal. En beide strings vergeleken met `CompareInfo` zoals hieronder getoond.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Best way to do Case insensitive Contains string check

Als u de laatste versie van `.Net` gebruikt, gebruik dan de methode `string.Contains()`.

Anders blijft u bij de methode `string.IndexOf()`.

Geef niet de voorkeur aan de methode `.ToUpper()` of `To.Lower()` omdat deze tot prestatieproblemen kunnen leiden.

Gebruik `CultureInfo` object voor strings in andere talen.

