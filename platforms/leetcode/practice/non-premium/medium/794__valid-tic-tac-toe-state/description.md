---
Problem Title: 794. Valid Tic-Tac-Toe State
Problem Difficulty: Medium
Problem Url: https://leetcode.com/problems/valid-tic-tac-toe-state/
Problem Tags: Array, String
Solution Url: https://leetcode.com/problems/valid-tic-tac-toe-state/solution/
IsPremium: No
IsTemplate: No
---

<span style="color: rgb(239, 108, 0);">Medium</span>

# Description

Given a Tic-Tac-Toe board as a string array `board`, return `true` if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.


The board is a `3 x 3` array that consists of characters `' '`, `'X'`, and `'O'`. The `' '` character represents an empty square.


Here are the rules of Tic-Tac-Toe:


* Players take turns placing characters into empty squares `' '`.
* The first player always places `'X'` characters, while the second player always places `'O'` characters.
* `'X'` and `'O'` characters are always placed into empty squares, never filled ones.
* The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
* The game also ends if all squares are non-empty.
* No more moves can be played if the game is over.


 


**Example 1:**


![](https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg)

```

**Input:** board = ["O  ","   ","   "]
**Output:** false
Explanation: The first player always plays "X".

```

**Example 2:**


![](https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg)

```

**Input:** board = ["XOX"," X ","   "]
**Output:** false
Explanation: Players take turns making moves.

```

**Example 3:**


![](https://assets.leetcode.com/uploads/2021/05/15/tictactoe3-grid.jpg)

```

**Input:** board = ["XXX","   ","OOO"]
**Output:** false

```

**Example 4:**


![](https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg)

```

**Input:** board = ["XOX","O O","XOX"]
**Output:** true

```

 


**Constraints:**


* `board.length == 3`
* `board[i].length == 3`
* `board[i][j]` is either `'X'`, `'O'`, or `' '`.




# LeetCode Similar Problems

- []()

# Useful Discussions

- []()
