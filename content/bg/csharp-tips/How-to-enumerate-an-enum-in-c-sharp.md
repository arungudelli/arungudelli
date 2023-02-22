---
title: "Как да зациклим/изброяваме C# enum"
description: "Различни начини за зацикляне или изброяване на C# enum с примери"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Енумите са широко използвани в езика `C#`. 

И има 4 начина за създаване на цикъл или изброяване на енум в `C#`. 

1. Използване на `C# Enum.GetValues()` в .Net 5 и по-нови версии.
2. Използване на `C# Enum.GetValues()` в по-стари версии на .Net.
3. Използване на `C# Enum.GetNames()` за изброяване на имената на енумите като низове.
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

 `enum` представя различни видове нива на регистриране.

Сега ще видим различни начини за изброяване на `C# enum`.

## Използване на `C# Enum.GetValues()` Generic method в .Net 5 и по-нови версии

Ако използвате най-новата версия на `.Net`, т.е. `.Net 5` и по-нови версии, можете да използвате обща версия за метода `Enum.GetValues`, за да преминете през цикъла на `C# enum`.

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

Новата генерична версия на `Enum.GetValues` връща масив от стойности на енума. 

И по-нататък можем да използваме оператори `for` или `foreach`, за да изброим `C# enum`. 

Тъй като масивът съдържа типа `enum`, трябва да го преобразуваме в низ, като използваме метода `ToString()`.

## Използване на `C# Enum.GetValues()` в по-старите версии на .Net.

В по-старите версии на `.Net` няма наличен общ метод за метода `Enum.GetValues()`. 

Трябва да предадете `typeof()` enum като параметър на метода `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
И той връща стойности на енума от тип `System.Array`, а по-нататък можем да използваме оператора `foreach`, за да направим цикъл през енума на C#.

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

Ако искате резултат от `IEnumerable`, можем допълнително да използваме метода `Enum.GetValues()`.

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

## Използване на `C# Enum.GetNames()` за изброяване на имената на енумите като низове 

`C# Enum.GetValues()` методът връща масив от енум типове. 

Ето защо конвертирахме стойностите на енумите в низ, преди да ги отпечатаме в конзолата.

Използвайки метода `C# Enum.GetNames()`, можем да изброим имената на енумите като низове, така че не е необходимо да ги конвертираме в низове.

Ако използвате `.Net 5` и по-горни версии, можете да използвате общата функция `C# Enum.GetNames()`.

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

В по-старите версии трябва да подадем параметър `typeof()` enum.

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

Така че ако искате да зациклите имената на енумите като низове, можете да използвате метода `C# Enum.GetNames()`.

## Използване на `Linq`

Можем да използваме метода `Linq forEach`, за да изброяваме C# enum, с помощта на методите `Enum.GetValues()` и `Enum.GetNames()`.

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

В този урок се научихме да правим цикъл през енум в C#, като използваме методите `Enum.GetValues()` и `Enum.GetNames()`.










