+++
title="Auto Resize An Image To Fit Into A HTML Div Using CSS"
summary="Auto resize an image (img) to fit into a smaller Div can be achieved through simple CSS or CSS3. In this tutorial I will explain both CSS and CSS3 ways using simple html example.Add max-width,max-height CSS as 100% for img tag,then image will be auto resized.Use CSS3 object-fit:contain to resize img to fit into div."
keywords=["css,html,auto resize image css,resize image,image fit into div"
]
type='post'
date='2019-11-03T18:03:33+0000'
lastmod='2019-11-03T18:03:33+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Auto resize an image (img) to fit into a smaller Div can be achieved through simple CSS or CSS3. In this tutorial I will explain both CSS and CSS3 ways using simple html example.

{{%toc%}}

{{< figure src="Auto-resize-image.jpeg" title="Auto resize image using css" alt="Auto resize image using css" >}}

### Auto resize image using CSS:

To auto resize image using CSS, use the below CSS code

Do not add explicit width and height to image(img) tag.

And then give <span style="text-decoration: underline;">max-width</span> and <span style="text-decoration: underline;">max-height</span> as 100%. As shown below.

<pre>img{
max-width:100%;
max-height:100%
}</pre>

For example say our image width is 100px and height is 100px.

<pre>&lt;!--Html example for Auto resize image to fit into parent div using CSS--&gt;

&lt;div class="auto-resize-portrait"&gt;
&lt;img src="auto-resize-image.png"&gt;
&lt;/div&gt;

&lt;div class="auto-resize-landscape"&gt;
&lt;img src="auto-resize-image.png"&gt;
&lt;/div&gt;

&lt;div class="auto-resize-square"&gt;
&lt;img src="auto-resize-image.png"&gt;
&lt;/div&gt;

&lt;div class="auto-resize-big"&gt;
&lt;img src="image.png"&gt;
&lt;/div&gt;</pre>

We have four divs of different sizes and width,height of divs are applied through css as shown below.

<pre>/* CSS for div elements and img tags */

img {
max-width: 100%;
max-height: 100%;
}

.auto-resize-portrait {
height: 80px;
width: 50px;
}

.auto-resize-landscape {
height: 30px;
width: 80px;
}

.auto-resize-square {
height: 75px;
width: 75px;
}

.auto-resize-big{
width:150px;
height:150px;
}</pre>

In the first div width and height of our image is auto resized to fit into 50*80px div element(Actual image size 100*100)&nbsp; i.e., image auto resized to 50*50 px

And in the second div, image auto resized to 30*30 px.

In third div i.e., div with the class .auto-resize-square the image auto resized to 75*75.

In last div we gave width and height of div element greater than that our image size, in this case the image will not be auto resized and displayed as its i.e., 100*100 px dimensions.

In the above examples Image will be fit into parent div element without scaling it. Say for example our image dimensions are 100*100 that means width to height ratio is 1:1.

In first div width is 50px and height is 80px i.e., maximum image width can be only 50px as the image width to height ration 1:1 so height is adjusted to 50px.

And in second div height is 30px and width is 80px. Maximum image height can be only 30px and width is adjusted to 30px.

In the last div i.e., div with&nbsp;.auto-resize-big class maximum available image height and width are 200px. But actual image dimensions are only 100*100px. So displayed as it is.

### Auto resize image using CSS3 (Modern Web browsers):

To auto resize image using CSS3 in modern web browsers use&nbsp;below simple one line of CSS3 code,image will be auto resized to fit into parent div element.

<pre>/* CSS3 example */

img{
height: 100%;
width: 100%;
object-fit: contain;
}</pre>

We have to give image tag width and height as 100%. And add the <span style="text-decoration: underline;">object-fit</span> property value as <span style="text-decoration: underline;">contain</span>.

But the difference is if parent div size is more than image size then image will be automatically resized to parent div element size.

In this case our image dimensions are 100*100 and div element size is 200*200. The image automatically resized to 200*200 dimensions. The clarity of the image will be reduced. See the below Demo

### Auto resize image using css Demo example:

Go through the demo and understand difference between both css and css3 way.

<a href="http://jsfiddle.net/arungudelli/v3rtxa5n/" target="_blank" rel="nofollow noopener">Auto resize image using CSS Demo</a>

{{< figure src="Auto-resize-image-css.png" title="Auto resize image using css" alt="Auto resize image using css" >}}









