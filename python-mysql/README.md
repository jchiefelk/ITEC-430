 <h1>Python-MySQL</h1>
 

<h3>Goals</h3>

<p>
	This is not a database class, our primary focus is accessing the mysqldump tool from the terminal, or Python scripts.  However, below is a list of topics that are absolutely necessary for a foundational grasp of MySQL. 
</p>

<p>
	In the era of Big Data it is absolutely essential for Systems Administrators to be familiar with foundational SQL knowledge. This means being able to Create, Read, Update, Delete aka CRUD on a whiteboard.  Also, or start a side project that requires you to settup a Database on a Linux or Windows Operating Systems.
</p>

<h3>Foundational Knowledge</h3>

<p>1) Understand the concept of Entities and Attributes - Basic Design Methods/Starting Data</p>
<p>2) Create a Database</p>
<p>3) Create a Table</p>
<p>4) Create a Column</p>
<p>5) Adding Data to a Database</p>
<p>6) Read from a database</p>
<p>7) What is Normalization used for?</p>
<p>8) What is Atomicity?</p>
<p>9) Relationships; a)One-To-One, b) One-to-Many, c) Many-to-Many</p>


<h3>Using SQL as Systems Administration</h3>

<p>
	We'll be using SQL in Windows Server 2016, see pros and cons <a href="https://medium.com/@mindfiresolutions.usa/a-comparison-between-mysql-vs-ms-sql-server-58b537e474be">here.</a>
	
</p>




<p>
 First install flask, and flask-mysql
</p>

<pre>
>pip install flask flask-mysql
</pre>


<h3>Entities and Attributes</h3>

<p>
 A user (entity) has a username (attribute). A table row represents an entity.
</p>



<h3>Create a Database</h3>

<p>After logging on to your database using the mysql terminal, see which databases are present by running</p>

<pre>
mysql>show tables;
</pre>

<p>
	To create a new database, run
</p>

<pre>
mysql>create database employees;
</pre>

<p>
To choose that table
</p>

<pre>
mysql>use employees;
</pre>

<h3>Create a Table</h3>

<p>
	To create a new table,
</p>

<pre>
mysql>create table instructors (firstname VARCHAR(20),lastname VARCHAR(20));
</pre>

<h3>Add data to a database</h3>

<p>
	Add data to the instructor data by performing.
</p>

<pre>
mysql> insert into instructors (firstname, lastname)
	-> (firstname,lastname)
	-> values
	-> ("Jackson", "Chief Elk");
</pre>

<h3>Show table structure</h3>

<pre>
mysql> describe instructors;
</pre>


<h3>Get data from a table</h3>

<pre>
mysql> select * from instructors;
</pre>



<h3>What is normalization?</h3>

<p>
	Normalization are a set of different procedures used to reduce
	data redunancy in large databases composed of many relationships.  It is used to ensure data 
	is atomic.
</p>


<h3>What is atomicity?</h3>

<p>
	Atomic data, atomicity, is having data stored in its most indivisible and irreducible piece.
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

