class DisjointSet:
	def __init__(self, n):
		self.rank = [0]*n
		self.parent = [i for i in range(n)]
		self.size = [1 for i in range(n)]
		
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
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow = 0
        maxCol = 0
        for i in range(len(stones)):
            maxRow = max(maxRow, stones[i][0])
            maxCol = max(maxCol, stones[i][1])
        ds = DisjointSet(maxRow + maxCol + 2)
        stoneNodes = [0]*len(stones)
        nodes = set()
        for coords in stones:
            nrow = coords[0]
            ncol = coords[1] + maxRow + 1
            ds.unionBySize(nrow,ncol)
            nodes.add(ds.findParent(nrow))
            nodes.add(ds.findParent(ncol))
        uniqueparents = set()
        for node in nodes:
            uniqueparents.add(ds.findParent(node))
        return len(stones) - len(uniqueparents)