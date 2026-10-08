from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        LeetCode 33 - Search in Rotated Sorted Array

        The array is originally sorted but rotated at an unknown pivot.
        At least one half of the array is always sorted.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        L = 0 
        R = len(nums) - 1

        while L <= R:
            mid = L + (R-L) // 2

            if nums[mid] == target:
                return mid

            if nums[L] <= nums[mid]:
                #left is sorted
                if nums[L] <= target and target < nums[mid]:
                    #it's in the left side
                    R = mid - 1
                else:
                    #it's in the right side
                    L = mid + 1

            else:
                # right is sorted
                if nums[mid] < target and target <= nums[R]:
                    #it's in the right side, move L
                    L = mid + 1
                else:
                    R = mid - 1

        return -1 
