+++
title   ="Örneklerle C#'ta `Enum` adresinden `int` değeri nasıl alınır"
summary ="C#'ta `enum` adresinden `int` değerini almak için enum değişkenini tamsayıya dönüştürün."
keywords=["C#'ta enum'dan int değeri,C#'ta dizeyi enum'a dönüştürme"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

C#'ta `enum` adresinden `int` değerini almak için `enum` değişkenini tamsayıya dönüştürün.

{{%toc%}}

## Çözüm 1: `int` değerini almak için Type cast kullanın `enum`

C#'ta `enums` için varsayılan temel tür `Int`'dir.

Böylece C#'ta enum'dan tamsayı değerini almak için `enum` adresini `int` adresine yazabiliriz.

Bunu daha iyi anlamak için bir örnek vereceğiz.

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

Şimdi enum değerlerini tamsayı değerlerine dönüştüreceğiz.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Çözüm 2: Enum'dan tamsayı değerini almak için `Convert.ToInt32()` yöntemini kullanın

Ya da aşağıda gösterildiği gibi bir `enum` adresini tamsayıya dönüştürmek için `Convert.ToInt32()` to yöntemini kullanabiliriz.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Farklı temel türlerin `enum` değerini alın

`Enums` c#'ta farklı temel türlere sahip olabilir 

C# enum bir `uint`, `long` veya `ulong` olarak bildirilirse, bunu `enum`'un karşılık gelen türüne atamalıyız.

Aşağıdaki `long` türüne sahip `Stars` enum örneğini göz önünde bulundurun.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```