+++
title="Oracle Rename Column Using ALTER Query & Rename Table Example"
summary="In Oracle, to rename a column in a table, use ALTER TABLE RENAME COLUMN statement"
keywords="rename column name in oralce,rename table in oracle,oracle"
type='post'
date='2019-11-16T20:50:55+0000'
lastmod='2019-11-16T20:50:55+0000'
draft='false'
authors=['admin']
[image]
caption='Oracle Rename Column Using ALTER Query & Rename Table Example'
focal_point=''
preview_only=false
+++








In Oracle, to rename a column in a table, use <strong>ALTER TABLE RENAME COLUMN</strong> statement.

<ol><li><a href="#step-1">Oracle Rename Column table syntax</a></li><li><a href="#step-2">Oracle Rename Column in a table query example</a></li><li><a href="#step-3">Oracle Rename table syntax</a></li><li><a href="#step-4">Oracle Rename table query example</a></li></ol>

{{< figure src="Alter-table-rename-column-in-oracle-table-query.jpg" title="Alter table rename column in oracle table query" alt="Alter table rename column in oracle table query" >}}

## Oracle Rename Column table syntax:

<ol><li>To rename a column in oracle we have to use <strong>rename column</strong> statement</li><li>You have to use <strong>rename column</strong>&nbsp;statement along with <strong>alter table</strong> statement</li><li>The RENAME COLUMN statement allows us to rename an existing column in an existing table in any schema (except the schema SYS).</li></ol>

<pre>ALTER TABLE
&nbsp; &nbsp;table_name
RENAME COLUMN
old_column_name 
TO
new_column_name;</pre>

For example, we have an employee table which contains columns as id,name,email,date_hired and job columns

We will rename the email column to email_id

<pre>create table employees ( 
   id number not null, 
   name varchar2(50) not null, 
   email varchar2(255), 
   date_hired date, 
   job varchar2(255) 
)</pre>

## Oracle Rename Column in a table query example

To rename a column in oracle table use the below query

<pre>ALTER TABLE
&nbsp; &nbsp;employees
RENAME COLUMN
email&nbsp;
TO
email_id;</pre>

## Oracle Rename table name syntax:

To rename a table name in oracle use following query syntax

<pre>RENAME TABLE_NAME to NEW_TABLE_NAME:</pre>

## Oracle Rename table query example:

The below query renames the table name employees to new table name

<pre>RENAME employees to emp;</pre>

To rename a column name or table name, you must be the database owner or the table owner.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







