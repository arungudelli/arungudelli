+++
title="How to convert string to enum in C#"
summary="To Convert string to enum in C# use Enum.TryParse and Enum.Parse methods"
keywords="['string to enum in C#','Convert string to enum in C#']"
type='post'
date='2020-01-02T18:08:51+0000'
lastmod='2020-01-02T18:08:51+0000'
draft='false'
authors=['admin']
[image]
caption='Convert int to enum in C#'
focal_point=''
preview_only=false
+++

To Convert string to enum in C# use the below methods.

1. Enum.TryParse method.
2. Enum.Parse method.

Converting string to enum is very helpful incase, if we get enum from an UI client over an API endpoint.

We will go through an example to understand it further.
{{%toc%}}

## **Convert string to enum in C# using Enum.Parse**

We will create an enum for Days in our C# application, which has predefined values like Sunday,Monday,Tuesday etc.

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

Now we declare a string variable and convert it to Enum.

```
var myDay = "Monday";
Days myDayEnum = (Days)Enum.Parse(typeof(Days), myDay);

```

Now `myDayEnum` contains the value of Monday.

What if the string does not contain value of Days Enum?

```
var myDay = "SomeDay";
Days myDayEnum = (Days)Enum.Parse(typeof(Days), myDay);
```

The above code throws `Requested value was not found.` exception.

`Requested value was not found.` exception is of type `System.ArgumentException`. So we will add a try catch block to handle the exception as shown below.

```
try{
   var myDay = "SomeDay";
   Days myDayEnum = (Days)Enum.Parse(typeof(Days), myDay);
}
catch(ArgumentException ex){
    //log the Requested value was not found error 
    //and throw the exception
    throw;
}
```

## **Convert case insensitive string to enum in C#** 

If we want convert a case insensitive string to enum in C#. 

`Enum.Parse` has an overloaded method which accepts an extra parameter `ignoreCase` through which we can convert case insensitive string to enum.

```
try{
  var myDayinsensitive = "MONDAY";
  Days myDayEnum = 
      (Days)Enum.Parse(typeof(Days), myDayinsensitive,true);
}
catch(ArgumentException ex){
    //log the Requested value was not found error 
    //and throw the exception
    throw;
}
```

## **Convert string to enum in C# using Enum.TryParse**

Enum.TryParse method convert a string to an enum in C#.

If the string conversion is successfull the method returns true or else false.
The `out` parameter contains the converted enum object.

Enum.TryParse introduced in .net framework 4.

```
var myDay = "Monday";
Days myDayEnum;
var isSuccess=Enum.TryParse(myDay, out myDayEnum);
if(isSuccess){
    //string converted to Enum
}else{
   //Cannot convert string to Enum
}
```

To convert case insensitive string to enum, `Enum.TryParse` has an overloaded method.

```
var myDayignoreCase = "MONDAY";
Days myDayEnum;
var isSuccess=Enum.TryParse(myDayignoreCase,true, out myDayEnum);
if(isSuccess){
    //string converted to Enum
}else{
   //Cannot convert string to Enum
}
```


