+++
title="Checked And UnChecked Keywords In C#"
summary="C# Tutorial explains checked,unchecked contexts with examples. C# unchecked context ignores arithmetic overflows & in C# checked context not."
keywords="checked and unchecked in c#,checked keyword in c#,unchecked keyword in c#,checked and unchecked context in c#,c#"
type='post'
date='2019-10-23T18:04:23+0000'
lastmod='2019-10-23T18:04:23+0000'
draft='false'
authors=['admin']
[image]
caption='Checked And UnChecked Keywords In C#'
focal_point=''
preview_only=false
+++


In this tutorial I will explain about little known keywords called <span style="text-decoration: underline;"><em><strong>checked</strong> </em></span>and <span style="text-decoration: underline;"><em><strong>unchecked</strong> </em></span>in C#.

I came to know about these keywords accidentally, I will share the story with you people.

One of my friends’s project simple&nbsp;<span style="color: #2a2a2a;">arithmetic addition failing and returning some garbage value (No exceptions). The code is something like this</span>

<pre>NumberOfOrders = NumberOfOrders+newOrders; 
Console.WriteLine(NumberOfOrders);</pre>

&nbsp;

{{< figure src="CheckedandUnchecked.png" title="CheckedandUnchecked" alt="CheckedandUnchecked" >}}

&nbsp;

The NumberOfOrders and newOrders are integer variables and after couple of minutes of investigation&nbsp;we came to know that it got reached it’s maximum value, To our surprise there is no compile time error as well as runtime error.

<pre>int x = int.MaxValue;   //2147483647
int y = x + x;          //No Exception
Console.WriteLine(y);   //Prints -2</pre>

&nbsp;

Then we came to know about <em><strong>checked</strong> </em>and <em><strong>unchecked</strong> </em>keywords.

In C# language we have two types of execution contexts <em><strong>checked</strong> </em>and <em><strong>unchecked</strong></em>(Which is very new to me). And this context is depend on compiler most of the cases it’s unchecked.

In Unchecked context arithmetic exceptions are ignored and result will be truncated. The following operations are affected due to this contexts

<ul><li>Statements using <span style="color: #2a2a2a;"><span class="input" style="font-weight: bold;">++</span>&nbsp;</span><span style="color: #2a2a2a;">&nbsp;&nbsp;&nbsp;</span><span style="color: #2a2a2a;"><span class="input" style="font-weight: bold;">—</span></span><span style="color: #2a2a2a;">&nbsp;&nbsp;&nbsp;– (unary)&nbsp;&nbsp;&nbsp;</span><span style="color: #2a2a2a;"><span class="input" style="font-weight: bold;">+</span></span><span style="color: #2a2a2a;">&nbsp;&nbsp;&nbsp;–&nbsp;&nbsp;&nbsp;</span><span style="color: #2a2a2a;"><span class="input" style="font-weight: bold;">*</span></span><span style="color: #2a2a2a;">&nbsp;&nbsp;&nbsp;</span><span style="color: #2a2a2a;"><span class="input" style="font-weight: bold;">/ &nbsp;</span>on integral&nbsp;types(byte ,char, short, int, long variables types).</span></li><li>Explicit numeric conversions between integral types.</li></ul>

{{< figure src="Overflowgif.gif" title="Checked and UnChecked Csharp" alt="Checked and UnChecked Csharp" >}}

So the correct code will be

<pre>checked
{
      int x = int.MaxValue;
      int y = x + x;
      Console.WriteLine(y);
}</pre>

&nbsp;

Just include the code in “<em><strong>checked</strong></em>” block. And now at runtime code will through arithmetic overflow exception. So to handle the exception I will add try catch blocks. So the final code is

<pre>            checked
            {
                try
                {
                    int x = int.MaxValue;
                    int y = x + x;
                    Console.WriteLine(y);
                }
                catch (Exception exception)
                {
                    Console.WriteLine(exception);
                }
            }</pre>

&nbsp;

Now you might be thinking that why we required two contexts , instead we can maintain only one <em><strong>checked</strong> </em>context. In real world projects chances of getting arithmetic overflow exceptions are very low(that’s why default context is unchecked).

So checking for exceptions for each such statements at runtime will be extra overhead for CLR. So the&nbsp;code that might cause overflow exception should be executed in a <em><strong>checked</strong> </em>context.Remaining code will be executed in <em><strong>unchecked</strong> </em>environment for which performance is priority

The ideal solution for this is to write code like below

<pre>            checked
            {
                // Code that might cause overflow should be executed in a checkd
                // environment. 
                try
                {
                    int x = int.MaxValue;
                    int y = x + x;
                    Console.WriteLine(y);
                }
                catch (Exception exception)
                {
                    Console.WriteLine(exception);
                }
                unchecked
                {
                    /*
                     this block will contain normal statements which will not cause overflow exceptions
                     * And performence will be priority her.
                     */
                    int z = 2 + 10;
                    Console.WriteLine(z);
                }
                // checked code here. 
            }</pre>

&nbsp;

### &nbsp;Checked and Unchecked contexts with Constant variables:

For constant variables compiler itself will throw the error “Overflow in constant value computation”.

<pre>            const int a = int.MaxValue;
            int b = a + 10;</pre>

&nbsp;

The above code will not compile and throws the error. And If you want to skip the exception just execute them in unchecked context as shown below

<pre>            unchecked
            {
                const int a = int.MaxValue;
                int b = a + 10;
                //Some garbage value will be stored in b
            }</pre>

&nbsp;

We can specify the context for single statements also as shown below.Just add the <em><strong>checked</strong> </em>or <em><strong>unchecked</strong> </em>keyword before the statements and enclose the statements in brackets.

<pre>            int z1 = int.MaxValue;
            int z2 = checked(z1 + z1);</pre>

&nbsp;

<span style="color: #000000;">I hope you’ve enjoyed this article and that it gives you more ideas on&nbsp;<span style="text-decoration: underline;"><em><strong>checked</strong></em>&nbsp;</span></span><span style="color: #000000;">and&nbsp;<span style="text-decoration: underline;"><em><strong>unchecked</strong></em></span></span><span style="text-decoration: underline;"><strong style="color: #000000; text-decoration: underline;">&nbsp;</strong></span>keywords<span style="color: #000000;">&nbsp;in C# .If so share this post with your friends, follow me on social networks and also join our mailing list.&nbsp;</span>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







