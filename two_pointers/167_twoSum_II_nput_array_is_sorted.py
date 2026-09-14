class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers

        L, R = 0, len(numbers) - 1

        while L < R:
            twoSum = numbers[L] + numbers[R]
            
            #too small
            if twoSum < target:
                L += 1 # move the left pointer by one to the right
            
            #too big
            elif twoSum > target:
                R -= 1 #move right pointer by one to the left
            
            #twoSum == target
            else:
                return [L+1, R+1]

        
