
---
title: "C# Case insensitive Contains string ellenőrzés"
description: "Ebben a bemutatóban megtanuljuk a különböző módokat, hogy nagy- és kisbetű-érzékeny string contains ellenőrzését végezzük C#-ban"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Ebben a bemutatóban megtanuljuk a különböző módokat, hogy nagy- és kisbetű-érzékeny string contains ellenőrzés C#-ban 

Egyszerű problémának tűnik, de az alapértelmezett C# `string.Contains()` módszer nagy- és kisbetű érzékeny 

És ha a karakterlánc nem angol nyelvű, azaz más nyelvek esetében nem tudjuk közvetlenül összehasonlítani a szöveget case insensitive 

Mindkét karakterláncnak ugyanabban a kultúrában kell lennie, és ismernünk kell a nyelvi kultúrát.

Legtöbbször csak angol nyelvű karakterláncokat fogunk összehasonlítani.

## 1. módszer: C# `string.IndexOf()` módszerrel.

Használhatjuk a C# `string.IndexOf()` módszert a nagy- és kisbetűket nem érzékelő string contains ellenőrzésére.

`IndexOf()` a módszer elfogadja a `StringComparison.OrdinalIgnoreCase` paramétert, amely megadja a karakterek keresésének típusát.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## 2. módszer: A `string.Contains()` módszer használata .Net 5+ és .NET Core 2.0+ rendszerekben

A dot net legújabb verzióiban, azaz a .Net Core 2.0+ és .Net 5+ rendszerekben. A `string.Contains()` metódusnak van egy túlterhelt metódusa, amely elfogadja a `StringComparison` paramétert.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## 3. módszer: A `Regex.IsMatch()` módszer használata

A szabályos kifejezésekkel elvégezhetjük a nagy- és kisbetűket nem figyelembe vevő contains string ellenőrzést.

Ha ismeri a `Regex`, használja a `Regex.IsMatch()` módszert, és a case insensitive ellenőrzéséhez adja át a `RegexOptions.IgnoreCase` paramétert 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## 4. módszer: A `.ToUpper()` &amp `.ToLower()`

Ha a karakterláncok angol nyelvűek, és a teljesítmény nem jelent problémát, akkor mindkét karakterláncot azonos esetre konvertálhatjuk, majd elvégezhetjük a string contains ellenőrzést.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check más nyelvek esetén

Az esetek érzéketlensége nyelvfüggő 

Például az angol nyelvben a `I` a `i` nagybetűs változata.

Míg a török nyelvben a `i` nagybetűs változata a `İ` ismeretlen karaktere.

A nagy- és kisbetű-független karakterlánc-ellenőrzéshez a `CultureInfo` objektumot kell használnunk.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Létrehoztam a `CultureInfo` objektumot a török nyelvhez. És összehasonlítottam mindkét karakterláncot a `CompareInfo` segítségével, ahogy az alább látható.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## A legjobb módja a Case insensitive Contains string ellenőrzésnek

Ha a `.Net` legújabb verzióját használja, használja a `string.Contains()` módszert.

Ellenkező esetben maradj a `string.IndexOf()` módszernél.

Ne részesítse előnyben a `.ToUpper()` vagy a `To.Lower()` módszert, mivel ezek teljesítményproblémákhoz vezethetnek.

Használja a `CultureInfo` objektumot más nyelvű karakterláncokhoz.

