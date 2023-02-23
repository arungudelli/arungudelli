---
title: "Kaip enumerate C# enum"
description: " Įvairūs būdai enumerate C# enum su pavyzdžiais"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumai plačiai naudojami `C#` kalboje. 

Ir yra 4 būdai, kaip enumerate enum `C#` . 

1. `C# Enum.GetValues()` naudojimas .Net 5 ir naujesnėse versijose.
2. Naudojant `C# Enum.GetValues()` senesnėse .Net versijose.
3. Naudojant `C# Enum.GetNames()` enum erate enum vardus kaip eilutes.
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

Svetainė `enum` žymi skirtingus registravimo lygius.

Dabar pamatysime skirtingus būdus, kaip enum`C# enum`.

## `C# Enum.GetValues()` bendrojo metodo naudojimas .Net 5 ir naujesnėse versijose

Jei naudojate naujausią `.Net`, t. y. `.Net 5` ir naujesnę, versiją, galite naudoti bendrąją `Enum.GetValues` metodo versiją, kad enumerate `C# enum`.

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

Ir toliau galime naudoti `for` arba `foreach` teiginius, kad išvardytume `C# enum` vardus. 

Kadangi masyve yra `enum` tipas, turime jį konvertuoti į eilutę naudodami `ToString()` metodą.

## Naudojant `C# Enum.GetValues()` senesnėse .Net versijose.

Senesnėse `.Net` versijose nėra bendrojo `Enum.GetValues()` metodo. 

Reikia perduoti `typeof()` enum kaip parametrą `Enum.GetValues()` metodui. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ir jis grąžina enum tipo `System.Array` reikšmes, o toliau galime naudoti `foreach` teiginį, kad cikliškai pereitume per `C# enum` vardus.

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

## Naudojant `C# Enum.GetNames()` enum erate enum vardus kaip eilutes 

`C# Enum.GetValues()` metodas grąžina enum tipų masyvą. 

Todėl prieš spausdindami enum vardus į eilutę juos konvertavome į eilutę.

Naudodamiesi `C# Enum.GetNames()` metodu galime enumeruoti enum vardus kaip eilutes, kad nereikėtų jų konvertuoti į eilutes.

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

Taigi, jei norite enumerate vardus kaip eilutes, galime naudoti `C# Enum.GetNames()` metodą.

## Naudojant `Linq`

 `Linq forEach` metodą galime naudoti enumerate C# enum, naudodami `Enum.GetValues()` ir `Enum.GetNames()` metodus.

 `.Net 5` ir aukštesniuose formatuose naudokite toliau pateiktą kodo fragmentą.

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

Šioje pamokoje išmokome enumerate enum C# kalba, naudodami `Enum.GetValues()` ir `Enum.GetNames()` metodus.










