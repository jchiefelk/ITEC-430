 <h1>Configure Global Github Configuration</h1>

<p>
  Set global github configuration with userName and Password.
</p>


<pre>
   git config --global user.name "Your Name"
   git config --global user.email you@example.com
</pre>

<p>
After doing this, you may fix the identity used for this commit with:
</p>

<pre>
    git commit --amend --reset-author
</pre>

<p>
  Now try to pull data.....
</p>
