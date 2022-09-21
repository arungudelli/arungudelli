
---
title: "C# Case insensitive Contains string check"
description: "En este tutorial aprendemos diferentes formas de hacer la comprobación de cadenas insensibles a mayúsculas y minúsculas en C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


En este tutorial aprendemos diferentes maneras de hacer case insensitive string contains check en C# 

Parece un problema sencillo, pero el método por defecto de C# `string.Contains()` distingue entre mayúsculas y minúsculas 

Y si la cadena no está en el idioma Inglés es decir, para otros idiomas, no podemos comparar el texto insensible a las mayúsculas y minúsculas directamente 

Las dos cadenas deben estar en la misma cultura y debemos conocer la cultura del idioma.

La mayoría de las veces compararemos cadenas en inglés solamente.

## Método 1: Usando el método C# `string.IndexOf()`.

Podemos usar el método C# `string.IndexOf()` para hacer la comprobación de la cadena insensible a mayúsculas y minúsculas.

`IndexOf()` el método acepta el parámetro `StringComparison.OrdinalIgnoreCase`, que especifica el tipo de búsqueda a utilizar para los caracteres.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Método 2: Usando el método `string.Contains()` en .Net 5+ &amp; .NET Core 2.0+

En las últimas versiones de dot net, es decir, en .Net Core 2.0+ y .Net 5+. El método `string.Contains()` tiene un método sobrecargado que acepta el parámetro `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Método 3: Usando el método `Regex.IsMatch()` 

Podemos utilizar expresiones regulares para hacer la comprobación de la cadena que contiene sin distinguir entre mayúsculas y minúsculas.

Si está familiarizado con `Regex`, utilice el método `Regex.IsMatch()` y para comprobar la insensibilidad a mayúsculas y minúsculas pase el parámetro `RegexOptions.IgnoreCase` 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Método 4: Usando `.ToUpper()` &amp `.ToLower()`

Si las cadenas están en inglés y el rendimiento no es un problema, podemos convertir ambas cadenas al mismo caso y luego hacer la comprobación de que la cadena contiene.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains check para otros idiomas

La insensibilidad a las mayúsculas y minúsculas depende del idioma 

Por ejemplo, en el idioma inglés `I` es la versión en mayúsculas de `i`.

Mientras que en el idioma turco la versión en mayúsculas de `i` es el carácter desconocido `İ`.

Para hacer la comprobación de la cadena sin distinguir entre mayúsculas y minúsculas tenemos que utilizar el objeto `CultureInfo`.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

He creado el objeto `CultureInfo` para el idioma turco. Y comparé ambas cadenas usando `CompareInfo` como se muestra a continuación.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## La mejor manera de hacer la comprobación de la cadena Contains insensible a mayúsculas y minúsculas

Si está utilizando la última versión de `.Net` utilice el método `string.Contains()`.

De lo contrario, utilice el método `string.IndexOf()`.

No prefiera los métodos `.ToUpper()` o `To.Lower()` ya que pueden provocar problemas de rendimiento.

Utilice el objeto `CultureInfo` para las cadenas de otros idiomas.

