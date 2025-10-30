"""
LeetCode 64: Minimum Path Sum
-----------------------------

Problem:
Given an m x n grid filled with non-negative numbers, find a path from top-left
to bottom-right that minimizes the sum of all numbers along its path.
You can only move right or down at any point.

Solutions:
1. Dynamic Programming with 2D DP table
2. In-place DP optimization
"""

# ====================================================
# Version 1: DP with separate 2D table
# ====================================================

def minPathSumDP(grid):
    """
    Classic DP solution using a separate dp table.

    dp[i][j] = min sum to reach (i, j) from (0, 0)

    Time: O(m*n)
    Space: O(m*n)
    """
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill the rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]


# ====================================================
# Version 2: In-place DP Optimization - preferred 
# ====================================================

def minPathSumInPlace(grid):
    """
    Optimized DP solution that modifies the grid in-place.
    Saves space by reusing the input grid.

    Time: O(m*n)
    Space: O(1)
    """
    m = len(grid) # len of rows
    n =  len(grid[0]) # len of cols

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue  # start cell

            # in first row, except grid[0][0], the values can be added only from the left, 
            # so we add to the cell the value from the left 
            elif i == 0: # first row
                grid[i][j] += grid[i][j-1]

            # in the first col, except grid[0][0], the values can be added only from above  
            # so we add to the cell the value from above 
            elif j == 0: # first col
                grid[i][j] += grid[i-1][j]
            
            else: # find a mininum value (either from the top, or from the left)
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1] # return final sum


# ====================================================
# Example Usage
# ====================================================
if __name__ == "__main__":
    grid1 = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]

    print("DP version:", minPathSumDP([row[:] for row in grid1]))       # Output: 7
    print("In-place version:", minPathSumInPlace([row[:] for row in grid1]))  # Output: 7
