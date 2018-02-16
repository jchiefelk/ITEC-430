<h1>Bash Tools</h1>

<h3>chmod</h3>

<p>
chmod is used to assign permisssions to files, folders, scripts. For example if I wanted to assign executable permissions to my Shell scripts, I would perform
</p>

<pre>
$chmod 755 sample.sh
</pre>

<p>
Also, in order to have executable permissions	
</p>

<h3>head & tail</h3>


<p>
Bash utility that prints to the terminal, either the starting or ending lines of a text file.	
</p>

<h3>Awk</h3>

<p>
A powerful command line tool. Useful for many things including reading structured data files in Bash.
</p>


<h4>Exercises</h4>

<p>
I.	Print to terminal the second column in a sample data file called sample.txt.  Use nano to create sample.txt,
<p>

<pre>
Bob 18
Alice 12
Sydney 13
Lindsey 40
</pre>

<p>
Using this command will print the second column to the terminal
</p>

<pre>
$awk ‘{print $2}’ sample.txt 
</pre>

<p>
II.	Write to file, the awk output.  To write data from a stream in Bash to a file you need to use the greater than operator (>). 
</p>

<pre>
$awk ‘{print $2}’ input.txt > output.txt
</pre>


<h3>sed</h3>

<p>
A very powerful Bash tool for editing data streams.
</p>

<h3>curl</h3>

<p>
cURL, aka curl, is a command line tool for transferring data between servers using one of the supported protocols; HTTP, HTTPS, FTP, more….
</p>

<p>
Let’s use curl in a shell script to automate unit-testing a REST API deployed locally to IP 127.0.0.1 and Port 5000. (http://127.0.0.1:5000/api).  In this script we’ll also do something new that we haven’t built into our shell script, use command line arguments.  Example,
</p>

<pre>
$curl -i -X GET http://localhost:5000/api -o output.txt
$sed '1!d' output.txt > http_responses_log.txt
$awk '{print $2}' http_responses_log.txt > tmp1.txt
$head tmp1.txt
</pre>

<h4>Exercises</h4>

<p>
I.	Create a server log and edit the output. You’ll need two terminal windows open for this exercise. Inside of <a href="https://github.com/jchiefelk/ITEC-430/tree/master/restAPI">restAPI</a>, deploy the api doing the following
</p>

<pre>
$python3 rest.py
</pre>

<p>
Next you need to send the API a query in order to generate a server log.  
</p>

<pre>
$curl -i -X GET http://localhost:5000/api -o server_response.txt
</pre>

<p>	
To edit the output file below, now we use sed.  We need sed because we are only interested in the http status code. Use sed to edit out all of the data except the first row
</p>

<pre>
$sed ‘1!d’ server_response.txt   
</pre>

<p>
sed receives it’s instructions inside of the single quotation mark.  The target file is specified after the instructions.
</p>

<p>
II.	Write sed output to data file. To write data from a stream in Bash to a file you need to use the greater than operator (>). 
</p>

<pre>
$sed ‘1!d’ server_response.txt > http_status_log.txt
</pre>
