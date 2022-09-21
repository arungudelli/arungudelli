
---
title: "C# Case insensitive Contains string check"
description: "W tym tutorialu uczymy się różnych sposobów, aby zrobić case insensitive string contains check w C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


W tym tutorialu uczymy się różnych sposobów, aby zrobić case insensitive string contains check w C# 

Wygląda to na prosty problem, ale domyślna metoda C# `string.Contains()` jest wrażliwa na wielkość liter 

A jeśli ciąg nie jest w języku angielskim, tzn. dla innych języków, nie możemy porównać tekstu z rozróżnianiem wielkości liter bezpośrednio 

Oba ciągi powinny być w tej samej kulturze i powinniśmy znać kulturę języka.

W większości przypadków będziemy porównywać ciągi tylko w języku angielskim.

## Metoda 1: Użycie metody C# `string.IndexOf()`.

Możemy użyć metody C# `string.IndexOf()`, aby sprawdzić czy łańcuch zawiera wielkość liter.

`IndexOf()` metoda przyjmuje parametr `StringComparison.OrdinalIgnoreCase`, który określa typ wyszukiwania znaków.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metoda 2: Używanie metody `string.Contains()` w .Net 5+ &amp; .NET Core 2.0+

W najnowszych wersjach dot net, czyli w .Net Core 2.0+ i .Net 5+. Metoda `string.Contains()` posiada przeciążoną metodę, która akceptuje parametr `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metoda 3: Użycie metody `Regex.IsMatch()` 

Możemy użyć wyrażeń regularnych, aby wykonać niewrażliwe na wielkość liter sprawdzenie contains string.

Jeśli jesteś zaznajomiony z `Regex`, użyj metody `Regex.IsMatch()` i aby sprawdzić niewrażliwość na wielkość liter przekaż parametr `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metoda 4: Użycie `.ToUpper()` &amp `.ToLower()`

Jeśli łańcuchy są w języku angielskim i wydajność nie jest problemem, możemy przekonwertować oba łańcuchy na ten sam przypadek, a następnie wykonać sprawdzenie string contains.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check dla innych języków

Niewrażliwość na wielkość liter jest zależna od języka 

Na przykład, w języku angielskim `I` jest wielką literą wersji `i`.

Natomiast w języku tureckim duża litera wersji `i` to nieznany znak `İ`.

Aby wykonać sprawdzenie łańcucha bez uwzględniania wielkości liter musimy użyć obiektu `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Stworzyłem obiekt `CultureInfo` dla języka tureckiego. I porównałem oba ciągi za pomocą `CompareInfo`, jak pokazano poniżej.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Najlepszy sposób, aby zrobić Case insensitive Contains string check

Jeśli używasz najnowszej wersji `.Net` użyj metody `string.Contains()`.

W przeciwnym razie trzymaj się metody `string.IndexOf()`.

Nie preferuj metody `.ToUpper()` lub `To.Lower()`, ponieważ mogą one prowadzić do problemów z wydajnością.

Użyj obiektu `CultureInfo` dla ciągów w innych językach.

