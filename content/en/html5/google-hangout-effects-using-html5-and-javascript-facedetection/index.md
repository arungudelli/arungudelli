+++
title="Google Hangout Effects Using HTML5 And JavaScript Facedetection"
summary="Face detection using javascript and HTML5 Canvas with an awesome Google hangout effects example.Face detection application like in Picassa and IPhoto."
keywords=["google hangout effects,js face recognition,facedetection with javascript,javascript face recognition,face detection using html5,face detection using php,,html5"
]
type='post'
date='2019-10-05T18:06:08+0000'
lastmod='2019-10-05T18:06:08+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Google hangouts very popular because of <span style="text-decoration: underline;"><em>Google effects</em></span> like face masks and background effects.

I tried to implement Google Effects using <span style="text-decoration: underline;"><em>HTML5 Canvas</em></span>,<span style="text-decoration: underline;"><em>HTML5 getUserMedia API</em></span> via JavaScript face detection library by &nbsp;Liuliu.

To simplify I divided this tutorial into two parts First <a title="get user media" href="https://www.arungudelli.com/2013/09/html5-getusermedia.html" target="_blank" rel="noopener">getUserMedia basics</a> and Second Face detection &amp; Google Effects.

Please go through the <a title="getUsermedia Basics" href="https://www.arungudelli.com/2013/09/html5-getusermedia.html" target="_blank" rel="noopener">getUserMedia basics</a> then you will understand the logic clearly.

Continuous to the previous post, we learnt how to take a snapshot using <span style="text-decoration: underline;"><em>getUsermedia</em></span> and Canvas. Here is the <a title="HTML5 getUsermedia Snapshot" href="https://www.arungudelli.com/Tools/HTML5/GoogleEffects/ScreenShot.htm" target="_blank" rel="noopener">Demo</a>

<pre>button.addEventListener('click',snapshot, false);

function snapshot() {
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
ctx.drawImage(video, 0, 0);
}</pre>

&nbsp;

Just remove capture button and replace onclick event with setInterval Method as shown below

<pre>setInterval(snapshot, 30);</pre>

&nbsp;

The Logic is simple I am injecting local media stream video into HTML5 Canvas.For every 30msec one latest image snapshot will be drawn on the canvas. As the Time Interval is very less both video and canvas look like exactly same. Here is the <a href="https://www.arungudelli.com/Tools/HTML5/GoogleEffects/FaceDemo.htm" target="_blank" rel="noopener">Demo</a>.

Now we will understand face detection JavaScript by LiuLiu. The library contains two js file ccv.js and face.js.







### 

I Added some CSS code to style our Google Effects page.Here is the Final HTML Code.

<pre>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;title&gt;Google Effects By By Arunkumar Gudelli&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-1.10.2.min.js" type="text/javascript"&gt;&lt;/script&gt;
    &lt;script src="ccv.js" type="text/javascript"&gt;&lt;/script&gt;
    &lt;script src="face.js" type="text/javascript"&gt;&lt;/script&gt;
    &lt;script&gt;

        var MaskImage = new Image();

        function selectmask(source) {
            console.log(source);
            MaskImage.src = source + ".png";
        }

        function onFailure(err) {
            alert("The following error occured: " + err.name);
        }

        jQuery(document).ready(function () {

            var video = document.querySelector('#webcam');
            var button = document.querySelector('#screenshot-button');
            var canvas = document.querySelector('#screenshot-canvas');
            var ctx = canvas.getContext('2d');

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
                onFailure();
            }
            //button.addEventListener('click', snapshot, false);
            setInterval(snapshot, 30);
            function snapshot() {
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                ctx.drawImage(video, 0, 0);
                var position = ccv.detect_objects({ "canvas": canvas,
                    "cascade": cascade,
                    "interval": 2,
                    "min_neighbors": 1
                });
                for (var i = 0; i &lt; position.length; i++) {
                    ctx.drawImage(MaskImage, position[i].x - 90, position[i].y - 150, position[i].width + 200, position[i].height + 200);
                }
            }
        });

    &lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div align="center" class="normaldiv"&gt;
        &lt;div style="width: 90%" class="normaldiv"&gt;
            &lt;div style="float: left;"&gt;
                &lt;h3&gt;
                    &lt;img src="GoogleEffects.png" alt="GoogleEffects" /&gt;
                    Google Effects By Arunkumar Gudelli&lt;/h3&gt;
            &lt;/div&gt;
            &lt;div&gt;
                &lt;p&gt;
                    &lt;input id="GlassesWithMask" onclick="selectmask(this.id)" type="button" style="background: url(glassesIcon.png);
                        background-repeat: no-repeat; width: 110px; height: 110px; cursor: pointer" /&gt;
                    &lt;input id="BatMan" onclick="selectmask(this.id)" type="button" style="background: url(batmanIcon.png);
                        background-repeat: no-repeat; width: 110px; height: 110px; cursor: pointer" /&gt;
&lt;input id="PirateCaptain" onclick="selectmask(this.id)" type="button" style="background: url(PirateCaptainIcon.png);
                        background-repeat: no-repeat; width: 110px; height: 110px; cursor: pointer" /&gt;

                &lt;/p&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;video id="webcam" autoplay&gt;
        &lt;/video&gt;
        &lt;canvas id="screenshot-canvas"&gt;
        &lt;/canvas&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

&nbsp;

Here is the Final <a title="Google Effects" href="https://www.arungudelli.com/Tools/HTML5/GoogleEffects/GoogleEffects.htm" target="_blank" rel="noopener">Google Effects Demo.</a>

You have to enable <span style="text-decoration: underline;"><em>getUserMedia</em></span> in your browser. That I explained in <a title="get User Media" href="https://www.arungudelli.com/2013/09/html5-getusermedia.html" target="_blank" rel="noopener">previous post</a> If you have any queries feel free to comment.

Remember getUserMedia does’not work on file:// URL you have host html in IIS or Apache.Use Chrome or Mozilla or Opera

<span style="text-decoration: underline;"><strong>NOTE:</strong></span>

It’s not perfect. Keep Your Face straight and Close to Webcam(with Clean Background) and Remove your Eye Glasses if you have.

And <span style="text-decoration: underline;"><em>Your suggestions are always welcome</em></span> Please Add your valuable feedback to improve this App.

{{< figure src="GoogleEffectsDemo.jpg" title="GoogleEffectsDemo" alt="GoogleEffectsDemo" >}}

I hope you’ve enjoyed this article and that it gives you more ideas <span style="text-decoration: underline;"><em>face detection</em></span> and <span style="text-decoration: underline;"><em>getUserMedia API</em></span>.If so share this post with your friends and also join our mailing list I will be sharing my learning’s and experiments with HTML5.

NOTE: <em>getUserMedia</em> has been removed from the Web standards.









