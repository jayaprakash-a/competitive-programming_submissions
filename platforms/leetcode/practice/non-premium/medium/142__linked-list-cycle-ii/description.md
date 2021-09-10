---
Problem Title: 142. Linked List Cycle II
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/linked-list-cycle-ii/
Problem Tags: Hash Table, Linked List, Two Pointers
Solution Url: https://leetcode.com/problems/linked-list-cycle-ii/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.


There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.


**Notice** that you **should not modify** the linked list.


 


**Example 1:**


![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```

**Input:** head = [3,2,0,-4], pos = 1
**Output:** tail connects to node index 1
**Explanation:** There is a cycle in the linked list, where tail connects to the second node.

```

**Example 2:**


![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```

**Input:** head = [1,2], pos = 0
**Output:** tail connects to node index 0
**Explanation:** There is a cycle in the linked list, where tail connects to the first node.

```

**Example 3:**


![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```

**Input:** head = [1], pos = -1
**Output:** no cycle
**Explanation:** There is no cycle in the linked list.

```

 


**Constraints:**


* The number of the nodes in the list is in the range `[0, 104]`.
* `-105 <= Node.val <= 105`
* `pos` is `-1` or a **valid index** in the linked-list.


 


**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
