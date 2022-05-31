+++
title="Kā pārbaudīt, vai virkne ir skaitlis, izmantojot C#"
summary="Kā pārbaudīt, vai virkne ir skaitlis c# valodā 1. Deklarējiet veselu skaitļu mainīgo. 2.Nododiet virkni `int.TryParse()` vai `double.TryParse()` metodēm ar `out` mainīgo. 3.Ja virkne ir skaitlis, `TryParse` metode atgriezīs true. Un piešķir vērtību deklarētajai veselā skaitļa `out` vērtībai."
keywords=["pārbaudīt, vai virkne ir skaitlis C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Soļi, lai pārbaudītu, vai virkne ir skaitlis C# valodā

1. Deklarējiet veselu skaitļu mainīgo.
2. Nododiet virkni `int.TryParse()` vai `double.TryParse()` metodēm ar `out` mainīgo.
3. Ja virkne ir skaitlis, `TryParse` metode atgriezīs true. Un piešķir vērtību deklarētajai veselā skaitļa `out` vērtībai.

{{%toc%}}

## Pārbaudīt, vai virkne ir skaitlis vai nav C# valodā 

Piemēram, mums ir virknes mainīgais "123", un, ja vēlaties pārbaudīt, vai tas ir skaitlis, izmantojiet tālāk norādīto C# kodu.

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

Sākot ar C# 7, mainīgo [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) mēs varam deklarēt pašā TryParse metodē.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Iepriekš minētās `int.TryParse` metodes problēma ir tā, ka tā nevar pārbaudīt negatīvas virknes skaitļa vērtības.

## Negatīva virknes skaitļa pārbaude C# valodā 

Lai pārbaudītu, vai virknes skaitļa vērtība ir negatīva, mēs varam izmantot C# `double.TryParse()` metodi.

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

## Labākais veids, kā pārbaudīt, vai virkne ir skaitlis C# valodā 

Lai pārbaudītu, vai virkne ir skaitlis, vienmēr izmantojiet `double.TryParse()` metodi, jo tā var pārbaudīt gan pozitīvus, gan negatīvus skaitļus.