+++
title="JavaScript Substring Vs Substr Vs Slice Differences With Examples"
summary="JavaScript substring(),substr(),slice() are predefined methods in string prototype used to get the substring from a string."
keywords="javascript subtring(),javascript substr(),javascript slice(),javascript substr vs slice vs substring,javascript"
type='post'
date='2019-11-16T20:51:38+0000'
lastmod='2019-11-16T20:51:38+0000'
draft='false'
authors=['admin']
[image]
caption='JavaScript Substring Vs Substr Vs Slice Differences With Examples'
focal_point=''
preview_only=false
+++








JavaScript&nbsp;<em>substring()</em>,<em>substr()</em>,<em>slice()</em>&nbsp;are predefined methods in string prototype used to get the substring from a string.In this tutorial, we will understand each one of them &amp; differences between them using examples.

<ol><li><a href="#step1-h2">JavaScript substring()</a><ul><li><a href="#step11-h3">JavaScript substring() syntax</a></li><li><a href="#step12-h3">JavaScript substring() Description</a></li><li><a href="#step13-h3">JavaScript substring() Examples</a></li><li><a href="#step14-h3">JavaScript substring() Browser Support</a></li></ul></li><li><a href="#step-211">JavaScript Substring After a Character:</a></li><li><a href="#step-212">JavaScript Substring before a Character</a></li><li><a href="#step2-h2">JavaScript substr()</a><ul><li><a href="#step21-h3">JavaScript substr() Syntax</a></li><li><a href="#step21-h3">JavaScript substr() Syntax</a></li><li><a href="#step23-h3">JavaScript substr() Examples</a></li><li><a href="#step24-h3">JavaScript substr() Browser Support</a></li></ul></li><li><a href="#step311">JavaScript Substring from End</a></li><li><a href="#step3-h2">JavaScript slice()</a><ul><li><a href="#step31-h3">JavaScript slice() Syntax</a></li><li><a href="#step32-h3">JavaScript slice() Description</a></li><li><a href="#step33-h3">JavaScript slice() Examples</a></li><li><a href="#step34-h3">JavaScript slice() method with negative indexes</a></li><li><a href="#step35-h3">JavaScript slice() Browser Support</a></li></ul></li><li><a href="#step4-h2">Differences between substring,slice and substr methods</a><ul><li><a href="#step41">Similarities between JavaScript substring() and slice() methods</a></li><li><a href="#step42">Javascript substring() vs slice() differences</a></li><li><a href="#step43">Why we have two methods substring() and slice() in JavaScript?</a></li><li><a href="#step44">Javascript substring() vs substr() differences</a></li></ul></li></ol>

## JavaScript substring():

<em>JavaScript substring()</em> method returns part of the string between <em>startIndex</em> &amp; <em>endIndex</em>&nbsp;(excluding endIndex character) or upto the end of the string if <em>endIndex</em> not provided

## JavaScript substring() syntax:

<em>JavaScript substring()</em> method takes two parameters start index and end index. And second parameter end index is optional.

And the return value is a new string between start, end indexes.

<pre>string.substring(startIndex[, endIndex])</pre>

## JavaScript substring() Description:

<ol><li>If we are not passing any parameters the method will return the same given string</li><li>If <em>endIndex</em> is not passed then it will return the substring starting from start index to end of the string.</li><li>If <em>startIndex</em> and endIndex are same then JavaScript&nbsp;<em>substring() </em>method&nbsp;return an empty string</li><li>If the <em>startIndex</em> or <em>endIndex</em> less than 0 (negative value) they are treated as 0.</li><li>If the startIndex or endIndex greater than string.length <em>substring()</em> method treats them as <em>string.length</em></li><li>If <em>startIndex</em> or <em>endIndex</em> is <em>NaN</em> they treated as 0.</li></ol>

Go through the below examples to understand it further.

## Javascript substring() Examples:

We will take a string variable and see how JavaScript&nbsp;<em>substring()</em> method works.

<pre>var string = "substring method example";

//No parameters passed
var substring = string.substring();
console.log(substring);
//"substring method example"

//Both paramters passed
var substring = string.substring(0,9); 
console.log(substring);
//substring

//endIndex is Missed
var substring = string.substring(0);
console.log(substring);
//substring method example

//StartIndex and EndIndex are equal
var substring = string.substring(0,0);
//""

//StartIndex is greater than endIndex
var substring = string.substring(9,0);
//Nothing but string.substring(0,9);
//substring

//StartIndex is negative value less than 0
var substring = string.substring(-5,9); 
//Nothing but string.substring(0,9)
//substring

//EndIndex is negative value
var substring = string.substring(0,-9); 
//Nothing but string.substring(0,0);&nbsp;
//""

var substring = string.substring(9,-19);
//Nothing but string.substring(9,0) =&gt; string.substring(0,9)
//Substring

//String Length
var length = string.length;
//22

//StartIndex greater than string length
var substring = string.substring(string.length+1,9);
// Nothing But string.substring(string.length,9) =&gt; string.substring(9,string.length)
//" method usage"&nbsp;

//endIndex greater than string length
var substring = string.substring(9,string.length+1);
//Nothing But string.substring(9,string.length)
//" method usage"&nbsp;
</pre>

## JavaScript substring() Browser Support:

<em>JavaScript substring()</em> method works in almost all browsers starting from IE 6+, Microsoft Edge, Chrome, Mozilla, Opera, Safari. And also Mobile browsers like Android webView, Chrome for Android, Edge mobile, Firefox for Android, Opera Android, iOS Safari and Samsung Internet.

## JavaScript Substring After a Character:

To get the substring after a character in Javascript we can use IndexOf() method and substring() method.

Take a sample string

<pre>var testString = "JavaScript-Substring";</pre>

To get the substring after a character (For example dash(-)), we need to identify the index of character and pass it to the substring method as shown below.

<pre>var substring= testString.substring(testString.indexOf('-') + 1);
//substring</pre>

## JavaScript Substring before a Character:

To get the substring before a character in Javascript we can use IndexOf() method and substring() or substr() method.

For example in the below string to get substring before the character(say dash) i.e., Javascript

<pre>var testString = "JavaScript-Substring";</pre>

We can use the following methods

<pre>var substring= testString.substring(0,testString.indexOf('-'));
var substring= testString.substr(0,testString.indexOf('-')); 
//Javascript</pre>

{{< figure src="javascript-slice-substr-substring.png" title="JavaScript slice() vs substr() vs substring()" alt="JavaScript slice() vs substr() vs substring()" >}}

## JavaScript substr():

<em>JavaScript substr()</em> method returns part of the string starting from an index and number of characters after the start index.

## JavaScript substr() Syntax:

<em>substr()</em> method takes two parameters

<ul><li><em>startIndex</em>: Index of the first character</li><li><em>length</em>: number of characters to include in substring after the startIndex and it is optional</li></ul>

And the return value is a new string as per the given parameters.

<pre>string.substr(startIndex[, length])</pre>

## JavaScript substr() Description:

<ul><li>If you are not passing any parameters return the same string</li><li>If the length parameter not passed,&nbsp;<em>substr()</em> will return string starting from index to end of the string</li><li>If the start index is less than 0 (negative value) it will be treated as (string.length-start) i.e., if the string length is 10 and if the index is -4. The start index is 10-4=6.</li><li>If start index or length is NaN,&nbsp;<em>substr()</em> method treats them as 0.</li><li>If the length is a negative number it is treated as 0</li><li>If the length is undefined,&nbsp;<em>substr()</em> method return up to end of the string (as if length parameter not passed).</li></ul>

## JavaScript substr() Examples:

We will take a sample string and see how <em>substr()</em> works

<pre>var string= "substr method usage";

//No Parameters passed
string.substr()
//"substr method usage"

//Two parametes passed start index and lenght
string.substr(0,6)
//"substr"

//Only start index passed
string.substr(7)
//"method usage"

//Start index is negative value
string.substr(-5)
//Nothing but string.substr(string.length-5)
//"usage"

//Start index is negative value and length passed
string.substr(-12,6)
//Nothing but string.substr(string.length-12,6)
//"method"

//Length is negative value
string.substr(2,-5)
//=&gt; string.substr(2,0)
//""

//Start index is NaN and length not passed
string.substr("test")
//=&gt;string.substr(0) NaN
//"substr method usage"

//Start index is NaN and length passed
string.substr("test",6)
//=&gt;string.substr(0,6)
//"substr"

//Length is NaN
//=&gt;string.substr()
string.substr(5,"test")
//=&gt;string.substr(5,0)
//""

</pre>

## JavaScript substr() Browser Support:

Like <em>substring()</em> method, even <em>substr()</em> method supports all browsers&nbsp;IE 6+, Microsoft Edge, Chrome, Mozilla, Opera, Safari. And also Mobile browsers like Android webView, Chrome for Android, Edge mobile, Firefox for Android, Opera Android, iOS Safari and Samsung Internet.

## JavaScript Substring From End:

To get the substring from the end of the string, we can use substr() method by passing the start index as a negative value as shown below

<pre>var str = "substring From End"
// To get "End" 
str.substr(-3);
//End</pre>

## JavaScript slice():

slice() method is similar to substring() method, returns partial string between start index &amp; end index (excluding end index character) or up to the end of the string if end index not provided

## JavaScript slice() Syntax:

<ul><li><em>slice()</em> methods takes two parameters startIndex,endIndex</li><li>endIndex is optional</li><li>returns a new string without changing the existing string.</li></ul>

<pre>string.slice(startIndex[, endIndex])</pre>

## JavaScript slice() Description:

<ul><li>If both parameters not passed then <em>slice()</em> method will return the same string</li><li>If end index is not passed it extracts the string between start index and end of the string.</li><li>If the start index or end index is a negative value, it is treated as (string.length-index). i.e., if the index is -5 its behaves as string.lenth-5.So if you want to read string from reverse we can use slice() method. See the below example and graphical representation.</li><li>If start index and end indexes are same then <em>slice()</em> method will return an empty string.</li><li>If start index is greater than end index, then an&nbsp;empty string will return.</li><li>If start index is NaN or undefined it will be treated as 0.</li><li>If end index is NaN an empty string will return.</li><li>If end index is undefined then <em>slice()</em> method will return partial string between start index and end of the string.</li></ul>

Go through the below examples to understand it further.

## JavaScript slice() Examples:

We will take an example string and see how it works

<pre>var string = "slice method usage";

//without parameters 
string.slice();
//"slice method usage"

//Only Start Index Passed
string.slice(0);
//"slice method usage"

//If Both start and end passed
string.slice(0,5);
//"slice"

//If Start index is negative
string.slice(-5);
//=&gt;string.slice(string.lenght-5)
"usage"

//IfEnd index is negative
string.slice(0,-5);
//=&gt;string.slice(0,string.length-5)
//"slice method "

//If Start index is NaN
string.slice("a",5);
//=&gt;string.slice(0,5)
//"slice"

//If end index is NaN
string.slice(0,"a");
//""

//If start index is greater than end index
string.slice(5,0);
//""

//If start index and end index are equal
string.slice(5,5);
//""

//If the start index is undefined
string.slice(undefined)
//=&gt;string.slice(0)
//"slice method usage"

If the end index is undefined
string.slice(0,undefined)
//"slice method usage"


</pre>

## JavaScript slice() method with negative indexes:

Use the negative indexes if you want parse string in reverse order. See the below graphical representation of slice method.

{{< figure src="javascript-Slice.png" title="JavaScript Slice() Method" alt="JavaScript Slice() Method" >}}

Negative indexes start from -1 and normal index starts from 0.

Always remember that start index should be less than end index.



<pre>string.slice(-5) //returns slice
string.slice(0) //return slice

</pre>

Now in both cases, we ignored end index so slice() method returns the entire string starting from start index.

<pre>string.slice(-5,-3) //returns "sli"</pre>

now both indexes are false. and start index is less than end index. so it returned “sli” (excluding end index character)

<pre>string.slice(-5,-1) //returns "slic"
string.slice(-1) //returns "e"</pre>

string.slice(-1) prints only “e” because -1 is the end of the string.

## JavaScript slice() Browser Support:

<em>slice()</em> method works in almost all browsers starting from IE 6+, Microsoft Edge, Chrome, Mozilla, Opera, Safari. And also Mobile browsers like Android webView, Chrome for Android, Edge mobile, Firefox for Android, Opera Android, iOS Safari and Samsung Internet.

## Differences between substring,slice and substr methods:

There is no difference between string.substring() and string.slice() methods, both works in the same way but behavior might change depending upon the parameters we pass.

## Similarities between JavaScript substring() and slice() methods:

<ol><li>Both accepts two parameters startIndex and endIndex. And the behavior is same when both parameters are positive and startIndex less than endIndex.</li><li>Both methods do not change the original string.</li><li>In both,&nbsp;<em>substring()</em> and <em>slice()</em> methods endIndex is an optional parameter.</li><li>If endIndex is not passed both returns the characters up to the end of the string.</li><li>If startIndex or endIndex is greater than the string length they treated as <em>string.length</em>.</li><li>If startIndex and endIndex are equal both <em>substring()</em> and <em>slice()</em> methods returns an empty string.</li></ol>

## Javascript substring() vs slice() differences:

<ol><li>If statIndex is greater than endIndex (startIndex &gt; endIndex) then <em>substring()</em> method will swap those parameters where as <em>slice()</em> method will return an empty string (No swapping).</li><li>If startIndex or endIndex is a negative value <em>substring()</em> method treats them as 0 whereas <em>slice()</em> method treats them as (string.length-index).Basically, it traverses string from the reverse as explained in above examples.</li></ol>

## Why we have two different methods slice() and substring() in JavaScript?

We might think why we need two different methods slice() and substring() as their behaviour is same. It is all about negative indexes.

The initial JavaScript created in Netscape 2.0 has only <em>substring()</em> method. If the parameters are negative they treated as 0. And the order of parameters does not matter. if start index is greater than end index it will swap those and performs the operation.



And in the next version of JavaScript 1.2 introduced in Netscape 4.0, they wanted to support negative indexes to traverse the string from the reverse.

And it is not a good idea to change the existing substring() function as it might break compatibility with existing scripts that expected negative indexes to treated as zero(0)

So they created a new function to handle negative indexes and called it as <em>slice()</em>

Generally, if you think of bread(food) we can slice it from start or from the end. The way we like. In the same way slice the string from start or end depending upon your requirement.

## Javascript substring() vs substr() differences:

In my opinion we should not compare <em>substring()</em>(or <em>slice()</em>) methods with <em>substr()</em> method. Both are useful depending upon our requirement

<ol><li>The second parameter in <em>substr()</em> method is the length of the string to return from start index.</li><li>Whereas the second parameter in <em>substring()</em>&nbsp;or&nbsp;<em>slice() </em>is, end index.</li></ol>

This is the only main difference between substring() or substr() methods.

&nbsp;

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







