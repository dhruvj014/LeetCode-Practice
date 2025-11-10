class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0],0,0)]
        vis = [[0 for _ in range(n)] for _ in range(n)]
        dr = [-1,0,1,0]
        dc = [0,-1,0,1]
        vis[0][0] = 1
        while pq:
            elev, row, col = heapq.heappop(pq)
            if row == n-1 and col == n-1:
                return elev
            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]
                if 0 <= new_row < n and 0 <= new_col < n and vis[new_row][new_col]==0:
                    vis[new_row][new_col] = 1
                    heapq.heappush(pq,(max(elev, grid[new_row][new_col]),new_row,new_col))
        return elev