class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r>=rows or r<0 or c>= cols or c<0:
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr,dc in dirs:
                dfs(r+dr,c+dc)
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    result += 1
                    dfs(r,c)
        return result