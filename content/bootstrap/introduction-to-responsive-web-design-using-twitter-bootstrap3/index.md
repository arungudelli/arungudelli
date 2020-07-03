+++
title="Introduction To Responsive Web Design Using Twitter Bootstrap3"
summary="Tutorial explains how to build responsive web pages using Twitter Bootstrap Framework.This is the best framework for designing responsive websites."
keywords="twitter bootstrap,responsive web design,responsive web design using twitter bootstrap,bootstrap"
type='post'
date='2019-10-21T18:04:42+0000'
lastmod='2019-10-21T18:04:42+0000'
draft='true'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

I started learning responsive web design using Twitter Bootstrap Framework. This is my first tutorial on responsive Web design, I will start with the introduction Bootstrap framework and responsive web design, and at the end of the post you will get an idea how to build responsive web pages using bootstrap framework.

### What is Responsive Web Design?

&nbsp; &nbsp; &nbsp; Instead of telling What is Responsive Web design It’s better to explain What problem does&nbsp;responsive web design solve? Earlier we used to build separate versions of websites for devices&nbsp;like Iphone Blackberry Ipad and Kindle etc because of different resolutions of devices. But daily one new device with new resolution coming into the mobile industry. Building again one more version of website for those new device is foolishness.

&nbsp; &nbsp; &nbsp;In simple words we should built&nbsp;webpages in such a way that they should look uniformly(best viewing experience) across all the devices irrespective of devices and resolutions.This is nothing but responsive web design.

&nbsp; &nbsp; &nbsp; Twitter Bootstrap framework provides a great platform for building such responsive web pages.

### Introduction To Twitter Bootstrap Framework:

So What is Bootstrap Framework? Initially&nbsp;UI designers has to give design of the website to the developers so that they can proceed further development. But this is waste of time.

<ul><li>Twitter Bootstrap is a CSS framework which helps developers in building&nbsp;web pages even though you don’t have any designing experience.</li><li>All you have to do is write HTML code&nbsp;according to the Bootstrap specifications.</li><li>There are so many inbuilt classes&nbsp;written in Bootstrap framework. Just you should learn how to use those classes.</li></ul>

I know it’s too high level explanation but once you started learning the framework you will understand.

Responsive web designing became very easy with the help of Twitter Bootstrap framework.

We will start with one simple example First we will decide some design for the webpage.

### Setting Up Twitter Bootstrap Framework:

Download the twitter Bootstrap framework zip file and extract them you will find three folders css,js and fonts.&nbsp;and create one html file I created as Index.html.

{{< figure src="BootstrapStructure.png" title="Twitter Bootstrap Framework Structure" alt="Twitter Bootstrap Framework Structure" >}}

### Setting up Bootstrap Responsive HTML page:

Before starting our example we will include the all necessary CSS and Js files and attributes to the html file. Have a look at the sample HTML page.Don’t forget to add jQuery file.

```
<meta charset="”utf-8”">
<meta name="viewport" content="width=device-width, initial-scale=1">


    <title>Bootstrap Tutorial</title> <script src="js/jquery-1.10.1.min.js"></script> <script src="js/bootstrap.min.js"></script> <link href="css/bootstrap.min.css" rel="stylesheet">

 <script defer="" src="//arun-arungudellicom.netdna-ssl.com/wp-content/cache/autoptimize/js/autoptimize_386847f70fd99f9944c9300a4f86207d.js"></script>
```

&nbsp;

No need to explain all fields all are self explanatory. The only new thing is viewport meta attribute.

<pre><meta name="viewport" content="width=device-width, initial-scale=1"></pre>

&nbsp;

The viewport attribute sets the width of the webpage to Device Width and Initially scaling to default size 1. And if you want to increase the zoom or decrease the Zoom you may change this value.

That’s it.Set up is Done. Now we will learn how to write HTML mark up according to bootstrap framework.

{{< figure src="Responsive-Web-Page-Using-Bootstrap.png" title="Responsive Web Page Using Bootstrap" alt="Responsive Web Page Using Bootstrap" >}}

Our webpage contains

<ul><li>One Header with Navigation bar</li><li>One Featured Content</li><li>Content with&nbsp;4 horizontal Divisions.</li></ul>

We will write appropriate HTML mark up according to our needs

### Bootstrap Header with Responsive Navigation bar:

Our page content should be in center of the screen.&nbsp;Bootstrap provides a “container” class with correct padding and margin values. We will use this container as our parent element. Just write the following Code.

```
<div class="container"></div>
```

&nbsp;

Now we will add Title of the web page&nbsp;inside this Div Container

```
<h1><a href="#">Bootstrap Site</a></h1>
```
&nbsp;

No need to add any external styles to H1 tags Bootstrap provides default styling for H1 element.

Now we will add responsive Navigation bar.First have a look at our navigation bar.

{{< figure src="Bootstrap-Navigation-Bar.png" title="Bootstrap Navigation Bar" alt="Bootstrap Navigation Bar" >}}

&nbsp;

The Navigation Bar contains one heading Navigation,Navigation Bar Menu and One search box with submit button.

Bootstrap provides&nbsp;&nbsp;“navbar” class for navigation bar. Add following HTML code below the title of the website(Inside container Only)

```
<nav class="navbar navbar-default" role="navigation">
</nav>
```

&nbsp;

I have added one more class “navbar-default” which will add default styles to Navigation bar. Now we will add navigation menu elements

```
<ul class="nav navbar-nav">
                        <li class="active"><a href="#">Home</a></li>
                        <li><a href="#">Projects</a></li>
                        <li><a href="#">Services</a></li>
                        <li><a href="#">Downloads</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Contact</a></li>
</ul>
```

&nbsp;

Just create a list of elements and Add classes named “nav navbar-nav”. and “Active” class refers to the selected navigation element. Our Menu is ready.

But we have one more search box in navigation Menu To add that search box just add following Code.

```
<form class="navbar-form navbar-right" role="search">
            <div class="form-group">
                <input type="text" class="form-control" placeholder="Search">
            </div>
             <button type="submit" class="btn btn-default">Submit</button>
 </form>
 ```

&nbsp;

Normally search box is a form so I added form element And To include it in navigation Bar add “navbar-form”. And I added one more class called “navbar-right” which tells that the search should be in right side of the navigation bar. You can play with this settings by giving “navbar-left” ,”navbar-top” etc.

Just go and look at your webpage. And if you tested it in Mobile or Tab you might observe that this is not responsive. How a responsive menu look like in mobile devices. Have a look at the below image

{{< figure src="Responsice-Navigation-Bar.gif" title="Bootstrap Responsive Navigation Bar" alt="Bootstrap Responsive Navigation Bar" >}}

&nbsp;

The above menu design is used in Mobile devices. We have Navigation Header (Brand) and Navigation elements in drop box and when you touch the button it will collapse.

So we will slightly modify our code to make it responsive menu

```
<div class="container-fluid">                
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#primaryNavigationBar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Navigation</a>
                </div>
                <div class="collapse navbar-collapse" id="primaryNavigationBar">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="#">Home</a></li>
                        <li><a href="#">Projects</a></li>
                        <li><a href="#">Services</a></li>
                        <li><a href="#">Downloads</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                    <form class="navbar-form navbar-right" role="search">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Search">
                        </div>
                        <button type="submit" class="btn btn-default">Submit</button>
                    </form>
                </div>
            </div>
```            

&nbsp;

First I added entire navigation menu inside “container-fluid” class.We are collapsing and expanding the menu so width and height should be varied accordingly. So I have added&nbsp;“container-fluid” class.

Now I added “navbar-header” class which contains a Button and Navigation header text. The button contains three horizontal icons as shown above figure.

So I have added three span elements with class “”icon-bar”.

And we have to give target and class “navbar-toggle” to button.Target is nothing but our Navigation Menu elements.

The list and search box I moved inside the “collapse navbar-collapse” class. which refers that this is Collapsable Menu. And gave some Id. The Id should be target of Button.

Our responsive Menu is Ready. Now we will add Featured Content.

### Featured Content in Twitter Bootstrap:

Now a days most of the webpages contains featured content which will hi-lite the important information of webpages. And some web pages contains&nbsp;carousel.

Bootstrap provides “”jumbotron” class to display featured content. Just add below code under the navigation menu code.

```
<div class="jumbotron">
            <h1>Hello, world!</h1>
            <p>...</p>
            <p><a class="btn btn-primary btn-lg" role="button">Learn more</a>             </p>
</div>
```

&nbsp;

And I gave few classes like btn btn-primary btn-lg etc. in anchor tags. those are all classes provided by the bootstrap. You can play around with them. In my coming posts I will try to explain all types of button classes.

Now we will add our main content. Now I am going to explain important feature of Bootstrap framework.

### Grid System in Twitter Bootstrap:

Bootstrap is famous because of this Grid System.Bootstrap provides a 12 grid column layout to build web pages. i.e., you can place 12 vertical grids or columns inside any parent element.

This is responsive and mobile first fluid system.More technical words rite I will explain it in simple words.

Our webpage design contains four horizontal divs(Heading1, Heading2, Heading3 and Heading4).

To add this horizontal divs add the following Code

```
<div class="row">
            <div class="col-md-3"></div>
            <div class="col-md-3"></div>
            <div class="col-md-3"></div>
            <div class="col-md-3"></div>
</div>
```

&nbsp;

The four grid elements should be inside the class “row”. and I gave class names as “col-md-3”. We want four equal grids so 3+3+3+3=12. To put four equally width elements you should give class name as “col-md-3”. Here md-refers to medium devices normally desktops, should display 4 columns inside a row element.

If you want two unequal columns just give classes names as “col-md-8” “col-md-4” and again (8+4=12.) You can play around with this grid system according to your requirements.

And I said this grid system is responsive rite. What does it mean? In medium devices it shows 4 columns and in small devices it shows only one column according to device width. Look at the above gif image. I tested it in my Moto X mobile it’s showing one column per row.

But it’s better to mention this values explicitly so add following classes to the divs

```
<div class="row">
            <div class="col-md-3 col-xs-12 col-sm-6"></div>
            <div class="col-md-3 col-xs-12 col-sm-6"></div>
            <div class="col-md-3 col-xs-12 col-sm-6"></div>
            <div class="col-md-3 col-xs-12 col-sm-6"></div>
</div>
```
&nbsp;

Have a look at the below images

{{< figure src="Responsive-Grid-in-Desktops.png" title="Responsive Grid in Desktops" alt="Responsive Grid in Desktops" >}}

&nbsp;

In Desktops medium devices Bootstrap displays&nbsp;4 columns are in a row. i.e.,”col-md-3″ (3+3+3+3=12)

{{< figure src="Responsive-Grid-in-Tabs.png" title="Responsive Grid in Tabs" alt="Responsive Grid in Tabs" >}}

&nbsp;

In tabs i.e., small devices Bootstrap displays&nbsp;Two columns in a row. col-sd-6 (6+6=12)

{{< figure src="Responsive-Grid-in-Mobiles.png" title="Responsive Grid in Mobiles" alt="Responsive Grid in Mobiles" >}}

&nbsp;

In Extra small devices i.e., Bootstrap displays one column in a row .col-xs-12

That means according to width of the device the webpage will adjust.

If you want to create any page layout you should use row- column grid system.

Follow my blog for bootstrap tutorials.

<span style="color: #000000;">I hope you enjoyed this article If so share with your friends and also subscribe to my blog and connect me at social networks.</span>

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







