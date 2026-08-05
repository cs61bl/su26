---
layout: page
title: "Testing"
parent: Project 2
nav_order: 5
---

## Spec Update

{% capture update %}{% include proj2-update.html %}{% endcapture %}
{{ update | markdownify }}

# Project 2: Testing

For the entirety of Project 2, we will not be checking your test coverage. Rather, you should be writing tests to save you time when you run into issues down the road!

## Project 2A: NGrams

### TimeSeries

We suggest writing your unit tests in the following order:
1. `years()`
2. `data()`
3. `TimeSeries(TimeSeries ts, int startYear, int endYear)`
4. `plus()`
5. `dividedBy()`

{: .NOTE}
For out of scope reasons, you do not have to test for thrown Exceptions.

You'll notice in `testFromSpec()` that we did not directly compare `expectedTotal` with `totalPopulation.data()`. This is because doubles are prone to rounding errors, especially after division operations (for reasons that you will learn in 61C). Thus, `assertThat(x).isEqualTo(y)` may unexpectedly return false when `x` and `y` are doubles. Instead, you should use `assertThat(x).isWithin(1E-10).of(y)`, which returns true as long as `x` and `y` are within $10^{-10}$ of each other.

### NGramMap

We suggest writing your unit tests in the following order:
1. `countHistory(String word)`
2. `countHistory(String word, int startYear, int endYear)`
3. `NGramMap(String wordsFilename, String countsFilename)`
4. `totalCountHistory()`
5. `weightHistory(String word, int startYear, int endYear)`
6. `weightHistory(String word)`
7. `summedWeightHistory(List words)`

{: .NOTE}
> For out of scope reasons, you do not have to test for execution time.

Rather than using one of the large input files (e.g. `word_history_size14377.csv`), we recommend starting with one of the smaller input files (e.g. `word_history_size3.csv`, `word_history_size4.csv`).

### HistoryTextHandler

We suggest writing the following unit tests:
1. `handle(NgordnetQuery query)` basic case
2. `handle(NgordnetQuery query)` invalid case

### HistoryHandler

You will not be able to write tests for your `HistoryHandler` without knowing the correct base-64 encoded image String. Verify your implementation visually by following the instructions in the spec.

---

## Project 2B: Wordnet (k==0)

### Graph

We suggest writing tests to ensure that your graph implementation is working as expected. Our solution has a class called `TestGraph` that evaluates various aspects of our implementation.

We recommend testing your graph methods with operations that are independent of the WordNet data. Granular tests will allow you to pinpoint whether a failing implementation is the result of an incorrect graph implementation, incorrect Wordnet data processing, or something else entirely. For example, if your implementation includes `createNode` or `addEdge` methods, confirm they yield an expected output separately from `hyponyms` and `synset` processing logic.

### WordNet

We recommend writing tests that evaluate queries on the examples above (for example, you might look at the hyponyms of "descent" in `synsets_size11.txt` and `hypernyms_size11.txt`, or the hyponyms of "change" in `synsets_size16.txt` and `hypernyms_size16.txt`.)

For example, our code has a class called `TestWordNet` containing the function below.

```java
@Test
public void testHyponymsSimple(){
        WordNet wn=new WordNet("./data/synsets_size11.txt","./data/hyponyms_size11.txt");
        assertThat(wn.hyponyms("antihistamine")).isEqualTo(Set.of("antihistamine","actifed"));
        }
```

Note your WordNet class may not have the same functions as mine so the test shown will probably not work verbatim with your code. Note that our test does NOT use an `NGramMap` anywhere, nor is it using a `HyponymHandler`, nor is it directly invoking an object of type `Graph`. It is specifically tailored to testing the WordNet class.

### Single Word

We've provided you with a short unit test files for this task in the file `tests/TestOneWordK0Hyponyms.java`.

This file corresponds to tests for finding hyponyms of a single word, where `k = 0`.

This test file is not comprehensive! In fact, it only contains one basic test. You should fill this file with more unit tests.

If you need help figuring out what the expected outputs of your tests should be, you can use the [staff solution webpage](https://ngordnet.datastructur.es/).

### List of Words

We've provided you with a short unit test files for this task in the file `tests/TestMultiWordK0Hyponyms.java`.

This file corresponds to tests for finding hyponyms of multiple words, where `k=0` (e.g. `gallery, bowl`).

This test file is not comprehensive! In fact, it only contains one basic test. You should fill this file with more unit tests.

If you need help figuring out what the expected outputs of your tests should be, you can use the [staff solution webpage](https://ngordnet.datastructur.es/).

### Testing in Browser

While you can (and should) write unit tests for the helper classes/methods that you create for this project, another good way to test and see what's going on with your code is to simply run `Main.java`, open `ngordnet.html`, enter some inputs into the boxes, and click the "Hyponyms" button. You may find visual debugging can lead to some useful discoveries in this project.

For example, you can use the web front-end to check the two input examples ("descent" and "change") from the diagrams above for `synsets_size16.txt` and `hyponyms_size16.txt`.

You can also run `Main.java` with the debugger to debug different inputs quickly. After clicking the “Hyponyms” button, your code will execute with the debugger - breakpoints will be triggered, you can use the variables window, etc.

Note: Relying on only browser tests will be incredibly frustrating (and slow!). Use your testing skills to build confidence in the foundational abstractions that you build (e.g. Graph, WordNet, etc.).

### Debugging

- Use the small input files while testing! This decreases the startup time to run `Main.java` and makes it easier to reason about the code. If you're running `Main.java`, these files are set in the first few lines of the `main` method. For unit tests, the file names are passed into the `getHyponymHandler` method.
- There are a lot of moving parts to this project. Don’t start by debugging line-by-line. Instead, narrow down which function/region of your code is not working correctly then search more closely in those lines.
- Because of the obfuscation that we applied to the Project 2A files (in particular, TimeSeries and NGramMap), the argument name previews when using these classes in IntelliJ may look a little weird. You may see long, random strings; these are intentional in order to obfuscate the code, and they do not represent an issue with your own code in any way.

## Project 2B: Wordnet (k!=0)

We have not provided any tests for the `k != 0` case.

You can use the sample tests in `TestOneWordK0Hyponyms` and `TestMultiWordK0Hyponyms` as a template to create new tests in this new testing file, e.g. `tests/TestKNonzeroHyponyms.java`.

You'll need to construct your own test cases. We provide one above: `words = "food, cake"`, `startYear = 1950`, `endYear = 1990`, `k = 5`.

If you need help figuring out what the expected outputs of your tests should be, you can use the [staff solution webpage](https://ngordnet.datastructur.es/).