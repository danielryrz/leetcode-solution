from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        LeetCode 347. Top K Frequent Elements
        
        Approach:
        ---------
        We use a Bucket Sort–based method to achieve O(n) time complexity.
        1. Count the frequency of each number.
        2. Create buckets where index = frequency.
        3. Traverse buckets from highest frequency down until we collect k elements.

        This avoids sorting the frequency list (which would be O(n log n))
        and satisfies the follow-up requirement: better than O(n log n).

        Parameters:
        -----------
        nums : List[int]
            The list of integers.
        k : int
            The number of most frequent elements to return.

        Returns:
        --------
        List[int]
            The k elements with the highest frequency.
        """

        # Step 1: Count each number's frequency
        freq = Counter(nums)  # e.g., {num: count}

        # Step 2: Create buckets where index = frequency
        # Max frequency cannot exceed len(nums), so allocate len(nums) + 1 buckets.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Place numbers into the corresponding bucket
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Build the result by scanning buckets from highest frequency
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result

        # Should never reach here since k is always valid
        return result

