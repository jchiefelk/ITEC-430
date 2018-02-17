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
 Now this will produce an errors. Something like port 22 not found.  This has to do with the need to generate an RSA key pair
</p>

<pre>
$ssh-keygen -t rsa
$sudo service ssh restart
</pre>

<p>
  Now try to login again. You'll be prompted for a password and if you want to save your public key on the OpenSSH server.  After you succesfully login, navigate about, create a file and example.txt.  Use nano to add the following test, "Working remotely". To exit the remote session, execute
</p>

<pre>
$exit
</pre>


<h3>Security Deprecations</h3>

<p>
  Older versions of OpenSSH use to offer DSA as an encription protocol to generate keys. It is very important that you NO LONGER USE DSA.   In fact, DSA is disabled in OpenSSH versions 7.0 and greater, see <a href='http://www.openssh.com/legacy.html'>Legacy.</a> You can read more about this DSA vulnerabilities in these useful links.</p> 
  
<p>
  <a href='https://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys'>Stack Exhcange thread</a>
</p>

<p>
  <a href='https://isecpartners.com/media/105564/ritter_samuel_stamos_bh_2013_cryptopocalypse.pdf'>A presentation at BlackHat 2013 </a>
</p>


<p>
  Essentially the reason behind this is because the DSA protocol is built on a SHA-1 Encryption Algorithm, which has been broken publicly in 2017, read here in <a href='https://www.pcworld.com/article/3173791/security/stop-using-sha1-it-s-now-completely-unsafe.html'>PC World</a>
</p>


<h3>SSH on Windows</h3>

<p>
SSH clients for Python are horrendous to settup on Windows (SharpSSH, paramiko).  It is way more advantages to use PuTTy.  Download Putty <a href="https://www.putty.org/">here.</a> . What we want from PuTTy for our backup strategy, is the command line tool pscp. pscp is equivalent to scp in linux
</p>

<h4>scp</h4>
<p>
  scp is a Bash command-line tool for transfering data files over ssh.  The equivalent command in Windows after installing PuTTy is pscp.  You'll need to restart your computer after installing in order to use pscp or other PuTTy tools in either the command prompt or PowerShell. 
</p>


<h3>Establishing an SSH connection</h3>

<p>
First lets Ping our Ubuntu localhost from Windows Command prompt.  To get the ip address of your Ubuntu server, execute
</p>

<h4>ifconfig</h4>
<pre>
$ifconfig
</pre>

<p>
 Then on your Windows machine Ping this address
</p>

<pre>
>ping 192.x.x.x
</pre>

<p>If no error, then test to see if you can send a file over ssh using pscp.  Create a test file in your directory, a Python script, called putty.py.

<pre>
>pscp -pw "password_here" putty.py username@x.x.x.x:
</pre>
