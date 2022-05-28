+++
title="Javascript FlatMap() And Javascript Flat()"
summary="JavaScript introduced two new methods flat(),flatMap() to flatten array of arrays into single one dimensional array."
keywords=["javascript,javascript flat(),javascript flatmap()"
]
type='post'
date='2019-11-08T18:03:13+0000'
lastmod='2019-11-08T18:03:13+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

JavaScript introduced two new methods flat(),flatMap() to flatten array of arrays into single one dimensional array. These two methods are under active develoment. Check the browser compatability before using.

flat() and flatMap() method APIs available in Chrome 69 and Mozilla firefox&nbsp;62,Opera 56.

{{%toc%}}

## JavaScript Array flat():

JavaScript Array flat() method takes depth as a parameter and returns a new single dimensional array by merging all sub-arrays. And depth parameter is optional.

Hava look at the below example

### Array flat() without depth parameter:

<pre>var array1 = [0, 1, [2, 3]];
array1.flat();
// [0, 1, 2, 3]

var array2 = [0, 1, [2, 3, [4, 5]]];
array2.flat();
// [0,1, 2, 3, [4, 5]]</pre>

### Array flat() with depth parameter:

<pre>var array2 = [0, 1, [2, 3, [4, 5]]];
array2.flat(2);
// [0,1, 2, 3, 4, 5]</pre>

### Remove empty slots in Array using JavaScript flat():

Array flat removes empty slots in JavaScript arrays

<pre>var arrayEmpty = [1, 2, , 4, 5];
arrayEmpty.flat();
// [1, 2, 4, 5]</pre>

{{< figure src="JavaScript-flat-and-flatMap-methods.jpeg" title="JavaScript flat and flatMap methods" alt="JavaScript flat and flatMap methods" >}}

## JavaScript Array flatMap():

Array flatMap() maps elements array using a mapping function and then flatten the array upto depth of 1.

<pre>let stringArray = ["Javascript flat()", "flatMap()"];

stringArray.map(x=&gt;x.split(" "));
// [["Javascript","flat()"],["flatMap()"]]

stringArray.flatMap(x =&gt; x.split(" "));
// ["Javascript","flat()","flatMap()"]</pre>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







