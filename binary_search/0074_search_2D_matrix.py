class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time O(log(m*n) binary seaerch on a m*n array, Space O(1) 
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        
        l, r = 0, (m * n) - 1

        while l <= r:
            mid = l + (r-l)//2
            row = mid // n 
            col = mid % n  # no need to do -1, as modulo % operator does 0 - indexing

            if matrix[row][col] < target: #move l pointer to mid +1 and search right side
                l = mid + 1
            elif matrix[row][col] > target: #move r pointer to mid -1  and search left side
                r = mid - 1
            else: # matrix[r][c] == target
                return True
        
        return False
