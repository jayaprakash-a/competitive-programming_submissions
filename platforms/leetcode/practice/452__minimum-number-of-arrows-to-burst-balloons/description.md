---
Problem Title: 452. Minimum Number of Arrows to Burst Balloons
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
Problem Tags: Array, Greedy, Sorting
Solution Url: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.


An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with `xstart` and `xend` bursts by an arrow shot at `x` if `xstart ≤ x ≤ xend`. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.


Given an array `points` where `points[i] = [xstart, xend]`, return *the minimum number of arrows that must be shot to burst all balloons*.


 


**Example 1:**



```

**Input:** points = [[10,16],[2,8],[1,6],[7,12]]
**Output:** 2
**Explanation:** One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

```

**Example 2:**



```

**Input:** points = [[1,2],[3,4],[5,6],[7,8]]
**Output:** 4

```

**Example 3:**



```

**Input:** points = [[1,2],[2,3],[3,4],[4,5]]
**Output:** 2

```

 


**Constraints:**


* `1 <= points.length <= 105`
* `points[i].length == 2`
* `-231 <= xstart < xend <= 231 - 1`




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
