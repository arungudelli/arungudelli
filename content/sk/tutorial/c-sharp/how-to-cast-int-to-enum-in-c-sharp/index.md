+++
title   ="Ako odovzdať `int` na `enum` v jazyku C#"
summary ="Ak chcete v jazyku C# vykonať cast `int` na `enum`, explicitne zadajte cast premennej `enum` na celé číslo."
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

Ak chcete v jazyku C# castovať premennú `int` na `enum`, explicitne zadajte cast premennej `enum` na celé číslo.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Riešenie 1: Použitie explicitného typového zápisu premennej `enum` 

Prejdime si príklad, aby sme ho lepšie pochopili.

Máme typ `enum` s názvom `Days`, ktorý reprezentuje dni v týždni počnúc pondelkom.

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

Vyskytol sa však problém s vyššie uvedenou **konverziou`int` na `enum` **.

Čo ak hodnota `int` v premennej C# `Enum` neexistuje?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Nevyhodí to žiadnu výnimku.

Preto je lepšie skontrolovať, či hodnota `int` existuje v `Enum`, skôr než ju prevediete na celé číslo.

## Skontrolujte, či v premennej `enum` existuje celé číslo alebo nie

Na získanie všetkých celočíselných hodnôt v C# `Enum` môžeme použiť metódu `Enum.GetValues`.

Prevedieme ich na zoznam v jazyku C#, aby sme mohli pomocou metódy `list.Contains()` skontrolovať, či dané celé číslo existuje v premennej `enum`.

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
Metódu `Enum.IsDefined()` môžeme použiť na kontrolu, či konvertovaná celočíselná hodnota existuje v danom type `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Riešenie 2: Použite metódu `Enum.ToObject()` 

Môžeme použiť metódu `Enum.ToObject()`, ktorou v jazyku C# prevedieme hodnotu `int` na `enum`.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





