+++
title="How To Check If A String Is Empty/Null/Undefined In JavaScript"
summary="To check if a string is null or empty or undefined use the following code snippet if(!emptyString){ // String is empty }"
keywords="js empty string,js null string,undefined string,string empty javascript,check if a string is empty in javascript,javascript"
type='post'
date='2019-11-17T18:02:33+0000'
lastmod='2019-11-17T18:02:33+0000'
draft='false'
authors=['admin']
[image]
caption='How To Check If A String Is Empty/Null/Undefined In JavaScript'
focal_point=''
preview_only=false
+++


To check if a string is empty or null or undefined in Javascript use the following js code snippet.

<pre>var emptyString;
if(!emptyString){
 // String is empty
}</pre>

In JavaScript, if the string is empty or null or undefined IF condition returns false.

<pre>var undefinedString;
if(!undefinedString){
 console.log("string is undefined");
}

var emptyString="";
if(!emptyString){
 console.log("string is empty");
}

var nullString=null;
if(!nullString){
 console.log("string is null");
}

</pre>

{{< figure src="check-if-string-is-empty-in-JavaScript.png" title="check if string is empty in JavaScript" alt="check if string is empty in JavaScript" >}}

&nbsp;

If the string is not undefined or null and if you want to check for empty string in Javascript we can use the length property of the string prototype as shown below.

<pre>var emptyString="";
if(emptyString &amp;&amp; emptyString.length==0){
  console.log("string is empty");
}

</pre>

Or you can directly check for the empty string with javascript Comparison operator “===” as shown below.

<pre>if(emptyString===""){
 console.log("string is empty");
}</pre>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







