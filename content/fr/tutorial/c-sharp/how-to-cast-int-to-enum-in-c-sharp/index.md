+++
title   ="2 ways to convert/cast int to enum in C#"
summary ="Il y a 2 façons de convertir int en enum en C# 1. En utilisant le casting de type explicite de C#. 2. En utilisant la méthode Enum.ToObject()"

keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2023-01-24T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Il y a deux façons de convertir ou de convertir `int` en `enum` en C#

1. En utilisant le casting explicite de type en C#.
2. Utilisation de la méthode `Enum.ToObject()` 

{{%toc%}}

## Solution 1 : Utilisation de la répartition explicite des types en C#

Le moyen le plus simple de convertir `int` en `enum` en C# est d'utiliser le moulage de type explicite.

Prenons un exemple pour mieux comprendre.

Nous avons un `enum` appelé `LogLevel`, qui représente différents niveaux de journalisation.

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}

int logEnumInteger = 1;
LogLevel errorEnum = (LogLevel) logEnumInteger;
Console.WriteLine(errorEnum.ToString());//ERROR
```

Le moulage explicite est effectué en plaçant le type `enum` entre parenthèses devant la valeur `int`.

Mais il y a un problème avec la **C# `int` to `enum` conversion**.

Que se passe-t-il si la valeur `int` n'existe pas dans la variable C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Il n'y aura pas d'exception.

Il est donc préférable de vérifier si la valeur `int` existe dans `C# Enum` avant de la convertir en entier.

## Vérifier si un entier existe ou non dans `C# enum` variable

Pour obtenir toutes les valeurs entières dans `C# Enum`, nous pouvons utiliser la méthode `Enum.GetValues`.

Les convertir en liste `C#`, afin que nous puissions utiliser la méthode `list.Contains()` pour vérifier si l'entier donné existe dans la variable `enum` variable.

```csharp
var intValue = 100;
var enumValues = Enum.GetValues(typeof(LogLevel)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
   Console.WriteLine("We can Cast C# int to Enum");  
   LogLevel loggingValue = (LogLevel) intValue;
}else{
  Console.WriteLine("Cannot Cast C# int to Enum");
}

```
Nous pouvons utiliser la méthode `Enum.IsDefined()` pour vérifier si la valeur entière convertie existe dans le type donné `enum` type donné.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solution 2 : Utilisez la méthode `Enum.ToObject()` 

Nous pouvons utiliser la méthode `C# Enum.ToObject()`, pour convertir la valeur de `int` en `enum` en C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





