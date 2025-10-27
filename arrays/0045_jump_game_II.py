"""
LeetCode Problem 45: Jump Game II
---------------------------------

Problem:
Given an array of non-negative integers nums, where each element represents
the maximum jump length from that position, return the minimum number of jumps
required to reach the last index.
"""

# ====================================================
# Version 1: Greedy (Minimum Jumps Only)
# ====================================================

def jump(nums):
    """
    Greedy solution for Jump Game II (minimum jumps count).
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    jumps = 0
    current_end = 0
    farthest = 0

    # we iterate through the nums until we reach the index that is second to last 
    # to ensure we can make a jump from there, to land on the last index
    for i in range(len(nums) - 1):
      
        # update the farthest index: either the current farthest, or the index we can reach from index i  
        farthest = max(farthest, i + nums[i])

        #if index is at current end, we need to make a jump
        if i == current_end:
            jumps += 1
            current_end = farthest # update current_end to the farthest reachable index

            #Once we found the farthest, updated jumps, and current_end, we can break early to save comp power
            if current_end >= len(nums) - 1:  
                break
    return jumps


# ====================================================
# Version 2: Greedy + Path Reconstruction
# ====================================================

def jump_with_path(nums):
    """
    Greedy solution with actual path reconstruction.
    Time Complexity: O(n)
    Space Complexity: O(n) (for storing path)
    Returns (min_jumps, path_taken)
    """
    jumps = 0
    current_end = 0
    farthest = 0
    lastIndex = len(nums) - 1
    path = [0]  # start at index 0
    best_index = 0

    for i in range(len(nums) - 1):
        if i + nums[i] > farthest:
            farthest = i + nums[i]
            best_index = i  # track which index gave the farthest reach

        if i == current_end:
            jumps += 1
            current_end = farthest
            path.append(best_index)
            if current_end >= lastIndex:
                path.append(lastIndex)
                break

    return jumps, path


# ====================================================
# Example Usage
# ====================================================
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print("Version 1 (jumps only):", jump(nums))           # Output: 2
    print("Version 2 (jumps + path):", jump_with_path(nums))  # Output: (2, [0, 1, 4])
