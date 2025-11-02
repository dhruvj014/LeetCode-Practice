class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        q = collections.deque()
        for j in range(n):
            if board[0][j] == "O":
                board[0][j] = "N"
                q.append((0,j))
            if board[m-1][j] == "O":
                board[m-1][j] = "N"
                q.append((m-1,j))
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "N"
                q.append((i,0))
            if board[i][n-1] == "O":
                board[i][n-1] = "N"
                q.append((i,n-1))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = r+dr, c+dc
                if(0 <= row < m and 0 <= col < n and board[row][col]=="O"):
                    board[row][col] = "N"
                    q.append((row,col))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "N":
                    board[i][j] = "O"