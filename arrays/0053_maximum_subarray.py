# LeetCode 53: Maximum Subarray
# Difficulty: Medium
# 
# 🧩 Problem Statement:
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum = 6
#
# ------------------------------------------------------------

from typing import List

def maxSubArray(nums: List[int]) -> int:
    """
    Kadane's Algorithm - O(n) time, O(1) space
    
    Approach:
    - Iterate through the array while keeping track of:
        1. currentSum: the maximum subarray sum ending at the current index.
        2. maxSum: the maximum subarray sum found so far.
    - At each step, decide whether to extend the previous subarray or start a new one.
    
    Formula:
        currentSum = max(num, currentSum + num)
        maxSum = max(maxSum, currentSum)
    """
    currentSum = maxSum = nums[0]

    for num in nums[1:]:
        currentSum = max(num, currentSum + num)  # Extend or start new subarray
        maxSum = max(maxSum, currentSum)          # Update global maximum
    
    return maxSum


# ------------------------------------------------------------
# ⏱️ Time Complexity: O(n)
#    We iterate through the array once.
#
# 💾 Space Complexity: O(1)
#    Only constant extra variables are used.
#
# ------------------------------------------------------------
# 🚀 Coming Soon:
# A more advanced O(n log n) Divide & Conquer approach that splits the array into halves
# and combines results from left, right, and crossing subarrays for an elegant recursive solution.
# ------------------------------------------------------------
