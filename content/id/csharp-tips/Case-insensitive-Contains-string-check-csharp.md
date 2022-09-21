
---
title: "C# Kasus tidak sensitif berisi pemeriksaan string"
description: "Dalam tutorial ini kita belajar berbagai cara untuk melakukan pengecekan case insensitive string contains di C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Dalam tutorial ini kita belajar berbagai cara untuk melakukan pengecekan case insensitive string contain di C# 

Sepertinya ini adalah masalah yang sederhana, tetapi metode default C# `string.Contains()` adalah case sensitive 

Dan jika string tidak dalam bahasa Inggris, misalnya, untuk bahasa lain, kita tidak dapat membandingkan teks case insensitive secara langsung 

Kedua string harus dalam budaya yang sama dan kita harus tahu budaya bahasanya.

Sering kali kita akan membandingkan string dalam bahasa Inggris saja.

## Metode 1: Menggunakan metode C# `string.IndexOf()`.

Kita bisa menggunakan metode C# `string.IndexOf()` untuk melakukan pengecekan isi string yang case insensitive.

`IndexOf()` metode ini menerima parameter `StringComparison.OrdinalIgnoreCase`, yang menentukan jenis pencarian yang akan digunakan untuk karakter.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Metode 2: Menggunakan metode `string.Contains()` di .Net 5+ &amp; .NET Core 2.0+

Dalam versi terbaru dot net, yaitu, di .Net Core 2.0+ dan .Net 5+. Metode `string.Contains()` memiliki metode overloaded yang menerima parameter `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Metode 3: Menggunakan metode `Regex.IsMatch()` 

Kita bisa menggunakan ekspresi reguler untuk melakukan pengecekan string contain yang case insensitive.

Jika anda sudah familiar dengan `Regex`, Gunakan metode `Regex.IsMatch()` dan untuk memeriksa case insensitive pass `RegexOptions.IgnoreCase` parameter 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Metode 4: Menggunakan `.ToUpper()` &amp `.ToLower()`

Jika string dalam bahasa Inggris dan kinerjanya tidak menjadi masalah, kita dapat mengubah kedua string ke kasus yang sama kemudian melakukan pemeriksaan string berisi.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Pemeriksaan Contains yang tidak sensitif terhadap kasus untuk bahasa lain

Ketidakpekaan kasus tergantung pada bahasa 

Sebagai contoh, dalam bahasa Inggris `I` adalah versi huruf besar dari `i`.

Sedangkan dalam bahasa Turki versi huruf besar dari `i` adalah karakter yang tidak dikenal `İ`.

Untuk melakukan pengecekan string case insensitive kita perlu menggunakan objek `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Saya telah membuat objek `CultureInfo` untuk bahasa Turki. Dan membandingkan kedua string menggunakan `CompareInfo` seperti yang ditunjukkan di bawah ini.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Cara terbaik untuk melakukan pengecekan Case insensitive Contains string

Jika Anda menggunakan versi terbaru dari `.Net` gunakan metode `string.Contains()`.

Jika tidak, tetap gunakan metode `string.IndexOf()`.

Jangan memilih metode `.ToUpper()` atau `To.Lower()` karena dapat menyebabkan masalah kinerja.

Gunakan objek `CultureInfo` untuk string bahasa lain.

