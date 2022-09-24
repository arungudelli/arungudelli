
+++
title="C#'ta değerden enum adı nasıl alınır"
summary="C#'ta değerden enum adını almanın iki yolu vardır 1. C# `Enum.GetName()` kullanın ve adı almak için enum değerini parametre olarak geçirin. 2. Döküm kullanarak enum değerini enumeration üyesine dönüştürün ve ardından `ToString()` yöntemini kullanın."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


 enum 'un popüler kullanım alanlarından biri, enum adını değerinden elde etmektir.

Gerçek bir dünya örneği düşünün, genellikle veri tabanında enum değerlerini saklayacağız. yani, yalnızca tamsayı değerlerini saklayacağız 

Ve veri tabanından enum değerini okuduktan sonra bunu enum adına geri dönüştürmemiz gerekir.

C#'da değerden enum adını almanın **iki yolu vardır** 

{{%toc%}}

## Çözüm 1: Kullanma `Enum.GetName()`

C# `Enum.GetName()` işlevi, enum türü ve değeri olmak üzere iki parametre alır ve enum adını döndürür.

 `LogLevel` Enum örneğini ele alalım

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Şimdi enum adını almak için enum değerini `Enum.GetName()` 'a aktaracağız 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

C# `.Net 6` sürümünü kullanıyorsanız, `Enum.GetName()` yöntemine yalnızca enum değerini ( enum'ye döküm) aktarabilirsiniz.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Çözüm 2: Tip dökümünü kullanma

Başka bir yol ise, enum değerini döküm kullanarak enumeration üyesine dönüştürmek ve ardından `ToString()` yöntemini kullanmaktır.

Bu, `C# Enum` yerleşik işlevlerini kullanmayan basit bir yoldur.

Önce enum değerini enumeration üyesine dönüştürün ve ardından `ToString()` yöntemini kullanın.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Özet

Bu eğitimde c#'ta enum isim değerini almanın farklı yollarını öğrendik 

1. enum tür ve değer parametrelerini `Enum.GetName()` yöntemine aktararak
2. Ve tip dökümünü kullanarak ilgili enum tipine dönüştürün 
