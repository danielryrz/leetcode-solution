# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        LeetCode Problem 98: Validate Binary Search Tree
        ------------------------------------------------
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        
        A valid BST satisfies:
          1. The left subtree of a node contains only nodes with keys less than the node’s key.
          2. The right subtree of a node contains only nodes with keys greater than the node’s key.
          3. Both left and right subtrees must also be valid BSTs.

        Approach:
        ----------
        - Use recursion to validate each node within a permissible value range.
        - Initially, the valid range is (-∞, +∞).
        - For each node:
            - The left child must be within (low, node.val)
            - The right child must be within (node.val, high)
        - If any node violates its range, the tree is not a valid BST.

        Time Complexity:
        ----------------
        O(n) — Each node is visited exactly once.

        Space Complexity:
        -----------------
        O(h) — Recursive call stack where h is the height of the tree.
               In the worst case (skewed tree), h = n.

        Returns:
        --------
        bool — True if the binary tree is a valid BST, False otherwise.
        """

        def validate(node, low=float('-inf'), high=float('inf')):
            # Base case: empty nodes are valid BSTs
            if not node:
                return True

            # The current node’s value must be within the valid range
            if not (low < node.val < high):
                return False

            # Recursively validate left and right subtrees with updated ranges
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Start recursion from the root with the full range
        return validate(root)
