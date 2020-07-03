+++
title="4 Ways To Capitalize The First Letter Of A String In JavaScript"
summary="In Javscript,we can capitalize the first letter of a string in Javascript by using simple Javascript code or regex or ES6 or by overriding string prototype."
keywords="javascript,ecma6,first letter capital in javascript,capitalize the first letter of a string in javascript"
type='post'
date='2019-11-06T18:03:20+0000'
lastmod='2019-11-06T18:03:20+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

We can capitalize the first letter of a string in Javascript by using several methods as listed below

{{%toc%}}

### Capitalize the First Letter of a String using simple Javascript:

To capitalize the first letter of a string use the following JavaScript function. The code takes out the first letter of string &amp; converts it into the capital letter (uppercase letter) using&nbsp;<code>toUpperCase</code> method in JavaScript &amp; then append it to the remaining string&nbsp; (uses <code>substr()</code> or <code>substring()</code> method in JavaScript to exclude the first letter).

Or You can use <code>slice()</code> method in JavaScript to exclude the first letter.

<pre>/*
* This JavaScript function takes string as input parameter
* and capitalizes the first letter
* @parameter : string
*
*/
function capitalizeFirstLetter(string) {
   if(typeof string==undefined) return;
   var firstLetter = string[0] || string.charAt(0);
   return firstLetter  ? firstLetter.toUpperCase() + string.substr(1) : '';
}


function capitalizeFirstLetter(string) {
   if(typeof string==undefined) return;
   var firstLetter = string[0] || string.charAt(0);
   return firstLetter ? firstLetter.toUpperCase() + string.substring(1) : '';
}

function capitalizeFirstLetter(string) {
   if(typeof string==undefined) return;
   var firstLetter = string[0] || string.charAt(0);
   return firstLetter ? firstLetter.toUpperCase() + string.slice(1) : '';
}

/* Usage :
*  var lowercase_string = "this is test string";
*  var firstLetter_capital = capitalizeFirstLetter(lowercase_string);
*  console.log(firstLetter_capital);
*  "This is test string"
*/</pre>

We can get the first letter of a string using <code>string[0]</code> or <code>string.charAt(0)</code>. <code>string.charAt()</code> method is standard function &amp; works in all browsers. The bracket version is a JavaScript and ECMAScript 5 feature. (Does not work in Internet Explorer 7).

That is why I have created one more variable called the first letter and assigning it to <code>string[0]</code> or&nbsp;<code>string.charAt(0)</code> so that it will work in all browsers.

Nowadays almost every browser supports bracket notion of accessing string (IE 8+ and Chrome, Mozilla etc)

<a href="https://www.arungudelli.com/tutorial/javascript/javascript-string-substring-vs-string-substr-vs-string-slice-differences/" target="_blank" rel="noopener">Difference between substring(),slice() and substr()</a>

The above code snippet uses simple JavaScript to make the first letter in a string to upper case. There are few other ways as well I will explain them one by one.

<ul><li></li></ul>

{{< figure src="Capitalize-first-letter.png" title="Capitalize the first letter in JavaScript String" alt="Capitalize the first letter in JavaScript String" >}}

### Capitalize the First Letter of a String in JavaScript using Regular expressions:

If you are comfortable with the regular expression use the following JavaScript function to capitalize the first letter of a string.

<pre>function capitalizeFirstLetter(string) {
  if(typeof string==undefined) return;
  var firstLetter = string[0] || string.charAt(0);
  return firstLetter ? string.replace(/^./, firstLetter.toUpperCase()) : '';
}</pre>

But it is not required to use regular expressions for this simple operation. And the performance is very low when compared to above methods. Use Regular expressions only for complex scenarios.

### Capitalize the First Letter of a String in JavaScript using ES6+(ECMAScript) features:

To capitalize the first letter of a string,&nbsp;use the following JavaScript ES6+ code snippet.

Here I am using Arrow functions in ES6+

<pre>const capitalizeFirstLetter = (string) =&gt;
      string[0] ? `${string[0].toUpperCase()}${string.substring(1)}` : '';
var lowercase_string = "this is test string";
var firstLetter_capital=capitalizeFirstLetter(lowercase_string);
console.log(firstLetter_capital);
//This is test string</pre>

Or We can use Destructuring&nbsp;assignment feature in ES6+

<pre>const capitalizeFirstLetter= ([first,...rest]) =&gt;
      first ? first.toUpperCase() + rest.join('') : '';</pre>

### Capitalize the first letter of a string in JavaScript by Overriding String Prototype:

If you want to make the first letter of a string to uppercase frequently in your application then you can override string prototype by adding a new function

<pre>String.prototype.capitalizeFirstLetter = function() {
return this.charAt(0).toUpperCase() + this.slice(1);
}
var lowercase_string="this is a test string";
var uppercase_string = lowercase_string.capitalizeFirstLetter();
console.log(uppercase_string);
// This is a test string</pre>

Altering the String.prototype is not advisable because.

<ul><li>It is very slow in terms of performance</li><li>Maintaining the code is difficult because it is very hard to identify where the function is being added to string prototype.</li><li>Can cause conflicts if other person uses the same name to add a new function to string prototype.</li><li>The browser might add a new native function with the same name in future.</li></ul>

### Best way to make the first letter of a string to uppercase in JavaScript:

If you are using the latest browser you can use ES6+ features (without Destructuring&nbsp;assignment) otherwise use simple JavaScript function as mentioned initially.

Regular expressions, overriding string prototype &amp; ES6+ with Destructuring&nbsp;assignment are very slow in terms of performance.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







