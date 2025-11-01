"""
LeetCode 322: Coin Change

🧩 Problem Summary:
Given a list of coin denominations and a target amount, 
return the minimum number of coins needed to make up that amount.
If it is not possible to make up the amount, return -1.

💡 Approach:
This solution uses Dynamic Programming (Bottom-Up).
We build a DP array where dp[i] represents the minimum number of coins
required to make up amount i. For each amount, we try every coin and 
update dp[i] with the smallest possible count.

⏱️ Time Complexity: O(amount * n)
    - For each amount up to `amount`, we iterate through all `n` coins.
    
💾 Space Complexity: O(amount)
    - We store one DP array of size `amount + 1`.

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)

        # It takes 0 coins to make up amount 0
        dp[0] = 0

        # Build dp from 1 up to the target amount
        for i in range(1, amount + 1):
            # Iterate through every coin to find the min number of coins to make amount i
            for coin in coins:
                # The coin can only be used if it does not exceed the current amount
                if i - coin >= 0:
                    # Take the minimum number of coins to make up value i
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Return result; if dp[-1] is still infinity, amount cannot be made
        return dp[-1] if dp[-1] != float('inf') else -1
