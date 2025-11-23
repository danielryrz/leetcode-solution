"""
LeetCode Problem 200: Number of Islands
---------------------------------------
Problem:
You are given an m x n 2D binary grid `grid` representing a map of '1's (land) and '0's (water).
An island is formed by connecting adjacent lands horizontally or vertically. You may assume all
four edges of the grid are surrounded by water.

Return the number of islands in the grid.

Approach:
We can solve this using either Breadth-First Search (BFS) or Depth-First Search (DFS):

- Traverse every cell in the grid.
- When a '1' (land) is found, increment the island count and perform BFS or DFS
  to "sink" all connected land cells by marking them as '0'.
- Continue until all land has been visited.

BFS uses an explicit queue to explore neighbors layer by layer.
DFS recursively explores all connected cells.
In theory both run at the same speed as they visit every cell once.
However, especially in python, bfs loop (in this case while loop) + queue is cheaper than dfs recursive calls

Time Complexity:  O(M × N)
Space Complexity:
    BFS → O(min(M, N)) for the queue (current frontier)
    DFS → O(M × N) for recursion stack in the worst case
"""

from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    rows  = len(grid) 
    cols = len(grid[0])
    
    islands = 0

    # ----------- BFS Implementation -----------
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # mark as visited (sink land)

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nc][nr] = '0' #sink 
                    queue.append((nc, nr))

    # ----------- DFS Implementation -----------
    # def dfs(r,c):
    #     grid[r][c] = "0" #sink the island

    #     directions = [(1,0), (-1,0), (0,1), (0,-1)]

    #     for dr, dc in directions:
    #         nr = r + dr
    #         nc = c + dc

    #         if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
    #             dfs(nr,nc)

    # ----------- Main Loop -----------
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)  # or dfs(r, c)

    return islands


# Example usage:
if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))  # Output: 3
