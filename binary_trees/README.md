# Binary Tree Problems 

This folder contains solutions to LeetCode Binary Tree problems.  
Each problem includes code + explanation, and sometimes multiple approaches. 

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

