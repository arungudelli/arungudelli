
+++
title="Comment obtenir le nom enum à partir d'une valeur en C#"
summary="Il y a deux façons d'obtenir le nom enum à partir d'une valeur en C# 1. Utiliser C# `Enum.GetName()` et passer la valeur enum comme paramètre pour obtenir le nom. 2. Convertir la valeur enum en membre d'eration enumen utilisant le casting et ensuite utiliser la méthode `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


L'un des cas d'utilisation populaires de enum est l'obtention du nom de enum à partir de sa valeur.

Prenons un exemple dans le monde réel. En général, nous stockons les valeurs enum dans la base de données, c'est-à-dire que nous ne stockons que des valeurs entières 

Et après avoir lu la valeur enum dans la base de données, nous devons la reconvertir en son nom enum.

Il existe **deux façons d'obtenir le nom enum à partir d'une valeur en C#** 

{{%toc%}}

## Solution 1 : Utiliser `Enum.GetName()`

La fonction C# `Enum.GetName()` prend deux paramètres enum type et valeur et renvoie le nom enum.

Prenons l'exemple de `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Maintenant, nous allons passer la valeur enum à la valeur `Enum.GetName()` pour obtenir le nom enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Si vous utilisez la version C# de `.Net 6`, vous pouvez transmettre uniquement la valeur enum (convertie en enum) à la méthode `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Solution 2 : Utiliser le casting de type

Une autre solution consiste à convertir la valeur de enum en un membre d'eration de enumen utilisant le casting, puis à utiliser la méthode `ToString()`.

Il s'agit d'une méthode simple qui n'utilise aucune des fonctions intégrées de `C# Enum`.

Convertissez d'abord la valeur enum en un membre d'énumération enum, puis utilisez la méthode `ToString()`.

```csharp
var enumValue = 2;

//Convert enum Value

var enumDisplayValue = (LogLevel)enumValue;

var enumName = enumDisplayValue.ToString();

Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output

The name of enum value : 2 is WARN
**/
```

## Résumé

Dans ce tutoriel, nous avons appris différentes façons d'obtenir la valeur du nom enum en c# 

1. En passant les paramètres de type et de valeur enum à la méthode `Enum.GetName()` 
2. Et en utilisant le casting de type vers le type correspondant de enum 
