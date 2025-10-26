"""
LeetCode 297. Serialize and Deserialize Binary Tree
---------------------------------------------------
This solution uses Depth-First Search (DFS) pre-order traversal
to serialize and deserialize a binary tree.

Serialization: Converts the tree into a comma-separated string.
Deserialization: Rebuilds the tree recursively from the string.

Time Complexity: O(N)
Space Complexity: O(N)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                vals.append("null")
                return #need to reutrn as we want to return to the previous level of the tree
            
            # append str(node.val) to vals list  
            vals.append(str(node.val))
            
            # recursively dive into the node.left (depth first search method)
            dfs(node.left)
            
            # once all the .left nodes are serialized, 
            # coming back from the bottom (leaves) add .right nodes, going up
            # (depth first search method)
            dfs(node.right)

            # no need to return anything, as the vals are appended as we dfs the binary tree
       
        vals = []
        dfs(root)
        return ",".join(vals) #return a single string


    def deserialize(self, data):
        """Decodes your encoded data to tree."""

        def dfs():
            val = next(vals)

            # if val == "null" then return None
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            
            # recursively build a Binary Tree first checking the left nodes
            node.left = dfs()

            # recursively build a Binary Tree first checking the right nodes
            node.right = dfs()

            return node

        vals = iter(data.split(","))
        return dfs()
        

# Example usage:
# ser = Codec()
# deser = Codec()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
# serialized = ser.serialize(root)
# print("Serialized:", serialized)
# deserialized = deser.deserialize(serialized)
# print("Deserialized root:", deserialized.val)



