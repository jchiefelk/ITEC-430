<h1>Using Github</h1>
<p>
Configure Global Github Configuration
Set global github configuration with userName and Password.
</p>
<pre>
   git config --global user.name "Your Name"
   git config --global user.email you@example.com
</pre> 
   
<p>
After doing this, you can fix the identity used for the commits within existing clone repos using....
</p>
<pre>
    git commit --amend --reset-author
</pre>

<p>
Now try to pull data.....
</p>


<h3>How to push to Github</h3>
<pre>
git add .
git commit -m "add comments here"
git push
</pre>
