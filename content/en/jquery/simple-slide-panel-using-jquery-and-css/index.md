+++
title="Simple Slide Panel Using Jquery And CSS"
summary="This jQuery Tutorial explains how to create a simple Slide Panel with jQuery.I used jQuery sliding methods like jQuery slide toggle to create sliding panel."
keywords=["jquery,css,slide panel jquery,slidetoggle,slideup,slidedown,vertical slide panel jquery,slide panel jquery example"
]
type='post'
date='2019-09-03T18:08:30+0000'
lastmod='2019-09-03T18:08:30+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

Today I will explain how to create a slide panel jquery effect with an example. Jquery provides various sliding methods such as

slideDown()
slideUp()
slideToggle()

I used slideToggle method to create  jquery slide panel effect.

slideToggle Method:
First we will understand what is this slideToggle Method.

As per the name of this method it changes between the slideDown and slideUp methods
If the element have been slideDown it changes it will Slide them Up and vice versa.
See the  slideToggle example

```
<!doctype html>
<html> 
<head> 
<style></style>
 <script></script>
 </head> <body> 
<div id="panel"> 
<img style="float:left; "src="welcome-to-my-blog.jpg" align="center" height="100%"/>
< br/><br/>
<p><i><h1>Put your own content here</h1></i></p>
 </div> <p><a href="#">Slide Panel</a></p> 
</body>
 </html>
``` 

I created one div with id ‘slide panel jquery‘.
You can add your own content in this slide panel jquery div.
And for sliding button I created one paragraph with class ‘jquery slide‘.

And I added some CSS stuff as shown below.


<pre>body {
	margin: 0 auto;
	padding: 0;
	width: 570px;
	font: 75%/120% Arial, Helvetica, sans-serif;
}
a:focus {
	outline: none;
}
#panel {
	background: #FAFAD2;
	height: 200px;
	display: none;
}
.slide {
	margin: 0;
	padding: 0;
	border-top: solid 4px #422410;
	background: url(button.gif) no-repeat center top;
}
.btn-slide {
	background: url(white-arrow.gif) no-repeat right -50px;
	text-align: center;
	width: 144px;
	height: 31px;
	padding: 10px 10px 0 0;
	margin: 0 auto;
	display: block;
	font: bold 120%/100% Arial, Helvetica, sans-serif;
	color: #000000;
	text-decoration: none;
}
.active {
	background-position: right 12px;
}</pre>

&nbsp;

And finally to create <span style="text-decoration: underline;"><em>slide panel jquery</em></span>&nbsp;simply add below jquery code

<pre>$(document).ready(function(){
	$(".btn-slide").click(function(){
		$("#panel").slideToggle("slow");
		$(this).toggleClass("active"); return false;
	});
});</pre>

&nbsp;

The syntax of slideToggle is

<pre>$(selector).slideToggle(speed,callback);</pre>

&nbsp;

It will take two parameters Speed and Callback both are optional

<ul><li>Speed parameter can be: “slow”, “fast”, milliseconds.</li><li>Callback parameter is a function that will execute after the sliding completes.</li></ul>

I hope you understand the <span style="text-decoration: underline;"><em>slide panel jquery example</em></span><em>&nbsp;</em> tutorial

Here is the <a title="Jquery Slide panel demo" href="https://www.arungudelli.com/Tools/HTML5/SlidePanel/JquerySlidePanelDemo.htm" target="_blank" rel="noopener">&nbsp;Jquery Slide Panel Demo </a>.

If You have any doubts feel free to contact me.











