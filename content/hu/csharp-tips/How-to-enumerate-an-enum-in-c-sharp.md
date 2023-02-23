---
title: "Hogyan enumerate C# enum"
description: "  A enumerate C# enum különböző módjai példákkal"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Az enumokat széles körben használják a `C#` nyelvben. 

És 4 módja van a enumerate enum a `C#`. 

1. A `C# Enum.GetValues()` használata a .Net 5 és újabb programokban.
2. A `C# Enum.GetValues()` használata régebbi .Net verziókban.
3. A `C# Enum.GetNames()` használata a enuma enum nevek stringként való előállításához.
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

A `enum` különböző típusú naplózási szinteket jelöl.

Most megnézzük a enumkülönböző módozatait `C# enum`.

## A `C# Enum.GetValues()` generikus módszer használata a .Net 5 és újabb verziókban

Ha a `.Net` legújabb verzióját használja, azaz a `.Net 5` és magasabb verziót, akkor a `Enum.GetValues` módszer általános verzióját használhatja a enumerate a módszerhez `C# enum`.

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

A `Enum.GetValues` új általános változata a enum értékek tömbjét adja vissza. 

Továbbá használhatjuk a `for` vagy a `foreach` utasításokat, hogy felsoroljuk a `C# enum` neveket. 

Mivel a tömb tartalmazza a `enum` típust tartalmaz, azt a `ToString()` módszerrel karakterlánccá kell konvertálnunk.

## A `C# Enum.GetValues()` használata a régebbi .Net verziókban.

A `.Net` régebbi verzióiban nem áll rendelkezésre általános módszer a `Enum.GetValues()` módszerhez. 

A `Enum.GetValues()` metódusnak paraméterként át kell adnia a `typeof()` enum  címet. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Ez pedig visszaadja a enum típusú `System.Array` értékeket, és a továbbiakban a `foreach` utasítással végighaladhatunk a típusú értékeken `C# enum` neveken.

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

## A `C# Enum.GetNames()` használata a enumerate enum nevek stringként való átalakításához 

`C# Enum.GetValues()` a módszer a enum típusok tömbjét adja vissza. 

Ezért alakítottuk át a enum neveket sztringgé, mielőtt a konzolra nyomtattuk volna őket.

A `C# Enum.GetNames()` metódus segítségével a enumert tudjuk a enum neveket karakterláncokká alakítani, így nem szükséges azokat karakterláncokká konvertálni.

Ha a `.Net 5` és a felette lévő neveket használja, használhatja az általános `C# Enum.GetNames()` függvényt.

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

Ha tehát a enumerate neveket karakterláncokként szeretnénk megadni, akkor használhatjuk a `C# Enum.GetNames()` módszert.

## A  használata `Linq`

A `Linq forEach` módszert használhatjuk a enumerate C# enum, a `Enum.GetValues()` és a `Enum.GetNames()` módszerek segítségével.

A `.Net 5` és a fentiekben az alábbi kódrészletet használjuk.

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

Ebben a bemutatóban megtanultuk, hogyan kell enumerate enum C# nyelven a `Enum.GetValues()` és a `Enum.GetNames()` módszer segítségével.










