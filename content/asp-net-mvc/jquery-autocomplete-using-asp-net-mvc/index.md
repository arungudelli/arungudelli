+++
title="Simple JQuery Autocomplete Using Asp Net MVC"
summary="I will explain how implement jQuery Autocomplete Search using Asp .Net MVC and Twitter Typeahead js library."
keywords="jquery autocomplete,jquery ui autocomplete,jquery autocomplete example,jquery autocomplete json,jquery autosuggest,twitter typeahead,asp net,asp net mvc"
type='post'
date='2019-10-09T18:05:43+0000'
lastmod='2019-10-09T18:05:43+0000'
draft='false'
authors=['admin']
[image]
caption='Simple JQuery Autocomplete Using Asp Net MVC'
focal_point=''
preview_only=false
+++








In this tutorial I will explain how implement <span style="text-decoration: underline;"><em>jQuery Autocomplete</em></span> Search functionality using <span style="text-decoration: underline;"><em>Asp .Net MVC</em></span> and <span style="text-decoration: underline;"><em>Twitter Typeahead.js</em></span> library.

This is continuation to my previous post&nbsp;<a title="jQuery Autocomplete" href="https://www.arungudelli.com/2013/10/simple-jquery-autocomplete-search-tutorial.html" target="_blank" rel="noopener">A Simple jQuery Autocomplete Search Tutorial</a>

As I explained in my previous post&nbsp;<em>Twitter Typeahead.js is&nbsp;</em>An open source autocomplete JavaScript library by Twitter.It comes with rich set of features. I explained about ‘local’ and ‘prefetch’ attributes in that post.

And If you want to retrieve data from server as-you-type &nbsp;we have to use ‘remote’ attribute in Twitter Typeahead.js.

Open your visual studio create a simple MVC application which contains

one controller <em>HomeController.cs</em> and one view page <em>Index.aspx</em>

Add HTML Code Index.aspx view page

<pre>&lt;asp:Content ID="indexContent" ContentPlaceHolderID="MainContent" runat="server"&gt;
&lt;div class="CustomTemplate"&gt;
    &lt;input class="WordpressPosts typeahead" type="text" placeholder="My WordPress Posts" /&gt;
    &lt;/div&gt;
&lt;/asp:Content&gt;</pre>

&nbsp;

And now in the same page add following jQuery Code

<pre>&lt;link href="../../Content/examples.css" rel="stylesheet" type="text/css" /&gt;
    &lt;script type="text/javascript" src="https://twitter.github.io/typeahead.js/js/jquery-1.9.1.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="https://twitter.github.io/typeahead.js/releases/latest/typeahead.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="https://twitter.github.io/typeahead.js/js/hogan-2.0.0.js"&gt;&lt;/script&gt;
    &lt;script src="../../Content/typeahead.min.js" type="text/javascript"&gt;&lt;/script&gt;
    &lt;script type="text/javascript"&gt;
        $(document).ready(function () {
            alert('Hello');
            $('.WordpressPosts').typeahead({
                name: 'Wordpress',
                valueKey: 'name',
                remote: 'Home/GetData?q=%QUERY',
                template: [
    '&lt;p class="repo-tag"&gt;{{tag}}&lt;/p&gt;',
    '&lt;p class="repo-name"&gt;{{name}}&lt;/p&gt;',
    '&lt;p class="repo-description"&gt;{{description}}&lt;/p&gt;'
  ].join(''),
                engine: Hogan
            });

        });

    &lt;/script&gt;</pre>

&nbsp;

Everything is same as previous example except for the “remote” attribute.

<pre>remote: 'Home/GetData?q=%QUERY'</pre>

&nbsp;

The code is straight forward we are passing queryString to a method called GetData() which return jSon data based upon input query in HomeController.

Typeahead.js &nbsp;‘%QUERY’ &nbsp;keyword will give input search keyword which is a queryString to server.

Now we will define GetData() method in HomeController.cs file

<pre>namespace AutoComplete.Controllers
{
    public class TagSys
    {
        public string tag { get; set; }
        public string name { get; set; }
        public string description { get; set; }

        public TagSys()
        {
            //
            // TODO: Add constructor logic here
            //
        }

        public List&lt;TagSys&gt; GetTagList()
        {
            List&lt;TagSys&gt; list = new List&lt;TagSys&gt;();
            list.Add(new TagSys() { tag = "HTML5", name = "HTML5 LocalStorage API", description = "HTML5 LocalStorage API,Client Side Storage" });
            list.Add(new TagSys() { tag = "HTML5", name = "HTML5 GeoLocations API", description = "HTML5 GeoLocations API,Used to Find Location" });
            list.Add(new TagSys() { tag = "JavaScript", name = "JavaScript Tips And Tricks", description = "Some Useful Javascript tips and tricks" });
            list.Add(new TagSys() { tag = "JavaScript", name = "JavaScript Tutorials", description = "JavaScript Tutorials" });
            list.Add(new TagSys() { tag = "CSS3", name = "CSS3 Tutorials", description = "CSS3 Tutorials" });
            list.Add(new TagSys() { tag = "CSS3", name = "CSS3 Animations", description = "CSS3 Animations" });
            return list;
        }
    }
    public class HomeController : Controller
    {
        public JsonResult GetData(string q)
        {
            var list = new TagSys();
            var fetchTag = list.GetTagList().Where(m =&gt; m.name.ToLower().StartsWith(q.ToLower()));
            return Json(fetchTag, JsonRequestBehavior.AllowGet);
        }
    }
}</pre>

&nbsp;

I defined one class called TagSys which contains tag,name,description as properties. And I added one method called GetTagList() which setups some hard coded data.

We can get the data from Database also but to simplify the code I am hard coding here. You can add your own Database Logic to retrieve data based upon queryString.

And I declared GetData() method which takes queryString as input and return jSon data based upon queryString. The Logic is straight forward no need to explain.

And the Demo will look like this.

{{< figure src="jQueryAutoComplete.gif" title="jQuery Auto Complete using Asp Net MVC" alt="jQuery Auto Complete using Asp Net MVC" >}}

It same as previous example the difference is previous example uses ‘prefetch’ attribute which stores Json data in localStorage where as this ‘remote’ attribute return the results as-you-type from Server.

<span style="text-decoration: underline;"><em><strong>Bonus Tip:</strong></em></span><em><strong>&nbsp;</strong><a href="https://www.arungudelli.com/csharp/delegates-and-events-in-csharp/" target="_blank" rel="noopener">Understand C# Delegates with simple real world examples</a></em>

Download the source code for <a title="Source Code" href="http://sdrv.ms/GY7k9Q" target="_blank" rel="noopener">jQuery autocomplete using Asp Net MVC.</a>

I hope you have enjoyed this article.If so share this post with your friends and also join our mailing list.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.









