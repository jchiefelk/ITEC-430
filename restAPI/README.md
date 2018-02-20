
<h1>REST APIs</h1>

<h4>What is an API?</h4>
<p>
	An API is an “Application Programming Interface”. 
</p>

<h4>What is an Application Programming Interface?</h4>
<p>
An Application Programming Interface is a set of protocols or routines for hosting application software.  There are many different types of APIs and REST is just one of the lot.
</p>

<h4>What is a REST API?</h4>
<p>
REST, “Representational State Transfer”, is a web service standard.  An organization hosting a RESTful service is hosting a web resource that can be requested via a URL-endpoint.
</p>


<h4>Where is REST implemented?</h4>
<p>Almost every company or organization that offers Software as a Service (SaaS).</p>


<h4>Industries that implement REST APIs</h4>
<p>US Government, Banking, Tech Companies, etc..</p>

<h4>Is REST implemented in Health Care Data?</h4>

<p> 
No and Yes. Medical Health Records are becoming accessible through a protocol called FHIR.  It is REST-like, in the sense that you access data via a URL-endpoint.  A long list of FHIR vendors can be found, here.
</p>

<h3>Exercises:</h3>

<p>
<h4>I.	Sample requests to a REST API using a Graphical User Interface.</h4>  

<p>
We’ll take a look at historical price data on Bitcoin served by GDAX’s REST API as an example. 
</p>

<p>1) You need to install Google Chrome on either Windows or Ubuntu.</p>
<p>2) You need to install Postman.</p>
<p>3) Create a GET Request inside of Postman. Inside of the “Enter request URL” input field, copy and paste https://api.coindesk.com/v1/bpi/historical/close.json. Then click send.</p>

<p>It is much better/easier to view the response as JSON. Click the dropdown that says “Auto” and select “JSON”.</p>


<h4>4) Add parameters to query</h4>

<p>
To get different information from the API, we need add some parameters to our query. Parameters in a REST API query are specified after the question mark (?).  To get the price of Bitcoin since 2017, add “start=2017-01-01” after adding (?).
https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-01-01
</p>

<p>
To add multiple parameters to the query, add an ampersand (&).  For example, to get the price of Bitcoin between January 1, 2017 and March 1, 2017 from the API, after (&) add “end=2017-09-01”.  https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-01-01&end=2017-09-01
</p>


<h4>II.	Querying a REST API with curl</h4>

<p>
cURL, aka curl, is a command line tool for transferring data between servers using one of the supported protocols; HTTP, HTTPS, FTP, more….  Let’s use curl in a shell script to automate unit-testing a REST API deployed locally to IP 127.0.0.1 and Port 5000. (http://127.0.0.1:5000/api).  In this script we’ll also do something new that we haven’t built into our shell script, use command line arguments.  Example,
</p>

<pre>
$curl -i -X GET http://localhost:5000/api -o output.txt
$sed '1!d' output.txt > http_responses_log.txt
$awk '{print $2}' http_responses_log.txt > tmp1.txt
$head tmp1.txt
</pre>
