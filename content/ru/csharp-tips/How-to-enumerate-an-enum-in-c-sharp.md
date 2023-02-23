---
title: "Как enumэратировать C# enum"
description: " Различные способы enumэратировать C# enum с примерами"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Перечисления широко используются в языке `C#`. 

И есть 4 способа enumэратировать enum в `C#`. 

1. Использование `C# Enum.GetValues()` в .Net 5 и выше.
2. Использование `C# Enum.GetValues()` в более старых версиях .Net.
3. Использование `C# Enum.GetNames()` для enumэратирования имен enum в виде строк.
4. Использование `Linq`

Давайте рассмотрим пример, чтобы лучше понять это. 

Сначала мы создадим C# `enum`

```csharp
public enum LogLevel
{
   ERROR, 
   WARN, 
   INFO, 
   DEBUG
}
```

На `enum` обозначают различные типы уровней протоколирования.

Теперь мы рассмотрим различные способы enum`C# enum`.

## Использование метода `C# Enum.GetValues()` Generic в .Net 5 и выше

Если вы используете последнюю версию `.Net`, т.е. `.Net 5` и выше, вы можете использовать общую версию для метода `Enum.GetValues`, чтобы enumвывести `C# enum`.

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

Новая общая версия `Enum.GetValues` возвращает массив значений enum. 

Далее мы можем использовать операторы `for` или `foreach` для составления списка `C# enum` имена. 

Поскольку массив содержит `enum` тип, нам необходимо преобразовать его в строку, используя метод `ToString()`.

## Использование `C# Enum.GetValues()` в старых версиях .Net.

В старых версиях `.Net` не существует общего метода для метода `Enum.GetValues()`. 

Вам необходимо передать `typeof()` enum в качестве параметра в метод `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Он возвращает значения enum типа `System.Array` и далее мы можем использовать оператор `foreach` для перебора имен `C# enum` имена.

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

Если вам нужен результат `IEnumerable`, мы можем использовать метод `Enum.GetValues()`.

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

## Использование `C# Enum.GetNames()` для enumэратирования enum имен как строк 

`C# Enum.GetValues()` метод возвращает массив enum типов. 

Поэтому мы преобразовали имена enum в строку, прежде чем вывести их в консоль.

Используя метод `C# Enum.GetNames()`, мы можем enumэрегировать имена enum как строки, так что конвертировать их в строки не требуется.

Если вы используете `.Net 5` и выше, вы можете использовать универсальную функцию `C# Enum.GetNames()`.

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

В старых версиях нам необходимо передать параметр `typeof()` enum .

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

Поэтому если вы хотите en enumerate имена в виде строк, мы можем использовать метод `C# Enum.GetNames()`.

## Использование `Linq`

Мы можем использовать метод `Linq forEach` для enumэратирования C# enum, с помощью методов `Enum.GetValues()` и `Enum.GetNames()`.

В `.Net 5` и выше используйте приведенный ниже фрагмент кода.

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

В более старых версиях

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

В этом уроке мы научились enumэратировать enum в C#, используя метод `Enum.GetValues()` и `Enum.GetNames()`.










