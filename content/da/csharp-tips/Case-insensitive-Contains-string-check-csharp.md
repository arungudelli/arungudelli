
---
title: "C# Case insensitive Contains string check"
description: "I denne tutorial lærer vi forskellige måder at lave case insensitive string contains check i C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


I denne tutorial lærer vi forskellige måder at lave case insensitive string contains check i C# 

Det ser ud som et simpelt problem, men standardmetoden C# `string.Contains()` er case sensitive 

Og hvis strengen ikke er på engelsk, dvs. for andre sprog, kan vi ikke sammenligne tekst case insensitive direkte 

Begge strenge skal være i samme kultur, og vi skal kende sprogkulturen.

De fleste gange vil vi kun sammenligne strenge på engelsk sprog.

## Metode 1: Brug af C# `string.IndexOf()` metoden.

Vi kan bruge C# `string.IndexOf()` -metoden til at foretage en kontrol af, om en streng indeholder en case insensitive streng.

`IndexOf()` metoden accepterer parameteren `StringComparison.OrdinalIgnoreCase`, som angiver den type søgning, der skal bruges til at søge efter tegnene.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metode 2: Brug af `string.Contains()` -metoden i .Net 5+ &amp; .NET Core 2.0+

I de nyeste versioner af dot net, dvs. i .Net Core 2.0+ og .Net 5+. Metoden `string.Contains()` har en overloaded metode, som accepterer `StringComparison` parameteren.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metode 3: Brug af `Regex.IsMatch()` -metoden

Vi kan bruge regulære udtryk til at foretage case insensitive contains string check.

Hvis du er bekendt med `Regex`, skal du bruge `Regex.IsMatch()` -metoden og for at kontrollere, om der ikke er forskel på store og små bogstaver, skal du bruge `RegexOptions.IgnoreCase` -parameteren 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metode 4: Brug af `.ToUpper()` &amp `.ToLower()`

Hvis strengene er på engelsk, og ydelsen ikke er et problem, kan vi konvertere begge strenge til samme kasus og derefter kontrollere, at strengen indeholder.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check for andre sprog

Kasusafhængighed er sprogafhængigt 

På engelsk er `I` f.eks. den store bogstavsudgave af `i`.

På det tyrkiske sprog er den store bogstavsversion af `i` det ukendte tegn `İ`.

For at foretage en kontrol af en streng uden hensyn til store og små bogstaver skal vi bruge `CultureInfo` -objektet.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Jeg har oprettet `CultureInfo` objektet for det tyrkiske sprog. Og sammenlignet begge strenge ved hjælp af `CompareInfo` som vist nedenfor.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Bedste måde at udføre case insensitive Contains string check

Hvis du bruger den nyeste version af `.Net`, skal du bruge `string.Contains()` -metoden.

Ellers skal du holde dig til `string.IndexOf()` -metoden.

Du bør ikke foretrække `.ToUpper()` eller `To.Lower()`, da de kan give problemer med ydeevnen.

Brug `CultureInfo` -objektet til strenge på andre sprog.

