+++
title="Comment vérifier si une chaîne est un nombre en C#"
summary="Etapes pour vérifier si une chaîne est un nombre en c# 1.Déclarer une variable entière. 2.Passez la chaîne aux méthodes `int.TryParse()` ou `double.TryParse()` avec la variable `out`. 3.Si la chaîne est un nombre, la méthode `TryParse` retournera vrai. Et attribue une valeur à la variable entière déclarée `out`."
keywords=["vérifier si une chaîne est un nombre en C#"]
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

Étapes à suivre pour vérifier si une chaîne de caractères est un nombre en C#

1. Déclarer une variable entière.
2. Passez une chaîne de caractères aux méthodes `int.TryParse()` ou `double.TryParse()` avec la variable `out`.
3. Si la chaîne est un nombre, la méthode `TryParse` renvoie true. Et attribue une valeur à la variable entière déclarée `out`.

{{%toc%}}

## Vérifier si une chaîne de caractères est un nombre ou non en C# 

Par exemple, nous avons une variable chaîne "123" et si vous voulez vérifier si elle est numérique, utilisez le code C# ci-dessous.

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

À partir de C# 7, nous pouvons déclarer la variable [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) dans la méthode TryParse elle-même.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Le problème de la méthode `int.TryParse` ci-dessus est qu'elle ne peut pas vérifier les valeurs négatives des chaînes de caractères.

## Vérification d'un nombre négatif de chaînes de caractères en C# 

Pour vérifier les valeurs négatives des chaînes de caractères, nous pouvons utiliser la méthode C# `double.TryParse()`.

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

## Meilleur moyen de vérifier si une chaîne de caractères est un nombre en C# 

Utilisez toujours la méthode `double.TryParse()` pour vérifier si une chaîne est un nombre, car elle peut valider les nombres positifs et négatifs.