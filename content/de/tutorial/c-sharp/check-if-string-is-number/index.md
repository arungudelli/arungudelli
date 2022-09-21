+++
title="Wie prüft man, ob eine Zeichenkette eine Zahl in C# ist"
summary="Schritte, um zu prüfen, ob eine Zeichenkette eine Zahl in C# ist 1.Deklarieren Sie eine Integer-Variable. 2.Übergeben Sie die Zeichenkette an die Methoden `int.TryParse()` oder `double.TryParse()` mit der Variablen `out`. 3.Wenn der String eine Zahl ist, gibt die Methode `TryParse` true zurück. Und weist der deklarierten Integer-Variable `out` einen Wert zu."
keywords=["Prüfen, ob ein String eine Zahl in C# ist"]
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

Schritte, um zu prüfen, ob eine Zeichenfolge eine Zahl in C# ist

1. Deklarieren Sie eine Integer-Variable.
2. Übergeben Sie eine Zeichenkette an die Methoden `int.TryParse()` oder `double.TryParse()` mit der Variablen `out`.
3. Wenn der String eine Zahl ist, gibt die Methode `TryParse` true zurück. Und weist dem deklarierten Integer-Wert `out` einen Wert zu.

{{%toc%}}

## Prüfen, ob eine Zeichenkette eine Zahl ist oder nicht in C# 

Zum Beispiel haben wir eine String-Variable "123", und wenn Sie überprüfen möchten, ob es numerisch ist, verwenden Sie den folgenden C#-Code.

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

Ab C# 7 können wir [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) Variable in TryParse Methode selbst deklarieren.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Das Problem mit der obigen `int.TryParse` Methode ist, dass sie nicht auf negative String-Zahlenwerte prüfen kann.

## Überprüfung auf negative String-Zahlen in C# 

Um nach negativen Zahlenwerten zu suchen, können wir die C#-Methode `double.TryParse()` verwenden.

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

## Bester Weg zu prüfen, ob String eine Zahl in C# ist 

Verwenden Sie immer die Methode `double.TryParse()`, um zu prüfen, ob eine Zeichenkette eine Zahl ist, da sie sowohl positive als auch negative Zahlen überprüfen kann.