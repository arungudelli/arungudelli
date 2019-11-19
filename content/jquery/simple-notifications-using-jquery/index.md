+++
title="Simple Notifications Using JQuery"
summary="Toastr is the best plugin for implementing Notifications using jQuery at client side.This Toastr jQuery notification plugin comes with so many features."
keywords="jquery,simple notifications using jquery,toastr plugin,jquery plugins,javascript"
type='post'
date='2019-11-16T20:54:03+0000'
lastmod='2019-11-16T20:54:03+0000'
draft='false'
authors=['admin']
[image]
caption='Simple Notifications Using JQuery'
focal_point=''
preview_only=false
+++








Today &nbsp;I will explain how to implement Simple Client Side <span style="text-decoration: underline;"><em>Notifications using jQuery</em></span>.

There are so many jQuery notifications&nbsp;plugins are available for implementing client side notifications , But recently I came across a beautiful plug in called ‘<a title="Toastr" href="http://codeseven.github.io/toastr/" target="_blank" rel="noopener noreferrer">Toastr</a>‘ , a CodeSeven jQuery plugin which is very simple to use and can be easily customized and extended.

Let’s go through a simple example. As I told before it’s very easy to use.

Link to toastr.css and toastr.js files.

<pre>&lt;link href="toastr.css" rel="stylesheet"/&gt; 
&lt;script src="toastr.js"&gt;&lt;/script&gt;</pre>

&nbsp;

We can trigger four types of notifications

<ul><li>Success</li><li>Error</li><li>Warning</li><li>Info</li></ul>

To Display Simple Notifications without Title&nbsp;use toastr.info() or toastr.error() or&nbsp;toastr.success() or&nbsp;toastr.warning()

<pre>## Success Message
toastr.success('Hurray..');

## Error Message
toastr.error('Ooops..');

## Warning Message
toastr.warning('Be careful..');

## Info Message
toastr.info('He He..');</pre>

&nbsp;

To Add Title to the notification pass Title as second argument.

<pre>## Success Message
toastr.success('Hurray..','Success');

## Error Message
toastr.error('Ooops..','Error');

## Warning Message
toastr.warning('Be careful..','Warning');

## Info Message
toastr.info('He He..','Information');</pre>

&nbsp;

Here is the simple Demo.

{{< figure src="SimplejQueryNotifications.gif" title="Simple jQuery Notifications" alt="Simple jQuery Notifications" >}}

Not only simple text you can &nbsp;write html tags as notification dialogue box body. Here is the simple example.

<pre>tostr.info('&lt;i&gt;Success&lt;/i&gt;','&lt;b&gt;&lt;i&gt;Success&lt;/i&gt;&lt;/b&gt;');</pre>

&nbsp;

### Enable Close Button in Toastr jQuery Notification plug in:

By default close button is disabled in this jQuery notification plug in and You can enable this by setting “closeButton” value to true.

<pre>toastr.options.closeButton = true;</pre>

&nbsp;

This will enable close button icon in notification dialogue box as shown in above figure. And if you want to override this closeButton use the below code.

<pre>toastr.options.closeHtml = '&lt;button&gt;&lt;i&gt;Close&lt;/i&gt;&lt;/button&gt;';</pre>



&nbsp;

And if you want to close all notifications at a time use the tostr.clear() function.

### Position of jQuery Notifications in Web page:

Default position of notifications is “top right”.You can change the position of notification using “positionClass” attribute. With this options we can display notifications in six different positions in a Web page.

<pre>toastr.options.positionClass = "toast-bottom-right";
toastr.options.positionClass = "toast-bottom-left";
toastr.options.positionClass = "toast-top-right";
toastr.options.positionClass = "toast-top-left";
toastr.options.positionClass = "toast-bottom-full-width";
toastr.options.positionClass = "toast-top-full-width";</pre>

&nbsp;

### Display Sequence of Multiple Notifications:

If you have multiple notifications, newest notification are shown at top side by default&nbsp;.However you can disable this options by setting “newestOnTop” to false. Then newest notification are shown at bottom side.

<pre>toastr.options.newestOnTop = false;</pre>

&nbsp;

Here I covered basic usage of this beautiful jQuery notification plug in “Toastr”.It comes with so many options like callback mechanisms , Animations etc and you can override the CSS file to change the display . Please go through the plugin site to explore these options.

Here is the <a title="Toastr Notifications Demo" href="https://arungudelli.com/Tools/HTML5/SimpleNotifications/SimpleNotification.html" target="_blank" rel="noopener noreferrer">Simple Demo</a>

### Toastr is Responsive:

Include the viewport meta tag and the “toastr.css”, and toastr will adjust to different device sizes.You can test responsiveness of this plug in here “<a title="Toastr Notification Plugin Responsiveness" href="http://www.responsinator.com/?url=http%3A%2F%2Farungudelli.com%2FTools%2FHTML5%2FSimpleNotifications%2FSimpleNotification.html" target="_blank" rel="noopener noreferrer">Toastr plug in Notification Responsiveness</a>”

I hope you have enjoyed this article.If so share this post with your friends and also join our mailing list.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.









