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

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found target
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Target lies in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                # Target lies in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target not found
        return -1
