+++
title="Javascript Encrypted Media Extensions API (HTML5) Is Now Official W3C Recommendation"
summary="HTML5 Encrypted Media Extensions (EME) an API used to play digital Rights Management (DRM) content (encrypted video or audio) on web applications. It is in"
keywords="html5"
type='post'
date='2019-10-29T18:03:52+0000'
lastmod='2019-10-29T18:03:52+0000'
draft='false'
authors=['admin']
[image]
caption='Javascript Encrypted Media Extensions API (HTML5) Is Now Official W3C Recommendation'
focal_point=''
preview_only=false
+++


HTML5 Encrypted Media Extensions (EME) an API used to play digital Rights Management (DRM) content (encrypted video or audio) on web applications.

It is in draft&nbsp;state from last few years and today its officially approved by W3C. (58.4 percent of W3C members voted in support &nbsp;and 30.8 percent to opposed, with 10.8 percent abstaining).

But it triggered controversy EFF resigned from W3C after this decision.

&nbsp;

### <span style="text-decoration: underline;">Why HTML5 based DRM?</span>

&nbsp;

The existing DRM schemes such as Google Widevine, Adobe PrimeTime, and Microsoft PlayReady are working very well, and very effective in protecting content but they are proprietary and comes with couple of restrictions.

But for the past few years, JavaScript is becoming very powerful and playing a key role in web development.

Now with the&nbsp;use of Html5 Media Source Extensions, and Encrypted Media Extensions Apis customers can define their own set of rules and they can easily change between schemes.

Apple developed it’s own DRM scheme fairplay using EME and MSE which protects content served by AppleTV.

&nbsp;

### <span style="text-decoration: underline;">Encrypted media extension API:</span>

&nbsp;

It’s an extension to Htmlmediaelement so its called extension API.

When the browser tries to play encrypted content it recognizes and fires an encrypted event with metadata (initData) obtained from the content.

If no MediaKeys object has been attached with the media element, then it first selects an available Key System by using <em>navigator.requestMediaKeySystemAccess() &nbsp;</em>then create a MediaKeys object using <em>MediaKeySystemAccessobject</em>.

And after that we have to assign the key to HtmlMediaelement (audio or video) using

<pre>&nbsp;<span class="javascript">var sysaccessobject= navigator.requestMediaKeySystemAccess(<span class="hljs-string">'org.w3.clearkey'</span>, [
        { <span class="hljs-attr">initDataTypes</span>: [<span class="hljs-string">'webm'</span>],
          <span class="hljs-attr">videoCapabilities</span>: [{ <span class="hljs-attr">contentType</span>: <span class="hljs-string">'video/webm; codecs="vp8"'</span> }] }
      ]);
var mediaKey=sysaccessobject.</span><span class="javascript">createMediaKeys();
</span><span class="javascript">video.setMediaKeys(mediaKey);
</span><span class="javascript"><span class="hljs-keyword">var</span> te = <span class="hljs-keyword">new</span> TextEncoder();
//using plain text
<span class="hljs-keyword">var</span> initData = te.encode( <span class="hljs-string">'{"kids":["LwVHf8JLtPrv2GUXFW2v_A"]}'</span>);
<span class="hljs-keyword">var</span> keySession = mediaKey.createSession();
keySession.addEventListener(<span class="hljs-string">"message"</span>, handleMessage, <span class="hljs-literal">false</span>);
//Returns new Key
<span class="hljs-keyword">//return</span> keySession.generateRequest(<span class="hljs-string">'keyids'</span>, initData);
</span><span class="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleMessage</span>(<span class="hljs-params">event</span>) </span>{
    <span class="hljs-keyword">var</span> keySession = event.target;
    <span class="hljs-keyword">var</span> te = <span class="hljs-keyword">new</span> TextEncoder();
    <span class="hljs-keyword">var</span> license = te.encode(<span class="hljs-string">'{"keys":[{"kty":"oct","k":"tQ0bJVWb6b0KPL6KtZIy_A","kid":"LwVHf8JLtPrv2GUXFW2v_A"}],"type":"temporary"}'</span>);
    keySession.update(license).catch(
      <span class="hljs-built_in">console</span>.error.bind(<span class="hljs-built_in">console</span>, <span class="hljs-string">'update() failed'</span>)
    );
  }</span></pre>

Now by calling, <em>createSession()</em> on the created MediaKey will create a <em>MediaKeySession object</em>, which represents the lifetime of a license and its key(s).

MediaKeySession call generateRequest() method to get license key from license server

And after receiving the response from the server&nbsp;MediaKeySession object updates the license key using update() method.

And it its valid media playback resumes.

This example I took it from W3C <a href="https://www.w3.org/TR/encrypted-media/" target="_blank" rel="noopener">documentation&nbsp;</a>

{{< figure src="ExtensionMediaAPI.png" title="ExtensionMediaAPI" alt="ExtensionMediaAPI" >}}

&nbsp;

You can read more about&nbsp;Encrypted media extension API in w3c specification.

&nbsp;

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







