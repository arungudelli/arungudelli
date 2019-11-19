+++
title="JavaScript Automatic Semicolon Insertion & Curly Brace Placement"
summary="JavaScript Automatic Semicolon insertion happens because semicolons are optional in JavaScript. Be careful while using curly braces with return statements."
keywords="javascript,javascript semicolon,javascript automatic semicolon insertion"
type='post'
date='2019-11-16T20:52:09+0000'
lastmod='2019-11-16T20:52:09+0000'
draft='false'
authors=['admin']
[image]
caption='JavaScript Automatic Semicolon Insertion & Curly Brace Placement'
focal_point=''
preview_only=false
+++








JavaScript is tricky sometimes &amp; every time it offers something new to learn.

Have a look at the following JavaScript example

<pre>function foo1()
{
  return
  {
    text: "hello"
  };
}

function foo2()
{
  return{
    text: "hello"
  };
}
console.log(foo1());
console.log(foo2());</pre>

&nbsp;

Both functions seem&nbsp;to be same and if you are a beginner in JavaScript you would expect both console logs display the same result.

<pre>undefined
{ text: 'hello' }

</pre>

foo1() displays undefined. Whats wrong with the code? If you see&nbsp;the foo1() method definition, after return statement curly brace starts from the new line. Whats wrong with it.

In JavaScript semicolons are optional. If you are coming from traditional programming languages you have a habit of inserting semicolons after each statement. But most of the JavaScript developers ignore semicolons as they are not necessary.

But in background automatic semicolon insertion being done by JavaScript interpreters based on few rules.

That is the problem with the above code.

{{< figure src="JavaScriptAutomaticSemicolon.jpg" title="JavaScript Automatic Semicolon Insertion" alt="JavaScript Automatic Semicolon Insertion" >}}

Because of JavaScript Automatic Semicolon insertion. The above code interpreted as

<pre>function foo1()
{
  return ;   // Semicolon being inserted by javascript interpreters&nbsp;
  {
    text: "hello"
  };
}</pre>

So because of semicolon after return statement function, execution stops there and return undefined. ignoring the below code block.

One workaround will be using the code block in foo2() or

<pre>function foo1() 
{
  var obj =
  {
    text: "hello"
  };
  return obj;
}</pre>

But this is not required as long as you know the basics of JavaScript and use semicolon whenever you think it is necessary to increase readability. Be careful while using return statement with curly braces.

Reference: <a href="https://www.ecma-international.org/ecma-262/5.1/#sec-7.9.1" target="_blank" rel="nofollow noopener">Rules of Automatic Semicolon Insertion</a>

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







