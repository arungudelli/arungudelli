+++
title   ="Como obter o valor `int` a partir de `Enum` em C# com exemplos"
summary ="Para obter o valor `int` a partir de `enum` em C#, lançar a variável enumerativa ao inteiro"
keywords=["int value from enum in C#,Convert string to enum in C#"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Para obter o valor `int` de `enum` em C#, lance a variável `enum` para o número inteiro.

{{%toc%}}

## Solução 1: Use o tipo de elenco para obter o valor `int` de `enum`

O tipo subjacente padrão para `enums` em C# é `Int`.

Por isso, podemos escrever o `enum` a `int` para obter o valor inteiro do enumero em C#.

Tomaremos um exemplo para o compreender melhor.

```
public enum Days
{
        Monday,  
        Tuesday,  
        Wednesday,  
        Thursday,  
        Friday,  
        Saturday,  
        Sunday
}
```

Agora vamos lançar valores enuméricos a valores inteiros.

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## Solução 2: Utilizar o método `Convert.ToInt32()` para obter o valor inteiro do enumero

Ou podemos usar o `Convert.ToInt32()` para converter um `enum` em inteiro, como se mostra abaixo.

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## Obtenha o valor `enum` de diferentes tipos subjacentes

`Enums` em C# pode ter diferentes tipos subjacentes 

Se o C# enum for declarado como um `uint`, `long`, ou `ulong` devemos lançá-lo para o tipo correspondente do `enum`.

Considere o exemplo abaixo de `Stars` enum, que tem um tipo `long`.

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```