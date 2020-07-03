+++
title="Matrix Effect Using HTML5 And Javascript"
summary="To create Matrix Effect using HTML5 and JavaScript,I used HTML5 canvas functions fillText,fillStyle & Javascript setInterval,javascript array map& Math.random()"
keywords="matrix effects,matrix effects html5,html5 canvas filltext,html5 canvas fillstyle,javascript setinterval,javascript math random,javascript array map,html5"
type='post'
date='2019-10-02T18:06:27+0000'
lastmod='2019-10-02T18:06:27+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++


Now a days I am playing around with <span style="text-decoration: underline;"><em>HTML5 Canvas</em> <em>API</em></span> and <span style="text-decoration: underline;"><em>Java Script</em></span>. It’s an amazing option to create animations.

The Matrix movie known for its visual effects.

Then I thought is it possible to <span style="text-decoration: underline;"><em>Create Matrix effects using HTML5 and JavaScript </em></span>&nbsp; something like below.

{{< figure src="MatrixEffect.gif" title="Matrix Effect" alt="Matrix Effect" >}}

First I wrote some JavaScript code as mentioned below.

<pre>&lt;canvas id="myCanvasMatrix" width="500" height="200" style="border:1px solid #c3c3c3;"&gt;
Please Upgrade your browser
&lt;/canvas&gt;
var c1=document.getElementById("myCanvasMatrix");
var ctx1=c1.getContext("2d");
var Matrix=function(){
ctx1.fillStyle='rgba(0,0,0,.05)';
ctx1.fillRect(0,0,500,500);
ctx1.fillStyle="#0f0";
ctx1.fillText('Matrix', Math.random()*(500), Math.random()*(500));
};
setInterval(Matrix,30);</pre>

&nbsp;

I wrote one Matrix function In which I am filling canvas with “Matrix” word at random locations using <span style="text-decoration: underline;"><em>Canvas fillText</em></span> method(Line 10). And I am calling that function using <span style="text-decoration: underline;"><em>J</em><em>avascript setInterval</em></span> Method (Line&nbsp; 12)(Interval Time 30.)

Line 7 and 8 will fill the screen with background color black and opacity of 0.05.

When each time the Matrix function is called,<span style="text-decoration: underline;"><em>Canvas fillStyle</em></span> will draw the background on the screen.Because of this you can see text has different colors at different places on canvas.Some text will have green color without transparent background color. This is because there will be a new layer drawn on the screen each time the Matrix is called

Line 10 will draw “Matrix” word at random locations. I am using <em><span style="text-decoration: underline;">JavaScrip</span><span style="text-decoration: underline;">t Math.random()</span></em> to do the same. Here is the <a title="Simple Matrix Effect Demo" href="https://www.arungudelli.com/Tools/HTML5/MatrixEffectsDemo.html" target="_blank" rel="noopener">Simple Matrix Effect Demo</a>.

But this is not what we expected,Carefully observe the above Matrix Effect Gif Image: All alphabets are drawn along Y-Axis while X-Coordinates are constant.So I changed my code little bit as shown below.This is the key point in our Algorithm to <span style="text-decoration: underline;"><em>Create Matrix effect using HTML5</em></span>

<pre>&lt;canvas id="myCanvas" width="500" height="200" style="border:1px solid #c3c3c3;"&gt;
Your browser does not support the HTML5 canvas tag.
&lt;/canvas&gt;
var YPositions= Array(30).join(0).split('');
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var draw=function(){
ctx.fillStyle='rgba(0,0,0,.05)';
ctx.fillRect(0,0,500,500);
ctx.fillStyle="#0f0";
YPositions.map(function(y,index){
x=(index*10)+10;
ctx.fillText('a', x, y);
if(y&gt;100)
{
YPositions[index]=0;
}
else
{
YPositions[index]=y+10;
}
});
};
setInterval(draw,30);</pre>

&nbsp;

### <span style="text-decoration: underline;">Algorithm Behind Matrix Effects using HTML5 Canvas And JavaScript:</span>

&nbsp;

Here I declared an array (YPositions) to store Y-Coordinates.Initially array will contain all zero’s.And Inside draw() function I am using <span style="text-decoration: underline;"><em>Java script Array Map</em></span> function, basically It Creates a new array with the results of calling a provided function on every element in this array.

Here is the quick <span style="text-decoration: underline;"><em>Example of Java Script Array Map</em></span>

<pre>var numbers = [1, 4, 9];
var roots = numbers.map(Math.sqrt);
/* roots is now [1, 2, 3], numbers is still [1, 4, 9] */
/* math sqrt method called on each element */</pre>

&nbsp;

The Array index starts at ‘0’ zero so, For X -co ordinate I am adding 10,Our X coordinates are (10,20,30,40………290)(Line 12)

And Y co-ordinates will vary from (0 to 110) If&nbsp; Y value &gt; 100 I am resetting array element to ‘0’ otherwise incrementing 10.(Line 14 to 21). Here I am not using new Array I am changing existing(YPositions) array itself using Java Script Array Map function.

I am drawing ‘a’ character on canvas at (x,y) locations. (Line 13).

<ul><li>i.e., on first Iteration we will draw “a” at (10,10)(20,10)(30,10)……(290,10)</li><li>Second Iteration&nbsp; (10,20)(20,20)(30,20)……….(290,20) and this goes until Y &gt;100 then we will reset the value to ‘0’</li></ul>

<em><strong>Also Read</strong></em>&nbsp;&nbsp; :&nbsp; Simple Algorithm to <a title="HTML5 Canvas Polygon" href="https://www.arungudelli.com/2013/08/html5-canvas-polygon.html" target="_blank" rel="noopener">Draw Polygon using HTML5 Canvas</a>

I think now you understood the Logic behind this implementation if you are still in doubt refer below image.

{{< figure src="HTML5CanvasTutorial.png" title="HTML5CanvasTutorial" alt="HTML5CanvasTutorial" >}}

I think now you are clear with Logic.

Now we have to replace “a” with random alphabets and Y positions to some random coordinates to create actual <span style="text-decoration: underline;"><em>Matrix Effect using HTML5 and javaScript</em></span>&nbsp; Here is the final Code.

<pre>&lt;html&gt;&lt;head&gt;
&lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"&gt;&lt;/script&gt;
		&lt;meta charset="utf-8"&gt;
		&lt;title&gt;Matrix&lt;/title&gt;
&lt;/head&gt;
	&lt;body&gt;
	&lt;div align="center"&gt;
	&lt;h3&gt;Matrix Redesigned by &lt;i&gt;Arunkumar Gudelli&lt;/i&gt;&lt;/h3&gt;
	&lt;canvas id="q" width="500" height="500"&gt;Sorry Browser Won't Support&lt;/canvas&gt;&lt;br/&gt;&lt;br/&gt;
	&lt;button id="play"&gt;Play&lt;/button&gt;
	&lt;button id="pause"&gt;pause&lt;/button&gt;
	&lt;/div&gt;
&lt;script&gt;
$(document).ready(function(){
var s=window.screen;
var width = q.width=s.width;
var height = q.height;
var yPositions = Array(300).join(0).split('');
var ctx=q.getContext('2d');

var draw = function () {
  ctx.fillStyle='rgba(0,0,0,.05)';
  ctx.fillRect(0,0,width,height);
  ctx.fillStyle='#0F0';
  ctx.font = '10pt Georgia';
  yPositions.map(function(y, index){
    text = String.fromCharCode(1e2+Math.random()*33);
    x = (index * 10)+10;
    q.getContext('2d').fillText(text, x, y);
	if(y &gt; 100 + Math.random()*1e4)
	{
	  yPositions[index]=0;
	}
	else
	{
      yPositions[index] = y + 10;
	}
  });
};
RunMatrix();
function RunMatrix()
{
if(typeof Game_Interval != "undefined") clearInterval(Game_Interval);
		Game_Interval = setInterval(draw, 33);
}
function StopMatrix()
{
clearInterval(Game_Interval);
}
//setInterval(draw, 33);
$("button#pause").click(function(){
StopMatrix();});
$("button#play").click(function(){RunMatrix();});

})
&lt;/script&gt;
&lt;/body&gt;&lt;/html&gt;</pre>

&nbsp;

I am using <em><span style="text-decoration: underline;">Java script </span><span style="text-decoration: underline;"><em>S</em>tring Char from Code </span></em> Method(Line 27) to generate random alphabets which take ASCII Value as input and gives the corresponding character. In short, it will convert ASCII Codes to Characters.

And also I added two buttons to Play and Pause Matrix Effects.

I prefer you to read <a title="Simle Snake Game Using HTML5 Canvas" href="https://www.arungudelli.com/2012/10/html5-canvas-example-snake-game.html" target="_blank" rel="noopener">Simple Snake Game using HTML5 Canvas</a> to understand this buttons mechanism.

<em><strong>Here is the Final demo</strong></em> of <a title="Matrix Effects Demo" href="https://www.arungudelli.com/Tools/HTML5/MatrixEffectUsingHTML5AndJavaScript.html" target="_blank" rel="noopener">Matrix effects using HTML5 and JavaScript</a>

Learn how to implement &nbsp;<a title="Google hangout Effects" href="https://www.arungudelli.com/2013/09/google-hangout-effects-using-html5-and-javascript-facedetection.html" target="_blank" rel="noopener">Google Hangout webcam Effects using HTML5 getUserMedia&nbsp;</a>

I hope you’ve enjoyed this article and that it gives you more ideas on how we can implement animations using the HTML5 Canvas API.If so share this post with your friends and also join our mailing list

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







