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
  This is an over simplification of the process, but for a newbie to crypto this is sufficient enough.  Specifically is is very important that you NO LONGER USE DSA.  The reasons behind this, is because DSA is now vulnerable to Brute-Force attack.  You can read more about this vulnerability here at this thread on <a href='https://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys'>Stack Exhcange</a>
</p>
