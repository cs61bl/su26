---
layout: page
title: >-
  FAQ
parent: >-
  Lab 09: Runtime Analysis
grand_parent: Labs
has_right_toc: true
released: true
---


### `Sorter`: Why do students get different timing results?

> "You may notice that other students in lab end up with different timing
> results and a different number of elements. What factors might contribute to
> these differences?"

<details markdown="block">
  <summary markdown="block">
#### Answer
{: .no_toc}
  </summary>

Wall-clock timing depends on much more than the algorithm itself:

- **Hardware**: CPU clock speed, number of cores, and cache sizes differ from
  machine to machine.
- **System load**: other programs and background processes competing for the
  CPU will slow down your run.
- **The JVM**: just-in-time (JIT) compilation and warmup mean the same code can
  run at different speeds even on the same machine.
- **The input**: `Sorter` fills the array with *randomly* generated values, so
  each run is sorting a slightly different array.

This is exactly why timing is a poor way to compare algorithms, and why the
next section motivates **step counting** as a machine-independent alternative.

</details>

### Counting Steps: How many steps to finish the assignment to `b`?

> ```java
> int b = 9 * (a - 24) / (9 - 7);
> ```
> "How many more steps does it take to finish the assignment to `b`?"

<details markdown="block">
  <summary markdown="block">
#### Answer
{: .no_toc}
  </summary>

**5 steps** — 4 to evaluate the right-hand side expression, plus 1 to assign
the result to `b`:

1. `a - 24` (subtraction)
2. `9 - 7` (subtraction)
3. `9 * (...)` (multiplication)
4. `(...) / (...)` (division)
5. assignment to `b`

</details>

### `if ... else` Counting

> ```java
> if (A) {
>     B;
> } else {
>     C;
> }
> ```
> "How many steps does it take to evaluate the entire `if ... else` block in
> terms of the number of steps it takes to evaluate `A`, `B`, and `C`?"

<details markdown="block">
  <summary markdown="block">
#### Answer
{: .no_toc}
  </summary>

The condition `A` is **always** evaluated, and then **exactly one** of the two
branches runs (never both):

- If `A` is true: `steps(A) + steps(B)`
- If `A` is false: `steps(A) + steps(C)`

So the **best case** is `steps(A) + min(steps(B), steps(C))` and the **worst
case** is `steps(A) + max(steps(B), steps(C))`.

</details>
