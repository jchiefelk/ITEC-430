 <h1>MySQL</h1>
 

<h3>Goals</h3>

<p>
	This is not a database class, our primary focus is accessing the mysqldump tool from the terminal, or Python scripts.  However, below is a list of topics that are absolutely necessary for a foundational grasp of MySQL.  The goals for this class is to equip you with experience deploying a disaster recovery strategy, by engineering an automated DATABASE BACKUP routine using Python and SSH.  Since MySQL accounts for roughly 45% of enterprise databases, plus it is an old standard of which many DB technologies are modeled after, makes it a good starting database technology to learn.
</p>

<p>In the era of Big Data it is absolutely essential for Systems Administrators to be familiar with foundational SQL knowledge.  In an on-site interview you could be expected to do simple one line SQL commands on a whiteboard. This means being able to Create, Read, Update, and Delete (aka CRUD).  For basic Database design it is also essential to know the foundational knowledge below.
</p>

<h3>Foundational Knowledge</h3>

<p>1) Understand the concept of Entities and Attributes - Basic Design Methods/Starting Data</p>
<p>2) Create a Database</p>
<p>3) Create a Table</p>
<p>4) Adding Data to a Database</p>
<p>5) Read from a database</p>
<p>6) What is Normalization?</p>
<p>7) What is Atomicity?</p>
<p>8) Relationships; a)One-To-One, b) One-to-Many, c) Many-to-Many</p>


<h3>Using SQL as a Systems Administrator</h3>

<p>We'll be using MySQL in Windows Server 2016, see pros and cons, <a href="https://medium.com/@mindfiresolutions.usa/a-comparison-between-mysql-vs-ms-sql-server-58b537e474be">here.</a>  MySQL is used by ~50% of enterprises.  Its free to use, can be used on many different platforms, multiple different DB engine selections, but costs for support. Microsoft SQL Server costs money, but has recently released a Linux port in 2017, read <a href="https://www.wired.com/2017/01/microsofts-old-school-database-surprise-software-hit-year/">here.</a>  It is the go-to standard for .NET specific applications.
</p>


<h3>1) Entities and Attributes</h3>

<p>A user (entity) has a username (attribute). A table row represents an entity.</p>

<h3>2) Create a Database</h3>

<p>After logging on to your database using the mysql terminal, see which databases are present by running</p>

<pre>
mysql>show tables;
</pre>

<p>To create a new database, run</p>

<pre>
mysql>create database employees;
</pre>

<p>
To choose that table
</p>

<pre>
mysql>use employees;
</pre>

<h3>3) Create a Table</h3>

<p>
To create a new table,
</p>

<pre>
mysql>create table instructors (firstname VARCHAR(20),lastname VARCHAR(20));
</pre>

<h3>4) Add data to a database</h3>

<p>
Add data to the instructor data by performing.
</p>

<pre>
mysql> insert into instructors (firstname, lastname)
	-> (firstname,lastname)
	-> values
	-> ("Jackson", "Chief Elk");
</pre>

<h3>5) Read from a database</h3>

<p>Show table structure</p> 

<pre>
mysql> describe instructors;
</pre>


<p>Get data from a table</p>

<pre>
mysql> select * from instructors;
</pre>

<h3>6) What is normalization?</h3>

<p>
	Normalization are a set of different procedures used to reduce
	data redunancy in large databases composed of many relationships.  It is used to ensure data 
	is atomic.
</p>


<h3>7) What is atomicity?</h3>

<p>
	Atomic data, atomicity, is having data stored in its most indivisible and irreducible piece.  An example of some data that is NOT atomic is a full name like "Satoshi Nakamoto".  This piece of data is made up of both a first name and a last name. In MySQL, the atomic way would be store the first and last name individually in their own column.  First and last names cannot be reduced further, therefore our data store in those columns is atomic.
</p>

<h3>Relationships</h3>

<p>
a) One-To-One: When a column is refrenced by another column, it references that column with a private key
</p>

<p>
b) One-To-Many: When many different refrence the same column from a table. An example would be a bidding website like Ebay. Only one user can post a listing, but mul 	
</p>

<p>
c) Many-To-Many: When a table contains a column that is related to another column that is itself, a refrence to another column
</p>


<h3>Interview Questions</h3>

<p>
An extensive list of interview questions for MySQL and Windows can be found on <a href="https://github.com/cshenoy/awesome-interviews">Github here</a>	
</p>
