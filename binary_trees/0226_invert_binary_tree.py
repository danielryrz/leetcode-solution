# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    Problem: Invert Binary Tree
    --------------------------------
    Given the root of a binary tree, invert the tree, and return its root.
    
    In an inverted binary tree, every node's left and right children are swapped.
    
    Example:
        Input:
                4
               / \
              2   7
             / \ / \
            1  3 6  9

        Output:
                4
               / \
              7   2
             / \ / \
            9  6 3  1

    Approach:
        1. Base case: If the current node is None, return None.
        2. Swap the left and right child nodes.
        3. Recursively invert the left subtree.
        4. Recursively invert the right subtree.
        5. Return the current root node.

    Time Complexity:  O(n)
        - Each node is visited exactly once.

    Space Complexity: O(h)
        - Due to recursion stack space, where h is the height of the tree.
        - Worst case (skewed tree): O(n)
        - Best case (balanced tree): O(log n)
    """

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Base case: if tree is empty, just return None
        if not root:
            return None
        
        # Step 1: Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Step 2: Recursively invert left subtree
        self.invertTree(root.left)
        
        # Step 3: Recursively invert right subtree
        self.invertTree(root.right)
        
        # Finally, return the root node (now inverted)
        return root
