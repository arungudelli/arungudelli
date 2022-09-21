+++
title   ="Πώς να λάβετε την τιμή `int` από το `Enum` σε C# με παραδείγματα"
summary ="Για να λάβετε την τιμή `int` από το `enum` σε C#, μετατρέψτε τη μεταβλητή enum σε ακέραιο αριθμό."
keywords=["int value from enum in C#,Convert string to enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Για να λάβετε την τιμή `int` από το `enum` σε C#, μετατρέψτε τη μεταβλητή `enum` σε ακέραιο αριθμό.

{{%toc%}}

## Λύση 1: Χρησιμοποιήστε Type cast για να λάβετε την τιμή `int` από την `enum`

Ο προεπιλεγμένος υποκείμενος τύπος για το `enums` στην C# είναι `Int`.

Έτσι μπορούμε να κάνουμε type cast το `enum` στο `int` για να πάρουμε την ακέραια τιμή από το enum στη C#.

Θα πάρουμε ένα παράδειγμα για να το κατανοήσουμε περαιτέρω.

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
```

Τώρα θα μετατρέψουμε τις τιμές enum σε ακέραιες τιμές.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Λύση 2: Χρησιμοποιήστε τη μέθοδο `Convert.ToInt32()` για να λάβετε την ακέραια τιμή από την enum

Ή μπορούμε να χρησιμοποιήσουμε τη μέθοδο `Convert.ToInt32()` to για να μετατρέψουμε ένα `enum` σε ακέραιο αριθμό, όπως φαίνεται παρακάτω.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Λήψη της τιμής `enum` διαφορετικών υποκείμενων τύπων

`Enums` στην C# μπορεί να έχει διαφορετικούς υποκείμενους τύπους 

Εάν η C# enum δηλώνεται ως `uint`, `long` ή `ulong` θα πρέπει να την εκχωρήσουμε στον αντίστοιχο τύπο του `enum`.

Σκεφτείτε το παρακάτω παράδειγμα του `Stars` enum, το οποίο έχει τύπο `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```