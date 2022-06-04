+++
title   ="C#で`Enum` から`int` の値を取得する方法と例"
summary ="C#で`enum` から`int` の値を取得するには、enum変数を整数にキャストします。"
keywords=["C#でenumからint値を取得する,C#で文字列をenumに変換する"]
type='post'
date='2020-01-04T18:08:51+0000'
lastmod='2022-06-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

C#で`enum` から`int` の値を取得するには、`enum` 変数を整数にキャストしてください。

{{%toc%}}

## 解決策1: 型キャストを使用して、`int` から値を取得する。`enum`

C# の`enums` のデフォルトの基礎となる型は`Int` です。

したがって、C#のenumから整数値を取得するために、`enum` を`int` にタイプキャストすることができます。

ここでは、例題を挙げて、さらに理解を深めていきます。

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

では、enumの値を整数値にキャストしてみます。

```
int mondayValue=(int)Days.Monday; //0
int tuesdayValue=(int)Days.Tuesday; //1
int wednesdayValue=(int)Days.Wednesday; //2
int thursdayValue=(int)Days.Thursday; //3
int fridayValue=(int)Days.Friday; //4
int saturdayValue=(int)Days.Saturday; //5
int sundayValue=(int)Days.Sunday; //6
```

## 解決策2:`Convert.ToInt32()` メソッドを使ってenumから整数値を取得する

また、`Convert.ToInt32()` to メソッドを使用して、以下のように`enum` を整数に変換することができます。

```
int mondayValue=Convert.ToInt32(Days.Moday); //0

```

## 異なる型の基礎となる`enum` の値を取得する

`Enums` C#では、異なる基礎となる型を持つことができます。 

C#のenumが`uint`,`long`, または`ulong` と宣言されている場合、対応する`enum` の型にキャストする必要があります。

次の例では、`Stars` の enum が`long` という型を持っているとします。

```
enum Stars:long 
{
    Sun = 1, Star1 = 2,Star2=3, .. Startn = n
};

var sunValue = (long)Stars.Sun;//1
```