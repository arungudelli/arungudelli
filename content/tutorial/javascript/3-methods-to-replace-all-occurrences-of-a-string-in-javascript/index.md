+++
title="3 Methods To Replace All Occurrences Of A String In JavaScript"
summary="Javascript replace method, replaces only the first occurrence of the string. To replace all occurrences of a string in Javascript use string replace() & regex,Javascript split() & join(), Javascript indexOf method."
keywords="replace all occurrences of a string in javascript,javascript replace,javascript replace all,javascript replace special characters,javascript replace all spaces,javascript replace all comma,javascript replace regex group,javascript replace all escape characters,javascript"
type='post'
date='2019-11-13T18:02:48+0000'
lastmod='2019-11-13T18:02:48+0000'
draft='false'
authors=['admin']
[image]
caption='3 Methods To Replace All Occurrences Of A String In JavaScript'
focal_point=''
preview_only=false
+++


Javascript replace() method replaces only the first occurrence of the string

To replace all occurrences of a string in Javascript, use the below methods

<ol><li>Javascript string replace method with regular expression</li><li>Javascript split and join method</li><li>Javascript indexOf method</li></ol>

Take a look at the below example of Javascript Replace() method

<pre>var stringtoreplace="js";
var targetstring="vanilla js has replace method and this js method wont replace all occurrences";
targetstring.replace(stringtoreplace,"javascript");
//vanilla javascript has replace method and this js method wont replace all occurrences</pre>

It will replace only first occurrence as shown above.

{{%toc%}}

{{< figure src="replace-all-occurences-of-a-string-in-javascript.jpg" title="replace all occurences of a string in javascript" alt="replace all occurences of a string in javascript" >}}

## Replace all occurrences of a string in Javascript using replace and regex:

To replace all occurrences of a string in JavaScript, we have to use regular expressions with string replace method.

We need to pass a regular expression as a parameter with <span style="text-decoration: underline;"><em>‘g’</em><em> flag</em></span><em>&nbsp;(global)</em> instead of a normal string.

In the above example, we will pass the parameter as regular expression as shown below

<pre>targetstring.replace(/js/g,"javascript");
//vanilla javascript has replace method and this javascript method wont replace all occurrences</pre>

Or we can use the syntax of regexp as shown below to replace all occurrences

<pre>var stringReg= new RegExp(stringtoreplace, 'g');
targetstring = targetstring.replace(stringReg, 'javascript');</pre>

Depending upon our comfort we can use either of the regular expression ways.

## Javascript case insensitive replace all:

The above method will not replace the case-insensitive string.

To replace all occurrences of case insensitive string in Javascript, we have to pass <span style="text-decoration: underline;"><em>‘i’ flag</em></span> in addition to global flag.

Go through the below example

<pre>var target = "javascript is very popular scripting language,and It IS easy to learn";
target.replace(/is/g,'');
//"javascript  very popular scripting language,and It IS easy to learn"</pre>

Now we will option additional option <em>i</em> to the regular expression

<pre>target.replace(/is/gi,'');
"javascript  very popular scripting language,and It  easy to learn"</pre>

## Replace all occurrences of a string in Javascript using split and Join method:

Instead of this we can replace all occurrences of a string in JavaScript using split and join methods in Javascript as shown below

<pre>let some_str = 'abc def def lom abc abc def'.split('abc').join('x')
console.log(some_str)
//"x def def lom x x def"</pre>

At First split method returns&nbsp; an array of token strings, divided at the string ‘abc’ position as shown below

<pre>&nbsp;&nbsp;["", " def def lom ", " ", " def"]</pre>

And after that we will combine the string array using join method with the target string.

<pre>["", " def def lom ", " ", " def"].join('x')
"x def def lom x x def"</pre>

## Replace all occurrences of a string in Javascript using indexOf method:

We can write our own function to replace all string occurrences in a text using javascript indexOf method.

All we need to do is, loop through each occurrence and replace it with the given string as shown below

The below method uses indexof method to find the occurrence and replaces it using the replace method until all occurrences are completed.

<pre>function replaceAll(find, replace, str)
{
  while( str.indexOf(find) &gt; -1)
  {
   str = str.replace(find, replace);
  }
 return str;
}</pre>

## Replace all occurrences of a string with special characters:

For example, we need to replace all occurrences of a string with special characters

Take a look at the below example

<pre>var some_string = 'a?bc def def lom a?bc a?bc def';</pre>

Now we will try to replace ‘a?bc’ string with ‘x’ with the above method

<pre>some_string.replace(/a?bc/g,'x')
"a?x def def lom a?x a?x def"</pre>

The string not being replaced properly why because regular expressions do not work well with special characters.

The solution for this problem is we need to escape the string which contains special character before passing it as a regular expression

Mozilla doc provided a method to escape the special characters in a string

<pre>function&nbsp;escapeRegExp(str)
{
return&nbsp;str.replace(/[.*+?^${}()|[\]\\]/g,&nbsp;"\\$&amp;");
// $&amp; means the whole matched string
}</pre>

Now we will pass our string to the above method to escape specail characters as shown below

<pre>var stringtoreplace =&nbsp;escapeRegExp('a?bc')
//"a\?bc"</pre>

And the we will create a regular expression using escaped string

<pre>var regextoreplace = new&nbsp;RegExp(stringtoreplace,'g');</pre>

Now by using the above regular expression, we will replace all occurrences of a string with special characters in the target string

<pre>some_string.replace(regextoreplace,'x');
"x def def lom x x def"</pre>

## Javascript replace all commas in a string:

To replace all commas in string use the below JavaScript code

<pre>var some_string = 'abc,def,ghi';
some_string.replace(/,/g,';')
"abc;def;ghi"</pre>

## Javascript replace all spaces in a string:

To replace all spaces in a string use the below JavaScript code

<pre>var some_string = 'abc def ghi';
some_string.replace(/ /g,';')
"abc;def;ghi"</pre>

## 

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







