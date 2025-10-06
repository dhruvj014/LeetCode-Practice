class Solution:
    def rowCheck(self,checker:str, board: List[List[str]],i:int,j:int) -> bool:
        for val in range(9):
            if board[i][val] == checker and val != j:
                return False
        return True
    
    def colCheck(self,checker:str, board: List[List[str]],i:int,j:int) -> bool:
        for val in range(9):
            if board[val][j] == checker and val != i:
                return False
        return True
    
    def boxCheck(self,checker:str, board: List[List[str]],i:int,j:int) -> bool:
        tracker = []
        boxi = (i // 3)*3
        boxj = (j // 3)*3
        for i in range(boxi,boxi+3):
            for j in range(boxj,boxj+3):
                key = board[i][j]
                if key in tracker:
                    return False
                if key != ".":
                    tracker.append(key)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                checker = board[i][j]
                if checker == ".":
                    continue
                if not self.rowCheck(checker,board,i,j):
                    return False
                if not self.colCheck(checker,board,i,j):
                    return False
                if not self.boxCheck(checker,board,i,j):
                    return False
        return True
