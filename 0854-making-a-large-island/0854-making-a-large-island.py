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
    def largestIsland(self, grid: List[List[int]]) -> int:
        def isValid(newr, newc, n):
            return 0<= newr<n and 0<= newc < n
        n = len(grid)
        ds = DisjointSet(n*n)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                dr = [-1,0,1,0]
                dc = [0,-1,0,1]
                for k in range(4):
                    newr = row+dr[k]                
                    newc = col+dc[k]
                    if isValid(newr,newc,n) and grid[newr][newc] == 1:
                        nodeNo = row*n + col
                        adjNodeNo = newr*n + newc
                        ds.unionBySize(nodeNo,adjNodeNo)
        maxlen = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                dr = [-1,0,1,0]
                dc = [0,-1,0,1]
                comp = set()
                for k in range(4):
                    newr = row+dr[k]                
                    newc = col+dc[k]
                    if isValid(newr,newc,n) and grid[newr][newc] == 1:
                        comp.add(ds.findParent(newr*n + newc))
                size = 0
                for parent in comp:
                    size += ds.size[parent]
                maxlen = max(maxlen, size+1)
        for cellnum in range(n*n):
            maxlen = max(maxlen, ds.size[ds.findParent(cellnum)])
        return maxlen