---
title: "Kuinka silmukoida/luetella C#-luetteloa"
description: "Eri tapoja silmukoida tai luetella C#-luetteloa esimerkkien avulla"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Enumeita käytetään laajalti `C#` -kielessä. 

Ja on olemassa 4 tapaa silmukoida tai luetella enumia `C#`. 

1. Käyttämällä `C# Enum.GetValues()` in .Net 5 &amp; above.
2. `C# Enum.GetValues()` käyttäminen vanhemmissa .Net-versioissa.
3. `C# Enum.GetNames()` käyttäminen luettelemalla luettelemien nimet merkkijonoina.
4. Käyttäminen `Linq`

Käydään läpi esimerkki sen ymmärtämiseksi tarkemmin. 

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

 `enum` edustaa erityyppisiä kirjaustasoja.

Nyt näemme erilaisia tapoja luetella `C# enum`.

## `C# Enum.GetValues()` Generic-menetelmän käyttäminen .Net 5:ssä ja sitä uudemmissa versioissa

Jos käytät uusinta versiota `.Net` eli `.Net 5` tai uudempaa versiota, voit käyttää `Enum.GetValues` -menetelmän geneeristä versiota `C# enum`-menetelmän läpikäymiseen.

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

Uusi geneerinen versio `Enum.GetValues` palauttaa enum-arvojen joukon. 

Lisäksi voimme käyttää `for` - tai `foreach` -lauseita luettelemalla `C# enum`. 

Koska array sisältää `enum` -tyypin, se on muunnettava merkkijonoksi käyttäen `ToString()` -metodia.

## `C# Enum.GetValues()` käyttäminen vanhemmissa .Net-versioissa.

Vanhemmissa versioissa `.Net` ei ole käytettävissä geneeristä metodia `Enum.GetValues()` -metodia varten. 

Sinun on annettava `typeof()` enum parametrina `Enum.GetValues()` -metodille. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Se palauttaa `System.Array` -tyyppiset enum-arvot, ja lisäksi voimme käyttää `foreach` -lauseketta C#- enumin läpikäymiseen.

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

## Käyttämällä `C# Enum.GetNames()` luettelemalla luettelemien nimet merkkijonoina 

`C# Enum.GetValues()` menetelmä palauttaa enum-tyyppien joukon. 

Siksi muunnimme enum-arvot merkkijonoksi ennen niiden tulostamista konsoliin.

 `C# Enum.GetNames()` -menetelmällä voimme luetella enum-nimet merkkijonoina, joten niitä ei tarvitse muuntaa merkkijonoiksi.

Jos käytät `.Net 5` ja sitä uudempaa toimintoa, voit käyttää yleistä `C# Enum.GetNames()` -funktiota.

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

Vanhemmissa versioissa meidän on annettava `typeof()` enum-parametri.

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

Jos siis haluat silmukoida enum-nimet merkkijonoina, voimme käyttää `C# Enum.GetNames()` -menetelmää.

## Käyttämällä `Linq`

Voimme käyttää `Linq forEach` -metodia C#-luettelon luettelemiseen `Enum.GetValues()` - ja `Enum.GetNames()` -metodien avulla.

 `.Net 5` ja sitä suuremmissa käytetään alla olevaa koodinpätkää.

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

Tässä opetusohjelmassa opimme käymään läpi enumia C#:ssa käyttäen `Enum.GetValues()` ja `Enum.GetNames()` -menetelmää.










