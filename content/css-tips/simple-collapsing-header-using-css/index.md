+++
title="A Simple Collapsing Header Using CSS"
summary="This Tutorial will explain how to Create a Simple Collapsing Header Effect using CSS. See the Collapsing Header Examples to Understand the Tutorial."
keywords="collapsing header effect,css,header tag,collapsing header examples,collapsing header css"
type='post'
date='2019-11-16T20:55:47+0000'
lastmod='2019-11-16T20:55:47+0000'
draft='false'
authors=['admin']
[image]
caption='A Simple Collapsing Header Using CSS'
focal_point=''
preview_only=false
+++








Today I will explain&nbsp;<span style="text-decoration: underline;"><em>How to create a Simple Collapsing &nbsp;Header Using CSS</em></span><em>&nbsp;</em>with an Example.

Here is the demo&nbsp;&nbsp;<a title="Collapsing Header CSS" href="https://www.arungudelli.com/Tools/HTML5/SimpleCollapsingHeaderusingCSS.htm" target="_blank" rel="noopener">Collapsing Header CSS</a>

Now a days most of the webpages are contains Header and &nbsp;Banner.

So First We will divide page into three parts like Header,Banner and Content.

Here is the sample HTML

<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;meta charset="utf-8" /&gt;
&lt;title&gt;Simple Collapsing Header using CSS&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div id="container"&gt;
	&lt;header&gt;
		&lt;h1&gt;Header&lt;/h1&gt;
	&lt;/header&gt;

	&lt;div id="banner"&gt;
		&lt;h2&gt;Banner&lt;/h2&gt;
	&lt;/div&gt;

	&lt;div id="content"&gt;
		&lt;p&gt;Content&lt;/p&gt;
	&lt;/div&gt;

&lt;/div&gt;

&lt;/body&gt;
&lt;/html&gt;</pre>

&nbsp;

{{< figure src="CollapsingHeaderUsingCSS.png" title="CollapsingHeaderUsingCSS" alt="CollapsingHeaderUsingCSS" >}}

You might be thinking what is this header tag, The <span style="text-decoration: underline;"><em>header tag</em></span> is new in HTML5. It supports almost all browsers. Here is the quick round of introduction to header Tag.

<ul><li>The &lt;header&gt; tag represents a header for a document or section</li><li>The &lt;header&gt; element should be used as a container for introductory content or set of navigational links.</li><li>You can have multiple &lt;header&gt; elements in one document.</li></ul>

The following CSS code will apply to Header Element

<pre>header {
	height: 100px;
	background: #99FF66;
	position: fixed;
	width: 100%;
	z-index: 10;
}</pre>



&nbsp;

Height I given as 100px and positions as fixed to prevent the scrolling.The important thing here is <em><span style="text-decoration: underline;">Z-Index</span></em> of header it should have higher index

<ul><li>Height I given as 100px</li><li>Positions as fixed to prevent the scrolling.</li><li>The important thing here is Z-Index of header should have higher index.this will ensure the rest of the page that does flows underneath &nbsp;the header. So I gave some maximum value as 10.</li></ul>

And Next thing is Banner

<pre>#banner {
	width: 100%;
	height: 300px;
	position: fixed;
	top: 100px;
	background: #FFFF66;
}</pre>

<ul><li>This needs scrolling effect.</li><li>As I given header height as 100px. It should be fixed relative to header height so I given position as fixed and top 100px.</li><li>This will ensure banner content to sit directly underneath the header.</li></ul>

And Finally Content

<pre>#content {
	width: 100%;
	position: relative;
	top: 400px;
	background: #FFFFCC;
	height: 1500px; /* Demo purposes */
}</pre>

<ul><li>We given header as 100px and Banner as 300px so relatively content should start from 400 px from top</li><li>So I gave position as relative and top as 400px.</li></ul>

Here is the Finale Demo <a href="https://www.arungudelli.com/Tools/HTML5/SimpleCollapsingHeaderusingCSS.htm" target="_blank" rel="noopener">Simple Collapsing Header using CSS</a>

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







