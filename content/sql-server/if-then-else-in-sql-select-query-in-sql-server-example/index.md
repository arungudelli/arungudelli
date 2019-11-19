+++
title="2 Ways To Write IF THEN ELSE In SQL SELECT Query In SQL Server"
summary="In SQL server, To write if then else in SQL select query we can use SELECT CASE statement (In all versions), SELECT IIF logical function (From SQL server 2012)"
keywords="sql server,if then else in sql select,sql-server"
type='post'
date='2019-11-16T20:50:24+0000'
lastmod='2019-11-16T20:50:24+0000'
draft='false'
authors=['admin']
[image]
caption='2 Ways To Write IF THEN ELSE In SQL SELECT Query In SQL Server'
focal_point=''
preview_only=false
+++








In SQL server, To write if then else in SQL select query we can use

<ol><li>SELECT CASE statement (In all versions of SQL server)</li><li>SELECT IIF logical function (From SQL server 2012 )</li></ol>

We will take an example Employee table which has columns EmpId, EmpName, Experience, Salary, Gender. Now we want to divide employees based upon their experience and salary.

If employee experience is more than 5 years consider them as “Senior Dev” Or “Junior Dev”. (if experience &gt; 5)

And additionally, we can consider employees having a salary greater than 1000USD as also “Senior Dev” (if experience &gt; 5 OR Salary &gt; 10000)

Now we will use case statement and IIF function to select such employees.

<a href="#step-1">Method:1 Using Select Case to write if else then in select query example</a>

<a href="#step-2">Method:2 Logical function to write if else then in select query example</a>

## Method:1 Using Select Case to write if else then in select query example:

To add an additional column position based upon the employee’s experience (column greater than 5)

That means IF experience &gt; 5 THEN “Senior Dev” ELSE “Junior Dev”.

<pre>SELECT CASE
  &nbsp; &nbsp; &nbsp;WHEN experience &gt; 5&nbsp; THEN "Senior Dev" ELSE "Junior Dev"
&nbsp; &nbsp; &nbsp; &nbsp;END as Position, *
FROM Employee;</pre>

And additionally, we can add one more criteria “If salary greater than 1000USD” as shown below

<pre> SELECT CASE &nbsp; &nbsp; &nbsp;
        WHEN experience &gt; 5&nbsp; 
            THEN "Senior Dev"
        WHEN salary &gt; 1000
            THEN "Senior Dev" 
        ELSE "Junior Dev" &nbsp; &nbsp; &nbsp; &nbsp;
   END as Position, * 
FROM Employee;</pre>

The above SQL query executes the below pseudo code

<pre>IF
 experience &gt; 5 OR salary &gt; 1000
THEN
 RETURN 'Senior Dev'
ELSE
 RETURN 'Junior Dev'
END</pre>

A case statement should have an END statement in SQL server.

{{< figure src="If-then-else-sql-server.png" title="If then else sql server" alt="If then else sql server" >}}

## Method 2: Using IIF Logical function to write if else then in select query example:

IIF is syntactic sugar for writing a CASE expression which introduced in SQL server 2012.

We can replace above IF THEN ELSE case statement to

<pre>SELECT
IIF(experience &gt; 5 OR salary &gt; 1000,'Senior Dev','Junior Dev')
AS Position, * FROM Employee</pre>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







