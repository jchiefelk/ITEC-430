<h1>Homework 8 - Import and Explore Recon Module</h1>



<h3>1) Import the Recon module.</h3>

<p>
This will install the PowerView Cmdlets 
</p>


<h3>Explore the Reconnaissance tools of PowerView</h3>


<h4>Finds machines on the local domain where specified users are logged into, and can optionally check if the current user has local admin access to found machines</h4>

<pre>
Invoke-UserHunter
</pre>


<h4>Get all current GPOs for a given domain</h4>

<pre>
Get-NetGPO
</pre>

<h4>Return the default domain or DC policy</h4>

<pre>
Get-DomainPolicy
</pre>


<h4>Takes a computer and determines who has admin rights over it through GPO enumeration</h4>

<pre>
Find-GPOComputerAdmin -OUName OU_Name
</pre>


<h3>Phineas Fisher</h3>

<p>
"The best tool these days for understanding windows networks in PowerView".  Reference, <a href="https://pastebin.com/raw/0SNSvyjJ">https://pastebin.com/raw/0SNSvyjJ</a>
</p>
