+++
title   ="Kako v jeziku C# pretvoriti `int` v `enum` "
summary ="Če želite v jeziku C# kastirati `int` v `enum`, izrecno vnesite cast spremenljivke `enum` v celo število."
keywords=["int v enum v C#,cast int v enum v C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Če želite v jeziku C# pretvoriti spremenljivko `int` v `enum`, izrecno vpišite cast spremenljivke `enum` v celo število.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Rešitev 1: Uporaba eksplicitnega uvajanja tipa spremenljivke `enum` 

Za boljše razumevanje si oglejmo primer.

Imamo tip `enum` z imenom `Days`, ki predstavlja dneve v tednu, začenši s ponedeljkom.

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

Vendar se pojavi težava pri zgornji pretvorbi **`int` v `enum` **.

Kaj če vrednost `int` ne obstaja v spremenljivki C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Ne bo vrgel nobene izjeme.

Zato je bolje preveriti, ali vrednost `int` obstaja v `Enum`, preden jo pretvorimo v celo število.

## Preverite, ali v spremenljivki `enum` obstaja celo število ali ne

Za pridobitev vseh celoštevilskih vrednosti v spremenljivki C# `Enum` lahko uporabimo metodo `Enum.GetValues`.

Pretvorimo jih v seznam C#, tako da lahko z metodo `list.Contains()` preverimo, ali dano celo število obstaja v spremenljivki `enum`.

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
Uporabimo lahko metodo `Enum.IsDefined()`, da preverimo, ali pretvorjena celoštevilska vrednost obstaja v danem tipu `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Rešitev 2: Uporabite metodo `Enum.ToObject()` 

Uporabimo lahko metodo `Enum.ToObject()`, s katero pretvorimo vrednost `int` v `enum` v jeziku C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





