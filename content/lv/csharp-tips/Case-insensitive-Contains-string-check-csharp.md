
---
title: "C# Uz lietām nejūtīga lietussargu nesaturoša satur virknes pārbaude"
description: "Šajā pamācībā mēs mācāmies dažādus veidus, kā veikt uz mazajiem un lielajiem burtiem nejūtīgu virknes satur pārbaudi C# valodā"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Šajā pamācībā mēs mācāmies dažādus veidus, kā veikt uz mazajiem un lielajiem burtiem neievērojošu virknes satur pārbaudi C# valodā 

Izskatās, ka tā ir vienkārša problēma, bet noklusējuma C# `string.Contains()` metodei ir lielo un mazo burtu atšķirība 

Un, ja virkne nav angļu valodā, t. i., citās valodās, mēs nevaram tieši salīdzināt tekstu, neņemot vērā mazo un lielo izmēru 

Abām virknēm jābūt vienas un tās pašas kultūras, un mums jāzina valodas kultūra.

Lielākoties mēs salīdzinām virknes tikai angļu valodā.

### 1. metode: izmantojot C# `string.IndexOf()` metodi.

Mēs varam izmantot C# `string.IndexOf()` metodi, lai pārbaudītu, vai virkne satur maznozīmīgu virkni.

`IndexOf()` metode pieņem `StringComparison.OrdinalIgnoreCase` parametru, kas norāda meklēšanas veidu, kas jāizmanto rakstzīmēm.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## 2. metode: `string.Contains()` metodes izmantošana .Net 5+ un .NET Core 2.0+ lietojumprogrammā

Jaunākajās dot net versijās, t. i., .Net Core 2.0+ un .Net 5+. Metodei `string.Contains()` ir pārslogota metode, kas pieņem parametru `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## 3. metode: izmantojot `Regex.IsMatch()` metodi

Mēs varam izmantot regulārās izteiksmes, lai pārbaudītu, vai virkne satur maznozīmīgu virkni.

Ja esat iepazinušies ar `Regex`, izmantojiet `Regex.IsMatch()` metodi, un, lai pārbaudītu, vai nav jānorāda lieli un mazie burti, nododiet `RegexOptions.IgnoreCase` parametru 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## 4. metode: Izmantojot `.ToUpper()` &amp `.ToLower()`

Ja virknes ir angļu valodā un veiktspēja nav problēma, mēs varam konvertēt abas virknes vienā un tajā pašā gadījumā un pēc tam veikt pārbaudi, vai virkne satur.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
### C# C# Lietošanas gadījuma nejūtīga pārbaude "satur" citās valodās

Lietošanas mazjūtība pret mazajiem un lielajiem burtiem ir atkarīga no valodas 

Piemēram, angļu valodā `I` ir `i` lielo burtu versija.

Turku valodā `i` lielais burts ir nepazīstams raksturs `İ`.

Lai pārbaudītu virknes maznozīmju pārbaudi, mums jāizmanto objekts `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Es esmu izveidojis `CultureInfo` objektu turku valodai. Un salīdzināju abas virknes, izmantojot `CompareInfo`, kā parādīts zemāk.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Labākais veids, kā pārbaudīt, vai virkne satur maznozīmīgu lietvārdu un burtu virkni

Ja izmantojat jaunāko `.Net` versiju, izmantojiet `string.Contains()` metodi.

Pretējā gadījumā izmantojiet `string.IndexOf()` metodi.

Nelietojiet `.ToUpper()` vai `To.Lower()` metodi, jo tās var radīt veiktspējas problēmas.

Citu valodu virknēm izmantojiet `CultureInfo` objektu.

