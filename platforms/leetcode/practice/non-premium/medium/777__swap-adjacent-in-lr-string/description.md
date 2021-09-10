---
Problem Title: 777. Swap Adjacent in LR String
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/swap-adjacent-in-lr-string/
Problem Tags: Two Pointers, String
Solution Url: https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

In a string composed of `'L'`, `'R'`, and `'X'` characters, like `"RXXLRXRXL"`, a move consists of either replacing one occurrence of `"XL"` with `"LX"`, or replacing one occurrence of `"RX"` with `"XR"`. Given the starting string `start` and the ending string `end`, return `True` if and only if there exists a sequence of moves to transform one string to the other.


 


**Example 1:**



```

**Input:** start = "RXXLRXRXL", end = "XRLXXRRLX"
**Output:** true
**Explanation:** We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

```

**Example 2:**



```

**Input:** start = "X", end = "L"
**Output:** false

```

**Example 3:**



```

**Input:** start = "LLR", end = "RRL"
**Output:** false

```

**Example 4:**



```

**Input:** start = "XL", end = "LX"
**Output:** true

```

**Example 5:**



```

**Input:** start = "XLLR", end = "LXLX"
**Output:** false

```

 


**Constraints:**


* `1 <= start.length <= 104`
* `start.length == end.length`
* Both `start` and `end` will only consist of characters in `'L'`, `'R'`, and `'X'`.




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
