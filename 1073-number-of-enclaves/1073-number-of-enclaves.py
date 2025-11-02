class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        q = collections.deque()
        ctr = 0
        for j in range(n):
            if board[0][j] == 1:
                board[0][j] = -1
                q.append((0,j))
            if board[m-1][j] == 1:
                board[m-1][j] = -1
                q.append((m-1,j))
        for i in range(m):
            if board[i][0] == 1:
                board[i][0] = -1
                q.append((i,0))
            if board[i][n-1] == 1:
                board[i][n-1] = -1
                q.append((i,n-1))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = r+dr, c+dc
                if(0 <= row < m and 0 <= col < n and board[row][col]==1):
                    board[row][col] = -1
                    q.append((row,col))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    ctr+=1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
        return ctr