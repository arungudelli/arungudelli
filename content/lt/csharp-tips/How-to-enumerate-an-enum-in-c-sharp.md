---
title: "Kaip sudaryti ciklą ir išvardyti C# enum"
description: "Įvairūs ciklo sudarymo arba išvardijimo būdai C# enum su pavyzdžiais"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumai plačiai naudojami `C#` kalboje. 

Yra 4 būdai, kaip sudaryti ciklą arba išvardyti enumą `C#`. 

1. `C# Enum.GetValues()` naudojimas .Net 5 ir naujesnėse versijose.
2. Naudojant `C# Enum.GetValues()` senesnėse .Net versijose.
3. Naudojant `C# Enum.GetNames()` išvardyti sąrašo vardus kaip eilutes.
4. Naudojant `Linq`

Kad geriau suprastume, panagrinėkime pavyzdį. 

Pirmiausia sukursime C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` atvaizduoja skirtingų tipų registravimo lygius.

Dabar pamatysime skirtingus būdus, kaip išvardyti `C# enum`.

## `C# Enum.GetValues()` bendrojo metodo naudojimas .Net 5 ir naujesnėse versijose

Jei naudojate naujausią `.Net` versiją, t. y. `.Net 5` ir naujesnę, galite naudoti bendrąją `Enum.GetValues` metodo versiją, kad galėtumėte suvesti ciklą per `C# enum`.

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

Naujoji bendroji `Enum.GetValues` versija grąžina enum reikšmių masyvą. 

Ir toliau galime naudoti `for` arba `foreach` teiginius, kad išvardytume `C# enum`. 

Kadangi masyve yra `enum` tipas, turime jį konvertuoti į eilutę naudodami `ToString()` metodą.

## Naudojant `C# Enum.GetValues()` senesnėse .net versijose.

Senesnėse `.Net` versijose nėra bendrojo `Enum.GetValues()` metodo. 

Reikia perduoti `typeof()` enum kaip parametrą `Enum.GetValues()` metodui. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
O jis grąžina `System.Array` tipo enumo reikšmes, o toliau galime naudoti `foreach` teiginį, norėdami cikliškai pereiti per C# enumą.

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

Jei norite `IEnumerable` rezultato, galime toliau naudoti `Enum.GetValues()` metodą.

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

## Naudojant `C# Enum.GetNames()` išvardyti enum vardus kaip eilutes 

`C# Enum.GetValues()` metodas grąžina enum tipų masyvą. 

Todėl prieš spausdindami enum reikšmes į eilutę jas konvertavome į eilutę.

Naudodamiesi `C# Enum.GetNames()` metodu galime išvardyti enum vardus kaip eilutes, todėl jų nereikia konvertuoti į eilutes.

Jei naudojate `.Net 5` ir aukštesnes funkcijas, galite naudoti bendrąją `C# Enum.GetNames()` funkciją.

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

Senesnėse versijose turime perduoti `typeof()` enum parametrą.

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

Taigi, jei norime įrašyti enum vardus kaip eilutes, galime naudoti `C# Enum.GetNames()` metodą.

## Naudojant `Linq`

C# enumams išvardyti galime naudoti `Linq forEach` metodą, naudodami `Enum.GetValues()` ir `Enum.GetNames()` metodus.

Naudodami `.Net 5` ir vėlesnius kodus, naudokite toliau pateiktą kodo fragmentą.

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

Senesnėse versijose

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

## Santrauka

Šioje pamokoje išmokome cikliškai peržiūrėti enum C#, naudodami `Enum.GetValues()` ir `Enum.GetNames()` metodą.










