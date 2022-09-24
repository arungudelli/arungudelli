
+++
title="Πώς να λάβετε το όνομα enum από την τιμή σε C#"
summary="Υπάρχουν δύο τρόποι για να λάβετε το όνομα enum από την τιμή σε C# 1. Χρησιμοποιήστε την C# `Enum.GetName()` και περάστε την τιμή enum ως παράμετρο για να λάβετε το όνομα. 2. Μετατρέψτε την τιμή enum στο μέλος enumeration χρησιμοποιώντας casting και στη συνέχεια χρησιμοποιήστε τη μέθοδο `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Μια από τις δημοφιλείς περιπτώσεις χρήσης του enum είναι να λάβετε το όνομα enum από την τιμή του.

Σκεφτείτε ένα πραγματικό παράδειγμα, γενικά θα αποθηκεύσουμε τιμές enum στη βάση δεδομένων. δηλ. θα αποθηκεύσουμε μόνο ακέραιες τιμές 

Και αφού διαβάσουμε την τιμή enum από τη βάση δεδομένων, πρέπει να την μετατρέψουμε πίσω στο όνομά της enum.

Υπάρχουν **δύο τρόποι για να πάρουμε το όνομα enum από την τιμή στη C#** 

{{%toc%}}

## Λύση 1: Χρησιμοποιώντας `Enum.GetName()`

Η συνάρτηση `Enum.GetName()` της C# λαμβάνει δύο παραμέτρους enum type και value και επιστρέφει το όνομα enum.

Πάρτε ένα παράδειγμα της `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Τώρα θα περάσουμε την τιμή enum στο `Enum.GetName()` για να λάβουμε το όνομα enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Εάν χρησιμοποιείτε την έκδοση C# `.Net 6`, μπορείτε να περάσετε μόνο την τιμή enum (cast σε enum) στη μέθοδο `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Λύση 2: Χρήση του type casting

Ένας άλλος τρόπος είναι να, Μετατρέψτε την τιμή enum στο μέλος enumeration χρησιμοποιώντας casting και στη συνέχεια χρησιμοποιήστε τη μέθοδο `ToString()`.

Αυτός είναι ένας απλός τρόπος που δεν χρησιμοποιεί καμία ενσωματωμένη συνάρτηση `C# Enum`.

Πρώτα μετατρέψτε την τιμή enum στο μέλος enumeration και στη συνέχεια χρησιμοποιήστε τη μέθοδο `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Περίληψη

Σε αυτό το σεμινάριο μάθαμε διαφορετικούς τρόπους για να λάβουμε την τιμή του ονόματος enum σε c# 

1. Περνώντας τις παραμέτρους enum type και value στη μέθοδο `Enum.GetName()` 
2. Και χρησιμοποιώντας τη μετατροπή τύπου σε αντίστοιχο τύπο enum 
