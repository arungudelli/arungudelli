
---
title: "C# Case insensitive Contains string check"
description: "Selles õpetuses õpime erinevaid viise, kuidas teha suur- ja väiketähelepanuta stringi sisaldab kontrolli C# keeles"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Selles õpetuses õpime erinevaid viise, kuidas teha suur- ja väiketundlikku stringi sisaldab kontrollimist C# keeles 

Tundub lihtne probleem, kuid C# `string.Contains()` meetod on vaikimisi suur- ja väiketundlik 

Ja kui string ei ole inglise keeles, st teiste keelte puhul ei saa me otseselt võrrelda teksti case insensitive 

Mõlemad stringid peaksid olema samas kultuuris ja me peaksime teadma keele kultuuri.

Enamasti võrdleme ainult ingliskeelseid stringisid.

## Meetod 1: Kasutades C# `string.IndexOf()` meetodit.

Me võime kasutada C# `string.IndexOf()` meetodit, et teha suur- ja väiketähelepanuta string contains check.

`IndexOf()` meetod võtab vastu parameetri `StringComparison.OrdinalIgnoreCase`, mis määrab, millist tüüpi otsingut kasutatakse märkide jaoks.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Meetod 2: meetodi `string.Contains()` kasutamine .Net 5+ ja .NET Core 2.0+ versioonides

Viimastes dot net versioonides, st .Net Core 2.0+ ja .Net 5+. `string.Contains()` meetodil on ülekoormatud meetod, mis võtab vastu parameetri `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Meetod 3: `Regex.IsMatch()` meetodi kasutamine

Me võime kasutada regulaarseid väljendeid, et teha suur- ja väiketähelepanuta sisaldab stringi kontrolli.

Kui olete tuttav `Regex`, kasutage `Regex.IsMatch()` meetodit ja kontrollige suur- ja väiketähelepanu kontrollimiseks andke parameeter `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Meetod 4: Kasutades `.ToUpper()` &amp `.ToLower()`

Kui stringid on inglise keeles ja jõudlus ei ole probleemiks, võime konverteerida mõlemad stringid samasse korpusesse ja seejärel teha string contains check.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check teiste keelte puhul

Suur- ja väiketähenduslikkus on keelest sõltuv 

Näiteks inglise keeles on `I` suurtähtedega versioon `i`.

Türgi keeles on aga suurtähtedega versioon `i` tundmatu tähemärk `İ`.

Suur- ja väiketähtedeta stringi kontrollimiseks peame kasutama `CultureInfo` objekti.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Olen loonud `CultureInfo` objekti türgi keele jaoks. Ja võrdlesin mõlemat stringi kasutades `CompareInfo` nagu allpool näidatud.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Parim viis teha Case insensitive Contains string check

Kui kasutate `.Net` uusimat versiooni, kasutage `string.Contains()` meetodit.

Vastasel juhul kasutage `string.IndexOf()` meetodit.

Ärge eelistage `.ToUpper()` või `To.Lower()` meetodit, kuna need võivad põhjustada probleeme jõudlusega.

Kasutage `CultureInfo` objekti teiste keelte stringide jaoks.

