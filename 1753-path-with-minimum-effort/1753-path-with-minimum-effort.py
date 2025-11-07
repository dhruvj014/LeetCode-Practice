import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        col = len(heights[0])
        dist = [[sys.maxsize for _ in range(col)] for _ in range(rows)]
        dist[0][0]=0
        q = [(0,0,0)]
        dr = [-1,0,1,0]
        dc = [0,-1,0,1]
        while q:
            dis,r,c = heapq.heappop(q)
            if r == rows -1 and c == col - 1:
                return dis
            for i in range(4):
                newr = r+dr[i]
                newc = c+dc[i]
                if 0<=newr<rows and 0<=newc<col:
                    new_d = max(abs(heights[newr][newc]-heights[r][c]),dis)
                    if new_d < dist[newr][newc]:
                        dist[newr][newc] = new_d
                        heapq.heappush(q,(new_d,newr,newc))
        return 0