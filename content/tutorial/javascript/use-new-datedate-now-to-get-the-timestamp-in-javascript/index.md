+++
title="4 Ways To Get The Current Timestamp In JavaScript"
summary="To get the current timestamp in JavaScript Just use +new Date() or You can use Date.now() or new Date().getTime() or new Date().valueOf()"
keywords="get timestamp in javascript,+new date(),date.now(),new date().gettime(),new date().valueof(),javascript"
type='post'
date='2019-11-07T18:03:16+0000'
lastmod='2019-11-07T18:03:16+0000'
draft='false'
authors=['admin']
[image]
caption='4 Ways To Get The Current Timestamp In JavaScript'
focal_point=''
preview_only=false
+++

To get the current timestamp in JavaScript we can use 4 different methods as shown in below table.

<div class='table-responsive'><table class='table'><thead><tr class="row-1 odd"><th class="column-1">Javascript Method</th><th class="column-2">Result</th></tr></thead><tbody class="row-hover"><tr class="row-2 even"><td class="column-1">Date.now();</td><td class="column-2">1561682894385</td></tr><tr class="row-3 odd"><td class="column-1">+new Date();</td><td class="column-2">1561682890500</td></tr><tr class="row-4 even"><td class="column-1">new Date().getTime()</td><td class="column-2">1561682885990</td></tr><tr class="row-5 odd"><td class="column-1">new Date().valueOf()</td><td class="column-2">1561682881972</td></tr></tbody></table></div>

Timestamp (originated from UNIX) is an integer represents of the number of seconds elapsed since January 1 1970.

The above methods returns current timestamp in milliseconds.

There are Four methods to get the current timestamp in JavaScript, as listed below

{{%toc%}}

{{< figure src="Get-current-timestamp-javascript.jpeg" title="Get current timestamp javascript" alt="Get current timestamp javascript" >}}

## Get the current timestamp in JavaScript by using +new Date():

<em>+new Date()&nbsp;</em>returns the current timestamp in milliseconds.

The unary operator plus(+) in&nbsp; <em>+new Date()&nbsp;</em>calls the <em>valueOf()</em> method in <em>Date</em> object and returns timestamp in milliseconds.

To get the timestamp in seconds use the following JavaScript code

<pre>Math.floor(+new Date() / 1000)</pre>

## Get the current timestamp in JavaScript by using Date.now():

We can use Date.now() method in Date object to get the current timestamp in JavaScript in milliseconds.

Almost all browsers supports this method except IE8 and earlier versions.

It is better to use Date.now() to get the timestamp because of readability.

<pre>&nbsp;Math.floor(Date.now() / 1000)
 // or you can use following javascript code to get timestamp in seconds
 Date.now() / 1000 | 0</pre>

The second method is little bit faster but lacks readability.

## Get the current timestamp in JavaScript by using new Date().getTime():

For cross browser compatbility we can use getTime() method of Date object to get the current timestamp in milliseconds

<pre>new Date().getTime()
Math.round(new Date().getTime()/1000)</pre>

## Get the current timestamp in JavaScript by using new Date().valueOf():

Or we can use new Date().valueOf() method

<pre>new Date().valueOf()
Math.round(new Date().valueOf()/1000)</pre>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







