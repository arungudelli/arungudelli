+++
title="Basics Of HTML5 GetUserMedia API"
summary="Capture video and audio with getUserMedia in HTML5,use HTML5's getusermedia to take snapshot.Tutorials explains HTML5's getusermedia API features with example"
keywords=["html5 getusermedia,html5 getusermedia api,html5 canvas,javascript,html5 getusermedia browser support,html5"
]
type='post'
date='2019-10-04T18:06:13+0000'
lastmod='2019-10-04T18:06:13+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

In this tutorial I will explain how to capture video and audio using <span style="text-decoration: underline;"><em>getUserMedia</em></span>&nbsp; in <span style="text-decoration: underline;"><em>HTML5</em></span> with an example.Then I will explain how to take snapshot using <span style="text-decoration: underline;"><em>HTML5 getUserMedia API</em></span>.

And Finally You will learn how to implement Google Hangout Effects using <span style="text-decoration: underline;"><em>html5 getUserMedia API</em></span>

First take a look at browser support for javascript getUserMedia API.

### <span style="text-decoration: underline;">HTML5 getUserMedia browser support:</span>

&nbsp;

Currently chrome,mozilla,opera supports getUsermedia API.

For chrome and Mozilla we have to prefix corresponding web engine i.e., for chrome we have to use <span style="text-decoration: underline;"><em>“webkitGetUserMedia”</em></span> function and for mozilla <span style="text-decoration: underline;"><em>“mozGetUserMedia”</em></span> function.

For Opera no need to add any prefix simply use “getUserMedia”.

By default getUserMedia disabled in chrome and mozilla.

### <span style="text-decoration: underline;">Enable getUserMedia in browsers:</span>

&nbsp;

To <span style="text-decoration: underline;"><em>enable getUserMedia in Chrome</em></span> type ‘chrome://flags/’&nbsp;in URL bar&nbsp;and enable “Enable screen capture support in getUserMedia().&nbsp;Mac, Windows, Linux, Chrome OS” option.

To <span style="text-decoration: underline;"><em>enable getUserMedia in Mozilla</em></span> type ‘about:config’ in URL bar search for&nbsp;“media.navigator.enabled” and set it True.

Safari and InternetExplorer does not support getUserMedia.

For more information check <a title="getUserMediabrowser support" href="http://html5test.com/compare/feature/device-getUserMedia.html" target="_blank" rel="nofollow noopener">getUserMedia Browser Support</a>

### <span style="text-decoration: underline;">getUserMedia Example:</span>

One important thing you should remember is

You cannot use&nbsp;<code>getUserMedia</code>&nbsp;on web pages served using&nbsp;<code>file://</code>&nbsp;URLs.

So host your HTML file in Apache or IIS , then browse better use Visual Studio.

Here is the sample HTML file

<pre>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="utf-8"&gt;
  &lt;title&gt;HTML5 getUserMedia Demo By Arunkumar Gudelli&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div id="video"&gt;
    &lt;video id="webcam" width="500" autoplay&gt;&lt;/video&gt;
  &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

&nbsp;

And next we will write javascript code. Instead of if else loops to support different browser we will define <span style="text-decoration: underline;"><em>navigator.getUserMedia</em></span> as shown below.

<pre>jQuery(document).ready(function () {
           navigator.getUserMedia = (navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia ||
                            navigator.msGetUserMedia);
});</pre>

&nbsp;

Now we will understand <span style="text-decoration: underline;"><em>HTML5 getUserMedia</em></span> function it will take three arguments like <span style="text-decoration: underline;"><em>constraints,successCallback,FailureCallback</em></span>. The syntax is shown below.

<pre>navigator.getUserMedia ( constraints, successCallback, errorCallback );</pre>

### <span style="text-decoration: underline;">constraints:</span>

getUserMedia constraints are nothing but which media streams to use i.e., audio or video.And it is required field

<pre>{ video: true, audio: true }</pre>

### <span style="text-decoration: underline;">successCallback:</span>

successcallback is the function we call when media stream is loaded successfully in our case put it into video tag.success callback is required field.

The getUserMedia function will call the function specified in the successCallback with the&nbsp;<a title="WebRTC/MediaStream_API#LocalMediaStream" href="https://developer.mozilla.org/en-US/docs/WebRTC/MediaStream_API#LocalMediaStream" rel="nofollow">LocalMediaStream</a>&nbsp;object that contains the media stream.

<pre>function(localMediaStream) {
   var video = document.querySelector('video');
   video.src = window.URL.createObjectURL(localMediaStream);
}</pre>

<ul><li>First we are getting video element using <span style="text-decoration: underline;"><em>document.querySelector()</em></span></li><li>And Then creating a object URL for the localMediaStream provided by the getUserMedia using <span style="text-decoration: underline;"><em>window.URL.createObjectURL</em></span></li><li>Finally use this URL for the source of Video element.</li></ul>

### <span style="text-decoration: underline;">errorCallback:</span>

Failure callback is the function we call when media stream cannot be loaded.The function called with different types of code arguments as mentioned below.And it is optional however in mozilla it’s required field.

<div class='table-responsive'><table class='table'><thead><tr><th scope="col">Error</th><th scope="col">Description</th></tr></thead><tbody><tr><td>PERMISSION_DENIED</td><td>The user denied permission to use a media device required for the operation.</td></tr><tr><td>NOT_SUPPORTED_ERROR</td><td>A constraint specified is not supported by the browser.</td></tr><tr><td>MANDATORY_UNSATISFIED_ERROR</td><td>No media tracks of the type specified in the constraints are found.</td></tr></tbody></table></div>

&nbsp;

Sample errorCallback function

<pre>function onFailure(err) {
            alert("The following error occurred:"+err.name);
        }</pre>

&nbsp;

err.name will display the corresponding error codes

And here is the Final Code. Load your document (remember host it on apache or IIS) and grant permission.

<pre>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="utf-8"&gt;
  &lt;title&gt;HTML5 getUserMedia Demo By Arunkumar Gudelli&lt;/title&gt;
  &lt;script src="https://code.jquery.com/jquery-1.10.2.min.js" type="text/javascript"&gt;&lt;/script&gt;
  &lt;script&gt;
      function onFailure(err) {
          alert("The following error occured: " + err.name);
      }
      jQuery(document).ready(function () {
          var video = document.querySelector('#webcam');
          navigator.getUserMedia = (navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia ||
                            navigator.msGetUserMedia);
          if (navigator.getUserMedia) {
              navigator.getUserMedia
                            (
                              { video: true },
                              function (localMediaStream) {
                                  video.src = window.URL.createObjectURL(localMediaStream);

                              }, onFailure);
          }
          else {
              alert('OOPS No browser Support');
          }
      });
  &lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div&gt;
    &lt;video id="webcam" width="500" autoplay&gt;&lt;/video&gt;
  &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

&nbsp;

And Next step we will take snapshot and display it into <span style="text-decoration: underline;"><em>HTML5 Canvas</em></span> element.

Add Canvas tag and Capture Button to our HTML Code.

<pre>&lt;canvas id="screenshot-canvas"&gt;&lt;/canvas&gt;
&lt;button id="screenshot-button"&gt;Capture&lt;/button&gt;</pre>

&nbsp;

And then add javaScript code

<pre>var button = document.querySelector('#screenshot-button');
var canvas = document.querySelector('#screenshot-canvas');
var ctx = canvas.getContext('2d');

button.addEventListener('click',snapshot, false);

function snapshot() {
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
ctx.drawImage(video, 0, 0);
}</pre>

&nbsp;

I added snapshot() method

<ul><li>Canvas width and height we are assigning to video element width and height</li><li>And then We are drawing Image on canvas using drawImage() function which takes argument video element and X,Y Coordinate position.</li><li>And Finally we added this method to capture button click event.</li></ul>

{{< figure src="HTML5getUserMediaDemo.jpg" title="HTML5 getUserMedia Demo" alt="HTML5 getUserMedia Demo" >}}

Here is the <a title="HTML5 getUserMedia Snapshot" href="https://www.arungudelli.com/Tools/HTML5/GoogleEffects/ScreenShot.htm" target="_blank" rel="noopener">Final Demo.</a>

Actually I tried to implement Google Hangout effects using HTML5 Canvas and getUserMedia, so in this post I tried to cover all basics of &nbsp;HTML5 getUserMedia.

Go through this awesome article &nbsp;<a title="Google Effects" href="https://www.arungudelli.com/2013/09/google-hangout-effects-using-html5-and-javascript-facedetection.html" target="_blank" rel="noopener">Learn how to implement Google Hangout effects</a>

{{< figure src="GoogleEffects.jpg" title="Google Effects" alt="Google Effects" >}}

I hope you’ve enjoyed this article and that it gives you more ideas on <span style="text-decoration: underline;"><em>HTML5 getUserMedia API</em></span>&nbsp;.

If so share this post with your friends and also join our mailing list I will be sharing my learnings and experiments with HTML5

NOTE: <em>getUserMedia</em> has been removed from the Web standards.

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







