+++
title="Html Table With Fixed Header & Scrollable Body"
summary="In HTML table most of the cases we need a fixed header & scrollable body. In this post I explains how to create a table with fixed header & body scrollable in HTML"
keywords="html"
type='post'
date='2019-08-16T18:09:25+0000'
lastmod='2019-08-16T18:09:25+0000'
draft='false'
authors=['admin']
[image]
caption='Html Table With Fixed Header & Scrollable Body'
focal_point=''
preview_only=false
+++

In this post I will explain how to create a HTML table with fixed header & scroll-able body.

How we can Fix headers in a html table(Scroll Body). Here is the simple and nice solution. 

## In Internet Explorer:
 
In IE we have a style option expression using this we can fix headers
Add following css code to tr tag in table (i.e.,th tag)

```
style=”position: relative; 
top: expression(this.offsetParent.scrollTop);”
```
But It will work only in IE 5+ . to fix headers in other browsers we have an alternate.

## For all browsers:

This is actual table.
I have created two div inner,outer as shown below
(actual table)

```
< div class=”outer”>
< div class=”inner”>
< table> < thead> < /thead> < tbody> < /tbody> < /table>
< /div>
< div class=”Headers”>
< table> < thead> < /thead> < tbody> < /tbody> < /table> (dummy table)
< /div>
< /div>
```

And also I have created one dummy table as shown above with class Headers

In CSS I wrote following code.

```
.outer {
position:relative;//this is very imp
width:500px;
}
.inner {
height:150px;
overflow:auto;
}
.header {
position:absolute; //this is very imp
top:0;
left:0;
overflow:hidden;
}
```

In header we have `position:absolute;` when we declare position absolute it checks for it is parent tag ie., outer

If in outer if position is relative. Then
Where ever we write header div class in html document it always print relative to outer div class.

And top position is 0 in header ie., outer div header div overlap with each other.
Initially header div contain nothing

In jquery we are copying header from inner table to header table as shown below

```
$(document).ready(function() {
$(‘.header table thead’).html( $(‘.inner table thead’).html() );
$(‘.header’).css(‘width’, $(‘.inner table’).outerWidth() );
$(‘.header’).css(‘height’, $(‘.inner table thead’).outerHeight() );
});
```












Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.









