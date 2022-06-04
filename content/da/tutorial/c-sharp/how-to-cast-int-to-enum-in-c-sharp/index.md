+++
title   ="Sådan kastes `int` til `enum` i C#"
summary ="Hvis du vil caste `int` til `enum` i C#, skal du eksplicit skrive caste variablen `enum` til heltal."
keywords=["int til enum i C#,cast int til enum i C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Hvis du vil omdanne `int` til `enum` i C#, skal du udtrykkeligt skrive "cast" af variablen `enum` til heltal.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Løsning 1: Brug af eksplicit typecasting af `enum` variabel

Lad os gennemgå et eksempel for at forstå det nærmere.

Vi har en `enum` type kaldet `Days`, som repræsenterer ugedage startende fra mandag.

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

Men der er et problem med ovenstående **`int` til `enum` konvertering**.

Hvad hvis `int` -værdien ikke findes i C# `Enum` -variablen?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Det vil ikke give nogen undtagelse.

Så det er bedre at kontrollere, om `int` -værdien findes i `Enum`, før den omformes til et heltal.

## Kontroller, om der findes et heltal eller ej i variablen `enum` 

For at få alle heltalsværdierne i C# `Enum` kan vi bruge `Enum.GetValues` -metoden.

Konverter dem til en C#-liste, så vi kan bruge `list.Contains()` -metoden til at kontrollere, om det givne heltal findes i `enum` -variablen.

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
Vi kan bruge metoden `Enum.IsDefined()` til at kontrollere, om den konverterede heltalsværdi findes i den givne type `enum`.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Løsning 2: Brug `Enum.ToObject()` metoden

Vi kan bruge `Enum.ToObject()` -metoden, konvertere `int` -værdien til `enum` i C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





