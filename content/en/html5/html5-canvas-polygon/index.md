+++
title="How To Draw Polygon Using HTML5 Canvas"
summary="To draw HTML5 Canvas Polygon we have to use JavaScript & Canvas API functions like HTML5 Canvas fill,stroke,lineTo based on path abstractions of Canvas API"
keywords=["html5 draw polygon,html5 canvas polygon,html5 canvas fill,html5 canvas stroke,html5,javascript,html5 canvas"
]
type='post'
date='2019-10-01T18:06:35+0000'
lastmod='2019-10-01T18:06:35+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

This tutorial I will explain simple algorithm to draw polygons using HTML5 canvas API.

First we have to identify the points on HTML5 canvas and then use context.lineto() method for drawing lines and finally use stroke or fill method to make polygon visible. Here is the sample code for Drawing <strong><span style="text-decoration: underline;"><em>HTML5 Canvas Polygon</em></span></strong>

Html5 canvas API comes with so many options and we can draw anything using <span style="text-decoration: underline;"><em>Javascript,</em></span><em>&nbsp;</em> based upon path abstractions.

<pre>var c2 = canvas.getContext('2d');
c2.fillStyle = '#f00';
c2.beginPath();
c2.moveTo(0, 0);
c2.lineTo(100,50);
c2.lineTo(50, 100);
c2.lineTo(0, 90);
c2.closePath();
c2.fill();</pre>

&nbsp;

But the problem is how identify the points to draw polygon?

In this post I will explain <em><strong><span style="text-decoration: underline;">how to draw a regular polygon using HTML5 Canvas.</span>&nbsp;</strong></em><em><br>
</em>

And also pattern to identify the points to draw polygon.

What exactly this regular polygon is.In a regular polygon all angles and all sides are equal.

{{< figure src="RegularPolygon.jpg" title="HTML5 Canvas Polygon" alt="HTML5 Canvas Polygon" >}}

If we observe the above images we can come to know that all vertices of regular polygon can be located on a circle.In other words regular polygon can be inscribed within a circle.

Also read: <a title="Html5 canvas example" href="https://www.arungudelli.com/html5/html5-canvas-example/" target="_blank" rel="noopener">How to develop simple snake game using HTML5 cavas</a>

We will go to our school days and understands some trigonometry functions cosine sine etc. Any point in a circle can be identified as &nbsp;(r cos e,r sin e) where r is the radius and e is the angle.Refer below images. This is the key point in our algorithm to draw regular <em><span style="text-decoration: underline;">&nbsp;HTML5 Canvas Polygon.</span></em>

{{< figure src="Html5CanvasPolygon.jpg" title="Html5CanvasPolygon" alt="Html5CanvasPolygon" >}}

For instance we will take equilateral&nbsp;triangle,as explained above this triangle divides circle into three equal parts and each part will make an angle of 120 degrees at the center(360/3=120).

Now identify the three vertices

<ul><li>First vertex &nbsp; &nbsp; : at 0 degree i.e., (r cos 0,r sin 0)=(r,0)</li><li>Second vertx &nbsp;: at 120 degree i.e., (r cos 120,r sin 120)</li><li>Third vertex &nbsp; &nbsp;: at 240 degree i.e., (r cos 240,r sin 240)</li></ul>

{{< figure src="Html5CanvasPolygon1.jpg" title="Html5CanvasPolygon" alt="Html5CanvasPolygon" >}}

Now our algorithm is ready.

<ul><li>First take number of sides(n) and radius of circle(r)</li><li>And calculate angle made by the each side of regular polygon at center (360/n)</li><li>Identify the first vertex (r,0)</li><li>Loop through the angles to identify the points</li><li>And draw the polygon using store or fill method</li></ul>

Observe the below code carefully I will explain each line one by one.

<pre>function regularpolygon(ctx, x, y, radius, sides) {
  if (sides &lt; 3) return;
  ctx.beginPath();
  var a = ((Math.PI * 2)/sides);
  ctx.translate(x,y);
  ctx.moveTo(radius,0);
  for (var i = 1; i &lt; sides; i++) {
    ctx.lineTo(radius*Math.cos(a*i),radius*Math.sin(a*i));
  }
  ctx.closePath();
}</pre>

&nbsp;

We are passing context(ctx),center of regular polygon(x,y),radius(r),number of sides(sides) as parameter to regular polygon function.if sides &lt; 3 we cannot make a polygon so return directly.

Next angle calculation,HTML5 canvas and Javascript&nbsp;trigonometric functions will take radian &nbsp;as unit to specify angles rather than degrees.And 2*,Math.PI(Javascript notation for PI) is equal to 360 degrees.

Now moving the center to (x,y) using translate method.

Next We will move to the first point of regular polygon using moveTo() method that is nothing but (r,0) as explained above.

Loop through the sides to identify remaining two points and then close the path using closePath() .

### <strong><em><span style="text-decoration: underline;">Draw Triangle using HTML5 Canvas:-</span></em></strong>

&nbsp;

However this function will not draw anything just it will define drawing path and we have to use storke or fill method to make polygon visible. Here is the sample HTML5 Code.

<pre>&lt;html&gt;
&lt;head&gt;
&lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"&gt;&lt;/script&gt;
&lt;script&gt;
$(document).ready(function(){
	var canvas = $("#canvas")[0];
	var context = canvas.getContext("2d");
	polygon(context, 120,120,100,3);
        context.stroke();
})
function polygon(ctx, x, y, radius, sides) {
  if (sides &lt; 3) return;
  var a = ((Math.PI * 2)/sides);
  ctx.beginPath();;
  ctx.translate(x,y);
  ctx.moveTo(radius,0);
  for (var i = 1; i &lt; sides; i++) {
    ctx.lineTo(radius*Math.cos(a*i),radius*Math.sin(a*i));
  }
  ctx.closePath();
}
&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;canvas id="canvas" width="500" height="300"&gt;OOPS.. Upgrade your Browser&lt;/canvas&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

&nbsp;

This will draw the triangle exactly as shown in above figure (with radius (3,0)) But that is not visually straight because we made first point as (3,0)

To make triangle straight we have to rotate the context about 90 degrees(negative direction i.e., -Math.PI/2) so we will slightly change our method as shown below

<pre>function polygon(ctx, x, y, radius, sides, rotateAngle) {
  if (sides &lt; 3) return;
  var a = (Math.PI * 2)/sides;
  ctx.beginPath();
  ctx.translate(x,y);
  ctx.rotate(rotateAngle);
  ctx.moveTo(radius,0);
  for (var i = 1; i &lt; sides; i++) {
  ctx.lineTo(radius*Math.cos(a*i),radius*Math.sin(a*i));
  }
  ctx.closePath();
}</pre>

&nbsp;

And now below code will draw exactly straight triangle

<pre>polygon(context, 120,120,100,3,-Math.PI/2);
context.stroke()</pre>

&nbsp;

If you don’t want to rotate the triangle do not pass the last argument i.e., rotateAngle.

I hope you understand &nbsp;<em><span style="text-decoration: underline;">how to draw a regular polygon using HTML5 canvas</span></em>.

But how we can generalize these to any polygon simply follow the below steps.For instance a take pentagon which is not regular pentagon

<ul><li>&nbsp;Identify any five points on a circle.</li><li>To identify the points we have to divide 360 degrees into 5 parts which are not equal(Say 80,90,100,30,60 degrees)</li><li>These angles are nothing but angles made by the each side at center of circle.</li><li>Now we know the points draw the lines using LineTo and finally stroke it. Please look into the below code.</li></ul>

&nbsp;

### <strong><span style="text-decoration: underline;"><em>Draw Polygon using HTML5 Canvas:-</em></span></strong>

<pre>var c = canvas.getContext("2d");
c.beginPath();    
c.translate(120,120);
c.moveTo(100,0);
c.lineTo(100*Math.cos((Math.PI/180)*80),100*Math.sin((Math.PI/180)*80));
c.lineTo(100*Math.cos((Math.PI/180)*(80+90)),100*Math.sin((Math.PI/180)*(80+90)));
c.lineTo(100*Math.cos((Math.PI/180)*(80+90+100)),100*Math.sin((Math.PI/180)*(80+90+100)));
c.lineTo(100*Math.cos((Math.PI/180)*(80+90+100+30)),100*Math.sin((Math.PI/180)*(80+90+100+30)));
c.closePath();
c.stroke();</pre>

&nbsp;

For regular polygons all angles are equal so we took a for loop to identify the points but this is not the case for normal polygon so we have to add angles one by one to identify the points.

The above code looks somewhat tricky, But I feel this is the best way to identify the points of a polygon on HTML5 Canvas instead of giving points normally like c.lineTo(120,50) where we have to guess so many points to <span style="text-decoration: underline;"><em>Draw HTML5 Canvas Polygon</em></span>.

Live Demo For <a title="Html5 canvas polygon" href="https://www.arungudelli.com/Tools/HTML5/DrawHTML5CanvasPolygon.html" target="_blank" rel="noopener">HTML5 Canvas Polygon</a>

I hope you’ve enjoyed this article and that it gives you more ideas on how you can use the HTML5 Canvas API.

&nbsp;









