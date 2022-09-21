+++
title="Bagaimana cara memeriksa apakah string adalah angka di C #"
summary="Langkah-langkah untuk memeriksa apakah string adalah angka di c# 1.Deklarasikan variabel integer. 2.Pass string ke metode `int.TryParse()` atau `double.TryParse()` dengan variabel `out`. 3.Jika string adalah angka `TryParse` metode akan kembali benar. Dan memberikan nilai ke nilai integer `out` yang dideklarasikan."
keywords=["periksa apakah string adalah angka dalam C #"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Langkah-langkah untuk memeriksa apakah string adalah angka di C#

1. Deklarasikan variabel bilangan bulat.
2. Berikan string ke metode `int.TryParse()` atau `double.TryParse()` dengan variabel `out`.
3. Jika string adalah angka `TryParse` metode akan mengembalikan nilai true. Dan memberikan nilai ke nilai integer `out` yang dideklarasikan.

{{%toc%}}

## Periksa apakah string adalah Angka atau bukan di C# 

Misalnya kita memiliki variabel string "123" dan jika Anda ingin memeriksa apakah itu numerik gunakan kode C # di bawah ini.

```
var stringNumber = "123";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is true and numericValue=123

var stringNumber = "123P";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is false and numericValue=0 default value

```

Dari C# 7 dan seterusnya kita dapat mendeklarasikan variabel [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) dalam Metode TryParse itu sendiri.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Masalah dengan metode `int.TryParse` di atas adalah tidak dapat memeriksa nilai angka string negatif.

## Memeriksa angka string negatif di C# 

Untuk memeriksa nilai angka string negatif kita dapat menggunakan metode C# `double.TryParse()`.

```
var negativeString = "-123";
double number;
if(double.TryParse(negativeString,out number)){
   if (number > 0){

   }else{
       //negative number 
   }   
}
```

## Cara terbaik untuk memeriksa apakah string adalah angka di C# 

Selalu gunakan metode `double.TryParse()` untuk mengecek apakah sebuah string adalah angka, karena metode ini dapat memvalidasi angka positif dan negatif.