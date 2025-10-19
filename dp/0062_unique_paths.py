"""
LeetCode 62: Unique Paths
-------------------------

Problem:
A robot is located at the top-left corner of an m x n grid. 
It can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner. 
How many possible unique paths are there?

Solutions:
1. Dynamic Programming (tabulation)
2. Combinatorial Formula
"""

# ====================================================
# Version 1: DP Tabulation
# ====================================================

def uniquePathsDP(m: int, n: int) -> int:
    """
    Dynamic Programming approach.
    dp[i][j] = ways to reach cell (i,j).
    
    Time: O(m*n)
    Space: O(m*n) -> can be optimized to O(n).
    """
    dp = [[1] * n for _ in range(m)]  # initialize first row/col with 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]


# ====================================================
# Version 2: Combinatorial Solution
# ====================================================

import math

def uniquePathsComb(m: int, n: int) -> int:
    """
    Combinatorial solution.
    Total moves = (m-1) downs + (n-1) rights = (m+n-2).
    Choose (m-1) positions for downs out of a set of total moves.
    I.e.: on how many ways can we make a move down, out of the possibilities of total moves.
    Once we choose down moves, the right moves are already determined by our down moves choices. 
    
    Time: O(min(m,n)) -> python > 3.8 computes math.comb(m+n-2,m-1) directly (it cancels out the factorial terms )
    Space: O(1)
    """
    return math.comb(m+n-2, m-1)


# ====================================================
# Example Usage
# ====================================================
if __name__ == "__main__":
    print("DP approach (3x7 grid):", uniquePathsDP(3, 7))     # Output: 28
    print("Combinatorial (3x7 grid):", uniquePathsComb(3, 7)) # Output: 28
    print("DP approach (3x2 grid):", uniquePathsDP(3, 2))     # Output: 3
    print("Combinatorial (3x2 grid):", uniquePathsComb(3, 2)) # Output: 3
