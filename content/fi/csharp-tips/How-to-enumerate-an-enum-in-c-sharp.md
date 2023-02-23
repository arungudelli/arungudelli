---
title: "Miten enumerate C# enum"
description: " Eri tapoja enumerate C# enum esimerkkien kera"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumeita käytetään laajalti `C#` kielessä. 

Ja on olemassa 4 tapaa enumerate enum `C#` . 

1. `C# Enum.GetValues()` käyttäminen .Net 5:ssä ja sitä uudemmissa ohjelmissa.
2. `C# Enum.GetValues()` käyttäminen vanhemmissa .Net-versioissa.
3. Käyttämällä `C# Enum.GetNames()` enum erate enum nimet merkkijonoina.
4. Käyttäminen `Linq`

Käydään läpi esimerkki, jotta ymmärrämme sen paremmin. 

Ensin luodaan C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

The `enum` edustaa erityyppisiä kirjaustasoja.

Nyt näemme erilaisia tapoja enumerate the `C# enum`.

## `C# Enum.GetValues()` Generic-menetelmän käyttäminen .Net 5:ssä ja sitä uudemmissa ohjelmissa

Jos käytät uusinta versiota `.Net`, eli `.Net 5` tai uudempaa versiota, voit käyttää geneeristä versiota `Enum.GetValues` -menetelmästä enumerate the `C# enum`.

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

Uusi geneerinen versio `Enum.GetValues` palauttaa enum -arvojen joukon. 

Lisäksi voimme käyttää `for` - tai `foreach` -lausekkeita listaamaan `C# enum` nimet. 

Koska array sisältää `enum` tyypin, se on muunnettava merkkijonoksi `ToString()` -menetelmällä.

## `C# Enum.GetValues()` -menetelmän käyttäminen vanhemmissa .Net-versioissa.

Vanhemmissa versioissa `.Net` ei ole käytettävissä geneeristä menetelmää `Enum.GetValues()` -menetelmää varten. 

Sinun on välitettävä `typeof()` enum parametrina `Enum.GetValues()` -metodille. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ja se palauttaa enum arvot tyyppiä `System.Array` ja lisäksi voimme käyttää `foreach` lauseketta kiertääksemme läpi arvot `C# enum` nimet.

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

Jos haluat `IEnumerable` tuloksen, voimme edelleen käyttää `Enum.GetValues()` -metodia.

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

## Käyttämällä `C# Enum.GetNames()` enum erate enum nimiä merkkijonoina 

`C# Enum.GetValues()` menetelmä palauttaa enum tyyppien joukon. 

Siksi muunnimme enum nimet merkkijonoksi ennen niiden tulostamista konsoliin.

Metodin `C# Enum.GetNames()` avulla voimme enumerate enum nimet merkkijonoina, jolloin niitä ei tarvitse muuntaa merkkijonoiksi.

Jos käytät `.Net 5` ja sitä uudempaa, voit käyttää yleistä `C# Enum.GetNames()` -funktiota.

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

Vanhemmissa versioissa meidän on annettava `typeof()` enum -parametri.

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

Jos siis halutaan enumerate-nimet merkkijonoina, voidaan käyttää `C# Enum.GetNames()` -menetelmää.

## Käyttämällä `Linq`

Voimme käyttää `Linq forEach` -menetelmää enumerate C# enum, `Enum.GetValues()` ja `Enum.GetNames()` -menetelmien avulla.

Käytä `.Net 5` ja sen yläpuolella alla olevaa koodinpätkää.

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

Vanhemmissa versioissa

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

## Yhteenveto

Tässä opetusohjelmassa opimme enumerate enum C#-kielellä käyttäen `Enum.GetValues()` - ja `Enum.GetNames()` -metodia.










