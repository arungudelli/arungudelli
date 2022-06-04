+++
title   ="Kā C# valodā `int` pārvērst `enum` "
summary ="Lai C# valodā atveidotu `int` uz `enum`, skaidri ierakstiet mainīgo `enum` uz veselu skaitli."
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

Lai `int` pārvērstu `enum` uz C#, skaidri ierakstiet cast `enum` mainīgo uz integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## 1. risinājums: Izmantojot `enum` mainīgā tiešo tipa atveidi

Lai to labāk izprastu, aplūkosim piemēru.

Mums ir `enum` tips ar nosaukumu `Days`, kas apzīmē nedēļas dienas, sākot no pirmdienas.

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

Bet ir problēma ar iepriekš minēto **`int` uz `enum` konvertēšanu**.

Ko darīt, ja `int` vērtība nepastāv C# `Enum` mainīgajā?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Izņēmums netiks mests.

Tāpēc labāk ir pārbaudīt, vai `int` vērtība eksistē `Enum` pirms tās pārrēķināšanas uz veselu skaitli.

## Pārbaudiet, vai mainīgajā `enum` ir vesels skaitlis vai nav

Lai iegūtu visas veselu skaitļu vērtības C# `Enum`, mēs varam izmantot `Enum.GetValues` metodi.

Konvertējiet tās uz C# sarakstu, lai mēs varētu izmantot `list.Contains()` metodi, lai pārbaudītu, vai dotais veslais skaitlis pastāv `enum` mainīgajā.

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
Mēs varam izmantot `Enum.IsDefined()` metodi, lai pārbaudītu, vai konvertētā veselā skaitļa vērtība pastāv dotajā `enum` tipā.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 2. risinājums: Izmantojiet `Enum.ToObject()` metodi

Mēs varam izmantot `Enum.ToObject()` metodi, konvertēt `int` vērtību uz `enum` C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





