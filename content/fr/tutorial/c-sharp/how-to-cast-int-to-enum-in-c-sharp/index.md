+++
title   ="Comment convertir `int` en `enum` en C#"
summary ="Pour convertir `int` en `enum` en C#, il faut explicitement convertir la variable `enum` en entier."
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Pour convertir `int` en `enum` en C#, tapez explicitement la variable `enum` en entier.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Solution 1 : Utilisation de l'attribution explicite de type de la variable `enum` 

Prenons un exemple pour mieux comprendre.

Nous avons un type `enum` appelé `Days`, qui représente les jours de la semaine à partir du lundi.

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

Mais il y a un problème avec la conversion ci-dessus ** de`int` en `enum` **.

Que faire si la valeur `int` n'existe pas dans la variable C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Il n'y aura pas d'exception.

Il est donc préférable de vérifier si la valeur `int` existe dans `Enum` avant de la convertir en entier.

## Vérifier si un entier existe ou non dans la variable `enum` 

Pour obtenir toutes les valeurs entières dans C# `Enum`, nous pouvons utiliser la méthode `Enum.GetValues`.

Convertissez-les en liste C#, afin que nous puissions utiliser la méthode `list.Contains()` pour vérifier si l'entier donné existe dans la variable `enum`.

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
Nous pouvons utiliser la méthode `Enum.IsDefined()` pour vérifier si la valeur entière convertie existe dans le type `enum` donné.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solution 2 : Utilisez la méthode `Enum.ToObject()` 

Nous pouvons utiliser la méthode `Enum.ToObject()`, pour convertir la valeur de `int` en `enum` en C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





