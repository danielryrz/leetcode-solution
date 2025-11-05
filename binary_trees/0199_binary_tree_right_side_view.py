"""
LeetCode Problem 199: Binary Tree Right Side View
-------------------------------------------------
Given the root of a binary tree, imagine yourself standing on the right side of it.
Return the values of the nodes you can see ordered from top to bottom.

Example:
---------
Input: root = [1,2,3,None,5,None,4]
Output: [1,3,4]

Explanation:
-------------
From the right side, you can see nodes 1, 3, and 4.

Approach:
----------
We perform a depth-first search (DFS), prioritizing the right subtree first.
At each depth level, we record the first node encountered — which will be the rightmost one.

Time Complexity:
-----------------
O(N), where N is the number of nodes in the tree.
Each node is visited exactly once.

Space Complexity:
------------------
O(H), where H is the height of the tree.
This accounts for the recursion stack in the worst case.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, depth):
            if not node:
                return
            # If this is the first node we encounter at this depth, record it
            if depth == len(res):
                res.append(node.val)
            
            # Visit the right subtree first to ensure rightmost nodes are recorded first
            dfs(node.right, depth + 1)
            # Then visit the left subtree
            dfs(node.left, depth + 1)

        res = []
        dfs(root, 0)
        return res
