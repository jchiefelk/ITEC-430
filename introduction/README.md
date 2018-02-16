<h1>Introduction to Scripting</h1>

<h3>Goals</h3>

<p>
To equip you with the ability to use variables, arrays, functions, in Python and Bash scripts.
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



<h4>Arrays</h4>
	Arrays is a very commonly used data structure.  In the latest versions of Bash & PowerShell come with these data types.  They are useful for storing a set of numbers or strings.  Arrays in Bash/PowerShell are analogous to Lists in Python.  The difference between Arrays in Shell are as follows.
This is how you assign contents to an array in Bash.

<pre>
$array=(“Bob” “Alice” “Charles” “Linda” “George”)
</pre>

This is how you assign a List in Python 3.
<pre>
list=[“Bob”,“Alice”,“Charles”,“Linda”,“George”]
</pre>
<p>
Note these differences. 1) In Bash you use Parentheses and in Python you use Brackets. 2) The Elements in Bash are white-space separated, in Python they are comma-separated.
	Elements are the contents of an array.  They are accessed by their indice, i.e their position in the Array/List.  Important, the first element in an Array, “Bob”, starts at 0, the first element in a List also starts at 0.  The next element, “Alice”, is at position 1. The next element “Charles” at position 2, and so on.
Another way to assign Array/List elements is to individually do so, as opposed to all at once. 
</p>
<p>
In Bash,
</p>

<pre>
array[0]=”Bob”
array[1]=”Alice”
array[2]=”Charles”
</pre>

<p>
In Python 3,
</p>

<pre>
list[0]=”Bob”
list[1]=”Alice”
list[2]=”Charles”
</pre>	
<p>
	Suppose you need to manually add a new element to an existing array.
</p>

<p>
In Bash, you use the += operator
</p>

<pre>
array=(“Bob” “Alice”)
array+=(“Charles”)
</pre>
<p>In Python, you use a List Method</p>

<pre>
list=(“Bob” “Alice”)
list.extend(“Charles”)
</pre>

<p>To access Array/List elements, in Bash you specify it first with dollar operator $ and Braces {}.  This tells the terminal’s interpreter that what comes after is an array.</p>
 
<pre>
${array[0]} 
</pre>

<p>To access List elements in Python,</p> 

<pre>
list[0]
</pre>

<h3>Control Statements</h4>
<p>
The most commonly used control statement is the for loop.  This statement controls
how many times a set of commands are executed.  Very useful when you need to repeat many of the same commands more than once.  Note, to use for loops in Bash you need to use the SheBang (!#) operator and set the script as an executable. This is because the latest version of Bash comes with all sorts of Bells and Whistles that the default on Bash in Ubuntu installed on your Virtual Machine.
</p>
<p>
In Bash, use nano to put this at the top of a script (name test.sh) that we set as an executable
</p>

<pre>
#!/binbash  
</pre>	
<p>Next, use chmod to set execute permissions,</p>

<pre>
chmod 755 test.sh
</pre>

<p>
Boom, now open test.sh with nano and add the following lines after the shebang.
</p>


<pre>
array=(“Bob” “Alice” “Charles” “Linda” “George”)
	for x in “${array[@]}”
	do
		echo ${array[$x]}
	done
</pre>

<p>Everything inside of the do-done lines is the instructions that are executed inside of the for loop.  Another way to use a for loop, if you know the length of your array(we do, 5) is so</p>
<pre>
	for x in {0..4}
	do
		echo ${array[$x]}
	done
</pre>
<p>
Note, recall an array starts at 0.  The 4 specifies which index is the last. So for the for loop, we need to subtract the length of the array (5) by one.  This all very cryptic.
</p>

<p>
In Python,
</p>

<pre>
for x in range(0,list.len()-1):
	print(list[x])
</pre>
<p>OR,</p>

<pre>
for x in range(0,4):
	print(list[x])
</pre>

<p>
len() is a List method in Python that gives the length of an array
</p>




