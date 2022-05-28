+++
title="Get Query String Parameter Values From URL Using JavaScript"
summary="We can get Javascript query string URL parameters by using JavaScript split, ECMAScript 6 split, reduce or JavaScript URLSearchParams. To get javascript url parameter values by name use a regular expression."
subtitle="Learn how to Get Query String Parameter Values From URL Using JavaScript"
keywords=["javascipt,query string parameter in javascript,urlsearchparams in javascript,javascript"
]
type='post'
date='2019-11-04T18:03:29+0000'
lastmod='2019-11-04T18:03:29+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

We can get query string parameters in JavaScript without using 3rd party js like jQuery etc by using

<ol><li>Simple JavaScript code</li><li>ECMAScript 6</li><li>JavaScript URLSearchParams API</li></ol>

Javascript Query string URL parameters are very useful while doing CRUD operations on the server side.&amp; from client side also we might need to get query string parameters from URL using JavaScript &amp; modify them.

{{%toc%}}

## Using JavaScript split() & regex.exec() method

To get query string parameters in JavaScript,use JavaScript <em>split()</em> function.Further using JavaScript regular expression we can get parameters in key value pair.

Take an example of sample url `https://www.arungudelli.com?param1=1&param2=2` the query string parameters in the given url are `param1=1&param2=2`

```
var url ="https://www.arungudelli.com?param1=1&param2=2";
var query_string_paramter = url.split("?")[1];
//returns&nbsp;param1=1&amp;param2=2, removing ?
```

Now we will use the regular expression to match pattern (“a=b”) and return paramters in json key value pair.

```
{param1:1,param2:2}
```

And if you are not passing URL parameter, it will take the current url from `window.location` and `window.location.search` will return query string parameter.

Full code snippet is as follows

```
/** 
 * This function getQueryStringParameters takes url as parmater
 * and returns 
 * parameters name and value in JSON key value format
 * @parameter {String} url 
 * (if url is not passed it takes the current url 
 * from window.location.href) 
 *
 **/
function getQueryStringParameters(url){

 var urlParams={},
 match,
 additional = /\+/g, 
 // Regex for replacing additional symbol with a space
 search = /([^&amp;=]+)=?([^&amp;]*)/g,
 decode = 
 function (s) 
 { return decodeURIComponent(s.replace(additional, " ")); },
 query;
 if (url){
    if(url.split("?").length&gt;0){
    query = url.split("?")[1];
 }
 }else{
    url = window.location.href;
    query = window.location.search.substring(1);
 }
 while (match = search.exec(query)){
   urlParams[decode(match[1])] = decode(match[2]);
 }
 return urlParams;
}
```

## using Javascript Split & reduce method methods

In JavsScript,to get the query string parameters in JSON format use the following ES6(ECMAScript 6) Code snippet

```

/** 
* This ES6(ECMAScript) function getQueryStringParameters takes url 
* as parmater and returns
* parameters name and value in JSON key value format 
* @parameter {String} url 
* (if url is not passed it takes the current url 
* from window.location.href) 
* 
**/
const getQueryStringParameters = url => {

    if (url){
      if(url.split("?").length>0){
      query = url.split("?")[1];
    }
    }else{
       url = window.location.href;
       query = window.location.search.substring(1);
    }
    return (/^[?#]/.test(query) ? query.slice(1) : query)
    .split('&')
    .reduce((params, param) => 
{
  let [ key, value ] = param.split('=');
  params[key] = value?decodeURIComponent(value.replace(/\+/g, ' ')):'';
  return params;
}, { });
};

```
{{< figure src="Get-query-string-1.png" title="Get query string parameters JavaScript" alt="Get query string parameters JavaScript" >}}

## Using JavaScript URLSearchParams API

To get query string parameter values in JavaScript, We can use <em>UrlSearchParmas</em> API in JavaScript.

The string parsing mechanism is ugly and old way of doing getting query string parameter values.

If you are using latest browsers like&nbsp;Firefox 44+, Opera 36+, Edge 17+, Safari 10.3+ and Chrome 49+ you can use&nbsp;<code>UrlSearchParams</code> API in Javascript.

Use the following code snippet to get query string parameters from current URL

```
/* This URLSearchParams takes the query string as parameter */ 
var parameters = new URLSearchParams(window.location.search);
```

For example, if the current url is 

```
https://www.arungudelli.com?param1=1&param2=2
```

Now you can get parameter values by name using `get(key)` method of `URLSearchParams` API.

```
parameters.get('param1') //1
parameters.get('param2') //2
```

Or we can get parameters object by using `searchParams` property of URL object.

```
var parameters = new URL(window.location).searchParams;
parameters.get('param1') //1
parameters.get('param2') //2
```

If you want to get query string parameter for any url, Use the following JavaScript code snippet

```
var url =  new URL('https://www.arungudelli.com?param1=1&param2=2');
var parameters = new URLSearchParams(url.search);
// or by using searchParams property
var parameters = url.searchParams; 

parameters.get('param1') //1 
parameters.get('param2') //2
```

Apart from get(key) method UrlSearchParams also have methods like has(key) , getAll(key) , append(key,value), toString().

```
console.log(parameters.has('param1')); // true
console.log(parameters.get('param1')); // "1"
console.log(parameters.getAll('param1')); // ["1"]
console.log(parameters.toString()); // "param1=1&amp;param2=2"
console.log(parameters.append('param3', '3')); 
// "?param1=1&amp;param2=2&amp;param3=3"
```

And we can loop through parameter keys using <code>keys()</code> method , values using <code>values()</code> method and key values using <code>entries()</code> method

```
var keys = parameters.keys();
for(key of keys) { 
console.log(key); 
}
// param1
// param2

for(val of parameters.values()){console.log(val)}
//1
//2

var entries =parameters.entries();
for(pair of entries) { console.log(pair ); } 
//["param1", "1"] 
//["param2", "2"]
```

## Get URL parameter values by name in JavaScript

To get URL parameter values by name in JavaScript, use the following code snippet.

```
/** 
 * This function JavascriptgetURLParameterValues 
 * takes parameter name and url 
 * as parmaters and returns parameter value 
 * @parameter {String} parameterName
 * @parameter {String} url
 * (if url is not passed it takes the current url 
 * from window.location.href)
 **/

function JavascriptgetURLParameterValues(parameterName, url) {
 if (!url) url = window.location.href;
 parameterName= parameterName.replace(/[\[\]]/g, "\\$&amp;");
 var regularExpression = 
 new RegExp("[?&amp;]" + parameterName + "(=([^&amp;#]*)|&amp;|#|$)"),
 results = regularExpression.exec(url);
 if (!results) return null;
 if (!results[2]) return '';
 return decodeURIComponent(results[2].replace(/\+/g, " "));
}
```

Now we can pass the parameter name to the above method to get URL parameter values.

```
var url =
'https://www.arungudelli.com?parameter1=1&parameter=2&&parameter=2';
JavascriptgetURLParameterValues("parameter1");//1
JavascriptgetURLParameterValues("parameter2");//2
JavascriptgetURLParameterValues("parameter3");//3
```

With the above function, you can get individual URL parameter values by passing the parameter name and URL. If you have any other snippets please do share

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







