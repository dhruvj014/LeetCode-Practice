class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def recur(row, col):
            if row==0 and col==0:
                return grid[0][0]
            if dp[row][col]:
                return dp[row][col]
            left = (recur(row,col-1) + grid[row][col]) if col-1>=0 else sys.maxsize
            up = recur(row-1,col) + grid[row][col] if row-1>=0 else sys.maxsize
            dp[row][col] = min(left,up)
            return dp[row][col]
        return recur(m-1,n-1)