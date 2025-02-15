---
Problem Title: 278. First Bad Version
Problem Difficulty: Easy
Problem Url: https://leetcode.com/problems/first-bad-version/
Problem Tags: Binary Search, Interactive
Solution Url: https://leetcode.com/problems/first-bad-version/solution/
IsPremium: No
IsTemplate: Yes
---

<span style="color: rgb(67, 160, 71);">Easy</span>

# Description

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since
each version is developed based on the previous version, all the versions after
a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the
first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version`
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.

**Example 1:**

```markdown
**Input:** n = 5, bad = 4
**Output:** 4
**Explanation:**
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

**Example 2:**

```markdown
**Input:** n = 1, bad = 1
**Output:** 1
```

**Constraints:**

-   `1 <= bad <= n <= 2^31 - 1`

# LeetCode Similar Problems

-   []()

# Useful Discussions

-   [[Python/ Clear explanation] Powerful Ultimate Binary Search Template. Solved many problems.](https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.)
