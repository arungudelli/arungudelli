+++
title="8 cara untuk mengulang/mengiterasi pasangan nilai kunci kamus di C#"
summary="Menggunakan loop foreach C# adalah cara paling sederhana dan mudah untuk mengiterasi nilai kunci kamus di C#."
keywords=["perulangan kamus di C#, iterasi kamus c#, perulangan kunci kamus, perulangan nilai kamus"]
type='post'
date='2022-05-27T00:00:00+0000'
lastmod='2022-05-27T00:00:00+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Untuk mengiterasi pasangan nilai kunci kamus dalam C# gunakan metode berikut ini

1. Menggunakan C# `foreach` loop
2. Mengiterasi kunci kamus C# saja
3. Hanya melakukan iterasi terhadap nilai kamus C# saja
4. Menggunakan `Deconstruct` dari `KeyValuePair<TKey,TValue>` di C# 7
5. Menggunakan `Deconstruct` dan `discards` di C# 7 
6. `Deconstruct` dari pasangan nilai kunci di versi C# yang lebih lama
7. Menggunakan fungsi `dictionary.ElementAt()` dan `for` loop
8. Menggunakan C# `dictionary.AsParallel().ForAll()` 

Mari kita lihat sebuah contoh untuk memahaminya lebih lanjut 

Saya telah membuat contoh kamus menggunakan `C#` for loop

Lihatlah kamus `C#` di bawah ini

```
var dictionaryExample = new Dictionary<string, string>();

for (var i = 1; i <= 5; i++)
{
    dictionaryExample["key" + i] = "value" + i.ToString();
}
```

{{{%toc%}}

## Solusi 1: Menggunakan `C# foreach` loop

Menggunakan `C# foreach` loop adalah cara paling sederhana dan mudah untuk mengiterasi nilai kunci kamus di C#.

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

Variabel `dictionary` dalam loop `foreach` di atas akan memiliki `KeyValuePair<TKey, TValue>` tipe 

Kita dapat dengan mudah mengakses properti `Key` &amp; `Value` dari tipe `KeyValuePair`.

## Solusi 2: Iterasi hanya pada kunci kamus C# saja

Jika anda ingin mengulang hanya kunci kamus saja, gunakan properti C# dictionary `dictionary.Keys`.

```
foreach(var key in dictionaryExample.Keys)
{
    Console.WriteLine("dictionary Key is {0}",key);
}
```

## Solusi 3: Mengiterasi nilai kamus C# saja

Jika Anda ingin mengiterasi hanya Nilai kamus menggunakan properti kamus C# `dictionary.Values`.

```
foreach (var value in dictionaryExample.Values)
{
    Console.WriteLine("dictionary Value is {0}", value);
}
```

## Solusi 4: Menggunakan `Deconstruct()` dari `KeyValuePair<TKey,TValue>` di C# 7

Dekonstruktor diperkenalkan di versi C# 7.0.
 
Dan jika Anda menggunakan Aplikasi .NET Core 2.0+, maka `KeyValuePair<TKey, TValue>` akan memiliki metode `Deconstruct()`.

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

Untuk mengakses pasangan nilai kunci dari dictionary gunakan fungsi `Deconstruct()` dari tipe `KeyValuePair`.

```
foreach (var (key,value) in dictionaryExample)
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);
}
```

## Solusi 5: Menggunakan `Deconstruct` dan `discards` di C# 7 

Dimulai dengan C# 7.0, C# mendukung discard 

Discards adalah variabel placeholder yang sengaja tidak digunakan dalam kode aplikasi 

Seringkali mereka disebut sebagai variabel `_`.

Discards tidak lain adalah variabel yang tidak ditetapkan, mereka tidak memiliki nilai.

Dalam kamus jika Anda ingin mengulang hanya Keys, kita dapat menggunakan variabel discard.

```
foreach (var (key, _) in dictionaryExample)
{
    Console.WriteLine($"dictionary key is {key}");
}
```
Demikian pula jika Anda hanya ingin menggunakan nilai kamus.

```
foreach (var (_, value) in dictionaryExample)
{
    Console.WriteLine($"dictionary value is {value}");
}
```

## Solusi 6: `Deconstruct` pasangan nilai kunci pada versi C# yang lebih lama


Struct KeyValuePair tidak memiliki fungsi `Deconstruct()` di versi C# yang lebih lama (C# 4.7.2 di bawah ini) 

Jadi jika Anda ingin menggunakan `Deconstruct()` untuk mengulang pasangan nilai kunci, ada solusinya 

```
foreach (var (key, value) in dictionaryExample.Select(x => (x.Key, x.Value)))
{
    Console.WriteLine("dictionary key is {0} and value is {1}", key, value);

}
```

Sebagian besar kasus kita tidak akan menggunakan metode ini, tetapi ada baiknya untuk diketahui.

## Solusi 7: Menggunakan fungsi `dictionary.ElementAt()` dan `for` loop

Kita bisa menggunakan loop `for` sederhana untuk mengiterasi pasangan nilai kunci kamus.

Kita bisa mengakses nilai `KeyValuePair` dengan indeks kamus menggunakan fungsi `dictionary.ElementAt()`.

```
for(var i = 0; i < dictionaryExample.Count; i++)
{
    var keyValuePair = dictionaryExample.ElementAt(i);
    Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value);
}
```

Sekali lagi ini bukan cara yang baik untuk mengulang-ulang kamus, karena fungsi `ElementAt()` akan memiliki `O(n)` dan kita memiliki loop `for` di atas sehingga kompleksitas waktu akan menjadi `O(n^2)` 

Dalam kamus besar, hal ini akan memiliki implikasi kinerja.

Jika Anda ingin mendapatkan indeks pasangan nilai kunci Kamus gunakan metode ini 

Saya tidak memikirkan kasus penggunaan dunia nyata di mana indeks kamus akan digunakan 

## Solusi 8: Menggunakan C# `dictionary.AsParallel().ForAll()`

Jika Anda memiliki kamus yang besar, kita dapat menggunakan query Parallel Language Integrated Query (LINQ) dengan menggunakan metode ekstensi `ParallelEnumerable.AsParallel` pada kamus dan mengeksekusi query dengan menggunakan metode `ParallelEnumerable.ForAll`.

Kueri mempartisi sumber ke dalam tugas-tugas yang dieksekusi secara asinkron pada beberapa thread

```
dictionaryExample.AsParallel().ForAll(keyValuePair => 
Console.WriteLine("dictionary key is {0} and value is {1}", keyValuePair.Key, keyValuePair.Value));
```

## Cara terbaik untuk mengulang kamus di C# 

Meskipun kita memiliki beberapa cara untuk mengiterasi nilai kunci kamus, lebih suka menggunakan loop foreach sederhana 

Dan jika anda ingin mengulang hanya kunci atau nilai kamus C# gunakan `dictionary.Keys` atau `dictionary.Values` daripada mengulang seluruh kamus 







