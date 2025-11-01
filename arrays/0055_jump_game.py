"""
LeetCode Problem 55: Jump Game
--------------------------------
Problem:
You are given an integer array nums. Each element nums[i] represents the maximum jump length at index i.
Return True if you can reach the last index, otherwise False.

Approach:
We use a greedy strategy:
- Track the farthest index we can reach at each step (`maxReach`).
- If at any point our current index exceeds `maxReach`, we are stuck → return False.
- If `maxReach` reaches or exceeds the last index, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def canJump(nums):
    maxReach = 0

    # we need to iterate until the last index to check if the last index is > maxReach
    for i in range(len(nums)):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
      
      #if maxReach already reach the last index of the array, break the loop, there is no need to continue looping through array's elements 
        if maxReach >= len(nums) - 1:
            return True
    return True


# Example usage:
if __name__ == "__main__":
    print(canJump([2,3,1,1,4]))  # True
    print(canJump([3,2,1,0,4]))  # False
