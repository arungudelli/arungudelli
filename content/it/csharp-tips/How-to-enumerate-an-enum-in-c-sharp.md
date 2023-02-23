---
title: "Come enumerare C# enum"
description: " Diversi modi per enumerare C# enum con esempi"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Gli enum sono ampiamente utilizzati nel linguaggio `C#`. 

Ci sono 4 modi per enumerare enum in `C#`. 

1. Usare `C# Enum.GetValues()` in .Net 5 e superiori.
2. Usando `C# Enum.GetValues()` nelle versioni precedenti di .Net.
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

Il `enum` rappresenta diversi tipi di livelli di registrazione.

Vedremo ora diversi modi per enumerare i livelli di registrazione `C# enum`.

## Utilizzo del metodo `C# Enum.GetValues()` Generic in .Net 5 e superiori

Se si utilizza l'ultima versione di `.Net`, ovvero `.Net 5` e superiori, è possibile utilizzare la versione generica del metodo `Enum.GetValues` per enumerare il file `C# enum`.

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

La nuova versione generica di `Enum.GetValues` restituisce l'array di valori enum. 

Inoltre, si possono usare le istruzioni `for` o `foreach` per elencare i nomi `C# enum` nomi. 

Poiché l'array contiene il tipo `enum` dobbiamo convertirlo in stringa utilizzando il metodo `ToString()`.

## Utilizzando `C# Enum.GetValues()` nelle vecchie versioni di .Net.

Nelle versioni più vecchie di `.Net` non è disponibile un metodo generico per il metodo `Enum.GetValues()`. 

È necessario passare `typeof()` enum come parametro al metodo `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Questo metodo restituisce enum valori di tipo `System.Array` e inoltre si può usare l'istruzione `foreach` per scorrere i nomi `C# enum` nomi.

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

Se si desidera un risultato di tipo `IEnumerable`, si può utilizzare il metodo `Enum.GetValues()`.

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

## Usare `C# Enum.GetNames()` per enumerare i nomi di enum come stringhe 

`C# Enum.GetValues()` il metodo restituisce un array di tipi enum. 

Ecco perché abbiamo convertito i nomi enum in stringhe prima di stamparli nella console.

Utilizzando il metodo `C# Enum.GetNames()` possiamo enumerare i nomi enum come stringhe, in modo da non doverli convertire in stringhe.

Se si usa `.Net 5` e oltre, si può usare la funzione generica `C# Enum.GetNames()`.

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

Nelle versioni precedenti è necessario passare il parametro `typeof()` enum .

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

Quindi, se si vogliono enumerare i nomi come stringhe, si può usare il metodo `C# Enum.GetNames()`.

## Utilizzando `Linq`

Possiamo usare il metodo `Linq forEach` per enumerare i nomi in C# enum, con l'aiuto dei metodi `Enum.GetValues()` e `Enum.GetNames()`.

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

In questa esercitazione abbiamo imparato a enumerare enum in C# utilizzando i metodi `Enum.GetValues()` e `Enum.GetNames()`.










