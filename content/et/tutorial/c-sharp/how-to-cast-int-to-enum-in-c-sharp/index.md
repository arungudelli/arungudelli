+++
title   ="Kuidas valada `int` aadressile `enum` C# keeles"
summary ="Selleks, et C# keeles valada `int` muutujaks `enum`, tuleb muutuja `enum` selgesõnaliselt valada täisarvuks."
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

Et castida `int` C#-s `enum` -ks, tipi selgesõnaliselt cast `enum` muutuja täisarvuks.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Lahendus 1: Muutuja `enum` selgesõnalise tüübi valimise kasutamine

Vaatame läbi ühe näite, et seda paremini mõista.

Meil on tüüp `enum` nimega `Days`, mis tähistab nädalapäevi alates esmaspäevast.

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

Kuid ülaltoodud **`int` konverteerimisega `enum` on probleem**.

Mis siis, kui `int` väärtust ei ole C# `Enum` muutujas olemas?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

See ei tekita ühtegi erandit.

Seega on parem kontrollida, kas `int` väärtus on olemas aadressil `Enum`, enne kui see täisarvuks valatakse.

## Kontrollida, kas `enum` muutujas on täisarv olemas või mitte

Kõigi täisarvude väärtuste saamiseks C# `Enum` saame kasutada `Enum.GetValues` meetodit.

Konverteerige need C# loendiks, et saaksime kasutada `list.Contains()` meetodit, et kontrollida, kas antud täisarv on olemas `enum` muutujas.

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
Me saame kasutada `Enum.IsDefined()` meetodit, et kontrollida, kas konverteeritud täisarvu väärtus on olemas antud `enum` tüübis.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Lahendus 2: Kasutage `Enum.ToObject()` meetodit

Me võime kasutada `Enum.ToObject()` meetodit, teisendada `int` väärtuse `enum` -ks C#-s.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





