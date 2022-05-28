+++
title="NDepend – A Static Code Analysis Tool"
summary="In this post I am going to review one of the static code analysis tool Ndepend by Patrick Smacchia. Before that I would like to explain few things about Static"
keywords=["csharp,ndepend,ndepend review,c#"
]
type='post'
date='2019-10-24T18:04:17+0000'
lastmod='2019-10-24T18:04:17+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

In this post I am going to review one of the static code analysis tool&nbsp;<a title="ndepend" href="http://www.ndepend.com/" target="_blank">Ndepend</a> by Patrick Smacchia. Before that&nbsp;I would like to explain few things about Static Analysis of Code.

### <span style="text-decoration: underline;"><strong>Static Analysis of Code:</strong></span>

I would like to quote the great Alan Turing (Father of computing) words here

”There is no automated (or mechanical method) and completely reliable way to decide whether a program will work without any errors”

This is the result of experiment done by Turing in the 1930s which lead to Undecidable problem. (Please Google for more details).

But due to the complexity of modern software, it’s impossible to read and review entire source code of a program. We need a smart automated tool or software to do the same.

I have been coding in C# from last 3 years after my graduation. When I first heard about static analysis code tools I used to have few assumptions or I can say myths which are proved to be wrong after some time.

<ul><li>Static analysis tools does not actually execute the Code, they examine the source code based on few rules and regulations gives information to the user (For instance language compiler also a static analysis code tool eg:c# compiler list out the unused variable as warning).</li><li>Testing and static analysis are not the same. A code analysis tool will examine the code give some warnings, if you are not getting any warnings that indicates the quality of code. But at the same if you are getting warnings that don’t mean that your code is buggy. But with these tools you can find hard to catch errors (eg: Object reference not set to an instance of an object, yes if you are new to C# you cannot escape this error J) and edge case scenarios that can cause problems in near future so that we can fix them in early phase of development.</li></ul>

I have not used any quality tool till now, I was asked to review Ndepend static code analysis tool for C#, Thanks to Patrick Smacchia, I learnt few things about static analysis tools, purpose of them and Here is my experience with Ndepend.

### <span style="text-decoration: underline;"><strong>NDepend static Code Analysis Tool:</strong></span>

First I took a visual studio project for instance I examined a simple MVC application. (Installing Ndepend and integrating it with visual studio you can have a look at the Videos and tutorials in Ndepend official Website)

It takes few minutes to analyze the project for the first time generates reports about current project.

The reports consists

<ul><li>Application Metrics like Lines Of Code, percentage of comments, method complexity, code coverage etc.</li><li>Few graphs like Dependency graph, Dependency metrics, Tree map view etc.</li><li>And also few predefined rules violation details</li></ul>

Please have a look at the below screenshot for more details

{{< figure src="NdependDashboard.png" title="Ndepend Dashboard" alt="Ndepend Dashboard" >}}

You might be thinking these reports we can get it with other static analysis code tools as well, but the real exciting feature of Ndepend is Code Query LINQ.

For example to get all methods having lines of Code more than 50 lines we can simply open the CQ linq editor and write

<pre>SELECT METHODS WHERE NbLinesOfCode &gt; 50</pre>

&nbsp;

And to know whether code is properly commented or not

<pre>SELECT METHODS WHERE NbLinesOfCode &gt; 50 AND&nbsp; NbLinesOfComment &lt; 10</pre>

&nbsp;

And know methods which are having high CyclomaticComplexity just type the following query

<pre>SELECT METHODS WHERE CyclomaticComplexity &gt; 20</pre>

&nbsp;

And double click on the methods you can directly edit them in visual studio.

When you run analysis NDepend will check against few built-in code quality queries

{{< figure src="NdependRules.png" title="Ndepend Rules" alt="Ndepend Rules" >}}

&nbsp;

I have received one warning saying “Instances size shouldn’t be too big” when I click on the warning it displays query

<pre>// &lt;Name&gt;Instances size shouldn't be too big&lt;/Name&gt;
warnif count &gt; 0 from t in JustMyCode.Types where
&nbsp; t.SizeOfInst &gt; 64
&nbsp; orderby t.SizeOfInst descending
select new { t, t.SizeOfInst, t.InstanceFields }
And it contains nice explanation, which is new to me.
// Types where SizeOfInst &gt; 64 might degrade performance
// (depending on the number of instances created at runtime)
// and might be hard to maintain. However it is not a rule
// since sometime there is no alternative (the size of
// instances of the System.Net.NetworkInformation.SystemIcmpV6Statistics
// standard class is 2064 bytes).
// Notice that a class with a large SizeOfInst value
// doesn't necessarily have a lot of instance fields.
// It might derive from a class with a large SizeOfInst value.
// See the definition of the SizeOfInst metric here
// http://www.ndepend.com/Metrics.aspx#SizeOfInst</pre>

&nbsp;

I learnt so many quality code rules while experimenting with NDepend

For example under .Net framework usage category I saw a rule saying

Don’t create threads explicitely : which consist a nice explanation

<pre>// Prefer using the thread pool instead of
// creating manually your own thread.
// Threads are costly objects.
// They take approximately 200,000 cycles to
// create and about 100,000 cycles to destroy.&nbsp;
// By default they reserve 1 megabyte of virtual
// memory for its stack and use 2,000-8,000
// cycles for each context switch.
// As a consequence, it is preferrable to let
// the thread pool recycle threads.
// Creating custom thread can also be the
// sign of flawed design, where tasks and
// threads have affinity. It is preferrable
// to code tasks that can be ran on any thread.</pre>

&nbsp;

Here I am listing out few quality code rules by Ndepend

<ul><li>Types should not extend System.ApplicationException</li><li>Collection properties should be read only</li><li>UI layer shouldn’t use directly DB types</li></ul>

Internally the tool executing few queries to generate reports in user friendly format. So if you are familiar with the query language you&nbsp;can write our own custom queries and you&nbsp;can generate our own reports.

And also the tool generates few graphs explaining about your code quality.

I tried summarize the important features of NDepend in this post. I recommend you people to install Ndepend trail version and explore the features on your own.

You can see complete list of NDepend features here <a href="http://www.ndepend.com/Features/" target="_blank">http://www.ndepend.com/Features/</a>

### <span style="text-decoration: underline;"><strong>Final Word:</strong></span>

As a C# developer, I found NDepend very useful and I really think that the CQLinq language best feature of the tool. I did some research on other tools as well, but didn’t find anything as good as <a title="ndepend" href="http://www.ndepend.com/" target="_blank">NDepend</a>.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







