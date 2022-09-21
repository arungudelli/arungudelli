+++
title   ="Como lançar `int` a `enum` em C#"
summary ="Para lançar `int` a `enum` em C#, digite explicitamente a variável `enum` para inteirar"
keywords=["int to enum in C#,cast int to enum in C#"]
type='post'
date='2021-02-10T00:00:51+0000'
lastmod='2022-06-03T00:00:52+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Para lançar `int` a `enum` em C#, digite explicitamente a variável `enum` para inteirar.

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## Solução 1: Usando fundição de tipo explícito de `enum` variável

Passemos por um exemplo para o compreender melhor.

Temos um tipo `enum` chamado `Days`, que representa os dias da semana a partir de segunda-feira.

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

int dayInteger = 6;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//Monday
```

Mas há um problema com **`int` a `enum` conversão***.

E se o valor `int` não existir na variável C# `Enum`?

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

Não irá lançar qualquer excepção.

Por isso é melhor verificar se o valor `int` existe em `Enum` antes de o lançar para o inteiro.

## Verificar se existe ou não um número inteiro na variável `enum` 

Para obter todos os valores inteiros em C# `Enum`, podemos utilizar o método `Enum.GetValues`.

Convertê-los para a lista C#, para que possamos utilizar o método `list.Contains()` para verificar se o número inteiro dado existe na variável `enum`.

```
var intValue = 100;
var enumValues = Enum.GetValues(typeof(Days)).Cast<int>().ToList();

if(enumValues.Contains(intValue)){
  Console.WriteLine("We can Cast int to Enum");  
   Days day = (Days) intValue;
}else{
  Console.WriteLine("Cannot Cast int to Enum");
}

```
Podemos utilizar o método `Enum.IsDefined()` para verificar se existe um valor inteiro convertido no tipo `enum` dado.  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## Solução 2: Utilizar o método `Enum.ToObject()` 

Podemos usar o método `Enum.ToObject()`, converter o valor `int` para `enum` em C#.

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





