# Problem 121: Best Time to Buy and Sell Stock
# 
# You are given an array `prices` where prices[i] is the price of a stock on day i.
# You want to maximize your profit by choosing a single day to buy one stock
# and a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve. If no profit is possible, return 0.
#
# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.


class Solution:
    def maxProfit(self, prices):
        """
        Calculate the maximum profit from buying and selling a stock once.

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum profit achievable.
        
        Approach:
            - Track the minimum price seen so far.
            - Calculate potential profit at each day.
            - Update maximum profit accordingly.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only two variables used
        """
        min_price = float('inf')  # Initialize minimum price
        max_profit = 0             # Initialize maximum profit

        for price in prices:
            min_price = min(min_price, price)           # Update minimum price if current is lower
            max_profit = max(max_profit, price - min_price)  # Update max profit if selling today is better
        
        return max_profit
