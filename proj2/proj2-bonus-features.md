---
layout: page
title: "Above and Beyond"
parent: Project 2
nav_order: 7
toc_max_heading: 2 # hide h3 headings from table of contents
---

## Spec Update

{% capture update %}{% include proj2-update.html %}{% endcapture %}
{{ update | markdownify }}

# Project 2: LLM Augmented Optional Tasks

<!--
### Optional: Hypohist with 0 K

If K is 0, instead of plotting the k most popular hyponyms, you should plot the total weight history of all words which
are hyponyms of the given words. For example, if the user enters "food, cake", startYear = 1900, endYear = 2020, k = 8,
then we'd see a plot of "cat" and "dog", where the cat represents the total weight of ALL hyponyms of cat, and "dog"
represents the total weight of ALL hyponyms of dog.

Note that the web front end sets k to zero if the value is missing.
-->

<!--
### Hypohist (text)

This is a bit less intresting, but you might find it interesting to return the

Lastly, modify the HTML, javascript, and Java code so that there is a new Hypohist (text) button. This button should
return a text display similar to History (text), but for the hypohists as described in the previous section.
-->

<!--
## Discovering Something Interesting

Lastly, once you've properly implemented all features of this assignment, you should use either the `history`,
`hyponyms`, or `hypohist` button to discover something interesting. When you've found something, submit your result
using this Google form (coming soon).

-->

If you're reading this, we're assuming you've already implemented the Hypohist button. For this final part of the project, we encourage you to use LLMs to try to build something even bigger.

{: .IMPORTANT}
**Do not use LLM generated code for any portion of 2B**. LLM generated code is only allowed for your own chosen "above and beyond" features!**

Some possibilities:

- Adding additional buttons that use one or both datasets in some creative way. For example, you might plot the average
  length of all words in a given year. Or you might create a visualization of all of a words' hyponyms. Or you might
  have a feature that prints the shortest path between two words.
- The hyponyms search finds all hyponyms, no matter how distant from the source. For example, there are a huge number of
  hyponyms of "dog". Add a new field d to the front end, which finds only words that are at a distance of d or less from the given words.
- Add a ! operator, e.g. if someone enters "!person, leader", your code will find all leaders which are not a person.
- Explore statistical properties of the dataset, for example by plotting counts (on the y-axis) vs. ranks (on the x-axis), you should be able to see Zipf's law in action.

If you discover or build something cool, email Josh (hug@cs.berkeley.edu) and say that you're a CS 61BL student taking the class in {{ site.semester_full }}.
