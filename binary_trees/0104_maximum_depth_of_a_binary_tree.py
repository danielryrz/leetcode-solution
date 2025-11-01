"""
LeetCode 104: Maximum Depth of Binary Tree

Problem Statement:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example:
Input: [3,9,20,None,None,15,7]
Output: 3

Explanation:
The longest path is 3 → 20 → 7 (or 3 → 20 → 15), which has 3 nodes.

--------------------------------------------------------
Approach:
Use recursion. For each node, the maximum depth is:
    1 + max(depth of left subtree, depth of right subtree)
The base case is when the node is None, in which case the depth is 0.

--------------------------------------------------------
Time Complexity: O(n)
  - We visit each node exactly once, where n is the number of nodes.

Space Complexity: O(h)
  - The recursion stack uses space proportional to the height (h) of the tree.
  - In the worst case (a skewed tree), h = n; in the best case (a balanced tree), h = log(n).
"""

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
