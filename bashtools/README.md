<h1>Bash Tools</h1>


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
