---
title: "Hogyan lehet a C# enumot hurokba zárni/számozni"
description: "A C# enum hurokba zárásának vagy felsorolásának különböző módjai példákkal"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Az enumokat széles körben használják a `C#` nyelvben. 

És 4 módja van a ciklus vagy enum felsorolásának a `C#`. 

1. A `C# Enum.GetValues()` használata a .Net 5 és magasabb verzióban.
2. A `C# Enum.GetValues()` használata régebbi .Net verziókban.
3. A `C# Enum.GetNames()` használata az enum nevek stringként történő felsorolásához.
4. A  használata `Linq`

Nézzünk végig egy példát, hogy jobban megértsük. 

Először is létrehozunk egy C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

A `enum` különböző típusú naplózási szinteket reprezentál.

Most a `C# enum` felsorolásának különböző módjait fogjuk látni.

## A `C# Enum.GetValues()` általános módszer használata a .Net 5 és újabb verziókban

Ha a `.Net` legújabb verzióját használja, azaz a `.Net 5` és magasabb verziót, akkor a `Enum.GetValues` módszer általános verzióját használhatja a `C# enum` végighaladásához.

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

A `Enum.GetValues` új generikus változata visszaadja az enum értékek tömbjét. 

A továbbiakban pedig a `for` vagy a `foreach` utasításokat használhatjuk a `C# enum` felsorolásához. 

Mivel a tömb a `enum` típust tartalmazza, a `ToString()` módszerrel kell azt stringgé konvertálnunk.

## A `C# Enum.GetValues()` használata a régebbi .Net verziókban.

A `.Net` régebbi verzióiban a `Enum.GetValues()` módszerhez nem áll rendelkezésre általános módszer. 

A `typeof()` enumot paraméterként kell átadni a `Enum.GetValues()` metódusnak. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ez pedig a `System.Array` típusú enum értékeket adja vissza, és a `foreach` utasítással a C# enumot ciklusosan végigjárhatjuk.

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

Ha a `IEnumerable` eredményt szeretnénk, akkor a `Enum.GetValues()` metódust tovább tudjuk castolni.

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

## A `C# Enum.GetNames()` használata az enum nevek felsorolásához karakterláncokként 

`C# Enum.GetValues()` a módszer az enum típusok tömbjét adja vissza. 

Ezért konvertáltuk az enum értékeket sztringgé, mielőtt a konzolra kiírnánk őket.

A `C# Enum.GetNames()` metódus segítségével az enum neveket sztringként tudjuk felsorolni, így nem szükséges sztringgé konvertálni őket.

Ha a `.Net 5` és a felette lévő `C# Enum.GetNames()` függvényt használja, akkor az általános függvényt használhatja.

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

A régebbi verziókban át kell adnunk a `typeof()` enum paramétert.

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

Ha tehát az enum neveket stringként akarjuk hurkosítani, akkor használhatjuk a `C# Enum.GetNames()` módszert.

## A  használatával `Linq`

A `Linq forEach` metódust a `Enum.GetValues()` és `Enum.GetNames()` metódusok segítségével használhatjuk a C# enum felsorolásához.

A `.Net 5` és annál magasabb kódrészletet használjuk az alábbi kódrészletet.

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

A régebbi verziókban

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

## Összefoglaló

Ebben a bemutatóban megtanultuk, hogyan lehet a `Enum.GetValues()` és a `Enum.GetNames()` módszerrel végighaladni az enumon C# nyelven.










