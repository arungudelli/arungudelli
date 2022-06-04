+++
title   ="Πώς να μετατρέψετε το `int` σε `enum` σε C#"
summary ="Για να μετατρέψετε την `int` σε `enum` σε C#, κάντε ρητή μετατροπή της μεταβλητής `enum` σε ακέραιο αριθμό."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Για να cast `int` σε `enum` σε C#, ρητά τύπου cast τη μεταβλητή `enum` σε integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Λύση 1: Χρήση ρητής μετατροπής τύπου της μεταβλητής `enum` 

Ας δούμε ένα παράδειγμα για να το κατανοήσουμε καλύτερα.

Έχουμε έναν τύπο `enum` που ονομάζεται `Days`, ο οποίος αντιπροσωπεύει τις ημέρες της εβδομάδας που ξεκινούν από τη Δευτέρα.

```
public enum Days
{
        Monday,  
        Tuesday,  
        Wednesday,  
        Thursday,  
        Friday,  
        Saturday,  
        Sunday
}

int dayInteger = 6;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//Monday
```

Υπάρχει όμως ένα πρόβλημα με την παραπάνω ** μετατροπή από`int` σε `enum` **.

Τι γίνεται αν η τιμή `int` δεν υπάρχει στη μεταβλητή C# `Enum` 

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Δεν θα πετάξει καμία εξαίρεση.

Επομένως, είναι καλύτερο να ελέγξετε αν η τιμή `int` υπάρχει στο `Enum` πριν τη μετατροπή της σε ακέραιο αριθμό.

## Ελέγξτε αν ένας ακέραιος αριθμός υπάρχει ή όχι στη μεταβλητή `enum` 

Για να πάρουμε όλες τις ακέραιες τιμές στη C# `Enum` μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Enum.GetValues`.

Μετατρέψτε τις σε λίστα C#, έτσι ώστε να μπορούμε να χρησιμοποιήσουμε τη μέθοδο `list.Contains()` για να ελέγξουμε αν ο συγκεκριμένος ακέραιος υπάρχει στη μεταβλητή `enum`.

```
var intValue = 100;
var enumValues = Enum.GetValues(typeof(Days)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
  Console.WriteLine("We can Cast int to Enum");  
   Days day = (Days) intValue;
}else{
  Console.WriteLine("Cannot Cast int to Enum");
}

```
Μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Enum.IsDefined()` για να ελέγξουμε αν η μετατρεπόμενη ακέραια τιμή υπάρχει στον δεδομένο τύπο `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Λύση 2: Χρήση της μεθόδου `Enum.ToObject()` 

Μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Enum.ToObject()`, να μετατρέψουμε την τιμή `int` σε `enum` σε C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





