---
title: "Как да enumerate C# enum"
description: " Различни начини за enumerate C# enum с примери"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Енумите са широко използвани в езика `C#`. 

И има 4 начина за enumerate enum в `C#`. 

1. Използване на `C# Enum.GetValues()` в .Net 5 и по-нови версии.
2. Използване на `C# Enum.GetValues()` в по-стари версии на .Net.
3. Използване на `C# Enum.GetNames()` за enumератиране на имена на enum като низове.
4. Използване на `Linq`

Нека разгледаме един пример, за да го разберем по-добре. 

Първо ще създадем C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

Сайтът `enum` представлява различни типове нива на регистриране.

Сега ще видим различни начини за enumерация на `C# enum`.

## Използване на `C# Enum.GetValues()` Generic метод в .Net 5 и по-нови версии

Ако използвате най-новата версия на `.Net`, т.е. `.Net 5` и по-висока, можете да използвате генеричната версия за `Enum.GetValues` метода, за да enumерате `C# enum`.

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

Новата обща версия на `Enum.GetValues` връща масива от стойности на enum. 

И по-нататък можем да използваме изявленията `for` или `foreach`, за да изброим `C# enum` имена. 

Тъй като масивът съдържа `enum` тип, трябва да го преобразуваме в низ, като използваме метода `ToString()`.

## Използване на `C# Enum.GetValues()` в по-старите версии на .Net.

В по-старите версии на `.Net` няма наличен общ метод за метода `Enum.GetValues()`. 

Трябва да предадете `typeof()` enum като параметър на метода `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
И той връща enum стойности от тип `System.Array`, а по-нататък можем да използваме `foreach` оператора, за да направим цикъл през `C# enum` имена.

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

Ако искате резултат `IEnumerable`, можем допълнително да използваме метода `Enum.GetValues()`.

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

## Използване на `C# Enum.GetNames()` за enumеретизиране на enum имена като низове 

`C# Enum.GetValues()` методът връща масив от enum типове. 

Ето защо преобразувахме enum имената в низ, преди да ги отпечатаме в конзолата.

Използвайки метода `C# Enum.GetNames()`, можем да enumеритираме имената enum като низове, така че да не е необходимо да ги конвертираме в низове.

Ако използвате `.Net 5` и по-високи версии, можете да използвате общата функция `C# Enum.GetNames()`.

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

В по-старите версии трябва да подадем параметър `typeof()` enum .

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

Така че, ако искате да enumерате имената като низове, можем да използваме метода `C# Enum.GetNames()`.

## Използване на `Linq`

Метод `Linq forEach` можем да използваме, за да enumerate C# enum, с помощта на методите `Enum.GetValues()` и `Enum.GetNames()`.

В `.Net 5` и по-горе използвайте долния фрагмент от код.

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

В по-старите версии

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

## Резюме

В този урок се научихме да създаваме enumна enum в C#, като използваме методите `Enum.GetValues()` и `Enum.GetNames()`.










