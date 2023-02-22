---
title: "C# enum döngüsü/ numaralandırması nasıl yapılır"
description: "Örneklerle C# enum döngüsü veya numaralandırması yapmanın farklı yolları"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumlar `C#` dilinde yaygın olarak kullanılmaktadır. 

Ve `C#` adresinde enum'u döngüye sokmanın veya numaralandırmanın 4 yolu vardır. 

1. .Net 5 ve üzeri sürümlerde `C# Enum.GetValues()` adresini kullanma.
2. Eski .Net sürümlerinde `C# Enum.GetValues()` adresini kullanma.
3. Enum adlarını dizeler olarak numaralandırmak için `C# Enum.GetNames()` adresini kullanma.
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

 `enum` farklı günlük kaydı seviyelerini temsil eder.

Şimdi `C# enum` adresini numaralandırmanın farklı yollarını göreceğiz.

##.Net 5 ve üzeri sürümlerde `C# Enum.GetValues()` Generic yöntemini kullanma

 `.Net` 'un en son sürümünü, yani `.Net 5` ve üstünü kullanıyorsanız, `C# enum`'da döngü oluşturmak için `Enum.GetValues` yönteminin genel sürümünü kullanabilirsiniz.

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

 `Enum.GetValues` adresinin yeni genel sürümü, enum değerleri dizisini döndürür. 

Ayrıca `C# enum` adresini numaralandırmak için `for` veya `foreach` ifadelerini kullanabiliriz. 

Dizi `enum` türünü içerdiğinden, `ToString()` yöntemini kullanarak dizeye dönüştürmemiz gerekir.

## Eski .Net sürümlerinde `C# Enum.GetValues()` adresini kullanma.

 `.Net` 'un eski sürümlerinde `Enum.GetValues()` yöntemi için genel bir yöntem mevcut değildir. 

 `Enum.GetValues()` yöntemine parametre olarak `typeof()` enum'unu geçirmeniz gerekir. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ve `System.Array` türünde enum değerleri döndürür ve ayrıca C# enum'u boyunca döngü yapmak için `foreach` deyimini kullanabiliriz.

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

## Enum adlarını dizeler olarak numaralandırmak için `C# Enum.GetNames()` adresini kullanma 

`C# Enum.GetValues()` metodu enum tiplerinden oluşan bir dizi döndürür. 

Bu yüzden enum değerlerini konsola yazdırmadan önce string'e dönüştürdük.

 `C# Enum.GetNames()` yöntemini kullanarak enum adlarını string olarak numaralandırabiliriz, böylece onları string'e dönüştürmek gerekmez.

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

Yani enum isimlerini string olarak döngüye sokmak isterseniz `C# Enum.GetNames()` metodunu kullanabiliriz.

## Kullanma `Linq`

C# enum'larını numaralandırmak için `Enum.GetValues()` ve `Enum.GetNames()` yöntemleri yardımıyla `Linq forEach` yöntemini kullanabiliriz.

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

Bu derste C#'ta `Enum.GetValues()` ve `Enum.GetNames()` yöntemlerini kullanarak enum içinde döngü yapmayı öğrendik.










