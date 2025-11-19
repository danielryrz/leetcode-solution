"""
133. Clone Graph
----------------
Given a reference to a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node contains a value and a list of neighbors.

Approach (DFS)
--------------
We use a Depth-First Search and a hash map to store already-cloned nodes.
This prevents re-cloning nodes and avoids infinite recursion caused by cycles.

Steps:
1. If input node is None, return None.
2. Use a recursive DFS:
    - If the current node has already been cloned, reuse it from the map.
    - Otherwise create a clone, store it in the map, then recursively
      clone all neighbors and attach them to the cloned node.
3. Return the clone of the starting node.

Why store the clone before cloning neighbors?
---------------------------------------------
Graphs may contain cycles. By storing the clone early, if a neighbor points
back to this node, DFS can immediately reuse the existing clone instead of
looping forever.

Time Complexity:  O(V + E)
Space Complexity: O(V)
Category: Graphs, DFS, HashMap
"""

# Definition for a Node (provided by LeetCode)
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        # Maps original nodes -> cloned nodes
        old_to_new = {}

        def dfs(node):
            # If this node was already cloned, return the clone
            if node in old_to_new:
                return old_to_new[node]

            # Clone the node (without neighbors initially)
            clone = Node(node.val)

            # Store clone early to handle cycles
            old_to_new[node] = clone

            # Recursively clone all neighbors and attach them
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
