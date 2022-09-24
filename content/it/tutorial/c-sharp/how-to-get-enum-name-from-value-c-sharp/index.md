
+++
title="Come ottenere il nome di enum dal valore in C#"
summary="Esistono due modi per ottenere il nome di enum dal valore in C# 1. Usare C# `Enum.GetName()` e passare il valore enum come parametro per ottenere il nome. 2. Convertire il valore enum nel membro enumerazione usando il casting e poi usare il metodo `ToString()`."
date='2022-03-16T00:00:00+0000'
lastmod='2022-03-16T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
+++


Uno dei casi d'uso più diffusi di enum è quello di ottenere il nome di enum dal suo valore.

Consideriamo un esempio del mondo reale: in genere si memorizzano i valori di enum nella base dati, cioè si memorizzano solo valori interi 

Dopo aver letto il valore enum dalla base dati, dobbiamo riconvertirlo nel suo nome enum.

Esistono **due modi per ottenere il nome enum dal valore in C# 

{{%toc%}}

## Soluzione 1: Usare `Enum.GetName()`

C# la funzione `Enum.GetName()` prende due parametri enum tipo e valore e restituisce il nome enum.

Prendiamo un esempio di `LogLevel` Enum

```csharp
public enum LogLevel
{
   ERROR=1, 
   WARN=2, 
   INFO=3, 
   DEBUG=4
}
```

Ora passeremo il valore enum a `Enum.GetName()` per ottenere il nome enum 

```csharp
var enumValue = 1;
var enumName = Enum.GetName(typeof(LogLevel),enumValue);
Console.WriteLine($"The name of enum value: {enumValue} is {enumName}");

/**
Here is the output:
The name of enum value : 1 is ERROR
**/
```

Se si utilizza la versione C# `.Net 6`, si può passare solo il valore enum (cast a enum) al metodo `Enum.GetName()`.

```csharp

/** get enum name from value in .Net 6**/
var enumName6 = Enum.GetName((LogLevel)enumValue);
```

## Soluzione 2: Usare il casting del tipo

Un altro modo è quello di convertire il valore enum nel membro di enumerazione utilizzando il casting e quindi utilizzare il metodo `ToString()`.

Si tratta di un metodo semplice che non utilizza alcuna funzione incorporata in `C# Enum`.

Prima si converte il valore enum nel membro di enumerazione e poi si usa il metodo `ToString()`.

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

## Riepilogo

In questo tutorial abbiamo imparato diversi modi per ottenere il valore del nome enum in c# 

1. Passando i parametri enum type e value al metodo `Enum.GetName()` 
2. E utilizzando il casting del tipo al tipo corrispondente di enum 
