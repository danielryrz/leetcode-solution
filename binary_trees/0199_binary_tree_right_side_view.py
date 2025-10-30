class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, depth):
            if not node:
                return
            # if this is the level that doesn't have a node yet, append this node.val
            if depth == len(res):
                res.append(node.val)

            # first dfs check the node.right
            dfs(node.right, depth+1)
            # then dfs check the node.right
            dfs(node.left, depth+1)

        res = []
        dfs(root, 0)

        return res
