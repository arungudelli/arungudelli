
---
title: "C# Storleken på det okänsliga skiftläget innehåller strängkontroll"
description: "I den här handledningen lär vi oss olika sätt att göra en storleksokänslig kontroll av strängar som innehåller i C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


I den här handledningen lär vi oss olika sätt att göra case insensitive string contains check i C# 

Det ser ut som ett enkelt problem, men standardmetoden C# `string.Contains()` är skiftlägeskänslig 

Och om strängen inte är på engelska, dvs. för andra språk, kan vi inte jämföra text direkt med skiftlägeskänslig text 

Båda strängarna bör vara i samma kultur och vi bör känna till språkkulturen.

Oftast kommer vi att jämföra strängar endast på engelska.

## Metod 1: Användning av C# `string.IndexOf()` -metoden.

Vi kan använda C# `string.IndexOf()` -metoden för att kontrollera om en sträng innehåller tecken som är okänslig för stor- och småbokstäver.

`IndexOf()` metoden accepterar parametern `StringComparison.OrdinalIgnoreCase`, som anger vilken typ av sökning som ska användas för tecknen.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metod 2: Användning av `string.Contains()` -metoden i .Net 5+ &amp; .NET Core 2.0+

I de senaste versionerna av dot net, dvs. i .Net Core 2.0+ och .Net 5+. Metoden `string.Contains()` har en överladdad metod som tar emot parametern `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metod 3: Användning av `Regex.IsMatch()` -metoden

Vi kan använda reguljära uttryck för att kontrollera om en sträng innehåller en storleksordning utan att ta hänsyn till storleken.

Om du är bekant med `Regex`, använd `Regex.IsMatch()` -metoden och för att kontrollera om det är okänsligt för stor bokstavsskillnader, använd `RegexOptions.IgnoreCase` -parametern 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metod 4: Använd `.ToUpper()` &amp `.ToLower()`

Om strängarna är på engelska och det inte är något problem med prestandan kan vi konvertera båda strängarna till samma bokstavsform och sedan kontrollera att strängen innehåller.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check för andra språk

Skiftlägeskänslighet är språkberoende 

På engelska är t.ex. `I` den stora bokstavsvarianten av `i`.

På det turkiska språket är den stora bokstavsversionen av `i` det okända tecknet `İ`.

För att göra en kontroll av strängar som inte tar hänsyn till storleken måste vi använda objektet `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Jag har skapat `CultureInfo` objektet för turkiska språket. Och jämfört båda strängarna med hjälp av `CompareInfo` enligt nedan.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Bästa sättet att göra en kontroll av strängar som inte är skiftlägeskänsliga innehåller strängar

Om du använder den senaste versionen av `.Net` kan du använda metoden `string.Contains()`.

I annat fall använder du metoden `string.IndexOf()`.

Föredra inte metoderna `.ToUpper()` eller `To.Lower()` eftersom de kan leda till prestandaproblem.

Använd `CultureInfo` objektet för strängar på andra språk.

