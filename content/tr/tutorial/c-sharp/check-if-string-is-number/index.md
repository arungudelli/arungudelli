+++
title="C#'ta bir dizenin sayı olup olmadığı nasıl kontrol edilir?"
summary="C#'ta bir dizenin sayı olup olmadığını kontrol etme adımları 1.Bir tamsayı değişkeni beyan edin. 2. `out` değişkeni ile `int.TryParse()` veya `double.TryParse()` metotlarına string geçirin. 3.Eğer string bir sayı ise `TryParse` metodu true döndürecektir. Ve bildirilen tamsayı `out` değerine değer atar."
keywords=["C#'ta bir dizenin sayı olup olmadığını kontrol edin"]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

C#'ta bir dizenin sayı olup olmadığını kontrol etme adımları

1. Bir tamsayı değişkeni bildirir.
2. `int.TryParse()` veya `double.TryParse()` yöntemlerine `out` değişkeni ile dize aktarın.
3. Dize bir sayı ise `TryParse` yöntemi true değerini döndürür. Ve bildirilen tamsayı `out` değerine değer atar.

{{%toc%}}

## C#'ta bir dizenin Sayı olup olmadığını kontrol edin 

Örneğin bir string değişkenimiz "123" var ve bunun sayısal olup olmadığını kontrol etmek istiyorsanız aşağıdaki C# kodunu kullanın.

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

C# 7'den itibaren [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) değişkenini TryParse Metodunun kendisinde bildirebiliriz.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

Yukarıdaki `int.TryParse` yöntemiyle ilgili sorun, negatif dize sayısı değerlerini kontrol edememesidir.

## C#'ta negatif dize sayısı kontrolü 

Negatif string sayı değerlerini kontrol etmek için C# `double.TryParse()` yöntemini kullanabiliriz.

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

## C#'ta dizenin sayı olup olmadığını kontrol etmenin en iyi yolu 

Bir dizenin sayı olup olmadığını kontrol etmek için her zaman `double.TryParse()` yöntemini kullanın, çünkü bu yöntem hem pozitif hem de negatif sayıları doğrulayabilir.