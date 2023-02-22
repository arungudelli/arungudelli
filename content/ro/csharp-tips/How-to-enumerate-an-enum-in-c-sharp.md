---
title: "Cum se face o buclă/enumerare C# enumera"
description: "Diferite moduri de a face buclă sau de a enumera C# enum cu exemple"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumerațiile sunt utilizate pe scară largă în limbajul `C#`. 

Și există 4 moduri de a face buclă sau de a enumera enum în `C#`. 

1. Folosind `C# Enum.GetValues()` în .Net 5 și versiunile superioare.
2. Utilizarea `C# Enum.GetValues()` în versiunile .Net mai vechi.
3. Utilizarea `C# Enum.GetNames()` pentru a enumera nume de enumerații ca șiruri de caractere.
4. Utilizarea `Linq`

Să parcurgem un exemplu pentru a înțelege mai bine acest lucru. 

În primul rând vom crea un fișier C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` reprezintă diferite tipuri de niveluri de logare.

Acum vom vedea diferite moduri de a enumera `C# enum`.

## Utilizarea metodei `C# Enum.GetValues()` Generic în .Net 5 și versiunile superioare

Dacă utilizați cea mai recentă versiune a `.Net`, adică `.Net 5` și versiunile superioare, puteți utiliza versiunea generică a metodei `Enum.GetValues` pentru a trece în buclă prin `C# enum`.

```csharp
void loopEnum()
{
   LogLevel[] logLevels = Enum.GetValues<LogLevel>();
   
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Noua versiune generică a metodei `Enum.GetValues` returnează matricea de valori enum. 

În continuare, putem utiliza declarațiile `for` sau `foreach` pentru a enumera `C# enum`. 

Deoarece matricea conține tipul `enum`, trebuie să o convertim în șir de caractere utilizând metoda `ToString()`.

## Utilizarea `C# Enum.GetValues()` în versiunile .Net mai vechi.

În versiunile mai vechi ale `.Net` nu există o metodă generică disponibilă pentru metoda `Enum.GetValues()`. 

Trebuie să treceți `typeof()` enum ca parametru la metoda `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Aceasta returnează valori enum de tip `System.Array` și, în continuare, putem utiliza instrucțiunea `foreach` pentru a parcurge în buclă enumerația C#.

```csharp
void loopEnum()
{
   Array logLevels = Enum.GetValues(typeof(LogLevel))
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

Dacă doriți rezultatul `IEnumerable`, putem folosi metoda `Enum.GetValues()`.

```csharp
void loopEnum()
{
   var logLevels = Enum.GetValues(typeof(LogLevel)).Cast<LogLevel>();
   foreach (LogLevel logLevel in logLevels)
   {
        Console.WriteLine(logLevel.ToString());
   }
}
```

## Utilizarea metodei `C# Enum.GetNames()` pentru a enumera nume de enumerații ca șiruri de caractere 

`C# Enum.GetValues()` metoda returnează o matrice de tipuri de enumerații. 

De aceea, am convertit valorile enum în șiruri de caractere înainte de a le imprima în consolă.

Utilizând metoda `C# Enum.GetNames()` putem enumera numele enum ca șiruri de caractere, astfel încât nu este necesară conversia lor în șiruri de caractere.

Dacă utilizați `.Net 5` și versiunile superioare, puteți utiliza funcția generică `C# Enum.GetNames()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames<LogLevel>();
   
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

În versiunile mai vechi, trebuie să transmitem parametrul enum `typeof()`.

```csharp
void loopEnum()
{
   string[] logLevels = Enum.GetNames(typeof(LogLevel));
   foreach (string logLevel in logLevels)
   {
        Console.WriteLine(logLevel);
   }
}
```

Astfel, dacă doriți să utilizați numele enum ca șiruri de caractere, puteți utiliza metoda `C# Enum.GetNames()`.

## Folosind `Linq`

Putem utiliza metoda `Linq forEach` pentru a enumera enum C#, cu ajutorul metodelor `Enum.GetValues()` și `Enum.GetNames()`.

În `.Net 5` și mai sus, utilizați fragmentul de cod de mai jos.

```csharp
//Using Enum.GetValues
Enum.GetValues<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames<LogLevel>()
        .ToList()
        .ForEach(loglevel => Console.WriteLine(loglevel));        
```

În versiunile mai vechi

```csharp
//Using Enum.GetValues
Enum.GetValues(typeof(LogLevel))
    .Cast<LogLevel>().ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel.ToString()));

//Using Enum.GetNames
Enum.GetNames(typeof(LogLevel))
    .ToList()
    .ForEach(loglevel => Console.WriteLine(loglevel));    
```

## Rezumat

În acest tutorial am învățat să parcurgem în buclă enum în C# folosind metoda `Enum.GetValues()` și `Enum.GetNames()`.










