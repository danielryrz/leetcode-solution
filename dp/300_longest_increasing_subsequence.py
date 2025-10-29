# Time: O(n^2) - not ideal, binary search solution, faster O(nlogn) will follow
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # create DP row with each value set to 1. 
        # as that's the starting length of the LIS (just this index in nums, value)
        LIS = [1] * len(nums)

        # iterate over the nums ints, starting from the second to last
        # moving by -1 to the very start. 
        # This is done to compare that int to the proceeding int found by j      
        for i in range(len(nums)-1,-1,-1): 
            # move j = i + 1, by 1, unitl the end, so we can compare: 
            # if the nums[i] < nums[j], and which of the LIS[j] have the highest value 
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    # LIS[i] either stays the same, 
                    # or is updated by the value of LIS at j with added 1 (1, becasue of just its own value)
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        

        return max(LIS)
        
