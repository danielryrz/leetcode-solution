from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Problem:
        Given an integer array `nums`, return True if any value appears
        at least twice in the array, and return False if every element is distinct.

        Approach:
        - Use a hash set to keep track of elements seen so far.
        - Iterate through the array:
            - If the current number is already in the set, a duplicate exists.
            - Otherwise, add the number to the set.
        - If the loop completes without finding duplicates, return False.

        Time Complexity:
        - O(n), where n is the length of `nums`.
          Each lookup and insertion into the set is O(1) on average.

        Space Complexity:
        - O(n) in the worst case, when all elements are unique and stored in the set.
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

