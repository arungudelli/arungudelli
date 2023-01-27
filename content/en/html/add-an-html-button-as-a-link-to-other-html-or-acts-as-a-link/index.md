+++
title="3 Ways to Add An HTML Button As A Link To Other HTML pages"
summary="There are 3 ways to add an HTML button as a link to other HTML pages 1. Using Button inside an HTML form 2. Using CSS style an anchor link as button 3. Using JavaScript button onClick event."
keywords=["html button link code,button as a link,button as link in css,html"]
type='post'
date='2019-11-18T18:02:28+0000'
lastmod='2023-01-26T00:02:28+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

There are 3 ways to create an HTML button that acts as a link to other HTML pages.

1. Using Button inside an HTML form
2. Using CSS style an anchor link as button
3. Using JavaScript button onClick event. 


{{%toc%}}

## 1. Add an HTML button as a link using the form tag

To create a button which acts as a link i.e., when we click on the button it will redirect to other HTML pages, place the `<button>` tag inside a `<form>` and add the HTML target link in action attribute of the form element as shown below.

```html
<form action="https://www.angularjswiki.com/">
<input type="submit" value="Go to Angular Tutorials" />
</form>

<form action="https://www.angularjswiki.com/"> 
 <button type="submit">Go to Angular Tutorials</button> 
</form>
```

Or we can use `<input>` tag with type submit which acts as a button.

To open a button link in a new tab we can add form target as blank as shown below

```html
<form action="https://www.angularjswiki.com/" target="_blank"> 
 <button type="submit">Go to Angular Tutorials</button> 
</form>
```
And we can use HTML5 `formaction` attribute with the `<button>` inside a form to redirect to other HTML pages as shown below

```html
<form target="_blank">
<button type="submit" formaction="https://www.angularjswiki.com/">
Go to Angular Tutorials</button>
</form>
```

But the problem with the above approach is it will add a question mark at the end of the URL.

And there is no straight way to remove that question mark from the target URL.

## 2. Add an HTML button as a link using CSS

The best way to add a button that acts as a link to other HTML pages is to style an anchor tag (link) as a button using CSS.

Because for me “add button as a link” means I can right-click on the link to open it in a new tab or I can open it in incognito mode or I can save or copy the link address, that I cannot do with the above approach.

{{< figure src="button-as-a-link-using-form.png" title="button as a link using form tag" alt="button as a link using form tag" >}}

Follow the below steps to add a button that acts as a link

<ol><li>Add an anchor tag with the class name “buttonLink”. (or whichever name you like)</li><li>Add to the button class, add the appearance CSS property as the button</li></ol>

```html
<a href="https://www.angularjswiki.com/" target="_blank" class="buttonLink">
 Go to Angular Tutorials
</a> 

<!--CSS-->
a.buttonLink{
  -moz-appearance: button; 
  -webkit-appearance: button;
   appearance: button;   
}

```

Additionally, you can add “text-decoration: none;” and “color: initial;” to button link class to make it look like exact button.

```css
a.buttonLink{
 -moz-appearance: button; 
 -webkit-appearance: button;
 appearance: button; 
 color: initial;
 text-decoration: none;
}
```

{{< figure src="button-as-a-link-using-CSS.png" title="button as a link using CSS" alt="button as a link using CSS" >}}

## 3. Add an HTML button as a link using JavaScript

If JavaScript is allowed we can use the button on click event to open other pages.

On clicking the button we can change the current window location using `location.href` as shown below.

```html
<button onclick="location.href='https://www.angularjswiki.com';"> 
Go to Angular Tutorials
</button>
```

And to open the button link in a new window we can use `window.open` function.

```html
<button onclick="window.open('https://www.angularjswiki.com')"> 
Go to Angular Tutorials
</button>
```

But as I said before we have few limitations like open in a new tab or saving the link etc.

So the best way to add a button as a link is to use the anchor link with the button look-alike CSS.









