+++
title   ="Bagaimana cara cast `int` ke `enum` di C#"
summary ="Untuk cast `int` ke `enum` di C#, secara eksplisit ketik cast variabel `enum` ke integer."
keywords=["int ke enum di C#, cast int ke enum di C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Untuk cast `int` ke `enum` di C#, secara eksplisit ketik cast variabel `enum` ke integer.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Solusi 1: Menggunakan pengecoran tipe eksplisit dari variabel `enum` 

Mari kita lihat sebuah contoh untuk memahaminya lebih lanjut.

Kita memiliki tipe `enum` yang disebut `Days`, yang merepresentasikan hari dalam seminggu mulai dari hari Senin.

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

Tetapi ada masalah dengan konversi **`int` ke `enum` ** di atas.

Bagaimana jika nilai `int` tidak ada di variabel C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Ini tidak akan melemparkan pengecualian apa pun.

Jadi lebih baik untuk memeriksa apakah nilai `int` ada di `Enum` sebelum casting ke integer.

## Periksa apakah integer ada atau tidak di variabel `enum` 

Untuk mendapatkan semua nilai integer di C# `Enum` kita bisa menggunakan metode `Enum.GetValues`.

Konversikan ke daftar C#, sehingga kita dapat menggunakan metode `list.Contains()` untuk memeriksa apakah integer yang diberikan ada di variabel `enum`.

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
Kita dapat menggunakan metode `Enum.IsDefined()` untuk memeriksa apakah nilai integer yang dikonversi ada dalam tipe `enum` yang diberikan.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solusi 2: Gunakan metode `Enum.ToObject()` 

Kita bisa menggunakan metode `Enum.ToObject()`, mengubah nilai `int` menjadi `enum` di C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





