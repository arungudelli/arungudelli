---
title: " C# özelliğine veya otomatik uygulanan özelliğine varsayılan değer nasıl ayarlanır Bu eğitimde, basit örnekler kullanarak özelliklerine varsayılan değer ayarlamanın 4 farklı yolunu öğreneceğiz

 özellikleri veya otomatik uygulanan özellikler, sınıflarımızda alanların, yani değişkenlerin yerine yaygın olarak kullanılmaktadır.  

Otomatik uygulanan özellikler 3.0'da tanıtılmıştır.

Bu eğitimde, basit örnekler kullanarak özelliklerine varsayılan değer ayarlamanın 4 farklı yolunu öğreneceğiz.

1.  6'da Otomatik Özellik Başlatıcıları Kullanma
2. Yapıcıda varsayılan değer atama
3.  Özellik Ayarlayıcısını Kullanma
4.  Öznitelik &amp;&amp; Özellik Ayarlayıcısını Kullanma

Varsayılan değeri adresindeki özelliğin başlangıç değeri olarak kabul edebiliriz.

 Yöntem 1 : 6'da Otomatik Özellik Başlatıcıları Kullanma

 6'da otomatik olarak uygulanan özelliği bildirebilir ve varsayılan değeri tek bir satır bildiriminde ayarlayabiliriz.

Sözdizimi şöyledir


Varsayılan olarak string özellikleri değerine sahip olacaktır, 6 satır içi bildirimini kullanarak, varsayılan değeri boş string olarak ayarlıyoruz. 

 Yöntem 2: Kurucuda varsayılan değer atama

 , 5 ve altındaki eski sürümlerde, sınıfın kurucusunda özelliklerinin varsayılan değerlerini ayarlamak iyi bir uygulamadır.



 Yöntem 3: Özellik Ayarlayıcısını Kullanma 

Otomatik uygulanan özelliklere varsayılan bir değer atamak için property setter'ı kullanabiliriz.



 yöntem 4: Öznitelik &amp;&amp; Özellik Ayarlayıcısını Kullanma

Yukarıdaki örnekte özel bir değişken oluşturduk ve varsayılan bir değer atadık. 

Bunun yerine varsayılan değer atamak için niteliğini kullanabiliriz.



Unutmayın ** niteliği yalnızca özellik ayarlayıcı ile çalışır.** 

Aşağıdaki kod, özelliğe varsayılan değer atamayacaktır. Varsayılan değer hala şeklindedir.


 niteliğini kullanıyorsanız, özellik ayarlayıcısını kullanmanız gerekir.


 Özet

 6 kullanıyorsanız, özelliklerine varsayılan değeri ayarlamak için satır içi bildirimi kullanın, aksi takdirde varsayılan değeri yapıcıda ayarlayın. 








 C#"
description: " C#"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---C# C# C# C# C# `DefaultValue` C### C# C#```csharp
class Product{
    public string Name {get;set;} = "";
}
``` `null` C### C# C# C#```csharp
class Product 
{
    public string Name { get; set; }
    public Product()
    {
        Name = "";
    }
}
```## C# C#```csharp
class Product 
{
    private string _name = "";
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
```## `DefaultValue` `DefaultValue````csharp
class Product 
{
    private string _name;

    [DefaultValue("")]
    public string Name { 
        
        get { return _name;}
        set { _name = value;} 
    }
}
````DefaultValue` `null````csharp
public class Product
{
    [DefaultValue("")]
    public string Name { get; set; }
}
``` `DefaultValue`## C# C# 