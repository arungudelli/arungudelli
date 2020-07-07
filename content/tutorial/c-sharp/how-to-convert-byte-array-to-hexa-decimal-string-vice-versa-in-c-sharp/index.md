+++
title="How to convert byte array to a hexadecimal string in C#, and vice versa?"
summary="This post contains two simple methods to convert byte array to hexadecimal string in C# and vice versa."
keywords=["['convert byte array to hexadecimal string in C#','convert hexa decimal string to byte array in c#']"
]
type='post'
date='2020-01-06T18:08:51+0000'
lastmod='2020-01-06T18:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

This post contains two simple methods to convert byte array to hexadecimal string in C# and vice versa.

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

or we can use BitConverter Class

```
public static string ByteArrayToHexadecimalString(byte[] byteArray)
{
  return BitConverter.ToString(byteArray).Replace("-","");
}
```

To convert hexa decimal string to byte array in c# use the below method

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