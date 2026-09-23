class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        L, R = 0, len(height) -1#two pointers
        maxL = height[L]
        maxR = height[R]

        while L < R:
            if height[L] <= height[R]:
                water = maxL - height[L]
                total_water += max(0,water)
                maxL = max(maxL, height[L])
                L += 1
            else:
                water = maxR - height[R]
                total_water += max(0,water)
                maxR = max(maxR, height[R])
                R -= 1
            
        return total_water


        
