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

Time Complexity:  O(M × N)
Space Complexity:
    BFS → O(min(M, N)) for the queue (current frontier)
    DFS → O(M × N) for recursion stack in the worst case
"""

from collections import deque


def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    # ----------- BFS Implementation -----------
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # mark as visited (sink land)

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))

    # ----------- DFS Implementation -----------
    # def dfs(r, c):
    #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
    #         return
    #     grid[r][c] = '0'  # mark as visited (sink land)
    #     dfs(r + 1, c)
    #     dfs(r - 1, c)
    #     dfs(r, c + 1)
    #     dfs(r, c - 1)

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
