---
Problem Title: 1954. Minimum Garden Perimeter to Collect Enough Apples
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
Problem Tags: Math, Binary Search
Solution Url: https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

In a garden represented as an infinite 2D grid, there is an apple tree planted at **every** integer coordinate. The apple tree planted at an integer coordinate `(i, j)` has `|i| + |j|` apples growing on it.


You will buy an axis-aligned **square plot** of land that is centered at `(0, 0)`.


Given an integer `neededApples`, return *the **minimum perimeter** of a plot such that **at least***`neededApples` *apples are **inside or on** the perimeter of that plot*.


The value of `|x|` is defined as:


* `x` if `x >= 0`
* `-x` if `x < 0`


 


**Example 1:**


![](https://assets.leetcode.com/uploads/2019/08/30/1527_example_1_2.png)

```

**Input:** neededApples = 1
**Output:** 8
**Explanation:** A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.

```

**Example 2:**



```

**Input:** neededApples = 13
**Output:** 16

```

**Example 3:**



```

**Input:** neededApples = 1000000000
**Output:** 5040

```

 


**Constraints:**


* `1 <= neededApples <= 1015`




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
