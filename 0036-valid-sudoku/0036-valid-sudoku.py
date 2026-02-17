class Solution:
    def validRow(self,row):
        track = [0]*9
        for i in row:
            if i.isnumeric():
                n = int(i)
                if track[n-1] == 0:
                    track[n-1] += 1
                else:
                    return False
        return True
    def validCol(self,board,j):
        track = [0]*9
        for row in board:
            if row[j].isnumeric():
                n = int(row[j])
                if track[n-1] == 0:
                    track[n-1] += 1
                else:
                    return False
        return True
    def validBox(self,board,i,j):
        row1 = (i//3)*3
        col1 = (j//3)*3
        track = [0]*9
        for row in range(row1,row1+3):
            for col in range(col1,col1+3):
                if board[row][col].isnumeric():
                    n = int(board[row][col])
                    if track[n-1] == 0:
                        track[n-1] += 1
                    else:
                        return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [-1]*9
        cols = [-1]*9
        box = [-1]*9
        for i in range(9):
            for j in range(9):
                if rows[i]==-1 and not self.validRow(board[i]):
                    return False
                rows[i] = 1
                if cols[j]==-1 and not self.validCol(board,j):
                    return False
                num = (i//3)*3 + (j//3)
                if box[num] == -1 and not self.validBox(board,i,j):
                    return False
                box[num] = 1
        return True