+++
title   ="2 būdai, kaip C# konvertuoti/atversti int į enum "
summary ="Yra 2 būdai, kaip C# konvertuoti int į enum 1. Naudojant C# aiškųjį tipų atvaizdavimą. 2. 2. Naudojant Enum.ToObject() metodą."

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Yra 2 būdai, kaip konvertuoti arba paversti `int` į `enum` c# kalba

1. Naudojant C# aiškiai išreikštą tipų atvaizdavimą.
2. Naudojant `Enum.ToObject()` metodą

{{%toc%}}

## 1 sprendimas: naudojant C# aiškaus tipo atvaizdavimą

Paprastas būdas konvertuoti `int` į `enum` c# kalba - naudoti aiškų tipo atvaizdavimą.

Kad geriau jį suprastume, panagrinėkime pavyzdį.

Turime `enum` tipą, pavadintą `LogLevel`, kuris reiškia skirtingus registravimo lygius.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Aiškus atvaizdavimas atliekamas dedant `enum` tipą skliausteliuose prieš `int` reikšmę.

Tačiau yra problema, kai pirmiau **C# `int` į `enum` konvertavimu**.

Ką daryti, jei `int` reikšmės nėra C# `Enum` kintamajame?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Tai nesukels jokių išimčių.

Todėl prieš atmetant į sveikąjį skaičių geriau patikrinti, ar `int` reikšmė egzistuoja `C# Enum`.

## Patikrinkite, ar sveikasis skaičius egzistuoja, ar ne `C# enum` kintamajame

Norėdami gauti visas sveikųjų skaičių reikšmes `C# Enum`, galime naudoti `Enum.GetValues` metodą.

Konvertuokite jas į `C#` sąrašą, kad galėtume `list.Contains()` metodu patikrinti, ar duotas sveikasis skaičius egzistuoja `enum` kintamajame.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Galime naudoti `Enum.IsDefined()` metodą, kad patikrintume, ar konvertuota sveikojo skaičiaus reikšmė egzistuoja duotame `enum` tipą.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 2 sprendimas: naudokite `Enum.ToObject()` metodą

Galime naudoti `C# Enum.ToObject()` metodą, konvertuoti `int` reikšmę į `enum` c# kalba.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





