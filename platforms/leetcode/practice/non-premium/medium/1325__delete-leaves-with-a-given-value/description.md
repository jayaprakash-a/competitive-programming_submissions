---
Problem Title: 1325. Delete Leaves With a Given Value
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/delete-leaves-with-a-given-value/
Problem Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
Solution Url: https://leetcode.com/problems/delete-leaves-with-a-given-value/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

Given a binary tree `root` and an integer `target`, delete all the **leaf nodes** with value `target`.


Note that once you delete a leaf node with value `target`**,**if it's parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you can't).


 


**Example 1:**


**![](https://assets.leetcode.com/uploads/2020/01/09/sample_1_1684.png)**



```

**Input:** root = [1,2,3,2,null,2,4], target = 2
**Output:** [1,null,3,null,4]
**Explanation:** Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

```

**Example 2:**


**![](https://assets.leetcode.com/uploads/2020/01/09/sample_2_1684.png)**



```

**Input:** root = [1,3,3,3,2], target = 3
**Output:** [1,3,null,null,2]

```

**Example 3:**


**![](https://assets.leetcode.com/uploads/2020/01/15/sample_3_1684.png)**



```

**Input:** root = [1,2,null,2,null,2], target = 2
**Output:** [1]
**Explanation:** Leaf nodes in green with value (target = 2) are removed at each step.

```

**Example 4:**



```

**Input:** root = [1,1,1], target = 1
**Output:** []

```

**Example 5:**



```

**Input:** root = [1,2,3], target = 1
**Output:** [1,2,3]

```

 


**Constraints:**


* `1 <= target <= 1000`
* The given binary tree will have between `1` and `3000` nodes.
* Each node's value is between `[1, 1000]`.




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
