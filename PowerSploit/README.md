<h1>PowerSploit</h1>

<h4>What is PowerSploit?</h4>

<p>PowerSploit is collection of Offensive Active Directory modules or Exploitation Framework</p>

<h4>Installing PowerSploit</h4>

<p>
Clone PowerSploit from Github
</p>

<pre>
>git clone https://github.com/PowerShellMafia/PowerSploit.git
</pre>


<p>
 Next, disable Windows Defender.
</p>

<pre>
 >Set-MpPreference -DisableRealtimeMonitoring $true
</pre>

<p>
 Then copy PowerSploit to your module path.  To find your module path,
</p>

<pre>
>$Env:PSModulePath
</pre>

<p>
To copy PowerSplot into this folder,
</p>

<pre>
>copy C:\Users\Administrator\PowerSploit C:\Windows\system32\WindowsPowerShell\v1.0\Modules
</pre>

<p>
 Then properly import the module into your environment variables
</p>

<pre>
>Import-Module PowerSploit
</pre>

<p>
To check if the installation was a success, run this command to see a list of all of the Cmdlets that come with this module. 
</p>

<pre>
>Get-Command -Module PowerSploit
</pre>
