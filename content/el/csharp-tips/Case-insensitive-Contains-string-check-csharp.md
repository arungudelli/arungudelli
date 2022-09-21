
---
title: "C# Έλεγχος συμβολοσειράς Contains χωρίς ευαισθησία στην πεζότητα"
description: "Σε αυτό το σεμινάριο μαθαίνουμε διαφορετικούς τρόπους για να κάνουμε case insensitive έλεγχο συμβολοσειράς contains σε C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Σε αυτό το σεμινάριο μαθαίνουμε διαφορετικούς τρόπους για να κάνουμε case insensitive string contains check σε C# 

Μοιάζει με ένα απλό πρόβλημα, αλλά η προεπιλεγμένη μέθοδος `string.Contains()` της C# είναι ευαίσθητη στην πεζότητα 

Και αν η συμβολοσειρά δεν είναι στην αγγλική γλώσσα, δηλαδή για άλλες γλώσσες, δεν μπορούμε να συγκρίνουμε κείμενο case insensitive άμεσα 

Οι δύο συμβολοσειρές θα πρέπει να είναι στην ίδια κουλτούρα και θα πρέπει να γνωρίζουμε την κουλτούρα της γλώσσας.

Τις περισσότερες φορές θα συγκρίνουμε συμβολοσειρές μόνο στην αγγλική γλώσσα.

## Μέθοδος 1: Χρήση της μεθόδου C# `string.IndexOf()`.

Μπορούμε να χρησιμοποιήσουμε τη μέθοδο C# `string.IndexOf()` για να κάνουμε έλεγχο της συμβολοσειράς που περιέχει, χωρίς να λαμβάνουμε υπόψη την πεζότητα.

`IndexOf()` η μέθοδος δέχεται την παράμετρο `StringComparison.OrdinalIgnoreCase`, η οποία καθορίζει τον τύπο αναζήτησης που θα χρησιμοποιηθεί για τους χαρακτήρες.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Μέθοδος 2: Χρήση της μεθόδου `string.Contains()` σε .Net 5+ &amp; .NET Core 2.0+

Στις τελευταίες εκδόσεις της dot net, δηλαδή στις εκδόσεις .Net Core 2.0+ και .Net 5+. Η μέθοδος `string.Contains()` έχει μια υπερφορτωμένη μέθοδο η οποία δέχεται την παράμετρο `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Μέθοδος 3: Χρήση της μεθόδου `Regex.IsMatch()` 

Μπορούμε να χρησιμοποιήσουμε κανονικές εκφράσεις για να κάνουμε έλεγχο συμβολοσειράς contains χωρίς ευαισθησία στην πεζότητα.

Αν είστε εξοικειωμένοι με τη μέθοδο `Regex`, χρησιμοποιήστε τη μέθοδο `Regex.IsMatch()` και για να ελέγξετε την έλλειψη ευαισθησίας στην πεζότητα περάστε την παράμετρο `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Μέθοδος 4: Χρήση του `.ToUpper()` &amp `.ToLower()`

Εάν τα αλφαριθμητικά είναι στην αγγλική γλώσσα και η απόδοση δεν αποτελεί πρόβλημα, μπορούμε να μετατρέψουμε και τα δύο αλφαριθμητικά στην ίδια περίπτωση και στη συνέχεια να κάνουμε τον έλεγχο του αλφαριθμητικού contains.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Έλεγχος Contains χωρίς ευαισθησία στην πεζότητα για άλλες γλώσσες

Η έλλειψη ευαισθησίας στην πεζότητα εξαρτάται από τη γλώσσα 

Για παράδειγμα, στην αγγλική γλώσσα `I` είναι η έκδοση με κεφαλαία γράμματα του `i`.

Ενώ στην τουρκική γλώσσα η έκδοση με κεφαλαία γράμματα του `i` είναι ο άγνωστος χαρακτήρας `İ`.

Για να κάνουμε τον έλεγχο συμβολοσειράς χωρίς πεζά γράμματα πρέπει να χρησιμοποιήσουμε το αντικείμενο `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Έχω δημιουργήσει το αντικείμενο `CultureInfo` για την τουρκική γλώσσα. Και συνέκρινα και τις δύο συμβολοσειρές χρησιμοποιώντας το `CompareInfo` όπως φαίνεται παρακάτω.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Καλύτερος τρόπος για να κάνετε έλεγχο συμβολοσειράς Contains χωρίς ευαισθησία στην πεζότητα

Εάν χρησιμοποιείτε την τελευταία έκδοση του `.Net` χρησιμοποιήστε τη μέθοδο `string.Contains()`.

Διαφορετικά χρησιμοποιήστε τη μέθοδο `string.IndexOf()`.

Μην προτιμάτε τη μέθοδο `.ToUpper()` ή `To.Lower()` καθώς μπορεί να οδηγήσουν σε προβλήματα απόδοσης.

Χρησιμοποιήστε το αντικείμενο `CultureInfo` για συμβολοσειρές άλλων γλωσσών.

