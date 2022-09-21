+++
title="List All Tables In Oracle Database Query"
summary="3 ways to show or list all tables in Oracle database. Based on privileges we can query oracle's all_tables,user_tables,all_all_tables,dba_tables to list all tables. all_tables lists all tables that have user access,user_tables lists all tables owned by the user,dba_tables displays all tables in the database."
keywords=["oracle,list all tables,query to show all tables"
]
type='post'
date='2019-11-01T18:03:40+0000'
lastmod='2019-11-01T18:03:40+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
focal_point=''
preview_only=false
+++

We can get a list of all tables in Oracle database in three ways depending upon the user privileges.

{{%toc%}}

&nbsp;

We can show or list all tables in Oracle by querying Oracle Data Dictionaries. A data dictionary in Oracle is a group of read-only tables that provide useful information to users about the database like schemas, users, privileges etc.

### List all Tables in Oracle database, owned by current Oracle user:

&nbsp;

The below query returns a list of all tables owned by the current user.

<pre>SELECT table_name FROM user_tables;
</pre>

### List all Tables in Oracle database, accessed by Current user:

&nbsp;

The below query lists all tables in oracle which are accessible by the current user.

<pre>SELECT owner, table_name FROM all_tables;</pre>

The owner column displays the owner’s name of the table. user_tables table does not have the owner column.

### List all Tables in Oracle database(entire database):

&nbsp;

To get a list of all tables in oracle database(entire database) use the below query.

<pre>SELECT owner, table_name FROM dba_tables;</pre>

However, you might get “ORA-00942: table or view does not exist” error if you do not have access to dba_tables. You should ask your database administrator to explicitly grants you privileges on that table, or SELECT ANY DICTIONARY privilege or the SELECT_CATALOG_ROLE role (both of them of which allows you to query any data dictionary table).

dba_tables contain information of all the tables in the current database. Whereas all_tables can be considered as a subset of dba_tables that has access to the current user. user_tables contains information about tables owned by the current user.

{{< figure src="ListAllTablesInOracle.png" title="List All Tables In Oracle" alt="List All Tables In Oracle" >}}

&nbsp;

### ALL_ALL_TABLES in Oracle:

Both all_tables and all_all_tables views provide details of the tables to which the current user has access.

But in addition, the ALL_ALL_TABLES will also return all object tables (system generated or not) accessible by the current user.

<pre>select *
from dictionary
where table_name in ('TABS','ALL_TABLES','ALL_ALL_TABLES')

TABLE_NAME           COMMENTS
-------------------- ------------------------------------------------------------------------------------------------
ALL_ALL_TABLES       Description of all object and relational tables accessible to the user
ALL_TABLES           Description of relational tables accessible to the user
TABS                 Synonym for USER_TABLES</pre>

ALL_ALL_TABLES view includes object tables as well as relational tables.

There is a difference between number of columns returned by ALL_ALL_TABLES and ALL_TABLES in Oracle.

ALL_ALL_TABLES have 3 additional columns which gives us the details about the object type on which the object table was created and the object identifier type used as shown below

<ol><li>OBJECT_ID_TYPE</li><li>TABLE_TYPE_OWNER</li><li>TABLE_TYPE</li></ol>

If you want to see the difference only between the two views, you can use a select query

<pre>SELECT * FROM ALL_ALL_TABLES 
WHERE TABLE_TYPE IS NOT NULL

</pre>

If we don’t have object tables in our schemas, still we will see some of the object tables used by different Oracle features installed.









