+++
title="Πώς να ελέγξετε αν μια συμβολοσειρά είναι αριθμός σε C#"
summary="Βήματα για να ελέγξετε αν μια συμβολοσειρά είναι αριθμός σε c# 1.Δηλώστε μια ακέραια μεταβλητή. 2.Περάστε τη συμβολοσειρά στις μεθόδους `int.TryParse()` ή `double.TryParse()` με τη μεταβλητή `out`. 3.Εάν το αλφαριθμητικό είναι αριθμός η μέθοδος `TryParse` θα επιστρέψει true. Και αναθέτει τιμή στη δηλωμένη ακέραια τιμή `out`."
keywords=["check if a string is number in C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Βήματα για να ελέγξετε αν μια συμβολοσειρά είναι αριθμός στη C#

1. Δηλώστε μια ακέραια μεταβλητή.
2. Περάστε τη συμβολοσειρά στις μεθόδους `int.TryParse()` ή `double.TryParse()` με τη μεταβλητή `out`.
3. Εάν το αλφαριθμητικό είναι αριθμός, η μέθοδος `TryParse` θα επιστρέψει true. Και αναθέτει τιμή στη δηλωμένη ακέραια τιμή `out`.

{{%toc%}}

## Έλεγχος αν μια συμβολοσειρά είναι αριθμός ή όχι σε C# 

Για παράδειγμα έχουμε μια μεταβλητή συμβολοσειράς "123" και αν θέλετε να ελέγξετε αν είναι αριθμητική χρησιμοποιήστε τον παρακάτω κώδικα C#.

```
var stringNumber = "123";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is true and numericValue=123

var stringNumber = "123P";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is false and numericValue=0 default value

```

Από τη C# 7 και μετά μπορούμε να δηλώσουμε τη μεταβλητή [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) στην ίδια τη μέθοδο TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Το πρόβλημα με την παραπάνω μέθοδο `int.TryParse` είναι ότι δεν μπορεί να ελέγξει για αρνητικές τιμές αριθμού συμβολοσειράς.

## Έλεγχος για αρνητικό αριθμό συμβολοσειράς σε C# 

Για να ελέγξουμε για αρνητικές τιμές αριθμού συμβολοσειράς μπορούμε να χρησιμοποιήσουμε τη μέθοδο C# `double.TryParse()`.

```
var negativeString = "-123";
double number;
if(double.TryParse(negativeString,out number)){
   if (number > 0){

   }else{
       //negative number 
   }   
}
```

## Ο καλύτερος τρόπος για να ελέγξετε αν η συμβολοσειρά είναι αριθμός σε C# 

Χρησιμοποιείτε πάντα τη μέθοδο `double.TryParse()` για να ελέγξετε αν μια συμβολοσειρά είναι αριθμός, επειδή μπορεί να επικυρώσει τόσο θετικούς όσο και αρνητικούς αριθμούς.