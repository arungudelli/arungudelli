+++
title   ="Hur man kastar `int` till `enum` i C#"
summary ="Om du vill kasta `int` till `enum` i C# skriver du uttryckligen casten av variabeln `enum` till heltal."
keywords=["int till enum i C#,cast int till enum i C#"]
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

Om du vill omvandla `int` till `enum` i C# ska du uttryckligen skriva casta variabeln `enum` till heltal.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Lösning 1: Använd explicit typgjutning av `enum` -variabeln

Låt oss gå igenom ett exempel för att förstå det bättre.

Vi har en `enum` -typ som heter `Days`, som representerar veckodagar som börjar med måndag.

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

Men det finns ett problem med ovanstående **omvandling från`int` till `enum` **.

Vad händer om värdet `int` inte finns i variabeln `Enum` i C#?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Det kommer inte att skapa något undantag.

Det är alltså bättre att kontrollera om värdet `int` finns i `Enum` innan det kastas till ett heltal.

## Kontrollera om det finns ett heltal eller inte i variabeln `enum` 

För att få fram alla heltalsvärden i C# `Enum` kan vi använda metoden `Enum.GetValues`.

Konvertera dem till en C#-lista så att vi kan använda `list.Contains()` -metoden för att kontrollera om det givna heltalet finns i `enum` -variabeln.

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
Vi kan använda metoden `Enum.IsDefined()` för att kontrollera om det konverterade heltalsvärdet finns i den givna typen `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Lösning 2: Använd `Enum.ToObject()` -metoden

Vi kan använda metoden `Enum.ToObject()` för att konvertera värdet `int` till `enum` i C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





