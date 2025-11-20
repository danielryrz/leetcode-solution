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

# ============================================================
# 🧠 Solution 1: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================

def maxSubArrayKadane(nums: List[int]) -> int:
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
        maxSum = max(maxSum, currentSum)         # Update global maximum
    
    return maxSum


# ============================================================
# 🧩 Solution 2: Divide and Conquer
# Time Complexity: O(n log n)
# Space Complexity: O(log n)  (recursion stack)
# ============================================================

def maxSubArrayDivideAndConquer(nums: List[int]) -> int:
    """
    Divide and Conquer approach (O(n log n))
    
    Idea:
    - Divide the array into two halves.
    - Recursively find:
        1. The maximum subarray sum in the left half.
        2. The maximum subarray sum in the right half.
        3. The maximum subarray sum that crosses the midpoint.
    - The final answer is the maximum of these three.
    """

    def cross_sum(nums, left, mid, right):
        # Find max sum crossing mid from left
        left_sum = float('-inf')
        current = 0
        for i in range(mid, left - 1, -1):
            current += nums[i]
            left_sum = max(left_sum, current)
        
        # Find max sum crossing mid to right
        right_sum = float('-inf')
        current = 0
        for i in range(mid + 1, right + 1):
            current += nums[i]
            right_sum = max(right_sum, current)

        return left_sum + right_sum

    def helper(nums, left, right):
        # Base case: one element
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        left_max = helper(nums, left, mid)
        right_max = helper(nums, mid + 1, right)
        cross_max = cross_sum(nums, left, mid, right)

        return max(left_max, right_max, cross_max)

    return helper(nums, 0, len(nums) - 1)


# ============================================================
# Example Usage
# ============================================================

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Kadane’s Algorithm Result:", maxSubArrayKadane(nums))
    print("Divide and Conquer Result:", maxSubArrayDivideAndConquer(nums))
