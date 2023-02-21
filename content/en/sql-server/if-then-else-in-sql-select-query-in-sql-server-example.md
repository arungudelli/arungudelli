---
title: "2 Ways To Write IF THEN ELSE In SQL SELECT Query In SQL Server"
description: "In SQL server, To write if then else in SQL select query we can use SELECT CASE statement (In all versions), SELECT IIF logical function (From SQL server 2012)"
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

In SQL server, To write if then else in SQL select query we can use

1. `SELECT CASE` statement (In all versions of SQL server)
2. `SELECT IIF` logical function (From SQL server 2012 )

We will take an example Employee table which has columns EmpId, EmpName, Experience, Salary, Gender. 

Now we want to divide employees based upon their experience and salary.

If employee experience is more than 5 years consider them as "Senior Dev" Or "Junior Dev". (if experience > 5)

And additionally, we can consider employees having a salary greater than 1000USD as also "Senior Dev" (if experience > 5 OR Salary > 10000)

Now we will use `case` statement and `IIF` function to select such employees.

## Method:1 Using `Select Case` to write if else then in select query example

To add an additional column position based upon the employee’s experience (column greater than 5)

That means IF experience > 5 THEN "Senior Dev" ELSE "Junior Dev".

```sql
SELECT CASE
       WHEN experience > 5  THEN "Senior Dev" ELSE "Junior Dev"
       END as Position, *
FROM Employee;
```
And additionally, we can add one more criteria "If salary greater than 1000USD" as shown below

```sql
 SELECT CASE      
        WHEN experience > 5  
            THEN "Senior Dev"
        WHEN salary > 1000
            THEN "Senior Dev" 
        ELSE "Junior Dev"        
   END as Position, * 
FROM Employee;
```

The above SQL query executes the below pseudo code

```text
IF
 experience > 5 OR salary > 1000
THEN
 RETURN 'Senior Dev'
ELSE
 RETURN 'Junior Dev'
END
```

A case statement should have an END statement in SQL server.

![If then else sql server](/images/sql-server/If-then-else-sql-server.png "If then else sql server")


## Method 2: Using `IIF` Logical function to write if else then in select query example

`IIF` function is syntactic sugar for writing a CASE expression which introduced in SQL server 2012.

We can replace above `IF THEN ELSE` case statement to


```sql
SELECT
IIF(experience > 5 OR salary > 1000,'Senior Dev','Junior Dev')
AS Position, * FROM Employee
```

So If you are using SQL server 2012 above it's best to use `IIF` function to write if else then in SQL select query.








