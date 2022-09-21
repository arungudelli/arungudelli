+++
title   ="Wie erhält man den Wert `int` von `Enum` in C# mit Beispielen"
summary ="Um den Wert `int` von `enum` in C# zu erhalten, wandeln Sie die enum-Variable in eine Ganzzahl um."
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

Um den Wert `int` von `enum` in C# zu erhalten, wandeln Sie die Variable `enum` in eine ganze Zahl um.

{{%toc%}}

## Lösung 1: Verwenden Sie Type cast, um den Wert `int` von `enum`

Der standardmäßig zugrunde liegende Typ für `enums` in C# ist `Int`.

So können wir den `enum` Typ in `int` umwandeln, um den Integer-Wert von enum in C# zu erhalten.

Wir werden ein Beispiel nehmen, um es weiter zu verstehen.

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

Jetzt werden wir Enum-Werte in Integer-Werte umwandeln.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Lösung 2: Verwenden Sie die Methode `Convert.ToInt32()`, um den Integer-Wert von enum zu erhalten

Oder wir können die Methode `Convert.ToInt32()` to verwenden, um eine `enum` in eine Ganzzahl zu konvertieren, wie unten gezeigt.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Abrufen des `enum` Wertes von verschiedenen zugrundeliegenden Typen

`Enums` in C# können verschiedene zugrundeliegende Typen haben 

Wenn C# enum als `uint`, `long`, oder `ulong` deklariert ist, sollten wir es auf den entsprechenden Typ der `enum` übertragen.

Betrachten Sie das folgende Beispiel von `Stars` enum, das einen Typ `long` hat.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```