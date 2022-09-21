+++
title="Como verificar se uma corda é um número em C#"
summary="Passos para verificar se uma string é um número em c# 1.Declarar uma variável inteira. 2.Passar a string para `int.TryParse()` ou `double.TryParse()` métodos com a variável `out`. 3.Se a cadeia de caracteres for um número `TryParse`, o método retornará verdadeiro. E atribui valor ao número inteiro declarado `out` "
keywords=["verificar se uma cadeia de caracteres é um número em C#"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Passos para verificar se uma cadeia é um número em C#

1. Declare uma variável inteira.
2. Passar cadeia de caracteres para `int.TryParse()` ou `double.TryParse()` métodos com a variável `out`.
3. Se a corda for um número `TryParse` o método voltará a ser verdadeiro. E atribui valor ao inteiro declarado `out` valor.

{{%toc%}}

## Verificar se um fio é um Número ou não em C# 

Por exemplo, temos uma variável de string "123" e se quiser verificar se é numérica utilize o código C# abaixo.

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

A partir de C# 7 podemos declarar [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) variável no próprio Método TryParse.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

O problema com o método `int.TryParse` acima mencionado é que não pode verificar os valores negativos do número de cordas.

## Verificação de número de cordas negativas em C# 

Para verificar valores negativos de números de cordas podemos usar o método C# `double.TryParse()`.

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

## A melhor maneira de verificar se a corda é número em C# 

Utilizar sempre o método `double.TryParse()` para verificar se uma cadeia é um número, porque pode validar tanto números positivos como negativos.