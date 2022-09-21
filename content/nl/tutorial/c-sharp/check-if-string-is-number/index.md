+++
title="Hoe te controleren of een string een nummer is in C#"
summary="Stappen om te controleren of een string een getal is in c# 1.Declare an integer variable. 2.Geef string door aan `int.TryParse()` of `double.TryParse()` methodes met `out` variabele. 3.Als de string een getal is zal `TryParse` methode true teruggeven. En kent waarde toe aan het gedeclareerde gehele getal `out` waarde."
keywords=["check if a string is number in C#"]
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

Stappen om te controleren of een string een getal is in C#

1. Geef een integer variabele aan.
2. Geef string door aan `int.TryParse()` of `double.TryParse()` methodes met `out` variabele.
3. Als de string een getal is zal `TryParse` methode true teruggeven. En kent waarde toe aan het gedeclareerde gehele getal `out` waarde.

{{%toc%}}

## Controleer of een string een getal is of niet in C# 

We hebben bijvoorbeeld een string variabele "123" en als je wilt controleren of het numeriek is gebruik dan de onderstaande C# code.

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

Vanaf C# 7 kunnen we [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) variabele declareren in TryParse Method zelf.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Het probleem met de bovenstaande `int.TryParse` methode is dat het niet kan controleren op negatieve string getal waarden.

## Controleren op een negatief tekenreeks getal in C# 

Om te controleren op negatieve string getal waarden kunnen we gebruik maken van de C# `double.TryParse()` methode.

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

## Beste manier om te controleren of string een getal is in C# 

Gebruik altijd `double.TryParse()` methode om te controleren of een string een getal is, omdat het zowel positieve als negatieve getallen kan valideren.