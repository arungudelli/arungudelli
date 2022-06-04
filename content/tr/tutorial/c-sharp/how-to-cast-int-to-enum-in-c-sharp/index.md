+++
title   ="C#'ta `int` adresinden `enum` adresine nasıl döküm yapılır?"
summary ="C#'ta `int` öğesini `enum` öğesine dönüştürmek için, `enum` değişkenini tamsayıya açıkça dönüştürün."
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

C#'ta `int` değişkenini `enum` değişkenine dönüştürmek için, `enum` değişkenini açık bir şekilde tamsayıya dönüştürün.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Çözüm 1: `enum` değişkeninin açık tip dökümünü kullanma

Bunu daha iyi anlamak için bir örnek üzerinden gidelim.

Pazartesiden başlayan hafta günlerini temsil eden `Days` adında bir `enum` türümüz var.

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

Ancak yukarıdaki **`int` - `enum` dönüşümü** ile ilgili bir sorun var.

 `int` değeri C# `Enum` değişkeninde mevcut değilse ne olur?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Herhangi bir istisna fırlatmayacaktır.

Bu nedenle, tamsayıya dönüştürmeden önce `int` değerinin `Enum` adresinde mevcut olup olmadığını kontrol etmek daha iyidir.

## `enum` değişkeninde bir tamsayı olup olmadığını kontrol edin

C#'ta tüm tamsayı değerlerini almak için `Enum` `Enum.GetValues` yöntemini kullanabiliriz.

Bunları C# listesine dönüştürün, böylece verilen tamsayının `enum` değişkeninde var olup olmadığını kontrol etmek için `list.Contains()` yöntemini kullanabiliriz.

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
Dönüştürülen tamsayı değerinin verilen `enum` türünde var olup olmadığını kontrol etmek için `Enum.IsDefined()` yöntemini kullanabiliriz.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Çözüm 2: `Enum.ToObject()` yöntemini kullanın

C#'ta `Enum.ToObject()` metodunu kullanabilir, `int` değerini `enum` değerine dönüştürebiliriz.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





