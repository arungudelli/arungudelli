---
title: "C# nasıl enumerate edilir enum"
description: " C#'ı enumerate etmenin farklı yolları enum örneklerle"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumlar `C#` dilinde yaygın olarak kullanılmaktadır. 

Ve `C#` adresinde enum adresini enumerate etmenin 4 yolu vardır. 

1. .Net 5 ve üzeri sürümlerde `C# Enum.GetValues()` adresini kullanma.
2. Eski .Net sürümlerinde `C# Enum.GetValues()` adresini kullanma.
3. `C# Enum.GetNames()` adlarını dizeler olarak enumerate etmek için enum kullanmak.
4. Kullanma `Linq`

Bunu daha iyi anlamak için bir örnek üzerinden gidelim. 

İlk olarak bir C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

Bu `enum` farklı günlük kaydı seviyelerini temsil eder.

Şimdi enumerate için farklı yollar göreceğiz `C# enum`.

##.Net 5 ve üzeri sürümlerde `C# Enum.GetValues()` Generic yöntemini kullanma

 `.Net`, yani `.Net 5` ve üstünün en son sürümünü kullanıyorsanız, `Enum.GetValues` yöntemi için genel sürümü enumerate etmek için kullanabilirsiniz `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

 `Enum.GetValues` 'un yeni genel sürümü enum değerleri dizisini döndürür. 

Ve ayrıca `for` veya `foreach` ifadelerini listelemek için kullanabiliriz `C# enum` isimler. 

Dizi aşağıdakileri içerdiğinden `enum` türünü `ToString()` yöntemini kullanarak dizeye dönüştürmemiz gerekir.

## Eski .Net sürümlerinde `C# Enum.GetValues()` adresini kullanma.

 `.Net` 'un eski sürümlerinde `Enum.GetValues()` yöntemi için genel bir yöntem mevcut değildir. 

 `typeof()` enum adresini `Enum.GetValues()` yöntemine parametre olarak geçirmeniz gerekir. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ve `System.Array` türünde enum değerlerini döndürür ve ayrıca `foreach` deyimini kullanarak `C# enum` isimler.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

 `IEnumerable` sonucunu istiyorsanız, `Enum.GetValues()` yöntemini daha fazla döküm yapabiliriz.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## `C# Enum.GetNames()` adlarını dizeler olarak enumerate etmek için enum kullanma 

`C# Enum.GetValues()` yöntemi enum türlerinden oluşan bir dizi döndürür. 

Bu yüzden konsola yazdırmadan önce enum adlarını dizeye dönüştürdük.

 `C# Enum.GetNames()` yöntemini kullanarak enum enum adlarını dizeler olarak erate edebiliriz, böylece bunları dizelere dönüştürmek gerekmez.

 `.Net 5` ve üstünü kullanıyorsanız, genel `C# Enum.GetNames()` işlevini kullanabilirsiniz.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Eski sürümlerde `typeof()` enum parametresini geçmemiz gerekir.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Eğer isimleri string olarak enumerate etmek istiyorsanız `C# Enum.GetNames()` metodunu kullanabiliriz.

## Kullanma `Linq`

 `Enum.GetValues()` ve `Enum.GetNames()` metotları yardımıyla C# enum'u enumerate etmek için `Linq forEach` metodunu kullanabiliriz.

 `.Net 5` ve üzerinde aşağıdaki kod parçacığını kullanın.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

Eski sürümlerde

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Özet

Bu eğitimde `Enum.GetValues()` ve `Enum.GetNames()` yöntemlerini kullanarak C#'ta enum adresini enumerate etmeyi öğrendik.










