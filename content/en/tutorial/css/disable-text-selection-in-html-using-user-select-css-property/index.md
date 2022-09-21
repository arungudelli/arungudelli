+++
title="Disable Text Selection Highlighting In HTML Using CSS"
summary="We can use user-select property in CSS to disable text selection highlighting in HTML pages.It is not a standard feature, but available in all modern browsers except IE 9 & before."
keywords=["user-select css,disable text selection css,disable text selection highlighting css,css"
]
type='post'
date='2019-11-09T18:03:09+0000'
lastmod='2019-11-09T18:03:09+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


We can use <em>user-select</em>&nbsp;property in CSS to disable text selection highlighting in HTML pages.It is not a standard feature, but&nbsp;available in all modern browsers except IE 9 &amp; before.

{{%toc%}}

{{< figure src="Disable-text-selection-css.jpg" title="Disable text selection css" alt="Disable text selection css" >}}

## Using user-select:none:

To disable the text selection in HTML we need to give <em>user-select</em> property value as <em>none.&nbsp;</em>Go through the below example to understand if further.

<pre>&lt;div&gt;
You can select this text.
&lt;/div&gt;
&lt;div class="disable-select"&gt;
You cannot select this text,text selection is disabled
&lt;/div&gt;</pre>

I have added <em>disable-select</em> class to the second div now we will add user-select css property

<pre>.disable-select {
    user-select: none; /* supported by Chrome and Opera */
   -webkit-user-select: none; /* Safari */
   -khtml-user-select: none; /* Konqueror HTML */
   -moz-user-select: none; /* Firefox */
   -ms-user-select: none; /* Internet Explorer/Edge */
}</pre>

But we have to add browser specific prefix before the <em>user-select</em> option for safari,firefox and internet explorer or edge.

Chrome and opera supports non prefixed versions.

## In Google Chrome:

To disable text selection highlighting in Google Chrome browser using CSS just set -user-select CSS property to none.

And no prefix is required for Google Chrome and Opera Browsers.

<pre>&nbsp;.disable-select{
  user-select:none;
}</pre>

## In mozilla firefox:

To disable text selection highlighting in mozilla firefox browser using CSS just set -moz-user-select CSS property to none.

And we need add -moz prefix before user-select property for mozilla firefox Browser.

<pre>&nbsp;.disable-select{
   -moz-user-select:none;
}</pre>

## In Safari:

To disable text selection highlighting in Safari browser using CSS just set -webkit-user-select CSS property to none.

And we need add -webkit prefix before user-select property for Safari Browser.

<pre>&nbsp;.disable-select{
  -webkit-user-select:none;
}</pre>

## In IOS Safari:

To disable text selection highlighting in IOS Safari browser using CSS just set -webkit-touch-callout CSS property to none.

<pre>&nbsp;.disable-select{
  -webkit-touch-callout:none;
}</pre>

## In Internet Explorer/Edge using:

To disable text selection highlighting in Internet Explorer/Edge browser using CSS just set -ms-user-select CSS property to none.

And we need add -ms prefix before user-select property for Safari Browser.

<pre>&nbsp;.disable-select{
   -ms-user-select:none;
}</pre>

## What does user-select property will do?

<em>user-select</em> css property controls whether a text in a HTML element can be selected or not. It is not a standard feature.

You can find more details about draft specification <a href="https://drafts.csswg.org/css-ui-4/#content-selection" target="_blank" rel="noopener">here</a>

## user-select property values:

<div class='table-responsive'><table class='table'><thead><tr class="row-1 odd"><th class="column-1">user-select value</th><th class="column-2">description</th></tr></thead><tbody class="row-hover"><tr class="row-2 even"><td class="column-1">none</td><td class="column-2">user cannot select the text</td></tr><tr class="row-3 odd"><td class="column-1">text</td><td class="column-2">user can select the text</td></tr><tr class="row-4 even"><td class="column-1">all</td><td class="column-2">user can select the text with one click</td></tr><tr class="row-5 odd"><td class="column-1">auto</td><td class="column-2">user-select value depend upon its parent user-select option</td></tr><tr class="row-6 even"><td class="column-1">contain</td><td class="column-2">selection will be bound to particular element</td></tr><tr class="row-7 odd"><td class="column-1">element</td><td class="column-2">IE version of user-select contain.</td></tr></tbody></table></div>

## user-select none:

As explained above, when we give user-select property value as none to an HTML element we cannot select the text inside the element including it’s children element.

<pre>&lt;div style="user-select:none;border:1px solid"&gt;
text selection is disabled 
&lt;div&gt;Text selection is disabled in children element also&lt;/div&gt;
&lt;/div&gt;</pre>



## user-select text:

When you give user-select property as text, user can select the text.

<pre>&lt;div style="user-select: none; border: 1px solid;"&gt;
text selection is disabled
&lt;div style="user-select: text;"&gt;You can select me&lt;/div&gt;
&lt;div&gt; text selection is disabled&lt;/div&gt;
&lt;/div&gt;</pre>



## user-select all:

When we give user-select property as all. Text inside the element is automatically selected on context click.

<pre>&lt;div style="user-select:all"&gt;
On click we can select the text
&lt;/div&gt;</pre>

## user-select auto:

user-select auto behavior depends upon its parent element’s computed value of user-select.

<ol><li>If the parent element’s computed value is none then it’s value is none. or if the computed value is all then it’s value is all. or if the value is text it’s value is text</li><li>Otherwise the default behavior is text. that is user can select the text.</li><li>On&nbsp;pseudo elements ::before and ::after the behavior is none</li><li>And if the element is an editable element i.e., text or textarea the computed value is contain or element (In IE)</li></ol>

## user-select contain:

user-select contain is not supported in other browsers except internet explorer. In IE we have to give user-select option as element instead of contain.

So what exactly this user-select contain will do?

When you give user-select as contain or element selection will be bound to that element and cannot be extended.

Go through the below demo to understand it further.

## user-select CSS example:

We will see all user-select options in one place.

<pre>&lt;h3&gt;user-select:none&lt;/h3&gt;
&lt;div class="text-selection-none"&gt;
text selection is disabled 
&lt;div&gt;Text selection is disabled in children element also&lt;/div&gt;
&lt;/div&gt;

&lt;h3&gt;user-select:text&lt;/h3&gt;
&lt;div class="text-selection-none"&gt;
text selection is disabled
&lt;div class="text-selection-text"&gt;You can select me&lt;/div&gt;
&lt;div&gt; text selection is disabled&lt;/div&gt;
&lt;/div&gt;

&lt;h3&gt;user-select:all&lt;/h3&gt;
&lt;div class="text-selection-all"&gt;
  On click we can select the text
&lt;/div&gt;

&lt;h3&gt;user-select:auto&lt;/h3&gt;
&lt;div class="text-selection-none"&gt;
text selection is disabled
&lt;div class="text-selection-auto"&gt;as parent element is none cannot select text&lt;/div&gt;
&lt;div&gt; text selection is disabled&lt;/div&gt;
&lt;br/&gt;

&lt;div class="text-selection-text"&gt;
text selection is enabled
&lt;div class="text-selection-auto"&gt;as parent element is text,can select text&lt;/div&gt;
&lt;div&gt; text selection is enabled&lt;/div&gt;

&lt;br/&gt;

&lt;div class="before text-selection-auto"&gt;as parent element is text,can select text&lt;br/&gt;&lt;/div&gt;

&lt;h3&gt;
user-select:contain
&lt;/h3&gt;

&lt;div class="text-selection-contain"&gt;text selection is contain&lt;br/&gt;&lt;/div&gt;


&lt;div&gt;This is not selected&lt;/div&gt;</pre>

And the corresponding CSS values are

<pre>.text-selection-none{
user-select: none; /* supported by Chrome and Opera */
-webkit-user-select: none; /* Safari */
-khtml-user-select: none; /* Konqueror HTML */
-moz-user-select: none; /* Firefox */
-ms-user-select: none;
}
.text-selection-text{
user-select: text; /* supported by Chrome and Opera */
-webkit-user-select: text; /* Safari */
-khtml-user-select: text; /* Konqueror HTML */
-moz-user-select: text; /* Firefox */
-ms-user-select: text;
}
.text-selection-all{
user-select: all; /* supported by Chrome and Opera */
-webkit-user-select: all; /* Safari */
-khtml-user-select: all; /* Konqueror HTML */
-moz-user-select: all; /* Firefox */
-ms-user-select: all;
}
.text-selection-auto{
user-select: auto; /* supported by Chrome and Opera */
-webkit-user-select: auto; /* Safari */
-khtml-user-select: auto; /* Konqueror HTML */
-moz-user-select: auto; /* Firefox */
-ms-user-select: auto;
}
.text-selection-contain{
user-select: contain; 
-webkit-user-select: contain; 
-khtml-user-select: contain; 
-moz-user-select: contain; 
-ms-user-select: element; /*Only IE supports user-select contain option*/
}
div.before::after {
content: "hi";
}</pre>

Here is the jsFiddle <a href="http://jsfiddle.net/arungudelli/309zd5ck/" target="_blank" rel="noopener">demo</a>

As explained above user-select : contain option is only supported in IE, if you open the fiddle in IE, You can observe its behaviour the element selection cannot be extended beyond the element with class .text-selection-contain.

