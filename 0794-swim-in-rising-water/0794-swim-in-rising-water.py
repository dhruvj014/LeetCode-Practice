class DisjointSet:
	def __init__(self, n):
		self.rank = [0]*(n+1)
		self.parent = [i for i in range(n+1)]
		self.size = [1 for i in range(n+1)]
		
	def findParent(self, node):
		if node == self.parent[node]:
			return node
		self.parent[node] = self.findParent(self.parent[node])
		return self.parent[node]
		
	def unionByRank(self, u,v):
		pu = self.findParent(u)
		pv = self.findParent(v)
		if pu == pv:
			return
		if self.rank[pu] < self.rank[pv]:
			self.parent[pu] = pv
		elif self.rank[pv]<self.rank[pu]:
			self.parent[pv] = pu
		else:
			self.parent[pv] = pu
			self.rank[pu]+=1
			
	def unionBySize(self,u,v):
		pu = self.findParent(u)
		pv = self.findParent(v)
		if pu == pv:
			return
		if self.size[pu] < self.size[pv]:
			self.parent[pu] = pv
			self.size[pv] += self.size[pu]
		else:
			self.parent[pv] = pu
			self.size[pu] += self.size[pv]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = [[0 for _ in range(n)] for _ in range(n)]
        ds = DisjointSet(n*n)
        pq = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(pq,(grid[i][j],i,j))
        dr = [-1,0,1,0]
        dc = [0,-1,0,1]

        while pq:
            ht, r, c = heapq.heappop(pq)
            vis[r][c] = 1
            index1 = r*n + c

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and vis[nr][nc]:
                    index2 = nr*n + nc
                    ds.unionBySize(index1, index2)
            
            if ds.findParent(0) == ds.findParent(n*n - 1):
                return ht