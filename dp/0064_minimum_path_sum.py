# ====================================================
# In-place DP Optimization
# ====================================================

def minPathSumInPlace(grid):
    """
    Optimized DP solution that modifies the grid in-place.
    Saves space by reusing the input grid.

    Time: O(m*n)
    Space: O(1)
    """
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue  # start cell
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1]
