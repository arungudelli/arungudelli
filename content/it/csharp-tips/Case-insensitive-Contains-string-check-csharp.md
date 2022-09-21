
---
title: "C# Controllo stringa Contains senza distinzione tra maiuscole e minuscole"
description: "In questo tutorial impariamo diversi modi per fare il controllo delle stringhe contenenti senza distinzione tra maiuscole e minuscole in C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


In questo tutorial impariamo diversi modi per fare il controllo delle stringhe contenenti senza distinzione tra maiuscole e minuscole in C# 

Sembra un problema semplice, ma il metodo predefinito di C# `string.Contains()` è case sensitive 

E se la stringa non è in lingua inglese, cioè in altre lingue, non è possibile confrontare direttamente il testo senza distinzione tra maiuscole e minuscole 

Le due stringhe devono essere della stessa cultura e dobbiamo conoscere la cultura della lingua.

Nella maggior parte dei casi si confrontano solo stringhe in lingua inglese.

## Metodo 1: Utilizzo del metodo C# `string.IndexOf()`.

È possibile utilizzare il metodo C# `string.IndexOf()` per eseguire il controllo del contenuto delle stringhe senza distinzione tra maiuscole e minuscole.

`IndexOf()` il metodo accetta il parametro `StringComparison.OrdinalIgnoreCase`, che specifica il tipo di ricerca da utilizzare per i caratteri.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metodo 2: Utilizzo del metodo `string.Contains()` in .Net 5+ &amp; .NET Core 2.0+

Nelle ultime versioni di dot net, ovvero in .Net Core 2.0+ e .Net 5+. Il metodo `string.Contains()` ha un metodo sovraccaricato che accetta il parametro `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metodo 3: Utilizzo del metodo `Regex.IsMatch()` 

È possibile utilizzare le espressioni regolari per effettuare un controllo delle stringhe contenenti senza distinzione tra maiuscole e minuscole.

Se si ha familiarità con `Regex`, utilizzare il metodo `Regex.IsMatch()` e per verificare l'assenza di maiuscole e minuscole passare il parametro `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metodo 4: Usare `.ToUpper()` &amp `.ToLower()`

Se le stringhe sono in lingua inglese e le prestazioni non sono un problema, possiamo convertire entrambe le stringhe nello stesso caso e poi eseguire il controllo del contenuto delle stringhe.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Controllo dei contenuti senza distinzione di maiuscole e minuscole per altre lingue

L'insensibilità alle maiuscole dipende dalla lingua 

Ad esempio, nella lingua inglese `I` è la versione maiuscola di `i`.

Mentre nella lingua turca la versione maiuscola di `i` è il carattere sconosciuto `İ`.

Per effettuare il controllo delle stringhe senza distinzione tra maiuscole e minuscole, è necessario utilizzare l'oggetto `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Ho creato l'oggetto `CultureInfo` per la lingua turca. E ho confrontato entrambe le stringhe utilizzando `CompareInfo` come mostrato di seguito.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Il modo migliore per fare un controllo insensibile alle maiuscole e ai minuscoli

Se si utilizza l'ultima versione di `.Net`, utilizzare il metodo `string.Contains()`.

Altrimenti utilizzare il metodo `string.IndexOf()`.

Non preferite i metodi `.ToUpper()` o `To.Lower()` perché potrebbero causare problemi di prestazioni.

Usare l'oggetto `CultureInfo` per le stringhe di altre lingue.

