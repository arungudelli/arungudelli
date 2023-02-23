---
title: " 3 cara berbeda untuk mengulang daftar C#"
description: "Berbagai cara untuk mengulang daftar C# dengan contoh"
lead: ""
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs

---

`List<T>` adalah salah satu struktur data yang paling sering digunakan dalam bahasa C#. 

Melakukan perulangan pada list `List<T>` dan melakukan beberapa operasi pada elemen-elemen list adalah hal yang sangat umum dilakukan dalam proyek-proyek kita sehari-hari.

Untuk mengulang sebuah list di C# kita bisa menggunakan 3 cara yang berbeda.

1. Menggunakan pernyataan C# `foreach`.
2. Menggunakan metode C# `List.ForEach`.
3. Menggunakan perulangan for sederhana.

Mari kita lihat sebuah contoh untuk memahaminya lebih lanjut. 

Pertama kita akan membuat daftar C# sederhana.

```csharp
List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};

```

Sekarang kita akan melihat berbagai cara untuk mengulang daftar C#.

## Menggunakan pernyataan C# `foreach` 

Menggunakan pernyataan `foreach` untuk mengulang daftar C# adalah metode yang banyak digunakan.

Dan selanjutnya kita dapat melakukan operasi apapun pada elemen list.

Pada contoh di bawah ini saya telah membuat daftar string.

Kemudian mengulang daftar tersebut menggunakan `foreach` dan selanjutnya mencetak elemen daftar pada konsol.

```csharp
///Method to Loop C# list
void loopList()
{
   List<string> languages = new List<string>() { "C#","Asp.Net","DotNet Core"};
   
   foreach (string lang in languages)
   {
        Console.WriteLine(lang);
   }
}
```

Sekarang kita akan membuat daftar objek dan mengulangnya menggunakan pernyataan `foreach`.

Mendefinisikan kelas `Person` dan membuat daftar dengan dua elemen orang.

```csharp

List<Person> persons = new List<Person>() 
{ 
      new Person() { Id = 1, Name="Arun" },
      new Person() { Id = 2, Name="Kumar"} 
};
```

Sekarang kita dapat menggunakan pernyataan `foreach` untuk mengulang daftar objek.

```csharp
void loopListOfObjects(List<Persons> persons){
 foreach(var person in persons)
    {
        Console.WriteLine(person.Name);            
        Console.WriteLine(person.Id);
    }
}
```

## Menggunakan metode C# `List.ForEach` 

`List<T>.ForEach` melakukan metode `action` yang diberikan pada setiap elemen List.

Metode ini menerima `Action<T>` parameter delegasi. 

Contoh berikut ini mengulang melalui daftar objek menggunakan `Action<T>` delegate.

```csharp
persons.ForEach((person) =>
    {
        Console.WriteLine(person.Name);
        Console.WriteLine(person.Id);
    });
```

## Menggunakan pernyataan `for` 

Kita dapat menggunakan pernyataan lama `for` untuk mengulang daftar C#, jika Anda ingin melakukan tindakan apa pun pada elemen daftar berdasarkan indeks. 

Jika tidak, gunakan `foreach` atau `List<T>.ForEach()` metode.

```csharp
for(var i=0;i<persons.Count;i++)
    {
        Console.WriteLine(persons[i].Name);
        Console.WriteLine(persons[i].Id);
    }
```

## Ringkasan

Pada tutorial ini kita belajar bagaimana cara mengulang sebuah list di C# menggunakan pernyataan `foreach`, `List<T.ForEach` dan `for`.










