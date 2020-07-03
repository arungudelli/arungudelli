+++
title="A Simple CSS Drop Down Menu"
summary="CSS Drop Down Menu: In this tutorial I will explain how to create a Simple Drop Down Menu using CSS alone without using Javascript and Images."
keywords="css,drop down menu,css drop down menu using css,css drop down menu,css3"
type='post'
date='2019-10-19T18:04:55+0000'
lastmod='2019-10-19T18:04:55+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++


Now a days I have been experimenting with CSS3 features, with some advanced CSS3 selectors we can easily Create a Drop Down Menu with pure CSS without using any fancy background images and JavaScript.

In this tutorial I will explain step by step procedure to create a simple drop down menu &nbsp;with pure CSS.

Here is the Simple Drop Down Demo.

{{< figure src="DropDownMenuSampleFinal.gif" title="A Simple Drop Down Menu" alt="A Simple Drop Down Menu" >}}

### HTML Drop Down Menu Structure:

First we will create HTML structure

<pre>&lt;nav&gt;
	&lt;ul&gt;
		&lt;li&gt;&lt;a href="#"&gt;Home&lt;/a&gt;&lt;/li&gt;
		&lt;li&gt;&lt;a href="#"&gt;Articles&lt;/a&gt;
			&lt;ul&gt;
				&lt;li&gt;&lt;a href="#"&gt;Web Design&lt;/a&gt;&lt;/li&gt;
                                     &lt;ul&gt;
					&lt;li&gt;&lt;a href="#"&gt;HTML&lt;/a&gt;&lt;/li&gt;
					&lt;li&gt;&lt;a href="#"&gt;CSS&lt;/a&gt;&lt;/li&gt;
				      &lt;/ul&gt;
				&lt;li&gt;&lt;a href="#"&gt;Fun&lt;/a&gt;&lt;/li&gt;
				&lt;li&gt;&lt;a href="#"&gt;freebies&lt;/a&gt;&lt;/li&gt;
			&lt;/ul&gt;
		&lt;/li&gt;
		&lt;li&gt;&lt;a href="#"&gt;Archives&lt;/a&gt;
			&lt;ul&gt;
				&lt;li&gt;&lt;a href="#"&gt;January&lt;/a&gt;&lt;/li&gt;
				&lt;li&gt;&lt;a href="#"&gt;February&lt;/a&gt;&lt;/li&gt;
			&lt;/ul&gt;
		&lt;/li&gt;
		&lt;li&gt;&lt;a href="#"&gt;AboutMe&lt;/a&gt;&lt;/li&gt;
	&lt;/ul&gt;
&lt;/nav&gt;</pre>

&nbsp;

The HTML structure as follows



&nbsp;<span style="line-height: 1.5em;">I created two sub Menus for Articles and Archives, these sub menus can be shown once the parent menu liks is activated by HOVER.</span>

And under Articles&gt;Web Design I have sub-sub-menu (HTML and CSS) this links are shown horizontally from the first drop down as shown in Drop Down Menu.

### CSS Code For Drop Down Menu:

Now we will write the CSS for the HTML code.

<pre>nav ul ul {
	display: none;
}

nav ul li:hover &gt; ul {
        display: block;
}</pre>

&nbsp;

First we will hide the first set of sub links Articles&gt;Web Design,Fun,Freebies and Archives&gt;January,February using <span style="color: #000000;"><em>“display:none” </em></span>&nbsp;attribute. and to make them appear we have to change the <em>“display” &nbsp;</em>attribute to <em>“block”&nbsp;</em>on HOVER of LI.

The child selector &nbsp;&gt; make sure only the child UL of LI are visible rather than all other UL elements or other sub menus.

Here is the Demo

{{< figure src="DropDownMenuElements.gif" title="Drop Down Menu Elements" alt="Drop Down Menu Elements" >}}

And in next step few lines of CSS code to make it look like Menu

<pre>        nav ul
        {
            list-style: none;
            position: relative;
            display: inline-table;
        }
        nav ul li a
        {
            display: block;
            padding: 25px 40px;
            text-decoration: none;
        }
        nav ul li
        {
            float: left;
        }
        nav ul ul li
        {
            position: relative;
            float: none;
        }</pre>

&nbsp;

First we will remove bullets for list elements by adding <em>“list-style:none”&nbsp;</em>to “nav ul” element. And <em>“position:relative”&nbsp;</em> attribute will allows us to position sub menu elements according to the Main Menu. <em>“display:inline-table”&nbsp;</em>attribute allows us to display main navigation elements to display as an inline-table.

I have added padding to anchor elements to separate links and I removed decoration (underline for anchor elements) with &nbsp;<em>“text-decoration:none”&nbsp;</em>attribute.

To make it look like Menu side by side I added <em>“float:left”</em> attribute to LI elements.(Main Navigation Bar)

For Drop Down elements I added <em>“float:none”</em> attribute to “nav ul ul li” and also <em>“position:relative”</em>.

Here is the Demo.

{{< figure src="DropDownMenuSample1.gif" title="Drop Down Menu Sample" alt="Drop Down Menu Sample" >}}

Now it has a look of Drop Down Menu But as you move from one link to other links the elements are dancing from right to left and also secondary sub menu elements are directly appearing below the LI elements. To fix this we will add few lines of CSS code

<pre>        nav ul ul
        {
            position: absolute;
            top: 100%;
        }
        nav ul ul ul
        {
            position: absolute;
            left: 100%;
            top: 0;
        }</pre>

&nbsp;

For first &nbsp;sub-menu elements I have added <em>“position:absolute”</em> and <em>“top:100%”</em>. So the drop down elements will appear directly below to the relative parent LI.

And For Secondary sub-sub-menu &nbsp;I have added <em>“position:absolute”</em> attribute and <em>“left:100%”</em>. So the drop down elements will appear exactly right side of the relative parent LI element.

Here is the Demo.

{{< figure src="DropDownMenuSample2.gif" title="Drop Down Menu Sample" alt="Drop Down Menu Sample" >}}

The logic part is completed now we will apply some styles and colors to Make it stylish Drop Down Menu as shown in the first Demo.

I have used few CSS3 features like gradient etc. The code is simple and easy to understand, added color to main navigation menu and then on HOVER changed the colors. Here is the code.

<pre>nav ul
        {
            background: #0052a4;
            background: linear-gradient(top, #0052a4 0%, #0052a4 100%);
            background: -moz-linear-gradient(top, #0052a4 0%, #0052a4 100%);
            background: -webkit-linear-gradient(top, #0052a4 0%,#0052a4 100%);
            box-shadow: 0px 0px 9px rgba(0,0,0,0.15);
            border-radius: 10px;
        }
        nav ul li:hover
        {
            background: #C0C0C0;
            background: linear-gradient(top, #C0C0C0 0%, #C0C0C0 40%);
            background: -moz-linear-gradient(top, #C0C0C0 0%, #C0C0C0 40%);
            background: -webkit-linear-gradient(top, #C0C0C0 0%,#C0C0C0 40%);
        }
        nav ul ul
        {
            background: #C0C0C0;
            background: linear-gradient(top, #C0C0C0 0%, #C0C0C0 40%);
            background: -moz-linear-gradient(top, #C0C0C0 0%, #C0C0C0 40%);
            background: -webkit-linear-gradient(top, #C0C0C0 0%,#C0C0C0 40%);
            border-radius: 0px;
            padding: 0;
        }
        nav ul ul li
        {
            border-top: 1px solid #000;
            border-bottom: 1px solid #000;
        }
        nav ul li a
        {
            color: #FFF;
        }
        nav ul li:hover a
        {
            color: #000;
        }

        nav ul ul li a
        {
            color: #fff;
        }
        nav ul ul li a:hover
        {
            color: #fff;
            background: #0052a4;
        }</pre>

&nbsp;

I tested it in almost all modern web browsers working fine.If you face any issues let me know.

Here is the Final Demo

<a title="A Simple Drop Down Menu" href="https://arungudelli.com/Tools/HTML5/CSS3%20Animations/DropDownMenuUsingCSS.htm" target="_blank">Demo For Drop Down Menu</a>

I hope you enjoyed this article If so share with your friends and also subscribe to my blog and connect me at social networks.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.









