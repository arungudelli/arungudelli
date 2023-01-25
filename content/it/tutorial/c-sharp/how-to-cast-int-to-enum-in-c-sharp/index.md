+++
title   ="2 modi per convertire/casttare int in enum in C#"
summary ="Ci sono 2 modi per convertire int in enum in C# 1. Utilizzando il casting di tipo esplicito in C#. 2. Utilizzando il metodo Enum.ToObject()."

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


Ci sono 2 modi per convertire o lanciare `int` in `enum` in C#

1. Utilizzando il casting di tipo esplicito in C#.
2. Utilizzo del metodo `Enum.ToObject()` 

{{%toc%}}

## Soluzione 1: Utilizzo del casting di tipo esplicito in C#

Il modo più semplice per convertire `int` in `enum` in C# è utilizzare il casting di tipo esplicito.

Vediamo un esempio per capire meglio.

Abbiamo un `enum` chiamato `LogLevel`, che rappresenta diversi livelli di registrazione.

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

Il casting esplicito viene fatto mettendo il tipo `enum` tra parentesi davanti al valore `int`.

Ma c'è un problema con la precedente **C# `int` a `enum` conversione**.

Cosa succede se il valore `int` non esiste nella variabile C# `Enum`?

```csharp
int logEnumInteger = 100;
LogLevel unknownEnum = (LogLevel) logEnumInteger;
Console.WriteLine(unknownEnum.ToString());//100
```

Non verrà lanciata alcuna eccezione.

Quindi è meglio controllare se il valore `int` esiste in `C# Enum` prima di lanciarlo in un intero.

## Controllare se un intero esiste o meno in `C# enum` variabile

Per ottenere tutti i valori interi in `C# Enum` possiamo utilizzare il metodo `Enum.GetValues`.

Convertirli in una lista `C#`, in modo da poter utilizzare il metodo `list.Contains()` per verificare se il dato intero esiste nella variabile `enum` variabile.

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
Possiamo usare il metodo `Enum.IsDefined()` per verificare se il valore intero convertito esiste nel tipo dato `enum` tipo.  

```csharp
var enumValue = (LogLevel)1;

if (Enum.IsDefined(typeof(LogLevel), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Soluzione 2: Utilizzare il metodo `Enum.ToObject()` 

È possibile utilizzare il metodo `C# Enum.ToObject()`, per convertire il valore `int` in `enum` in C#.

```
var enumValue = Enum.ToObject(typeof(LogLevel),1);

Console.WriteLine(enumValue);

//ERROR

Console.WriteLine(enumValue.GetType());
//LogLevel

```





