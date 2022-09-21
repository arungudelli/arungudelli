+++
title="C#'ta sözlük anahtar değer çiftlerini döngüye sokmanın/yinelemenin 8 yolu"
summary="C# foreach döngüsünü kullanmak, C#'ta sözlük anahtar değerleri üzerinde yineleme yapmanın en basit ve anlaşılır yoludur."
keywords=["C#'ta sözlük döngüsü, c# sözlük yineleme, sözlük anahtarları döngüsü, sözlük değerleri döngüsü"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[resim]
focal_point=''
preview_only=false
+++

C#'ta sözlük anahtar değer çiftlerini yinelemek için aşağıdaki yöntemleri kullanın

1. C# kullanarak `foreach` döngüsü
2. Yalnızca C# sözlük anahtarları üzerinde yineleme
3. Yalnızca C# sözlük değerleri üzerinde yineleme
4. `Deconstruct` adresini kullanarak `KeyValuePair<TKey,TValue>` c# 7'de
5. C# 7'de `Deconstruct` ve `discards` adreslerini kullanma 
6. `Deconstruct` eski C# sürümlerinde anahtar değer çiftinin
7. `dictionary.ElementAt()` işlevini ve `for` döngüsünü kullanma
8. C# Kullanma `dictionary.AsParallel().ForAll()` 

Bunu daha iyi anlamak için bir örnek üzerinden gidelim 

 `C#` for döngüsünü kullanarak örnek bir sözlük oluşturdum

Aşağıdaki `C#` sözlüğe bir göz atın

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{%toc%}}

## Çözüm 1: `C# foreach` döngüsünü kullanma

 `C# foreach` döngüsünü kullanmak, C#'ta sözlük anahtar değerleri üzerinde yineleme yapmanın en basit ve anlaşılır yoludur.

```
foreach (var dictionary in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", dictionary.Key, dictionary.Value);
}

//OUTPUT

dictionary key is key1 and value is value1
dictionary key is key2 and value is value2
dictionary key is key3 and value is value3
dictionary key is key4 and value is value4
dictionary key is key5 and value is value5
```

Yukarıdaki `foreach` döngüsünde `dictionary` değişkeni `KeyValuePair<TKey, TValue>` tip 

 `KeyValuePair` türündeki `Key` &amp; `Value` özelliklerine kolayca erişebiliriz.

## Çözüm 2: Yalnızca C# sözlük anahtarları üzerinde yineleme yapın

Yalnızca sözlük anahtarları üzerinde döngü yapmak istiyorsanız C# dictionary `dictionary.Keys` özelliğini kullanın.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Çözüm 3: Yalnızca C# sözlük değerleri üzerinde yineleme yapın

Yalnızca sözlük Değerleri üzerinde yineleme yapmak istiyorsanız C# dictionary `dictionary.Values` özelliğini kullanın.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Çözüm 4: `Deconstruct()` adresini kullanarak `KeyValuePair<TKey,TValue>` c# 7'de

Deconstructor'lar C# 7.0 sürümünde tanıtılmıştır.
 
Ve eğer .NET Core 2.0+ Uygulamasını kullanıyorsanız `KeyValuePair<TKey, TValue>` türü `Deconstruct()` yöntemine sahip olacaktır.

```
public readonly struct KeyValuePair<TKey, TValue>
{
        private readonly TKey key;

        private readonly TValue value;

        private readonly int _dummyPrimitive;

        public TKey Key
        {
            get
            {
                throw null;
            }
        }

        public TValue Value
        {
            get
            {
                throw null;
            }
        }

        public KeyValuePair(TKey key, TValue value)
        {
            throw null;
        }

        [EditorBrowsable(EditorBrowsableState.Never)]
        public void Deconstruct(out TKey key, out TValue value)
        {
            throw null;
        }

        public override string ToString()
        {
            throw null;
        }
}
```

Sözlüğün anahtar değer çiftine erişmek için `KeyValuePair` türündeki `Deconstruct()` işlevini kullanın.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Çözüm 5: C# 7'de `Deconstruct` ve `discards` adreslerini kullanma 

C# 7.0 ile başlayarak, C# ıskartaları destekler 

Atılanlar, uygulama kodunda kasıtlı olarak kullanılmayan yer tutucu değişkenlerdir 

Genellikle alt çizgi `_` değişkenleri olarak adlandırılırlar.

Iskartalar atanmamış değişkenlerden başka bir şey değildir, bir değerleri yoktur.

Sözlükte yalnızca Anahtarları döngüye sokmak istiyorsanız, atma değişkenlerinden yararlanabiliriz.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Benzer şekilde, yalnızca sözlük değerlerini kullanmak istiyorsanız.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Çözüm 6: `Deconstruct` eski C# sürümlerinde anahtar değer çifti


C#'ın eski sürümlerinde struct KeyValuePair'in `Deconstruct()` işlevi yoktur (C# 4.7.2 aşağıda) 

Dolayısıyla, anahtar değer çiftlerini döngüye sokmak için `Deconstruct()` adresini kullanmak istiyorsanız, geçici bir çözüm vardır 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Çoğu durumda bu yöntemi kullanmayacağız, ancak bilmekte fayda var.

## Çözüm 7: `dictionary.ElementAt()` işlevini ve `for` döngüsünü kullanma

Sözlük anahtar değer çiftleri üzerinde yineleme yapmak için basit `for` döngüsünü kullanabiliriz.

 `dictionary.ElementAt()` fonksiyonunu kullanarak `KeyValuePair` değerlerine sözlük indeksi ile erişebiliriz.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Yine sözlükte döngü yapmak için iyi bir yol değildir, çünkü `ElementAt()` işlevi `O(n)` 'a sahip olacaktır ve yukarıda `for` döngüsüne sahibiz, bu nedenle zaman karmaşıklığı `O(n^2)` olacaktır 

Büyük sözlüklerde bunun performans etkileri olacaktır.

Sözlük anahtar değer çiftlerinin dizinini almak istiyorsanız bu yöntemi kullanın 

Sözlük dizininin kullanılacağı herhangi bir gerçek kullanım durumu düşünmüyorum 

## Çözüm 8: C# Kullanımı `dictionary.AsParallel().ForAll()`

Eğer büyük bir sözlüğünüz varsa, sözlük üzerinde `ParallelEnumerable.AsParallel` extension metodunu kullanarak Parallel Language Integrated Query (LINQ) sorgusundan yararlanabilir ve `ParallelEnumerable.ForAll` metodunu kullanarak sorguyu çalıştırabiliriz.

Sorgu, kaynağı birden fazla iş parçacığı üzerinde eşzamansız olarak yürütülen görevlere böler

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## C#'ta sözlüğü döngüye sokmanın en iyi yolu 

Bir sözlük anahtar değerleri üzerinde yineleme yapmanın birden fazla yolu olsa da, basit foreach döngüsünü kullanmayı tercih ediyoruz 

Ve yalnızca C# sözlük Anahtarlarını veya Değerlerini döngüye sokmak istiyorsanız, tüm sözlüğü yinelemek yerine `dictionary.Keys` veya `dictionary.Values` adresini kullanın 







