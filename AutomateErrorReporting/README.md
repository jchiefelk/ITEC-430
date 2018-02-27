 <h1>Automate Error Reporting</h1>


<h3>Step 1: Set up Mail Server</h3>

<p>
</p>

<pre>
sudo apt-get install mailutils
</pre>



<pre>
apt-get install ssmtp
</pre>


<pre>
sudo nano /etc/ssmtp/ssmtp.conf
</pre>

<p>Add the following to the file:</p>
 
AuthUser=<user>@gmail.com
AuthPass=Your-Gmail-Password
mailhub=smtp.gmail.com:587
UseSTARTTLS=YES

<p>
Save and close the file:
</p>

<pre>
Hit Escape
Type :wq
Hit Enter
</pre>


<p>Test it out</p>

<pre>
echo "This is a test" | mail -s "Test" <user>@<email>.com
</pre>
