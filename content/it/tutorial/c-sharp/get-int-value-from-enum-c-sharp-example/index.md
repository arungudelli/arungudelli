+++
title   ="Come ottenere il valore di `int` da `Enum` in C# con esempi"
summary ="Per ottenere il valore di `int` da `enum` in C#, eseguire il cast della variabile enum in un numero intero."
keywords=["Valore int da enum in C#,Convertire stringa in enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Per ottenere il valore di `int` da `enum` in C#, eseguire il cast della variabile `enum` in un numero intero.

{{%toc%}}

## Soluzione 1: Usare il cast di tipo per ottenere il valore di `int` da `enum`

Il tipo sottostante predefinito per `enums` in C# è `Int`.

Possiamo quindi eseguire il cast di tipo da `enum` a `int` per ottenere il valore intero da enum in C#.

Facciamo un esempio per capire meglio.

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

Ora eseguiremo il cast dei valori enum in valori interi.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Soluzione 2: Utilizzare il metodo `Convert.ToInt32()` per ottenere il valore intero da enum

Oppure si può usare il metodo `Convert.ToInt32()` to per convertire un `enum` in intero, come mostrato di seguito.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Ottenere il valore `enum` di diversi tipi sottostanti

`Enums` in C# possono avere tipi sottostanti diversi 

Se l'enum C# è dichiarato come `uint`, `long`, o `ulong`, dobbiamo eseguire il cast al tipo corrispondente di `enum`.

Consideriamo il seguente esempio di enum `Stars`, che ha un tipo `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```