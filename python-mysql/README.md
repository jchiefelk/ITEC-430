 <h1>Python-MySQL</h1>

<p>
	First install flask, and flask-mysql
</p>

<pre>
>pip install flask flask-mysql
</pre>

<h3>Goals</h3>

<p>
	This is not a database class, our primary focus is accessing mysql from the terminal or Python scripts.  However, here is a list of topics
	that are absolutely necessary for an intermediate grasp of MySQL 
</p>

<p>1) Understand the concept of Entities and Attributes - Basic Design Methods/Starting Data</p>
<p>2) Create a Database</p>
<p>3) Create a Table</p>
<p>4) Create a Column</p>
<p>5) Adding Data to a Database</p>
<p>6) Read from a database</p>
<p>7) What is Normalization used for?</p>
<p>8) What is Atomicity?</p>
<p>9) Relationships; a)One-To-One, b) One-to-Many, c) Many-to-Many</p>

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
mysql> select * from instructors
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

a) One-To-One: When a column is refrenced by another column, it references that column with a private key


