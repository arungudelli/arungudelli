+++
title="Understanding Delegates And Events In C# / .Net Simplified : C# Tutorial"
summary="Delegates and Events in C# are used to implement event handlers in C#.Delegate in C# is a reference to a method & Events in C# adds extra abstraction to Delegates.you will understand difference between Delegate and events after reading this C# tutorial."
keywords=["c# delegate,delegates in c#,delegate c#,delegates c#,c# delegate event,c# events and delegates,c# delegates tutorial,multicast delegates in c#,delegate in c#,c# delegate example,advantages of delegates in c#,c# delegates explained,c#"
]
type='post'
date='2019-10-12T18:05:30+0000'
lastmod='2019-10-12T18:05:30+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

This C# tutorial explains all the basics of <span style="text-decoration: underline;"><em>C# Delegates and Events</em></span>, &amp; Where to use Delegates in our daily projects.

You might read so many definitions like

<ul><li><span style="text-decoration: underline;"><em>C# Delegate</em></span> similar to functional pointer in C++ but type safe</li><li>A delegate can point to a method, which is having same signature as that of the delegate.</li><li>With the use of delegates we can call methods asynchronously.</li><li>Delegates and events can be used to implement publisher-Subscriber models. &nbsp; labla labla labla……………………….</li></ul>

{{%toc%}}

{{< figure src="What-are-Delegates-and-Events.jpg" title="What are Delegates and Events in C#" alt="What are Delegates and Events in C#" >}}

But What is the purpose of having delegates &amp; Events in C#? If you understand the use of delegates,events then we can apply them in our daily projects.

### <span style="text-decoration: underline;">What is a Delegate?</span>

Lets forgot about C# for a while, a quick google search will tell a Delegate is a person who authorised to represent others. For example companies send their delegates to conferences to represent their products(because CEO might be busy with other things).

The CEO defines certain responsibilities to delegates (in advance)

<ul><li>What has to be done &nbsp;(in programming world function)</li><li>What he should talk &nbsp;(say parameter)</li><li>Collect feedback or get new customers (return value).</li></ul>

Now the CEO select one delegate for the conference when needed (say at run time)

Now if you read above definition a delegate can invoke a method which is having a same signature as that delegate. Confused??

I will try to explain the use of <em>delegates &amp; Events with simple C# examples</em> so that at the end of this post you will have clear picture on Delegates and Events.

### <span style="text-decoration: underline;">C# Delegate Example:</span>

See the below example

<pre>//A simple C# Calculator class which will do arithmetic operations 
public class Calculator
    {
        public int Add(int x, int y){}
        public int Sub(int x, int y){}
        public int Multi(int x, int y){}
        public int Div(int x, int y){}
    }</pre>

&nbsp;

Our client(say console application) will use above Calculator class to do maths operations. Console application will take two arguments

<pre>int operatorX = Convert.ToInt32(args[0]);
int operatorY = Convert.ToInt32(args[1]);
Calculator obj=new Calculator();
obj.Add(operatorX,operatorY);
obj.Sub(operatorX,operatorY);
obj.Multi(operatorX,operatorY);
obj.Div(operatorX,operatorY);</pre>

&nbsp;

The Code looks fine and it will work perfectly but if you observe carefully client (console application) and our class are tightly coupled.

Say for example I want to calculate LCM (Least Common Multiple) of two numbers. We will add method in Calculator class and call that method in our client(Console application).

<pre>//Add method in Calculator Class
public LCM(int x,int y){}

// And in client sidere
obj.LCM(x,y);</pre>

&nbsp;

Both are tightly coupled that means both Class and Client needs to be compiled in order to affect the changes.

This problem can be solved with the use of Delegates. Before that I will explain a simple delegate example and then will solve the above problem

### <span style="text-decoration: underline;">A Simple C# Delegate:</span>

Follow the below steps to create a Delegate

<ul><li>Define &nbsp;: Define a Delegate</li><li>Create &nbsp;: Create a Delegate object to assign</li><li>Refer or Point : Point to reference of a Method</li><li>Invoke : Finally Call or Invoke the delegate</li></ul>

Delegates definition syntax

<pre>delegate returntype delegateName (parameters);</pre>

&nbsp;

For example see the below example.”SumDelegate” is a delegate which can refer functions which takes two integer parameters and returns one integer.

<pre>delegate int SumDelegate(int x,int y);</pre>

&nbsp;

Create a Delegate Object

<pre>SumDelegate objDelgate=null;</pre>

&nbsp;

We will use the above delegate to Call sum method which will add two numbers. In third steps we have to assign delegate to reference of a method

<pre>objDelegate=Sum;</pre>

&nbsp;

And in the final step invoke the delegate

<pre>objDelegate.Invoke(x,y);</pre>

&nbsp;

Final example

<pre>    //Define a Delegate
    delegate void SumDelegate(int x,int y);

    static void Main(string[] args)
    {
        //Declare Delegate Objetc
        SumDelegate objDelegate= null;

        //Point to method reference in our example "Sum"
        objDelegate=Sum;

        //Final Step Invoke Delegate
        objDelegate.Invoke(10, 20);
        Console.Read();
    }

    static void Sum(int x,int y)
    {
        Console.WriteLine((x+y).ToString());
    }</pre>

&nbsp;

So What is the advantage? We can directly call the Sum method right why we have to use Delegate?

With the use of Delegates we call or assign methods at run time. How?

Going back to our problem we will slightly modify our Calculator as shown below

<pre>        //Declare Delegate
        public delegate int CalculatorDelegate(int x, int y);

        //Create Delegate Reference
        CalculatorDelegate delegateObj = null;

        //Depending upon request we will assign Delegate
        public CalculatorDelegate GetDelegateRef(int intoperation)
        {
            //And Finally assign based on request
            switch (intoperation)
            {
                case 1:
                    delegateObj = Add;
                    break;
                case 2:
                    delegateObj = Sub;
                    break;
                case 3:
                    delegateObj = Multi;
                    break;
                case 4:
                    delegateObj = Div;
                    break;
                default: break;
            }
            return delegateObj;
        }
        private int Add(int x, int y){}
        private int Sub(int x, int y){}
        private int Multi(int x, int y){}
        private int Div(int x, int y){}</pre>

&nbsp;

We Declare a Delegate “CalculatorDelegate” which takes two int parameters and returns int.This delegate can refer methods like Add,Sub,Multi,Div etc.

<pre>public CalculatorDelegate GetDelegateRef(int intoperation){}</pre>

&nbsp;

The above method GetDelegateRef() is used to get delegate reference i.e., which method to call(Add,Sub,Multi etc) &nbsp;based upon request from clients.

We will modify our client code slightly as shown below

<pre>int intoperation = Convert.ToInt32(args[0]);
int operatorX = Convert.ToInt32(args[1]);
int operatorY = Convert.ToInt32(args[2]);

Calculator obj=new Calculator();</pre>

&nbsp;

Console client will take three arguments first argument decides which operation to perform and 2nd , 3rd arguments are used for calculations.

And for invoking

<pre>obj.GetDelegateRef(intoperation).Invoke(operatorX, operatorY);</pre>

With the use of GetDelegateRef() method at run time we will know which method to call and then Invokes the delegate.

Now if you want to Add LCM operation simply add it to Calculator Class (if intoperation=5 assign delegate to LCM method) and no need to change any code at client side, at run time we will decide which operation to invoke. No need to compile client code.

That means we are decoupling client from our Class with the help of Delegates. <span style="text-decoration: underline;"><em>Whenever we introduce any features try to avoid changes at client side</em></span>

### <span style="text-decoration: underline;">Multicast Delegate in C#&nbsp;:</span>

In the above example the delegate object pointing to single function or method at a time.

But delegate object has the capability of holding multiple method references and whenever we invoke delegate object it will call those methods one by one. That is Called “Multicast delegate”(Naming convention only).

We will be having <span style="text-decoration: underline;"><em>only a Delegate</em></span> depending upon its usage we call it either Delegate or Multicast Delegate. See the below example

<pre>CalculatorDelegate delegateObj = null;
delegateObj +=Add;
delegateObj +=Sub;
delegateObj +=Multi;

//Performs Add,Sub,Multi one by one.
delegateObj.Invoke(10,20);</pre>

&nbsp;

### <span style="text-decoration: underline;">Purpose Of Multicast Delegate in C#:</span>

So where we &nbsp;can use multicast delegates in our daily projects.Everyone will have Facebook account rite. Whenever we get any notifications we will be receiving SMS and as well as emails.

Facebook will publish notifications and we will receive notifications to Mobile and Email.This is like publisher and subscriber Model.

{{< figure src="publisherAndSubscriberDelegate.png" title="publisher And SubscriberDelegate" alt="publisher And SubscriberDelegate" >}}

In this kind of publisher &amp; Subscribers model we can use Multicast Delegates. We will go through one simple example to understand it better.

<pre>//Subscribers
    public class SendViaMobile
    {
        public void sendMessage(string msg)
        {
            Console.WriteLine("Send to Mobile"+msg);
        }
    }
    public class SendViaEmail
    {
        public void sendEmail(string msg)
        {
            Console.WriteLine("Send to EMail"+msg);
        }
    }

    //Publisher
    public class Publisher
    {
        //Declare Delegate
        public delegate void PublishMessageDel(string msg);

        //Define Delegate
        public PublishMessageDel publishmsg = null;
        //Method used to Invoke Delegate
        public void PublishMessage(string message)
        { 
            //Invoke Delegate
            publishmsg.Invoke(message);
        }
    }</pre>

&nbsp;

The Code is easy to Understand I declared two Subscribers “SendViaEmail” and “SendViaSMS”. And in publisher class I declared one Delegate which takes string parameter and returns void.

And For invoking delegate I wrote one more method called “PublishMethod” &nbsp;(You will understand why I wrote this method at the end of this post)

And To test the application we will write one Console Application

<pre>Publisher publisher = new Publisher();

SendViaEmail SE = new SendViaEmail();
SendViaMobile SM = new SendViaMobile();

publisher.publishmsg += SE.sendEmail;
publisher.publishmsg += SM.sendMessage;

publisher.PublishMessage("Hello You Have received New Notification");</pre>

&nbsp;

But the problem with the above code is it’s more over like “Master and Slave model”.

That means You are not subscribed to Mobile notifications but still Facebook sending notifications to your mobile.

In the above code subscribers do not have rights to decline notifications.Publisher only sending notifications irrespective of subscriber interests.This is not ideal Publisher/Subscriber Model.&nbsp;First Subscribers has to subscribe for notification then only it should receive notifications.

So we will slightly modify above code to look like Publisher/Subscriber Model.

<pre>public class SendViaMobile
{
        private void sendMessage(string msg)
        {
            Console.WriteLine("Send to Mobile:" + msg);
        }
        public void Subscribe(Publisher pub)
        {
            pub.publishmsg += sendMessage;
            //pub.publishmsg = null;
        }
}</pre>

&nbsp;

I added one method called Subscribe() which takes Publisher Object as parameter and decides whether to receive notifications or not.Subscribe Method assigns Delegate to corresponding methods(I declared Method as private).And it can assign any number of methods to delegate like For example “SendViaMobile” wants to save the notifications in Log files So internally it can define one method which is same signature as Delegate and assign it to Delegate Object.

So in our console application we have to call subscribe method before invoking the delegate.

<pre>Publisher publisher = new Publisher();

SendViaMobile SM = new SendViaMobile();
SendViaEmail SE = new SendViaEmail();

//Subscribing for Mobile notifications
SM.Subscribe(publisher);

//Emails are not subscribed so it wont receive notifications via Email
//SE.Subscribe(publisher);

//Invoking the delegate Only Mobile will receive notifications.
publisher.PublishMessage("Hello You Have New Notifications");</pre>

&nbsp;

“SendViaEmail” not subscribed(I put it in comments) to notifications so it wont receive any notifications.

So far everything is Good But here we are ignoring one serious issue “<span style="text-decoration: underline;"><em>We are exposing Delegate to Subscribers</em></span>” So what ? what happens if we expose to subscribers?

In the the above code “SendViaMobile” class, In subscribe method I wrote one Line

//pub.publishmsg = null;

<pre>public void Subscribe(Publisher pub)
{
            pub.publishmsg += sendMessage;
            //pub.publishmsg = null;
}</pre>

&nbsp;

Just remove the comment line that means we assigning delegate object to ‘null’

And in our client code

Publisher publisher = new Publisher();<br>
SendViaMobile SM = new SendViaMobile();<br>
SendViaEmail SE = new SendViaEmail();<br>
SE.Subscribe(publisher);<br>
SM.Subscribe(publisher);<br>
publisher.PublishMessage(“Hello You have new Notifications”);

First I subscribed Email and then mobile. But In Mobile Subscribe class we assigned delegate to null. That means even Email also do not receive any notifications.

And also Subscriber can invoke our delegate.

{{< figure src="Delegate-Problem.png" title="C# Delegate Problem" alt="C# Delegate Problem" >}}

&nbsp;

that means we are violating Encapsulation principle

So What is the solution?

<ul><li>We should not expose delegate to subscribe (In that case it will become Master Slave Model)</li><li>If we expose also we should not give permissions to subscriber to change or invoke delegate.That means it should only assign some methods or functions to Delegate.</li></ul>

The Second solution seems to be good right. <span style="text-decoration: underline;"><em>That’s how Events Came into Picture</em></span>.

### <span style="text-decoration: underline;">The purpose of Events in C#:</span>

As explained above Events can solve the problem of exposing delegates to subscribers to achieve ideal Publisher/Subscriber Model.

See the below example

<pre>public delegate void PublishMessageDel(string msg);
public event PublishMessageDel publishevent=null;

//Just Add "event" keyword before delegate object declaration</pre>

&nbsp;

The invoking and everything is same as above

And if want to change &nbsp;or invoke delegate from other classes it will throw following error

{{< figure src="DelegateEvent.png" title="Delegate and Events in C#" alt="Delegate and Events in C#" >}}

That means we cannot invoke or change the delegate event in outside classes other than Publisher Class. That’s the reason I wrote&nbsp;PublishMessage() method in Publisher class. This method will invoke the delegate event internally. The outside classed can call PublishMessage() method to invoke delegate.

<ul><li>Events are invoked in within the class itself.</li><li>Outside classes do not have access to invoke the Delegate Event.</li><li>It can appear only on left hand side of += or -= that means only appending or removing allowed No assignment.</li></ul>

That means <span style="text-decoration: underline;"><em>Event will hide the sensitive data of Delegate and exposes necessary data</em></span> to outside world.This is the ideal example of Encapsulation principle in OOPS.

I hope you understand the difference between Delegates and Events in C#.

One more use of Delegates is it’s used to call methods&nbsp;asynchronously.

### <span style="text-decoration: underline;">Delegates and Asynchronous Method Calls:</span>

What are Asynchronous method calls? Some times we need to perform a large task. But we don’t want to wait till the task ends so that we can perform other tasks.

And whenever the large task ends we need to receive a notification whether it is success or not. In real world we call this as asynchronous execution of task.

We can easily achieve this with the use of Delegates.

<pre>public class AsynchDelegate
    {
        delegate string AsynchDel();
        public static void Main(string[] args)
        {
            AsynchDel delegateObj = LargeTask;
            delegateObj.BeginInvoke(new AsyncCallback(CallBackLargeTask), delegateObj);
            Console.WriteLine("New task is started!");
            Console.Read();
        }
        public static void CallBackLargeTask(IAsyncResult asyncResult)
        {
            AsynchDel doLargeTask = (AsynchDel)asyncResult.AsyncState;
            string message = doLargeTask.EndInvoke(asyncResult);
            Console.WriteLine(message);
        }
        public static string LargeTask()
        {
            Thread.Sleep(3000);
            return "success";
        }
    }</pre>

&nbsp;

The code is straight forward and easy to understand

<ul><li>Assigned LargeTask() to delegate object.</li><li>Invoke delegate using .BeginInvoke()</li><li>First parameter is callback mechanism(In our case ‘CallBackLargeTask’) and second one is delegate object.</li><li>Callback mechanism is responsible for sending notification back to client.</li><li>We will use .EndInvoke() Method to get the success message.</li></ul>

&nbsp;<a href="http://sdrv.ms/196Agb1" target="_blank" rel="noopener noreferrer">Click here</a>&nbsp;to Download source Codes





Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







