+++
title   ="Miten saada `int` arvo `Enum` osoitteesta C# esimerkkien avulla"
summary ="Jos haluat saada `int` arvon `enum`:stä C#:ssa, castaa enum-muuttuja kokonaisluvuksi."
keywords=["int-arvo enumista C#:ssa,Muunna merkkijono enumiksi C#:ssa"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Jos haluat saada `int` arvon `enum`:stä C#:ssa, valaa `enum` -muuttuja kokonaisluvuksi.

{{%toc%}}

## Ratkaisu 1: Käytä Type cast -tyyppiä saadaksesi `int` -arvon muuttujasta `enum`

Oletustyyppi `enums`:lle C#:ssa on `Int`.

Voimme siis tyypittää tyypin `enum` muotoon `int` saadaksemme kokonaislukuarvon C#:n enumista.

Otetaan esimerkki sen ymmärtämiseksi tarkemmin.

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

Nyt muunnetaan enum-arvot kokonaislukuarvoiksi.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Ratkaisu 2: Käytä `Convert.ToInt32()` -menetelmää saadaksesi kokonaislukuarvon enumista

Tai voimme käyttää `Convert.ToInt32()` to -menetelmää `enum`:n muuntamiseen kokonaisluvuksi alla esitetyllä tavalla.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Hae `enum` arvo eri perustyypeille

`Enums` c#:ssa voi olla erilaisia perustyyppejä 

Jos C# enum on ilmoitettu `uint`, `long` tai `ulong`, meidän pitäisi castata se vastaavaan tyyppiin `enum`.

Tarkastellaan alla olevaa esimerkkiä `Stars` enum, jonka tyyppi on `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```