---
title: "Kuidas enumerate C# enum"
description: " Erinevad viisid enumerate C# enum koos näidetega"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumid on `C#` keeles laialdaselt kasutusel. 

Ja on 4 viisi, kuidas enumerate enum `C#` . 

1. Kasutades `C# Enum.GetValues()` in .Net 5 &amp; above.
2. Kasutades `C# Enum.GetValues()` vanemates .Net versioonides.
3. Kasutades `C# Enum.GetNames()` enum erate enum nimed stringidena.
4. Kasutades `Linq`

Käime selle täpsemaks mõistmiseks läbi ühe näite. 

Kõigepealt loome C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

The `enum` tähistab erinevaid logimistasemeid.

Nüüd näeme erinevaid viise, kuidas enumerateerida `C# enum`.

## `C# Enum.GetValues()` Generic meetodi kasutamine .Net 5 ja kõrgemates versioonides

Kui te kasutate `.Net` uusimat versiooni, st `.Net 5` ja uuemat versiooni, saate kasutada `Enum.GetValues` meetodi enumerate generic versiooni `C# enum`.

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

Uus üldine versioon `Enum.GetValues` tagastab enum väärtuste massiivi. 

Ja edasi saame kasutada `for` või `foreach` avaldusi, et loetleda `C# enum` nimed. 

Kuna massiiv sisaldab `enum` tüübi, peame selle teisendama stringiks, kasutades meetodit `ToString()`.

## Kasutades `C# Enum.GetValues()` vanemates .Net versioonides.

Vanemates versioonides `.Net` ei ole `Enum.GetValues()` meetodi jaoks saadaval üldist meetodit. 

Sa pead andma `typeof()` enum parameetrina `Enum.GetValues()` meetodile üle. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ja see tagastab enum tüüpi `System.Array` väärtused ja edasi saame kasutada `foreach` avaldust, et loopida läbi `C# enum` nimede läbi.

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

Kui soovite `IEnumerable` tulemust, saame edasi valada `Enum.GetValues()` meetodi.

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

## Kasutades `C# Enum.GetNames()`, et enumerate enum nimed stringidena 

`C# Enum.GetValues()` meetod tagastab enum tüüpide massiivi. 

Seepärast teisendasime enum nimed stringiks enne nende väljastamist konsooli.

Kasutades `C# Enum.GetNames()` meetodit saame enumerate enum nimed stringideks, nii et neid ei ole vaja teisendada stringideks.

Kui te kasutate `.Net 5` ja rohkem, võite kasutada üldist `C# Enum.GetNames()` funktsiooni.

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

Vanemates versioonides tuleb edastada `typeof()` enum parameeter.

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

Nii et kui soovite en enumerate nimed stringidena saame kasutada `C# Enum.GetNames()` meetodit.

## Kasutades `Linq`

 `Linq forEach` meetodit saame kasutada enumerate C# enum, `Enum.GetValues()` ja `Enum.GetNames()` meetodite abil.

In `.Net 5` ja eespool kasutada alljärgnevat koodilõiku.

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

Vanemates versioonides

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

## Kokkuvõte

Selles õpetuses õppisime enumerate enum C# keeles, kasutades `Enum.GetValues()` ja `Enum.GetNames()` meetodit.










