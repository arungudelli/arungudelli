+++
title="Jak sprawdzić, czy ciąg znaków jest liczbą w C#"
summary="Kroki do sprawdzenia, czy ciąg znaków jest liczbą w c# 1.Zadeklaruj zmienną typu integer. 2.Przekaż ciąg znaków do metod `int.TryParse()` lub `double.TryParse()` za pomocą zmiennej `out`. 3.Jeśli łańcuch jest liczbą, metoda `TryParse` zwróci wartość true. I przypisze wartość do zadeklarowanej wartości całkowitej `out`."
keywords=["sprawdź, czy ciąg znaków jest liczbą w C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Kroki sprawdzania, czy ciąg znaków jest liczbą w C#

1. Zadeklaruj zmienną typu integer.
2. Przekaż łańcuch do metod `int.TryParse()` lub `double.TryParse()` za pomocą zmiennej `out`.
3. Jeśli łańcuch jest liczbą, metoda `TryParse` zwróci wartość true. I przypisze wartość do zadeklarowanej wartości całkowitej `out`.

{{%toc%}}

## Sprawdzanie, czy ciąg znaków jest liczbą czy nie w języku C# 

Na przykład mamy zmienną łańcuchową "123" i jeśli chcesz sprawdzić, czy jest ona liczbą, użyj poniższego kodu C#.

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

Począwszy od C# 7 możemy deklarować zmienną [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) w samej metodzie TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Problem z powyższą metodą `int.TryParse` polega na tym, że nie sprawdza ona ujemnych wartości liczb łańcuchowych.

## Sprawdzanie ujemnej liczby łańcuchowej w języku C# 

Aby sprawdzić, czy liczba łańcuchowa jest ujemna, możemy użyć metody C# `double.TryParse()`.

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

## Najlepszy sposób na sprawdzenie, czy ciąg znaków jest liczbą w C# 

Zawsze używaj metody `double.TryParse()`, aby sprawdzić, czy ciąg znaków jest liczbą, ponieważ może ona sprawdzać zarówno liczby dodatnie, jak i ujemne.