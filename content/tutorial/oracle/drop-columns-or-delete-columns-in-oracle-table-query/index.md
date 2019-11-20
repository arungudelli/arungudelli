+++
title="Drop Columns Or Delete Columns In Oracle Table Query"
summary="To delete columns in Oracle use ALTER TABLE...DROP COLUMN statement query. Dropping columns in oracle can be done in 2 ways Logical Delete, Physical Delete."
keywords="drop column in oracle table,delete column in oracle table,drop column query in oracle,oracle"
type='post'
date='2019-11-10T18:03:05+0000'
lastmod='2019-11-10T18:03:05+0000'
draft='false'
authors=['admin']
[image]
caption='Drop Columns Or Delete Columns In Oracle Table Query'
focal_point=''
preview_only=false
+++








To Delete columns in Oracle, we have to use ALTER TABLE…DROP COLUMN statement query.

Dropping columns in oracle can be done in 2 ways.

<ol><li>Delete Columns Logically or make them unused columns</li><li>Delete columns with data or physically deleting the columns</li></ol>

<ul><li><a href="#step-1">Delete columns in oracle table logically</a><ul><li><a href="#step-2">Delete a single column in oracle table Logically</a></li><li><a href="#step-3">Delete multiple columns in oracle table Logically</a></li><li><a href="#step-4">Deleting unused columns in oracle table</a></li><li><a href="#step-5">View all unused columns in Oracle Database query</a></li></ul></li><li><a href="#step-6">Delete column with data in oracle or Physically Deleting</a><ul><li><a href="#step-7">Delete a single column in oracle table query</a></li><li><a href="#step-8">Delete multiple columns in oracle table query</a></li><li><a href="#step-9">Deleting columns from oracle compressed tables</a></li></ul></li></ul>

{{< figure src="Drop-Columns-in-Oracle-Table-query.png" title="Drop Columns in Oracle Table query" alt="Drop Columns in Oracle Table query" >}}

## Delete columns in oracle table logically:

Logically deleting columns in oracle is nothing but setting unused columns.

Once you mark the column as unused you can longer see that column in oracle table.

Dropping a column from a huge table is time consuming &amp; uses too many resources.So it’s better to mark column as unused and can be deleted after some time.

<ul><li>Once the column marked as unused it will be no longer visible in oracle select queries and data dictionary views.</li><li>All indexes, statistics, constraints created on that columns are also removed.</li><li>But it does not actually remove the target column data or restore the disk space occupied by these columns.</li><li>We can also reuse the column name to create new columns.</li></ul>

## Delete a single column in oracle table Logically:

To delete a single column in oracle table logically use below query

<pre>ALTER TABLE oracle_table_name SET UNUSED (column_to_be_deleted);</pre>

We have to pass column name to the unused statement.

For example if you want to mark department_id from employee table as unused use the below query

<pre>ALTER TABLE employee SET UNUSED (department_id);</pre>

## Delete multiple columns in oracle table Logically:

To delete multiple columns in oracle table logically use the following UNUSED statement query

<pre>ALTER TABLE oracle_table_name SET UNUSED (column_to_be_deleted1,column_to_be_deleted1);</pre>

We have to pass multiple column names to unused statements as shown above.

For example, the below oracle query marks department_id and is_manager columns in the employee table as unused.

<pre>ALTER TABLE employee SET UNUSED (department_id,is_manager);</pre>

## Deleting unused columns in oracle table:

To permanently delete the unused columns in oracle use the below DROP UNUSED query statement

<pre>ALTER TABLE oracle_table_name DROP UNUSED COLUMNS;</pre>

For example, the below oracle query permanently deletes department_id,is_manager columns from the employee table, which are marked as unused

<pre>ALTER TABLE employee DROP UNUSED COLUMNS;</pre>

We can specify the <em>checkpoint</em> clause to avoid the amount of undo logs created during the drop column query to avoid potential exhaustion of undo space.

The below query creates a checkpoint for every 300 records processed.

<pre>ALTER TABLE employee  DROP UNUSED COLUMNS CHECKPOINT 300;

</pre>

## View all unused columns in Oracle Database query:

To view all unused columns in oracle database we use the following data dictionary views

<ol><li>USER_UNUSED_COL_TABS</li><li>ALL_UNUSED_COL_TABS</li><li>DBA_UNUSED_COL_TABS</li></ol>

<pre>SELECT * FROM DBA_UNUSED_COL_TABS;

OWNER&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;TABLE_NAME&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; COUNT
---------------------&nbsp; &nbsp;---------------&nbsp; &nbsp;    -----
DBA&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;EMPLOYEE&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2</pre>

The count column displays the number of unused columns in a given table.

## Delete column with data in oracle or Physically Deleting:

We can use ALTER TABLE…DROP COLUMN statement to delete the column with data from oracle table.

## Delete a single column in oracle table query:

To delete a single column in oracle table use the following query

The DROP COLUMN statements delete columns including their data.

<pre>ALTER TABLE oracle_table_name DROP COLUMN column_to_be_deleted;</pre>

The following query deletes the department_id column from the employee table

<pre>ALTER TABLE employee DROP COLUMN department_id;</pre>

## Delete multiple columns in oracle table query:

To drop multiple columns in oracle table use the below query statement.

<pre>ALTER TABLE oracle_table_name DROP COLUMN (column_to_be_deleted1,column_to_be_deleted2);</pre>

The following query deletes the department_id,is_manager columns from the employee table.

<pre>ALTER TABLE employee DROP COLUMN (department_id,is_manager);</pre>

## Deleting columns from oracle compressed tables:

If we enable compression for all operations in the oracle table, you can drop table columns as shown above.

But If you enable compression only for direct-path inserts, you cannot drop columns from the table.

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank">Facebook</a> or <a href="https://plus.google.com/+ArunkumarGudelli" target="_blank">googlePlus</a> or <a href="https://www.linkedin.com/in/arungudelli/" target="_blank">linkedn</a> to get in touch with me.







