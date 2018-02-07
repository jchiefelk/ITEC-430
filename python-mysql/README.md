 <h1>Python-MySQL</h1>
 

<h3>Using SQL as a Windows Systems Administrator</h3>

<p>
 To install MySQL on Windows Server 2016 you first need to install the MySQL Installer, located <a href="https://www.mysql.com/">here</a>. Then install MySQL and required libraries. Then install install flask, and flask-mysql
</p>

<pre>
>pip install flask flask-mysql
</pre>

<h3>Exercise: Create a Disaster Recovery Strategy</h3>
 
 <p>1) Do NOT store backups in the same physical location as database files.</p>
 <p>2) Make sure you have a proper backup schedule established. This will be unique per organization based on the needs of the company.</p>
 <p>3) Make sure to actually restore backups on a testserver, and verify that you can restore with all the options and conditions you need to use during a planned or un-planned downtime.</p>
 
<p>
This strategy is ideal for automation. And since the strategy needs to be repeated on schedule, we will use Python to build a scheduler that repeats cloning a mysql database using the terminal tool "mysqldump".  To this we will need to invoke an operationg system subprocess call using the "os" module. Next in our script, we will transfer the cloned schema ( *.sql file), . Next, you'll transfer the *.sql file to an external server via SSH, then we will restore the backup sql schema into remote db, perform a simple query to verify that the clone was performed sucessfully
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
The reason that we are importing the "sys" module is so we can accept a user's root password as a command line argument, and then assign it to a variable called password, which is then concatenated into mysqldump command called by the subprocess.
</p>
