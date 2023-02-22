---
title: "Come eseguire un ciclo/enumerazione di enum in C#"
description: "Diversi modi per eseguire un ciclo o un'enumerazione di enum in C#, con esempi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Gli enum sono ampiamente utilizzati nel linguaggio `C#`. 

Ci sono 4 modi per eseguire il loop o l'enumerazione di enum in `C#`. 

1. Utilizzo di `C# Enum.GetValues()` in .Net 5 e superiori.
2. Utilizzo di `C# Enum.GetValues()` nelle versioni precedenti di .Net.
3. Utilizzo di `C# Enum.GetNames()` per enumerare i nomi di enum come stringhe.
4. Utilizzo di `Linq`

Vediamo un esempio per capire meglio. 

Per prima cosa creeremo un oggetto C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` rappresenta diversi tipi di livelli di registrazione.

Vedremo ora diversi modi per enumerare i `C# enum`.

## Usare il metodo `C# Enum.GetValues()` Generic in .Net 5 e superiori

Se si utilizza l'ultima versione di `.Net`, ossia `.Net 5` e superiori, è possibile utilizzare la versione generica del metodo `Enum.GetValues` per eseguire un ciclo di `C# enum`.

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

La nuova versione generica di `Enum.GetValues` restituisce un array di valori enum. 

Inoltre, possiamo usare le istruzioni `for` o `foreach` per enumerare i valori di `C# enum`. 

Poiché l'array contiene il tipo `enum`, dobbiamo convertirlo in stringa con il metodo `ToString()`.

## Utilizzando `C# Enum.GetValues()` nelle vecchie versioni di .Net.

Nelle versioni più vecchie di `.Net` non è disponibile un metodo generico per il metodo `Enum.GetValues()`. 

È necessario passare l'enum `typeof()` come parametro al metodo `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Questo metodo restituisce valori enum di tipo `System.Array` e inoltre si può utilizzare l'istruzione `foreach` per eseguire un ciclo attraverso l'enum in C#.

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

Se si desidera un risultato di tipo `IEnumerable`, è possibile eseguire un ulteriore cast del metodo `Enum.GetValues()`.

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

## Utilizzo di `C# Enum.GetNames()` per enumerare i nomi di enum come stringhe 

`C# Enum.GetValues()` il metodo restituisce un array di tipi di enum. 

Ecco perché abbiamo convertito i valori degli enum in stringhe prima di stamparli nella console.

Utilizzando il metodo `C# Enum.GetNames()` possiamo enumerare i nomi degli enum come stringhe, in modo da non doverli convertire in stringhe.

Se si utilizza il metodo `.Net 5` o superiore, è possibile utilizzare la funzione generica `C# Enum.GetNames()`.

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

Nelle versioni precedenti è necessario passare il parametro enum `typeof()`.

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

Perciò, se si vogliono inserire in loop i nomi delle enum come stringhe, si può usare il metodo `C# Enum.GetNames()`.

## Utilizzando `Linq`

Possiamo usare il metodo `Linq forEach` per enumerare gli enum in C#, con l'aiuto dei metodi `Enum.GetValues()` e `Enum.GetNames()`.

In `.Net 5` e oltre, utilizzare il seguente frammento di codice.

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

Nelle versioni precedenti

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

## Sommario

In questo tutorial abbiamo imparato a fare un ciclo di enum in C# usando i metodi `Enum.GetValues()` e `Enum.GetNames()`.










