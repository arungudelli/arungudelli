+++
title="How to convert byte array to a hexadecimal string in C#, and vice versa?"
summary="To convert byte array to hexadecimal string in C# use the following methods.1. Using C# 5 `Convert.ToHexString()` method 2. Using `C# StringBuilder` and `AppendFormat` 3. Using `C# BitConverter.ToString()` method"
keywords=["convert byte array to hexadecimal string in C#,convert hexadecimal string to byte array in c#"]
type='post'
date='2020-01-06T18:08:51+0000'
lastmod='2022-08-03T00:00:00+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

To convert byte array to hexadecimal string in C# use the following methods.

1. Using C# 5 `Convert.ToHexString()` method
2. Using `C# StringBuilder` and `AppendFormat`
3. Using `C# BitConverter.ToString()` method

## Using C# 5 `Convert.ToHexString()` method

If you are using C# 5 version you can make use of `Convert.ToHexString()` method to convert byte array to hexadecimal string.

```
string result = Convert.ToHexString(bytesToConvert);

```

This is the fastest way to convert a byte array to hexadecimal string in C# and also it's very clean and simple method.

If you are using older versions of C# .Net use the below methods.

## Using `C# StringBuilder` and `AppendFormat`

We can loop through the byte array and append it to a string builder to convert byte array to hexadecimal string as shown below. 

```
public static string ByteArrayToHexadecimalString(byte[] byteArray)
{
  StringBuilder hexadecimalString = new StringBuilder(byteArray.Length * 2);
  foreach (byte b in byteArray){
     hexadecimalString.AppendFormat("{0:x2}", b);
  }
  return hexadecimalString.ToString();
}
```

## Using `C# BitConverter.ToString()` method

Another way is to use `C# BitConverter.ToString()` method, through which we can directly convert C# byte array to hexadecimal string. 

```
public static string ByteArrayToHexadecimalString(byte[] byteArray)
{
  return BitConverter.ToString(byteArray).Replace("-","");
}
```

## Convert Hexadecimal string to byte array in C#

Similarly to convert hexadecimal string to byte array we can use `Convert.FromHexString()` method in C# 5. 

```
var result = Convert.FromHexString(hexadecimalstring);
```

In the older versions of C# .Net use the below method.

```
public static byte[] HexadecimalStringToByteArray(String hexadecimalString)
{
  int length = hexadecimalString.Length;
  byte[] byteArray = new byte[length / 2];
  for (int i = 0; i < length; i += 2){
    byteArray[i / 2] = Convert.ToByte(hexadecimalString.Substring(i, 2), 16);
  }
  return byteArray;
}
```