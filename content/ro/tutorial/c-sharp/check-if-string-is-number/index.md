+++
title="Cum să verificați dacă un șir de caractere este un număr în C#"
summary="Pași pentru a verifica dacă un șir de caractere este un număr în c# 1.Declară o variabilă întreagă. 2.2.Treceți șirul de caractere la metodele `int.TryParse()` sau `double.TryParse()` cu variabila `out`. 3.Dacă șirul este un număr, metoda `TryParse` va returna true. Și atribuie valoarea la valoarea întreagă declarată `out`."
keywords=["verificați dacă un șir de caractere este număr în C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Pași pentru a verifica dacă un șir de caractere este un număr în C#

1. Declarați o variabilă de număr întreg.
2. Treceți șirul de caractere la metodele `int.TryParse()` sau `double.TryParse()` cu variabila `out`.
3. Dacă șirul este un număr, metoda `TryParse` va returna true. Și atribuie valoarea la valoarea întreagă declarată `out`.

{{%toc%}}

## Verifică dacă un șir de caractere este sau nu un număr în C# 

De exemplu, avem o variabilă de tip șir de caractere "123" și dacă doriți să verificați dacă este un număr, utilizați codul C# de mai jos.

```
var stringNumber = "123";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is true and numericValue=123

var stringNumber = "123P";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is false and numericValue=0 default value

```

Începând cu C# 7, putem declara variabila [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) chiar în metoda TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Problema metodei `int.TryParse` de mai sus este că nu poate verifica valorile negative ale șirurilor de caractere.

## Verificarea numerelor de șir de caractere negative în C# 

Pentru a verifica valorile negative ale unui șir de caractere, putem utiliza metoda C# `double.TryParse()`.

```
var negativeString = "-123";
double number;
if(double.TryParse(negativeString,out number)){
   if (number > 0){

   }else{
       //negative number 
   }   
}
```

## Cea mai bună metodă de a verifica dacă un șir de caractere este un număr în C# 

Utilizați întotdeauna metoda `double.TryParse()` pentru a verifica dacă un șir de caractere este un număr, deoarece poate valida atât numere pozitive, cât și negative.