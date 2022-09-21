+++
title   ="Wie castet man `int` nach `enum` in C#"
summary ="Um `int` in `enum` in C# zu casten, casten Sie die Variable `enum` explizit in eine Ganzzahl."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Um `int` nach `enum` in C# zu casten, geben Sie explizit cast der Variable `enum` nach integer ein.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Lösung 1: Verwendung der expliziten Typisierung der Variablen `enum` 

Lassen Sie uns ein Beispiel durchgehen, um es besser zu verstehen.

Wir haben einen Typ `enum` mit dem Namen `Days`, der die Wochentage beginnend mit Montag darstellt.

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

Es gibt jedoch ein Problem mit der obigen **`int` zu `enum` Umwandlung**.

Was ist, wenn der Wert `int` nicht in der C#-Variable `Enum` vorhanden ist?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Es wird keine Ausnahme ausgelöst.

Es ist also besser zu prüfen, ob der Wert `int` in `Enum` existiert, bevor er in eine Ganzzahl umgewandelt wird.

## Prüfen, ob eine Ganzzahl in der Variablen `enum` existiert oder nicht

Um alle Integer-Werte in C# `Enum` zu erhalten, können wir die Methode `Enum.GetValues` verwenden.

Konvertieren Sie sie in eine C#-Liste, so dass wir mit der Methode `list.Contains()` prüfen können, ob die angegebene Ganzzahl in der Variablen `enum` vorhanden ist.

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
Mit der Methode `Enum.IsDefined()` können wir prüfen, ob der konvertierte Integer-Wert im angegebenen Typ `enum` vorhanden ist.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Lösung 2: Methode `Enum.ToObject()` verwenden

Wir können die Methode `Enum.ToObject()` verwenden, um den Wert `int` in `enum` in C# zu konvertieren.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





