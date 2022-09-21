+++
title   ="Cum se transformă `int` în `enum` în C#"
summary ="Pentru a transforma `int` în `enum` în C#, scrieți explicit cast-ul variabilei `enum` în integer."
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

Pentru a transforma `int` în `enum` în C#, scrieți explicit cast the `enum` variable to integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Soluția 1: Utilizarea distribuției explicite a tipului de variabilă `enum` 

Să analizăm un exemplu pentru a înțelege mai bine.

Avem un tip `enum` numit `Days`, care reprezintă zilele săptămânii începând de luni.

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

Dar există o problemă cu conversia **`int` în `enum` de mai sus**.

Ce se întâmplă dacă valoarea `int` nu există în variabila C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Nu se va arunca nicio excepție.

Așadar, este mai bine să verificați dacă valoarea `int` există în `Enum` înainte de a o transforma în număr întreg.

## Verificați dacă există sau nu un număr întreg în variabila `enum` 

Pentru a obține toate valorile întregi în C# `Enum` putem folosi metoda `Enum.GetValues`.

Conversia lor în listă C#, astfel încât să putem folosi metoda `list.Contains()` pentru a verifica dacă numărul întreg dat există în variabila `enum`.

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
Putem utiliza metoda `Enum.IsDefined()` pentru a verifica dacă valoarea întreagă convertită există în tipul `enum` dat.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Soluția 2: Utilizați metoda `Enum.ToObject()` 

Putem utiliza metoda `Enum.ToObject()`, pentru a converti valoarea `int` în `enum` în C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





