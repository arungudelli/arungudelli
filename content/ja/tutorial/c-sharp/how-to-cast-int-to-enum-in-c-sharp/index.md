+++
title   ="C#で`int` を`enum` にキャストする方法"
summary ="C#で`int` を`enum` にキャストするには、変数`enum` を明示的に integer にタイプキャストします。"
keywords=["C#でintをenumにする,C#でintをenumにキャストする"]
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

C#で`int` を`enum` にキャストするには、明示的に`enum` 変数を integer にタイプキャストしてください。

```
SampleEnum sample = (SampleEnum)IntVariable;
```

{{%toc%}}

## 解決策1:`enum` 変数の明示的な型変換を利用する

例題でさらに理解を深めましょう。

`Days` という`enum` 型があり、これは月曜日から始まる曜日を表しています。

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

しかし、上記の **`int` から`enum` への変換** には問題があります。

もし、`int` の値が C# の`Enum` 変数に存在しない場合はどうなるのでしょうか？

```
int dayInteger = 100;
Days day = (Days) dayInteger;
Console.WriteLine(day.ToString());//100
```

例外はスローされません。

ですから、`int` の値を整数にキャストする前に、`Enum` に存在するかどうかをチェックする方がよいでしょう。

## 変数`enum` に整数が存在するかどうかをチェックする

C#`Enum` のすべての整数値を取得するには、`Enum.GetValues` メソッドを使用します。

それらを C# のリストに変換し、`list.Contains()` メソッドで与えられた整数が`enum` 変数に存在するかどうかをチェックできるようにします。

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
`Enum.IsDefined()` メソッドで、変換された整数値が与えられた`enum` 型に存在するかどうかをチェックすることができます。  

```
var enumValue = (Days)1;

if (Enum.IsDefined(typeof(Days), enumValue)){
   Console.WriteLine("The converted int to enum value is",enumValue);
}else{
   Console.WriteLine("Cannot Convert int to Enum",enumValue);
}
```


## 解決策2：`Enum.ToObject()` メソッドを使う

C#で`int` の値を`enum` に変換する`Enum.ToObject()` メソッドを使用することができます。

```
var enumValue = Enum.ToObject(typeof(Days),1);

Console.WriteLine(enumValue);

//Tuesday

Console.WriteLine(enumValue.GetType());
//Days

```





