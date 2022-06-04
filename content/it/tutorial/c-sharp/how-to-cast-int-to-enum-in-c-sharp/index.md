+++
title   ="Come eseguire il cast di `int` in `enum` in C#"
summary ="Per eseguire il cast di `int` in `enum` in C#, eseguire un cast esplicito della variabile `enum` in un numero intero."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Per eseguire il cast di `int` in `enum` in C#, digitare esplicitamente il cast della variabile `enum` in un numero intero.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Soluzione 1: Utilizzo del casting esplicito del tipo di variabile `enum` 

Vediamo un esempio per capire meglio.

Abbiamo un tipo `enum` chiamato `Days`, che rappresenta i giorni della settimana a partire dal lunedì.

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

Ma c'è un problema con la conversione di cui sopra ** da`int` a `enum` **.

Cosa succede se il valore `int` non esiste nella variabile C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Non verrà lanciata alcuna eccezione.

Quindi è meglio controllare se il valore `int` esiste in `Enum` prima di lanciarlo in un intero.

## Controllare se un intero esiste o meno nella variabile `enum` 

Per ottenere tutti i valori interi in C# `Enum` possiamo utilizzare il metodo `Enum.GetValues`.

Convertirli in un elenco C#, in modo da poter utilizzare il metodo `list.Contains()` per verificare se il dato intero esiste nella variabile `enum`.

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
Possiamo usare il metodo `Enum.IsDefined()` per verificare se il valore intero convertito esiste nel tipo `enum` dato.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Soluzione 2: Utilizzare il metodo `Enum.ToObject()` 

È possibile utilizzare il metodo `Enum.ToObject()` per convertire il valore `int` in `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





