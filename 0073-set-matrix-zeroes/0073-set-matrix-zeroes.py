class Solution:
    def markRow(self, i, matrix):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=0:
                matrix[i][j] = -sys.maxsize -1
    
    def markCol(self, j, matrix):
        for i in range(len(matrix)):
            if matrix[i][j]!=0:
                matrix[i][j] = -sys.maxsize -1

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.markRow(i,matrix)
                    self.markCol(j,matrix)
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -sys.maxsize -1:
                    matrix[i][j] = 0