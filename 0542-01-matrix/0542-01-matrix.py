class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        sol = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    sol[i][j] = 0
                    q.append((i,j))
        
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = r+dr, c+dc
                if(0 <= row < m and 0 <= col < n and sol[row][col]==-1):
                    sol[row][col] = sol[r][c] + 1
                    q.append((row,col))
        return sol