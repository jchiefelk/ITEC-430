 <h1>Python-MySQL</h1>
 

<h3>Goals</h3>

<p>
	This is not a database class, our primary focus is accessing the mysqldump tool from the terminal, or Python scripts.  However, below is a list of topics that are absolutely necessary for a foundational grasp of MySQL.  The goals for this class is to equip you with experience preparing a disaster recovery strategy and the technical skills automate DATABASE BACKUP.  Since MySQL accounts for roughly 45% of enterprize databases, plus its an old reliable standard, its a good starting database technology to learn.
</p>

<p>
	In the era of Big Data it is absolutely essential for Systems Administrators to be familiar with foundational SQL knowledge for their interview processes.  In an on-site interview you could be expected to do simple one line SQL commands on a whiteboard. This means being able to Create, Read, Update, and Delete (aka CRUD).  In addition, questions on any of the foundational knowledge below is also fair game for an interview.
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

<p>
	We'll be using MySQL in Windows Server 2016, see pros and cons, <a href="https://medium.com/@mindfiresolutions.usa/a-comparison-between-mysql-vs-ms-sql-server-58b537e474be">here.</a> . MySQL is used by ~50% of enterprises.  Its free to use, can be used on many different platforms, multiple different DB engine selections, but costs for support. Microsoft SQL Server costs money, but has recently released a Linux port in 2017, read <a href="https://www.wired.com/2017/01/microsofts-old-school-database-surprise-software-hit-year/">here.</a> . It is the go-to standard for .NET specific applications.
</p>

<h3>Getting Started on Windows</h3>

<p>
 To install MySQL on Windows you first need to install the MySQL Installer, located here <a href="https://www.mysql.com/">here</a>. Then install MySQL and required libraries. Then install install flask, and flask-mysql
</p>

<pre>
>pip install flask flask-mysql
</pre>


<h3>1) Entities and Attributes</h3>

<p>
 A user (entity) has a username (attribute). A table row represents an entity.
</p>

<h3>2) Create a Database</h3>

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

<h3>Creating a Disaster Recovery Strategy</h3>
 
 <p>1) Do NOT store backups in the same physical location as database files.</p>
 <p>2) Make sure you have a proper backup schedule established. This will be unique per organization based on the needs of the company.</p>
 <p>3) Make sure to actually restore backups on a testserver, and verify that you can restore with all the options and conditions you need to use during a planned or un-planned downtime.</p>
 
<p>
This strategy is ideal for automation. And since the strategy needs to be repeated on schedule, we will use Python to build a scheduler that repeats cloning a mysql database using the terminal tool "mysqldump".  To this we will need to invoke an operationg system subprocess call using the "os" module. Next in our script, we will transfer the cloned schema ( *.sql file), . Next, you'll transfer the *.sql file to an external server via SSH, then we will restore the backup sql schema into remote db, perform a simple query to verify that the clone was performed sucessfully
</p>



<h3>1) Create a clone using mysqldump</h3>

<p>
	First, import os and create subprocess that calls on the command line tool, "mysqldump". mysqldump is a tool installed natively with MySQL distributions. It cannot be used from mysql shell, but directly from Bash or Windows terminal.  
</p>

<pre>
import os
import sys
password=sys.argv[1]
os.popen("mysqldump -u root --password="+password+" --databases employees > dump.sql")
</pre>

<p>
The reason that we are importing the "sys" module is so that we can accept a user's root password as a command line argument, and then assign it to a variable called password, which is the concatenated into mysqldump command called by the subprocess.
</p>



 
