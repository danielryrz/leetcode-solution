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

        L = 1
        R = max(piles)
        res = R

        while L <= R:
            k = (L + R) // 2
            time = 0

            # Calculate total hours needed at speed k
            for p in piles:
                # Ceiling division to account for partial hours
                time += (p + k - 1) // k

            # If Koko can finish within h hours, try smaller speed
            if time <= h:
                res = min(res, k)
                R = k - 1
            # Otherwise, speed is too slow
            else:
                L = k + 1

        return res
