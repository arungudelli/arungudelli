---
title: "Kuidas loopida/loendada C# enum"
description: "Erinevad viisid loopida või loendada C# enum koos näidetega"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumid on `C#` keeles laialdaselt kasutusel. 

Ja seal on 4 viisi, kuidas loopida või loendada enum `C#`. 

1. Kasutades `C# Enum.GetValues()` in .Net 5 &amp; above.
2. Kasutades `C# Enum.GetValues()` vanemates .Net versioonides.
3. `C# Enum.GetNames()` kasutamine loenduste nimede loendamiseks stringidena.
4. Kasutades `Linq`

Käime läbi ühe näite, et seda paremini mõista. 

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

 `enum` esindab erinevaid logimistasemeid.

Nüüd näeme erinevaid viise, kuidas loetleda `C# enum`.

## Kasutades `C# Enum.GetValues()` Generic meetodit .Net 5 ja kõrgemates versioonides

Kui te kasutate `.Net` uusimat versiooni, st `.Net 5` ja uuemat versiooni, siis saate kasutada `Enum.GetValues` meetodi generic versiooni, et läbida `C# enum`.

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

Uus üldine versioon `Enum.GetValues` tagastab enum-väärtuste massiivi. 

Ja edasi saame kasutada `for` või `foreach` avaldusi, et loetleda `C# enum`. 

Kuna massiiv sisaldab `enum` tüüpi, peame selle teisendama stringiks, kasutades `ToString()` meetodit.

## Kasutades `C# Enum.GetValues()` vanemates .Net versioonides.

Vanemates `.Net` versioonides ei ole `Enum.GetValues()` meetodi jaoks saadaval üldist meetodit. 

Meetodile `Enum.GetValues()` tuleb parameetrina üle anda `typeof()` enum. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ja see tagastab `System.Array` tüüpi enumi väärtused ja edasi saame kasutada `foreach` avaldust, et C# enumil läbi käia.

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

## Kasutades `C# Enum.GetNames()`, et loendada loenduste nimesid stringidena 

`C# Enum.GetValues()` meetod tagastab enum-tüüpide massiivi. 

Sellepärast konverteerisime enum väärtused stringiks enne nende väljastamist konsooli.

Kasutades meetodit `C# Enum.GetNames()` saame loendada enumide nimed stringidena, nii et neid ei ole vaja teisendada stringideks.

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

Nii et kui soovite loop enum nimed stringidena saame kasutada `C# Enum.GetNames()` meetodit.

## Kasutades `Linq`

 `Linq forEach` meetodit saame kasutada `Enum.GetValues()` ja `Enum.GetNames()` meetodite abil C# enumide loendamiseks.

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

Selles õpiobjektis õppisime C# keeles enumide läbimist, kasutades `Enum.GetValues()` ja `Enum.GetNames()` meetodit.










