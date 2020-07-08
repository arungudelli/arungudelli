+++
title="How to check if a string is a number in C#"
summary="Steps to check if a string is a number in c# 1.Declare an integer variable. 2.Pass string to int.TryParse() or double.TryParse() methods with out variable. 3.If the string is a number TryParse method will return true. And assigns value to the declared integer value."
keywords=["check if a string is number in C#"
]
type='post'
date='2020-07-01T19:08:51+0000'
lastmod='2020-07-01T19:08:51+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Steps to check if a string is a number in C#

1. Declare an integer variable.
2. Pass string to int.TryParse() or double.TryParse() methods with out variable.
3. If the string is a number TryParse method will return true. And assigns value to the declared integer out value.

{{%toc%}}

## Check if a string is a Number or not in C# 

For example we have a string variable "123" and if you want to check whether it is numeric use the below C# code.

```
var stringNumber = "123";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is true and numericValue=123

var stringNumber = "123P";
int numericValue;
bool isNumber = int.TryParse(stringNumber, out numericValue);

//isNumber is false and numericValue=0 default value

```

From C# 7 onwards we can declare [out](https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/) variable in TryParse Method itself.

```
bool isNumber = int.TryParse(stringNumber, out int numericValue);

```

The problem with the above int.TryParse method is it cannot check for negative string number values.

## Checking for negative string number in C# 

To Check for negative string number values we can use C# double.TryParse() method.

```
var negativeString = "-123";
double number;
if(double.TryParse(negativeString,out number)){
   if (number > 0){

   }else{
       //negative number 
   }   
}
```

## Best way to check if string is number in C# 

Always use double.TryParse() method to check if a string is number, because it can validate both positive and negative numbers.