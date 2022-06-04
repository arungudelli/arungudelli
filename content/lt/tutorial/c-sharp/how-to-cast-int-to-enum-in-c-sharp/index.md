+++
title   ="Kaip C# kalba paversti `int` į `enum` "
summary ="Norėdami C# kalba `int` paversti į `enum`, aiškiai įveskite `enum` kintamąjį į sveiką skaičių."
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

Norėdami C# kalba `int` paversti į `enum`, aiškiai įveskite cast `enum` kintamąjį į sveiką skaičių.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## 1 sprendimas: Naudojant aiškų `enum` kintamojo tipo atvaizdavimą

Kad geriau suprastume, panagrinėkime pavyzdį.

Turime `enum` tipą, pavadintą `Days`, kuris žymi savaitės dienas, prasidedančias pirmadieniu.

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

Tačiau kyla problema dėl pirmiau minėto **`int` konvertavimo į `enum` **.

Ką daryti, jei `int` reikšmė neegzistuoja C# `Enum` kintamajame?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Tai nesukels jokių išimčių.

Todėl prieš atmetant į sveikąjį skaičių geriau patikrinti, ar `int` reikšmė egzistuoja `Enum`.

## Patikrinkite, ar `enum` kintamajame yra sveikasis skaičius, ar ne

Norėdami gauti visas sveikojo skaičiaus reikšmes C# `Enum`, galime naudoti `Enum.GetValues` metodą.

Konvertuokite jas į C# sąrašą, kad galėtume `list.Contains()` metodu patikrinti, ar `enum` kintamajame egzistuoja nurodytas sveikasis skaičius.

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
Galime naudoti `Enum.IsDefined()` metodą, kad patikrintume, ar konvertuota sveikojo skaičiaus reikšmė egzistuoja duotame `enum` tipe.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 2 sprendimas: naudokite `Enum.ToObject()` metodą

Galime naudoti `Enum.ToObject()` metodą, konvertuoti `int` reikšmę į `enum` C# kalba.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





