+++
title   ="C#'ta int türünü enum türüne dönüştürmenin/dökmenin 2 yolu"
summary ="C#'ta int türünü enum türüne dönüştürmenin/dökmenin 2 yolu vardır 1. C# açık tip dökümünü kullanma. 2. Enum.ToObject() yöntemini kullanarak."

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


Dönüştürmenin veya döküm yapmanın 2 yolu vardır `int` `enum` c#'ta

1. C# açık tip dökümünü kullanma.
2. `Enum.ToObject()` yöntemini kullanma

{{%toc%}}

## Çözüm 1: C# açık tip dökümünü kullanma

Basit bir şekilde `int` şu biçime dönüştürülür `enum` c#'ta açık tip dökümünü kullanmaktır.

Bunu daha iyi anlamak için bir örnek üzerinden gidelim.

Bizim bir `enum``LogLevel` olarak adlandırılan ve farklı günlük kaydı seviyelerini temsil eden tür.

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

Yerleştirilerek yapılan açık döküm `enum``int` değerinin önüne parantez içinde yazın.

Ancak yukarıdaki **C# `int` ile ilgili bir sorun var `enum` dönüşüm**.

 `int` değeri C# `Enum` değişkeninde mevcut değilse ne olur?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Herhangi bir istisna fırlatmayacaktır.

Bu nedenle, tamsayıya dönüştürmeden önce `int` değerinin `C# Enum` adresinde var olup olmadığını kontrol etmek daha iyidir.

## Bir tamsayının var olup olmadığını kontrol edin `C# enum` değişken

 `C# Enum` adresindeki tüm tamsayı değerlerini almak için `Enum.GetValues` yöntemini kullanabiliriz.

Bunları `C#` listesine dönüştürün, böylece verilen tamsayının içinde olup olmadığını kontrol etmek için `list.Contains()` yöntemini kullanabiliriz `enum` değişken.

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
Verilen tamsayı değerinde dönüştürülmüş tamsayı değerinin olup olmadığını kontrol etmek için `Enum.IsDefined()` yöntemini kullanabiliriz `enum` tip.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Çözüm 2: `Enum.ToObject()` yöntemini kullanın

 `C# Enum.ToObject()` yöntemini kullanabilir, `int` değerini `enum` c#'ta.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





