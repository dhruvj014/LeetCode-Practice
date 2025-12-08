class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0,(rows*cols - 1)
        
        while l<=r:
            mid = (l + r) // 2
            mr = mid // cols
            mc = mid % cols
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False