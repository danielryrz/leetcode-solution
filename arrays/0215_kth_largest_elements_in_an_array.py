import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quickselect with Dutch National Flag partitioning.
        
        Converts the problem to finding the (n - k)-th smallest element.
        Uses 3-way partitioning to group values < pivot, = pivot, and > pivot.
        
        This version avoids recursion (iterative approach) and handles duplicates
        efficiently, preventing worst-case behavior that causes TLE in Python.
        """

        # Convert "k-th largest" to index in sorted ascending array.
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            # Random pivot to avoid worst-case input patterns.
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # 3-way partition (Dutch National Flag algorithm)
            lt, i, gt = left, left, right

            # Partition into three sections:
            # nums[left : lt]     -> values < pivot
            # nums[lt   : gt + 1] -> values == pivot
            # nums[gt+1 : right]  -> values > pivot
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            # Now check which section contains the target index.
            if target < lt:
                # Target is in the "less than pivot" section.
                right = lt - 1
            elif target > gt:
                # Target is in the "greater than pivot" section.
                left = gt + 1
            else:
                # Target index lies within the pivot-equal section.
                return nums[target]

