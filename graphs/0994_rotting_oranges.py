"""
994. Rotting Oranges
LeetCode Problem Link: https://leetcode.com/problems/rotting-oranges/

🧩 Problem Description:
You are given an m x n grid where each cell can have one of three values:
    0 -> empty cell
    1 -> fresh orange
    2 -> rotten orange

Every minute, any fresh orange that is 4-directionally adjacent (up, down, left, right)
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

------------------------------------------------------------
💡 Example:
Input:
grid = [
 [2,1,1],
 [1,1,0],
 [0,1,1]
]

Output:
4

Explanation:
Each minute, the rot spreads to adjacent oranges.
After 4 minutes, all oranges become rotten.

------------------------------------------------------------
🧠 Approach (BFS - Breadth First Search):
1. Use a queue to perform a multi-source BFS starting from all rotten oranges.
2. Each level in BFS represents 1 minute passing.
3. For each rotten orange, spread rot to its 4-directionally adjacent fresh oranges.
4. Track the number of fresh oranges; when it reaches 0, return the minutes elapsed.
5. If after BFS some fresh oranges remain, return -1.

------------------------------------------------------------
⚙️ Why 'elif' instead of two 'if's in the setup loop?
We use 'elif' because each cell can only hold ONE value (0, 1, or 2).
If we used two separate 'if' statements, both conditions would be checked unnecessarily.
Using 'elif' skips the second check once the first condition is true — slightly more efficient.

------------------------------------------------------------
⏱️ Time Complexity:  O(m × n)
- Each cell is visited at most once during BFS.

📦 Space Complexity: O(m × n)
- In the worst case, all cells could be added to the queue.
------------------------------------------------------------
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0  # count of fresh oranges
        
        # Step 1: Initialize queue with all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If there are no fresh oranges initially
        if fresh == 0:
            return 0
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = -1  # start at -1 so the final increment equals the correct time
        
        # Step 2: BFS traversal
        while queue:
            for _ in range(len(queue)):
                
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # make orange rotten
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1  # one minute passes after each BFS layer
            
        
        # Step 3: Check if any fresh oranges remain
        return minutes if fresh == 0 else -1
