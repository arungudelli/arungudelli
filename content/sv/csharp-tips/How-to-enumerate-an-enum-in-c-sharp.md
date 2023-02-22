---
title: "Hur man loopar/räknar upp C# enum"
description: "Olika sätt att loopa eller räkna upp C# enum med exempel"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enum är ett vanligt förekommande språk i `C#`. 

Det finns 4 sätt att räkna upp eller slinga upp enum i `C#`. 

1. Användning av `C# Enum.GetValues()` i .Net 5 och högre.
2. Användning av `C# Enum.GetValues()` i äldre .Net-versioner.
3. Användning av `C# Enum.GetNames()` för att räkna upp enum-namn som strängar.
4. Användning av `Linq`

Låt oss gå igenom ett exempel för att förstå det bättre. 

Först skapar vi en C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

 `enum` representerar olika typer av loggningsnivåer.

Nu ska vi se olika sätt att räkna upp `C# enum`.

## Använda `C# Enum.GetValues()` Generisk metod i .Net 5 och högre

Om du använder den senaste versionen av `.Net`, dvs. `.Net 5` och senare, kan du använda den generiska versionen av `Enum.GetValues` -metoden för att gå igenom `C# enum`.

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

Den nya generiska versionen av `Enum.GetValues` returnerar en array av enumvärden. 

Vidare kan vi använda `for` eller `foreach` för att räkna upp `C# enum`. 

Eftersom arrayen innehåller typen `enum` måste vi omvandla den till strängar med hjälp av `ToString()` -metoden.

## Användning av `C# Enum.GetValues()` i äldre .Net-versioner.

I de äldre versionerna av `.Net` finns det ingen generisk metod tillgänglig för `Enum.GetValues()` -metoden. 

Du måste skicka `typeof()` enum som en parameter till `Enum.GetValues()` -metoden. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Den returnerar enumvärden av typen `System.Array` och vi kan använda `foreach` -anvisningen för att gå igenom C#-enummet.

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

Om du vill ha resultatet `IEnumerable` kan du använda `Enum.GetValues()` -metoden.

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

## Användning av `C# Enum.GetNames()` för att räkna upp enum-namn som strängar 

`C# Enum.GetValues()` metoden returnerar en array av enumtyper. 

Det är därför vi konverterade enumvärdena till strängar innan vi skrev ut dem i konsolen.

Med hjälp av metoden `C# Enum.GetNames()` kan vi räkna upp enum-namn som strängar, så att vi inte behöver konvertera dem till strängar.

Om du använder `.Net 5` och högre kan du använda den generiska funktionen `C# Enum.GetNames()`.

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

I de äldre versionerna måste vi skicka `typeof()` enum-parametern.

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

Så om du vill slinga enum-namn som strängar kan du använda `C# Enum.GetNames()` -metoden.

## Användning av `Linq`

Vi kan använda metoden `Linq forEach` för att räkna upp C# enum med hjälp av metoderna `Enum.GetValues()` och `Enum.GetNames()`.

I `.Net 5` och högre använder du nedanstående kodutdrag.

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

I äldre versioner

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

## Sammanfattning

I den här handledningen har vi lärt oss hur man loopar genom enum i C# med hjälp av metoderna `Enum.GetValues()` och `Enum.GetNames()`.










