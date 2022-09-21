+++
title="Key Differences Between Ref And Out Parameters In C#"
summary="Ref and out in C# allows us to pass the parameters by reference instead of Value.Ref parameters required to assign the value before calling the function where as for Out parameters its not required. tutorial explains difference between ref and out in C# with examples.& also it tells the difference between ref and out parameters in C# (ref vs out) at CLR level."
keywords=["c#,ref parameter in c#,out parameter in c#,ref vs out in c#"
]
type='post'
date='2019-10-26T18:04:05+0000'
lastmod='2019-10-26T18:04:05+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++


Ref and out parameters in C# allows us to pass the parameters by reference instead of Value.

This C# tutorial will explain the main differences between ref and out parameters with examples and also with respect to Common language runtime(CLR).

{{%toc%}}


### <span style="text-decoration: underline;">Ref vs Out in C# difference:</span>

The difference between <em><strong>ref</strong> </em>and <em><strong>out</strong> </em>parameter in C# is&nbsp;<em><strong>Out</strong> </em>parameters is not required to assign the value before calling the function where as <em><strong>ref</strong> </em>parameter should assign the value like normal parameters.

{{< figure src="Ref-and-out.png" title="Difference between Ref and out in C#" alt="Difference between Ref and out in C#" >}}

The simple way of declaring methods with <em><strong>ref</strong> </em>and <em><strong>out</strong></em> parameters are as follows

<pre>//Methods
public static void MethodRef(ref int a){
}
public static void MethodOut(out int a){
}

//Calling
MethodRef(ref b);
MethodOut(out b).</pre>

### 

### <span style="text-decoration: underline;">Ref Parameter in C# with Example:</span>

We will understand “<em><strong>ref</strong></em>” parameter further with a simple c# program. Have a look at the following C# sample.

<pre>private static void Main(string[] args)
        {
            int aref;
            int bref;
            //This is Wrong
            Method(aref);
            MethodRef(ref aref);
            
            //This is correct
            MethodOut(out bref);
        }

        public static void Method(int a)
        {
        }

        public static void MethodRef(ref int a)
        {
            Console.WriteLine(a);
        }
        public static void MethodOut(out int a)
        {
            a = 1;
            Console.WriteLine(a);
        }</pre>

The code will throw following error

<ul><li>Use of unassigned local variable ‘aref’</li></ul>

That means you must assign the value before calling the function.(Same for normal variables but the difference is ref parameter called by reference and normal parameters called by Value).

So When to use “<em><strong>ref</strong></em>” parameters If you want to do manipulations on parameters (For example swapping two variables) we can use the ref parameters. Please see the below example

<pre>//You must assign a and b before calling the method
public static void swap(ref int a,ref int b)
        {
            int c;
            c = a;
            a = b;
            b = c;
        }</pre>

### <span style="text-decoration: underline;">Out Parameter in C# with example:</span>

Have a look at below C# example with ref and out parameters.

<pre>internal class Program
    {
        private static void Main(string[] args)
        {
            int aref = 1;
            int bref = 2;
            MethodRef(ref aref);
            MethodOut(out bref);
        }

        public static void MethodRef(ref int a)
        {
            Console.WriteLine(a);
        }
        public static void MethodOut(out int a)
        {
            Console.WriteLine("Called");
        }
    }</pre>

&nbsp;

### 

If you compile the above program you will get following error

<em>The <strong>out</strong> parameter ‘a’ must be assigned to before control leaves the current method</em>

i.e., you must initialise the <em><strong>out</strong> </em>parameter in CalledMethod (MethodOut).

It’s not necessary to initialise the <em><strong>out</strong> </em>parameter before calling the method. Even though you initialise the variable, called method cannot read it.

Have a look at the below C# program I am assigning the value as 2 to bref variable before passing it as out parameter and using it in Called method. If you compile the program we will get following error

<em>Use of Unassigned out parameter ‘a’.</em>

That means it does not matter whether you assign the out parameter before calling method. The called method (MethodOut) cannot access the value. i.e., we must assign the out parameter before using it.

As in below example we can use the out parameter after assigning it to some value.

<pre> private static void Main(string[] args)
        {
            
            int bref = 2;
            MethodOut(out bref);
        }

void MethodOut(out int a)
        {
            //This is wrong
            Console.WriteLine(a);
            a = 1;

             //This is correct
            //Console.WriteLine(a);
            
        }</pre>

&nbsp;

Called method should assign the “<em><strong>out</strong></em>” parameter before returning to calling method.

### <span style="text-decoration: underline;">Why Out parameter in C#?</span>

&nbsp;

We can have only one return type to a particular Method. So “<em><strong>out</strong></em>” parameter is useful when you want a method to return multiple values.

<pre>public static bool UpdateDb(int a,out string reason)
        {
            bool success = true;
            try
            {
                reason = string.Empty;
                //Callling Database
                //update Db Success
            }
            catch (Exception ex)
            {
                //If Fails
                success = false;
                reason = ex.Message;
            }
            
            return success;
        }</pre>

&nbsp;

In the above example we are updating “a” to Database the method will return true or false. If its failed we want the reason why it got failed. In that case we can “out” parameter as reason and assign corresponding error to that “out” parameter.

You must assign out parameter that’ y I assigned to Empty in the success case (I have used this example for understanding the out parameter)

### 

### <span style="text-decoration: underline;">Difference&nbsp;between ref and out Parameters in C# at CLR level:</span>

&nbsp;

Both allows us to pass parameters by reference instead of by Value

For CLR(Common Language Run time) both <em><strong>ref</strong> </em>and <em><strong>out</strong></em>&nbsp;parameters are identical that means same Intermediate code will generate for both keywords. and the metadata also same except for one bit which specifies whether you specified <em><strong>out</strong> </em>or <em><strong>ref</strong> </em>when declaring the method.

The difference is that the C# Compiler ensures that we write the correct code.(That’s why compile time error will come when didn’t initialize the <em><strong>ref</strong> </em>parameter).

{{< figure src="CLR-ref-and-out-c.png" title="Difference between ref and out at CLR level" alt="Difference between ref and out at CLR level" >}}

A <em><strong>ref</strong> </em>or <em><strong>Out</strong> </em>parameter cannot have default values as normal parameters. The following code snippet will not compile, Because I have passed default parameters to ref and out parameters.

<pre>public static void Method(int a = 1)
        {
        }

        public static void MethodRef(ref int a=1)
        {
            Console.WriteLine(a);
        }
        public static void MethodOut(out int a=1)
        {
            a = 1;
            Console.WriteLine(a);
        }</pre>

&nbsp;

### 

### <span style="text-decoration: underline;">Overloading of Methods with ref and out Parameters in C#:</span>

&nbsp;

This is an interesting question just execute the following code snippet

<pre>public static void Add(out int a)
        {
            a = 1;
        }
        public static void Add(ref int a)
        {
           Console.WriteLine(a);
        }</pre>

&nbsp;

This will throw the following error

<em>Cannot define overloaded method ‘Add’ because it differs from another method only on ref and out</em>

As I mentioned before CLR (Common Language Runtime) treat both ref and out keywords as same and their Metadata representation of the method signature will be identical. It’s not correct to declare a method with same signatures and parameters.

It’s again C# Compiler responsibility to ensure we write the correct code(third point in similarities) So that’s why it’s returned an error.

But overloading can be possible if one method takes a simple parameter and other method takes either ref or out parameter. The following case is perfectly valid

<pre>public static void Add(out int a)
        {
            a = 1;
        }
        public static void Add(int a)
        {
           Console.WriteLine(a);
        }</pre>

&nbsp;

&nbsp;

I hope you’ve enjoyed this article and that it gives you more ideas on&nbsp;<em><strong>ref</strong></em><strong>&nbsp;</strong> and <em><strong>out</strong></em><strong>&nbsp;</strong>parameters in C#&nbsp;and similarities and differences between them. If so share this post with your friends and also join our mailing list

&nbsp;









