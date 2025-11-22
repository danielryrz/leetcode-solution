"""
417. Pacific Atlantic Water Flow
--------------------------------
You are given an m x n matrix of integers representing the height of each cell
in a continent. Water can flow from a cell to neighboring cells (up, down,
left, right) if the neighbor's height is *less than or equal* to the current cell.

There are two oceans:
- The Pacific touches the left and top edges of the matrix.
- The Atlantic touches the right and bottom edges.

Return a list of grid coordinates where water can flow to *both* oceans.

--------------------------------
Approach:
We reverse the water-flow logic.

Instead of starting from each cell and checking if it can reach both oceans
(which would be slow), we start DFS/BFS *from the oceans*:

1. Perform DFS/BFS from all Pacific-border cells.
   - Mark all cells reachable following the inverse of the NON-INCREASING rule 
     (i.e., we allow moving water to equal or higher heights → reversed logic).

2. Do the same for Atlantic-border cells.

3. Any cell reachable in both searches can flow to both oceans.

--------------------------------
Time Complexity:
    O(m * n)
Every cell is visited at most twice (once for each ocean). 
We need to visit cell twice to confirm whether it can be reached by two oceans.

Space Complexity:
    O(m * n)
To store the visited sets for Pacific and Atlantic oceans.
"""

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        # Directions: up, down, right, left
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and height condition
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Do DFS 
        for c in range(cols):
            # Start at top row to check which cells we can reach from the Pacific (top row)
            # This will tell us: from which cells water will flow to Pacific "through" the top row
            dfs(0, c, pacific) 

            # Start at bottom row to check which cells we can reach from the Atlantic (from bottom row)
            # This will tell us: from which cells water will flow to Atlantic "through" the bottom row 
            dfs(rows - 1, c, atlantic) 

        for r in range(rows):
            #Iterate through the rows starting at column 0 (left side) from side which we will check if the water can flow (ni reverse) from there. 
            #This will add to pacific set cells from which the water can flow to Pacific "through" the left side (col 0)
            dfs(r, 0, pacific)          

            #Iterate through the rows starting at the last col (cols-1), so from the right side, to check if the water can flow (in reverse) from there.
            #This will add to atlantic set cells from which the water can flow to Atlantic "through" the right side (col cols-1)
            dfs(r, cols - 1, atlantic) 

        # Cells reachable by both oceans
        result = list(pacific & atlantic)
        return result
