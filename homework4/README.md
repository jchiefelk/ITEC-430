<h1>Homework 4 - More practice with Python</h1>

<p>
1)a)Take this unordered list of numbers,
</p>

<pre>
numlist = [100, 5, 9, 20, 1000, 3, 17, 87, 74]
</pre>

<p>
Now, using Python, create a new list with these numbers ordered from least to greatest.  Hint: You’ll have use something called a nested for loop, with a conditional if and else statement.  Feel free to lookup resources for this problem on the internet, note: I want this solved in the most simplest way (ie the least computationally efficient way) 
</p>

<p>
b)Take this list of strings, 
</p>

<pre>
Stringlist = [“robot”, “developer”, “engineer”, “AI”, “data”, “quantum”, “computing”, “statistics”, “backend”,”frontend”,”encryption”,”hacking”]
</pre>

<p>
2) Now, using Python, create a new numeric list, with elements being the length of the string elements in Stringlist. Hint: You’ll need to use string method len()
</p>

<p>
3) Create a method that prints to the screen, ‘Homework 3 problem 3’.
In a Python script, make a call to this method.
</p>
<p>
4) Create a new MySQL database on your Windows virtual machine, called users. Users is an entity that has attributes; username, password, score.  Populate with 5 entries, makeup 
</p>

<p>
5) Build a Python script that connects to your MySQL database using not a command line tool, but through a module called Flask.  This is like a research project on how to use methods from one of the MANY modules there are for Python
</p>


<h3>Problem 1 Help</h3>

<p>
  Odds are problem 1 was a humdinger of a problem for you. It sounds simple, but when you first Google how to sort an array of numbers you'll be hit with math-heavy material that is foreign.  This is good as you have not been introduced to it formally at SKC.  The intent of this problem was to expose you to the topic of Data Structures and Algorithms</p>
  
<h4>Brute-Force Method</h4> 

<p>  
This easiest method for a Newb to implement this is by using a method does not require any fancy data structure or algroithm.  The Brute-Force method just requires a nested for loop with a conditional statement to create a new ordered array.  The brute force method of taking an unordered list/array and creating an ordered array is called Bubble Sort.
</p>
  
<p>
Bubble Sort is the LEAST efficient method (ie. the slowest) for sorting an unordered array.  This method should be avoided for any professional task. It serves as only as an intro to sorting.  The example code below is how you go about implementing bubble sort in Python.
</p>

<p>
  Bubble sort works comparing adjacent elements in an array and repeatedly swapping the adjacent elements if they are in wrong order.  It is an N^2 algorithm, meaning it takes longer and longer required to sort the larger the unsorted array size.  Below is it's
</p>

<pre>
# Python program for implementation of Bubble Sort
 
def bubbleSort(numlist):
    n = len(numlist)
 
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if numlist[j] > numlist[j+1]:
            	numlist[j], numlist[j+1] = numlist[j+1], numlist[j] #array swap
 

# unsorted list
numlist = [64, 34, 25, 12, 22, 11, 90] 
bubbleSort(numlist)
print("Sorted array is:")
print(numlist)
</pre>
