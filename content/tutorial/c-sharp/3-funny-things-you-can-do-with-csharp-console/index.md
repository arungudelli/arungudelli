+++
title="3 Funny Things You Can Do With C# Console"
summary="Play around with C# Console with properties like C# Console.Title,C# Console.SetWindowSize() and C# Console.Beep().I hope you will enjoy this article"
keywords="c# console.title,c# console.setwindowsize(),c# console.beep(),c# console,c#"
type='post'
date='2019-10-13T18:05:25+0000'
lastmod='2019-10-13T18:05:25+0000'
draft='false'
authors=['admin']
[image]
focal_point=''
preview_only=false
+++

Yesterday I am discussing with one of my cousin, he is currently doing a course on C# .Net. He is experimenting lot of things in C#, I came to to 3 funny code snippets to play around C# console through him. I thought it’s a good idea to share with you people.

These code snippets may not help us in our daily life but it’s good know these things.

### <span style="text-decoration: underline;">Fun with Console Title:</span>

<a title="Console.Title CSharp" href="http://msdn.microsoft.com/en-us/library/system.console.title%28v=vs.110%29.aspx" target="_blank" rel="noopener">Console.Title</a> property sets the title of C# console window.

We can set animated console title like below using following code snippet.

{{< figure src="AnimatedConsoleTitles.gif" title="Animated Console Title" alt="Animated Console Title" >}}

<pre>            string Progresbar = "This is animated title of Console";
            var title = "";
            while (true)
            {
                for (int i = 0; i &lt; Progresbar.Length; i++)
                {
                    title += Progresbar[i];
                    Console.Title = title;
                    Thread.Sleep(100);
                }
                title = "";  
            }</pre>

&nbsp;

### <span style="text-decoration: underline;">Moving Console Window</span>

We can use&nbsp;<span style="text-decoration: underline;">Console.SetWindowSize(numberColumns, numberRows)</span>&nbsp;property to set the console window size. We use this property to create moving console window as shown above with following code snippet.

{{< figure src="AnimatedWindowSizeConsole.gif" title="Animated Window Size Console" alt="Animated Window Size Console" >}}

<pre>            for (int i = 1; i &lt; 40; i++)
            {
                Console.SetWindowSize(i, i);
                System.Threading.Thread.Sleep(50);
            }</pre>

&nbsp;

### <span style="text-decoration: underline;">Annoying Beep Sound:</span>

We can use Console.Beep() method to emit beep sound from system speakers.

We can annoy the &nbsp;user by setting different frequencies and durations.

<pre>            private static int frequency = 10000;
            private static int duration = 100;
            Console.WriteLine("Use keyboard arrows to adjust frequency and duration");
            do
            {
                while (!Console.KeyAvailable)
                {
                    Console.Beep(frequency, duration);
                }

                var key = Console.ReadKey(true);

                switch (key.Key)
                {
                    case ConsoleKey.UpArrow:
                        frequency += 100;
                        frequency = Math.Min(frequency, 15000);
                        break;
                    case ConsoleKey.DownArrow:
                        frequency -= 100;
                        frequency = Math.Max(frequency, 1000);
                        break;
                    case ConsoleKey.RightArrow:
                        duration += 100;
                        duration = Math.Min(duration, 1000);
                        break;
                    case ConsoleKey.LeftArrow:
                        duration -= 100;
                        duration = Math.Max(duration, 100);
                        break;
                }
            } while (true);</pre>

&nbsp;

<span style="text-decoration: underline;"><strong>Bonus Tips:</strong></span><strong>&nbsp;&nbsp;</strong><a title="C# Delegates and Events" href="https://www.arungudelli.com/csharp/delegates-and-events-in-csharp/" target="_blank" rel="noopener">Understand C# Delegates and Events in C# with simple real world examples</a>

&nbsp;

Download&nbsp;<a href="http://sdrv.ms/1b4HWa7" target="_blank" rel="noopener">Source Code</a>

Download&nbsp;<a href="http://sdrv.ms/1b4HWa7" target="_blank" rel="noopener">Source Code</a>

&nbsp;

Wait before leaving.
why can’t you follow me on <a href="https://twitter.com/arungudelli" target="_blank" rel="noopener">twitter</a> or be a friend on <a href="https://www.facebook.com/gudelliArun" target="_blank" rel="noopener">Facebook</a> or  <a href="https://www.linkedin.com/in/arungudelli/" target="_blank" rel="noopener">linkedn</a> to get in touch with me.







