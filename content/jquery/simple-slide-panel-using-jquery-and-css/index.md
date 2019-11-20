+++
title="Simple Slide Panel Using Jquery And CSS"
summary="This jQuery Tutorial explains how to create a simple Slide Panel with jQuery.I used jQuery sliding methods like jQuery slide toggle to create sliding panel."
keywords="jquery,css,slide panel jquery,slidetoggle,slideup,slidedown,vertical slide panel jquery,slide panel jquery example"
type='post'
date='2019-09-03T18:08:30+0000'
lastmod='2019-09-03T18:08:30+0000'
draft='false'
authors=['admin']
[image]
caption='Simple Slide Panel Using Jquery And CSS'
focal_point=''
preview_only=false
+++
















&nbsp;





And for sliding button I created one paragraph with class ‘<span style="text-decoration: underline;"><em>jquery slide</em></span>‘.

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

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.









