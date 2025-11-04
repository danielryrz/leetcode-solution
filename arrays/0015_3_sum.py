"""
LeetCode Problem #15 — 3Sum
------------------------------------

🧩 Problem Statement:
---------------------
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]`
such that:

    i != j, i != k, and j != k
    nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example:
---------
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]


🧠 Approach (Two-Pointer Technique):
------------------------------------
1. Sort the array. This helps to:
   - Simplify duplicate handling.
   - Use the two-pointer approach effectively.

2. Iterate through the array with index `i`, fixing `nums[i]` as the first number
   in the triplet.

3. Use two pointers:
   - `left` starts at `i + 1`
   - `right` starts at the end of the array

   Compute `total = nums[i] + nums[left] + nums[right]`

   - If `total < 0`, increment `left` (need a larger number)
   - If `total > 0`, decrement `right` (need a smaller number)
   - If `total == 0`, record the triplet and skip duplicates on both sides

4. Continue until all unique triplets are found.

⏱️ Time Complexity:
-------------------
O(n²) — The array is sorted in O(n log n), and for each element, we perform a two-pointer search in O(n).

💾 Space Complexity:
--------------------
O(1) — Apart from the output list, no extra space is used.

------------------------------------
"""

def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate 'i' elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicate left and right values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result


# Example usage:
if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
