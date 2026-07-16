---
layout: page
title: "Data"
parent: Project 2
nav_order: 3
---

## Spec Update

{% capture update %}{% include proj2-update.html %}{% endcapture %}
{{ update | markdownify }}

# Project 2: Data

## NGrams

In [Project 2A](/proj2/proj2a/), you'll be working with NGrams data consisting of word history files and a year history file.

{: .TASK}
> Download [`cs61b_{{ site.semester_slug }}_ngrams_data.zip`](https://drive.google.com/file/d/1uy-Lz0i5DRXvetPcLOIlSdak1g8BBZVm/view?usp=sharing).
> - [How to unzip folders on Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc#:~:text=To%20unzip%20files,folder%20to%20a%20new%20location.)
> - [How to unzip folders on Mac](<https://support.apple.com/guide/mac-help/zip-and-unzip-files-and-folders-on-mac-mchlp2528/mac#:~:text=Unzip%20(expand)%20a%20compressed%20item,zip%20file.>)
>
> Move the `data` folder underneath `proj2a` such that it is on the same level as `src` and `tests`.
>
> ```sh
> proj2a
> ├── data
> ├── src
> ├── static
> ├── tests
> ```
>
> See the [video](https://www.youtube.com/watch?v=8uIt7pXua6Y) below for an overview of the setup process. As this was made with an older version of the project, some of the filenames have been changed since then.
> <iframe width="560" height="315" src="https://www.youtube.com/embed/8uIt7pXua6Y?si=wd35tOl_CZlRsMGs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


{: .CAUTION}
> Do not commit your `data` folder to GitHub!
>
> The [`.gitignore`](https://help.github.com/articles/ignoring-files/) file should prevent you from calling `git add` on it. You can check this by running the following command from your `{{ site.semester_slug }}-s***` repository and verifying if the lines below are included in it:
>
> ```sh
> $ cat .gitignore
> ...
> proj2*/data/
> proj2*/*.zip
> proj2*/*.txt
> ...
> ```
>
> If you commit it, please see the [Large Files Detected](/troubleshooting/git-wtfs/#large-files-detected) section in Git WTFS to fix it.

### Word History File

The NGram dataset comes in two different file types. The first type is a "word history file". Each line of a word history file provides tab separated information about the history of a particular word in English during a given year.

```
word_history_size3.csv:
-----------------------------
airport     2007    175702  32788
airport     2008    173294  31271
request     2005    646179  81592
request     2006    677820  86967
request     2007    697645  92342
request     2008    795265  125775
wandered    2005    83769   32682
wandered    2006    87688   34647
wandered    2007    108634  40101
wandered    2008    171015  64395
```

On each row:
1. The first column is the word.
2. The second column is the year.
3. The third column is the number of times that the word appeared in any book that year.
4. You can ignore the fourth column. (If you're curious, it is the number of distinct sources that contain that word.)

For example, from the text file above, we can observe that the word "wandered" appeared 171,015 times during the year 2008, and these appearances were spread across 64,395 distinct texts.

### Year History File

The other type of file is a "year history file". Each line of a year history file provides comma separated information about the total corpus of data available for each calendar year.

```
year_history.csv:
-----------------------------
1470,984,10,1
1472,117652,902,2
1475,328918,1162,1
1476,20502,186,2
1477,376341,2479,2
...
```

On each row:
1. The first column is the year.
2. The second column is the total number of words recorded from all texts that year.
3. You can ignore the third column. (If you're curious, it is the total number of pages of text from that year.)
4. You can ignore the fourth column. (If you're curious, it is the total number of distinct sources from that year.)

For example, we see that Google has exactly 1 English language text from the year 1470, and that it contains 984 words and 10 pages. For our project, the 10 and the 1 are irrelevant.

You may wonder why one file is tab separated and the other is comma separated. I didn't do it, Google did. Luckily, this difference won't be too hard to handle.

{: .TASK}
Return to begin [Project 2A Task 1: TimeSeries](/proj2/proj2a/#task-1-timeseries).

---

## Wordnet

In [Project 2B](/proj2/proj2b/), you'll be working with Wordnet data consisting of synset and hyponym files.

{: .TASK}
> Download [`cs61b_{{ site.semester_slug }}_wordnet_data.zip`](https://drive.google.com/file/d/1q3uxwWs0bahk5QQBPwQvtaUBE2MgmdFE/view?usp=sharing).
> - [How to unzip folders on Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc#:~:text=To%20unzip%20files,folder%20to%20a%20new%20location.)
> - [How to unzip folders on Mac](<https://support.apple.com/guide/mac-help/zip-and-unzip-files-and-folders-on-mac-mchlp2528/mac#:~:text=Unzip%20(expand)%20a%20compressed%20item,zip%20file.>)
>
> Move the `data` folder underneath `proj4cd` such that it is on the same level as `src` and `tests`.
>
> ```sh
> proj2b
> ├── data
> ├── src
> ├── static
> ├── tests
> ```

{: .NOTE}
> This dataset contains the same word history and year history files from the NGrams dataset which you'll need to
> complete [Project 2B Task 6: Nonzero k](/proj2/proj2b/#task-6-nonzero-k) as well as [optional bonus features](/proj2/proj2-bonus-features/).

{: .CAUTION}
> As a reminder, do not commit your `data` folder to GitHub!
>
> The [`.gitignore`](https://help.github.com/articles/ignoring-files/) file should prevent you from calling `git add` on it. You can check this by running the following command from your `{{ site.semester_slug }}-s***` repository and verifying if the lines below are included in it:
>
> ```sh
> $ cat .gitignore
> ...
> proj2*/data/
> proj2*/*.zip
> proj2*/*.txt
> ...
> ```
>
> If you commit it, please see the [Large Files Detected](/troubleshooting/git-wtfs/#large-files-detected) section in Git WTFS to fix it.

### Wordnet Dataset

Before we can incorporate WordNet into our project, we first need to understand the WordNet dataset.

[WordNet](http://en.wikipedia.org/wiki/WordNet) is a "semantic lexicon for the English language" that is used
extensively by computational linguists and cognitive scientists; for example, it was a key component in IBM's Watson. WordNet groups words into sets of synonyms called synsets and describes semantic relationships between them.

One such relationship is the is-a relationship, which connects a **hypo**nym (more specific synset) to a **hyper**nym (more general synset). For example, "change" is a **hypernym** of "demotion", since "demotion" is-a (type of) "change". "change" is in turn a **hyponym** of "action", since "change" is-a (type of) "action". A visual depiction of some hyponym relationships in English is given below:

![WordNet]({{ "/assets/projects/proj4c/1-wordnet-fig.webp" | relative_url }} "WordNet")

Each node in the graph above is a **synset**. Synsets consist of one or more words in English that all have the same meaning. For example, one synset
is "jump, parachuting", which represents the act of descending to the ground with a parachute. "jump, parachuting" is a hyponym of "descent", since "jump, parachuting" is-a "descent".

Words in English may belong to multiple synsets. This is just another way of saying words may have multiple meanings. For example, the word "jump" also belongs to the synset "jump, leap", which represents the more figurative notion of jumping (e.g. a jump in attendance) rather the literal meaning of jump from the other synset (e.g. a jump over a puddle). The synset "jump, leap" is a hyponym of "increase", since "jump, leap" is-an "increase". Of course, there are other ways to "increase" something: for example, we can increase something through "augmentation," and thus it is no surprise that we have an arrow pointing downwards from "increase" to "augmentation" in the diagram above.

Synsets may include not just words, but also what are known as [collocations](http://en.wikipedia.org/wiki/Collocation). These are multi-word phrases that are represented as a **single word** due to how common they are together, e.g "nasal_decongestant".

A synset may be a hyponym of multiple synsets. For example, "actifed" is a hyponym of both "antihistamine" and "nasal_decongestant", since "actifed" is both of these things.

Here is a list of all of the data files for synsets/hyponyms for this project and a quick explanation on what they will do.

`synsets/hyponyms_size 82191`

- The full data set from the NGrams data set!

`synsets/hyponyms_eecs`

- Is a graph containing the names of various courses in ee/cs with two words ("bee" and "bean") added in for testing.

`synsets/hyponyms_size 11,14,16`

- Example graphs used from the spec.

`synsets/hyponyms_size 10,25,1000`

- Subsets of the full data set used for autograder testing.

The autograder will only use synsets/hyponyms_size 10,25,1000,82191 and synsets/hyponyms_eecs for testing - the other files are just for your understanding!

### Synset File

We now describe the two types of data files that store the WordNet dataset. These files are in comma separated format, meaning that each line contains a sequence of fields, separated by commas.

The first type of file is a "synset file". Each line of a synset file provides comma separated information about a synset. The file `synsets_size82191.txt` (and other smaller files with `synset` in the name) lists all the synsets in WordNet. The first field is the synset id (an integer), the second field is the synonym set (or synset), and the third field is its dictionary definition. For example, the line

       6829,Goofy,a cartoon character created by Walt Disney

means that the synset `{ Goofy }` has an id number of 6829, and its definition is "a cartoon character created by Walt Disney". The individual nouns that comprise a synset are separated by spaces (and a synset element is not permitted to contain a space). The id numbers are useful because they also appear in the hyponym files, described described below.

### Hyponym File

The other type of file is a "hyponym file". Each line of a hypoynm file provides comma separated information about a hyponym. The file `hyponyms_size82191.txt` (and other smaller files with hyponym in the name) contains the hyponym relationships. The first field is a synset id, and subsequent fields are the id numbers of the synset's direct
hyponyms. For example, the following line

      79537,38611,9007

means that the synset 79537 ("viceroy vicereine") has two hyponyms: 38611 ("exarch") and 9007 ("Khedive"),
representing that exarchs and Khedives are both types of viceroys (or vicereine). The synsets are obtained from the corresponding lines in the file `synsets.txt`:

      79537,viceroy vicereine,governor of a country or province who rules...
      38611,exarch,a viceroy who governed a large province in the Roman Empire
      9007,Khedive,one of the Turkish viceroys who ruled Egypt between...

There may be more than one line that starts with the same synset ID. For example, in `hyponyms_size16.txt`, we have

      11,12
      11,13

This indicates that both synsets 12 and 13 are direct hyponyms of synset 11. These two could also have been combined on to one line, i.e. the line below would have the exact same meaning, namely that synsets 12 and 13 are direct hyponyms of synset 11.

      11,12,13

You might ask why there are two ways of specifying the same thing. Real world data is often messy, and we have to deal with it.

{: .TASK}
Return to begin [Project 2B Task 1: Dummy HyponymsHandler](/proj2/proj2b/#task-1-dummy-hyponymshandler) and optionally the [Project 2B Checkpoint](/proj2/proj2b/#optional-task-checkpoint).