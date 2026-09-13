class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Time O(n log n)

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1 
            k = len(nums) - 1

            while j < k:
                threeSum = nums[i] + nums[k] + nums[j]

                if threeSum < 0: #too small
                    j += 1 #move left pointer one to the right (increase the sum as nums are sorted)
                
                elif threeSum > 0: # too large
                    k -= 1 #move right pointer one to the right (decrease the sum as nums are sorted)
                else: # it is 0 
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1 # or can be j += 1 equally fine. just move one pointer
                    
                    #skip duplicates
                    while nums[k] == nums[k+1] and j<k:
                        k -= 1
        return res
