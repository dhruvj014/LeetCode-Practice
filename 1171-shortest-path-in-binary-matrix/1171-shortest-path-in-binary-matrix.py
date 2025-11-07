class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1 and grid[0][0] == 0:
            return 1
        q = collections.deque()
        dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        dist[0][0] = 1
        q.append((1,0,0))
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]
        while q:
            dis, r, c = q.popleft()
            for i in range(8):
                newr = r+dr[i]
                newc = c+dc[i]
                if 0<=newr<n and 0<=newc<n and grid[newr][newc] == 0 and dis+1 < dist[newr][newc]:
                    dist[newr][newc] = 1 + dis
                    if newr == n-1 and newc == n-1:
                        return dis+1
                    q.append((dis+1, newr, newc))
        return -1