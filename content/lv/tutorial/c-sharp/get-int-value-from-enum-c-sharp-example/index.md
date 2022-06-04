+++
title   ="Kā iegūt `int` vērtību no `Enum` programmā C# ar piemēriem"
summary ="Lai iegūtu `int` vērtību no `enum` valodā C#, pārveidojiet enuma mainīgo uz veselu skaitli."
keywords=["int vērtība no enum programmā C#,Konvertēt virkni uz enum programmā C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Lai iegūtu `int` vērtību no `enum` C# valodā, pārrēķiniet `enum` mainīgo uz veselu skaitli.

{{%toc%}}

### 1. risinājums: Izmantojiet Type cast, lai iegūtu `int` vērtību no `enum`

Noklusējuma pamattips `enums` valodā C# ir `Int`.

Tāpēc mēs varam atveidot `enum` uz `int`, lai iegūtu veselu skaitļa vērtību no C# enuma.

Lai to izprastu sīkāk, aplūkosim piemēru.

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

Tagad pārveidosim enuma vērtības veselos skaitļos.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## 2. risinājums: Izmantojiet `Convert.ToInt32()` metodi, lai no enum iegūtu veselu skaitļu vērtību

Vai arī mēs varam izmantot `Convert.ToInt32()` to metodi, lai konvertētu `enum` uz veselu skaitli, kā parādīts zemāk.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Iegūstiet `enum` vērtību dažādiem bāzes tipiem

`Enums` c# var būt dažādi bāzes tipi 

Ja C# enums ir deklarēts kā `uint`, `long` vai `ulong`, mums tas jāpārveido uz atbilstošo `enum` tipu.

Aplūkojiet tālāk sniegto piemēru par `Stars` enumu, kuram ir tips `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```