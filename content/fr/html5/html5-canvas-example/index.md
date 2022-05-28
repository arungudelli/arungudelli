+++
title="HTML5 Canvas Example :A Simple Snake Game"
summary="A simple Snake Game using HTML5 Canvas.Step by step tutorial to develope Snake game using Html5 Canvas and JavaScript."
keywords=["html5 canvas example,html5 canvas tag,html5 canvas tutorial,html5"
]
type='post'
date='2019-09-16T18:07:47+0000'
lastmod='2019-09-16T18:07:47+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++


I will explain basics of HTML5 Canvas with an Example.

You will learn How to develop <a title="Snake Game" href="https://www.arungudelli.com/Tools/HTML5/SnakeGame/snakeGame.html" target="_blank" rel="noopener">Snake Game</a> using HTML5 Canvas.If you familiar with JQuery then it’s very easy.

<span style="text-decoration: underline;"><em><strong>HTML5 Code:</strong></em></span>

These are the main elements in html.

<ul><li>One &lt;canvas&gt; element for Snake Game.</li><li>Two &lt;audio&gt; tags for GamePlay and GameOver</li><li>One &lt;p&gt; Tag for displaying Scores.</li><li>And buttons for Play,pause,SoundOFF,SoundON.</li></ul>





<span style="text-decoration: underline;"><em><strong>Game Conditions:</strong></em></span>

<ul><li>Use Arrows to Move Snake.</li><li>And exit Game when snake eat itself.It’s your decision you can exit your game if it hits the Wall.</li></ul>

<span style="text-decoration: underline;"><em><strong>Now Play around with Jquery:</strong></em></span>

First thing Logic of the Game.It is simple.

<ul><li>Create an Array of Snake.</li><li>Write a function to paint snake array in Canvas.</li><li>Write a function for creating food.</li><li>Moving of snake:Remove Tail of the snake(Last element in array) and append to the Head(First Element)</li><li>Increment the Head.</li><li>Trigger the Paint function continuously.</li><li>And write exit conditions.</li></ul>



&nbsp;

<span style="text-decoration: underline;"><em><strong>Key Board Movements:</strong></em></span>

Here is the code for key board movements. This function calls when keydown event occurs.Here I am checking one condition “allowPressKeys” this will disable the arrows when game is in pause mode.



&nbsp;

<span style="text-decoration: underline;"><em><strong>Creating Food and snake:</strong></em></span>

Creating food is nothing but painting one random pixel within the canvas.Each time generate one random pixel,paint it.For Snake Declare one array.Assign some length initially.Call Paint_cell function.



&nbsp;

<span style="text-decoration: underline;"><em><strong>Checking Exit Conditions:</strong></em></span>

If snake head meets it’s body then the game will end. Ouroboros_Check take arguments HeadX,HeadY,And SnakeArray,checks whether head meets Snake Body.(The&nbsp;Ouroboros<a href="http://en.wikipedia.org/wiki/Ouroboros" target="_blank" rel="noopener">&nbsp;</a>is a symbol representing a Dragan eating own it’s tail.).When game ends we will call Startgame function.



&nbsp;

<span style="text-decoration: underline;"><em><strong>Play and Pause Game:</strong></em></span>

The key of the Game is calling Paint function continuously. &nbsp;<em><strong>setInterval</strong></em> is a standard Java Script function,we can call it with a function(or code snippet) to execute it for every period in milliseconds.

For Example &nbsp;<em><strong>var AlertMsg=setInterval(function (){alert(“Hello”);},2000);</strong></em>

The above Code &nbsp;display alert message for every 2 seconds. And For stopping we use&nbsp;<em><strong>clearInterval</strong><strong>(AlertMsg)</strong></em> function.

In play method we will call setInterval with Paint() and in Pause we will call clearInterval.<br>



&nbsp;

<span style="text-decoration: underline;"><em><strong>Game Sounds And Buttons:</strong></em></span>

With &lt;audio&gt; tag in HTML5 We can include sounds in Web page.I am used three audio tags for Gameplaying(background music),GameOver(When snake eat itself) and SnakeEatingFood.



&nbsp;

And I included some text between &lt;audio&gt; and &lt;canvas&gt; tags.



If a browser supports canvas and audio tags then it simply ignore the text between the tags.And If not then the browser ignore the tags and displays the text between tags.No need to check canvas and audio support explicitly.


If you have any doubts,suggestion feel Free to Post comments.


Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







