class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0] 
        profit = 0

        for price in prices:
            profit = max(profit, price-buy)
            
            if price < buy: # as we traverse through the list we can select when to buy 
                buy = price
        
        return profit

        
