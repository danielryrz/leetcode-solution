# 11. Container With Most Water
# Category: Two Pointers / Arrays
#
# Problem Statement:
# You are given an integer array 'height' where each element represents 
# the height of a vertical line drawn at index i. You must find two lines 
# that, together with the x-axis, form a container that holds the most water.
# Return the maximum amount of water such a container can store.
#
# Time Complexity: O(n)
#   - Two pointers move inward at most n steps total.
#
# Space Complexity: O(1)
#   - Only constant extra variables are used.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_area = max(max_area, width * current_height)

            # Move the pointer with the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
