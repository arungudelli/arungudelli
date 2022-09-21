+++
title="C#で文字列が数値かどうかを確認する方法"
summary="C#で文字列が数値かどうかを確認する手順 1.整数変数を宣言する。 2.`out` 変数で`int.TryParse()` または`double.TryParse()` メソッドに文字列を渡す。 3.文字列が数値の場合、`TryParse` メソッドは真を返します。そして宣言された整数`out` の値に値を代入する。"
keywords=["check if a string is number in C#" ]
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

C#で文字列が数値かどうかを確認する手順

1.整数型変数を宣言する。
2.`out` 変数で、`int.TryParse()` または`double.TryParse()` メソッドに文字列を渡す。
3.文字列が数値の場合、`TryParse` メソッドは真を返します。そして宣言された整数値`out` に値を代入する。

{{%toc%}}

## C#で文字列が数値かどうかをチェックする。 

例えば、文字列変数 "123 "があり、それが数値かどうかをチェックしたい場合は、以下のC#コードを使用します。

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

C# 7以降では、TryParseメソッド自体で[out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/)変数を宣言することができるようになりました。

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

上記`int.TryParse` メソッドの問題点は、負の文字列数値のチェックができないことです。

## C#で負の文字列数をチェックする 

負の文字列番号の値をチェックするには、C#の`double.TryParse()` メソッドを使用します。

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

## C# で文字列が数値かどうかを確認する最良の方法 

文字列が数字であるかどうかを確認するには、常に`double.TryParse()` メソッドを使用します。