---
Problem Title: 1297. Maximum Number of Occurrences of a Substring
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
Problem Tags: Hash Table, String, Sliding Window
Solution Url: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

Given a string `s`, return the maximum number of ocurrences of **any** substring under the following rules:


* The number of unique characters in the substring must be less than or equal to `maxLetters`.
* The substring size must be between `minSize` and `maxSize` inclusive.


 


**Example 1:**



```

**Input:** s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
**Output:** 2
**Explanation:** Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

```

**Example 2:**



```

**Input:** s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
**Output:** 2
**Explanation:** Substring "aaa" occur 2 times in the string. It can overlap.

```

**Example 3:**



```

**Input:** s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
**Output:** 3

```

**Example 4:**



```

**Input:** s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
**Output:** 0

```

 


**Constraints:**


* `1 <= s.length <= 10^5`
* `1 <= maxLetters <= 26`
* `1 <= minSize <= maxSize <= min(26, s.length)`
* `s` only contains lowercase English letters.


# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
