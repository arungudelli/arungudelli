+++
title   ="Jak rzutować `int` na `enum` w C#"
summary ="Aby rzutować `int` na `enum` w C#, jawnie wpisz rzutowanie zmiennej `enum` na liczbę całkowitą."
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

Aby zamienić `int` na `enum` w języku C#, należy jawnie zamienić zmienną `enum` na liczbę całkowitą.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Rozwiązanie 1: Użycie jawnego rzutowania typu zmiennej `enum` 

Prześledźmy przykład, aby lepiej to zrozumieć.

Mamy typ `enum` o nazwie `Days`, który reprezentuje dni tygodnia zaczynające się od poniedziałku.

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

Istnieje jednak problem z powyższą **konwersją`int` na `enum` **.

Co zrobić, jeśli wartość `int` nie istnieje w zmiennej C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Nie spowoduje to rzucenia żadnego wyjątku.

Dlatego lepiej jest sprawdzić, czy wartość `int` istnieje w `Enum`, zanim zamienimy ją na liczbę całkowitą.

## Sprawdź, czy liczba całkowita istnieje czy nie w zmiennej `enum` 

Aby uzyskać wszystkie wartości całkowite w C# `Enum`, możemy użyć metody `Enum.GetValues`.

Przekonwertuj je na listę w języku C#, tak abyśmy mogli użyć metody `list.Contains()` do sprawdzenia, czy dana liczba całkowita istnieje w zmiennej `enum`.

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
Możemy użyć metody `Enum.IsDefined()`, aby sprawdzić, czy przekonwertowana wartość całkowita istnieje w podanym typie `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Rozwiązanie 2: Użyj metody `Enum.ToObject()` 

Możemy użyć metody `Enum.ToObject()`, aby przekonwertować wartość `int` na `enum` w języku C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





