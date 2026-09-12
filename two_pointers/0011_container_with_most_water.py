class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        L, R = 0, len(height) - 1

        while L < R:
            h = min(height[L], height[R])
            area = h * (R-L)
            maxArea = max(area, maxArea)
            if height[L] < height[R]:
                L += 1 #height[L] is smaller, so L is limiting, move L to the right
            else:
                R -= 1 #height[R] is smaller, so R is limiting, move R to the left

        return maxArea
# Time O(n) (while loop going from L or R to the middle. Space O(1) : maxArea, L and R pointers, height  
