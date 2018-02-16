<h1>Introduction to Scripting</h1>

<h3>Goals</h3>

<p>
Using variables in shell
</p>

<h4>What are variables?</h4>
<p>Variables are just locations in memory that store information.  In shell, variables can store strings, numbers, or files.</p>


<h4>How are variables used in Bash Shell?</h4>
<p>In Bash variables are treated just as they were in Python.  Variables are not declared, and are assigned a value upon first use.</p>

<pre>
$variable=”hello world”
</pre>

<p>
Note, in Shell there can be no space between the equals sign, while in Python there is some more leeway to use white spaces.
</p>					

<h4>How are variables assessed in Python?</h4>

<p>In Shell, variables are assessed using the dollar sign prompt $.  This tells the Bash Interpreter that the text specified after the $ is a variable.</p>

<h4>How is number variable assignment different?</h4>

<p>In Shell, numeric variables are assigned using declare.</p>

<pre>
$declare -f number=2
</pre>

<h3>Exercises</h3>

<h4>String Variables</h4>

<p>
Write a script that prints the variable to the screen using the echo command.  Echo is the analogous function in Shell as print() in Python 3 and Javascript.  It prints to the terminal console anything followed after echo.  Example, “hello World” to the terminal.
</p>
	
<pre>
$echo $variable
</pre>

<h4>Number Variables</h4>

<p>Write a script that prints the number variable to the terminal</p>


