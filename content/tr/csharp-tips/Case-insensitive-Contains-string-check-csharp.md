
---
title: "C# Büyük/Küçük Harfe Duyarsız Dize Kontrolü İçerir"
description: "Bu eğitimde C#'ta büyük/küçük harfe duyarlı olmayan dize içerme kontrolü yapmanın farklı yollarını öğreniyoruz"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Bu eğitimde, C#'ta büyük/küçük harfe duyarlı olmayan dize içerme kontrolü yapmanın farklı yollarını öğreniyoruz 

Basit bir sorun gibi görünüyor, ancak varsayılan C# `string.Contains()` yöntemi büyük/küçük harfe duyarlıdır 

Ve eğer dize İngilizce değilse, yani diğer diller için, metni büyük/küçük harfe duyarsız olarak doğrudan karşılaştıramayız 

Her iki dizge de aynı kültürde olmalı ve dil kültürünü bilmeliyiz.

Çoğu zaman dizeleri yalnızca İngilizce dilinde karşılaştıracağız.

## Yöntem 1: C# `string.IndexOf()` yöntemini kullanma.

Büyük/küçük harfe duyarlı olmayan dize içerme kontrolü yapmak için C# `string.IndexOf()` Metodunu kullanabiliriz.

`IndexOf()` yöntemi, karakterler için kullanılacak arama türünü belirten `StringComparison.OrdinalIgnoreCase` parametresini kabul eder.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Yöntem 2: .Net 5+ ve .NET Core 2.0+'da `string.Contains()` yöntemini kullanma

Nokta net'in en son sürümlerinde, yani .Net Core 2.0+ ve .Net 5+'da. `string.Contains()` yöntemi, `StringComparison` parametresini kabul eden aşırı yüklenmiş bir yönteme sahiptir.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Yöntem 3: `Regex.IsMatch()` yöntemini kullanma

Büyük/küçük harfe duyarlı olmayan dize kontrolü yapmak için düzenli ifadeleri kullanabiliriz.

 `Regex` ile aşinaysanız, `Regex.IsMatch()` yöntemini kullanın ve büyük/küçük harf duyarsızlığını kontrol etmek için `RegexOptions.IgnoreCase` parametresini geçin 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Yöntem 4: `.ToUpper()` &amp; adresini kullanma `.ToLower()`

Dizeler İngilizce dilindeyse ve performans bir sorun değilse, her iki dizeyi de aynı büyük/küçük harfe dönüştürebilir ve ardından dize içeriyor kontrolünü yapabiliriz.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Harfe duyarsız Diğer diller için kontrol içerir

Büyük/küçük harf duyarsızlığı dile bağlıdır 

Örneğin, İngilizce dilinde `I`, `i`'un büyük harf versiyonudur.

Türkçe'de ise `i` 'un büyük harfli versiyonu yabancı bir karakter olan `İ`'dur.

Büyük/küçük harfe duyarlı olmayan dize kontrolü yapmak için `CultureInfo` nesnesini kullanmamız gerekir.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Türkçe dili için `CultureInfo` nesnesini oluşturdum. Ve aşağıda gösterildiği gibi `CompareInfo` kullanarak her iki dizeyi karşılaştırdım.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Büyük/küçük harfe duyarlı olmayan Contains dizesi denetimi yapmanın en iyi yolu

 `.Net` 'un en son sürümünü kullanıyorsanız `string.Contains()` yöntemini kullanın.

Aksi takdirde `string.IndexOf()` yöntemine bağlı kalın.

Performans sorunlarına yol açabileceğinden `.ToUpper()` veya `To.Lower()` yöntemini tercih etmeyin.

Diğer dil dizeleri için `CultureInfo` nesnesini kullanın.

