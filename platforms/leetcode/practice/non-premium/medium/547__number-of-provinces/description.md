---
Problem Title: 547. Number of Provinces
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/number-of-provinces/
Problem Tags: Depth-First Search, Breadth-First Search, Union Find, Graph
Solution Url: https://leetcode.com/problems/number-of-provinces/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.


A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.


You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.


Return *the total number of **provinces***.


 


**Example 1:**


![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

```

**Input:** isConnected = [[1,1,0],[1,1,0],[0,0,1]]
**Output:** 2

```

**Example 2:**


![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

```

**Input:** isConnected = [[1,0,0],[0,1,0],[0,0,1]]
**Output:** 3

```

 


**Constraints:**


* `1 <= n <= 200`
* `n == isConnected.length`
* `n == isConnected[i].length`
* `isConnected[i][j]` is `1` or `0`.
* `isConnected[i][i] == 1`
* `isConnected[i][j] == isConnected[j][i]`




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
