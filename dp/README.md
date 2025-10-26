# Dynamic Programming Problems

This folder contains solutions to LeetCode DP problems.  
Each problem includes code + explanation, and sometimes multiple approaches.

---

### [Unique Paths (#62)](0062_unique_paths.py)

**Problem:**  
A robot is located at the top-left corner of an `m x n` grid.  
It can only move either **down** or **right** at any point.  
The robot is trying to reach the bottom-right corner.  

Return the number of **unique paths** from start to finish.

---

**Solutions:**

- **Version 1: Dynamic Programming (Tabulation)**  
  Build a `dp` grid where `dp[i][j]` = number of ways to reach cell `(i,j)`.  
  Transition: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.  
  - Time: O(m·n)  
  - Space: O(m·n) → can be optimized to O(n)  

- **Version 2: Combinatorial (Mathematical)**  
  To reach the bottom-right corner, the robot must make exactly `(m-1)` downs and `(n-1)` rights.  
  This is equivalent to choosing positions for downs (or rights) in `(m+n-2)` moves.
  Once the downs are chosen, the rights are already determined, to reach the right bottom.
  We can think of it as following: on how many ways can we pick `(m-1)` downs from the set of total `(m+n-2)` moves.
  After selecting downs, the rights will be determined.    
  Formula:  

  ![formula](https://latex.codecogs.com/png.image?\dpi{110}\bg_white\large\binom{m+n-2}{m-1}=\frac{(m+n-2)!}{(m-1)!(n-1)!})

  The same results if selecting rights from the total moves. Then the downs would be determined.
  ![formula](https://latex.codecogs.com/png.image?\dpi{110}\bg_white\large\binom{m+n-2}{n-1}=\frac{(m+n-2)!}{(n-1)!(m+n-21-n+1)!}=\frac{(m+n-2)!}{(n-1)!(m-1)!})

  - Time: O(min(m,n))  
  - Space: O(1)  

  **Why O(min(m, n))?**  
  Instead of computing full factorials, modern implementations of `math.comb(n, k)` compute the product  
  \[
  \frac{n × (n-1) × … × (n-k+1)}{k!}
  \]  
  and always use the smaller of `k` and `n−k`.  
  Therefore, it performs roughly `min(m, n)` multiplications/divisions, making it extremely fast in practice.

---

**Examples:**

- `m = 3, n = 7 → 28`  
- `m = 3, n = 2 → 3`

---

### [Climbing Stairs (#70)](0070_climbing_stairs.py)

**Problem:**  
You are climbing a staircase with `n` steps. Each time you can climb either **1** or **2** steps.  
Return the number of distinct ways to reach the top.

**Solution: Combinatorial (Mathematical)**  
This implementation uses a **combinatorial counting** approach rather than a dynamic programming table.  

A total length of all the steps is `n = 2t + s  => s = n - 2t`. 
Where `t` is a two steps move, `s` is a one step move.
That's why the length of a two step move is `2t`.
Now, the total number of possible steps (set of all the possible moves) is 
`t + s = t + n -2t = n - t`
We can rephrase the problem: of selecting two steps move from the total number (set) of possible moves.  
`t` can take values from `t=0` up to `t = n//2` .

The number of distinct sequences is determined by choosing which positions are 2-steps. 
Once 2-steps moves are chosen, the 1 step moves are determined. 

**Formula:**  

![formula](https://latex.codecogs.com/png.image?\dpi{120}\bg_white\large\text{ways}(n)=\sum_{t=0}^{\lfloor%20n/2%20\rfloor}\binom{n-t}{t})

`ways(n) = Σ (from t = 0 to ⌊n/2⌋) C(n - t, t)`


---

**Implementation:**

```python
import math

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    total = 0
    for t in range(0, n // 2 + 1):
        total += math.comb(n - t, t)
    return total
