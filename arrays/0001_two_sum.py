"""
LeetCode Problem #1: Two Sum
--------------------------------
Given an array of integers `nums` and an integer `target`, 
return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Time Complexity:
    O(n) — We iterate through the list once, and each dictionary lookup is O(1) on average.

Space Complexity:
    O(n) — We use a dictionary to store up to `n` elements.

:type nums: List[int]
:type target: int
:rtype: List[int]
"""
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic:
                return [dic[diff], i]
            dic[num] = i
