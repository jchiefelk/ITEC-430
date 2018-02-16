<h1>Disaster Recovery Strategy - Database Backup</h1>
 
<p>
	This is a multi-part lesson.  It is absolutely essentially that as a Systems Administrator, Linux or Windows Server that you implement measures to ensure data recovery in the instance of server crash. These can happen for a number of reasons; fire, electricity outage, software error, hard drive failure,...lots.
</p>	
 
<p>
	The objective of this series is to give you experience implementing a security protocol to backup a MySQL database.  MySQL is used by ~45% of enterprises running Windows Server 2016. Read more about MySQL in Windows Server enterprises here on <a href="https://medium.com/@mindfiresolutions.usa/a-comparison-between-mysql-vs-ms-sql-server-58b537e474be">Medium</a>
</p>

<p>
	You will engineer a Python program that will automate MySQL databse backup and testing.  To automate the process of database of backup and testing, one could spend some money on some third-party software with a GUI that may or may not provide all of the robustness you need.  Using Python will not only provide robustness for this task, it also can save you money.  
</p>

<p>
	In order to successfully implement a backup and test strategy in Python, you must have a foundational grasp of the following first.
</p>

<p><a href="https://github.com/jchiefelk/ITEC-430/tree/master/mysql">1) MySQL</a></p>
<p><a href="https://github.com/jchiefelk/ITEC-430/tree/master/sshserver">2) Using SSH in Windows Server</a></p>
<p><a href="https://github.com/jchiefelk/ITEC-430/tree/master/sshserver">3) Deploying a SSH server on Ubuntu</a> </p>
<p><a href="">4) Public/Private Key Cryptography</a> </p>


<p>
  We will cover these topics in several seperate lessons.  
</p>
 
 
<h3> Using SQL as a Windows Systems Administrator</h3>

<p>
 To install MySQL on Windows Server 2016 you first need to install the MySQL Installer, located <a href="https://www.mysql.com/">here</a>. Then install MySQL and required libraries.
</p>

<h3>Creating a Disaster Recovery Strategy</h3>
 
 <p>These are the requirements of a sound disaster recover strategy.  Your server could crash for a number of different reasons. To protect against potential damages to business this may cause, it is absolutely necessary to back your data. You want to backup your data in a way that ensures that the backup is saved in the event of hard disc failure.  It is also vital that you test your backup to ensure that it is possible to restart a company's server-side engines without damage to business.</p>
 
 <p>1) Do NOT store backups in the same physical location as database files.</p>
 <p>2) Make sure you have a proper backup schedule established. This will be unique per organization based on the needs of the company.</p>
 <p>3) Make sure to actually restore backups on a testserver, and verify that you can restore with all the options and conditions you need to use during a planned or un-planned downtime.</p>
 
<p>
This strategy is ideal for automation. And since the strategy needs to be repeated on schedule, we will use Python to build a scheduler that repeats cloning a mysql database using the terminal tool "mysqldump".  To do this we will need to invoke an operationg system subprocess using the "os" module. Next in our script, we will transfer the cloned schema ( *.sql file). Next, you'll transfer the *.sql file to an external server via SSH, then we will restore the backup sql schema into remote db, perform a simple query to verify that the clone was performed sucessfully
</p>



<h5>1) Create a clone using mysqldump</h5>

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
The reason that we are importing the "sys" module is so we can accept a user's root password as a command line argument, and then assign it to a variable called password, which is then concatenated into mysqldump command called by the subprocess.  The next step involves using SSH to transfer .sql files to a mock remote server.  A sound disaster recover strategy involves transfer clone SQL schema to a server in a different geographical location then host server.  Before we add a couple more lines in python to accomplish this task, lets first set tup a remote SSH server on a virtual machine.
</p>


