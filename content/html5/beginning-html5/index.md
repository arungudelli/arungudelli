+++
title="Beginning HTML5"
summary="This tutorial help you to understand the Syntax of HTML5 Look at the below sample html code Doctype: type of the document we are loading in this case HTML"
keywords="html5"
type='post'
date='2019-08-27T18:08:54+0000'
lastmod='2019-08-27T18:08:54+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

This tutorial help you to understand the Syntax of HTML5
 Look at the below sample html code

```
<!DOCTYPE html PUBLIC “-//W3C//DTD HTML 4.01//EN”“http://www.w3.org/TR/html4/strict.dtd”>
<html>
<head>
<meta http-equiv=“content-type” content=“text/html; charset=UTF-8”>
<title>Arunkumar ‘s blog</title>
<link type=“text/css” rel=“stylesheet” href=“example.css”>
<script type=“text/javascript” src=” example.js”></script>
</head>
<body>
<h1>Welcome to My blog</h1>
<p>Join my site to know about Web. </p>
</body>
</html>
```
```
<!DOCTYPE html PUBLIC “-//W3C//DTD HTML 4.01//EN”
“http://www.w3.org/TR/html4/strict.dtd”>
```

Doctype: type of the document we are loading in this case HTML
Public: it tells that standard is publicly available

 
HTML4.0:Tells the version of the HTML and this mark up is written in english
W3c.com/strict.dtd:This url points to the file that identify this standard

And now what is the new Doctype for HTML5 you may think just replace html4.0 with html 5.0

No your wrong New doctype is simply

```
<!doctype html>
```

Simple and easy.No need to write complex doctype from now on wards. You may think why they removed dtd also.I will come to that point mean while we will see other changes

```
<meta http-equiv=”content-type” content=”text/html; charset=UTF-8″> 
```
Old one

And the new one is
```
<meta charset=”utf-8″>
```
Much simpler than earlier. And All browsers including old browsers already understand this and you can use it any page it will work perfectly

```
<link type=”text/css” rel=”stylesheet” href=”example.css”>
<script type=”text/javascript” src=” example.js”></script>
```

They removed type in HTML5 ,they declared CSS ,java script as standards in HTML5
CSS default style for HTML5 
Javascript default scripting language for HTML5

```
<link type=”text/css” rel=”stylesheet” href=”example.css”>
<script type=”text/javascript” src=” example.js”></script>
```

And the new HTML5 document is 

```
<!DOCTYPE html >
<html>
<head>
<meta charset=UTF-8">
<title>Arunkumar ‘s blog</title>
<link rel="stylesheet" href="example.css">
<script src=" example.js"></script>
</head>
<body>
<h1>Welcome to My blog</h1>
<p>
Join my site to know about Web 
</p>
</body>
</html>

```
How it works in old browsers with new doctype meta etc?

Because CSS,Javascript are now defaults standards for html5 and no need to give type. And many browsers assuming that they are the defaults already. Even though you did not mension type browser will render the pages as expected

 
And from now onwards no versions in html we call it HTML language as simple as that.

And without DTD ?

HTML used to be based on a standard called SGML, and that standard required both the complex form of the doctype and the DTD.

The new standard has moved away from SGML as a way to simplify HTML language and make it more flexible. 

And you know many of the browsers just CHECKS ONLY HTML in doctype to ensure that they are parsing HTML document.  So it is not a problem.

Still have doubt goto w3c validator or click here to check html validity








Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







