---
title: "Как зацикливать/перечислять перечисления в C#"
description: "Различные способы зацикливания или перечисления перечислений в C# с примерами"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

Перечисления широко используются в языке `C#`. 

Существует 4 способа зацикливания или перечисления перечислений в `C#`. 

1. Использование `C# Enum.GetValues()` в .Net 5 и выше.
2. Использование `C# Enum.GetValues()` в старых версиях .Net.
3. Использование `C# Enum.GetNames()` для перечисления имен перечислений в виде строк.
4. Использование `Linq`

Давайте рассмотрим пример, чтобы понять это дальше. 

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

На странице `enum` представлены различные типы уровней протоколирования.

Теперь мы рассмотрим различные способы перечисления `C# enum`.

## Использование метода `C# Enum.GetValues()` Generic в .Net 5 и выше

Если вы используете последнюю версию `.Net`, т.е. `.Net 5` и выше, вы можете использовать общую версию для метода `Enum.GetValues` для перебора `C# enum`.

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

Новая универсальная версия `Enum.GetValues` возвращает массив значений перечисления. 

И далее мы можем использовать операторы `for` или `foreach` для перечисления `C# enum`. 

Поскольку массив содержит тип `enum`, нам необходимо преобразовать его в строку с помощью метода `ToString()`.

## Использование `C# Enum.GetValues()` в старых версиях .Net.

В старых версиях `.Net` не существует общего метода для метода `Enum.GetValues()`. 

Вам необходимо передать `typeof()` enum в качестве параметра в метод `Enum.GetValues()`. 

```csharp
Array logLevels = Enum.GetValues(typeof(LogLevel))
```
Он возвращает значения перечисления типа `System.Array`, и далее мы можем использовать оператор `foreach` для перебора перечислений в C#.

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

## Использование `C# Enum.GetNames()` для перечисления имен перечислений в виде строк 

`C# Enum.GetValues()` метод возвращает массив типов перечислений. 

Поэтому мы преобразовали значения перечислений в строку, прежде чем вывести их в консоль.

Используя метод `C# Enum.GetNames()`, мы можем перечислять имена перечислений в виде строк, поэтому нет необходимости преобразовывать их в строки.

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

В старых версиях нам необходимо передать параметр `typeof()` enum.

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

Поэтому если вы хотите зациклить имена перечислений как строки, мы можем использовать метод `C# Enum.GetNames()`.

## Использование `Linq`

Мы можем использовать метод `Linq forEach` для перечисления перечислений C# с помощью методов `Enum.GetValues()` и `Enum.GetNames()`.

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

В этом уроке мы научились перебирать перечисления в C# с помощью методов `Enum.GetValues()` и `Enum.GetNames()`.










