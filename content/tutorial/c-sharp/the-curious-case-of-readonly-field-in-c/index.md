+++
title="The Curious Case Of Readonly Field In C#"
summary="Readonly modifier in C# used to declare variables constant. & this readonly keyword applicable only to fields not locals."
keywords="c#,readonly field in c#,readonly variable in c#,readonly"
type='post'
date='2019-10-27T18:04:01+0000'
lastmod='2019-10-27T18:04:01+0000'
draft='false'
authors=['admin']
[image]
caption='The Curious Case Of Readonly Field In C#'
focal_point=''
preview_only=false
+++








Readonly keyword is a modifier in C# when it applied to a field, the value of the field can be assigned at the time of declaration or in constructor only not in any other methods. After that we cannot change the value.

But most of the people I discussed will compare it with constant field. But Readonly field is different from constant field. And often it is misunderstood.

And Readonly&nbsp;modifier can be applied only to the Fields not local variables.

First of all Readonly value is not constant it may be different depending upon object created. So its <strong><em>Constant to the object created</em></strong>

{{< figure src="Readonly-keyword.png" title="Readonly field in C#" alt="Readonly field in C#" >}}

### <span style="text-decoration: underline;">Readonly field in C#:</span>

&nbsp;

As mentioned above we can assign the C# readonly fields in constructor. But a class may be having multiple constructors, in that case, the value will be different depending upon the constructor used.

Please see the following example

<pre>public class ReadonlyClass
{
  // Assing a readonly field
  public readonly int discount;

  public ReadonlyClass()
  {
    discount = 10;
  }
  
  public ReadonlyClass(int _discount)
  {
    discount = _discount;
  }
}
</pre>

For example, a customer gets by default 10% discount on the product. Often in some special cases if we want to increase the discount or decrease the discount we will use another constructor to create an object.

<pre>var customer1 = new ReadonlyConstant.ReadonlyClass();

Console.WriteLine("Discount :{0}",customer1.discount);

//Discount : 10

var customer2 = new ReadonlyConstant.ReadonlyClass(20);

Console.WriteLine("Discount :{0}", customer2.discount);

//Discount : 20

//customer1.discount = 5; This is wrong

//customer2.discount = 10; This is wrong

</pre>

So for the customer1 discount is 10 and it is constant to the customer 1. For customer 2 discount is 20 and it is constant for the customer 2.

After assigning the value in constructor we cannot change it it will show following error.

{{< figure src="Readonly-Field-example.png" title="Readonly Field in C#" alt="Readonly Field in C#" >}}

So the readonly field value constant to the object created. To make it constant across the object add static keyword.

I explained about static readonly in differences between constant vs readonly variables article.

### <span style="text-decoration: underline;">We can pass C#&nbsp;<span style="text-decoration: underline;">readonly</span>&nbsp;fields as ref or out parameters in Constructor Context:</span>

&nbsp;

As the readonly&nbsp;fields can be assigned inside the constructor we can pass them as ref or out parameters inside the constructor context as shown below.

<pre>public class Program
{
 public readonly int z = 5;
 public readonly int y;
 public static readonly int x = 1;
 
 static void printOut(out int v)
 {
  v= 0;
  Console.WriteLine(v);
 }

 static void printRef(ref int v)
 {
  v = 90;
  Console.WriteLine(v);
 }

 public void NormalMethod()
 {
    //printOut(ref y); This is wrong
    //printRef(out y);
 }

 //Normal Constructor
 public Program()
 {
  y = 9;
  z = 90;
  z = 9000;
  printOut(out z);
  printRef(ref z);
  //The value of y is 90
 }

 //Static constructor
 static Program()
 {
   x = 3;
   x = 9;
   printOut(out x);
   printRef(ref x);
   //The value of x is 90
 }
}</pre>

&nbsp;

But we cannot pass them in any other methods in above example we cannot pass readonly field y in NormalMethod() as ref or out parameter because its not in constructor context.

<a href="https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/" target="_blank" rel="noopener">Understand difference between ref and out parameters in c#</a>

### 

### <span style="text-decoration: underline;">Do not declare mutable types like arrays collections as readonly in C#:</span>

&nbsp;

Please go through the following article

<a href="https://www.arungudelli.com/tutorial/c-sharp/10-differences-between-constant-vs-readonly-static-readonly-fields/" target="_blank" rel="noopener">Difference between </a>readonly, constant and static readonly in C#

As mentioned above article in differences we should not assign mutable types to readonly because only the reference cannot be changed but the object that holds can be changed.

Please see the below example.

<pre>public class ReadonlyCollection
 {
&nbsp; public readonly List&lt;int&gt; readonList;

&nbsp; public ReadonlyCollection()
&nbsp;{
&nbsp; &nbsp;readonList = new List&lt;int&gt;() {1,2};
&nbsp;}

}

var readcollection = new ReadonlyCollection();

readcollection.readonList[0] = 3;

readcollection.readonList[1] = 4;

//But this is wrong
//readcollection.readonList = new List&lt;int&gt;();

</pre>

We can change the values of readonly list as shown above.

But If we you want to assign it to new collecation it will throw error because only reference is immutable not the object that holds.

{{< figure src="Readonly-field-mutable.png" title="Readonly field in C# with mutable types" alt="Readonly field in C# with mutable types" >}}

&nbsp;

I hope this article clears the most common doubts about Readonly keyword modifier in C#.

If you have any doubts feel free to comment below.

Read my article on <a href="https://www.arungudelli.com/tutorial/c-sharp/delegates-and-events-in-c-sharp/" target="_blank" rel="noopener">Delegates and Events in c#</a>

Happy Coding..!

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







