---
layout: page
title: "DO NOT USE: Project 2A: NGrams"
nav_order: 1
toc_max_heading: 2 # hide h3 headings from table of contents
nav_exclude: true
---

## Spec Update

{% capture update %}{% include proj2-update.html %}{% endcapture %}
{{ update | markdownify }}

## Unreleased

{: .IMPORTANT}
> Since some students may still be working on Project 2A: NGrams, we are leaving the original Project 2A spec
> up [here](/projects/proj2a/). Please refer to this one for now.
>
> The new spec below will replace the original one once we are finished running the Project 2A: NGrams assignment (e.g. when
> no one is actively working on it).

# Project 2A: NGrams

{: .NOTE}
> *Lectures needed for this project:*
> - Lecture 3: ADTs + Lists
>
> *Partner policy:* No partners, and the solutions you submit should be your own work! More details on [the policies page](/policies/#collaboration-policy).
>
> *LLM policy:* LLMs should not write any of the code that you turn in. See more info in [the LLM policies page](/policies/#llm-policy) for more details.

---

## Overview

In this project, we will build a browser-based tool for exploring the history of word usage in English texts.

The [Google Ngram dataset](http://storage.googleapis.com/books/ngrams/books/datasetsv3.html) provides many terabytes of information about the historical frequencies of all observed words and phrases in English (or more precisely, all observed [ngrams](http://en.wikipedia.org/wiki/N-gram)). Google provides the [Google Ngram Viewer on the web](https://books.google.com/ngrams/graph?content=global+warming%2Cto+the+moon&year_start=1800&year_end=2019&corpus=en-2019&smoothing=0), allowing users to visualize the relative historical popularity of words and phrases. For example, the link above plots the *weighted popularity history* of the phrases "global warming" (a 2gram) and "to the moon" (a 3gram).

In Project 2A, you will be build a version of this tool that only handles 1grams. In other words, you'll only be able to handle individual words. We'll only use a small subset (around 150 MB) of the full 1grams dataset, as larger datasets will require more sophisticated techniques that are out of scope for this class.

We have provided the front end code (in Javascript and HTML) that collects user inputs and displays outputs. Your Java code will be the back end for this tool, accepting input and generating appropriate output for display.

To support this tool, you will write a series of Java packages that will allow for data analysis. Along the way we'll get lots of experience with different useful data structures. The early part of the project (Project 2A) will start by telling you exactly what functions to write and classes to create. The later part (Project 2B) will be more open to your own design.

[See below or click here for a video introduction to the project.](https://www.youtube.com/watch?v=ri9BzE723QA&list=PL8FaHk7qbOD7-899l1hKEd5aICB9u1wrm&index=1) Note that the videos might have some slightly outdated sections.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ri9BzE723QA?si=CSpOnUIKmQjQ3Jm_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jd1g9LnpTtg?si=cnti0cxFieGNAYrm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/kX11gp2l_y0?si=d5ysNhFD6iJLIPKQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

To see what the fully-finished project looks like, check out the staff implementation at [ngordnet.datastructur.es](https://ngordnet.datastructur.es).

## Setup

Follow the [Assignment Workflow Guide](/resources/assignment-workflow/) to get started with this assignment. This starter code is in the `proj2a` folder.

You'll also need to download the NGrams data files (they are around 150 MB, which is too large to be pushed to GitHub).

## Task 0: NGrams Data

{: .TASK}
> Follow the instructions in the [Data](/proj2/proj2-data/#ngrams) spec to get the NGrams data. There, you'll find descriptions of the dataset. Make sure you understand how each file is structured so you can read and parse it.

## Task 1: TimeSeries

A `TimeSeries` is a special purpose extension of the existing `TreeMap` class, where:
- The key type parameter is always `Integer`, representing a year.
- The value type parameter is always `Double`, representing a numerical data point for that year.

The `TimeSeries` class provides some additional utility methods to the `TreeMap` class, which it extends. [See the `TreeMap` API](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeMap.html) to see which methods are available to you.

For example, the following code would create a `TimeSeries` and associate the year 1992 with the value 3.6 and 1993 with 9.2.

```java
TimeSeries ts = new TimeSeries();
ts.put(1992, 3.6);
ts.put(1993, 9.2);
```

{: .TASK}
> Write tests for each `TimeSeries` method in `src/tests/TimeSeriesTest.java`.
>
> Your tests will not be graded, however keep in mind that test writing is good practice and will save you time down the line when you run into issues. See the [Testing](/proj4/proj4-testing/#timeseries) spec for more information.
>
> Once you've finished writing tests, implement the methods in `src/main/TimeSeries.java` according to the API provided in the file. See `testFromSpec()` in `src/tests/TimeSeriesTest.java` for an example of how to use a `TimeSeries`.

You may not add additional public methods to this class. You're welcome to add additional private methods.

Tips:
- `TimeSeries` objects should have no instance variables. A `TimeSeries` is-a `TreeMap`. That means your `TimeSeries` class also has access to all methods that a TreeMap has; see [the TreeMap API](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeMap.html).
- Several methods require that you compare the data of two `TimeSeries`. You should not have any code which fills in a zero if a year or value is unavailable.
- You may assume that the `dividedBy` operation never divides by zero.


## Task 2: NGramMap

The `NGramMap` class will provide various convenient methods for interacting with Google's NGrams dataset. This task is more open-ended and challenging than the creation of the `TimeSeries` class. As with `TimeSeries`, you'll be filling in the methods of an existing `NGramMap.java` file.

There is a lot to think about for this part of the project. We're trying to mimic the situation in the real world where you have some big open-ended problem and have to figure out the approach from scratch. This can be intimidating! It will likely take some time and a lot of experimentation to figure out how to proceed. To help keep things from being too difficult, we've at least provided a list of methods to implement. Keep in mind that in the real world (and in later projects in this class), even the list of methods will be your choice.

{: .TASK}
> Fill out the constructor of the `NGramMap`.
>
> You'll need to parse through the provided data files and store this data in data structure(s) of your choice.

Tips:
- Choosing the right data structure(s) is important, since picking the right data structure(s) can make your life a lot easier when implementing the rest of the methods. Thus, we **STRONGLY RECOMMEND** taking a look at the rest of the methods first to help you decide what data structure might be best; then, begin implementing the constructor.
- Avoid using a HashMap or TreeMap as an [actual type argument](https://docs.google.com/presentation/d/1j2vivowiaZWepIjUoWj6Cx3CdJiyuYslxkg8GsT8kxM/pub?start=false&loop=false&delayms=3000&slide=id.g631db3c57_38) for your maps. This is usually a sign that what you actually want is a custom defined type. In other words, if your instance variables include a nested mapping that looks like `HashMap<blah, HashMap<blah, blah>>`, then a `TimeSeries` or some other class you come up with might be useful to keep in mind instead.
- We have not taught you how to read files in Java. We recommend using the `In` class. [The official `In` documentation can be found here.](https://introcs.cs.princeton.edu/java/stdlib/javadoc/In.html) We provide an example class `src/demo/FileReadDemo.java` that gives examples of how to use `In`. You're welcome to use whatever technique you'd like that you learn about online but staff may not be familiar and unable to provide assistance.
- If you use `In`, don't use `readAllLines` or `readAllStrings`. These methods are slow. Instead, read inputs one chunk at a time. See `src/demo/FileReadDemo.java` for an example.


### NGramMap Methods

Your constructor parsed the data files, and stored the data in some data structures. Now, the methods in NGramMap can compute interesting results from that data. For example, consider these data files (only relevant rows/columns shown):

```
word_history_size3.csv:
-----------------------------
Word        Year    Frequency
airport     2007    175702
airport     2008    173294
wandered    2005    83769
wandered    2006    87688
wandered    2007    108634
wandered    2008    171015
...
```

```
year_history.csv:
-----------------------------
Year    Total number of words
2005,   26609986084
2006,   27695491774
2007,   28307904288
2008,   28752030034
...
```

<table>
    <tr>
        <th style="width:20%">Method</th>
        <th style="width:30%">Description</th>
        <th style="width:50%">Example</th>
    </tr>
    <tr>
        <td><code>countHistory</code></td>
        <td>
            Takes in a word. For each year, return the frequency of the word in that year.
        </td>
        <td>
            <code>countHistory("wandered", 2006, 2007)</code><br>should return<br><code>{2006: 87688, &nbsp;&nbsp; 2007: 108634}</code>.
        </td>
    </tr>
    <tr>
        <td><code>totalCountHistory</code></td>
        <td>
            For each year, return the total number of words in that year.
        </td>
        <td>
            <code>totalCountHistory()</code> should return<br><code>{2005: 26609986084, &nbsp;&nbsp; 2006: 27695491774, ...}</code>.
        </td>
    </tr>
    <tr>
        <td><code>weightHistory</code></td>
        <td>
            Takes in a word. For each year, return the frequency of the word in that year, divided by the total number of words in that year.
        </td>
        <td>
            <code>weightHistory("wandered", 2006, 2007)</code><br>should return<br><code>{2006: 87688 / 27695491774,<br>&nbsp;2007: 108634 / 28307904288}</code>.
        </td>
    </tr>
    <tr>
        <td><code>summedWeightHistory</code></td>
        <td>
            Takes in multiple words. For each year, return the summed frequency of all the input words in that year, divided by the total number of words in that year.
        </td>
        <td>
            <code>summedWeightHistory(["wandered", "airport"], 2006, 2007)</code><br>should return<br><code>{2006: (87688 + 0) / 27695491774,<br>&nbsp;2007: (108634 + 175702) / 28307904288}</code>.
        </td>
    </tr>
</table>

For all methods, if start and end years are provided, limit the returned output to only the years in the provided range.

You can assume all data is between the years 1400 and 2100. These variables are stored as constants `MIN_YEAR` and `MAX_YEAR` in the `TimeSeries` class.

If you call a method that returns a `TimeSeries`, and there is no available data for the given method call, you should return an empty `TimeSeries`.
- Example: `ngm.weightHistory("asdfasdf")` should return a `TimeSeries` with nothing in it, since `"asdfasdf"` is not a word in the dataset.
- Example: `ngm.countHistory("adopt", 1400, 1410)` should also return a `TimeSeries` with nothing in it, since `"adopt"` has no data during those years.

{: .TASK}
> Implement the methods in `src/main/NGramMap.java` according to the API provided in the file.
>
> See `testOnLargeFile()` in `src/tests/NGramMapTest.java` for an example of how to use a `NGramMap`.

NGramMap should not extend any class.

You may not add additional public methods to this class. You're welcome to add additional private methods.

Tips:
- Your methods should be simple! If you pick the right data structures, the methods should be relatively short.
- Like in TimeSeries, you should *not* have any code which fills in a zero if a value is unavailable.
- Your code should be fast enough that you can create an `NGramMap` using `word_history_size14377.csv`. Loading should take less than 60 seconds (maybe a bit longer on an older computer).
- The provided tests are already mostly comprehensive. If you'd like to write additional tests, see the [Testing](/proj2/proj2-testing/#ngrammap) spec for more information.

## Task 3: HistoryTextHandler

In tasks 3 and 4 of Project 2A, we'll do a bit of software engineering to set up a web server that can handle NgordnetQueries. While this content isn't strictly related to data structures, it is incredibly important to be able to take projects and deploy them for real world use.

Note: You should only begin this part when you are fairly confident that `TimeSeries` and `NGramMap` are working properly.

1.  In your web browser, open up the `ngordnet_2a.html` file in the `static` folder. You can do this from your finder menu in your operating system, or by right-clicking on the `ngordnet_2a.html` in IntelliJ, clicking "Open in", then "Browser". You can use whatever browser you want, though TAs will be most familiar with Chrome. You'll see a web browser based interface that will ultimately (when you're done with the project) allow a user to enter a list of words and display a visualization.

2.  Try entering "cat, dog" into the "words" box, then click `History (Text)`. You'll see that nothing useful shows up.

    Optional: If you open the developer tools in your web browser (see Google for how to do this), you'll see an error that looks like either "CONNECTION_REFUSED" or "INVALID_URL". The problem is that the Javascript tries to access a server to generate the results, but there is no web server running that can handle the request to see the history of cat and dog.

3.  Open the `main.Main` class. This class's `main` method first creates a `NgordnetServer` object. The API for this class is as follows: First, we call `startUp` on the `NgordnetServer` object, then we "register" one or more `NgordnetQueryHandler` using the `register` command. The precise details here are beyond the scope of our class.

    The basic idea is that when you call `hns.register("historytext", new DummyHistoryTextHandler(ngm))`, an object of type `DummyHistoryTextHandler` is created that will handle any clicks to the `History (Text)` button.

4.  Try running the `main.Main` class. In the terminal output in IntelliJ you should see the
    line: `INFO org.eclipse.jetty.server.Server - Started...`, which means the server started correctly.

    Now open the `ngordnet_2a.html` file again (or visit <http://localhost:4567/ngordnet_2a.html>). Enter "cat, dog" again, then click `History (Text)`. This time, you should see a
    message that says:

    ```
    You entered the following info into the browser:
    Words: [cat, dog]
    Start Year: 2000
    End Year: 2020
    ```

5.  Now open `main.DummyHistoryTextHandler`, you'll see a `handle` method. This is called whenever the user clicks the `History (Text)` button. The expected behavior should instead be that when the user clicks `History (Text)` for the prompt above (when using the larger words file `word_history_size14377.csv`), the following text should be displayed:

    ```
    cat: {2000=1.71568475416827E-5, 2001=1.6120939684412677E-5, 2002=1.61742010630623E-5, 2003=1.703155141714967E-5, 2004=1.7418408946715716E-5, 2005=1.8042211615010028E-5, 2006=1.8126126955841936E-5, 2007=1.9411504094739293E-5, 2008=1.9999492186117545E-5, 2009=2.1599428349729816E-5, 2010=2.1712564894218663E-5, 2011=2.4857238078766228E-5, 2012=2.4198586699546612E-5, 2013=2.3131865569578688E-5, 2014=2.5344693375481996E-5, 2015=2.5237182007765998E-5, 2016=2.3157514119191215E-5, 2017=2.482102172595473E-5, 2018=2.3556758130732888E-5, 2019=2.4581322086049953E-5}
    dog: {2000=3.127517699525712E-5, 2001=2.99511426723737E-5, 2002=3.0283458650225453E-5, 2003=3.1470761877596034E-5, 2004=3.2890514515432536E-5, 2005=3.753038415155302E-5, 2006=3.74430614362125E-5, 2007=3.987077208249744E-5, 2008=4.267197824115907E-5, 2009=4.81026086549733E-5, 2010=5.30567576173992E-5, 2011=6.048536820577008E-5, 2012=5.179787485962082E-5, 2013=5.0225599367200654E-5, 2014=5.5575537540090384E-5, 2015=5.44261096781696E-5, 2016=4.805214145459557E-5, 2017=5.4171157785607686E-5, 2018=5.206751570646653E-5, 2019=5.5807040409297486E-5}
    ```

    To pass on the autograder, the formatting of the output must match exactly.

    All lines of text, including the last line, should end in a new line character.

    All whitespace and punctuation (commas, braces, colons) should follow the example above.

These numbers represent the *weighted popularity histories* of the words cat and dog in the given years. Due to rounding errors, your numbers may not be exactly the same as shown above.

Your format should be exactly as shown above, specifically:
- The word...
- ...followed by a colon...
- ...followed by a space...
- ...followed by a string representation of the appropriate `TimeSeries` where key-value pairs are given as a comma-separated list inside curly braces, with an equals sign between the key and values. Note that you don't need to write any code to generate the string representation of each `TimeSeries`, you can just use the `toString()` method.

Now it's time to implement the HistoryText button!

{: .TASK}
> In the `main` folder, create a new file called `HistoryTextHandler.java` that takes the given `NgordnetQuery` and returns a String in the same format as above.
>
> Then, modify `Main.java` so that your `HistoryTextHandler` is used when someone clicks `History (Text)`. In other words, instead of registering `DummyHistoryTextHandler`, you should register your `HistoryTextHandler` class instead.

Tips:
- Use the `DummyHistoryTextHandler.java` as a guide, pattern matching where appropriate. Being able to tinker with example code and bend it to your will is an incredibly important real world skill. Experiment away, don't be afraid to break something!
- For Project 2A, you can ignore the `k` instance variable of `NgordnetQuery`.
- Use the `.toString()` method built into the `TimeSeries` class that gets inherited from `TreeMap`.
- For your `HistoryTextHandler` to be able to do something useful, it's going to need to be able to access the data stored in your `NGramMap`. **Do not make the NGramMap into a static variable!** This is known as a "global variable" and is rarely the appropriate solution for any problem. Hint: Your `HistoryTextHandler` class can have a constructor like this: `public HistoryTextHandler(NGramMap map)`.
- If a word is invalid, think about how `NGramMap` is handling this situation.
- The provided test is already mostly comprehensive. If you'd like to write additional tests, see the [Testing](/proj2/proj2-testing/#historytexthandler) spec for more information.


## Task 4: HistoryHandler

The text-based history from the previous section is not useful for much other than auto-grading your work. Actually using our tool to discover interesting things will require visualization.

`src/demo/PlotDemo.java` provides example code that uses your `NGramMap` to generate a visual plot showing the weighted popularity history of the words cat and dog between 1900 and 1950. Try running it. If your `NGramMap` class is correct, you should see a very long string printed to your console that might look something like:

    iVBORw0KGg...

This string is a base 64 encoding of an image file. To visualize it, go to [codebeautify.org](https://codebeautify.org/base64-to-image-converter). Copy and paste this entire string into the website, and you should see a plot similar to the one shown below:

![decoded base 64](/assets/projects/proj2a/1-default-base-64.webp)

What's going on here? The string your code printed IS THE IMAGE. Keep in mind that any data can be represented as a string of bits. This website knows how to decode this string into the corresponding image, using a predefined standard.

If you look at the plotting library, this code relies on the `Plotter.generateTimeSeriesChart` method, which takes two arguments. The first is a list of strings, and the second is a `List<TimeSeries>`. The `TimeSeries` are all plotted in a different color, and each is assigned the label given in the list of strings. Both lists must be of the same length (since the ith string is the label for the ith time series).

The `Plotter.generateTimeSeriesChart` method returns an object of type `XYChart`. This object can in turn either be converted into base-64 by the `Plotter.encodeChartAsString` method, or can be displayed to the screen directly by `Plotter.displayChart`.

Run `Main.java` again, and in your web browser, open up `ngordnet_2a.html` (or visit <http://localhost:4567/ngordnet_2a.html>). Enter "cat, dog" into the "words" box, then click "History". You'll see the strange image below:

![parabola and sinusoid](/assets/projects/proj2a/2-default-history-plot.webp)

You'll note that the code is not plotting the history of cat and dog, but rather a parabola and a sinusoid. If you open `DummyHistoryHandler`, you'll see why.

{: .TASK}
> In the `main` folder, create a new file called `HistoryHandler.java` that takes the given `NgordnetQuery` and returns a String that contains a base-64 encoded image of the appropriate plot.
>
> Then, modify the `Main.java` so that your `HistoryHandler` is called when someone clicks the `History` button.

Tips:
- The constructor for `HistoryHandler` should be of the following form: `public HistoryHandler(NGramMap map)`.
- Just like before, use `DummyHistoryHandler.java` as a guide. As mentioned in the previous section, we really want you to learn the skill of tinkering with complex library code to get the behavior you want.


## Submission

Try submitting to the autograder. You may or may not pass everything.

- If you fail a correctness test, this means that there is a case that your local tests did not cover.
- The autograder will not run unless you fix all your style errors. Reminder that you can check style in IntelliJ as often as you'd like:
  ![Run style checker in IntelliJ](/assets/resources/style-guide-img/intellij_style_checker.webp)
- You will have a token limit of 8 tokens every 24 hours. We will not reinstate tokens for failing to add/commit/push your code, run style, etc.

Project 2A will be worth 13 points.

Grading breakdown:
- **TimeSeries (30%)**: Correctly implement `TimeSeries.java`.
- **NGramMap Count (20%)**: Correctly implement `countHistory()` and `totalCountHistory()` in `NGramMap.java`.
- **NGramMap Weight (30%)**: Correctly implement `weightHistory()` and `summedWeightHistory()` in `NGramMap.java`.
- **HistoryTextHandler (10%)**: Correctly implement `HistoryTextHandler.java`.
- **HistoryHandler (10%)**: Correctly implement `HistoryHandler.java`.

The score you receive on Gradescope is your final score for this assignment (assuming you followed the [collaboration policy](/policies/#collaboration-policy)).

{: .ACKNOWLEDGMENT}
> The WordNet part of this assignment is loosely adapted from Alina Ene and Kevin Wayne's
> [Wordnet assignment](http://www.cs.princeton.edu/courses/archive/fall14/cos226/assignments/wordnet.html) at Princeton
> University.
