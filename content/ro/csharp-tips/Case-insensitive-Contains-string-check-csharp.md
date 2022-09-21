
---
title: "C# Case insensitive Verificarea șirului Contains"
description: "În acest tutorial vom învăța diferite moduri de a face o verificare insensibilă la case insensitive a șirului conține în C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


În acest tutorial învățăm diferite moduri de a face case insensitive string contains check în C# 

Pare o problemă simplă, dar metoda implicită C# `string.Contains()` este sensibilă la majuscule și minuscule 

Iar dacă șirul nu este în limba engleză, adică pentru alte limbi, nu putem compara direct textul fără a ține cont de majuscule și minuscule 

Ambele șiruri ar trebui să fie în aceeași cultură și ar trebui să cunoaștem cultura limbii.

De cele mai multe ori vom compara șiruri de caractere doar în limba engleză.

## Metoda 1: Utilizarea metodei C# `string.IndexOf()`.

Putem folosi metoda C# `string.IndexOf()` pentru a verifica dacă un șir de caractere conține majuscule sau minuscule.

`IndexOf()` metoda acceptă parametrul `StringComparison.OrdinalIgnoreCase`, care specifică tipul de căutare a caracterelor care trebuie utilizat.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metoda 2: Utilizarea metodei `string.Contains()` în .Net 5+ și .NET Core 2.0+

În cele mai recente versiuni de dot net, și anume în .Net Core 2.0+ și .Net 5+. Metoda `string.Contains()` are o metodă supraîncărcată care acceptă parametrul `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metoda 3: Utilizarea metodei `Regex.IsMatch()` 

Putem utiliza expresii regulate pentru a face o verificare insensibilă la majuscule și minuscule a șirului de caractere.

Dacă sunteți familiarizați cu `Regex`, utilizați metoda `Regex.IsMatch()` și pentru a verifica dacă nu este cazul treceți parametrul `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metoda 4: Utilizarea `.ToUpper()` &amp `.ToLower()`

Dacă șirurile de caractere sunt în limba engleză și dacă performanța nu este o problemă, putem converti ambele șiruri în aceeași majusculă și apoi putem face verificarea string contains.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# C# Case insensitive Contains check pentru alte limbi

Insensibilitatea la majuscule și minuscule este dependentă de limbă 

De exemplu, în limba engleză, `I` este versiunea cu majuscule a lui `i`.

În timp ce în limba turcă, versiunea cu majuscule a `i` este caracterul necunoscut `İ`.

Pentru a efectua verificarea șirurilor de caractere fără a ține cont de majuscule și minuscule, trebuie să folosim obiectul `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Am creat obiectul `CultureInfo` pentru limba turcă. Și am comparat ambele șiruri de caractere folosind `CompareInfo`, după cum se arată mai jos.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Cel mai bun mod de a face o verificare a șirului Contains insensibilă la majuscule și minuscule

Dacă utilizați cea mai recentă versiune a `.Net`, utilizați metoda `string.Contains()`.

În caz contrar, folosiți metoda `string.IndexOf()`.

Nu preferați metoda `.ToUpper()` sau `To.Lower()`, deoarece acestea pot duce la probleme de performanță.

Utilizați obiectul `CultureInfo` pentru șirurile de caractere în alte limbi.

