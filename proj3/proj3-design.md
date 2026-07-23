---
layout: page
title: "Design"
parent: Project 3
nav_order: 3
toc_max_heading: 3 # hide h4 headings from table of contents
---

## Deadlines

{% capture deadlines %}{% include proj3-deadlines.html %}{% endcapture %}
{{ deadlines | markdownify }}

## Note on Grading

{: .IMPORTANT}
> For {{ site.semester_full }}, **we are NOT grading thi assignment as it is considered optional**. However, we will
> grade it based on effort to determine whether you receive the recovery points. Make sure to submit this before the
> Project 3A: World Generation deadline in order to be eligible to receive recovery points. Additionally, if you'd
> like feedback on your design doc, feel free to ask in lab.

# Design

{: .TASK}
> Before getting started, please read the [Project 3A: World Generation](/proj3/proj3a/) and
> [Project 3B: Interactivity](/proj3/proj3b/) specs. You won't be able to begin either task without understanding the
> BYOW spec first!

## Task: Writing Your TDD

We have provided a template for you to use if you'd like. See
the [Project 3: BYOW Design Template](https://docs.google.com/document/d/1y7t34IhqdryOPT8fcTcc3YZlkkQAqT5-HIk5soSZlTQ/edit?usp=sharing),
which is
also linked in the assignment below.

{: .NOTE}
> Check the [Technical Design Document tab](/resources/design-doc) for a refresher and an example of a design document
>
> As mentioned earlier, design docs are living documents. You (the designer) might not understand the entire project
> scope while drafting, *and that's fine*. Including a section for questions can help track your thoughts for future
> iterations.
>
> A "Questions" section is useful for collaboration. Your collaborators may want to understand which assumptions you
> made or questions you had when designing.

{: .TASK}
> Write a TDD for BYOW and submit it to the
> [Project 3: BYOW Design](https://www.gradescope.com/courses/1318601/assignments/8321280/) assignment.

{: .NOTE}
> For BYOW, the complexity of your program is not as important.
>
> On the other hand, the data of your program is. What type of data do you expect to save and load?

{: .WARNING}
> If you expect to work on this project during office hours, we may ask to see your design document to help understand
> your approach. As such, please put effort into this assignment! Grasping project requirements in the design phase
> will help immensely during the later implementation phases.

### Design Tips

We've included below a few questions for you to consider while brainstorming your design:

#### General Questions

- Look through the provided code:
    - Notice what's already built for you. What may be useful for your implementation?
    - Notice what isn't. What gaps does your implementation need to fill?
- Where do tasks overlap? Are there opportunities to reuse methods across different cases? Think about opportunities for
  helper methods.
- Can you find groups of data structures and methods that serve a similar, clearly defined purpose? If so, consider
  moving them to a separate class. Building abstraction barriers may be helpful for managing code complexity.

#### World Generation

- What are the core components of each world? Does it makes sense to have a separate class for each component?
- How will you ensure that every generated world is valid?
    - Will you decide on a layout first, validate it, then build the world after?
    - Or, will you gradually generate the world, ensuring that only valid components are built as you go?
- Ultimately, each world is a 2D grid of values, each representing a Tile. What data structures would be helpful for
  tracking the state of the world on top of this grid? Representing specific aspects of your world with data structures
  may be helpful for building ambition features later.

#### Interactivity

- Read through the [StdDraw library documentation](https://introcs.cs.princeton.edu/java/stdlib/javadoc/StdDraw.html).
  This library acts as the bridge between your implementation and what is outputted on screen (e.g. the `/tileengine`
  implementation uses library methods to draw to the screen).
    - Can you find methods for drawing on the screen, not specifically for tile drawing?
    - Can you find methods for soliticiting user inputs?
- Rendering video is much like a classic film projector, in that by rapidly rendering images, we can create the illusion
  of motion. Video games are essentially the same, except that user inputs can alter what's displayed in the next
  frame. (Read about common paradigms for implementing video games and graphics
  engines [here](https://gameprogrammingpatterns.com/game-loop.html))
    - Does your implementation clearly separate the steps of collecting, processing, and displaying the result of user
      inputs?
- Consider that your computer can compute thousands of instructions each second. If your implementation has real-time
  elements (i.e. timers, slow-motion movement, NPCs moving at user-like speed, etc.), how can you adjust the speed of
  your event loop to match real-time?

#### Ambition Features

- Most importantly, **which ambition features are you most excited about building?**
- For each feature, determine *where* it fits within your current abstraction barriers:
    - Does it require fundamental changes to the process of generating and representing worlds?
    - Does it alter the process for collecting user input?
    - Does it change the process for rendering the world state?
- Do any features span multiple domains of this project? If so, consider creating separate classes to contain their
  complexity.
- How could you structure your core project implementation (world generation and interactivity) to make feature
  integration seamless?

{: .NOTE}
> **You aren't bound to the ambition features you choose to write about within your design doc**. That said, certain
> features(especially primary ones) are better aligned with certain implementation choices in the world generation and
> interactivity tasks. It's important to think about this early!

## Submission

{: .TASK}
> Submit your design document on
> gradescope: [Project 3: BYOW Design](https://www.gradescope.com/courses/1318601/assignments/8321280/) (TODO recovery
> points)
>
> Don't forget to add your partner to the submission!

The score you receive on Gradescope is your final score for this assignment (assuming you followed
the [collaboration policy](/policies/#collaboration-policy)).

TODO: While we're unable to give detailed individual feedback for each TDD, we'll aggregate common mistakes we notice and
showcase them (as well as implementation hints...) in assignment section during Week 13 (11/17-11/21). As always, come
to office hours if you want specific feedback from 61B staff!

{: .NOTE}
> A note on grading, we are looking for thoughtfulness and effort. In other words, you do not have to be correct in
> your design or your complexity analysis, but we expect you to have put in considerable time into designing your
> approach. As long as you attempt to describe your approach for the components in the rubric, you'll receive full
> credit.

For the TDD, we have provided the rubric we'll be grading submissions on below for your reference.

1. **Data (10%)**: Describes how the data will be used.
2. **Data Structures (40%)**: Describes what data structures will be used with the data.
3. **Algorithms (40%)**: Describes what algorithms will be used with the data structures and data.
4. **Complexity (10%)**: Describes the expected time and space complexity of the program.

{: .ACKNOWLEDGMENT}
This spec was written by Daniel Wang and Ronnie Beggs as a new assignment in Fall 2025. The provided template was
created by Kanav Mittal and Stella Kaval in Spring 2025 and edited by Daniel Wang.
