from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search on a sorted array.

        Invariant:
        - If target exists, it must always be in the range [left, right]

        Key rule:
        - Once nums[mid] is checked and is NOT the target,
          mid must be excluded from the next search interval.
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            # Midpoint of current search interval
            # mid = (left + right) // 2 #this could be used but for big nums size, let's prevent the overflow:
            mid = l + ((r-l)//2) # as ((r-l)//2) gives us a half in between l and r, the l + ((r-l)//2) lands exactly where the new mid should be 

            # Case 1: Found the target
            if nums[mid] == target:
                return mid

            # Case 2: Target is strictly on the right side
            elif nums[mid] < target:
                # mid is too small and already checked → exclude it
                left = mid + 1

            # Case 3: Target is strictly on the left side
            else:  # nums[mid] > target
                # mid is too large and already checked → exclude it
                right = mid - 1

        # Target does not exist in the array
        return -1
