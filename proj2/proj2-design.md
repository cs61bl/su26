---
layout: page
title: "Design"
parent: Project 2
nav_order: 3
toc_max_heading: 3 # hide h4 headings from table of contents
---

## Spec Update

{% capture update %}{% include proj2-update.html %}{% endcapture %}
{{ update | markdownify }}

## Note on Grading

{: .IMPORTANT}
> For {{ site.semester_full }}, **we are NOT grading these assignments as they are considered optional**. However, if you'd
> like feedback on your design doc, feel free to ask in lab.

# Design

In these optional tasks, you'll design your approach to Wordnet, the rest of the Ngordnet tool.

## Task 0: Wordnet Spec

{: .TASK}
> Before getting started, please read the [Project 2B: Wordnet](/proj2/proj2b/) spec. You won't be able to begin this 
> task without understanding the Wordnet spec first!

## Task 1: Checkpoint

[Project 2B: Wordnet Checkpoint](https://www.gradescope.com/courses/1318601/assignments/8287569/) is a conceptual
assignment testing your understanding of Wordnet. We recommend completing this before designing your project.

{: .TASK}
> Complete the [Project 2B: Wordnet Checkpoint](https://www.gradescope.com/courses/1318601/assignments/8287569/). You
> have unlimited submissions until the deadline and explanations will be shown upon entering the correct answers. You
> may not extend the checkpoint$^*$, as this is intended to help you get started on the rest of the project.
>
> $^*$_Students with DSP accommodations may extend the checkpoint_

## Task 2: Technical Design Doc

[Project 2B: Wordnet Design](https://www.gradescope.com/courses/1318601/assignments/8308497/) is a design assignment for you to plan your approach for Wordnet before implementing
it.

For your design document, you must include each of these components from the rubric below. An introduction to design
documents and examples can be found in the [Design Doc Guide](/resources/design-doc-guide).

1. **Data (20%)**: Describes how the data will be used.
2. **Data Structures (20%)**: Describes what data structures will be used with the data.
3. **Algorithms (20%)**: Describes what algorithms will be used with the data structures and data.
4. **Complexity (20%)**: Describes the expected time and space complexity of the program.
5. **Diagram (20%)**: Describes how the data, data structures, and algorithms work together. Must be a visual
   representation.

We’ll grade your design document on completion and effort, not correctness. The correctness of your final design is
checked by running the autograder on your code. We will grade your design document by the end of the week of the
deadline.

Your design document must be readable and typed aside from your diagram. Please include your diagram as a separate page
upon submission. If your diagram doesn't fit on one page, you may submit it as multiple pages. You may be deducted a
format point penalty if you do not follow these instructions.

If you do not submit your design doc by the original deadline, we cannot guarantee that we'll have it graded by the end
of the week.

If you intend to work on this project during office hours, we may ask to see your design document to help understand
your approach. As such, please put effort into this assignment! Grasping project requirements in the design phase will
help immensely during the later implementation phases.

{: .TASK}
> Write a design document for Wordnet and submit it to the
> [Project 2B: Wordnet Design](https://www.gradescope.com/courses/1318601/assignments/8308497/) assignment.

### Design Tips

We've included below a few questions for you to consider while brainstorming your design:

#### General Questions

- Poke around the `/browser` and `/main` folders and observe what code exists. How do the examples in the `/demo` folder use existing classes/methods?
- How are a user's inputs (i.e. hyponyms of "cat", k > 0) communicated to us from the ngordnet website? How do we communicate results back to the website?
    - *You aren't expected to know how the website works. However, it's important to understand the boundaries of your implementation.*
- Where do tasks overlap? Are there opportunities to reuse methods across different cases? Think about helper methods or opportunities to overload methods.
- Can you find groups of data structures and methods that serve a similar, clearly defined purpose? If so, consider moving them to a separate class. Building abstraction barriers may be helpful for managing code complexity.

#### Considering Edge Cases

- How will your implementation handle words that exist within multiple hyponyms?
- What output do we expect when a list of words are inputted? Under what circumstances is a synset a hyponym of two words? What about multiple words? How will your implementation determine the correct output?
- What output do we expect when the user provides a k > 0? Does this relate to anything we've already built?

### Template

We have provided a template for you to use if you'd like. See the [Project 2B: Wordnet Design Template](https://docs.google.com/document/d/1CweFh2omEOZRndvjxq2KuNNa2Dpg6p876DasdZWr1x4/edit?usp=sharing), which is
also linked in the assignment below.

Alternatively, you can diagram your entire design. If you choose to do this, make sure you include all components in
the rubric.

## Submission

Once you have submitted to both assignments below, you're done!

1. [Project 2B: Wordnet Checkpoint](https://www.gradescope.com/courses/1318601/assignments/8287569/) (10 points)
2. [Project 2B: Wordnet Design](https://www.gradescope.com/courses/1318601/assignments/8308497/) (15 points)

The score you receive on Gradescope is your final score for this assignment (assuming you followed the [collaboration policy](/policies/#collaboration-policy)).

{: .ACKNOWLEDGMENT}
> This spec was written by Daniel Wang and Ronnie Beggs as a new assignment in Fall 2025. The provided template was
> created by Kanav Mittal and Stella Kaval in Spring 2025 and edited by Daniel Wang.
