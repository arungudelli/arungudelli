+++
title   ="Hogyan lehet a `int` -t `enum` -re vetíteni C#-ban"
summary ="A `int` egész számra történő átváltásához `enum` -re C# nyelven, explicit módon írja át a `enum` változót egész számra."
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

Ahhoz, hogy a `int` -t a `enum` -re öntse C#-ban, kifejezetten írja be a `enum` változót integerre.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## 1. megoldás: A `enum` változó explicit típusátvitelének használata

Nézzünk végig egy példát, hogy jobban megértsük.

Van egy `enum` típusunk, a `Days`, amely a hétfőtől kezdődő hétköznapokat jelöli.

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

De van egy probléma a fenti **`int` és `enum` közötti átalakítással**.

Mi van akkor, ha a `int` érték nem létezik a C# `Enum` változóban?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Nem dob semmilyen kivételt.

Tehát jobb, ha ellenőrizzük, hogy a `int` érték létezik-e a `Enum` címen, mielőtt egész számra öntjük.

## Ellenőrizze, hogy létezik-e egész szám a `enum` változóban vagy sem

A C# `Enum` összes egész szám értékének kinyeréséhez a `Enum.GetValues` metódust használhatjuk.

Konvertáljuk őket C# listává, így a `list.Contains()` módszerrel ellenőrizhetjük, hogy az adott egész szám létezik-e a `enum` változóban.

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
A `Enum.IsDefined()` módszerrel ellenőrizhetjük, hogy a konvertált egész érték létezik-e az adott `enum` típusban.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 2. megoldás: Használja a `Enum.ToObject()` módszert

Használhatjuk a `Enum.ToObject()` módszert, a `int` értéket `enum` értékké alakíthatjuk C# nyelven.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





