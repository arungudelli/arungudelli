+++
title="4 Ways To Display Indian Rupee Symbol In HTML(₹) Pages"
summary="To display Indian rupee symbol in HTML pages, Use rupee ASCII code 8377 Or rupee Unicode character code &#x20B9 Or CSS content values Or Use font awesome icons."
keywords="indian rupee currency symbol,indian rupee symbol,code for displaying indian rupee symbol,indian rupee symbol in html,html"
type='post'
date='2019-10-14T18:05:22+0000'
lastmod='2019-10-14T18:05:22+0000'
draft='false'
authors=['admin']
[image]
caption='4 Ways To Display Indian Rupee Symbol In HTML(₹) Pages'
focal_point=''
preview_only=false
+++








Steps to display Indian rupee symbol in HTML pages (₹)

<ol><li>Use rupee symbol ASCII code <em><strong><span style="text-decoration: underline;">8377</span></strong></em></li><li>Or Use rupee symbol Unicode character code <span style="text-decoration: underline;"><em><strong>&amp;#x20B9</strong></em></span></li><li>Or Use CSS content values</li><li>Or Use font awesome icons</li></ol>

<ul><li><a href="#step-1">Display Rupee symbol in HTML using ASCII Code</a></li><li><a href="#step-2">Display Rupee symbol in HTML using Unicode Character code</a></li><li><a href="#step-3">Display Rupee symbol in HTML using CSS content values</a></li><li><a href="#step-4">Display Rupee symbol in HTML using font awesome icons</a></li></ul>

Before that let’s go to the history of &nbsp;Indian Currency Rupee Symbol(₹).

The Union Cabinet&nbsp;approved Indian currency rupee symbol&nbsp;on 15 July 2010. And this Rupee symbol designed by&nbsp;Uday Kumar, Assistant Professor IIT Gauhathi.

It’s a combination of Devanagari Letter “र”(ra)&nbsp;and Latin Capital ‘R’ without vertical bar.(₹)

{{< figure src="New-Indian-Rupee-Symbol.jpg" title="New Indian Rupee Symbol in HTML Websites" alt="New Indian Rupee Symbol in HTML Websites" >}}

## Display Rupee symbol in HTML using ASCII Code:

To display Rupee Symbol in HTML Use ASCII code &amp;#8377; as shown below.

<pre>&lt;p&gt;Rupee sign: &amp;#8377;&lt;/p&gt;</pre>

## ₹

## Display Rupee symbol in HTML using Unicode character Code:

One more method is by using the Unicode Character of Indian Rupee Symbol.

On August 10th, 2010 Unicode Technical Committee accepted the Code position as <span style="text-decoration: underline;"><em>U+20B9</em></span><em> .</em>

To display rupee sign in HTML pages, use the Unicode <span style="text-decoration: underline;"><em><strong>&amp;#x20B9;</strong></em>&nbsp;</span> as shown below

<pre>&lt;p&gt;Rupee sign: &amp;#x20B9;&lt;/p&gt;</pre>

## ₹

But the problem with this method is Unicode will only be converted on the systems with Unicode version 6.0. The user with the lower version of the Unicode system may not able to see the Rupee symbol.

## Display Rupee symbol in HTML using CSS content values:

To display the rupee symbol in HTML using CSS content values. Use CSS pseudo-elements ::before or ::after with CSS content value as <strong>“\20B9”</strong>

<pre>&lt;style&gt;
.inr-sign::before{
content:"\20B9";
}
// Or use with ::after
.inr-sign::after{
content:"\20B9";
}
&lt;/style&gt;

&lt;span class="inr-sign"&gt;&lt;/span&gt;</pre>

## ₹

## Display Rupee symbol in HTML using font awesome icons:

If you are using font awesome icons in your project. You can use font awesome icon code to display Indian rupee sign in HTML.

The icon name for rupee symbol is “fa-rupee-sign”

<pre>&lt;i class="fas fa-rupee-sign"&gt;&lt;/i&gt;</pre>

To use font awesome icons and for the complete 1534 free font awesome icons list go through this article

<a href="https://www.angularjswiki.com/angular/font-awesome-icons-list-usage-css-content-values/" target="_blank" rel="noopener noreferrer">1534 font awesome icons list,usage,css content values cheatsheet</a>

And to display rupee symbol in Angular applications go through the below article

<a href="https://www.angularjswiki.com/angular/angular-currency-pipe-formatting-currency-in-angular/" target="_blank" rel="noopener noreferrer">Angular Currency Pipe &amp; Formatting Currency In Angular</a>

And one more method is to use some third-party Web API like Web Rupee. But I will not prefer to use this method as we have standard codes to display the rupee symbol. It’s like for displaying ‘&amp;’ in our web pages using some external library.

The above 4 ways are widely accepted and used by many people around the world to display the Indian Rupee symbol(₹) in HTML websites.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.









