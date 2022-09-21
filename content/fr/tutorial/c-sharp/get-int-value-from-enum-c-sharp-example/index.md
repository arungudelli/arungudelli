+++
title   ="Comment obtenir la valeur de `int` à partir de `Enum` en C# avec des exemples"
summary ="Pour obtenir la valeur de `int` à partir de `enum` en C#, convertissez la variable enum en entier."
keywords=["Valeur entière d'un enum en C#, Convertir une chaîne de caractères en enum en C#"]
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

Pour obtenir la valeur de `int` à partir de `enum` en C#, transformez la variable `enum` en nombre entier.

{{%toc%}}

## Solution 1 : Utilisez le cast de type pour obtenir la valeur de `int` à partir de `enum`

Le type sous-jacent par défaut de `enums` en C# est `Int`.

Nous pouvons donc effectuer un cast de type de `enum` vers `int` pour obtenir la valeur entière de l'enum en C#.

Nous allons prendre un exemple pour mieux comprendre.

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

Nous allons maintenant convertir les valeurs de l'enum en valeurs entières.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Solution 2 : Utilisez la méthode `Convert.ToInt32()` pour obtenir la valeur entière de l'énumération

Ou nous pouvons utiliser la méthode `Convert.ToInt32()` to pour convertir un `enum` en entier comme indiqué ci-dessous.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Obtenir la valeur `enum` de différents types sous-jacents

`Enums` en C# peuvent avoir différents types sous-jacents 

Si l'enum C# est déclarée comme une `uint`, `long` ou `ulong`, nous devons la convertir au type correspondant de la `enum`.

Prenons l'exemple ci-dessous de l'enum `Stars`, qui a un type `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```