+++
title="How To Check If An Object Is Empty In JavaScript Examples"
summary="In javascript, we can check if an object is empty or not by using JSON.stringify, Object.keys (ECMA 5+),Object.entries (ECMA 7+)"
keywords="check if an object is empty in javascript,javascript"
type='post'
date='2019-11-14T18:02:45+0000'
lastmod='2019-11-14T18:02:45+0000'
draft='false'
authors=['admin']
[image]
caption='How To Check If An Object Is Empty In JavaScript Examples'
focal_point=''
preview_only=false
+++

Usually, we will return JSON data from server APIs (through AJAX). Sometimes the API might return an empty object i.e., “{}”.

In javascript, we can check if an object is empty or not by using

<ol><li>JSON.stringify</li><li>Object.keys (ECMA 5+)</li><li>Object.entries (ECMA 7+)</li></ol>

And if you are using any third party libraries like jquery, lodash, Underscore etc you can their existing methods for checking javascript empty object. I will be listing down those methods in this article with examples.

{{%toc%}}

{{< figure src="check-if-an-object-is-empty-javascript.jpg" title="check if an object is empty javascript" alt="check if an object is empty javascript" >}}

## Check if an object is empty in JavaScript using JSON.stringify:

JSON.stringify converts an object to JSON string. We can convert the javascript empty object to JSON string and check with JSON.stringify({})

<pre>function ifObjectIsEmpty(object){
   var isEmpty=true;
   if(JSON.stringify(object)==JSON.stringify({})){
     // Object is Empty
     isEmpty = true;
   }
   else{
     //Object is Not Empty
     isEmpty = false;
   }
}</pre>

Now we can pass the object to above ifObjectisEmpty method to check if an object is empty as shown below.

<pre>var emptyObject = {};
ifObjectIsEmpty(emptyObject);
true // Object is Empty</pre>

## Check if an object is empty in JavaScript using Object.keys in es5+:

In ECMAScript 5 Object.keys() method returns an array of an object’s own property names. So to check if an object is empty or not in Javascript we can check if Object.keys().length is zero or not as shown below.

<pre>var normalObject = {a:2};
Object.keys(normalObject).length
//1

var sampleObject= {};
Object.keys(sampleObject).length
//0

if(Object.keys(sampleObject).length==0){
console.log('Object is empty');
}else{
console.log('Object is not empty');
}

</pre>

## Check if an object is empty in JavaScript using Object.entries in es7+:

Object.entries() method in ECMAScript 7 returns an array of an object’s key-value pairs.

To check if an object is empty or not in javascript using Object.entries() use the below code snippet

<pre>var normalObject = {a:2};
Object.entries(normalObject).length
//["a","2"]

var sampleObject= {};
Object.entries(sampleObject).length
//0

if(Object.entries(sampleObject).length==0){
console.log('Object is empty');
}else{
console.log('Object is not empty');
}</pre>

## Checking if an object is empty or not in Javascript in older browsers:

The above methods might not work in older browsers like IE 7 and 8 (es5 or ECMAScript 5 and before). So to check if an object is empty or not in all browsers we can loop through the object properties using for as shown below

<pre>function ifObjectIsEmpty(obj) {
for(var prop in obj) {
if(obj.hasOwnProperty(prop)) {
return false;
}
}

return JSON.stringify(obj) === JSON.stringify({});
}</pre>

## Check if an object is empty in JavaScript using jQuery:

In jQuery, we can use isEmptyObject() method to check if an object is empty or not as shown below

<pre>var emptyObject = {};
if(jQuery.isEmptyObject(emptyObject)){
console.log("Javscript Object is empty");
}else{
console.log("Javscript Object is not empty");
};</pre>

## Check if an object is empty in JavaScript using extjs:

In Extjs, we can use Ext.Object.isEmpty method to check if an object is empty or not as shown below

<pre>var emptyObject = {};
if(Ext.Object.isEmpty(emptyObject)){
console.log("Javscript Object is empty");
}else{
console.log("Javscript Object is not empty");
};</pre>

## Check if an object is empty in JavaScript using lodash:

In loadash js, we can use _.isEmpty method to check if an object is empty or not as shown below

<pre>var emptyObject = {};
if(_.isEmpty(emptyObject)){
console.log("Javscript Object is empty");
}else{
console.log("Javscript Object is not empty");
};</pre>

## Check if an object is empty in Javascript using Underscore:

In Underscore js, we can use _.isEmpty method to check if an object is empty or not as shown below

<pre>var emptyObject = {};
if(_.isEmpty(emptyObject)){
console.log("Javscript Object is empty");
}else{
console.log("Javscript Object is not empty");
};</pre>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







