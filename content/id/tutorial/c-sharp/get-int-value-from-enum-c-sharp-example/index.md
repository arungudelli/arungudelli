+++
title   ="Cara mendapatkan nilai `int` dari `Enum` di C# dengan contoh"
summary ="Untuk mendapatkan nilai `int` dari `enum` di C#, ubah variabel enum menjadi integer."
keywords=["nilai int dari enum di C#, Konversi string ke enum di C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Untuk mendapatkan nilai `int` dari `enum` di C#, ubah variabel `enum` menjadi integer.

{{%toc%}}

## Solusi 1: Gunakan Type cast untuk mendapatkan nilai `int` dari `enum`

Tipe dasar default untuk `enums` di C# adalah `Int`.

Jadi kita dapat mengetikkan cast `enum` ke `int` untuk mendapatkan nilai integer dari enum di C#.

Kita akan mengambil contoh untuk memahaminya lebih lanjut.

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
```

Sekarang kita akan meng-cast nilai enum ke nilai integer.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Solusi 2: Gunakan metode `Convert.ToInt32()` untuk mendapatkan nilai integer dari enum

Atau kita bisa menggunakan metode `Convert.ToInt32()` to untuk mengubah `enum` menjadi integer seperti yang ditunjukkan di bawah ini.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Dapatkan nilai `enum` dari tipe dasar yang berbeda

`Enums` dalam C# dapat memiliki tipe dasar yang berbeda 

Jika C# enum dideklarasikan sebagai `uint`, `long`, atau `ulong` kita harus cast ke tipe yang sesuai dari `enum`.

Perhatikan contoh `Stars` enum di bawah ini, yang memiliki tipe `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```