---
layout: page
title: "Project 3A: BYOW (World Generation)"
parent: Project 3
nav_order: 0
toc_max_heading: 2 # hide h3 headings from table of contents
---

## Deadlines

{% capture deadlines %}{% include proj3-deadlines.html %}{% endcapture %}
{{ deadlines | markdownify }}

# Project 3A: BYOW (World Generation)

## Welcome and Overview

In this project, you will create an engine for generating explorable worlds. This is a large design project that will require you and one partner to work through every stage of development from ideation to presentation.

{: .NOTE}
In accordance with this, the grading of this project will be different from other projects. Since there is no notion of "the correct answer" when it comes to world design and implementation, you will be assessed much like a performance review you might receive at an internship or job. While this means you will be graded slightly subjectively, we promise to be pretty nice bosses and will respect you as any boss should respect their hardworking employees. You will have the opportunity to dispute if the grading scheme feels unfair.

**This project is about software engineering**, and will achieve several goals that come with large design projects

1. Emulating a real product development cycle. This comes from handling a larger pieces of code with little starter code
2. Recognize and mitigate code complexity. Inevitably, whenever a team builds a large software system, they'll make some bad design decisions and cut corners, resulting in "technical debt". Your code becomes complicated to understand and modify, which in the real world translates to software that becomes stale and expensive to maintain. It is *very likely* that your code will feel sort of hacked together by the end of this project. As you grow as a programmer over the course of your career, arguably the main skill you'll be building is to avoid such hacks. However, the only way to know and defeat this is to suffer from it.
3. Exploring and experimenting with resources. Know that there are no right and wrong answers, as this is a very open-ended project. In fact, it is not required to use any of the data structures from class, but it will likely make your solution significantly simpler and more efficient. You will likely go through several iterations before settling on your final implementation


[A video playlist (from Spring 2018) discussing tips for working on this project can be found at this link](https://www.youtube.com/playlist?list=PL8FaHk7qbOD6REWjsJd5jz9fpXO5_3ebY&disable_polymer=true) Note: The tour through the skeleton code is a bit out of date, for example, the `playWithKeyboard` and `playWithInputString` methods are gone.

Your task for the next few weeks is to design and implement a 2D tile-based world exploration engine. As an example of a much more sophisticated system than you will build, the NES game "Zelda II" is (sometimes) a tile based world exploration engine that happens to be a video game:

<img alt="Screenshot of Zelda II." src="/assets/projects/proj3a/1-zelda.webp">

The system you build can either use graphical tiles (as shown above), or it can use text based tiles, like the game shown below:

<img alt="Screenshot of Brogue." src="/assets/projects/proj3a/2-brogue.webp">

We will provide a tile renderer and a small set of starter tiles for you to use. This will be the same tile renderer you used in Project 0 and 3.

### Project Roadmap

1. Implement code to generate random worlds (Project 3A).
2. Add a main menu for the user to start the game from (Project 3B).
3. Add support for saving a game and loading it back (Project 3B).
4. Add several game mechanics/features to your project (Project 3B).

### Large Language Model (LLM) Policy

Recall that in the collaboration policy, we say:

{: .danger}
> **DANGER: LLMs are Prohibited from Accessing or Interacting with Code and Repositories**
>
> You must **never** allow an LLM or any GenAI tool to read, analyze, or interface with your codebase or your GitHub repository in any way. This means all local and terminal-based tools (such as **Claude Code**), GitHub Copilot, built-in IDE extensions (e.g., Cursor, IntelliJ AI Assistant), or any other agentic coding tools are **outright banned**.
>
> You may **ONLY** interact with LLMs and GenAI tools conceptually, and this interaction must take place **exclusively through browser-based chatbots** (such as chatgpt.com or claude.ai).

## Task 0: Partnerships

{: .TASK}
> Follow the instructions in the [Partnerships](/proj3/proj3-partnerships) spec by the deadline for partnerships.

## Task 1: Setup

The setup for this project is different from all other assignments so far. **Read this carefully and do not skip any steps!**

{: .TASK}
Follow the instructions below after partnerships have been released to use your group repo. Make sure to provide a screenshot of your group repository to submit to gradescope to show that you have accepted the invite.

{: .WARNING}
> You need to accept your Github repo invite **within a week** of it being sent, or else it will expire, and you will not be able to work on the project.

1. Go to your email associated with your Github account and accept the Github repo invite.

    <img alt="Github repo invite email." src="/assets/projects/proj3a/3-github-invite.webp">

2. Screenshot your github repo like below, showing that you have accepted the invite. Here is an example

   <img alt="Github repo proof" src="/assets/projects/proj3a/9-repo.webp">

3. Log in to Beacon, and click on the "Groups" tab. You should have a group listed here.

4. Click the "View Repository on GitHub" link.

5. Click "Code" -> "SSH" and copy the link that appears. It should look like this, with `***` replaced with some group number:

   `git@github.com:Berkeley-CS61B-Student/{{ site.semester_slug }}-proj3-g***.git`

    <img alt="Copy SSH link." src="/assets/projects/proj3a/4-ssh-copy.webp">

6. Open a new terminal window in your local computer.

7. Use `cd` to navigate to your desired location your project. Most students have a folder called `cs61b`.

   {: .WARNING}
   Do not navigate to your personal `{{ site.semester_slug }}-s***` repo! You should not be cloning your group repo inside your personal one.

   [//]: # <img alt="pwd should not display your personal repo." src="/assets/projects/proj3a/5-pwd.webp">

8. In your terminal, clone your repo, replacing the URL with the one you copied earlier:

   `git clone git@github.com:Berkeley-CS61B-Student/{{ site.semester_slug }}-proj3-g***.git`

9. Navigate into the repo you just cloned:

   `cd {{ site.semester_slug }}-proj3-g***`


Once you’ve completed the above steps, you should see your new group repo called `{{ site.semester_slug }}-proj3-g***` in your local files, and if you open this repo, you’ll see the `proj3` skeleton folder. From here, you and your partner can proceed as normal, by adding, committing, pushing, and pulling from this repo as you would otherwise.

## Optional Task: Design

{: .TASK}
> [Project 3: BYOW Design](/proj3/proj3-design) is a design assignment for you to plan your approach for BYOW before implementing it. Although this is optional, we highly recommend attempting this to ensure you have a plan before building your own world.
> 
> To further incentivize you to do this, completing this assignment with effort by the Project 3A: BYOW deadline will grant you TODO recovery points for the checkoff. In other words, if you lose points on the checkoff, these recovery points can be used to gain back points.

### Code Overview

### Skeleton Code

{: .NOTE}
> [A walkthrough of the skeleton code and demos is available here.](https://youtu.be/2VMoC4eMj7Y) 
> 
> We also highly recommend watching [Lecture 31](https://youtu.be/BRsuHSQ800U) before beginning this project.

In the `TileEngine` package, you'll find the following useful files:

- `TERenderer.java` contains rendering-related methods.
- `TETile.java` represents a tile.
- `Tileset.java` has some pre-made tile designs that you can use.

In the `Utils` package, you'll find the following useful file:

- `RandomUtils.java` has methods for generating randomness for your world.

In the `Core` package, you'll write code for your game. We recommend putting all your code in this package (though this is not required).

- `Main.java` is how your user starts the entire system.
- `World.java` represents your world!
- You can add other classes of your own, too!


This project makes heavy use of `StdDraw`, which is a package that has basic graphics rendering capabilities. Additionally, it supports user interaction with keyboard and mouse clicks. You will likely need to consult the API specification for `StdDraw` at some points in the project. [See here for the API specification.](https://introcs.cs.princeton.edu/java/stdlib/javadoc/StdDraw.html)


### Imports

Your project should only use standard Java libraries or any libraries we provided with your repo and `library-{{ site.semester_slug }}`.

Here is a non-comprehensive list of allowed imports:

- `java.util.List`, `java.util.ArrayList`, `java.util.Collections`, `java.awt.*`, `java.io.*`, or anything else starting with `java.` is fine.
- `javax.sound`, `javax.imageio`, `javax.swing.JOptionPane`, or anything else starting with `javax.` is fine.
- `edu.princeton.cs.algs4.StdDraw`, `edu.princeton.cs.algs4.StdAudio`, or anything else starting with `edu.princeton.cs.algs4.` is fine, because this is in `library-{{ site.semester_slug }}`.
- `tileengine.TETile`, `utils.RandomUtils`, or anything else starting with `tileengine.` or `utils.` is fine, because these are the starter code.


### Getting Started

### TETile Array

At a high level, your goal is to create a 2D array of `TETile` objects, and fill in the array with different tiles, to create a nice-looking world. Then, you can call one of our library functions to display this world to the user.

{: .TASK}
Go through the files in the tileengine folder: TETile.java, Tileset.java, and TERenderer.java. Overall, you do not need to understand these implementations deeply, but they provide useful context.

Important notes on orientation:
- `world[0][0]` corresponds to the **bottom-left** tile of the world.
- The first coordinate is the x-coordinate. For example, `world[8][0]` is 8 spaces to the right of the bottom-left tile.
- The second coordinate is the y-coordinate. For example, `world[0][3]` is 3 spaces above the bottom-left tile.

<img alt="2D grid with coordinates (0,0) at bottom-left, (8,0) at bottom-right, and (0,3) at top-right." src="/assets/projects/proj3a/coords.webp">

### Tile Rendering

Open up the skeleton and check out the `BoringWorldDemo` file in the `demo` folder. Try running
it.

This code does 3 things:

- Initializing the tile rendering engine.
- Generating a two dimensional TETile[][] array.
- Using the tile rendering engine to display the TETile[][] array.

{: .NOTE}
> For empty tiles, make sure to use `Tileset.NOTHING`, the pure black tile. If you don't initialize unused squares, you'll get a NullPointerException when you try to draw the world.
>
> The rendering engine calls most of the `StdDraw` methods for you. We recommend against using `StdDraw` commands like `setXScale` or `setYScale` unless you really know what you're doing, as you may considerably alter or damage the *a e s t h e t i c* of the system otherwise.


### Pseudo-Randomness

To generate random numbers in Java, we can use create a `Random` object, which represents a random number generator:

```java
Random r = new Random(); // Totally random. Don't do this in Project 3.
System.out.println(r.nextInt());
System.out.println(r.nextInt());
System.out.println(r.nextInt());
```

Every time you run this program, you'll get 3 totally random integers.

What if we want to control the output of the random number generator (e.g. for debugging purposes)? In that case, we can provide a **seed** to the constructor. 

`r` is now a **pseudorandom** number generator, because it generates a deterministic sequence of random-looking numbers based on the seed you provide.

If you provide the same seed, you will get the same sequence of values. For example, every time you run this program, **you will get the same 3 integers**.

Here's another example:

```java
Random r = new Random(82731);
System.out.println(r.nextInt());
System.out.println(r.nextInt());
r = new Random(82731);
System.out.println(r.nextInt());
```

This code snippet will always print out the same number twice. If you run this program multiple times, you'll still get the same number twice.

In Project 3, you should always seed your Random objects, so that your worlds look random, but you can re-create them consistently for debugging and grading purposes. The **RandomUtils** class provides some useful methods for getting other types of randomness out of a `Random` object, examples include:
 - `int uniform(Random random, int a, int b)`: Returns an integer from the range `[a, b)`
 - `T randomChoice(Random random, List<T> items)`: Returns a random item from items.
 - `void shuffle(Random random, Object[] a)`: Shuffles the given array.
 - `double gaussian(Random random, double mu, double sigma)`: Gives a sample from a Gaussian distribution.
 
Note: Most students won't use any of the fancy stuff from `RandomUtils`.

### Pseudo-Randomness with World Generation Demo/Example

{: .TASK}
Open up the skeleton and check out the `RandomWorldDemo.java` file in the `demo` folder. Try running it.

You should see something that looks like this:

![random world](/assets/projects/proj3a/randomWorld.webp)

This world is sheer chaos -- walls and flowers everywhere! If you look at the `RandomWorldDemo.java` file, you'll
see that we're doing a few new things:

- We create and use an object of type `Random` that is a "[pseudorandom number generator](https://docs.oracle.com/javase/8/docs/api/java/util/Random.html)".
- We use a new type of conditional called a `switch` [statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html).
- We have delegated work to functions instead of doing everything in `main`.

### World Requirements

Your goal in Project 3A is to write a world generator that can create pseudorandom worlds with hallways and floors.

Here are some examples of valid worlds, where `#` is wall, dot/quote is floor, and the empty square is the empty space (outside the world).

<img alt="A valid 2D world with hallways and rooms." src="/assets/projects/proj3a/valid-world.webp">

<img alt="Another valid 2D world with hallways and rooms." src="/assets/projects/proj3a/valid-world-2.webp">


### Valid

**Requirements for a valid world:**

1. The world must include distinct rooms and hallways. For any floor square, it should be obvious whether that square belongs to a room or a hallway.

    It's okay if you occasionally generate some worlds where a few squares are ambiguous, but the vast majority (>90%) of floor squares should be clearly identifiable as a room or a hallway.

    Overlapping rooms are fine, as long as it's clear that the squares belong to rooms, not hallways.

    <details>
        <summary>(click to expand) Examples of invalid worlds, because we can't tell where rooms and hallways are.</summary>

        <img alt="Invalid world where hallways and rooms are indistinguishable." src="/assets/projects/proj3a/invalid-indistinct-hallways.webp">

        <img alt="Another invalid world where hallways and rooms are indistinguishable." src="/assets/projects/proj3a/invalid-indistinct-hallways2.webp">
    </details>

2. At least some rooms should be rectangular. You can optionally support rooms of other shapes as well.

3. Hallways should be width-1 or width-2. However, hallways must be visually distinct from rooms. The vast majority of students use width-1 hallways.

    <details>
        <summary>(click to expand) Examples of hallway widths.</summary>

        <br>

        Below is a width 1 hallway (most/all hallways should look like this):

        <br>

        <img alt="Width 1 hallway." src="/assets/projects/proj3a/width1-hallway.webp">

        <br>

        Below is a width 2 hallway:

        <br>

        <img alt="Width 2 hallway." src="/assets/projects/proj3a/width2-hallway.webp">
    </details>

4. Your world generator must be capable of generating hallways that include turns (or equivalently, straight hallways that intersect). Random worlds should generate a turning hallway with high frequency, in that a majority of worlds should have a turning hallway.

5. The world should not have any dead-end hallways. Hallways should always lead into rooms.

    <details>
        <summary>(click to expand) Example of an invalid world, because it has a dead-end hallway.</summary>

        <img alt="Invalid world where there's a dead-end hallway." src="/assets/projects/proj3a/invalid-dead-end-hallway.webp">
    </details>

6. Walls, floors, and empty spaces should all be visually distinct.

    The easiest way to do this is to use three different tile types: one for walls, one for floors, and one for empty spaces.

    <details>
        <summary>(click to expand) Example of an invalid world, because we can't distinguish between walls and floors.</summary>

        <img alt="Invalid world where walls and rooms are yellow squares." src="/assets/projects/proj3a/invalid-indistinct-walls.webp">
    </details>

7. Walls in the corners of rooms and hallways are optional.

    <details>
        <summary>(click to expand) As an example, all these rooms and hallways are valid.</summary>

        <br>

        As an example, the left room has walls in the corners, but the right room does not. Either one is fine. (Note: This world itself would be invalid because the two rooms are disconnected.)

        <br>

        <img alt="Example of rooms with and without corner walls." src="/assets/projects/proj3a/room-corners.webp">

        As an example, the top-left corner of this hallway has a wall tile, but the top-right corner of this hallway does not have a wall tile. Either one is fine. (Note: This world itself would be invalid because there are no rooms.)

        <br>

        <img alt="Example of hallways with and without corner walls." src="/assets/projects/proj3a/hallway-corners.webp">
    </details>

8. All floor tiles (rooms and hallways) should be reachable from each other. Note: As part of the ambition features you may end up with worlds that are only conditionally reachable, e.g. using teleporters, locked doors, destructable walls, etc.

    In other words, it should be possible to trace a path of floor tiles between any pair of floor tiles.

9. All the space "inside" the walls should be floor tiles, and all the space "outside" the walls should be empty space tiles.

    In other words, a floor tile should only be bordered by floor tiles or wall tiles.

10. Rooms cannot clip off the edge of the world. In other words, there should be no floor tiles on the edge of the world.

    <details>
        <summary>(click to expand) Example of an invalid world, because it clips off the world.</summary>

        <img alt="Invalid world where a room clips off the world." src="/assets/projects/proj3a/invalid-clipping-world.webp">
    </details>

11. The world must not have excess unused space. There's no strict requirement, but try to consistently fill at least 50% of the world with rooms and hallways.

    <details>
        <summary>(click to expand) Example of an invalid world, because there are too few rooms.</summary>

        <img alt="Invalid world where there are only three rooms." src="/assets/projects/proj3a/invalid-insufficient-rooms.webp">
    </details>


### Pseudorandom

**Requirements for a pseudorandom world:**

1. The world must be pseudorandom.

    If the user chooses the same seed twice, the resulting world must be identical.

    If the user chooses two different seeds, the resulting worlds should be different.

2. Different worlds should different numbers of rooms and hallways.

    It's okay if your numbers always fall in a fixed range. For example, it's okay if all worlds have between 8 and 12 rooms, as long as different worlds have different numbers of rooms. 8 to 12 is just an example here; feel free to have more or fewer rooms.

3. Different worlds should have rooms and hallways in different locations.

   For example, if every world you generate has a room in the exact same place, that's not sufficiently random.

4. Different rooms should have different widths and heights.

5. Different hallways should have different lengths.

6. The world should be substantially different each time, i.e. you should *not* have the same basic layout with easily predictable features.

7. You can pick any window size you want, as long as the window size is reasonable (e.g. not something tiny like 3×3), and the entire window is visible on your computer. For example, a fixed, non-random window size is fine.


### Clarifications

**Note on grading:** We know that some of these requirements are subjective, and we'll try to be generous as long as your worlds follow the spirit of the requirements.

Staff cannot answer questions like "is my world valid" or "is my world good enough" on Ed or in office hours. In Project 3A, you'll turn in some worlds for us to grade, and if they aren't valid, we'll give you a second chance to fix any problems for full credit.

**Miscellaneous edge case FAQ:**

1. Two adjacent rooms can be separated by either one wall or two walls. Either is fine.

    Similarly, if a room and hallway are adjacent, or if two hallways are adjacent, they can be separated by either one wall or two walls. Either is fine.

    <details>
        <summary>(click to expand) Example of rooms being separated by one or two walls.</summary>

        <br>

        Note that regardless of which option you choose (one wall or two walls), the two rooms must still be connected, i.e. there must be some way to get from one room to the other. The worlds below are not valid because the rooms are not connected.

        Two rooms separated by a single wall:

        <img alt="Two rooms separated by a single wall." src="/assets/projects/proj3a/single-wall.webp">

        Two rooms separated by a double wall:

        <img alt="Two rooms separated by a double wall." src="/assets/projects/proj3a/double-wall.webp">
    </details>

2. Walls should not appear inside a room, because this makes it hard to tell which squares belong to a room and which squares belong to a hallway.

    It's okay if something like this happens occasionally, but it should not happen often.

    <details>
        <summary>(click to expand) Example of a wall inside a room.</summary>

        <br>

        This is invalid if it happens often.

        <img alt="A room with a wall inside it." src="/assets/projects/proj3a/wall-inside-room.webp">
    </details>

## Task 3: World Generation

It's time to generate some worlds!

{: .TASK}
Implement code that takes in a seed, generates a pseudo-random 2D world array, and displays that world back to the user.

For Project 3A, when the user runs the `main` method in `Main.java`, they should see a world pop up. For now, you can hard-code the seed in the `main` method (and change the code to see the output of different seeds).

Besides the `Main.main` requirement, your world generation code can live anywhere in the repo (we suggest making your own files in the `Core` package).


## Deliverables

### World Screenshots

1. [Go to this Java Visualizer link](https://cscircles.cemc.uwaterloo.ca/java_visualize/#code=import+java.util.Random%3B%0A%0Apublic+class+SeedGenerator+%7B%0A+++public+static+void+main(String%5B%5D+args)+%7B%0A++++++%0A++++++//+Replace+1270+with+your+fa25-g***+group+ID.%0A++++++Random+r+%3D+new+Random(1270)%3B%0A++++++%0A++++++System.out.println(%22Your+seeds+are%3A+%22)%3B%0A++++++%0A++++++for+(int+i+%3D+0%3B+i+%3C+5%3B+i+%2B%3D+1)+%7B%0A+++++++++System.out.println(Math.abs(r.nextLong()))%3B%0A++++++%7D%0A++++++%0A++++++%0A+++%7D%0A%7D&mode=edit) to generate 5 seeds. Remember to replace `1270` with your group ID.

2. Use your code to generate the 5 worlds corresponding to these seeds.

    You may need to add an "L" after the seed so that Java recognizes it as a long number, e.g. `6578897764558030256L`.

3. Take screenshots of each world. Your screenshots should look like the other world screenshots throughout this spec.

4. In your terminal, navigate to your group repo, and type `git show --summary`. Make sure that the latest commit you see corresponds to the code you used to generate these worlds:

    <img alt="git show output." src="/assets/projects/proj3a/git-show.webp">

5. Take a screenshot of the `git show --summary` output.

    Warning: All 5 of your worlds should be generated with the same code. You shouldn't submit 3 worlds from one algorithm, and 2 worlds from another one. We will use your commit log to check this.

6. Upload these 6 screenshots (5 world + git show) to Gradescope. You should submit **all six screenshots together for the same question** (World Screenshots).

7. Make sure that only one partner submits, and then [tags the other partner](https://guides.gradescope.com/hc/en-us/articles/21863861823373-Adding-Group-Members-to-a-Submission) on Gradescope. Each group should only have one submission.

Warning: Don't hard-code worlds in your code. Your world generation code should be able to generate pseudo-random worlds for any seed we provide, not just the 5 seeds. Again, we will use your commit log to check this.

**Grading:**

We will grade your worlds after the Project 3A deadline, but before the Project 3B deadline. It can take up to a week to grade your world (especially if you have an extension), so please be patient.

If your worlds do not receive full credit, you can submit a regrade request on Gradescope.

In your regrade request, please include:
- A screenshot of `git show --summary` with the commit of the new code you used to generate your fixed worlds.
- The 5 worlds you generated with your fixed code. Use the same seeds as you did originally.

It can take up to a week to respond to your regrade request, so please be patient.


### Style

Note: Since there are no autograders in Project 3, we will not be enforcing the 61B style guide on this project. However, we still highly recommend following the style guide, so that your code is readable by your partner!
