
---
title: "C# Groß-/Kleinschreibungsunabhängige Contains-String-Prüfung"
description: "In diesem Tutorial lernen wir verschiedene Möglichkeiten, wie man in C# die Groß- und Kleinschreibung von Strings prüfen kann."
lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


In diesem Tutorial lernen wir verschiedene Möglichkeiten, um case insensitive string contains check in C# zu tun 

Es sieht aus wie ein einfaches Problem, aber die Standard-C# `string.Contains()` Methode ist case sensitive 

Und wenn die Zeichenfolge nicht in englischer Sprache ist, d.h. für andere Sprachen, können wir nicht vergleichen Text case insensitive direkt 

Die beiden Strings sollten in der gleichen Kultur sein und wir sollten die Sprachkultur kennen.

Meistens werden wir nur englischsprachige Zeichenketten vergleichen.

## Methode 1: Mit C# `string.IndexOf()` Methode.

Wir können C# `string.IndexOf()` Methode verwenden, um die Groß- und Kleinschreibung zu prüfen.

`IndexOf()` die Methode akzeptiert den Parameter `StringComparison.OrdinalIgnoreCase`, der die Art der Suche nach den Zeichen angibt.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Methode 2: Verwendung der Methode `string.Contains()` in .Net 5+ &amp; .NET Core 2.0+

In den neuesten Versionen von Dot Net, d.h. in .Net Core 2.0+ und .Net 5+. Die Methode `string.Contains()` hat eine überladene Methode, die den Parameter `StringComparison` akzeptiert.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Methode 3: Verwendung der Methode `Regex.IsMatch()` 

Wir können reguläre Ausdrücke verwenden, um die Groß-/Kleinschreibung bei der Prüfung von Zeichenketten zu berücksichtigen.

Wenn Sie mit `Regex` vertraut sind, verwenden Sie die Methode `Regex.IsMatch()` und übergeben Sie den Parameter `RegexOptions.IgnoreCase`, um die Groß-/Kleinschreibung zu prüfen 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Methode 4: Verwendung von `.ToUpper()` &amp `.ToLower()`

Wenn die Zeichenketten in englischer Sprache sind und die Leistung kein Problem darstellt, können wir beide Zeichenketten in dieselbe Groß-/Kleinschreibung konvertieren und dann die Prüfung auf "String enthält" durchführen.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check für andere Sprachen

Groß- und Kleinschreibung ist sprachabhängig 

In der englischen Sprache ist beispielsweise `I` die Großbuchstabenversion von `i`.

In der türkischen Sprache hingegen ist die Großschreibung von `i` das unbekannte Zeichen `İ`.

Um die Groß-/Kleinschreibung zu prüfen, müssen wir das Objekt `CultureInfo` verwenden.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Ich habe das Objekt `CultureInfo` für die türkische Sprache erstellt. Und verglichen beide Zeichenfolgen mit `CompareInfo` wie unten gezeigt.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Der beste Weg, um Groß-/Kleinschreibung nicht zu beachten, ist die Prüfung von Contains string

Wenn Sie die neueste Version von `.Net` verwenden, benutzen Sie die Methode `string.Contains()`.

Ansonsten bleiben Sie bei der Methode `string.IndexOf()`.

Bevorzugen Sie nicht die Methoden `.ToUpper()` oder `To.Lower()`, da diese zu Leistungsproblemen führen können.

Verwenden Sie das Objekt `CultureInfo` für Zeichenketten anderer Sprachen.

