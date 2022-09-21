+++
title   ="Jak v jazyce C# převést adresu `int` na adresu `enum` "
summary ="Chcete-li v jazyce C# provést cast `int` na `enum`, explicitně zadejte cast proměnné `enum` na celé číslo."
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

Chcete-li v jazyce C# provést cast `int` na `enum`, explicitně zadejte cast proměnné `enum` na celé číslo.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Řešení 1: Použití explicitního odlitku typu proměnné `enum` 

Projděme si příklad, abychom jej lépe pochopili.

Máme typ `enum` s názvem `Days`, který reprezentuje dny v týdnu počínaje pondělím.

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

S výše uvedeným **`int` na `enum` převodem** je však problém.

Co když hodnota `int` v proměnné C# `Enum` neexistuje?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Nevyhodí žádnou výjimku.

Proto je lepší před převedením na celé číslo zkontrolovat, zda hodnota `int` existuje v `Enum`.

## Zkontrolujte, zda v proměnné `enum` existuje celé číslo, nebo ne

Pro získání všech celočíselných hodnot v proměnné C# `Enum` můžeme použít metodu `Enum.GetValues`.

Převedeme je na seznam v jazyce C#, abychom mohli pomocí metody `list.Contains()` zkontrolovat, zda dané celé číslo existuje v proměnné `enum`.

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
Metodu `Enum.IsDefined()` můžeme použít k tomu, abychom zkontrolovali, zda převedená celočíselná hodnota existuje v daném typu `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Řešení 2: Použijte metodu `Enum.ToObject()` 

Můžeme použít metodu `Enum.ToObject()`, která převede hodnotu `int` na `enum` v jazyce C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





