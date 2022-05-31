+++
title="Come verificare se una stringa è un numero in C#"
summary="Passi per verificare se una stringa è un numero in C# 1. Dichiarare una variabile intera. 2.Passare la stringa ai metodi `int.TryParse()` o `double.TryParse()` con la variabile `out`. 3.Se la stringa è un numero, il metodo `TryParse` restituirà true. E assegna il valore al valore intero dichiarato `out`."
keywords=["controllare se una stringa è un numero in C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Passi per verificare se una stringa è un numero in C#

1. Dichiarare una variabile intera.
2. Passare la stringa ai metodi `int.TryParse()` o `double.TryParse()` con la variabile `out`.
3. Se la stringa è un numero, il metodo `TryParse` restituirà true. E assegna il valore al valore intero dichiarato `out`.

{{%toc%}}

## Controllare se una stringa è un numero o no in C# 

Ad esempio, abbiamo una variabile stringa "123" e se vogliamo verificare se è un numero, utilizziamo il seguente codice C#.

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

Da C# 7 in poi possiamo dichiarare la variabile [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) nel metodo TryParse stesso.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Il problema del metodo `int.TryParse` di cui sopra è che non può controllare i valori negativi dei numeri di stringa.

## Controllo dei numeri di stringa negativi in C# 

Per verificare la presenza di valori negativi di numeri di stringa, è possibile utilizzare il metodo C# `double.TryParse()`.

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

## Il modo migliore per verificare se una stringa è un numero in C# 

Usare sempre il metodo `double.TryParse()` per verificare se una stringa è un numero, perché può convalidare sia numeri positivi che negativi.