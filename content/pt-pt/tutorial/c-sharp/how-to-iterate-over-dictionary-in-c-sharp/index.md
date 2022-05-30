+++
title="8 formas de loop/alfabetizar pares de valores chave do dicionário em C#"
summary="A utilização de laço em C# para a frente é a forma mais simples e directa de iterar sobre os valores chave do dicionário em C#"
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Para iterar os pares de valores chave do dicionário em C#, utilize os seguintes métodos

1. Usando o laço C# `foreach` 
2. Iterate over C# dictionary key only
3. Iterar apenas sobre os valores do dicionário C#
4. Usando `Deconstruct` de `KeyValuePair<TKey,TValue>` em C# 7
5. Usando `Deconstruct` e `discards` em C# 7 
6. `Deconstruct` de par de valores chave em versões C# mais antigas
7. Usando a função `dictionary.ElementAt()` e `for` loop
8. Usando C# `dictionary.AsParallel().ForAll()` 

Passemos por um exemplo para o compreender melhor 

Criei um dicionário de amostras usando `C#` para loop

Dê uma vista de olhos no dicionário abaixo `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}}

## Solução 1: Usando `C# foreach` loop

A utilização do laço `C# foreach` é a forma mais simples e directa de iterar sobre os valores chave do dicionário em C#.

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

A variável `dictionary` em cima `foreach` loop terá `KeyValuePair<TKey, TValue>` tipo 

Podemos aceder facilmente a `Key` &amp; `Value` propriedades do tipo `KeyValuePair`.

## Solução 2: Iterate over C# dictionary key only

Se quiser passar por cima apenas das chaves do dicionário, utilize a propriedade C# do dicionário `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Solução 3: Iterar apenas sobre os valores do dicionário C

Se quiser iterar apenas sobre valores do dicionário, utilize a propriedade C# `dictionary.Values` do dicionário.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Solução 4: Usando `Deconstruct()` de `KeyValuePair<TKey,TValue>` em C# 7

Os desconstrutores são introduzidos na versão C# 7.0.
 
E se estiver a utilizar a aplicação .NET Core 2.0+ a `KeyValuePair<TKey, TValue>` tipo terá o método `Deconstruct()`.

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

Para aceder ao par de valores chave do dicionário, utilize a função `Deconstruct()` do tipo `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Solução 5: Usando `Deconstruct` e `discards` em C# 7 

Começando com C# 7.0, C# suporta descartes 

Os descartes são variáveis de lugar reservado que são intencionalmente não utilizadas no código de aplicação 

Muitas vezes referiam-se às variáveis `_`.

Os descartes não são mais do que as variáveis não atribuídas, não têm um valor.

No dicionário, se quiser apenas fazer looping de chaves, podemos fazer uso de variáveis de descarte.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Da mesma forma, se quiser utilizar apenas valores de dicionário.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Solução 6: `Deconstruct` do par de valores chave em versões C# mais antigas


A estrutura KeyValuePair não tem a função `Deconstruct()` nas versões mais antigas do C#.(C# 4.7.2 abaixo) 

Assim, se quiser usar `Deconstruct()` para fazer o loop de pares de valores chave, há uma solução alternativa 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Na maioria dos casos não vamos utilizar este método, mas é bom saber.

## Solução 7: Usando a função `dictionary.ElementAt()` e `for` loop

Podemos utilizar o simples laço `for` para iterar sobre os pares de valores chave do dicionário.

Podemos aceder aos valores `KeyValuePair` através do índice de dicionário usando a função `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Mais uma vez, não é uma boa maneira de fazer loop through dicionário, porque a função `ElementAt()` terá `O(n)` e temos `for` loop above, pelo que a complexidade temporal será `O(n^2)` 

Em grandes dicionários, terá implicações de desempenho.

Se quiser obter o índice dos pares de valores chave do Dicionário, utilize este método 

Não penso em nenhum caso de uso do mundo real onde o índice do dicionário será utilizado 

## Solução 8: Usando C# `dictionary.AsParallel().ForAll()`

Se tiver um dicionário grande, podemos fazer uso da consulta Parallel Language Integrated Query (LINQ) usando o método de extensão `ParallelEnumerable.AsParallel` no dicionário e executando a consulta usando o método `ParallelEnumerable.ForAll`.

A consulta divide a fonte em tarefas que são executadas de forma assíncrona em vários fios

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## A melhor maneira de fazer o dicionário em C# 

Embora tenhamos múltiplas formas de iterar sobre os valores chave de um dicionário, preferimos usar um simples laço de testa 

E se quiser apenas o dicionário C#, use `dictionary.Keys` ou `dictionary.Values` em vez de iterar todo o dicionário 







