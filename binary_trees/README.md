# Binary Tree Problems 

This folder contains solutions to LeetCode Binary Tree problems.  
Each problem includes code + explanation, and sometimes multiple approaches. 

---

### [Binary Tree Maximum Path Sum (#124)](0124_binary_tree_maximum_path_sum.py)

# LeetCode 124. Binary Tree Maximum Path Sum

This repository contains a Python solution for **LeetCode Problem 124: Binary Tree Maximum Path Sum**.  
The solution uses **Depth-First Search (DFS)** to compute the maximum possible path sum in a binary tree, where a path can start and end at any node.

---

## Problem Description

Given a **non-empty binary tree**, find the path with the **maximum sum**.  
A path is any sequence of nodes where each pair of adjacent nodes has an edge connecting them.  
The path must contain **at least one node**, and it **does not need to go through the root**.

---

## Approach

- Use **DFS traversal** to recursively compute two quantities for each node:
  - **max_gain(node)**: maximum path sum starting from this node and extending to one of its subtrees.
  - **global_max_sum**: track the maximum path sum found so far.
- For each node:
  - Recursively compute left and right gains.
  - Ignore negative contributions (use `max(left_gain, 0)`).
  - Update the global max if `node.val + left_gain + right_gain` is greater.
  - Return `node.val + max(left_gain, right_gain)` to parent call.

---

## Complexity

- **Time Complexity**: O(N) – each node is visited once.
- **Space Complexity**: O(H) – recursion stack (H = height of the tree).

---

### Code

```python
# binary_trees/0124_binary_tree_maximum_path_sum.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute max gain from left and right subtrees
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Update global max if the path through this node is higher
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max gain including this node and one subtree
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
```
--- 

### [Serialize and Deserialize Binary Tree (#297)](0297_serialize_and_deserialize_binary_tree.py) 

# LeetCode 297. Serialize and Deserialize Binary Tree

This repository contains a Python solution for **LeetCode Problem 297: Serialize and Deserialize Binary Tree**. The solution uses **Depth-First Search (DFS)** with pre-order traversal to serialize a binary tree into a string and deserialize it back into a tree.

---

## Problem Description

Design an algorithm to **serialize** and **deserialize** a binary tree.  
Serialization is the process of converting a data structure into a string so it can be stored or transmitted.  
Deserialization is the reverse process of reconstructing the data structure from the string.

We need to implement the following methods:

- `serialize(root)`: Encodes a tree to a single string.
- `deserialize(data)`: Decodes your encoded data to tree.

---

## Approach

- **Serialization**:
  - Use pre-order DFS traversal (root → left → right).
  - Represent `None` nodes as `"null"`.
  - Join all node values into a comma-separated string.

- **Deserialization**:
  - Split the string by commas and iterate through the values.
  - Recursively rebuild the tree using DFS.
  - If a value is `"null"`, return `None`.

---

## Complexity

- **Time Complexity**: `O(N)` – each node is visited exactly once.
- **Space Complexity**: `O(N)` – storing the serialized string and recursion stack.

---

