class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, (i-index)*height)
                start = index
                
            
            stack.append([start, h])
        
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, (len(heights)-index) * height)

        return maxArea
        
