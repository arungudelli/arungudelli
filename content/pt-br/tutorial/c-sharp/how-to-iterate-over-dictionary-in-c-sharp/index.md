+++
title="8 formas de loop/alfabetizar pares de valores chave do dicionário em C#"
summary="O uso de loop C# foreach é a maneira mais simples e direta de iterar sobre os valores chave do dicionário em C#"
keywords=["loop dictionary in C#, iterate dictionary c#, loop dictionary keys, loop dictionary values"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
rascunho='falso''
autores=['admin']
[imagem]
focal_point='''
preview_only=false
+++

Para iterar os pares de valores chave do dicionário em C#, use os seguintes métodos

1. Usando o laço C# `foreach` 
2. Iterar somente sobre as chaves do dicionário C#
3. Iterar somente sobre os valores do dicionário C#
4. Usando `Deconstruct` de `KeyValuePair<TKey,TValue>` em C# 7
5. Usando `Deconstruct` e `discards` em C# 7 
6. `Deconstruct` de par de valores chave em versões C# mais antigas
7. Usando a função `dictionary.ElementAt()` e `for` loop
8. Usando C# `dictionary.AsParallel().ForAll()` 

Vamos passar por um exemplo para entendê-lo melhor 

Eu criei um dicionário de amostras usando `C#` para loop

Dê uma olhada no dicionário abaixo `C#` 

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}}

## Solução 1: Usando `C# foreach` loop

Usando `C# foreach` loop é a maneira mais simples e direta de iterar sobre os valores chave do dicionário em C#.

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

A variável `dictionary` no laço `foreach` acima terá `KeyValuePair<TKey, TValue>` tipo 

Podemos acessar facilmente `Key` &amp; `Value` propriedades do tipo `KeyValuePair`.

## Solução 2: Iterar apenas sobre as chaves do dicionário C

Se você quiser passar por cima apenas das chaves do dicionário, use a propriedade C# `dictionary.Keys` do dicionário.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Solução 3: Iterar apenas sobre os valores do dicionário C

Se você quiser iterar sobre apenas valores do dicionário, use o dicionário C# `dictionary.Values` propriedade.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Solução 4: Usando `Deconstruct()` de `KeyValuePair<TKey,TValue>` em C# 7

Os desconstrutores são introduzidos na versão C# 7.0.
 
E se você estiver usando o .NET Core 2.0+ Aplicação a `KeyValuePair<TKey, TValue>` tipo terá o método `Deconstruct()`.

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

Para acessar o par de valores chave do dicionário, use a função `Deconstruct()` do tipo `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Solução 5: Usando `Deconstruct` e `discards` em C# 7 

Começando com C# 7.0, C# suporta descartes 

Os descartes são variáveis de espaço reservado que são intencionalmente não utilizadas no código de aplicação 

Muitas vezes eles se referiam às variáveis `_`.

Os descartes não são nada além das variáveis não atribuídas, eles não têm valor.

No dicionário, se você quiser apenas loopar teclas, podemos fazer uso de variáveis de descarte.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Da mesma forma, se você quiser usar apenas valores de dicionário.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Solução 6: `Deconstruct` do par de valores chave em versões C# mais antigas


A KeyValuePair estrutural não tem `Deconstruct()` função nas versões mais antigas do C#.(C# 4.7.2 abaixo) 

Portanto, se você quiser usar `Deconstruct()` para loopar pares de valores chave, há uma solução 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

A maioria dos casos não usaremos este método, mas é bom saber.

## Solução 7: Usando a função `dictionary.ElementAt()` e `for` loop

Podemos usar o simples laço `for` para iterar sobre os pares de valores chave do dicionário.

Podemos acessar os valores `KeyValuePair` através do índice do dicionário usando a função `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Mais uma vez não é uma boa maneira de fazer loop through dicionário, porque `ElementAt()` função terá `O(n)` e temos `for` loop acima, portanto a complexidade do tempo será `O(n^2)` 

Em grandes dicionários, isso terá implicações de desempenho.

Se você quiser obter o índice de pares de valores chave do Dicionário, use este método 

Não penso em nenhum caso de uso do mundo real onde o índice do dicionário será usado 

## Solução 8: Usando C `dictionary.AsParallel().ForAll()`

Se você tiver um dicionário grande, podemos fazer uso da consulta de LINQ (Parallel Language Integrated Query) usando o método de extensão `ParallelEnumerable.AsParallel` no dicionário e executando a consulta usando o método `ParallelEnumerable.ForAll`.

A consulta divide a fonte em tarefas que são executadas de forma assíncrona em vários fios

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Melhor maneira de loopar o dicionário em C# 

Embora tenhamos várias maneiras de iterar sobre os valores chave de um dicionário, preferimos usar um simples laço frontal 

E se você quiser apenas o dicionário de loop C# Chaves ou Valores use `dictionary.Keys` ou `dictionary.Values` em vez de iterar todo o dicionário 







