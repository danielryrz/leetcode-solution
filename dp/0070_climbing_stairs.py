"""
LeetCode 70: Climbing Stairs
-----------------------------

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Mathematical idea:
A total length of all the steps is n = 2t + s  => s = n - 2t ; where t is a two steps move, s is a one step move.
That's why the length of a two step move is 2t.
Now, the total number of steps (set of all the moves) is t + s = t + n -2t = n - t
We can rephrase the problem: of selecting two steps move from the total number (set) of moves.  
t can take values from t=0 up to t = n//2 .

Formula:
    ways(n) = Σ (from t=0 to ⌊n//2⌋) C(n - t, t)

where ways(n) is number of ways of choosing n steps to get to the top.

As, this approach uses Python's built-in math.comb() function for
efficient integer arithmetic implemented in C, it results in a fast
and numerically exact solution.
Solutions:
1. Combinatorial approach
"""

# ====================================================
# Version 1: Combinatorial approach
# ====================================================
import math


def climb_stairs(n: int) -> int:
    """
    Return the number of distinct ways to climb `n` stairs,
    where each move is either 1 or 2 steps.

    Args:
        n (int): Number of steps.

    Returns:
        int: Total number of distinct ways.
    """
    if n <= 2:
        return n

    total = 0
    for t in range(0, n // 2 + 1):
        total += math.comb(n - t, t)
    return total


if __name__ == "__main__":
    # Example runs
    print(climb_stairs(5))   # 8
    print(climb_stairs(10))  # 89
    print(climb_stairs(15))  # 987
    print(climb_stairs(25))  # 121393
