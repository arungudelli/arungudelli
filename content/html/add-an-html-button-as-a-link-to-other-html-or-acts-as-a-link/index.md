+++
title="Add An HTML Button As A Link To Other HTML Or Acts As A Link"
summary="To add an HTML button that acts as a link to other HTML, we can use the button inside HTML form or style an anchor link as a button or use button onClick event."
keywords="html button link code,button as a link,button as link in css,html"
type='post'
date='2019-11-18T18:02:28+0000'
lastmod='2019-11-18T18:02:28+0000'
draft='false'
authors=['admin']
[image]
caption='Add An HTML Button As A Link To Other HTML Or Acts As A Link'
focal_point=''
preview_only=false
+++








To add an HTML button as a link to other HTML, we can use the button inside HTML form or style an anchor link as a button or use button onClick event.

{{%toc%}}

## 1. Add an HTML button as a link using the form tag:

To create a button which acts as a link i.e., when we click on the button it will redirect to other HTML pages we can place the <em>&lt;button&gt;&nbsp;</em>tag inside a <em>&lt;form&gt;</em> and add the HTML target link in action attribute of the form element as shown below

<pre>&lt;form action="https://www.angularjswiki.com/"&gt;
&lt;input type="submit" value="Go to Angular Tutorials" /&gt;
&lt;/form&gt;

&lt;form action="https://www.angularjswiki.com/"&gt; 
 &lt;button type="submit"&gt;Go to Angular Tutorials&lt;/button&gt; 
&lt;/form&gt;</pre>

Or we can use <em>&lt;input&gt;</em> tag with type submit which acts as a button.

To open a button link in a new tab we can add form target as blank as shown below

<pre>&lt;form action="https://www.angularjswiki.com/" target="_blank"&gt; 
 &lt;button type="submit"&gt;Go to Angular Tutorials&lt;/button&gt; 
&lt;/form&gt;</pre>

And we can use HTML5 <em>formaction</em> attribute with the <em>&lt;button&gt;</em> inside a form to redirect to other HTML pages as shown below

<pre>&lt;form target="_blank"&gt;
&lt;button type="submit" formaction="https://www.angularjswiki.com/"&gt;
Go to Angular Tutorials&lt;/button&gt;
&lt;/form&gt;</pre>

But the problem with the above approach is it will add a question mark at the end of the URL.

And there is no straight way to remove that question mark from the target URL.

## 2. Add an HTML button as a link using CSS

The best way to add a button that acts as a link to other HTML pages is to style an anchor tag (link) as a button using CSS.

Because for me “add button as a link” means I can right-click on the link to open it in a new tab or I can open it in incognito mode or I can save or copy the link address, that I cannot do with the above approach.

{{< figure src="button-as-a-link-using-form.png" title="button as a link using form tag" alt="button as a link using form tag" >}}

Follow the below steps to add a button that acts as a link

<ol><li>Add an anchor tag with the class name “buttonLink”. (or whichever name you like)</li><li>Add to the button class, add the appearance CSS property as the button</li></ol>

<pre>&lt;a href="https://www.angularjswiki.com/" target="_blank" class="buttonLink"&gt;
 Go to Angular Tutorials
&lt;/a&gt; 

a.buttonLink{
  -moz-appearance: button; 
  -webkit-appearance: button;
   appearance: button;   
}</pre>

Additionally, you can add “text-decoration: none;” and “color: initial;” to button link class to make it look like exact button.

<pre>a.buttonLink{
 -moz-appearance: button; 
 -webkit-appearance: button;
 appearance: button; 
 color: initial;
 text-decoration: none;
}</pre>

{{< figure src="button-as-a-link-using-CSS.png" title="button as a link using CSS" alt="button as a link using CSS" >}}

## 3. Add an HTML button as a link using JavaScript

If JavaScript is allowed we can use the button on click event to open other pages.

On clicking the button we can change the current window location using <em>location.href</em> as shown below.

<pre>&lt;button onclick="location.href='https://www.angularjswiki.com';"&gt; 
Go to Angular Tutorials
&lt;/button&gt;

</pre>

And to open the button link in a new window we can use <em>window.open</em> function.

<pre>&lt;button onclick="window.open('https://www.angularjswiki.com')"&gt; 
Go to Angular Tutorials
&lt;/button&gt;</pre>

But as I said before we have few limitations like open in a new tab or saving the link etc.

So the best way to add a button as a link is to use the anchor link with the button look-alike CSS.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







