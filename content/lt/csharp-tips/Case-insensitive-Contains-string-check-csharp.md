
---
title: "C# Didžiųjų ir mažųjų raidžių neatspari eilutės Contains patikra"
description: "Šioje pamokoje mes sužinome įvairių būdų, kaip C# kalba patikrinti, ar eilutėje yra mažųjų ir didžiųjų raidžių neatspari eilutė."

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Šioje pamokoje mokomės įvairių būdų, kaip C# kalba patikrinti eilutę, kurioje yra, neatsižvelgiant į mažųjų ir didžiųjų raidžių skirtumus 

Atrodo, kad tai paprasta problema, tačiau numatytuoju C# `string.Contains()` metodu atsižvelgiama į mažąsias ir didžiąsias raides 

O jei eilutė yra ne anglų kalba, t. y. kitų kalbų, negalime tiesiogiai lyginti teksto, neatsižvelgdami į mažąsias ir didžiąsias raides 

Abi eilutės turi būti tos pačios kultūros ir Mes turime žinoti kalbos kultūrą.

Dažniausiai lyginsime tik anglų kalbos eilutes.

### 1 metodas: naudojant C# `string.IndexOf()` metodą.

Galime naudoti C# `string.IndexOf()` metodą, kad patikrintume, ar eilutėje yra mažųjų ir didžiųjų raidžių.

`IndexOf()` metodas priima `StringComparison.OrdinalIgnoreCase` parametrą, kuris nurodo, kokio tipo simbolių paiešką naudoti.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## 2 būdas: `string.Contains()` metodo naudojimas .NET 5+ ir .NET Core 2.0+

Naujausiose "dot net" versijose, t. y. .Net Core 2.0+ ir .Net 5+. Metodas `string.Contains()` turi perkrovimo metodą, kuris priima parametrą `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## 3 metodas: naudojant `Regex.IsMatch()` metodą

Galime naudoti reguliarias išraiškas, kad atliktume tikrinimo eilutę contains string, neatsižvelgdami į mažąjį ar didįjį raidžių skirtumą.

Jei esate susipažinę su `Regex`, naudokite `Regex.IsMatch()` metodą, o norėdami patikrinti, ar nepažeista didžioji ir mažoji raidės, perduokite `RegexOptions.IgnoreCase` parametrą 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## 4 metodas: naudojant `.ToUpper()` &amp `.ToLower()`

Jei eilutės yra anglų kalba ir našumas nėra problema, galime konvertuoti abi eilutes į tą pačią raidę, tada atlikti eilutės yra patikrinimą.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## ## C# Kitų kalbų tikrinimas "Contains", kai neatsižvelgiama į mažąją raidę

Didžiųjų ir mažųjų raidžių nejautrumas priklauso nuo kalbos 

Pavyzdžiui, anglų kalboje `I` yra `i` didžiosios raidės.

Tuo tarpu turkų kalboje didžioji `i` raidė yra nepažįstamas simbolis `İ`.

Norėdami patikrinti eilutę, neatsižvelgdami į mažąsias ir didžiąsias raides, turime naudoti objektą `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Sukūriau `CultureInfo` objektą turkų kalbai. Ir palyginau abi eilutes naudodamas `CompareInfo`, kaip parodyta toliau.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Geriausias būdas patikrinti eilutę "Contains", neatsižvelgiant į mažąsias ir didžiąsias raides

Jei naudojate naujausią `.Net` versiją, naudokite `string.Contains()` metodą.

Priešingu atveju naudokite `string.IndexOf()` metodą.

Nesirinkite `.ToUpper()` arba `To.Lower()` metodo, nes dėl jų gali kilti našumo problemų.

Kitų kalbų eilutėms naudokite `CultureInfo` objektą.

