+++
title   ="2 τρόποι μετατροπής/μετατροπής int σε enum σε C#"
summary ="Υπάρχουν 2 τρόποι για να μετατραπεί int σε enum σε C# 1. Χρησιμοποιώντας ρητή χύτευση τύπου της C#. 2. Χρησιμοποιώντας τη μέθοδο Enum.ToObject()."

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Υπάρχουν 2 τρόποι για να μετατρέψετε ή να ρίξετε το `int` σε `enum` σε C#

1. Χρησιμοποιώντας ρητή χύτευση τύπου της C#.
2. Χρήση της μεθόδου `Enum.ToObject()` 

{{%toc%}}

## Λύση 1: Χρήση ρητής διανομής τύπου C#

Ο απλός τρόπος μετατροπής του `int` σε `enum` στη C# είναι η χρήση ρητής χύτευσης τύπου.

Ας δούμε ένα παράδειγμα για να το κατανοήσουμε καλύτερα.

Έχουμε ένα `enum` τύπο που ονομάζεται `LogLevel`, ο οποίος αντιπροσωπεύει διαφορετικά επίπεδα καταγραφής.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Το ρητό casting γίνεται με την τοποθέτηση του `enum` τύπου σε παρένθεση μπροστά από την τιμή `int`.

Αλλά υπάρχει ένα πρόβλημα με το παραπάνω **C# `int` σε `enum` μετατροπή**.

Τι γίνεται αν η τιμή `int` δεν υπάρχει στη μεταβλητή C# `Enum` 

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Δεν θα πετάξει καμία εξαίρεση.

Επομένως, είναι προτιμότερο να ελέγξετε αν η τιμή `int` υπάρχει στο `C# Enum` πριν τη μετατροπή της σε ακέραιο αριθμό.

## Ελέγξτε αν ένας ακέραιος αριθμός υπάρχει ή όχι στο `C# enum` μεταβλητή

Για να πάρουμε όλες τις ακέραιες τιμές στο `C# Enum` μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Enum.GetValues`.

Μετατρέψτε τις σε λίστα `C#`, ώστε να μπορούμε να χρησιμοποιήσουμε τη μέθοδο `list.Contains()` για να ελέγξουμε αν ο συγκεκριμένος ακέραιος υπάρχει στη `enum` μεταβλητή.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Enum.IsDefined()` για να ελέγξουμε αν η μετατρεπόμενη ακέραια τιμή υπάρχει στη δεδομένη `enum` τύπο.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Λύση 2: Χρήση της μεθόδου `Enum.ToObject()` 

Μπορούμε να χρησιμοποιήσουμε τη μέθοδο `C# Enum.ToObject()`, μετατρέποντας την τιμή `int` σε `enum` σε C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





