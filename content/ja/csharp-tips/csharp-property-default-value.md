---
title: "How to Set default value toC# property orC# auto implemented property"
description: "In this tutorial we will learn 4 different ways to set default value toC# properties using simple examples."
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

C# プロパティや自動実装プロパティは、フィールド、すなわち変数の代わりにクラスで広く使用されています。  

自動実装されたプロパティは、C# 3.0から導入されました。

このチュートリアルでは、C# プロパティにデフォルト値を設定する4つの方法を、簡単な例を使って学びます。

1.C# 6 で自動実装プロパティのイニシャライザを使用する
2.コンストラクタでデフォルト値を割り当てる
3.C# プロパティセッターの使用
4.`DefaultValue` 属性 &amp; プロパティセッターを使う

C# で、プロパティの初期値をデフォルト値とすることができる。

## 方法 1 :C# 6 の自動プロパティ初期化子を使用する。

C# 6 では、自動実装されたプロパティを宣言し、一行でデフォルト値を設定することができます。

構文は以下の通りです。

```csharp
class Product{
    public string Name {get;set;} = "";
}
```
デフォルトの文字列プロパティは、`null` の値を持ちます。C# 6 のインライン宣言を使って、デフォルトの値を空文字列として設定しています。 

## 方法2：コンストラクタでデフォルト値を割り当てる

C#,C# 5 以下の古いバージョンでは、クラスのコンストラクタでC# プロパティのデフォルト値を設定するのがよい方法です。

```csharp
class Product 
{
    public string Name { get; set; }
    public Product()
    {
        Name = "";
    }
}
```

## 方法3：C# プロパティセッターを使用する 

自動実装されたプロパティにデフォルト値を割り当てるには、C# プロパティセッターを利用することができます。

```csharp
class Product 
{
    private string _name = "";
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

## method 4:`DefaultValue` Attribute &amp;&amp; Property Setter を使う。

上記の例では、プライベート変数を作成し、デフォルト値を割り当てています。 

その代わりに、`DefaultValue` 属性を使用してデフォルト値を割り当てることができます。

```csharp
class Product 
{
    private string _name;

    [DefaultValue("")]
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```

`DefaultValue` 属性は、プロパティ・セッターでのみ動作することを忘れないでください。 

以下のコードでは、プロパティにデフォルト値を割り当てません。デフォルト値は`null` のままです。

```csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
```
`DefaultValue` 属性を使用する場合は、プロパティ・セッターを使用する必要があります。


## まとめ

C# 6 を使用している場合は、インライン宣言を使用してC# プロパティにデフォルト値を設定します。それ以外の場合は、コンストラクタでデフォルト値を設定します。 








