
---
title: "C# Caixa insensível Contém verificação de cordel"
description: "Neste tutorial aprendemos diferentes formas de fazer uma cadeia de caracteres insensível a casos contém verificação em C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Neste tutorial aprendemos diferentes formas de fazer uma sequência insensível a casos contém verificação em C# 

Parece ser um problema simples, mas o método padrão C# `string.Contains()` é sensível a maiúsculas e minúsculas 

E se a corda não estiver em inglês, ou seja, para outras línguas, não podemos comparar directamente os casos de texto insensíveis 

As duas cordas devem estar na mesma cultura e nós devemos conhecer a cultura linguística.

Na maioria das vezes iremos comparar as cordas apenas em língua inglesa.

## Método 1: Usando o método C# `string.IndexOf()`.

Podemos utilizar o método C# `string.IndexOf()` para fazer uma verificação de cadeia insensível a maiúsculas e minúsculas.

`IndexOf()` o método aceita o parâmetro `StringComparison.OrdinalIgnoreCase`, que especifica o tipo de pesquisa a utilizar para os caracteres.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Método 2: Usando o método `string.Contains()` em .Net 5+ &amp; .NET Core 2.0+

Nas últimas versões do dot net, ou seja, em .Net Core 2.0+ e .Net 5+. O método `string.Contains()` tem um método sobrecarregado que aceita o parâmetro `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Método 3: Usando o método `Regex.IsMatch()` 

Podemos usar expressões regulares para fazer a verificação de casos insensíveis contém cordel.

Se estiver familiarizado com `Regex`, utilize o método `Regex.IsMatch()` e verifique se o parâmetro `RegexOptions.IgnoreCase` é insensível a maiúsculas e minúsculas 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Método 4: Usando `.ToUpper()` &amp `.ToLower()`

Se as cordas estiverem em língua inglesa e o desempenho não for um problema, podemos converter ambas as cordas para o mesmo caso, então a corda contém verificação.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Insensível à caixa Contém verificação para outras línguas

A insensibilidade ao caso é dependente da linguagem 

Por exemplo, na língua inglesa `I` é a versão maiúscula de `i`.

Considerando que na versão em maiúsculas em língua turca de `i` é o carácter desconhecido `İ`.

Para fazer a verificação de corda insensível ao caso, precisamos de utilizar o objecto `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Criei `CultureInfo` objecto para a língua turca. E comparei as duas cordas usando `CompareInfo` como se mostra abaixo.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## A melhor maneira de fazer Insensível ao caso Contém verificação de cordel

Se estiver a utilizar a última versão de `.Net`, utilize o método `string.Contains()`.

Caso contrário, seguir o método `string.IndexOf()`.

Não preferem o método `.ToUpper()` ou `To.Lower()`, pois podem conduzir a problemas de desempenho.

Utilizar `CultureInfo` objecto para cordas de outras línguas.

