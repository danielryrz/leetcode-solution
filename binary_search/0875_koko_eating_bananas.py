from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        LeetCode 875 - Koko Eating Bananas

        Problem:
        Koko has a list of banana piles. Each hour, she chooses one pile and eats
        up to k bananas from it. If the pile has fewer than k bananas, she eats
        the entire pile in that hour.

        Given an integer h (total hours available), return the minimum integer
        eating speed k such that Koko can eat all the bananas within h hours.

        Approach:
        - Use binary search on the possible eating speed k
        - Minimum possible speed is 1
        - Maximum possible speed is max(piles)
        - For each candidate speed k, calculate how many hours it would take
          to finish all piles
        - If total time <= h, try a smaller speed (move left)
        - Otherwise, increase the speed (move right)

        Time Complexity:
        - Let n = number of piles
        - Binary search runs in O(log(max(piles)))
        - Each check iterates over all piles in O(n)
        - Total time complexity: O(n * log(max(piles)))

        Space Complexity:
        - Only constant extra space is used
        - Space complexity: O(1)
        """

        L = math.ceil(sum(piles) / h) 
        R = max(piles)
        res = R


        while L <= R:
            k = (L+R)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            
            if totalTime <= h:
                res = k 
                R = k - 1
            else:
                L = k + 1
        
        return res
