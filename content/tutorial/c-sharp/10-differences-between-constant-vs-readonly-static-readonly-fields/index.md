+++
title="C# Const, ReadOnly & Static ReadOnly Differences"
summary="C# Const makes fields or locals constant.ReadOnly applies to fields in C#, value is constant after initialization.Static ReadOnly makes ReadOnly field class member."
keywords="c#,readonly field in c#,const field in c#,static readonly in c#,const vs readonly,"
type='post'
date='2019-11-16T20:52:29+0000'
lastmod='2019-11-16T20:52:29+0000'
draft='false'
authors=['admin']
[image]
caption='C# Const, ReadOnly & Static ReadOnly Differences'
focal_point=''
preview_only=false
+++








C# Const makes fields or locals constant.ReadOnly applies to fields in C#, value is constant after initialization.Static ReadOnly makes ReadOnly field class member.(Can be accessed through class name)

Please go through the summary of differences between const and readonly then I will try to explain each point after that.

## Table Of Contents:

<ul><li><a href="#step-1">Const vs Readonly in C#</a></li><li><a href="#step-2">C# Const field or local</a></li><li><a href="#step-3">C# ReadOnly Field</a></li><li><a href="#step-4">Versioning problem of the Const field in C#</a></li><li><a href="#step-5">C# Static Readonly field</a></li><li><a href="#step-6">C# Readonly vs Static Readonly</a></li><li><a href="#step-7">When to use Const and When to use readonly in C#</a></li></ul>

## <span style="text-decoration: underline;">Const vs Readonly in C#:</span>

<div class='table-responsive'><table class='table'><thead><tr class="row-1 odd"><th class="column-1">Const</th><th class="column-2">Readonly</th></tr></thead><tbody class="row-hover"><tr class="row-2 even"><td class="column-1">const keyword can be applied to fields or local variables</td><td class="column-2">readonly keyword applies only to fields not local variables</td></tr><tr class="row-3 odd"><td class="column-1">We must assign const field at the time of declation only</td><td class="column-2">We can assign readonly field at the time of declaration or  in constructor,not in any other methods.</td></tr><tr class="row-4 even"><td class="column-1">No Memory Allocated Because const value embedded in IL code itself after compilation</td><td class="column-2">dynamic memory allocated for readonly fields and we can get the value at run time.</td></tr><tr class="row-5 odd"><td class="column-1">Const in C# are by default static.Can be accessed only through class name</td><td class="column-2">Readonly belongs to the object created so accessed through only through instance of class. To make it class member we need to add static keyword before readonly.</td></tr><tr class="row-6 even"><td class="column-1">We can declare following built in (primitive types) datatypes as const Boolean,Char, Byte, SByte, Int16, UInt16, Int32, UInt32, Int64, UInt64, Single, Double, Decimal and also string.</td><td class="column-2">Same as Const</td></tr><tr class="row-7 odd"><td class="column-1">The value is constant (as it is belongs to class)</td><td class="column-2">The value may be different depending upon constructor used (as it belongs to object of the class)</td></tr><tr class="row-8 even"><td class="column-1">If we want to declare const for someclass (non-primitive types) we should assign it to null which as of no use.</td><td class="column-2">If you declare a non-primitive types (reference type) as readonly  only reference is immutable not the object it contains.(see the example below)</td></tr><tr class="row-9 odd"><td class="column-1">Do not use const field that might change over the time it leads to dll version problem <br>
(see the example)</td><td class="column-2">As the value obtained at run time there is no dll versioning problem with static readonly fields</td></tr><tr class="row-10 even"><td class="column-1">Const field can not be passed as ref or out parameter</td><td class="column-2">We can pass readonly field as ref or out parameters in the constructor context.</td></tr></tbody></table></div>

&nbsp;

{{< figure src="ReadOnlyConstantincsharp-min.png" title="ReadOnly and Constant in C#" alt="ReadOnly and Constant in C#" >}}

&nbsp;

## <span style="text-decoration: underline;">C# Const field or local:</span>

We will use keyword “<em>const”</em>&nbsp;to declare Constant fields or locals in C#.

Whenever you are defining a const field its value must be assigned&nbsp;at the time of declaration itself, after that we cannot change its value. Go through the following example to understand it



<pre>        
        Public class Program
        {
           const int fieldConstant = 10; //Field

           static void Main(string[] args)
           {
             const int X = 10, Y = 50; //Correct //Local Variable
             const int Z = X + Y;      //Correct
             const int A = X + GettheValue(); // Error
           } 
           public static int GettheValue()
           {
             const int localx=10;
             return 10;
           }
        }</pre>

&nbsp;

The first two lines will works without any errors because X,Y,Z field values are evaluated at the time of compile time itself. But in 3rd line we declared a variable ‘A’ as const and trying to evaluate its value at runtime using GettheValue() method.The line will not execute because const variables must be assigned at the time of compile time itself.



In the above example&nbsp;<em>fieldConstant&nbsp;</em>is a field because its directly declared inside program class.

And we can declare local variables as <em>const</em> as shown in above GetTheValue() method.



The following built in value types&nbsp;can be declared as Const:&nbsp;int, long, char, float, double, decimal, bool, byte, short, string variable as const.

And we can assign non-primitive types to null to define a const.But it’s useless to declare a const reference type which is assigned to null.

<pre>            const string constantString = "Hi Iam Constant"; //Correct
            const Program program = new Program(); //Error
            const Program program1 = null; //Correct</pre>

&nbsp;

You cannot declare a const variable as static because const fields are considered as static members by default.

<pre>            ReadonlyConstant r1=new ReadonlyConstant();// Please see the below code for class declaration

            Console.WriteLine(r1.ynumber);              //Error
            Console.WriteLine(ReadonlyConstant.ynumber);//Correct</pre>

&nbsp;

As the const variable by default static, you cannot access it from the instance of the class. And we cannot pass const values as ref or out params.

## <span style="text-decoration: underline;">C# ReadOnly Field:</span>

We can declare fields as Readonly in C# not local variables.

ReadOnly fields can be initialized at the time of declaration or only within the constructor which is called only once at the time of object creation, not in any other method.

<pre>    public class ReadonlyConstant
    {
        
        public const int numberOfDays = 7; //Field
        public readonly double PI=3.14;             //inline intialization
        
        public readonly int znumber;
        public readonly List&lt;int&gt; readonlyList;

        public ReadonlyConstant()
        {
            znumber= 50;//Constructor initialization            
        }

        public ReadonlyConstant(int x)
        {
             znumber=100;
        }
        
        public NormalMethod()
        {
            //readonly int i=0; This is wrong
        }
    }</pre>



&nbsp;

And the value may be different depending upon the constructor used. i.e., readonly field belongs to object of the class.

Please read the further article about readonly field to understand it further.

<a href="https://www.arungudelli.com/tutorial/c-sharp/the-curious-case-of-readonly-field-in-c/" target="_blank" rel="noopener">The curious case of Readonly field in C#</a>

Now we will go through the differences between const and readonly fields, As mentioned in the second point for const fields no memory allocated and the value directly embedded in IL code. please see the below picture of IL code. (Few differences explained in above post)

{{< figure src="Constant-Readonly-IL-Code.png" title="Constant-Readonly-IL-Code" alt="Constant-Readonly-IL-Code" >}}

I used resharper tool to see Intermediate Language(IL) code of above sample program (ReadonlyConstant.cs)

As you can see the IL code of const field numberOfdays value (7) directly embedded into IL code. Where as the readonly field piValue is displayed as piValue i.e., the value can be obtained at run time.

This leads to versioning problem.

## <span style="text-decoration: underline;">Versioning problem of the Const field in C#:</span>

I compiled above sample program as a class library(A) and used it in another project (in B) as a reference. &nbsp;Now see the generated IL code of project B

{{< figure src="Readonly-Constant-IL-Code.png" title="Readonly and Constant field difference at IL Code" alt="Readonly and Constant field difference at IL Code" >}}

And Even in project B IL code, the value of const field numberofdays embedded in IL code. Now the problem is, in the source (in A ReadonlyConstant.cs library) the const field (numberOfdays )value changed to 5 and compiled and generated a new dll.

But this new value of the const field does not affect in project B until unless we compile the project. After compilation the new const field value will be embedded in IL code of project B.



To overcome this problem we will use static readonly fields.

## <span style="text-decoration: underline;">C# Static Readonly field:</span>

As the readonly field value is different depending upon the constructor used (As explained in the above article). To make it class member (static member) and unique to the class, we will add static keyword before the variable as shown below.

<pre>public class ReadonlyStatic
{
   public static readonly string x = "Hi";
   public static readonly string y;

   public ReadonlyStatic()
   {
     //y = "Hello"; This is wrong
   }

   static ReadonlyStatic()
   {
      y = "Hello";
   }
}</pre>

Now we can use it as constant across the class will overcome the dll version problem with const variables.There may be some performance issues but no need to build the destination project as the value can be obtained at run time.

As shown in the above example we can assign static readonly fields at the time of declaration or in static constructor only.

remaining differences I explained in above readonly article (as the post is becoming large I thought of splitting it two)

## <span style="text-decoration: underline;">C# Readonly vs Static Readonly:</span>

Following are the main differences between readonly and static readonly fields in C#.

<div class='table-responsive'><table class='table'><thead><tr class="row-1 odd"><th class="column-1">Readonly in C#</th><th class="column-2">Static Readonly in C#</th></tr></thead><tbody class="row-hover"><tr class="row-2 even"><td class="column-1">Can be assigned at the time of declaration or constructor</td><td class="column-2">Can be assigned at the time of declaration or static constructor</td></tr><tr class="row-3 odd"><td class="column-1">Value may be different depending upon the constructor used</td><td class="column-2">Value will be constant after the initialization</td></tr></tbody></table></div>

&nbsp;

## <span style="text-decoration: underline;">When to use Const and When to use readonly in C#</span>

Use const when the value is absolute constant that won’t change over the time. For example Number of days in a week is 7. This is always constant. and when in doubt use static readonly to avoid the dll versioning problem.

As the const field value embedded inside IL. Use const modifier for absolute constants to gain performance benefits.

And as explained in the above readonly article if we want to use different constant values for a different instance of the class (or objects) use readonly.

I hope you understand the key differences between const and readonly modifiers in C#.

If so share with your friends and If you have any doubts please feel free to comment below.

Read my articles

<a href="https://www.arungudelli.com/tutorial/c-sharp/delegates-and-events-in-c-sharp/" target="_blank" rel="noopener">Understand delegates and events in c#</a>

<a href="https://www.arungudelli.com/tutorial/c-sharp/difference-between-ref-and-out-parameters-in-c-sharp/" target="_blank" rel="noopener">Difference between Ref and out parameters in C#</a>

Happy Coding….!

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







