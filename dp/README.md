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

As, this approach uses Python's built-in math.comb() function for
efficient integer arithmetic implemented in C, it results in a fast
and numerically exact solution.

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
```
---

### [Climbing Stairs (#72)](0072_edit_distance.py)

**Problem:**  
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
  - Insert a character
  - Delete a character
  - Replace a character

---

**Solution: DP Table**  
This solution includes solving the problem using DP table (len(word1)+1) x (len(word2)+1).
A further optimisation can be mode by keeping only two rows of DP, as at each tieration we compare only the current row, and the row before.


---

### [Word Break (#139)](0139_word_break.py)

**Problem:**  
Given a string `s` and a list of words `wordDict`, determine if `s` can be segmented into a sequence of one or more dictionary words.  
You may reuse the same word multiple times.

---

**Solution: Dynamic Programming (Tabulation)**  

We define `dp[i]` as **True** if the substring `s[:i]` can be segmented into valid dictionary words.  
Start with `dp[0] = True` (the empty string is segmentable).  
Then, for each prefix length `i`, and for each word `w` in the dictionary:

If  
1. the word fits (`len(w) <= i`),  
2. the prefix before it is valid (`dp[i - len(w)]`), and  
3. the ending matches that word (`s[i - len(w):i] == w`),  

then mark `dp[i] = True`.

The final result is `dp[len(s)]`.

- **Time Complexity:** O(n · m · k)  
  (where `n = len(s)`, `m = len(wordDict)`, `k = average word length`)  
- **Space Complexity:** O(n)

---

### [Coin Change (#322)](0322_coin_change_.py)

**Problem:**  
You are given an integer array `coins` representing coin denominations and an integer `amount` representing a total amount of money.  
Return the **fewest number of coins** needed to make up that amount.  
If the amount cannot be made up by any combination of the coins, return `-1`.  
You may assume you have an infinite number of each kind of coin.

---

**Solution: Dynamic Programming (Tabulation)**  

We define `dp[i]` as the **minimum number of coins** required to make up the amount `i`.  
Start with `dp[0] = 0` (zero coins are needed to make amount 0).  
Initialize all other values to infinity (or a large number), meaning they are not yet reachable.

For each amount `i` from `1` to `amount`,  
we iterate through all coin denominations and update `dp[i]` using the recurrence:

If  
1. the coin can be used (`i - coin >= 0`), then  
2. `dp[i] = min(dp[i], dp[i - coin] + 1)`

This ensures that for every possible coin, we consider the fewest number of coins needed to build up to amount `i`.

The final result is stored in `dp[amount]`.  
If it remains infinity, the amount cannot be formed, and we return `-1`.

- **Time Complexity:** O(amount × n)  
  (where `n = len(coins)`)  
- **Space Complexity:** O(amount)

---

**Example Walkthrough**

Example:  
`coins = [1, 2, 5]`, `amount = 11`

| Amount (i) | Calculation                              | dp[i] | Coins Used Example |
|:-----------:|:----------------------------------------|:------:|:-------------------:|
| 0 | Base case | 0 | – |
| 1 | 1 = 1×1 | 1 | [1] |
| 2 | min(dp[2-1]+1, dp[2-2]+1) = 1 | 1 | [2] |
| 3 | min(dp[2]+1, dp[1]+1) = 2 | 2 | [1,2] |
| 5 | min(dp[5-5]+1, dp[4]+1) = 1 | 1 | [5] |
| 6 | min(dp[6-5]+1, dp[4]+1) = 2 | 2 | [5,1] |
| 10 | min(dp[10-5]+1) = 2 | 2 | [5,5] |
| 11 | min(dp[11-5]+1) = 3 | 3 | [5,5,1] |

✅ **Result:** `3` coins (5 + 5 + 1)

---

