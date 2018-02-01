 <h1>PowerShell</h1>
<h3>Review</h3>

<p>1) creating a new directory using new-item</p>

<pre>
new-item -Name itec430 -ItemType directory 
</pre>

<p>2) Navigating directory</p>

<pre>
Set-Location dir_name
</pre>

<p>3) Listing directory (same as Bash)</p>

<pre>
ls
</pre>

<p>4) Print to terminal</p>

<pre>
Write-Host "Hello World"
</pre>

<p>5) Print working directory to console</p>
<pre>
cmd
</pre>

<p>6) The "which" command, used to locate the directory an execuatble is stored, is "where" in Windows.</p>

<pre>
(Get-Command python).Path
</pre>


<p>7) Removing a Directory</p>
<pre>
rd directory_name
</pre>


<h3>Installing Python 3, Pip, and an IDE</h3>
<p>First, you need login into Administrator account on your Virtual Machine.  Python 2 is installed by default in Windows Server 2016.  First go into Interent Explorer, then go to "Internet Options", then "Security", then check "Disable", then select into "Custom level".  Enable downloads.
</p>

<p>
Next download the latest version of Python 3 from <a href="https://www.python.org/downloads/windows/"> https://www.python.org/downloads/windows/ </a>. Select add Python 3 to Path, and Recommended Installation.
</p>

<p>
Test if Python 3 is copied to your default path in PowerShell running
</p>

<pre>
python
</pre>

<p>This should print Verson 3. something.  Exit the Python Shell, then download <a href="https://www.sublimetext.com/">Sublime Text</a> </p>

<p>Last, install Git on Windows Server 2016 at <a href="https://git-scm.com/downloads">https://git-scm.com/downloads</a> </p>


<h3>Accessing PowerShell inside of a Python Script.</h3>

<pre>
import os
import msvcrt
def getch():
        msvcrt.getch()
print("Type a key!")
getch()
print("Okay")	
</pre>
