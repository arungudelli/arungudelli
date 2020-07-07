+++
title="Most Useful JavaScript Tips & Tricks For JavaScript Developers"
summary="Useful Tips & Tricks for JavaScript developers.These are not related to any browser these Tips & Tricks are some best practices for the JavaScript Language."
keywords=["javascript tips and tricks,top javascript tricks,javascript tips and techniques,javascript best practices,javascript best practices 2013,javascript best practices google,javascript"
]
type='post'
date='2019-10-25T18:04:11+0000'
lastmod='2019-10-25T18:04:11+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++








Here I collected some <span style="text-decoration: underline;"><em>JavaScript Tips &amp; Tricks</em></span>&nbsp;and <span style="text-decoration: underline;"><em>JavaScript Best Practices</em></span> which can be used in our daily projects or bookmark it for reference purpose.

This includes some useful <span style="text-decoration: underline;"><em>JavaScript</em></span> snippets too.

{{< figure src="javascript-tips-and-trick.jpg" title="javascript tips and tricks" alt="javascript tips and tricks" >}}

### 

These <span style="text-decoration: underline;"><em>JavaScript Tips And Tricks</em></span> are I collected from some books and Google.

### <span style="text-decoration: underline;">[] is better than “new Array();”:</span>

This is from the book “JavaScript: Good Parts”.

“A common error in JavaScript programs is to use an object when an array is required or an array when an object is required. The rule is simple: when the property names are small sequential integers, you should use an array. Otherwise, use an object.”

Instead of using

<pre>var a = new Array();
a[0] =  “1”;
a[1] = “2”;</pre>

&nbsp;

Use the below code snippet

<pre>var a = [‘1’,’2’];</pre>

&nbsp;

### <span style="text-decoration: underline;">Append an array to existing Array in JavaScript:</span>

The following JavaScript code snippet will append array ‘a’ to ‘b’. We can use&nbsp;concat() method for the same but concat() method creates new array but Array Prototype push append to existing array itself

<pre>var a = [1,2,3];
var b = [4,5,6];
Array.prototype.push.apply(a, b);
// a contains [1,2,3,4, 5, 6]</pre>

&nbsp;

### <span style="text-decoration: underline;">Check If An Object Is Array in JavaScript:</span>

In JavaScript we can use type of to check the type of a variable but we cannot use type of for array.The below JavaScript code snippet can be used for array detection.In ECMAScript 5 we can use&nbsp;Array.isArray(obj) but this ECMAScript&nbsp;not widely adopted.

<pre>if( Object.prototype.toString.call( obj ) === '[object Array]' ) {
    alert( 'Array' );
}</pre>

&nbsp;

I wrote some other code but that is not efficient as above code snippet.The concept here is the array length cannot be negative but when you are forced to do it it throws an exception.

<pre>function (obj) {
    try {
        obj.length = -1;
        return false;
    }
    catch (error) {
        return true;
    }</pre>

&nbsp;

### <span style="text-decoration: underline;">Truncate array in JavaScript:</span>

Most of them use splice or slice method to truncate but we can use JavaScript length property to do the same. And it is more efficient than slice or splice method Here is the <a title="Truncate Array" href="http://jsperf.com/the-fastest-way-to-truncate-an-array" target="_blank" rel="noopener noreferrer">performance result</a>&nbsp;. JavaScript slice or splice methods will return new array this might be the reason for the performance degradation

<pre>var array = ["1", "2", "3", "4", "5"];
array.length = 3;
// array contains [1,2,3]
var array1=array.slice(0, 3);</pre>

&nbsp;

### <span style="text-decoration: underline;">JavaScript array to CSV:</span>

To convert Java Script array to CSV format comma separated values you can use below code snippet.Use <span style="text-decoration: underline;"><em>JavaScript&nbsp;valueOf()</em></span> method for comma separated values

And if you want to use pipe instead as deliminator you can use <span style="text-decoration: underline;"><em>JavaScript&nbsp;join()</em></span> method as shown below

<pre>var numbers = ['1', '2', '3', '4']; 
var str = numbers.valueOf();  
//str: 1,2,3,4

//If you want pipe instead of comma as deliminator you can use this code
var str= numbers.join("|");</pre>

&nbsp;

If you want to convert CSV to Array use following code

<pre>var str = "1,2,3,4,5";  
var numbers = str.split(",");

//str[0]=1</pre>

&nbsp;

### <span style="text-decoration: underline;">Remove array element by Index or value in JavaScript:</span>

If you want to remove array element by Index use the below JavaScript code snippet. We can use slice() method.

<pre>function removeElementByIndex(arr, index) {
    arr.splice(index, 1);
}

test = new Array();
test[0] = '1';
test[1] = '2';
test[2] = '3';
test[3] = '4';
test[4]='5';

//before 1,2,3,4

removeElementByIndex(test, 2);

//After 1,2,4</pre>

&nbsp;

To remove element by value use the below JavaScript code snippet

<pre>function removeElementByValue(arr, val) {
    for(var i=0; i&lt;arr.length; i++) {
        if(arr[i] == val) {
            arr.splice(i, 1);
            break;
        }
    }
}</pre>

&nbsp;

### <span style="text-decoration: underline;">Capture browser close Event:</span>

To invalidate the session of an user when the user close the browser, we can use the below code snippet. &nbsp;In JavaScript we have events such as&nbsp;<strong>onbeforeunload&nbsp;</strong>and&nbsp;<strong>onunload</strong>. These events triggered whenever the page gets unload i.e., if user close the browser or move to different page.

<pre>&lt;script language="javascript"&gt;
function PageUnloadHandler() {
    alert("Do something to invalidate the sessions");
}
&lt;/script&gt;
&lt;body onbeforeunload="PageUnloadHandler()"&gt;
    &lt;!-- Body content --&gt;
&lt;/body&gt;</pre>

&nbsp;

### <span style="text-decoration: underline;">Redirect webpage in JavaScript:</span>

The below JavaScript code snippet &nbsp;used to perform http redirect on a given URL.

<pre>window.location.href = "https://arungudelli.com";</pre>

&nbsp;

### <span style="text-decoration: underline;"><span style="color: #000000; text-decoration: underline;">Declare Variables Outside of the For Statement:</span></span>

This is the most common mistake done by most of the developers observer the below code snippet

<pre>for(var i = 0; i &lt; someArray.length; i++) {  
   var container = document.getElementById('container');  
   container.innerHtml += 'my number: ' + i;  
   console.log(i);  
}</pre>

&nbsp;

In each iteration we must determine array length and also we should traverse through the DOM to find container instead of this assign array length and DOM elements to variables before for loop.So use the below JavaScript code snippet.

<pre>var container = document.getElementById('container');
var len = someArray.length;  
for(var i = 0; i &lt; len;  i++) {  
   container.innerHtml += 'my number: ' + i;  
   console.log(i);  
}</pre>

&nbsp;

### <span style="text-decoration: underline; color: #000000;">Shorten the JavaScript Code snippets:</span>

Apart from the above code snippets and <span style="text-decoration: underline;"><em>JavaScript Tips And Tricks</em></span> here are the some tips to improve the code quality.

These are all “false” in boolean expressions:

<ul><li><code>null</code></li><li><code>undefined</code></li><li><code>''</code>&nbsp;or empty string</li><li><span style="font-family: monospace;">0</span> the number</li></ul>

and below are all true:

<ul><li><code>"0"</code>&nbsp;the string</li><li><code>[]</code>&nbsp;the empty array</li><li><code>{}</code>&nbsp;the empty object</li></ul>

i.e., instead of using below code

<pre>while (x != null) {}</pre>

&nbsp;

we can use the following JavaScript code(as long as you don’t expect x to be 0, or the empty string, or false)

<pre>while (x) {}</pre>

&nbsp;

And to check the empty string or null we might be using this below code snippet

<pre>if (y != null &amp;&amp; y != '') {}</pre>







Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







