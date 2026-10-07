class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R: 

            mid = L + (R-L) // 2

            #min is in the right side, move L to mid + 1
            if nums[mid] > nums[R]:
                L = mid + 1
            #min is the left side or it is nums[mid], move R to mid 
            else:
                R = mid
        
        return nums[L] #it either starts on the left already or it finds it later in the while loop
      
