<h1>SSH</h1>

<p>
  SSH is a technology that allows for secure remote access between computers, over an unsecured network.  It achieves this extra security measure using Public Key Cryptography.
</p>

<h3>Public/Private Key Cryptography</h3>

<p>
  This technology was originally engineered by the US Military.  It provides an extra layer of security on top of remote acess using a just password, which is vulnerable against a Brute-Force Attack.  As an example, lets think of 2 people who want to remotely connect over ther internet, Alice and Bob. The method works as follows  
</p>

<p> 1) A User encrypts their message using both their Private and the others servers Public Key</p> 
<p> 2) They send this message over unsecure network</p>
<p> 3) The receiver then decrypts </p>

<p>
  This is an over simplification of the process, but for a newbie to crypto this is sufficient enough.  To launch SSH on your Ubuntu machine, first download OpenSSH.
</p>

<h3>Download SSH</h3>

<pre>
$sudo apt-get install openssh-server
</pre>


<h3>Configure SSH and Deploy</h3>

<p>
  Next, lets look at the configuation file. IMPORTANT note, sshd_config is the configuration file for the OpenSSH server. ssh_config is the configuration file for the OpenSSH client. Make sure not to get them mixed up.  To edit server ssh config file on your Ununtu machine, execute 
</p>

<pre>
$nano /etc/ssh/sshd_config
</pre>

<p>
Important Note, do not edit your server configuration file before you make a backup, just incase you edit it and something goes FUBAR.  To backup your configuration file, perform the following.
</p>

<pre>
$sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
</pre>

<p>
 To connect to your locahost, execute
</p>

<pre>
$ssh 127.0.0.1
</pre>

<p>
 Now, this will produce an errors. Something like port 22 not found.  This has to do with the need to generate an RSA key pair
</p>


<pre>
$ssh-keygen -t rsa
$sudo service ssh restart
</pre>

<p>
  After you succesfully login, navigate about. To exit the remote session, execute
</p>


<pre>
exit
</pre>

<p>
 Specifically is is very important that you NO LONGER USE DSA.  The reasons behind this, is because DSA is now vulnerable to Brute-Force attack.  You can read more about this vulnerability here at this thread on <a href='https://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys'>Stack Exhcange.</a>
</p>

<p>
  In fact, DSA is disabled in OpenSSH versions 7.0 and greater, see <a href='http://www.openssh.com/legacy.html'>Legacy.</a>
</p>





