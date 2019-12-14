+++
title="Javascript String Contains: Check If A String Contains A Substring"
summary="To check if a Javascript String Contains a substring or not, we can use 7 different Javascript methods as listed in below table."
keywords="check if a string contains a substring in javascript (in es6),substring check javascript (in es5 and before),substring check javascript by using javascript search method,substring check javascript by using javascript match method,substring check javascript using regular expression,substring check in javascript using lodash js,substring check javascript using underscore js,best way of substring check javascript,javascript"
type='post'
date='2019-11-12T18:02:52+0000'
lastmod='2019-11-12T18:02:52+0000'
draft='false'
authors=['admin']
[image]
caption='Javascript String Contains: Check If A String Contains A Substring'
focal_point=''
preview_only=false
+++

To check if a Javascript String Contains a substring or not, we can use 7 different Javascript methods as listed in below table.

<div class='table-responsive'><table class='table'><thead><tr class="row-1 odd"><th class="column-1">Javascript string contains Method</th><th class="column-2">Javascript string contains example</th><th class="column-3">Result</th></tr></thead><tbody class="row-hover"><tr class="row-2 even"><td class="column-1">Javascript includes</td><td class="column-2">"Javascript String Contains".includes("String")</td><td class="column-3">true</td></tr><tr class="row-3 odd"><td class="column-1">Javascript indexOf</td><td class="column-2">"Javascript String Contains".indexOf("substring")!== -1;</td><td class="column-3">false</td></tr><tr class="row-4 even"><td class="column-1">Javscript search</td><td class="column-2">"Javascript String Contains".search("substring")!== -1;</td><td class="column-3">false</td></tr><tr class="row-5 odd"><td class="column-1">Javascript match</td><td class="column-2">"Javascript String Contains".match("Contains")!=null<br></td><td class="column-3">true</td></tr><tr class="row-6 even"><td class="column-1">Javascript Regular expression</td><td class="column-2">/Contains/.test("Javascript String Contains")</td><td class="column-3">true</td></tr><tr class="row-7 odd"><td class="column-1">Lodash includes</td><td class="column-2">_.includes('lodash substring',&nbsp;'lodash');</td><td class="column-3">true</td></tr><tr class="row-8 even"><td class="column-1">Underscore</td><td class="column-2">includes("underscore substring","underscore")</td><td class="column-3">true</td></tr></tbody></table></div>

To check for case-insensitive Javascript string contains or Javascript string contains after some index, go through the complete tutorial.

{{%toc%}}

## 1.JavaScript string contains substring check using includes method (in ES6):

If you are using latest versions of Javascript like ES6 you can use <em>include</em> method to check if a string contains a substring or not as shown below.

We will take an example and understand it further.

<pre>var substringtocheck = "includes";
var actualstring="ES6 contains includes method";
var isContains = actualstring.includes(substringtocheck);
//returns true.</pre>

<em>includes</em> method is case sensitive, so the below substring check returns false

<pre>var substringtocheck = "Includes";
var actualstring="ES6 contains includes method";
var isContains = actualstring.includes(substringtocheck);
// returns false</pre>

Javascript string <em>includes</em> method accepts two parameters

<ol><li>substring to check</li><li>search position</li></ol>

The second parameter search position is optional and the default value is 0.

If you want to check whether a string contains a substring only after a certain position you can pass the search position as a parameter as shown in the below examples.

<pre>var substringtocheck = "ES6";
var actualstring="ES6 contains includes method";
var isContains = actualstring.includes(substringtocheck,1);
//returns false. As we are checking for ES6 substring after position 1.</pre>

includes method is very easy to use and comes with additional options like search position.

In older versions of Javascript, we can add a polyfill for include method

<pre>if (!String.prototype.includes) {

Object.defineProperty(String.prototype, 'includes', {
  value: function(substring, searchposition) {
     if (typeof searchposition!== 'number') {
       searchposition= 0
     }
     if (searchposition+ substring.length &gt; this.length) {
       return false
     } else {
       return this.indexOf(substring, searchposition) !== -1
     }
  }
})
}</pre>

## 2.check if a string contains a substring in javascript (in ES5 and before):

In ES5 and before versions of Javascript we can use <em>indexOf</em> method to check if a string contains a substring or not.

Go through the following code example to understand it further.

<pre>var actualstring = "In ES5 use IndexOf method",
var substringToCheck = "IndexOf";
var isContains=actualstring.indexOf(substringToCheck) !== -1;
//isContains true</pre>

The <em>indexOf</em> method will return the substring position if it found, otherwise returns -1.

And <em>indexOf</em> method is case sensitive,accepts two parameter similar to includes method.

<pre>var actualstring = "In ES5 use IndexOf method",
var substringToCheck = "indexOf";
var isContains=actualstring.indexOf(substringToCheck) !== -1;
//isContains false as
var isContainsAfterPosition = actualstring.indexOf("In",2) !== -1;
//false.

</pre>

We can simply add pollyfil method for includes as it uses indexOf method internally.

## 3.Javascript string contains substring check using search method:

Javascript string prototype contains <em>search</em> method which accepts regular expression as parameter.

We can use <em>search</em> method to check if a string contains a substring or not as shown below.

<pre>var actualstring = "Javascript search method",
var substringToCheck = "search";
var isContains=actualstring.search("search") !== -1;
//isContains true

</pre>

The search method in JavaScript will return substring position if found, otherwise -1.

## 4.check if a string contains a substring or not by using Javascript match method:

To check if a string contains substring or not, use the Javascript <em>match</em> method.

Javascript match method accepts a regular expression as a parameter and if the string contains the given substring it will return an object with details of index, substring, input, and groups.

If the string does not contain the substring then it will return null.

We will take an example to understand it.

<pre>var actualstring = "Javascript match method",
var substringToCheck = "match";
actualstring.match("match");
//["match", index: 11, input: "Javascript match method", groups: undefined]

actualstring.match("javascript");
//null
</pre>

## 5. Javascript string contains a substring using Regular Expressions:

Using regular expression <em>test</em> method, we can verify if a string contains a substring or not.

We have to create a regular expression for the substring and then test it using the target string.

<pre>var actualstring = "RegExp test method";
var regexp = /test/;
regexp.test(actualstring);
//returns true

/RegExp/.test(actualstring);
//returns true</pre>

We have to pass our substring as regular expression only (i.e., without quotes) as shown above.

The regular expression test method in javascript will return true or false only.

We cannot get the index of a substring with this method.

{{< figure src="check-if-a-string-contains-substring-in-Javascript.png" title="check if a string contains substring in Javascript" alt="check if a string contains substring in Javascript" >}}

## 6. Javascript String Contains Case-insensitive check

To check for case-insensitive Javascript string contains, use the below methods.

The simplest way is to convert the entire string to either to lowercase or uppercase and use the javascript indexOf, includes methods as shown below.

<pre>var actualstring = "javascript string contains case-insensitive";
var targetstring = "Contains";

if(actualstring.toLowerCase().includes(targetstring.toLowerCase())
{
 //String contains
}

if(actualstring.actualstring.indexOf(targetstring.toLowerCase()) !== -1)
{
 //String contains
}

if(actualstring.toUpperCase().includes(targetstring.toUpperCase())
{ 
 //String contains 
} 

if(actualstring.toUpperCase.indexOf(targetstring.toUpperCase()) !== -1)
{
 //String contains 
}

</pre>

To check for case insensitive string contains, use the regular expressions. Add suffix “i” after the string regular expression as shown.

<pre>var actualstring = "Javascript Regular Exp";
var regexp = "javascript";
/regexp/i.test(actualstring);
//returns true</pre>

Javascript search method accepts regular expressions, we can do case insensitive string contains check as shown below.

<pre>var actualstring = "Javascript search method";
var isContains=actualstring.search("javascript") !== -1;
// false
actualstring.search(/javascript/i) !== -1;
//true</pre>

And also we can use Javascript match method to do case insensitive substring check&nbsp; as it accepts regular expressions

<pre>actualstring.match(/javascript/i)
["Javascript", index: 0, input: "Javascript match method", groups: undefined]

if(!actualstring.match(/javascript/i)){
//Found
}</pre>

Or we can use third-party libraries like lodash js and underscore js to check if a string contains a substring or not in javascript.

These libraries contain so many javascript utility methods that can be used in our daily projects.

And lodash and underscore js libraries are well documented and well tested. So we can use them without any worries

## 7.check if a string contains a substring in javascript using Lodash js:

lodash library contains <em>._includes()</em> method which is used to check if a string contains another substring or not in javascript.

This method will return true if match found otherwise it will return false

<pre>_<span class="delimiter method">.</span><span class="name">includes</span>(<span class="string">'lodash substring'</span><span class="delimiter">,</span>&nbsp;<span class="string">'lodash'</span>);
//returns true</pre>

## 8.check if a string contains a substring in javascript using Underscore js:

Similary underscore js contains <em>includes()</em> method and we can pass substring and actual string as parameters, if match found it will return true otherwise false

Syntax of includes method is <em>include(string, substring) </em>

<pre>includes("underscore substring","underscore")
//returns true.</pre>

## 9.Best way to check if a string contains a substring or not in javascript:

<ol><li>Using regular expressions to check a simple substring is not advisable due to performence related issues.</li><li>lodash and underscore methods requires to load external javascript files.</li><li>If speed matters use the simple indexOf method in javascript to check whether a string contains a substring.</li></ol>

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







