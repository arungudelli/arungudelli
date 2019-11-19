+++
title="Simple Pagination Using JQuery & JPages Plugin"
summary="Client side pagination using jQuery,jPages plugin.This jQuery pagination plugin has many features like scroll pagination,CSS3 animations to pagination."
keywords="simple pagination jquery,jquery pagination plugin,jquery pagination tutorial,jquery"
type='post'
date='2019-11-16T20:54:23+0000'
lastmod='2019-11-16T20:54:23+0000'
draft='false'
authors=['admin']
[image]
caption='Simple Pagination Using JQuery & JPages Plugin'
focal_point=''
preview_only=false
+++








In this Tutorial I will explain how to implement simple <span style="text-decoration: underline;"><em>C</em></span><span style="text-decoration: underline;"><em>lient</em>&nbsp;S<em>ide Pagination</em></span> using <span style="text-decoration: underline;"><em>jQuery</em></span>

There are so many <em><span style="text-decoration: underline;">jQuery&nbsp;</span><span style="text-decoration: underline;">plugins</span></em> available for <span style="text-decoration: underline;"><em>pagination</em></span> &nbsp;but recently I came across one beautiful plug in called ‘<em><strong>jPages</strong></em> ‘ with rich set of features like such as

<ul><li>Auto page turn</li><li>Key and scroll browse</li><li>Showing items with delay</li><li>Completely customizable navigation panel etc…</li></ul>

Let’s go through a simple pagination example using ‘<em><strong>jPages</strong></em>‘ plugin.

<pre>//Used to display Page Numbers
&lt;div class="holder"&gt; &lt;/div&gt;

&lt;ul id="itemContainer"&gt;
            &lt;li&gt;&lt;/li&gt;
            &lt;li&gt;&lt;/li&gt;
            &lt;li&gt;&lt;/li&gt;
            &lt;li&gt;&lt;/li&gt;
            &lt;li&gt;&lt;/li&gt;
            &lt;li&gt;&lt;/li&gt;
&lt;/ul&gt;</pre>

&nbsp;

Just We need to create one list of elements in which we will display our Items. and one div for showing page numbers. and then we have to add ‘jQuery’ and ‘jPages’ plugins to enable pagination.

<pre>$(document).ready(function () {

$("div.holder").jPages({
containerID: "itemContainer",
perPage: 5,
keyBrowse: true,
scrollBrowse: true
});
});</pre>

&nbsp;

{{< figure src="SimplejQueryPagination.gif" title="Simple jQuery Pagination" alt="Simple jQuery Pagination" >}}

As I told before <span style="text-decoration: underline;"><em>jQuery jPages&nbsp;Pagination Plugin </em></span><em>&nbsp;</em>comes with rich set of options,In “containerId” we have to pass Id of our List of elements and ‘perPage’ represents how many elements we should show in particular page. and that’s it nothing more than that.

If we set ‘keyBrowse’ parameter to true we can use left and right arrows to browse through pages. and to enable mouse scroll browse just set ‘scrollBrowse’ &nbsp;parameter to true.



And if we want to jump to particular page,add one text box and button to HTML and in jQuery add following code.

<pre>$("button").click(function () {
                /* get given page */
                var page = parseInt($("input").val());
                /* jump to that page */
                $("div.holder").jPages(page);
});

&lt;input type="text" value="5" /&gt;
&lt;button&gt;jump to this page&lt;/button&gt;</pre>

&nbsp;

{{< figure src="jQueryPaginationJumpToPage.gif" title="jQuery Pagination Jump To Page" alt="jQuery Pagination Jump To Page" >}}

If we want to change the number of elements to show dynamically you can add one select box and then in jQuery add following code

<pre>        &lt;label&gt;
            items per page:
        &lt;/label&gt;
        &lt;select id="Itemsperpage"&gt;
            &lt;option&gt;5&lt;/option&gt;
            &lt;option selected="selected"&gt;10&lt;/option&gt;
            &lt;option&gt;15&lt;/option&gt;
        &lt;/select&gt;

$("select#Itemsperpage").change(function () {
                /* get new no of items per page */
                var newPerPage = parseInt($(this).val());
                /* destroy jPages and initiate plugin again */
                $("div.holder").jPages("destroy").jPages({
                    containerID: "itemContainer",
                    perPage: newPerPage
});
});</pre>



&nbsp;

‘jPages’ <span style="text-decoration: underline;"><em>pagination plugin</em></span> provides an option called ‘destroy’ to remove pagination from the container. So first we will remove the pagination using “destroy” parameter and then we will add pagination using new ‘perPage’ value which comes from select box.

{{< figure src="jQueryPaginationItemsPerPage.gif" title="jQuery Pagination Items Per Page" alt="jQuery Pagination Items Per Page" >}}

And we can customize buttons as per our needs, by default it will show ‘previous’ and ‘next’ buttons with page numbers in pagination div.

<pre> $("div.holder").jPages({
        containerID : "itemContainer",
        first       : "Intial",
        previous    : "previous",
        next        : "next",
        last        : "last"
 });</pre>

&nbsp;

And If you don’t want to show page numbers or simply you can show blank links by setting all above parameters to false and add one parameter called ‘links’ with blank value.

<pre>//setting midRange to 15 to prevent the breaks "..."
   $("div.holder").jPages({
        containerID : "itemContainer",
        first       : false,
        previous    : false,
        next        : false,
        last        : false,
        midRange    : 15,
        links       : "blank"
    });
});</pre>



&nbsp;

‘jPages’ pagination plugin integrated with Animate.css an amazing CSS3 Animation library by&nbsp;&nbsp;<a title="CSS3 Animation Library" href="https://daneden.me/animate/" target="_blank" rel="noopener">Dan Eden</a>&nbsp;. To use these animations just add Animate.css into your HTML file.<a href="https://daneden.me/"><br>
</a>

And then Add Animation property as shown below.

<pre>$("div.holder").jPages({
        containerID : "itemContainer",
        animation   : "bounceInUp"
});</pre>

&nbsp;

And Animate.css contains rich set of animations, to use all those animations we will add select options in our HTML and on change we will call different animations as shown below.

<pre>$("select#Animation").change(function () {
                            /* get new css animation */
                            var newAnimation = $(this).val();
                            /* destroy jPages and initiate plugin again */
                            $("div.holder").jPages("destroy").jPages({
                                containerID: "itemContainer",
                                animation: newAnimation
                            });
                        });

&lt;select id="Animation"&gt;
            &lt;option&gt;fadeIn&lt;/option&gt;
            &lt;option&gt;fadeInUp&lt;/option&gt;
            &lt;option&gt;fadeInDown&lt;/option&gt;
            &lt;option&gt;fadeInLeft&lt;/option&gt;
            &lt;option&gt;fadeInRight&lt;/option&gt;
&lt;/select&gt;</pre>

&nbsp;

{{< figure src="jQueryPaginationCSS3Animation.gif" title="jQuery Pagination CSS3 Animation" alt="jQuery Pagination CSS3 Animation" >}}

One more most important feature of jpages pagination plugin is call backing mechanism. For example you want to show page numbers information like ‘2 of 10 pages’ or Elements information like ‘1-10 of 120 Items’ we can use callback parameter in jpages plugin.

<pre>$("div.holder").jPages({
                containerID: "itemContainer",
                perPage: 3,
                callback: function (pages,
        items) {
                    $("#legend1").html("Page " + pages.current + " of " + pages.count);
                    $("#legend2").html(items.range.start + " - " + items.range.end + " of " + items.count);
                }
            });

&lt;p id="legend1"&gt;&lt;/p&gt;
&lt;p id="legend2"&gt;&lt;/p&gt;</pre>

&nbsp;

{{< figure src="jQueryPaginationCallbackMechanism.gif" title="jQueryPaginationCallbackMechanism" alt="jQueryPaginationCallbackMechanism" >}}

There are so many things to explore in this jQuery jPages Pagination plug in I covered almost all important features.Visit <a href="http://luis-almeida.github.io/jPages/" target="_blank" rel="noopener">jPages</a> home page for more feature

Here is the Final Demo <a title="Pagination Using jQuery" href="https://arungudelli.com/Tools/HTML5/SimplePaginationJQuery/SimplePagination.htm" target="_blank" rel="noopener">Pagination Using&nbsp;jQuery and&nbsp; jPages plugin</a>.

Download source code

<em><strong><a href="http://sdrv.ms/1jQNy22" target="_blank" rel="noopener">Download</a></strong></em>

I hope you have enjoyed this article.If so share this post with your friends and also join our mailing list.

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







