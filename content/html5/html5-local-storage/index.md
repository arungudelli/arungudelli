+++
title="HTML5 Local Storage API Tutorial With Examples"
summary="Local Storage HTML5 API is a better Storage than cookies. it's often as Web Storage.With Local storage API in HTML5 web pages can store data locally in browser."
keywords="html5 local storage,html5,html4 web storage,html5 local storage tutorial,web development,websorage api"
type='post'
date='2019-09-11T18:08:03+0000'
lastmod='2019-09-11T18:08:03+0000'
draft='false'
authors=['admin']
[image]
caption='HTML5 Local Storage API Tutorial With Examples'
focal_point=''
preview_only=false
+++


In this <span style="text-decoration: underline;"><em>Tutorial</em></span> I will explain all the Basics of <span style="text-decoration: underline;"><em>HTML5 Local Storage API</em></span>.

It’s often referred as <span style="text-decoration: underline;"><em>Web Storage</em></span>. Web storage is nothing but client side storage.Right now we are using cookies for the purpose of storing objects locally in client machine(in browser).

There is a big debate happening around cookie vs Local Storage I don’t want to get into that but I will start with Cookie basics, limitations of cookies and then <span style="text-decoration: underline;"><em>Html5 Local Storage</em></span>

### <span style="text-decoration: underline;">Why Cookie?</span>

Cookies are mainly used in Shopping carts to customize the user experience by storing data locally(user specific).I will explain how cookie works in high level.

<ul><li>Your playing a game in online,to maintain your state of game server will store cookies in your browser.</li><li>If you close the browser and try to access the same website then browser will send cookie along with HTTP request.</li><li>Based on Cookie,server customize the user experience and&nbsp;retrieve&nbsp;the state of a game</li><li>And Cookies are Domain Specific i.e., abc.com cannot access cookie of xyz.com.</li></ul>



### <span style="text-decoration: underline;">Limitations of Cookies :-</span>

<ul><li>Cookies can able to store only 4k of data. For each domain browser will assign 4k of memory.</li><li>Each time browser has to send cookie along with HTTP request,it’s inefficient especially if you are using mobile device with not a lot of bandwidth</li><li>Difficult to handle(I mean coding) cookie key value pairs within a HTTP request.</li><li>Each time we are sending cookie along with http request,Are we sending our personal data?</li><li>Finally everything is handle at server side,there is no client side development.</li></ul>

### <span style="text-decoration: underline;">Introduction to HTML5 Local Storage:-</span>

In HTML5 there is no concept of Cookies everything can be done by <span style="text-decoration: underline;"><em>Local Storage API</em></span>.A simple JavaScript API in the browser for storing Key value pairs that are persistent and you are not limited to 4k of memory.

{{< figure src="localstorage-feature.jpg" title="Html5 Local Storage" alt="Html5 Local Storage" >}}

### <span style="text-decoration: underline;">HTML5 Local Storage browser support:</span>

Almost All browsers are supports HTML5 Local storage. I checked the <span style="text-decoration: underline;"><em>Local storage API</em></span> browser&nbsp;compatibility&nbsp; in <a title="Html5 test" href="http://html5test.com" target="_blank" rel="nofollow noopener">HTML5test.com</a> Here is the &nbsp;result &nbsp; <a title="Html5 local storage API" href="http://html5test.com/compare/feature/storage-localStorage.html" target="_blank" rel="nofollow noopener">click here</a>.

Internet explorer 6,7 ,Opera 10 ,Firefox 3.0 are not supporting this <span style="text-decoration: underline;"><em>HTML5 local storage</em></span> API anyway we are not using these browsers now a days

### <span style="text-decoration: underline;">HTML5 Local Storage limit:</span>

All browsers today offering 5-10 MB of storage in every user’s browser.i.e., For each domain 5MB of local storage.

HTML5 local storage supports different web apps and mobile apps.Local storage is nothing but your app can store data in browser <em>to reduce communication needed with the server.</em>

A page can store one or more key/value pairs in the browser’s local storage.And later use key to&nbsp;retrieve value.&nbsp;These can be done by <span style="text-decoration: underline;"><em>Local Storage</em></span> object in local storage API.

You may thing why Local Storage why not Web Storage,Web refers to something more and we are implementing at client side,local make sense instead of Web.

### <span style="text-decoration: underline;">Html5 Local Storage Example:-</span>

Before going to example first we will understand basic functions of html5 local storage. With “localstorage” object we can create a key using ‘<span style="text-decoration: underline;"><em>setItem</em></span>‘ method.And to retrieve value use ‘<span style="text-decoration: underline;"><em>getItem</em></span>‘ method.

<pre>localstorage.setItem("key1","value1"); 
var value=localstorage.getItem("key1");
alert(value);</pre>

&nbsp;

Most of the browsers support local storage object but safer side you can check browser&nbsp;compatibility as shown below

<pre>if (window["localStorage"]) { // your localStorage code here... }</pre>

&nbsp;

And also keys are unique for example<span style="line-height: 125%; background-color: white; color: black;">&nbsp;</span>

<pre>local.storage.setItem("key1","value1");
 local.storage.setItem("key1","value2");
var value = localstorage.getItem("key1");
 alert(value);</pre>

&nbsp;

Now value contain value2 not value1. And one thing <span style="text-decoration: underline;"><em>Local Storage</em></span> stores only string values.But in Shopping cart if we want to store item counts and prices in Local Storage you need to use parsing.

<pre>localStorage.setItem("numitems", 1);
var numItems = localStorage.getItem("numitems");
var numItems = parseInt(localStorage.getItem("numitems")); 
numItems = numItems + 1; 
localStorage.setItem("numitems", numItems);
 localStorage.setItem("price", 9.99);
 var price = parseFloat(localStorage.getItem("price"));</pre>

&nbsp;

### <span style="text-decoration: underline;">Html5 Local Storage Array:-</span>

Instead of using setItem and getItem methods we can use arrays as shown below

<pre>localStorage["key1"]="value1";
 var value=localStorage["key1"];</pre>

&nbsp;

And <span style="text-decoration: underline;"><em>Local Storage</em></span> has two interesting things :<em>Length </em>property and <em>Key&nbsp;</em>method.Length property holds number of items in the local store.And get can be used to&nbsp;retrieve value as shown below

for (var i = 0; i &lt; localStorage.length; i++) {<br>
var key = localStorage.key(i);<br>
var value = localStorage[key];<br>
alert(value);<br>
}

or you can use foreach loop as shown below

for (var key in localStorage) {<br>
var value = localStorage[key];alert(value); }

And you can remove keys from Local Storage using removeItem method:&nbsp;localStorage.removeItem(key);

### <span style="text-decoration: underline;">Html5 Session Storage:-</span>

If you substitute the global variable&nbsp;sessionStorage everywhere you’ve used&nbsp;<span style="text-decoration: underline;"><em>localStorage</em></span> then your items are stored only during&nbsp;the browser session. So, as soon as that session is over&nbsp;(in other words, the user closes the browser window),&nbsp;the items in storage are removed.The sessionStorage object supports exactly the&nbsp;same API as Local Storage.

### <span style="text-decoration: underline;">Where we can see Local Storage keys and Values:-</span>

<a href="https://arun-arungudellicom.netdna-ssl.com/wp-content/uploads/2012/10/LocalStorageinChrome.png"><img class="alignleft size-medium wp-image-352" title="LocalStorageinChrome" src="https://arun-arungudellicom.netdna-ssl.com/wp-content/uploads/2012/10/LocalStorageinChrome-300x224.png" alt="LocalStorageinChrome" width="300" height="224" srcset="https://arun-arungudellicom.netdna-ssl.com/wp-content/uploads/2012/10/LocalStorageinChrome-300x224.png 300w, https://arun-arungudellicom.netdna-ssl.com/wp-content/uploads/2012/10/LocalStorageinChrome.png 334w" sizes="(max-width: 300px) 100vw, 300px"></a>And we can see the <span style="text-decoration: underline;"><em>local storage</em></span> key values in browsers using developer tools as shown in the pic.In developer tools select resources and Local Storage. you can select key and delete from browser itself instead of using local storage removeItem method.

To clear entire local storage you can use

localStorage.clear();

But how to use this clear method you need to create one sample HTML page.No need to bother download this <a href="https://www.arungudelli.com/Tools/HTML5/ClearStorage.html" target="_blank" rel="noopener">ClearWebStorage.html</a> file and click on clear button it will clear the total localStorage elements.

&nbsp;

### <span style="text-decoration: underline;">What happens if 5MB storage exceeds:-</span>

If 5MB storage exceeds browser should throw&nbsp;QUOTA_EXCEEDED_ERR exception.Most of the modern browsers will throw this exception.And remember don’t forgot to use try,catch loops.If you are not using it may crash the browser if it exceeds 5mb storage.Do you want to test this? download this <a href="https://www.arungudelli.com/Tools/HTML5/BlowUpStorage.html" target="_blank" rel="noopener">BlowUpStorage.html</a> file and test.

### <span style="text-decoration: underline;">Important things to remember while using Local Storage API:-</span>



I hope you understood the basics of HTML5 Local Storage API in this Tutorial.

You might Like

<a title="Html5 basics" href="https://www.arungudelli.com/2012/08/beginning-html5.html" target="_blank" rel="noopener">Beginning Html5</a>

<a title="What is HTML5" href="https://www.arungudelli.com/2012/08/a-new-era-of-web-development-html5.html" target="_blank" rel="noopener">A new era in web development </a>

<a title="Html5 canvas tutorial" href="https://www.arungudelli.com/2012/10/html5-canvas-example-snake-game.html" target="_blank" rel="noopener">Html5 canvas tutorial</a>

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.









