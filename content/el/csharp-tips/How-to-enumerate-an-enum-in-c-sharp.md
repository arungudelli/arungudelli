---
title: "Πώς να κάνετε βρόχο/αρίθμηση C# enum"
description: "Διαφορετικοί τρόποι βρόχου ή απαρίθμησης C# enum με παραδείγματα"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Τα enums χρησιμοποιούνται ευρέως στη γλώσσα `C#`. 

Και υπάρχουν 4 τρόποι για να κάνετε βρόχο ή απαρίθμηση enum στο `C#`. 

1. Χρήση του `C# Enum.GetValues()` σε .Net 5 και άνω.
2. Χρήση του `C# Enum.GetValues()` σε παλαιότερες εκδόσεις .Net.
3. Χρήση του `C# Enum.GetNames()` για την απαρίθμηση ονομάτων απαρίθμησης ως συμβολοσειρές.
4. Χρήση του `Linq`

Ας δούμε ένα παράδειγμα για να το κατανοήσουμε καλύτερα. 

Πρώτα θα δημιουργήσουμε μια C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

Το `enum` αντιπροσωπεύει διαφορετικούς τύπους επιπέδων καταγραφής.

Τώρα θα δούμε διαφορετικούς τρόπους απαρίθμησης του `C# enum`.

## Χρήση της μεθόδου `C# Enum.GetValues()` Generic σε .Net 5 και άνω

Εάν χρησιμοποιείτε την τελευταία έκδοση του `.Net`, δηλαδή το `.Net 5` και πάνω, μπορείτε να χρησιμοποιήσετε τη γενική έκδοση για τη μέθοδο `Enum.GetValues` για να κάνετε βρόχο στο `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Η νέα γενική έκδοση της `Enum.GetValues` επιστρέφει τον πίνακα τιμών enum. 

Και επιπλέον μπορούμε να χρησιμοποιήσουμε τις εντολές `for` ή `foreach` για να απαριθμήσουμε το `C# enum`. 

Καθώς ο πίνακας περιέχει τον τύπο `enum` πρέπει να τον μετατρέψουμε σε συμβολοσειρά χρησιμοποιώντας τη μέθοδο `ToString()`.

## Χρήση του `C# Enum.GetValues()` σε παλαιότερες εκδόσεις .Net.

Στις παλαιότερες εκδόσεις του `.Net` δεν υπάρχει διαθέσιμη γενική μέθοδος για τη μέθοδο `Enum.GetValues()`. 

Πρέπει να περάσετε το `typeof()` enum ως παράμετρο στη μέθοδο `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Και αυτή επιστρέφει τιμές enum τύπου `System.Array` και περαιτέρω μπορούμε να χρησιμοποιήσουμε την εντολή `foreach` για να κάνουμε βρόχο μέσα από το enum της C#.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Εάν θέλετε αποτέλεσμα `IEnumerable`, μπορούμε να εκθέσουμε περαιτέρω τη μέθοδο `Enum.GetValues()`.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## Χρήση του `C# Enum.GetNames()` για την απαρίθμηση ονομάτων απαρίθμησης ως συμβολοσειρές 

`C# Enum.GetValues()` η μέθοδος επιστρέφει πίνακα τύπων enum. 

Γι' αυτό μετατρέψαμε τις τιμές enum σε συμβολοσειρά πριν τις εκτυπώσουμε στην κονσόλα.

Χρησιμοποιώντας τη μέθοδο `C# Enum.GetNames()` μπορούμε να απαριθμήσουμε τα ονόματα enum ως συμβολοσειρές, ώστε να μην απαιτείται η μετατροπή τους σε συμβολοσειρές.

Εάν χρησιμοποιείτε τη μέθοδο `.Net 5` και άνω, μπορείτε να χρησιμοποιήσετε τη γενική συνάρτηση `C# Enum.GetNames()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Στις παλαιότερες εκδόσεις πρέπει να περάσετε την παράμετρο `typeof()` enum.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Έτσι, αν θέλετε να βιδώσετε τα ονόματα enum ως συμβολοσειρές, μπορούμε να χρησιμοποιήσουμε τη μέθοδο `C# Enum.GetNames()`.

## Χρησιμοποιώντας τη μέθοδο `Linq`

Μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Linq forEach` για να απαριθμήσουμε τα enum της C#, με τη βοήθεια των μεθόδων `Enum.GetValues()` και `Enum.GetNames()`.

Στο `.Net 5` και πάνω χρησιμοποιήστε το παρακάτω απόσπασμα κώδικα.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

Στις παλαιότερες εκδόσεις

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Περίληψη

Σε αυτό το σεμινάριο μάθαμε να κάνουμε βρόχο σε enum στη C# χρησιμοποιώντας τις μεθόδους `Enum.GetValues()` και `Enum.GetNames()`.










