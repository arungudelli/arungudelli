---
title: "Cum să enumerate C# enum"
description: "  Diferite moduri de enumerate C# enum cu exemple"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumerațiile sunt utilizate pe scară largă în limbajul `C#`. 

Și există 4 moduri de enumerate enum în `C#`. 

1. Utilizarea `C# Enum.GetValues()` în .Net 5 și versiunile superioare.
2. Folosind `C# Enum.GetValues()` în versiuni .Net mai vechi.
3. Utilizarea `C# Enum.GetNames()` pentru a enumerată numele enum ca șiruri de caractere.
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

The `enum` reprezintă diferite tipuri de niveluri de jurnalizare.

Acum vom vedea diferite moduri de a enumerate the `C# enum`.

## Utilizarea metodei `C# Enum.GetValues()` Generic în .Net 5 și versiunile superioare

Dacă utilizați cea mai recentă versiune a `.Net`, adică `.Net 5` și versiunile superioare, puteți utiliza versiunea generică a metodei `Enum.GetValues` pentru enumerate the `C# enum`.

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

Noua versiune generică a `Enum.GetValues` returnează matricea de valori enum. 

În continuare, putem utiliza declarațiile `for` sau `foreach` pentru a lista valorile `C# enum` nume. 

Deoarece array-ul conține valorile `enum` tip trebuie să îl convertim în șir de caractere folosind metoda `ToString()`.

## Utilizarea `C# Enum.GetValues()` în versiunile .Net mai vechi.

În versiunile mai vechi ale `.Net` nu există o metodă generică disponibilă pentru metoda `Enum.GetValues()`. 

Trebuie să treceți `typeof()` enum ca parametru pentru metoda `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Aceasta returnează valorile enum de tip `System.Array` și, în continuare, putem utiliza instrucțiunea `foreach` pentru a trece în buclă prin `C# enum` nume.

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

## Utilizarea `C# Enum.GetNames()` pentru a enumerată numele enum ca șiruri de caractere 

`C# Enum.GetValues()` metoda returnează o matrice de tipuri enum. 

De aceea, am convertit numele enum în șiruri de caractere înainte de a le imprima în consolă.

Cu ajutorul metodei `C# Enum.GetNames()` putem enumerate numele enum sub formă de șiruri de caractere, astfel încât nu mai este necesară conversia lor în șiruri de caractere.

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

În versiunile mai vechi, trebuie să transmitem parametrul `typeof()` enum .

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

Astfel, dacă doriți să enumerate nume sub formă de șiruri de caractere, puteți utiliza metoda `C# Enum.GetNames()`.

## Folosind `Linq`

Putem utiliza metoda `Linq forEach` pentru a enumerate C# enum, cu ajutorul metodelor `Enum.GetValues()` și `Enum.GetNames()`.

În `.Net 5` și mai sus folosiți fragmentul de cod de mai jos.

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

În acest tutorial am învățat să enumerate enum în C# folosind metoda `Enum.GetValues()` și `Enum.GetNames()`.










