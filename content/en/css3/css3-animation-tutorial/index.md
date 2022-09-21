+++
title="A Simple Walking Man CSS3 Animation Tutorial"
summary="This CSS3 Animation Tutorial will explains Basics of CSS3 Animations like CSS3 Keyframe Animation,CSS3 Transform,CSS3 Rotate Animation with walking man Example."
keywords=["css3 animations,css3 animation tutorial,css3 animation example,css3 rotate animation,css3 keyframes,css3 transform,css3 animation effects,css,html5,css3"
]
type='post'
date='2019-10-07T18:05:56+0000'
lastmod='2019-10-07T18:05:56+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


CSS3 is great way to Create Animations, we can replace flash Animations,Animated images and JavaScript with&nbsp;<span style="text-decoration: underline;"><em>CSS3 Animation</em></span>&nbsp;properties.

In this <span style="text-decoration: underline;"><em>CSS3 Animation Tutorial</em></span> I will explain how to create Walking Man <span style="text-decoration: underline;"><em>Animation Effect Using CSS3</em></span> alone as shown below.

{{< video attributes="controls autoplay muted" webm-src="CSS3-Animation.webm" mp4-src="CSS3-Animation.mp4" >}}


&nbsp;

At the end of this post you will understand following CSS3 Animation Properties.

<ul><li><span style="text-decoration: underline;"><em>CSS3 KeyFrame Animation</em></span>&nbsp;: &nbsp; &nbsp; &nbsp; &nbsp;property which allows us to create animations.</li><li><span style="text-decoration: underline;"><em>CSS3 Transform</em></span>&nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;property which allows us to rotate,scale,skew,move elements.</li><li><span style="text-decoration: underline;"><em>CSS3 Transform Origin :</em></span><em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</em>property which sets the origin of transformations</li></ul>

First we will create static man here is the sample HTML code

<pre>&lt;div id='WalkingMan'&gt;
 &lt;div class='ManBody'&gt;
	&lt;div class='body'&gt;
                &lt;p class='Manhead'&gt;&lt;/p&gt;
		&lt;p class='Middlepart'&gt;&lt;/p&gt;
		&lt;p class='Lhand'&gt;&lt;/p&gt;
		&lt;p class='Rhand'&gt;&lt;/p&gt;
	&lt;/div&gt;
	&lt;p class='LLeg'&gt;&lt;/p&gt;
	&lt;p class='RLeg'&gt;&lt;/p&gt;
 &lt;/div&gt;
&lt;/div&gt;</pre>

&nbsp;

We divided man into two parts

<ul><li>Man Body which contains Head , chest and Hands.</li><li>Man Legs</li></ul>

Now we will apply CSS

<pre>.ManHead 
{
	width: 20px;
	height: 20px;
	border-radius: 50%;
	background: #000;
}
.MiddlePart 
{
	background: #000;
	height: 40px;
	width: 10px;
        border-radius: 100%;
	-webkit-transform: scale(2.2,1.3) skewY(-30deg);

}
.LHand,.RHand,LHand,RHand
{
       height: 50px;
       width: 5px;
       background: #000;
}</pre>

&nbsp;

The CSS code is straight forward except transform property(For Middle Part)

<ul><li>Skew property turns element at an given angle,depending upon parameters X or Y axis</li></ul>

<pre>-webkit-transform: skew(30deg,20deg);</pre>

&nbsp;

In our example I used skewY which turns element vertically(Y-axis) -30 deg.

<ul><li>And scale property increased or decreases the element size,&nbsp;depending on the parameters given for the width (X-axis) and the height (Y-axis)</li></ul>

The above code creates sample body parts as shown below



{{< figure src="CSS3AnimationBody-102x150.png" title="CSS3 Animation" alt="CSS3 Animation" >}}

&nbsp;

Now we have to align all this body parts to create man

Apply the following CSS Code.

<pre>#WalkingMan {
	background: #FFF;
	width: 700px;
	height: 150px;
	margin: 50px auto;
	text-align: center;
}
.body {
	float:left;
	position: absolute;
}

.Manhead {
	width: 20px;
	height: 20px;
	border-radius: 50%;
	background: #000;
	position: absolute;
	margin-top: 15px;
	margin-left: 0px;
}

.Middlepart {
	background: #000;
	height: 40px;
	width: 10px;
	position: absolute;
	margin-top: 38px;
	margin-left: -5px;
	border-radius: 100%;
	-webkit-transform: scale(2.2,1.3) skewY(-30deg);	
}
.Lhand, .Rhand {
	margin-top: 38px;
	margin-left: -5px;
	height: 50px;
	width: 5px;
	background: #000;
	float:left;
}
.LLeg, .RLeg {
	margin-top: 80px;
	margin-left: -5px;
	height: 50px;
	width: 5px;
	background: #000;
	float:left;
}
.ManBody
{
margin-left: 350px;
}</pre>

&nbsp;

This will create the static Man as shown below.

{{< figure src="CSS3AnimationStaticman-150x144.png" title="CSS Animation" alt="CSS Animation" >}}

Now we apply <span style="text-decoration: underline;"><em>CSS3 KeyFrame rule</em></span><em>&nbsp;</em>&nbsp;property to move this man.

### <span style="text-decoration: underline;"><em>What is CSS3 KeyFrame rule?</em></span>

This property allows us to Create Animations Using CSS3. Keyframe property supports all major browsers (IE 10+) and for safari chrome we have to prefix corresponding browser engine

To create Animations follow below two steps

<ul><li>First Define CSS styles inside the @keyframetag</li><li>Now apply the rule to the element using animation property.</li></ul>

Observe the below sample <span style="text-decoration: underline;"><em>CSS3 KeyFrame Animation Example</em></span> which changes the div color to red to yellow for every 5 sec

<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;style&gt; 
div
{
width:100px;
height:100px;
background:red;
-webkit-animation:myfirst 5s alternate infinite ease-out;
}
@-webkit-keyframes myfirst
{
from {background:red;}
to {background:yellow;}
}
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

&nbsp;

We defined a @keyframe with name “myfirst” &nbsp;We are changing from red to yellow.And applying the animation property on div with duration.&nbsp;You must specify the duration otherwise animation wont effect because default value is ‘0’

We can use keywords like “<span style="text-decoration: underline;">from</span>” and “<span style="text-decoration: underline;">to</span>” for changing styles or we can specify change in percent 0% means “first” &nbsp;and 100% means “to”

0% is the beginning of the animation and 100% is when the animation is complete. Visit W3schools for more details.

Now come to our <span style="text-decoration: underline;"><em>CSS3 Animation Demo</em></span>

I divided animations into two parts

<ul><li>Moving hands and Legs</li><li>Moving Entire Body</li></ul>

For Moving Hands Apply the Following CSS

<pre>.Lhand, .RLeg {
	-webkit-transform-origin: 0 0;
	-webkit-animation: movement1 0.5s alternate infinite ease-out;

}
.Rhand, .LLeg {
	-webkit-transform-origin: 0 0;
	-webkit-animation: movement2 0.5s alternate infinite ease-in;
}

/* for movement 1 */
@-webkit-keyframes movement1
{
	from {
		-webkit-transform:rotate(-30deg);
	}
	to {
		-webkit-transform:rotate(30deg);
	}
}

/* for movement 2 */
@-webkit-keyframes movement2
{
	from {
		-webkit-transform:rotate(30deg);
	}
	to {
		-webkit-transform:rotate(-30deg);
	}
}</pre>

&nbsp;

Right hand and left leg should sink with each other so applied same <span style="text-decoration: underline;"><em>CSS3 Animation Effect</em></span> for both elements and vice versa.

For moving hands I am using <span style="text-decoration: underline;"><em>CSS3 transform rotate</em></span> property from 30 degrees to -30 degree.

And I applied <span style="text-decoration: underline;"><em>CSS3 transform-origin</em></span> property as 0%(x-axis) 0%(Y-axis) which specify that with respect to element starting position we should apply the transformation.

i.e., we should rotate leg or hand at angle of 30 deg with respect element starting position.(Remove this property in demo example and check the animation you will understand in a better way).

And infinite means continuously we should apply the animation.

Here is the CSS3 Animation.

{{< video attributes="controls autoplay muted" webm-src="AnimatedManCSS3.webm" mp4-src="AnimatedManCSS3.mp4" >}}


Only Legs and Hands are moving rite. Now we should move entire body for that purpose I applied following animation to manBody

<pre>.ManBody {
                margin-left:350px;		
		-webkit-animation: ManBody 9s infinite ease-in;

	}
@-webkit-keyframes ManBody
{
	from {margin-left:30px;}
	to {margin-left:600px;}
}</pre>

&nbsp;

The Logic straight forward simply we should apply the margin-left style &nbsp;30px to 600px for every 9 sec.

Here is the Final Demo for <a title="Css3 Animation Demo" href="https://arungudelli.com/Tools/HTML5/CSS3%20Animations/CSS3Animation.html" target="_blank" rel="noopener">Walking Man Effect Using CSS3 Animation</a>.

<strong>NOTE:</strong>&nbsp;The above CSS is for Chrome and Safari which uses Webkit engine For Opera and IE10 No need to add any prefix and For mozilla add Moz prefix.

The Demo works fine with Chrome Safari Mozilla IE10 I have not tested with Opera I hope it will work.

Also Read: <a title="Google hangouts" href="https://www.arungudelli.com/html5/google-hangout-effects-using-html5-and-javascript-facedetection/" target="_blank" rel="noopener">Google Hangout Effects using HTML5 Canvas</a>

I hope you’ve enjoyed this <span style="text-decoration: underline;"><em>CSS3 Animation Tutorial</em></span> and that it gives you more ideas on <span style="text-decoration: underline;"><em>CSS3 Animation effects</em></span>.











