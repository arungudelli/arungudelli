+++
title="8 sätt att loopa/iterera ordboks-nyckelvärdepar i C#"
summary="Att använda C# foreach-slingan är det enklaste och rakaste sättet att iterera över nyckelvärden i ordböcker i C#."
keywords=["loop dictionary in C#, iterera dictionary c#, loop dictionary keys, loop dictionary values"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Använd följande metoder för att iterera nyckel- och värdepar i en ordbok i C#

1. Användning av C# `foreach` loop
2. Iterera endast över C#-ordboksnycklar
3. Iterera endast över C#-ordboksvärden
4. Användning av `Deconstruct` av `KeyValuePair<TKey,TValue>` i C# 7
5. Användning av `Deconstruct` och `discards` i C# 7 
6. `Deconstruct` av nyckel-värdepar i äldre C#-versioner
7. Användning av funktion `dictionary.ElementAt()` och slinga `for` 
8. Användning av C# `dictionary.AsParallel().ForAll()` 

Låt oss gå igenom ett exempel för att förstå det bättre 

Jag har skapat ett exempel på en ordbok med hjälp av `C#` for loop

Ta en titt på nedanstående `C#` ordbok

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Lösning 1: Användning av `C# foreach` loop

Att använda `C# foreach` -slingan är det enklaste och rakaste sättet att iterera över nyckelvärden i ordböcker i C#.

```
foreach (var dictionary in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", dictionary.Key, dictionary.Value);
}

//OUTPUT

dictionary key is key1 and value is value1
dictionary key is key2 and value is value2
dictionary key is key3 and value is value3
dictionary key is key4 and value is value4
dictionary key is key5 and value is value5
```

Variabeln `dictionary` i ovanstående `foreach` -slinga kommer att ha följande värden `KeyValuePair<TKey, TValue>` typ 

Vi kan enkelt få tillgång till `Key` och `Value` egenskaperna hos `KeyValuePair` type.

## Lösning 2: Iterera endast över C#-ordboksnycklar

Om du vill slinga över endast ordboksnycklar använder du egenskapen C#-ordbok `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Lösning 3: Slingra endast över C#-ordboksvärden

Om du vill iterera över endast ordboksvärden använder du egenskapen C# dictionary `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Lösning 4: Användning av `Deconstruct()` av `KeyValuePair<TKey,TValue>` i C# 7

Deconstructors införs i C# 7.0.
 
Och om du använder .NET Core 2.0+ Application är `KeyValuePair<TKey, TValue>` typ kommer att ha metoden `Deconstruct()`.

```
public readonly struct KeyValuePair<TKey, TValue>
{
        private readonly TKey key;

        private readonly TValue value;

        private readonly int _dummyPrimitive;

        public TKey Key
        {
            get
            {
                throw null;
            }
        }

        public TValue Value
        {
            get
            {
                throw null;
            }
        }

        public KeyValuePair(TKey key, TValue value)
        {
            throw null;
        }

        [EditorBrowsable(EditorBrowsableState.Never)]
        public void Deconstruct(out TKey key, out TValue value)
        {
            throw null;
        }

        public override string ToString()
        {
            throw null;
        }
}
```

För att få tillgång till ordbokens nyckel- och värdepar använder du funktionen `Deconstruct()` för typen `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Lösning 5: Användning av `Deconstruct` och `discards` i C# 7 

Från och med C# 7.0 har C# stöd för bortkastningar 

Discards är platshållarvariabler som avsiktligt inte används i programkoden 

Ofta kallas de för underscore `_` variabler.

Discards är inget annat än icke tilldelade variabler, de har inget värde.

Om du i ordboken vill slinga endast nycklar kan vi använda oss av diskarneringsvariabler.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
På samma sätt om du vill använda endast ordboksvärden.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Lösning 6: `Deconstruct` av nyckel-värdepar i äldre C#-versioner


Struct KeyValuePair har inte funktionen `Deconstruct()` i äldre versioner av C# (C# 4.7.2 nedan) 

Så om du vill använda `Deconstruct()` för att slinga nyckelvärdepar finns det en lösning 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

I de flesta fall kommer vi inte att använda den här metoden, men det är bra att veta.

## Lösning 7: Användning av funktionen `dictionary.ElementAt()` och slingan `for` 

Vi kan använda en enkel `for` -slinga för att iterera över ordbokens nyckel- och värdepar.

Vi kan få tillgång till värdena på `KeyValuePair` genom att använda `dictionary.ElementAt()` -funktionen för att få tillgång till ordboksindex.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Återigen är det inte ett bra sätt att slinga sig igenom ordboken, eftersom `ElementAt()` -funktionen kommer att ha `O(n)` och vi har `for` -slinga ovan, så tidskomplexiteten kommer att bli `O(n^2)` 

I stora ordböcker får det konsekvenser för prestandan.

Om du vill få fram indexet för Dictionary key value par använder du den här metoden 

Jag kan inte tänka mig något verkligt användningsfall där ordboksindex används 

## Lösning 8: Användning av C# `dictionary.AsParallel().ForAll()`

Om du har ett stort lexikon kan vi använda oss av LINQ-frågor (Parallel Language Integrated Query) genom att använda tilläggsmetoden `ParallelEnumerable.AsParallel` på lexikonet och utföra frågan med hjälp av metoden `ParallelEnumerable.ForAll`.

Frågan delar upp källan i uppgifter som utförs asynkront på flera trådar

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Bästa sättet att slinga ordboken i C# 

Även om vi har flera sätt att iterera över en ordboks nyckelvärden, föredrar vi att använda en enkel foreach-slinga 

Och om du bara vill slinga C#-ordbokens nycklar eller värden använder du `dictionary.Keys` eller `dictionary.Values` i stället för att iterera hela ordboken 







