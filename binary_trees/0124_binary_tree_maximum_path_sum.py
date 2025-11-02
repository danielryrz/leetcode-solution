"""
LeetCode 124. Binary Tree Maximum Path Sum
------------------------------------------
This solution uses Depth-First Search (DFS) to compute the maximum path sum in a binary tree.

At each node:
- We recursively compute the maximum path sum from its left and right subtrees.
- If a subtree sum is negative, we treat it as 0 (i.e., we omit that path).
- The path sum that passes through the current node is calculated as:
    node.val + left_max + right_max
- We update a global maximum (`self.max_sum`) whenever we find a higher path sum.

The recursion returns the maximum path sum *extending to the parent*:
    node.val + max(left_max, right_max)

Time Complexity: O(N), N - no. of nodes
Space Complexity: O(H), where H is the height of the tree. H <= N, unless the tree is skewed, then O(H) = O(N). For a balanceed tree O(H) = O(logN)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Initialize the maximum path sum as negative infinity
        # As at least one node needs to be included in the sum, so any node.val > float('-inf') 
        self.max_sum = float('-inf')

        def dfs(node):
            # Base case: empty node contributes 0
            if not node:
                return 0

            # dfs node.left. I.e. dive in on the left side of the tree, take 0 instead of -ve value
            # I.e. omit the -ve node.val
            left_max = max(dfs(node.left), 0)

            # dfs node.right I.e. dive in on the right side of the tree, take 0 instead of -ve node.val
            # I.e. omit the -ve node.val
            right_max = max(dfs(node.right), 0)

            # Update global maximum if found new maximum
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)

            # Return the max path sum extending upward to the parent, either left OR right subtree side
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum


# Example usage:
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# sol = Solution()
# print("Maximum Path Sum:", sol.maxPathSum(root))  # Output: 42
